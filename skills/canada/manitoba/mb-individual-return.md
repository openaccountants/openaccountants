---
name: mb-individual-return
description: >
  Compute Manitoba individual income tax for calendar 2026 from the federal T1
  workpaper. Covers provincial bands, the income-tested basic personal amount,
  family and other non-refundable credits, dividends, AMT and split-income
  handoffs, and separate refundable housing, caregiver and investment credits.
  Keeps actual 2025 annual forms in the 2025-2026 filing cycle separate from
  provisional 2026 estimates. Includes farmer and northern-resident questions
  and routes sales tax and employer payroll levies to their own methods.
version: "2.0"
jurisdiction: CA-MB
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: computation
---

# Manitoba individual return v2.0

## Scope

Use this method for a Manitoba individual's provincial T1 workpaper. The ordinary case is a Canadian resident whose province of residence at year-end is Manitoba. A non-resident with Manitoba-source income or a business with permanent establishments in several provinces needs the allocation route, not a blanket refusal or a time-apportioned resident calculation. Corporate returns, trusts and a complete federal AMT or split-income engine are outside this method. [Act ss.3-4](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) [CRA annual scope](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/manitoba/5007-pc.html)

| Quick reference | What to use |
|---|---|
| Place and currency | Manitoba, Canada; CAD |
| Current computation | Calendar 2026; Manitoba's legislated bands are frozen, not indexed in 2026 |
| Actual annual-form edition read | 2025 MB428, Worksheet MB428, MB428-A, MB479, MB(S2), MB(S11) and MB428MJ within T2203, for the 2025-2026 filing cycle |
| Administrator | CRA administers the provincial return; Manitoba legislation controls provincial eligibility and amounts |
| Return route | Federal T1 plus MB428 and applicable schedules; MB479 is separate refundable credits |
| Other jobs | `mb-rst` for retail sales tax; `canada-payroll` for employment deductions; `ca-fed-cpp-ei` for CPP/EI; `ca-capital-gains` for capital-gain classification and exemptions |

Current law and 2026 withholding forms support the 2026 estimates below. A 2026 TD1MB is a payroll declaration, not a published 2026 annual MB428. Never relabel a 2025 annual field as a final 2026 field. The current CRA general rates page prints different Manitoba thresholds; apply the Act's frozen bands, not that conflicting table. [Act ss.4.1,4.6](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) [conflicting CRA general table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html) [2026 TD1MB](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1mb/td1mb-26e.pdf)

## Ask the client first

1. Which tax year, country/province of residence and arrival/departure dates apply? Obtain business permanent-establishment locations, allocation workpapers, and any deceased, bankrupt or separate-return status.
2. What are final federal taxable income, net income, deductions, CPP/EI credit bases, dividend designations and slips? Obtain T691, T1206, T2036 and carryover records where relevant.
3. What are the actual marital status, spouse/dependant incomes, ages, support, shared-home and disability facts? Unknown family status is unresolved, not a default to single with no dependants.
4. Which tuition, education months, medical expenses, donations, pension, fitness/arts, student-loan interest and prior unused amounts are documented? Obtain the other claimant's use and transfer designation.
5. For housing, what principal residence, owner/renter dates, eligible rent, school taxes and advance credit, family income and senior status apply? Obtain property statements and rent receipts rather than assuming no entitlement.
6. Which caregiver registration/care dates, fertility invoices, approved investment receipts, farming programme slips or northern residency/address records support additional claims?

## The method, step by step

### Rates, bands and thresholds

These are provincial amounts. A credit base is not cash tax relief unless multiplied by the applicable credit rate and subject to the stated limit.

