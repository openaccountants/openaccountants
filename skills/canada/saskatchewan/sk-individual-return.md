---
name: sk-individual-return
description: Compute Saskatchewan provincial individual income tax for 2026, its three brackets and non-refundable credits, and route current benefits, GRP, farming, northern deductions, investment income and PST correctly. Complete federal T1 first. Distinguish current 2026 rates from the latest 2025 SK428/SK479 form layout and the July 2026-June 2027 benefit year.
version: "2.0"
jurisdiction: CA
tax_year: 2026
tax_year_notes: "2026 income and official provincial amounts; latest filed forms are the 2025-2026 filing cycle. SLITC benefit July 2026-June 2027 uses 2025 income."
last_updated: 2026-11-14
category: international
type: computation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Saskatchewan individual return: method v2.0

## Scope

Compute provincial tax in CAD for a Saskatchewan individual for **January 1-December 31, 2026**, after completing `ca-fed-t1-return`. CRA administers the provincial income tax through the same T1, not a separate Saskatchewan tax return. Provincial residence is ordinarily determined at December 31; emigrants, newcomers, death and multi-province business allocation have different tests. Resolve them before applying this resident method. [CRA Saskatchewan guide](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html).

Use the province's **2026 tax structure** for amounts below. The latest SK428/SK479 and worksheets are the **2025 return / 2026 filing cycle**, used here for the workflow and labelled historical amounts only. Do not copy their old bracket/BPA figures into a 2026 computation. PST is a separate consumption tax; its classification is routed to `sk-pst` rather than included as personal income tax. [2026 structure](https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure), [latest SK428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5008-c/5008-c-25e.pdf).

## Ask the client first

- Confirm the residence province on December 31, actual arrival/departure/death dates, any foreign ties, and all business permanent establishments; obtain the correct provincial package or T2203 allocation.
- Obtain the complete federal return and slips, taxable income at **26000**, net income at **23600**, spouse/dependant income, birth dates and support/custody facts. Withhold a final calculation when these are unknown rather than assume single status or zero dependants.
- Reconcile T4 pensionable/insurable wages, base CPP/QPP and EI credits, enhanced CPP deductions, CPP2, and other earnings. Do not credit the same contribution already deducted.
- Ask for pension eligibility, disability approval, care expenses, medical reimbursements/periods, donations and student-loan interest. Obtain prior Saskatchewan tuition carry-forwards; a current tuition receipt is not automatically a new provincial tuition credit.
- For graduate relief obtain graduation date, approved credential/programme, GRP certificate, lifetime eligible tuition, prior claims and Saskatchewan residence years. An eligible programme may be outside Saskatchewan.
- For refundable family benefits obtain actual eligible activity fees, child ages/disability, guardian/custody agreement, family adjusted income and 2025 return data for the current benefit year.
- For farm/resource income obtain accounts, grant letters, grain tickets/settlement dates, leases and slips. For northern deductions obtain prescribed-zone addresses, consecutive residence period, dwelling claimants, travel dates/costs/benefits and lowest-return-airfare evidence.

## The method, step by step

### 1. Establish the base and current rates

Use federal **line 26000 taxable income** after federal deductions. For 2026 ordinary provincial tax before credits is:

| 2026 taxable-income slice | Saskatchewan rate | Official source |
|---|---|---|
| First $54,532 | 10.5% | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Above $54,532 to $155,805 | 12.5%; second band is $101,273 wide | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure ; https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html |
| Above $155,805 | 14.5% | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure ; https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html |

Compute `min(income,54532)*0.105 + min(max(income-54532,0),101273)*0.125 + max(income-155805,0)*0.145`. Use continuous slices; do not leave a dollar untaxed by treating rounded whole-dollar bracket labels as the arithmetic boundaries.

#### Combined ordinary marginal rates, before credits and special items

These are **computed sums** of the official 2026 federal and provincial rates, not average/effective rates, dividend rates or a substitute for a complete return. Split income, AMT, deductions and benefit reductions can change a marginal result.

| Taxable-income slice, 2026 | Computed federal plus Saskatchewan rate | Official inputs |
|---|---|---|
| Up to $54,532 | 24.5% (derived) = 14% + 10.5% | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html ; https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Above $54,532 to $58,523 | 26.5% (derived) = 14% + 12.5% | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html ; https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Above $58,523 to $117,045 | 33% (derived) = 20.5% + 12.5% | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html ; https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Above $117,045 to $155,805 | 38.5% (derived) = 26% + 12.5% | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html ; https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Above $155,805 to $181,440 | 40.5% (derived) = 26% + 14.5% | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html ; https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Above $181,440 to $258,482 | 43.5% (derived) = 29% + 14.5% | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html ; https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Above $258,482 | 47.5% (derived) = 33% + 14.5% | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html ; https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |

### 2. Apply the correct non-refundable credits

A credit **amount** is not cash paid. Normally multiply eligible amounts by **10.5%** and limit ordinary non-refundable relief to the tax it can offset; donations have their own two rates. Enhanced CPP contributions are deductions, not a second base-credit amount. The province confirms CPP/EI and student-loan-interest credit amounts follow the federal amounts. [2026 structure and notes](https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure), [federal CPP tax recognition](https://www.canada.ca/en/department-finance/services/publications/federal-tax-expenditures/2026/part-7.html).

| Item | 2026 amount and condition | Official source |
|---|---|---|
| Basic personal amount, 58040 | $20,381 before any required newcomer/emigrant limitation | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Spouse/eligible dependant, 58120/58160 | Lesser of $20,381 and max(0, $22,419 minus that person's net income), with underlying eligibility | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Dependent child, 58210 | $8,358 for eligible child age 18 or under living with claimant at December 31; not also claimed as equivalent-to-spouse; lower-income spouse normally claims, unused may transfer | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Senior supplement, 58220 | $2,569 if 65 or over at December 31, even when age amount is zero; not the old stated income ceiling | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Age amount, 58080 | Maximum $5,901; net-income threshold $43,927; apply the applicable age worksheet, not an unreduced maximum | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Disability amount, 58440 | $14,266 with federal disability eligibility; under 18 supplement/expenses need the applicable worksheet | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Pension income, 58360 | Lesser of eligible federal pension amount and $1,000 | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Caregiver / infirm dependant | Maximum $14,266 each with qualifying facts; published net-income thresholds $33,756 caregiver / $22,363 infirm dependant, actual worksheet required | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Medical threshold | Lesser of 3% of net income and $2,735; allowable unreimbursed medical claim uses the relevant period/dependant allocation | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| CPP/EI and student-loan interest | Eligible federal credit amounts, not gross deductions or any private loan interest | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |
| Donations |10.5% of first $200 and 14.5% of excess eligible donations | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |

New provincial tuition/education credits were eliminated effective July 1, 2017. Valid **unused** amounts remain under **SK(S11)/58560**, with the existing carry/transfer rules, not a fresh credit on all current tuition. This is separate from the GRP. A final claim needs the actual carry-forward balance. [Province history](https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax), [CRA tuition instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html).

The 2026 programme page also reports doubled volunteer firefighter/search-and-rescue/emergency-first-responder credit amounts from $3,000 to $6,000. Apply the actual qualifying service/election rules and final worksheet before adding a claim; do not treat volunteer status as automatic entitlement. [2026 changes](https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax).

### 3. Complete SK428, not an invented SK(S12) tax schedule

1. Complete federal T1 steps 1-5 and reconcile income/deductions. On SK428 **Part A line 1** enter T1 **26000** and compute current-year provincial gross tax; use the published **2026** rate inputs above, not the old printed form constants.
2. Complete **Part B** with the province-specific amounts/limits. The latest form identifies **58040 BPA,58080 age,58120 spouse,58160 eligible dependant,58210 children,58220 senior supplement,58360 pension,58440 disability,58520 student-loan interest,58560 unused tuition,58689/58729 medical**. Transfer relevant spouse amounts with **SK(S2)** and tuition carry with **SK(S11)**.
3. Finish **Part C**: donations/dividend credit, any farm/small-business capital-gains credit **T1237**, split-income **T1206**, provincial AMT **T691**, foreign credit **T2036**, political or labour-sponsored/mineral-exploration credits, and GRP where applicable. A simple gross-tax-minus-BPA result is not sufficient when these facts exist.
4. **SK(S12)** is the latest home-renovation schedule, **not** the provincial tax calculation. SK428 is the tax calculation. Its current programme allows eligible renovation costs, subject to dwelling/receipt/period conditions; don't mistake it for taxable-income allocation.
5. Carry final SK428 tax to **T1 42800**. Prepare **SK479** refundable amounts separately to **47900**. The SLITC benefit is assessed/paid separately and is not an amount to subtract again from SK428. [CRA latest form workflow](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html), [latest SK428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5008-c/5008-c-25e.pdf).

### 4. Benefits, graduate relief and other provincial programmes

| Programme | Correct amount, period and route | Official source |
|---|---|---|
| SLITC | July 2026-June 2027: $460 individual +$460 spouse/eligible dependant +$181 per child, maximum 2 children/$1,282 family; reduction begins at AFNI $39,345; CRA assesses from 2025 return | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-saskatchewan.html |
| SLITC payment | Tax-free, combined with quarterly federal Canada Groceries and Essentials Benefit; not a second independent Saskatchewan sales-tax credit or a SK428 reduction | https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-saskatchewan.html |
| Active Families Benefit | Continuing 2025 and later maximum $300 child or $400 eligible disability, adjusted family income not over $120,000; actual eligible activity fees and one claimant per child, SK479 | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax ; https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html |
| Graduate Retention Program | Up to $24,000 for graduation on/after October 1, 2024; up to $20,000 before, programme-specific cap/tuition/certificate required | https://www.saskatchewan.ca/residents/education-and-learning/graduate-retention-program |
| GRP earning and use | 10% of eligible amount in first four years, 20% in final three; non-refundable and unused can carry for nine years after graduation under latest instructions | https://www.saskatchewan.ca/residents/education-and-learning/graduate-retention-program ; https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html |
| Home renovation | Continuing 2025 and later eligible expense ceiling $4,000, credit 10.5%, computed maximum $420; eligible seniors may claim additional $1,000 expenses for total $525 credit; SK(S12) | https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax ; https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html |

For AFB establish registration/payment for an eligible Saskatchewan provider's supervised sport/cultural/recreational programme, appropriate child age and adjusted-income calculation; exclude school curriculum/daycare activities and unsupported receipts. Shared-custody parents must agree on the claimant or meet the documented primary-care rules; don't split two full maximum claims. The latest 2025 form uses that year's child birth cutoff; apply the correct 2026 age criterion when the final form is published. [AFB instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html).

GRP eligibility is an approved programme equivalent to at least six months' full-time study yielding an eligible certificate/diploma/undergraduate degree/journeyperson qualification. An outside-Saskatchewan or eligible international institution can qualify; a master's/PhD is not itself eligible under the current programme. Obtain the provincial certificate through the Student Services/Advanced Education portal; attach the first claim's certificate and **RC360** as directed. Saskatchewan residence and filing are required for a claim year. Apply the certificate's graduation date, programme category and lifetime cap; unused amounts and missed years need the CRA adjustment/continuity calculation. The seven-year earning pattern does not mean an unconditional annual refund. [GRP programme](https://www.saskatchewan.ca/residents/education-and-learning/graduate-retention-program), [CRA GRP instructions](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html).

Do not transfer the GRP to a spouse/parent or call it an ordinary tuition credit. Keep earlier/later graduation cohorts and multi-credential limits separate. A certificate not obtained or a disputed eligible programme is a referral, not permission to use the maximum. The latest guide also names the refundable fertility-treatment credit; route a specific claim to its complete programme instructions rather than assume the old short list was exhaustive. [CRA provincial credits](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html).

### 5. Investment income and slips

Use the federal slip's actual income character, not one line for every T3/T5 receipt:

| Income source | Correct route | Official source |
|---|---|---|
| T4 employment | Federal 10100, payroll credits/deductions reconciled before 26000 | https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html ; https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html |
| Pension/T4A | Determine actual pension/annuity/other box and federal 11500/13000 or other line; pension eligibility is not established by a T4A label | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html |
| T5 investment income | Classify interest, Canadian eligible/other dividends and foreign income separately using federal slip instructions | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html |
| T3 trust allocations | Preserve capital gain/dividend/foreign/other-income character from each box; not universally 10400 | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html |
| T2125 business | Net 13500 for business; professional/commission and partnership categories have their own federal lines | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html |
| T776 rental | Net 12600, with capital/expense and co-owner allocation | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html |
| Capital gains | Schedule 3 to 12700 after current federal inclusion/exemption/loss rules | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html |
| Farm income | T2042/14100, with actual cash/accrual and restricted-loss treatment | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-31.html ; https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-76.html |

The current **ITA38(a)** general inclusion is **one-half**, not the withdrawn two-thirds/$250,000 split asserted by the old file. Exceptions such as qualifying donated securities and business losses require the federal capital-gains method. The 2026 QSBC/farm/fishing LCGE limit must come from `ca-capital-gains`; do not carry the old 2025 $1,250,000 unlabelled into a 2026 claim. [ITA38](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html).

For Canadian taxable dividends, the current federal ITA82 gross-up is 38% for eligible dividends and 15% for other-than-eligible dividends, subject to the actual designation and exceptions. Use the slip and federal method to calculate the taxable amount and federal credit. [ITA82(1)(b)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-82.html). The latest **2025** Saskatchewan worksheet gives **11% of taxable eligible dividends** and **2.519% of taxable other-than-eligible dividends**, not the old 2.105%; these are percentages of the **taxable**, grossed-up amount. The final 2026 dividend worksheet has not been confirmed here, so do not silently label the 2025 percentage table as a verified 2026 worksheet. Dividends from a CCPC are not automatically all non-eligible; designation and source matter. [Latest Worksheet SK428 line 61520](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5008-d/5008-d-25e.pdf).

### 6. Farm, resource and northern edge cases

**Farm losses.** Under ITA31, where farming is not the chief source, nor the required farming-plus-subordinate-other-income combination, the ordinary restricted-loss limit is the lesser of the actual relevant loss and **$2,500 + min(50% of the loss above $2,500, $15,000)**, maximum $17,500, with the statutory adjustments. Do not create a loss or apply a restriction without determining the chief-source and business facts. Full farming losses and manufacturing/processing exceptions need their actual tests. [ITA31](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-31.html).

Cash versus accrual, AgriStability/AgriInvest assistance and grant terms feed the federal farm accounts; don't call a Saskatchewan Farm and Ranch Water Infrastructure payment tax-free just because it is a grant. The old exemption assertion is unconfirmed. Grain settlement deferral under **ITA76(4)-(5)** is limited to the qualifying cash-purchase ticket/settlement for listed Canadian grain delivered to a qualifying elevator, with interest-free payment after year-end; the purchase price goes into the immediately following year. It is not a general option to defer all farm sales. [ITA76](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-76.html).

**Resource receipts.** Corporate resource surcharges are not a general extra personal tax. An individual's oil/potash/uranium royalties or partnership allocation must be classified from the actual lease, business activities and slip; don't assign every royalty to a single "other income" line or ignore deduction/foreign-credit implications. Refer disputed ownership, resource-tax or partnership cases. [CRA federal/provincial workflow](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html).

**Northern residents.** Use the official T2222 instructions and prescribed-location list, not an approximate 54 thparallel. The latest T2222 requires permanent residence in Zone A or B for at least **six consecutive months** (which may cross years). Zone A basic residency is **$11/day** and an additional **$11/day** only where the dwelling and sole-basic-claimant conditions are met; Zone B receives **half**, not an additional 50%. Multiple claimants in the same dwelling can lose the additional amount. Tax-free special-work-site benefits can reduce the claim. These continuing figures are read from the latest **2025** form; final 2026 form not assumed. [T2222 instructions](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2222/t2222-25e.pdf).

Travel deduction is limited by the applicable employment benefit or allocated **$1,200 standard amount**, actual eligible cost and lowest-return-airfare ceiling. There are generally at most **two non-medical trips per traveller**, counted across taxpayers, while qualifying medical trips are not limited to two. No double claim or deduction for non-taxable reimbursed travel. **$11 x 365=$4,015** describes the basic full-year Zone A amount alone, not every northern person's entitlement. [T2222 Steps 2-3](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2222/t2222-25e.pdf).

### 7. Saskatchewan Pension Plan and consumption-tax costs

SPP is a voluntary retirement-savings arrangement with deductions subject to the member's available **RRSP room**, and benefits/withdrawals taxable under its rules. It is not restricted to Saskatchewan residents simply by its name. The old $7,000 annual cap is obsolete: the official **2026 Department of Finance tax-expenditure report** says annual contribution and transfer limits were removed in April 2023, leaving RRSP limits. Establish the actual deduction limit and receipts, not an invented unlimited deduction. [Finance Canada, SPP section and ITA146(21)-(21.3) reference](https://www.canada.ca/en/department-finance/services/publications/federal-tax-expenditures/2026/part-7.html).

PST is **6%** on taxable Saskatchewan consumption/use, including qualifying imports, separate from federal **5% GST**, with no Saskatchewan HST. PST is not a federal GST input tax credit. Unrecoverable tax forms part of the relevant acquisition/expense cost: capital assets are capitalised and deducted only under applicable capital rules, not always immediately written off. Basic groceries, prescriptions and children's clothing remain classification/exemption topics for `sk-pst`; the old blanket "under 15" clothing condition is not confirmed and must not be used. Check the actual bulletin and exemption documentation before deciding a purchase is exempt. [Saskatchewan PST](https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins/provincial-sales-tax), [CRA rate table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html).

## Worked cases

### Case 1: preserve the $85,000 employment example with correct bases

My client is a single full-year Saskatchewan resident in 2026, under 65, with one pensionable/insurable employment of **$85,000**, no other income or deductions beyond mandatory enhanced CPP, and no other credits. Payroll evidence confirms base CPP **$3,519.45**, first additional CPP **$711**, CPP2 **$416** and EI **$1,123.07**. The enhanced $1,127 is deductible, so taxable income is **$83,873**, not $85,000. Provincial gross tax is $9,393.49; credits on BPA $20,381, base CPP and EI total $2,627.47, giving provincial tax **$6,766.02**. This is an annual tax computation, not payroll withholding. [2026 payroll inputs](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html), [provincial amounts](https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure).

For the same uncomplicated facts, federal gross tax on $83,873 is $13,389.97; using the current full BPA $16,452, employment amount $1,501, base CPP and EI credits at 14% gives federal tax $10,226.60. Combined income tax is **$16,992.62**, about 20.0% of gross employment income, before any tax already withheld/refund or separately paid benefits. It replaces the old unsupported $19,466 total. [2026 federal inputs](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html); special federal adjustments remain in `ca-fed-t1-return`.

```oa-check
name: Saskatchewan employee 85000 gross, current 2026 contributions and income tax
inputs:
  gross_income: 85000
  base_cpp: 3519.45
  first_additional_cpp: 711
  cpp2: 416
  ei: 1123.07
steps:
  - taxable_income: gross_income - first_additional_cpp - cpp2
  - sk_gross: round(min(taxable_income, 54532) * 0.105 + min(max(taxable_income - 54532, 0), 101273) * 0.125 + max(taxable_income - 155805, 0) * 0.145, 2)
  - sk_credits: round((20381 + base_cpp + ei) * 0.105, 2)
  - sk_tax: max(0, sk_gross - sk_credits)
  - federal_gross: round(58523 * 0.14 + (taxable_income - 58523) * 0.205, 2)
  - federal_credits: round((16452 + 1501 + base_cpp + ei) * 0.14, 2)
  - federal_tax: max(0, federal_gross - federal_credits)
  - combined_tax: sk_tax + federal_tax
expected:
  taxable_income: 83873
  sk_gross: 9393.49
  sk_credits: 2627.47
  sk_tax: 6766.02
  federal_gross: 13389.97
  federal_tax: 10226.60
  combined_tax: 16992.62
```

### Case 2: residence/credit and GRP boundaries

My senior client is 65 or over at December 31,2026 and the correctly completed age calculation gives zero, but the **$2,569 senior supplement remains available**, worth up to $269.75 at 10.5%, limited by tax. Do not impose the old $86,810 income ceiling on that separate supplement.

For a separate eligible four-year graduate on/after October 1, 2024 with a $24,000 certificate, a first-four-year instalment earns **$2,400**. If available Saskatchewan tax after other credits is $1,000 and no older carry exists, only $1,000 can be used now and $1,400 remains for the permitted carry-forward calculation; it is not a $2,400 refund. A pre-cutoff $20,000 certificate would generate $2,000 instead. These are separate taxpayers illustrating two different boundaries, not stacked claims. [Province senior note](https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure), [GRP schedule](https://www.saskatchewan.ca/residents/education-and-learning/graduate-retention-program ; https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html).

```oa-check
name: Independent senior supplement and new-cohort graduate non-refundable ceiling
inputs:
  senior_supplement: 2569
  graduate_certificate: 24000
  available_tax: 1000
steps:
  - senior_credit_value: round(senior_supplement * 0.105, 2)
  - annual_graduate_amount: graduate_certificate * 0.10
  - graduate_used: min(annual_graduate_amount, available_tax)
  - graduate_unused: annual_graduate_amount - graduate_used
  - old_cohort_annual_amount: 20000 * 0.10
expected:
  senior_credit_value: 269.75
  annual_graduate_amount: 2400
  graduate_used: 1000
  graduate_unused: 1400
  old_cohort_annual_amount: 2000
```

## When to refuse or refer

- Never apply Alberta or another province's rates to Saskatchewan, call GST plus PST an HST, ignore the three tax brackets, or treat withheld tax as the annual liability.
- Never infer province, marital status, dependant eligibility, disability or a GRP certificate. Outside-Saskatchewan institutions are not automatically excluded, but programme approval must be evidenced.
- Refer multiple provincial permanent establishments, non-residents/partial years, death/bankruptcy, split income/AMT, disputed foreign credits, trusts, complex dividend/capital-gain claims and partnership allocations to the applicable federal/provincial method.
- Farm chief-source restrictions, grant character, resource royalties, grain tickets and prescribed-zone travel need their documentary tests. No approximate latitude, blanket tax-free grant or automatically deductible capital PST.
- Final 2026 forms or programme values not confirmed below must not be guessed. Keep any estimate explicitly tied to complete assumptions, then reconcile the actual return and assessment before filing.

### Existing review requirement

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CGA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Filing and payment

The ordinary **2026 income-year** T1 deadline is **April 30, 2027**, with **June 15, 2027** for a qualifying self-employed person or spouse; balance owing remains April 30. Special death/non-resident/exceptional rules can alter the result. These annual dates are under **ITA150(1)(d)** and the **ITA248 balance-due-day** definition, not dates copied from a 2025 return calendar. File through certified NETFILE/EFILE software or the actual paper package; **My Account** provides account/notices and is not itself a general return-preparation product. [CRA filing dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/important-dates-individuals.html), [ITA150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html), [ITA248](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html).

Before transmission, reconcile 26000, SK428, SK479, carry-forwards and tax deducted; get client approval. Keep the accepted filing confirmation, a copy of return/schedules and supporting receipts. Check the assessment/benefit notices, separately record payments, and correct an actual error through the appropriate adjustment route rather than submit a duplicate original. Use federal filing, instalment and penalty methods in `ca-fed-t1-return` for amounts not restated here.

## Sources

- https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-82.html. Read for subsection 1(b) current 15%/38% gross-ups and designation scope, 2026-11-14.

| Official source | Read date | What was read |
|---|---|---|
| https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax/personal-income-tax-structure |2026-11-14| Read for all 2026 rate/credit rows and notes, spouse/child/senior/donation rules |
| https://www.saskatchewan.ca/residents/taxes-and-investments/personal-income-tax |2026-11-14| Read for 2026 changes and continuing Affordability Act programmes,2017 tuition abolition and 2025-onward benefit changes |
| https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/saskatchewan/5008-pc.html |2026-11-14| Read for latest 2025-2026 filing cycle SK428/SK479 workflow, tuition carry, GRP, AFB, new programme routes; deeper old URL served 2022 and was not used |
| https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5008-c/5008-c-25e.pdf |2026-11-14| Read for 2025 SK428 Parts A-C, actual fields and SK(S12)renovation route;2025 amounts not used as 2026 figures |
| https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5008-d/5008-d-25e.pdf |2026-11-14| Read for 2025 Worksheet SK428 dividend credit line 61520,11% and 2.519%; final 2026 worksheet not confirmed |
| https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032sk-jan/t4032sk-january-general-information.html |2026-11-14| Read for 2026 federal/SK rate charts, BPA/CEA, base/enhanced CPP, CPP2 and EI amounts used in worked case |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |2026-11-14| Read for 2026 federal rates/thresholds as combined marginal table inputs |
| https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/province-saskatchewan.html |2026-11-14| Read for July 2026-June 2027 SLITC amounts, family maximum, AFNI threshold and quarterly CGEB payment |
| https://www.saskatchewan.ca/residents/education-and-learning/graduate-retention-program |2026-11-14| Read for approved programmes/outside institutions, graduate cohorts, certificate application and 7 year earning pattern |
| https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-31.html |2026-11-14| Read for ITA31 chief-source/business loss restriction,2500 plus capped half-excess and exceptions |
| https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-38.html |2026-11-14| Read for ITA38 current one-half capital gain/loss inclusion and exceptions |
| https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-76.html |2026-11-14| Read for ITA76(4)-(5)qualifying grain settlement deferral and listed conditions |
| https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2222/t2222-25e.pdf |2026-11-14| Read for latest 2025 T2222 instructions,6 month qualification, Zone A/B basic/additional dwelling rules, medical/non-medical travel and ceilings |
| https://www.canada.ca/en/department-finance/services/publications/federal-tax-expenditures/2026/part-7.html |2026-11-14| Read for 2026 report's SPP section, RRSP room and April 2023 limit removal; enhanced CPP tax recognition section |
| https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins/provincial-sales-tax |2026-11-14| Read for 6% taxable goods/services/imports, registration and self-assessment overview; classification routed to sk-pst |
| https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html |2026-11-14| Read for Saskatchewan 5% GST/separate 6% PST rate table |
| https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html |2026-11-14| Read for paragraph 1(d)ordinary/self-employed annual filing dates |
| https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-248.html |2026-11-14| Read for balance-due-day definition(c)and death exception(b) |

Not yet confirmed: final 2026 SK428/SK479/worksheets and the 2026 provincial dividend-credit worksheet (verified latest 2025 rates 11%/2.519% kept labelled); 2027 SLITC indexed amounts from 2026 income; 2026 QSBC/farm/fishing LCGE limit requires the current ca-capital-gains method; under 18 disability supplement, age, caregiver and infirm-dependant worksheet details beyond the published 2026 summary need the final form; the former assertion of tax-free Farm and Ranch Water Infrastructure grants and the under 15 children's PST clothing rule are unsupported and not usable guidance. Individual resource/royalty classification, grant tax character, AFB 2026 age cutoff and specific PST exemptions need their actual documents/programme instructions. No author/reviewer name or approval has been added.