| Item | 2026 amount, conditions and computation | Official source |
|---|---|---|
| First ordinary band | First CAD47,000 of taxable income at 10.8% | [Act s.4.1(2)-(3)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Second ordinary band | Excess over CAD47,000 up to CAD100,000 at computed12.75%=10.8%+1.95%; the Act expresses this as base rate plus an additional rate | [Act s.4.1(2)-(3)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Third ordinary band | Excess over CAD100,000 at 17.4% | [Act s.4.1(2)-(3)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Basic personal amount | CAD15,780, reduced by CAD15,780 times min(200000,max(0,net income minus 200000))/200000; nil at CAD400,000 net income. Use the Act's applicable income adjustments | [Act s.4.6(3),(3.0.1)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Ordinary credit rate | 10.8% for the qualifying ordinary credit bases; donations, dividends and direct credits have their own computations | [Act s.4.6(2)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Age credit base | Up to CAD3,728 for qualifying age65 or older, less 15% of adjusted net income over CAD27,749, not below zero | [Act s.4.6(4)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Spouse or eligible dependant base | Up to CAD9,134 less the qualifying person's net income, not below zero; relationship, support, household and overlapping-claim restrictions apply | [Act s.4.6(5)-(6),(20)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Infirm dependant base | Up to CAD3,605, reduced for dependant income over CAD5,115 and the same dependant's eligible-dependant claim; support and sharing rules apply | [Act s.4.6(7),(20)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Caregiver base | Up to CAD3,605, using CAD15,917 minus max(dependant income,CAD12,312), less the overlapping eligible-dependant base, not below zero; qualifying shared-home and relationship/age/infirmity tests apply | [Act s.4.6(8),(20)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Pension income base | Up to CAD1,000 of qualifying pension income, with residence and eligible-income conditions | [Act s.4.6(10)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Disability base | CAD6,180 plus an under18 supplement of up to CAD3,605 reduced by qualifying care expenses over CAD2,112; unused dependant transfers require their own calculation | [Act s.4.6(11)-(12)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Medical expense reduction | Lesser of CAD1,728 and 3% of the relevant net income; calculate eligible other-dependant amounts separately, using qualifying federal expense rules | [Act s.4.6(17)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Donation credit | 10.8% on the first CAD200 and 17.4% on the qualifying remainder; apply the federal qualifying donation base and limits | [Act s.4.6(18)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Fitness expense base | Up to CAD500 for a qualifying resident under25 at year-end; an additional CAD500 can apply for an eligible disabled participant with at least CAD100 qualifying expense. Programme, claimant and reimbursement restrictions remain | [Act s.4.6(10.2)-(10.6)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Children's arts expense base | Separate qualifying programme amount up to CAD500 for a child under16 at the start of the year, or under18 when disability conditions apply. Additional disabled-child base CAD500 requires at least CAD100 eligible base and the disability entitlement. Do not duplicate another claim for the same expense | [Act s.4.6(10.7)-(10.9)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Tuition and education bases | Eligible tuition plus CAD400 per qualifying full-time month or CAD120 per qualifying part-time month; disability-related full-time treatment, own-use and carryforward conditions apply | [Act s.4.6(13)-(15)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Current-year tuition transfer ceiling | CAD5,000 before the student's current-year own use; old carryforwards are not transferable and the student must make a valid designation | [Act s.4.6(14.1)-(16)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Family tax benefit base | CAD2,065 personal and qualifying spouse/eligible-dependant/age components; qualifying dependant components can be CAD2,752. Subtract 9% of the claimant's applicable net income, not family income; priority and anti-duplication rules apply | [Act s.4.6(16.1)-(16.2)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Dividend credits | 8% of eligible taxable dividends; 0.7835% of other taxable Canadian dividends. Use the payer's actual designation and taxable slip amount | [Act s.4.7](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Additional AMT and carryover | 50% of the statutory additional federal minimum-tax comparison; separate carryover is 50% of the allowable federal carryover, not another deduction for current AMT | [Act ss.4.5,4.9](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
| Provincial split-income tax | 17.4% applied through the statutory TOSI calculation; perform the final comparison, not an unconditional addition of a second full tax | [Act ss.4,4.4](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |

**Ordinary gross tax:** 0.108 times taxable income +0.0195 times max(taxable income minus47000,0) +0.0465 times max(taxable income minus100000,0). Equivalently, tax at the second band's floor is CAD5,076 and at the third band's floor CAD11,833.50, derived from the linked Act. Use continuous brackets, without a one-dollar gap at a threshold. [Act s.4.1](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php)

The nominal combined federal-plus-Manitoba ordinary rates for 2026 are computed, not separate provincial rates:24.8% through47000;26.75% to58523;33.25% to100000;37.9% to117045;43.4% to181440;46.4% to258482;50.4% above258482. These are sums of the two jurisdictions' ordinary marginal rates, not effective rates after credits, benefit reductions, AMT or TOSI. Manitoba's personal-amount withdrawal can add a derived0.85212 percentage point when net and taxable income move together in its withdrawal range; the federal personal amount can also change. For the actual2025 filing cycle the corresponding first two nominal rates are25.3% and27.25%, and federal boundaries differ. Never reuse the old158468/220000 breakpoints as a2026 federal table. [Act ss.4.1,4.6(3.0.1)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) [2026 federal table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html) [2025 federal table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html)

### Build the federal input and ordinary-credit workpaper

1. Reconcile the federal T1 first. Start Manitoba Part A from line26000, using taxable income after supported federal deductions. Keep line23600 net income distinct: the personal amount and family benefit do not simply use taxable income. Obtain slip designations rather than infer eligible/non-eligible dividends from public-company or CCPC status. Transaction classification remains in `ca-fed-t2125`, not a merchant-name default in this return method. [2025 MB428 PartsA-B](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-c/5007-c-25e.pdf) [federal dividend inclusion](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-82.html)
2. Build each ordinary credit base separately. For CPP/QPP and EI use the federal credit-base amounts on lines30800,31000,31200 and31217 where applicable, not total enhanced contributions already deducted federally. Pension eligibility, adoption expenses, student-loan interest and transfers also have their own federal links and provincial caps. The ordinary base includes the family tax benefit from MB428-A, so do not omit that benefit when solving tuition own use. [2025 MB428 PartB](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-c/5007-c-25e.pdf) [2025 MB428-A](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-a/5007-a-25e.pdf)
3. Apply spouse, dependant, infirm and caregiver restrictions before summing. A shared dependant claim cannot exceed the allowed combined maximum; the same dependant does not generate duplicate spouse/eligible-dependant or caregiver/infirm benefits. Part-year, non-resident, support-payment, deceased and bankruptcy rules can restrict eligibility or the amount. Healthy senior-parent caregiver eligibility requires the actual statutory relationship, age and shared-home facts, not an automatic disability assumption. [Act s.4.6(5)-(8),(20)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php)
4. For fitness and arts, establish programme eligibility, participant age, disability status, receipt and reimbursement. Fitness is not restricted to children under16. Arts is a separate programme with its own age test. Keep the ordinary and disability additions separate. Obtain medical eligibility, measurement period and dependant net income before using a medical base. [CRA lines58315-58326,58769](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/manitoba/5007-pc.html)
5. Complete tuition own use using MB(S11), using old carryforward before current-year amounts where the schedule requires. The taxable-income-minus-other-credits comparison changes in higher bands; the schedule's tax-equivalent method must be followed. Transfer only the permitted unused current-year amount, with designation. A spouse first uses their own age, pension, disability and tuition amounts; MB(S2) computes the remainder, not their entire gross entitlement. [2025 MB(S2)](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-s2/5007-s2-25e.pdf) [2025 MB(S11)](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-s11/5007-s11-25e.pdf)
6. Compute MB428-A with the claimant and priority rules. Dependent children, infirm dependants, spouse/eligible dependant, disability and senior components require actual eligibility and other-claimant checks. A higher-income spouse generally has priority for stated dependent-child components; the agreement/highest-income rule for competing eligible claimants also matters. Do not copy a birth-year cut-off from an older worksheet into2026. [Act s.4.6(16.1)-(16.2)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) [2025 MB428-A](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-a/5007-a-25e.pdf)
7. Multiply only the eligible ordinary base by10.8%. Add separately computed donation and dividend credits and any allowed carryover in the statutory order. A base, a non-refundable credit, a refundable credit and an income deduction are different things. [Act ss.4.6-4.9](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php)

### Compute the provincial-tax line in order

For the actual2025 MB428, Part C adds Part A gross tax and the T1206 provincial split-income amount, then subtracts Part B non-refundable credits, the dividend credit and the allowable minimum-tax carryover, with a zero floor. It then adds the provincial additional minimum tax. The2025 form uses **T691 Part7 line1 minus line2**, multiplied by50%; it does not use the final Part7 balance or the gross federal AMT number as an interchangeable input. Minimum-tax carryover instead starts with federal line40427 and is separately limited. [2025 MB428 PartC](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-c/5007-c-25e.pdf) [T691 Part7](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t691/t691-25e.pdf)

Continue through political, labour-sponsored, foreign, community-enterprise, small-business-venture-capital, employee-share and mineral-exploration credits in the actual form's sequence, applying each non-negative floor. For political contributions obtain the eligible provincial recipient and receipt; the statutory formula is75% of the first400,50% of the next350 and one-third of the qualifying balance, capped1000. The2025 printed worksheet's33.33% differs slightly from exact one-third at a boundary; do not silently certify those as identical. For a Manitoba resident, T2036 applies the per-country cap and unrelieved eligible non-business foreign tax. **No Manitoba provincial foreign tax credit when subject to federal minimum tax** under the stated Act rule; do not import another province's exception. [Act ss.4.11-4.12](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) [T2036 Manitoba restriction](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2036/t2036-25e.pdf) [2025 Worksheet MB428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-d/5007-d-25e.pdf)

Where T1206 applies, follow its provincial split-income adjustments, including the adjusted net/taxable-income substitutions for affected credits. Complete the final provincial comparison and use the required greater result; do not charge full TOSI plus full ordinary tax a second time. The actual2025 T1206 Part3 comparison points to MB428 line82. [T1206 Part3 Manitoba row and final comparison](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1206/t1206-25e.pdf)

For multiple jurisdictions use T2203: allocate the underlying computation and follow the Manitoba-resident-only dividend/carryover adjustments and subsequent credit sequence. It is not simply the ordinary resident result times a province-of-income percentage; certain adjustments use the percentage **not** allocated to Manitoba. Carry the final MB428MJ amount to T2203 Part5. These are2025 field references, not invented final2026 fields. [T2203 MB428MJ](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2203/t2203-25e.pdf)

### Refundable credits are a separate workpaper

| Item | Rule and conditions | Official source |
|---|---|---|
|2026 homeowner affordability credit | Lesser of eligible school taxes and CAD1,600 times eligible days divided by days in year; subtract the advance already received, not below zero. Principal-residence, residence, age, spouse and shared-period restrictions apply | [Act ss.5.4-5.5](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
|2026 renters credit | Lesser of qualifying rent and CAD625 times eligible months divided by12; actual month/primary-residence and no-double-claim tests apply | [Act s.5.6.1](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
|2026 senior renters maximum | Derived annual ceiling CAD982.14 minus min(CAD357.14,0.008929 times family net income), multiplied by eligible months/12 and capped by eligible rent. Apply the senior definition and eligibility conditions | [Act s.5.6.1](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
|2025 housing amounts for the actual annual-form cycle | Homeowner annual ceiling CAD1,500; ordinary renter CAD575; senior annual formula CAD903.57 minus min(CAD328.57,0.008214 times family income), with eligible-period/rent limits | [2025 MB479 housing sections](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-tc/5007-tc-25e.pdf) |
|Senior school tax rebate | Up to CAD235, limited by eligible school taxes after homeowner benefit and advance, reduced by1% of family income above CAD40,000; eligible-period, age and ownership conditions apply | [Act s.5.5.1](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
|Personal tax credit | Separate household calculation beginning with CAD195 personal, eligible partner/dependant and additional qualifying child/age/disability components, less1% of family income; claimant priority and assistance restrictions apply. It is not the caregiver credit | [Act s.5.7](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
|Primary caregiver | CAD1,400 for a qualifying unpaid caregiver with a creditable care period and required registration; not an automatic low-income personal credit | [Act s.5.11](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
|Fertility treatment | Lesser of CAD16,000 and40% of qualifying costs, with the statutory medical, provider, medicine and eligible donor/surrogacy conditions; no spouse double claim | [Act s.5.13](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) |
|Community enterprise development investment |45% of qualifying cost; eligible annual investment ceiling CAD60,000 and combined individual credit cap CAD27,000. Authorised issuer/receipt, investment timing, related rules and restrictions apply | [Act s.11.8](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) [Manitoba CED programme](https://www.gov.mb.ca/jec/busdev/financial/cedtc/index.html) |

The old Education Property Tax Credit description is not a current2026 computation. It was replaced in the2025 cycle by the homeowner/renter measures above. Retain the actual school-tax statement, household occupancy and any advance, then use the right year's MB479. A homeowner credit is not a deduction from general municipal property tax; a renter does not use a percentage of rent copied from the old programme. Eligible care-home rent excludes the portion claimed as medical expenses under the actual rule. Different household claimants cannot duplicate periods. [CRA MB479 housing instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/manitoba/5007-pc.html) [2025 MB479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-tc/5007-tc-25e.pdf)

2027 housing increases enacted in2026 do **not** change2026 claims. The2026 amending Act makes its later homeowner/renter amount changes effective1January2027, while specified family/tuition corrections have earlier deemed dates. Read commencement with the operative section, not the announcement alone. [2026 amendment ss.2-6,62](https://web2.gov.mb.ca/laws/statutes/2026/c04426.php?lang=en)

The printed2025 senior-rent worksheet has a monthly minimum47.91: twelve such rounded months produce574.92 rather than the advertised annual575 floor. Preserve the actual form's rounding and obtain the final2026 form before asserting a2026 field-by-field result. This is a specific source-edition difference, not permission to invent a benefit. [2025 MB479 page3](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-tc/5007-tc-25e.pdf)

For the personal tax credit, the Act includes eligible spouse/dependant, child, infirmity, age and disability components, with sharing, support, residency and assistance conditions. The common child component is26 and qualifying senior/disability components are113, alongside the195 base components and62 infirm-dependant component. Calculate family net income from both partners as required. The actual MB479 includes the social-assistance adjustment using T5007 information. An arbitrary income-under12500 test does not replace that computation. [Act s.5.7](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) [2025 MB479 personal credit](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-tc/5007-tc-25e.pdf)

For primary caregiving, verify the recipient's qualifying care level and private-home/residence conditions and the caregiver's unpaid status. The statutory creditable period begins after the required care period; collect exact dates rather than treating a loosely described ninety-day period as sufficient. Registration must be made by30April of the following year under the Act; a registration covers the applicable year and following two years, subject to continued conditions and renewal. Do not duplicate a paid-caregiver or another claimant's benefit. [Act s.5.11 definitions,(2)-(3)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) [caregiver administration](https://www.gov.mb.ca/finance/tao/caregiver.html)

For CED, match the authorised investment receipt and statutory acquisition timing, including the first60days of the following year and prior claims. T1256 separates current refundable qualifying investments from historical non-refundable credit and its unused balance; the old universal five-year carryforward is wrong, and the historical non-refundable carryforward is up to ten years. The minimum holding restriction is generally three years with specific statutory/regulatory exceptions; do not promise a safe early redemption without checking the exception. File the required receipt. [Act ss.11.8-11.11](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php) [2025 T1256](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1256/t1256-25e.pdf) [Reg231/2004 s.9](https://web2.gov.mb.ca/laws/regs/current/_pdf-regs.php?reg=231/2004)

Other applicable MB479 jobs, including paid-work-experience, eligible green-energy, book-publishing/printing, teaching-expense and certified rental-housing credits, require their own programme evidence and schedules. Historical odour-control claims are period-limited. Do not let this overview substitute an uncapped automatic business credit for those separate computations. [CRA MB479 additional-credit instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/manitoba/5007-pc.html)

## Boundary and exception table

| Situation | Action |
|---|---|
| Province or tax year unknown | Stop the provincial calculation and obtain it; never substitute another province or stale brackets |
| Marital, dependant or housing facts unknown | Complete supported tax components and identify the unresolved credit; do not default to single or silently exclude an entitlement |
| Move within Canada | Establish the correct year-end residence rule and business allocation before selecting the provincial return; do not prorate Manitoba solely by days lived there |
| Newcomer, emigrant, deceased or bankrupt | Apply the actual statutory restrictions and federal/provincial links; do not grant a full-year credit automatically |
| Federal AMT, TOSI or multi-province business | Use the specific T691/T1206/T2203 handoffs above and obtain the full underlying workpaper |
| Pension splitting | Reconcile the supported federal T1032 election and resulting federal taxable income before computing provincial tax; do not invent a second provincial split election |
| Capital gain, LCGE or dividend | Use `ca-capital-gains` and actual federal inclusion/exemption workpapers; obtain dividend designation. Do not copy the old fixed LCGE amount into every2026 gain or identify dividend class from company type alone |
| Self-employment | Use `ca-fed-t2125` and `ca-fed-cpp-ei` for net income, both contribution components, ceilings and optional self-employed EI. Do not use the old first-tier-only2025 CPP shortcut for2026 |
| RST on business purchases | Use `mb-rst` for taxability, exemptions, resale and liability. Recoverability, expense deduction and capital cost are distinct; tax on a capital asset is not automatically a current T1 expense |
| Employer health/education levy | It is an employer liability on qualifying remuneration, not an individual's T1 tax or a separate levy on sole-proprietor drawings. Use the current payroll programme, associated-group and part-year-establishment rules |
| Northern Manitoba home | Establish the exact prescribed zone and qualifying residency, not a city-name assumption, then compute the supported federal deduction before the provincial taxable-income input |
| Farming and programme payments | Reconcile the correct farming return, grain delivery/payment terms, AgriInvest fund and actual government slips. Do not invent a universal farming credit or treat every fund withdrawal as taxable |

**Sales tax and employer levy routing.** Manitoba does not combine GST and RST into HST. The existing RST task includes insurance, telecommunications, accommodation, electricity, groceries, drugs, children's clothing and residential-energy questions, but each needs its statutory scope and transaction date. Neither a category label nor a July2024 bulletin proves all2026 exemptions. The current retail-tax page and2026 budget identify changes; the complete item-specific RST computation belongs to `mb-rst`. Similarly, the old employer-levy table is obsolete. The current programme has an exemption, a notch band and a full-payroll rate above its upper boundary, with sharing and part-year rules; do not carry the old2million/2.5million table into a2026 employer estimate. [current RST programme](https://www.gov.mb.ca/finance/taxation/taxes/retail.html?locale=en-ca) [2026 budget changes](https://www.gov.mb.ca/finance/taxation/pubs/bulletins/2026budget.pdf) [current employer-levy table](https://www.gov.mb.ca/finance/taxation/taxes/payroll.html)

**Northern deductions.** The latest annual instructions read cover2025 in the2025-2026 filing cycle: qualifying prescribed-zone residence requires at least six consecutive months; the basic daily amount and the separate additional-dwelling amount are different. A second household basic claimant prevents the additional amount for that same dwelling/period. The2025 daily basic amounts are11 in ZoneA and5.50 in ZoneB; the additional amount can match the respective basic amount only with its conditions. Resolve Thompson, Churchill, ThePas and every other actual address through the official prescribed-zone list; no classification is inferred here. Obtain the actual2026 T2222 instructions before using these2025 form details for a final2026 return. [CRA residency eligibility and calculation](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25500-northern-residents-deductions.html)

**Farming.** The old “Farm and Small Business Tax Credit” name is not an established entitlement here. Farmland school-tax relief and MASC's separately administered Farmland School Tax Rebate require actual land/tax/owner evidence and the programme's application. The2026 MASC FAQ describes up to40% of eligible farmland school tax, capped2500 across related applicants, a31March2027 receipt/payment deadline and its residency/joint-owner rules; it excludes the residential/building portion. Do not double count relief already on a statement. The application PDF was not readable in the direct cache; obtain the correct application before preparing a claim. [2026 MASC FAQ](https://www.masc.mb.ca/wp-content/uploads/2026/10/faqs_fstr_2026.pdf)

Federal section76 is not a general permission to delay all grain income. The prescribed non-interest-bearing cash-purchase-ticket rule concerns the specified Canadian grains delivered to a primary/process elevator, with the stated price-payable-after-year-end condition, and moves the relevant amount to the immediately following year. Obtain delivery, ticket and payment terms; do not apply it to any sale described as deferred. [federal Act s.76(1)-(5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-76.html)

AgriInvest has separate funds: government contributions and interest in Fund2 are taxable when withdrawn; the producer's Fund1 deposits are not taxable when withdrawn, after the required withdrawal ordering. Reconcile actual annual slips and fund transactions. AgriStability remains a separate programme/slip-classification task; the old blanket “AgriStability/AgriInvest payments taxable” does not establish every deposit or withdrawal's treatment. [AgriInvest handbook sections2,6](https://agriculture.canada.ca/en/programs/agriinvest/resources/agriinvest-program-handbook-sustainable-canadian-agricultural-partnership)

## Worked cases

### Case1: 2026 personal-amount withdrawal

A full-year Manitoba resident has net income equal to taxable income of300000, no other eligible credit or special tax and no refundable claim. The ordinary gross tax is46633.50. The personal base is7890 and its tax value852.12, giving45781.38 provincial tax before any later documented adjustment. At400000 the personal base is nil. This estimate is not a federal/provincial combined return or a completed2026 annual form. [Act ss.4.1,4.6(3.0.1)](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php)

```oa-check
name: Manitoba 2026 personal amount withdrawal
inputs:
  taxable_income: 300000
  net_income: 300000
  personal_max: 15780
steps:
  - gross_tax: taxable_income * 0.108 + max(taxable_income - 47000, 0) * 0.0195 + max(taxable_income - 100000, 0) * 0.0465
  - personal_base: personal_max * (1 - min(200000, max(net_income - 200000, 0)) / 200000)
  - personal_credit: personal_base * 0.108
  - provincial_tax: max(0, gross_tax - personal_credit)
  - base_at_400000: personal_max * (1 - min(200000, max(400000 - 200000, 0)) / 200000)
expected:
  gross_tax: 46633.50
  personal_base: 7890
  personal_credit: 852.12
  provincial_tax: 45781.38
  base_at_400000: 0
```

### Case2: 2025 annual form, refundable credits stay separate

For the actual2025 filing cycle a qualifying full-year resident has net and taxable income40000, a qualifying supported spouse with no income, and two qualifying dependent children. Documented credit-base CPP/EI amounts are2000 and500, not assumed statutory contributions. MB428-A base is2065+2065+2times2752 minus9%times40000=6034. The ordinary credit base is15780+9134+2000+500+6034=33448; tax credit3612.38 after cent rounding. Gross tax4320 gives provincial tax707.62, with no donation/dividend/AMT/TOSI or later non-refundable adjustment.

The same household's documented personal-credit components are195+195+2times26 minus1%times40000=42. Eligible homeowner school tax2000 less the1500 advance leaves no further homeowner credit. Independently proven caregiver registration/creditable period gives1400; qualifying fertility costs5000 give2000; a qualifying2000 CED investment gives900. MB479 therefore totals4342. Report tax707.62 on the provincial-tax route and refundable credits4342 separately. Their difference is not the taxpayer's final federal T1 refund. [2025 MB428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-c/5007-c-25e.pdf) [2025 MB479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-tc/5007-tc-25e.pdf) [2025 MB428-A](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-a/5007-a-25e.pdf) [2025 T1256](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1256/t1256-25e.pdf)

```oa-check
name: Manitoba 2025 family tax and separate refundable credits
inputs:
  taxable_income: 40000
  net_income: 40000
  spouse_income: 0
  qualifying_children: 2
  cpp_credit_base: 2000
  ei_credit_base: 500
  eligible_school_tax: 2000
  homeowner_advance: 1500
  fertility_cost: 5000
  qualifying_investment: 2000
steps:
  - family_base: max(0, 2065 + 2065 + qualifying_children * 2752 - net_income * 0.09)
  - ordinary_base: 15780 + max(0, 9134 - spouse_income) + cpp_credit_base + ei_credit_base + family_base
  - ordinary_credit: round(ordinary_base * 0.108, 2)
  - provincial_tax: max(0, taxable_income * 0.108 - ordinary_credit)
  - personal_credit: max(0, 195 + 195 + qualifying_children * 26 - net_income * 0.01)
  - homeowner_credit: max(0, min(1500, eligible_school_tax) - homeowner_advance)
  - fertility_credit: min(16000, fertility_cost * 0.4)
  - ced_credit: min(27000, qualifying_investment * 0.45)
  - refundable_total: personal_credit + homeowner_credit + 1400 + fertility_credit + ced_credit
  - provincial_components_difference: provincial_tax - refundable_total
expected:
  family_base: 6034
  ordinary_base: 33448
  ordinary_credit: 3612.38
  provincial_tax: 707.62
  personal_credit: 42
  homeowner_credit: 0
  fertility_credit: 2000
  ced_credit: 900
  refundable_total: 4342
  provincial_components_difference: -3634.38
```

## When to refuse or refer

- Refuse a final provincial result when province/year, federal workpaper or material claimant facts are unresolved. State which supported components are complete and which input changes the remaining result.
- Refer the full federal AMT, TOSI, treaty/non-resident, estate, bankruptcy or multi-jurisdiction computation where its underlying workpaper is missing; continue the ordinary Manitoba calculation that is actually supported.
- Obtain a programme decision or specialist workpaper for disputed disability/support, shared claims, complex fertility/surrogacy, investment redemption, farming timing or Indigenous-exemption facts. Do not treat a mailing address, family label or platform name as a legal conclusion.
- Never substitute another province's rates, label GST plus RST as HST, claim a housing credit without residence/expense evidence, ignore a band, or confuse the employer levy with individual T1 tax. Present an estimate with its year and missing inputs until the final return is reconciled.

## Filing and payment

For calendar2026, the ordinary filing/payment date is30April2027; the qualifying self-employed filing extension is15June2027 and does not extend payment. Check the actual taxpayer's applicable exception, death/bankruptcy status and official extension before assigning a date. The2025 filing-cycle dates are30April2026 and the qualifying self-employed15June2026. The federal filing rule and the CRA's actual deadline factsheet, not a heading containing a year, control. [federal Act s.150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html) [CRA filing/payment calendar](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html)

Prepare the federal T1 workpaper in the correct year's CRA-certified NETFILE software, or through an authorised EFILE preparer; MyAccount gives account access and notices and is not interchangeable with a certified return-preparation application. Use paper forms where required. Complete MB428 PartA, PartB with applicable MB428-A/MB(S2)/MB(S11), then PartC and special T691/T1206/T2036/T2203 calculations. Complete MB479 separately and carry its final amount to the refundable-credit route, not as a negative MB428 balance. For the actual2025 form, MB428 goes to T1 line42800 and MB479 to line47900. [CRA annual-form instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/manitoba/5007-pc.html) [2025 MB428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-c/5007-c-25e.pdf) [2025 MB479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-tc/5007-tc-25e.pdf)

Review taxpayer identity, authorisation and return summary before any transmission. Retain the actual submission acknowledgement or EFILE acceptance, not merely an exported file; check the notice of assessment and reconcile changes. A payment arrangement/reference or prepared posting is not proof of settlement. Use the CRA payment route for the correct taxpayer, tax and year and retain bank/CRA reconciliation. This method has not submitted a return, payment or account registration.

Late filing, payment interest and instalments have separate federal/provincial provisions; use `ca-fed-instalments` and the applicable current notice/rule rather than invent a single Manitoba penalty. [federal Act s.162](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html) [Act administration provisions](https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php)

## Completion checklist

- Correct residence/year, business allocation and special-return status established; no assumed single/no-dependant default.
- Federal net income and taxable income reconciled separately, with current-year CPP/EI and gains workpapers linked.
- Frozen Manitoba bands used, personal-amount withdrawal applied, and nominal combined rates not represented as effective tax.
- Every ordinary credit has claimant eligibility, receipt, own-use/transfer and overlap checks; MB428-A is included before tuition own use.
- Dividends follow actual designations; donations, AMT/carryover, foreign credits and TOSI use their separate computations and final ordering.
- Housing period, rent/school tax, advance, senior status and other claimants established; no superseded EPTC formula applied.
- Caregiver dates/registration, fertility scope and authorised investment records independently established where claimed.
- RST, employer levy, northern addresses and farm programme questions routed or explicitly unresolved.
- MB428 provincial tax and MB479 refundable totals kept separate; actual2025 fields not represented as final2026 fields.
- Accepted return, assessment and actual payment evidence retained where filing is performed by the authorised human.

## Sources

| Source and what was read | Official URL | Read on |
|---|---|---|
| Read for the following bounded scope: Current Manitoba Income Tax Act. Read ss.3-4.12,5,5.1,5.4-5.7,5.11,5.13,11.8 and the specified investment restrictions for residence, ordinary and special taxes, credit bases and refundable eligibility; not a whole-Act audit. | https://web2.gov.mb.ca/laws/statutes/ccsm/i010.php |2026-11-14|
| Read for the following bounded scope: Official bilingual Act PDF. Read the header and printed ordinary-band/personal-amount provisions as a countercheck to the HTML; no whole-document read claimed. | https://web2.gov.mb.ca/laws/statutes/ccsm/_pdf.php?cap=i10 |2026-11-14|
| Read for the following bounded scope: CRA Manitoba2025 information. Read the annual scope, PartsA-C, credit eligibility, transfers and all MB479 sections for the2025-2026 filing cycle. | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/manitoba/5007-pc.html |2026-11-14|
| Read for the following bounded scope: Manitoba2026 budget bulletin. Read all three pages for2026 housing, later2027 measures and dated RST changes; announcement and operative law distinguished. | https://www.gov.mb.ca/finance/taxation/pubs/bulletins/2026budget.pdf |2026-11-14|
| Read for the following bounded scope: CRA current-year rates. Read federal2026 bands and the conflicting Manitoba table; Manitoba figures are rejected in favour of Act s.4.1. | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |2026-11-14|
| Read for the following bounded scope: CRA previous-year rates. Read federal2025 bands/rates for the expressly dated comparison only. | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html |2026-11-14|
| Read for the following bounded scope: Actual2025 T1206. Read ChartC Manitoba and Part3 including adjusted-income substitutions and the final comparison; not a complete federal TOSI engine. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1206/t1206-25e.pdf |2026-11-14|
| Read for the following bounded scope: Actual2025 T2036. Read calculation and notes including the Manitoba federal-minimum-tax prohibition and separate-country limit. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2036/t2036-25e.pdf |2026-11-14|
| Read for the following bounded scope: Actual2025 T2203. Read MB428MJ, resident-only credit adjustments, income allocation and final sequence; not every other province schedule. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2203/t2203-25e.pdf |2026-11-14|
| Read for the following bounded scope: Actual2025 T691. Read Part7 line1-minus-line2 comparison for the Manitoba handoff; not a complete federal AMT engine. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t691/t691-25e.pdf |2026-11-14|
| Read for the following bounded scope: Federal Act s.150. Read the ordinary and qualifying self-employed filing provisions; special cases still depend on actual facts. | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html |2026-11-14|
| Read for the following bounded scope: Federal Act s.162. Read ordinary/repeated late-filing provisions as a routing reference, without inventing a single provincial interest rate. | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html |2026-11-14|
| Read for the following bounded scope: Federal Act s.82. Read taxable-dividend inclusion and eligible/non-eligible distinction; apply actual slips/designations. | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-82.html |2026-11-14|
| Read for the following bounded scope: CRA small-business deadline factsheet. Read the actual dates for the2026 return filed in2027 and the distinction between filing and payment. | https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html |2026-11-14|
| Read for the following bounded scope: Actual2025 MB428. Read all three pages for taxable-income input, ordinary-credit bases, PartC sequence and T1 provincial-tax handoff; page3 visually checked. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-c/5007-c-25e.pdf |2026-11-14|
| Read for the following bounded scope: Actual2025 Worksheet MB428. Read all four pages for personal amount, dependant/caregiver/disability, medical, dividend and political calculations. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-d/5007-d-25e.pdf |2026-11-14|
| Read for the following bounded scope: Actual2025 MB479. Read all five pages for personal credit, housing, senior rent, caregiver, fertility and other credits; page3 rent layout visually checked. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-tc/5007-tc-25e.pdf |2026-11-14|
| Read for the following bounded scope: Actual2025 MB428-A. Read the whole form for claimant components, income reduction and the base carried to MB428; visually checked. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-a/5007-a-25e.pdf |2026-11-14|
| Read for the following bounded scope: Actual2025 MB(S2). Read the whole form for spouse own use, unused eligible amounts and transfer limitation. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-s2/5007-s2-25e.pdf |2026-11-14|
| Read for the following bounded scope: Actual2025 MB(S11). Read both pages for prior/current tuition use, education months, high-band comparison, transfer and carryforward. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5007-s11/5007-s11-25e.pdf |2026-11-14|
| Read for the following bounded scope: Current Manitoba employer-levy programme. Read the exemption/notch/full-payroll table, associated-group sharing and part-year-establishment note; detailed employer computation routed separately. | https://www.gov.mb.ca/finance/taxation/taxes/payroll.html |2026-11-14|
| Read for the following bounded scope: 2026 TD1MB. Read both pages for current personal bases and payroll-declaration limits; this is not a2026 annual tax-return form. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1mb/td1mb-26e.pdf |2026-11-14|
| Read for the following bounded scope: Primary caregiver programme. Read care, unpaid caregiver and registration/renewal administration alongside Act s.5.11. | https://www.gov.mb.ca/finance/tao/caregiver.html |2026-11-14|
| Read for the following bounded scope: Community enterprise development programme. Read eligible investment, annual ceiling, authorised issuer and approval/receipt requirements. | https://www.gov.mb.ca/jec/busdev/financial/cedtc/index.html |2026-11-14|
| Read for the following bounded scope: Actual2025 T1256. Read the full form for current refundable versus historical non-refundable amounts, annual cap and carryforward. | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t1256/t1256-25e.pdf |2026-11-14|
| Read for the following bounded scope: Community Enterprise Development Tax Credit Regulation231/2004. Read s.9 for the holding restriction and exceptions; not the whole regulation. | https://web2.gov.mb.ca/laws/regs/current/_pdf-regs.php?reg=231/2004 |2026-11-14|
| Read for the following bounded scope: Current Manitoba RST programme. Read the retail/rental scope, separate GST base and general-rate statement; item-specific exemptions are not certified here. | https://www.gov.mb.ca/finance/taxation/taxes/retail.html?locale=en-ca |2026-11-14|
| Read for the following bounded scope: MASC2026 Farmland School Tax Rebate FAQ. Read both pages in the official web PDF for eligible land, maximum/refund, related applicants, payment/application deadline and ownership rules; direct cache download failed. | https://www.masc.mb.ca/wp-content/uploads/2026/10/faqs_fstr_2026.pdf |2026-11-14|
| Read for the following bounded scope: CRA northern residents deductions. Read the prescribed-zone residency eligibility, household additional-amount conditions and explicitly2025 daily figures; client address/2026 form remain open. | https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-25500-northern-residents-deductions.html |2026-11-14|
| Read for the following bounded scope: Federal Act s.76. Read subsections1-5 for debt securities and the prescribed cash-purchase-ticket rule and grain definition; not all farming income law. | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-76.html |2026-11-14|
| Read for the following bounded scope: AgriInvest handbook. Read sections2 and6 for Fund1/Fund2 composition, withdrawal ordering and tax treatment; not a full AgriStability audit. | https://agriculture.canada.ca/en/programs/agriinvest/resources/agriinvest-program-handbook-sustainable-canadian-agricultural-partnership |2026-11-14|
| Read for the following bounded scope: Assented2026 Manitoba amendment c.44. Read ss.2-6 and62 for the specified deemed dates and2027 housing commencements, not the whole amending Act. | https://web2.gov.mb.ca/laws/statutes/2026/c04426.php?lang=en |2026-11-14|

Not yet confirmed: final2026 MB428, MB428-A, MB479, MB(S2), MB(S11), T1206/T691/T2036/T2203 annual fields and rounding; the exact political-credit statute-versus-printed-worksheet rounding instruction and2025 senior-rent monthly rounding difference; full current2026 item-specific RST exemptions, provider/insurance/cloud and residential-energy treatment through mb-rst; the exact prescribed zone for the client's Thompson/Churchill/ThePas or other northern address and final2026 T2222 instructions; the current MASC application attachment, notwithstanding its separately readable2026 FAQ; actual claimant-dependent optional credits and special-case election/redemption conditions; complete AgriStability slip/classification law for a particular payment. The conflicting CRA generic Manitoba brackets are not used because the current Act controls. No professional approval is inferred from this source rewrite.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CGA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
