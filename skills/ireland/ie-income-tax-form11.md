---
name: ie-income-tax-form11
description: "Irish income tax self-assessment on Form 11 for tax year 2026 (and the 2025 return filed in 2026). Covers who is a chargeable person (self-employed, proprietary directors over 15%, non-PAYE income over EUR 5,000 net or EUR 30,000 gross), the 20% and 40% bands (EUR 44,000 single, EUR 53,000 married) and the main credits including the EUR 2,000 Earned Income Credit, Case I and II trading profit, add-backs, capital allowances at 12.5% over 8 years and the car CO2 limits, losses, pension relief, Case V rental income, where USC and PRSI Class S fit, pay and file on 31 October (18 November 2026 on ROS), preliminary tax, the 5% and 10% surcharges and 0.0219% daily interest. Trigger on: Form 11, self-assessment Ireland, sole trader tax Ireland, Case I, ROS pay and file, earned income credit, proprietary director return. Out of scope: ie-payroll, ie-usc, ie-prsi-class-s, ie-preliminary-tax, ie-paye-rental-nonresident, ie-cgt, ie-corporation-tax, ie-cross-border."
version: 2.3
jurisdiction: IE
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Ireland Form 11 (2026): self-assessment for self-employed and other chargeable persons

Authority: the Revenue Commissioners. Currency: euro. This Guide separates the 2025 return filed in 2026 from the 2026 computation. Section numbers are TCA 1997 unless stated otherwise. Use the enacted amendments and their commencement dates where a summary table differs.

The **2025 Form 11** deadline was 31 October 2026, extended to 18 November 2026 only where the ROS filing and payment conditions were met. Both dates have passed as at 27 November 2026. The **2026 Form 11** is due by 31 October 2027. Bands and the listed credit maxima are unchanged between those years; USC and Class S rates differ. Confirm tax year, residence, assessment status, age, medical-card status, income sources, assets, pension payments, prior liabilities and payments before computing.

See also: `ie-payroll` (PAYE under the RPN, Class A PRSI), `ie-usc` (USC in depth), `ie-prsi-class-s` (Class S in depth), `ie-preliminary-tax` (preliminary tax in depth), `ie-paye-rental-nonresident` (Form 12, Case V rental income in depth, non-residents), `ie-cgt` (the CGT panel), `ie-corporation-tax` (companies), `ie-formation` (registering), `ie-vat-return` (VAT), `ie-cross-border` and `ie-foreign-tax-and-withholding` (residence, treaties).

## Who this applies to

- **A chargeable person files Form 11** (s.959A, s.959I). You are a chargeable person if any of these apply for the year ([Revenue, Guide to Completing 2025 Returns, "Who is this guide for?"](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)):
  - you have trading income from a business, trade, profession or vocation (Case I or Case II);
  - you are a **proprietary director**: you own, or can control directly or indirectly, more than 15% of the company's ordinary share capital;
  - you have PAYE income and non-PAYE income over EUR 5,000 net (after capital allowances, expenses and losses carried forward), or over EUR 30,000 gross (before capital allowances and losses);
  - your taxable income is only rental, foreign or other non-PAYE income;
  - foreign-account reporting can create a separate obligation: do not decide the s.895 reporting exemption from this Guide. Check this point with one of our partner accountants.
- **The EUR 5,000 and EUR 30,000 tests.** Section 959B takes out of self-assessment a PAYE worker whose net non-PAYE income does not exceed EUR 5,000 (and gross does not exceed EUR 30,000), where it is coded against their credits or fully taxed at source. This exclusion does not apply to company directors or their jointly assessed spouses, unless the company is dormant ([Revenue, Notes for Guidance Part 41A, s.959B](https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part41a.pdf)). For the PAYE side-income threshold, non-PAYE income excludes social welfare payments/pensions and legally enforceable maintenance payments. Below the limits, use Form 12 in myAccount only if the non-PAYE income is coded or fully taxed at source and the director exclusion does not apply; nil profits after relief do not automatically remove an existing self-assessment obligation ([Revenue, who should register](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)).
- **Out:** companies (they file CT1, see `ie-corporation-tax`; a proprietary director still files their own Form 11); the partnership itself (the precedent partner files Form 1 (Firms), s.959M; each partner then puts their share on their own Form 11); a PAYE-only employee (Form 12, see `ie-paye-rental-nonresident`).
- **Residence** decides what is taxed: see `ie-cross-border`. Non-resident filing and credit entitlement require a separate scope check; do not apply the PAYE side-income limits to every non-resident. Check this point with one of our partner accountants.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate band, single or widowed, no qualifying children (s.15, Table Part 1) | first EUR 44,000 at 20%, balance at 40% | 2025 and 2026 | https://www.irishstatutebook.ie/eli/2024/act/43/section/3/enacted/en/html |
| Band, single person qualifying for the Single Person Child Carer Credit (s.15, Part 2) | first EUR 48,000 at 20%, balance at 40% | 2025 and 2026 | same |
| Band, married or civil partners (s.15, Part 3) | first EUR 53,000 at 20%, balance at 40% | 2025 and 2026 | same |
| Increase for a second income (s.15(3)(i)) | lower of EUR 35,000 or the lower earner's income; not transferable | 2025 and 2026 | same |
| Single Person Tax Credit / Married or Civil Partner Tax Credit (s.461) | EUR 2,000 / EUR 4,000 | 2025 and 2026 | same |
| Single Person Child Carer Credit (s.462B) | EUR 1,900 | 2025 and 2026 | same |
| Home Carer Tax Credit, maximum (s.466A) | EUR 1,950 | 2025 and 2026 | same |
| Employee (PAYE) Tax Credit (s.472) | EUR 2,000 | 2025 and 2026 | same |
| Earned Income Tax Credit (s.472AB) | lower of EUR 2,000 or 20% of qualifying earned income; with the Employee credit, the two together cannot exceed EUR 2,000 | 2025 and 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx |
| Age Tax Credit, single / married | EUR 245 / EUR 490 | 2025 and 2026 | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx |
| USC (detail in `ie-usc`) | 0.5% on first EUR 12,012; 2% on next EUR 16,688; 3% on next EUR 41,344; 8% on the balance; none if income is EUR 13,000 or less; 3% surcharge on non-PAYE income over EUR 100,000 | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html ; https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part18d.pdf |
| USC for the 2025 return | 0.5% on first EUR 12,012; 2% from EUR 12,012 to EUR 27,382; 3% to EUR 70,044; 8% on the balance | 2025 | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf |
| PRSI Class S on self-assessed income (detail in `ie-prsi-class-s`) | 4.2375% blended (4.2% to 30 September, 4.35% from 1 October), minimum EUR 650; nil if income under EUR 5,000 | 2026 | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf |
| PRSI Class S on 2025 income | 4.125% blended, minimum EUR 650 | 2025 | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf |
| Wear and tear on plant, machinery and cars bought on or after 4 December 2002 (s.284) | 12.5% a year over 8 years | 2026 | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf |
| Car qualifying expenditure, purchases in 2025 or 2026: CO2 0-140 g/km (A, B) / 141-155 (C) / over 155 (D, E, F) | EUR 24,000 / 50% of EUR 24,000, or 50% of the retail price new if lower / nil | 2025 and 2026 | https://www.irishstatutebook.ie/eli/2008/act/3/section/31/enacted/en/html ; https://www.irishstatutebook.ie/eli/2019/act/45/section/19/enacted/en/html ; https://www.irishstatutebook.ie/eli/2020/act/26/enacted/en/pdf |
| Pension relief (RAC, PRSA), % of net relevant earnings by age | under 30: 15%; 30-39: 20%; 40-49: 25%; 50-54: 30%; 55-59: 35%; 60+: 40% | 2026 | https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx |
| Pension relief earnings limit | EUR 115,000 a year | 2026 | same |
| Pay and file date (s.959A specified return date; s.959AO) | 31 October after the tax year; preliminary tax for the current year on the same date | 2026 | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part41a.pdf |
| ROS extension for the 2025 return and 2026 preliminary tax, if both filed and paid on ROS | 18 November 2026 | 2026 | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx |
| Preliminary tax safe harbours (s.959AO) | lowest of 90% of current year, 100% of previous year, 105% of pre-preceding year (direct debit only, not if that year was nil) | 2026 | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx |
| Late filing surcharge (s.1084) | 5% of tax due, max EUR 12,695, within 2 months; 10%, max EUR 63,485, after 2 months | 2026 | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx |
| Interest on late income tax (s.1080) | 0.0219% a day or part of a day | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf |
| Revenue estimate for a missing return (s.959AX, from 1 January 2026) | greater of the average tax due on the last 2 returns or EUR 1,000 | 2026 | https://www.irishstatutebook.ie/eli/2025/act/18/section/32/enacted/en/html |

The car table uses the statutory emissions categories, not a current VRT rate band. Section 380L treats the qualifying cost as EUR 24,000 for category A or B, rather than a cap at actual purchase cost. Obtain the emissions certificate; do not infer emissions from the price or model. Finance Act 2024 s.33 tightens these groups only for expenditure from 1 January 2027; it does not govern a 2026 purchase. [FA 2024 s.33](https://www.irishstatutebook.ie/eli/2024/act/43/section/33/enacted/en/html).

Credit maxima are not automatic entitlements: the married band and credit assume the applicable joint assessment; the child-carer band requires entitlement to that credit; the Home Carer credit requires its own eligibility and income tests and cannot be combined with the two-income band increase. The Employee credit is the lower of EUR 2,000 and 20% of qualifying PAYE income, is non-transferable, and is not available on a proprietary director’s pay. Directorship-related spouse/civil-partner income and employment by a spouse, parent or related partnership have exclusions; a child’s statutory exception must be established before granting the credit. Check this point with one of our partner accountants. The Age credit requires age 65 or over during the year (one spouse/civil partner qualifying suffices under joint assessment). Confirm those conditions before using a row; unresolved child-carer or home-carer entitlement: Check this point with one of our partner accountants.

The pension table is the ordinary age scale, measured by age attained during the year. Specified occupations can qualify for a different percentage. The EUR 115,000 earnings limit is aggregate across pension products, with pensionable employment earnings counted first. Do not use rent as relevant earnings. Special occupations, multiple products or disputed contribution timing: Check this point with one of our partner accountants.

USC exemption uses USC aggregate income, excluding exempt sources, not every receipt. Above EUR 13,000 the whole chargeable amount is taxed. Reduced rates apply at age 70 or over, or for full medical-card eligibility, only where aggregate income does not exceed EUR 60,000: 0.5% on EUR 12,012 and 2% on the rest. Use `ie-usc` for exemptions, week-53 adjustments and property-relief surcharges. PRSI rows apply only to liable Class S contributors: annual reckonable income of at least EUR 5,000; ordinary liability below pensionable age, with the post-2024 continuation to under 70 for those born on or after 1 January 1958 who have not been awarded State Pension (Contributory). Do not apply the older guide's blanket exemption at 66. Excluded contributors, Class K, non-residents or pensions require classification before computing. Check this point with one of our partner accountants.

## The taxable base

**Step 1: trading profit (Case I trade, Case II profession).** Start from the accounts and the proper basis period; gross platform sales and platform fees are separate, not just net payouts. Turnover excludes VAT if the trader is VAT registered (see `ie-vat-return`). Separate non-trading receipts: salary, rent, interest, dividends, refunds (checking whether they reverse a previously deducted cost) and transfers between the client's own accounts. Accounts are kept, not sent: complete the "Extract from Accounts" panels and keep the records for six years ([Guide, "Attachments to Returns"](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

**Step 2: deductions and add-backs.** A cost is deductible if it is revenue (not capital) and incurred wholly and exclusively for the trade. Add back on Form 11: the private part of motor, light, heat and phone; donations and non-staff entertainment; depreciation; a loss on sale of fixed assets (deduct a profit on sale) ([Guide, Panel B](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)). Never deduct income tax, USC, PRSI or preliminary tax as trading expenses; drawings and loan principal are not revenue expenses. Premises, insurance, professional fees, software, advertising, finance fees, training, subscriptions, travel, business interest and bad debts must each meet the revenue/wholly-and-exclusively test; the category name alone establishes no relief. Fines and general bad-debt provisions are not defaults for deduction; disputed treatment requires a separate check. Check this point with one of our partner accountants.

**Step 3: capital allowances instead of depreciation.** Plant, machinery and business cars: 12.5% a year over 8 years on net cost (after grants and reclaimable VAT). A car’s qualifying expenditure follows its CO2 band (rates table) and the allowance is cut to the business-use share. The asset must belong to the trader and be in use for the trade at the end of the basis period; adjust for a short period and private use. A disposal can give a balancing allowance or charge; no normal wear-and-tear allowance is claimed for that disposal year. Disposal exceptions, car proceeds adjustments and accelerated energy-efficient equipment eligibility are not computed here. Check this point with one of our partner accountants. Taxis and cars for short-term hire use 40% reducing balance ([Guide, capital allowances](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

**Step 4: losses.** A trading loss can be set against other income of the same year (s.381), or carried forward against later profits of the same trade only (s.382). Claim s.381 relief within two years after the loss year; do not use the same loss twice, and use s.382 carry-forward as far as possible against the first subsequent profits. Non-active trades, restricted trades and partnership loss restrictions need their own tests; the former general EUR 31,750 rule is not a usable default. Check this point with one of our partner accountants. ([Guide, Lines 117-118](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

**Step 5: other income.** Add Case V rental profit, PAYE income (Panels D and E), foreign income (Panel F), and other Irish income such as interest and dividends (Panel G). **Rental income in outline:** compute each letting separately: rent receivable less the outgoings s.97(2) allows. Ignore uneconomic lettings excluded under s.75(4), and do not offset one spouse’s rental deficiency against the other’s surplus. Use rental capital allowances before brought-forward rental losses. Residential-landlord income-tax relief and retrofit relief require their own conditions; neither is assumed in the examples. Check this point with one of our partner accountants. Interest must relate to borrowing for the purchase, improvement or repair of the let premises, and the applicable RTB registration conditions must be satisfied for residential property; private borrowing does not qualify. Do not assume that all rent or every expense is chargeable/deductible merely because it is received/paid. Rental losses carry forward against rental income ([Guide, Panel C](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)). Use `ie-paye-rental-nonresident` for Case V in depth.

**Step 6: total income and deductions.** Deduct pension contributions (Panel I) within the age percentage of net relevant earnings and the EUR 115,000 earnings limit. Rental income is not relevant earnings. Relief also cannot exceed qualifying contributions paid; allocate the pension deduction against its relevant source. The examples assume a qualifying PRSA paid in the year, no competing pensionable employment and no carry-forward or election.

**Step 7: income tax.** Apply the band for the person's status at 20% and the rest at 40%. Then subtract credits; credits reduce tax, not income ([FA 2024 s.3](https://www.irishstatutebook.ie/eli/2024/act/43/section/3/enacted/en/html)). Unused personal/earned/employee credits do not produce a refund: floor the resulting income tax at zero. The Earned Income Credit is for self-employed earned income and a proprietary director's pay, not rent or interest. It cannot pass to a spouse. With the Employee credit, the two together cannot exceed EUR 2,000 ([Revenue, EIC](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx)).

**Step 8: USC and PRSI.** Include the self-assessed amounts on Form 11 and reconcile any deductions already made at source; a self-employed company director’s Class S on pay is collected under PAYE rather than charged twice.
- USC: on total income after capital allowances (active traders) but **before** pension contributions; the surcharge tests non-PAYE income only. Use only qualifying capital allowances actually used against that trade and same-trade losses carried forward actually used; current-year trading losses cannot shelter unrelated income for USC. Exclude exempt sources before applying the bands. Use `ie-usc`.
- PRSI Class S: on gross income after capital allowances, before pension contributions; minimum EUR 650 ([Revenue, PRSI](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx)). Pension contributions get income tax relief only, not PRSI or USC relief ([Revenue, pension relief](https://www.revenue.ie/en/jobs-and-pensions/pension/relief/index.aspx)). Use `ie-prsi-class-s`. Department of Social Protection pensions and benefits are exempt from PRSI ([Guide, PRSI for the self-employed](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

**Step 9: self-assessment.** Total income tax, USC and PRSI, less tax deducted at source and preliminary tax paid, gives the balance due or overpaid (Panel P).

**Where items go on the 2025 Form 11** ([Guide, contents](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)): A personal details; B self-employed income; C Irish rental income; D and E PAYE, BIK, pensions; F foreign income; G Irish other income; H exempt income; I charges and deductions; J personal tax credits; K restriction of reliefs (HIER); L capital gains; M, N, O chargeable assets, capital acquisitions, property incentives; P self-assessment. A shorter Form 11S exists for simpler cases.

## Deadlines and filing

- **Register** through eRegistration on ROS or Form TR1 parts A and B ([Revenue, who should register](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx)).
- **Pay and file, 31 October each year** (s.959I, s.959AO). By 31 October 2026: file the 2025 return, make the 2025 self-assessment, pay the 2025 balance, and pay 2026 preliminary tax ([Guide, "Pay and File"](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
- **ROS extension:** 18 November 2026, but only if the 2025 return is filed **and** the 2025 balance and 2026 preliminary tax are paid through ROS. If only one is done on ROS, the date stays 31 October 2026 ([eBrief 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx)).
- **The 2026 return** is due by 31 October 2027, with 2027 preliminary tax. No 2027 ROS extension is established by this Guide; do not assume one.
- **Preliminary tax:** pay at least the lowest of the three safe harbours (rates table). If too little is paid, or it is paid late, all the year's tax is treated as due on 31 October of the tax year and interest runs from then (s.959AO). For the ordinary first-year case the previous chargeable-year liability is treated as nil; assessment-status changes and the statutory special-relief adjustments must be checked before treating a comparator as zero ([Revenue, preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)). Detail in `ie-preliminary-tax`.
- **Direct debit:** Finance Act 2025 s.100 deleted s.959AP(2) to (4). Section 959AP(1) still requires authorisation and compliance with conditions reasonably imposed by the Collector-General; subsection (5) deems compliant preliminary tax paid on 31 October. Do not reuse the deleted statutory minimum of 3 or 8 instalments as a current safe harbour. The applicable scheme conditions must be established before relying on the 105% option. Check this point with one of our partner accountants. ([FA 2025 s.100](https://www.irishstatutebook.ie/eli/2025/act/18/section/100/enacted/en/html); [Notes for Guidance, s.959AP](https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part41a.pdf)).
- **Paper returns:** file by 31 August 2026 and Revenue calculates the tax; Revenue extended this to 30 September 2026. A paper return after that must include the self-assessment; failure to make a required self-assessment attracts a EUR 250 penalty under s.959X(1) ([Guide](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).
- **How to pay:** on ROS by debit instruction or Visa or Mastercard card; on myAccount; or by direct debit for preliminary tax ([Revenue, preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx)).
- **Amend** a ROS return on ROS; for a paper return, contact Revenue ([Revenue, pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx)).
- **Late claims:** from Finance Act 2025, a return filed late can still claim allowances, deductions and reliefs, unless another provision sets its own deadline (s.959I(6), [FA 2025 s.102](https://www.irishstatutebook.ie/eli/2025/act/18/section/102/enacted/en/html)).
- **Repayment claims** have a four-year limit (s.865): 2022 claims must reach Revenue by 31 December 2026 ([Guide](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)).

## Penalties and interest

- **Late filing surcharge (s.1084):** apply the statutory surcharge base after the permitted tax deductions/credits, not merely the balance left after preliminary tax. Directors and jointly assessed spouses/civil partners have special PAYE-credit restrictions. Do not infer the base from a single combined ROS balance. For the 2025 return: 5% (max EUR 12,695) if filed after 31 October 2026 and by 31 December 2026; 10% (max EUR 63,485) after 31 December 2026 ([Guide, "Surcharge for Late Returns"](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf)). Missing the ROS conditions means the 31 October date applies.
- **LPT surcharge:** if the Local Property Tax return or payment (or an agreed arrangement) is outstanding when Form 11 is filed, the self-assessment is increased by 10%, even if Form 11 is on time. Once LPT is brought up to date, this surcharge is capped at the LPT owed (same source).
- **Interest (s.1080):** 0.0219% a day, or part of a day, on late income tax ([TDM, interest guidelines](https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf)). A preliminary tax shortfall can move the due date of the whole liability back to 31 October of the tax year. Apply actual payment/credit dates; do not charge interest on amounts already paid.
- **Revenue estimate (s.959AX, from 2026):** if a return is not filed, Revenue may serve an estimate of the greater of the average tax due on the last two returns or EUR 1,000, recoverable as if self-assessed. It falls away if, within 30 days, the person files and pays the tax due, if any, with any incurred interest, penalties and surcharge, or notifies Revenue in writing that they are not a chargeable person for that period ([FA 2025 s.32](https://www.irishstatutebook.ie/eli/2025/act/18/section/32/enacted/en/html)).
- **Audit:** self-assessed returns are open to Revenue audit; refer audit and disclosure cases to a practitioner.

## Cross-border points

Foreign income belongs in Panel F, but residence, ordinary residence, domicile, remittances and treaty relief must be established before choosing the taxable amount. The former blanket worldwide/remittance statement is not a usable residence test. Non-resident credits (including the s.1032 tests), foreign-account reporting exemptions, foreign withholding/credits and A1/posting rules remain covered referral topics: use `ie-cross-border`, `ie-non-dom`, `ie-foreign-tax-and-withholding`, `ie-paye-rental-nonresident` and `ie-prsi-cross-border`. Check this point with one of our partner accountants.

## Worked examples

### Example 1: single sole trader, profit EUR 60,000 (2026 estimate)

Siobhan, single, aged 38, a designer, has adjusted trading profit of EUR 60,000 for 2026 after capital allowances. No other income, no pension contributions. Assume Irish residence, ordinary Class S liability, no reduced USC entitlement or additional reliefs, and a full-year computation.

Income tax: EUR 44,000 at 20% = 8,800; EUR 16,000 at 40% = 6,400; gross 15,200. Less the Single Person credit 2,000 and the Earned Income Credit 2,000 (20% of 60,000 is more than 2,000): EUR 11,200. USC: 60.06 + 333.76 + 3% of (60,000 less 28,700) = 939.00, total EUR 1,332.82; no surcharge. PRSI Class S: 60,000 x 4.2375% = EUR 2,542.50, above the EUR 650 minimum. Total 2026 liability: EUR 15,075.32. This supplies the previous-year comparator for the ordinary 2027 preliminary-tax test, subject to the statutory adjustments for assessment-status changes and special reliefs.

```oa-check
name: Single sole trader, profit EUR 60,000 (2026)
inputs:
  profit: 60000
steps:
  - it_gross: min(profit, 44000) * 0.20 + max(profit - 44000, 0) * 0.40
  - eic: min(2000, profit * 0.20)
  - income_tax: it_gross - 2000 - eic
  - usc: 12012 * 0.005 + 16688 * 0.02 + (min(profit, 70044) - 28700) * 0.03 + max(profit - 70044, 0) * 0.08
  - prsi: max(profit * 0.042375, 650)
  - total: income_tax + usc + prsi
expected:
  income_tax: 11200.00
  usc: 1332.82
  prsi: 2542.50
  total: 15075.32
```

### Example 2: trader with a car, rental income, a pension and the USC surcharge (2026)

Ciaran, single, aged 42, an active sole trader, has trading profit of EUR 95,000 before capital allowances. In 2026 he buys a new car for EUR 40,000 with CO2 of 130 g/km (VRT category B), used 80% for business, and a laptop for EUR 2,400. He has Case V rental profit of EUR 12,000 and pays EUR 8,000 into a PRSA.

Capital allowances: the 130 g/km car is category B, qualifying expenditure EUR 24,000 for its 2026 purchase. EUR 24,000 x 12.5% x 80% = 2,400. Laptop: 2,400 x 12.5% = 300. Total EUR 2,700. Trading profit EUR 92,300; with the given rental profit, total EUR 104,300. Assume both assets belong to the trader and are in use at the year end, a full-year basis period, and no reclaimable VAT or grants reducing the laptop cost.

Pension: 25% of net relevant earnings EUR 92,300 = EUR 23,075, so the given EUR 8,000 PRSA payment is relieved. Taxable income EUR 96,300. Income tax: EUR 8,800 + 40% of EUR 52,300 - EUR 4,000 credits = EUR 25,720.

USC is on EUR 104,300 before pension relief: EUR 60.06 + 333.76 + 1,240.32 + 8% of EUR 34,256 = EUR 4,374.62. All is non-PAYE income, so add 3% of EUR 4,300 = EUR 129. USC EUR 4,503.62. Class S on the given trading and rental profits: EUR 104,300 x 4.2375% = EUR 4,419.71. Total EUR 34,643.33. The rent is a given Case V profit after its own expense computation; no further rental deduction or relief is assumed.

```oa-check
name: Trader with car, rental income, PRSA and USC surcharge (2026)
inputs:
  trading_before_ca: 95000
  car_cost: 40000
  business_use: 80
  laptop: 2400
  rent_profit: 12000
  pension_paid: 8000
steps:
  - car_qualifying: 24000
  - car_ca: car_qualifying * 0.125 * business_use / 100
  - ca: car_ca + laptop * 0.125
  - trading: trading_before_ca - ca
  - total_income: trading + rent_profit
  - pension_relief: min(pension_paid, min(trading, 115000) * 0.25)
  - taxable: total_income - pension_relief
  - income_tax: 44000 * 0.20 + (taxable - 44000) * 0.40 - 2000 - min(2000, trading * 0.20)
  - usc_standard: 12012 * 0.005 + 16688 * 0.02 + 41344 * 0.03 + (total_income - 70044) * 0.08
  - usc_surcharge: max(total_income - 100000, 0) * 0.03
  - usc: usc_standard + usc_surcharge
  - prsi: round(max(total_income * 0.042375, 650), 2)
  - total: income_tax + usc + prsi
expected:
  ca: 2700.00
  total_income: 104300.00
  taxable: 96300.00
  income_tax: 25720.00
  usc: 4503.62
  prsi: 4419.71
  total: 34643.33
```

### Historical case 1: 2026 sole trader, EUR 60,000

The earlier case for Siobhán, single, age 38, designer, profit EUR 60,000 with no pension or other income is preserved by Example 1 above: income tax EUR 11,200, USC EUR 1,332.82, Class S EUR 2,542.50, total EUR 15,075.32. No year or numeric input changed.

### Historical case 2: jointly assessed couple, 2026

Aidan has adjusted sole-trade profit EUR 72,000; Niamh has employment pay EUR 20,000. Assume both resident, eligible for the married credit and their own full earned/employee credits, with no other income, deductions or reliefs. Band EUR 53,000 + min(EUR 35,000, EUR 20,000) = EUR 73,000; the second-earner increase is not transferable. Gross income tax EUR 22,200 less EUR 8,000 credits = EUR 14,200 before PAYE deducted from Niamh’s pay. Compute USC and PRSI separately for each spouse: Aidan’s USC EUR 1,790.62 and Class S EUR 3,051. Niamh’s payroll PRSI is a separate calculation, not Class S on the combined income.

```oa-check
name: Historical married two-income case 2026
inputs:
  trade: 72000
  employment: 20000
steps:
  - band: 53000 + min(35000, employment)
  - income_tax: band * 0.20 + (trade + employment - band) * 0.40 - 4000 - 2000 - 2000
  - trader_usc: 12012 * 0.005 + 16688 * 0.02 + 41344 * 0.03 + (trade - 70044) * 0.08
  - trader_prsi: trade * 0.042375
expected:
  band: 73000
  income_tax: 14200
  trader_usc: 1790.62
  trader_prsi: 3051
```

### Historical case 3: non-PAYE consultant, 2026

Given trading profit EUR 130,000, no PAYE income, no other income, deductible allowances or USC exemptions, standard USC is EUR 6,430.62 plus EUR 900 surcharge on the excess over EUR 100,000: EUR 7,330.62.

```oa-check
name: Historical consultant USC 2026
inputs:
  profit: 130000
steps:
  - standard: 12012 * 0.005 + 16688 * 0.02 + 41344 * 0.03 + (profit - 70044) * 0.08
  - surcharge: (profit - 100000) * 0.03
  - usc: standard + surcharge
expected:
  standard: 6430.62
  surcharge: 900
  usc: 7330.62
```

### Historical case 4: business car bought in March 2026

Siobhán buys a EUR 40,000 car in March 2026 with 75% evidenced business use. Assume ownership and use at the basis-period end, full-year allowances, and no disposal. At 110 g/km (A), EUR 24,000 x 12.5% x 75% = EUR 2,250. Add EUR 500 on the EUR 4,000 laptop/desk (assumed wholly business use, net of reclaimable VAT/grants): EUR 2,750. At 150 g/km (C), min(50% x EUR 24,000, 50% x EUR 40,000 retail price new) x 12.5% x 75% = EUR 1,125 for the car. At 170 g/km (D), no car allowance. Use the purchase price, not finance repayments; deduct only evidenced business running costs and add back private 25%.

```oa-check
name: Historical car alternatives 2026
inputs:
  car_price: 40000
  business_share: 0.75
  equipment: 4000
steps:
  - category_a: 24000 * 0.125 * business_share
  - equipment_ca: equipment * 0.125
  - total_a: category_a + equipment_ca
  - category_c: min(24000 * 0.5, car_price * 0.5) * 0.125 * business_share
  - category_d: 0
expected:
  category_a: 2250
  equipment_ca: 500
  total_a: 2750
  category_c: 1125
  category_d: 0
```

### Historical case 5: 2025 return and 2026 preliminary tax

Siobhán’s 2025 adjusted profit is EUR 52,000 and preliminary tax paid is EUR 10,000. Assume single status, full EUR 2,000 personal/Earned Income credits, ordinary Class S liability, standard USC, no other income or reliefs, and the same 2026 estimate as Example 1. Income tax EUR 8,000; USC EUR 1,106; PRSI EUR 2,145: total EUR 11,251 and balance EUR 1,251. With no direct debit, the ordinary comparators are EUR 11,251 (100% of 2025) and EUR 13,567.79 (90% of 2026 estimate); EUR 11,251 suffices. Combined payment EUR 12,502 met the ROS extension only if properly paid and filed by 18 November 2026. The original alternative uses a 2024 liability EUR 8,000 and a direct-debit scheme joined early in 2026: 105% is arithmetically EUR 8,400, but this is **not a usable payment instruction** until the scheme conditions and statutory comparator adjustments are satisfied. Check this point with one of our partner accountants.

```oa-check
name: Historical 2025 balance and 2026 preliminary tax
inputs:
  profit_2025: 52000
  paid_2025: 10000
  estimate_2026: 15075.32
  liability_2024: 8000
steps:
  - income_tax: 44000 * 0.20 + (profit_2025 - 44000) * 0.40 - 4000
  - usc: 12012 * 0.005 + 15370 * 0.02 + (profit_2025 - 27382) * 0.03
  - prsi: profit_2025 * 0.04125
  - liability: income_tax + usc + prsi
  - balance: liability - paid_2025
  - current_test: round(estimate_2026 * 0.90, 2)
  - preliminary: min(liability, current_test)
  - combined: balance + preliminary
  - dd_arithmetic_only: liability_2024 * 1.05
expected:
  income_tax: 8000
  usc: 1106
  prsi: 2145
  liability: 11251
  balance: 1251
  current_test: 13567.79
  preliminary: 11251
  combined: 12502
  dd_arithmetic_only: 8400
```

### Historical case 6: late filing and payment

Preserve the earlier facts: 2025 return filed 10 December 2026, alternative filing 15 January 2027, candidate combined liability EUR 11,251, unpaid balance EUR 1,251, and an assumed 30 interest days. The first filing falls within two months of 31 October; the second is later. Assume this is an ordinary non-director case with no source deductions, refunds or additional credits, so the Panel P amount of tax payable (IT, USC and PRSI after credits, before preliminary tax) is EUR 11,251. Under the 2025 Form 11 instructions, surcharge is calculated on that amount: 5% = EUR 562.55 or 10% = EUR 1,125.10, both below the relevant cap. A case with different source credits or director status needs a separate base calculation. For an established EUR 1,251 overdue income-tax amount and exactly 30 chargeable days at 0.0219%, interest is EUR 8.22. A preliminary-tax default could instead accelerate the liability; do not apply a 30-day balance-only calculation to that different case.

```oa-check
name: Historical late-return and interest case
inputs:
  candidate_base: 11251
  overdue_income_tax: 1251
  assumed_days: 30
steps:
  - early_surcharge: min(candidate_base * 0.05, 12695)
  - later_surcharge: min(candidate_base * 0.10, 63485)
  - interest: round(overdue_income_tax * 0.000219 * assumed_days, 2)
expected:
  early_surcharge: 562.55
  later_surcharge: 1125.10
  interest: 8.22
```

## Ask the client first

1. Which year, and why are you in self-assessment: trading, proprietary director (over 15%), rent, foreign income, or side income over EUR 5,000 net / EUR 30,000 gross? (Form 11 or Form 12.)
2. Single, married or civil partner (one or two incomes), or a single parent; your age and any full medical card? (Band, credits, USC reduced rates, pension limit.)
3. Accounts or records for the year, assets bought or sold, and for any car: cost, date, CO2 g/km and business-use share? (Capital allowances and add-backs.)
4. Other income: PAYE pay, rent, interest, dividends, foreign income, social welfare? (Credits, USC surcharge, PRSI.)
5. Preliminary tax paid and how (direct debit?), and the final liabilities for the two previous years? (Balance due and the 90/100/105% tests.)
6. Losses or capital allowances carried forward, pension contributions paid, and is your LPT up to date? (Base, relief, the 10% LPT surcharge.)

Refer to a practitioner: partnerships' own accounts (Form 1 (Firms)), the High Income Earner Restriction, property-based incentive reliefs and Section 23 relief, farming reliefs, residence changes and split years, foreign tax credits, share schemes, Revenue audits or unfiled years, and any year other than 2025 or 2026.

Before filing: open the appropriate year’s Form 11 on ROS; confirm every pre-populated panel, including PAYE and tax deductions; complete Panel P, compare the ROS calculation with the records, complete the Statement of Net Liabilities, arrange the payment, and Sign and Submit. A saved RPF file must be uploaded to ROS; saving it does not file it. Retain the acknowledgement and payment evidence. [Revenue filing steps](https://www.revenue.ie/en/self-assessment-and-self-employment/filing-your-tax-return/key-steps-in-filing-your-tax-return.aspx).

**Non-usable specialist holds.** Accelerated energy-efficient allowances (including the extension to 2030), non-active trade losses, HIER/Form RR1 (including ring-fenced income), property incentives/Section 23 and the property USC surcharge, farming, share schemes, audits/disclosures and unfiled years require their own operative tests. For each: Check this point with one of our partner accountants. For home working, establish an evidenced business allocation; no blanket floor-area allowance is granted here. Where capital/revenue classification is uncertain, do not default to capital allowances. Check this point with one of our partner accountants. DIRT, first-two-years filing concessions and disputed late-filing surcharge bases must be resolved before filing. Check this point with one of our partner accountants. Budget announcements and an assumed future ROS extension are not filing authority for another year.

## Sources

| Source and part read | URL | Read on |
|---|---|---|
| Finance Act 2024 s.3; read bands/credit amendments applicable from 2025 | https://www.irishstatutebook.ie/eli/2024/act/43/section/3/enacted/en/html | 2026-11-27 |
| Finance Act 2025 s.2; read the 2026 USC table and effective year | https://www.irishstatutebook.ie/eli/2025/act/18/section/2/enacted/en/html | 2026-11-27 |
| Finance Act 2025 s.26; read extension only; eligibility remains a hold | https://www.irishstatutebook.ie/eli/2025/act/18/section/26/enacted/en/html | 2026-11-27 |
| Finance Act 2025 s.32; read estimated-tax notice, amount and discharge conditions | https://www.irishstatutebook.ie/eli/2025/act/18/section/32/enacted/en/html | 2026-11-27 |
| Finance Act 2025 s.100; read deleted direct-debit subsections | https://www.irishstatutebook.ie/eli/2025/act/18/section/100/enacted/en/html | 2026-11-27 |
| Finance Act 2025 s.102; read late-return relief-claim saving and exceptions | https://www.irishstatutebook.ie/eli/2025/act/18/section/102/enacted/en/html | 2026-11-27 |
| Finance Act 2025 s.107; read commencement | https://www.irishstatutebook.ie/eli/2025/act/18/section/107/enacted/en/html | 2026-11-27 |
| Finance Act 2012 Schedule 4; read inserted TCA 959A/B/I/X/AO/AP and their operative conditions | https://www.irishstatutebook.ie/eli/2012/act/9/schedule/4/enacted/en/html | 2026-11-27 |
| Finance Act 2014 s.86; read PAYE coding exclusion amendment | https://www.irishstatutebook.ie/eli/2014/act/37/section/86/enacted/en/html | 2026-11-27 |
| Finance Act 2015 s.13; read net-income threshold amendment | https://www.irishstatutebook.ie/eli/2015/act/52/section/13/enacted/en/html | 2026-11-27 |
| Finance Act 2015 s.3; read EIC mechanism and separate spouse computations; current maxima in FA 2024 s.3 | https://www.irishstatutebook.ie/eli/2015/act/52/section/3/enacted/en/html | 2026-11-27 |
| TCA 1997 s.81; read revenue, private/capital expense and bad-debt restrictions | https://www.irishstatutebook.ie/eli/1997/act/39/section/81/enacted/en/html | 2026-11-27 |
| TCA 1997 s.381; read loss claim, ordering and time limit | https://www.irishstatutebook.ie/eli/1997/act/39/section/381/enacted/en/html | 2026-11-27 |
| TCA 1997 s.382; read same-trade carry-forward and no double relief | https://www.irishstatutebook.ie/eli/1997/act/39/section/382/enacted/en/html | 2026-11-27 |
| TCA 1997 s.1084; read surcharge base, credits and director exclusion; current euro maxima corroborated in Revenue instructions | https://www.irishstatutebook.ie/eli/1997/act/39/section/1084/enacted/en/html | 2026-11-27 |
| Finance Act 2003 s.23; read wear-and-tear rate, exceptions and commencement | https://www.irishstatutebook.ie/eli/2003/act/3/section/23/enacted/en/html | 2026-11-27 |
| Finance Act 2008 s.31; read car qualifying cost, emissions documents, exceptions and private-car regime | https://www.irishstatutebook.ie/eli/2008/act/3/section/31/enacted/en/html | 2026-11-27 |
| Finance Act 2019 s.19; read categories A/B and C and effective expenditure date | https://www.irishstatutebook.ie/eli/2019/act/45/section/19/enacted/en/html | 2026-11-27 |
| Finance Act 2020 s.14; read categories and emissions evidence; table read from PDF | https://www.irishstatutebook.ie/eli/2020/act/26/enacted/en/pdf | 2026-11-27 |
| Finance Act 2024 s.33; read tighter car treatment and 2027 expenditure start | https://www.irishstatutebook.ie/eli/2024/act/43/section/33/enacted/en/html | 2026-11-27 |
| Finance Act 1999 s.19; read ordinary 30-49 age percentages and specified occupations | https://www.irishstatutebook.ie/eli/1999/act/2/section/19/enacted/en/html | 2026-11-27 |
| Finance Act 2006 s.14; read later pension age percentages and earnings-limit references | https://www.irishstatutebook.ie/eli/2006/act/6/section/14/enacted/en/html | 2026-11-27 |
| Finance Act 2011 s.19; read earnings-limit amendment, corroborated for current year by Revenue | https://www.irishstatutebook.ie/eli/2011/act/6/section/19/enacted/en/html | 2026-11-27 |
| Finance (No. 2) Act 2009 s.29; read statutory daily interest table | https://www.irishstatutebook.ie/eli/2009/act/12/section/29/enacted/en/html | 2026-11-27 |
| Social Welfare Act 2023 s.32; read self-employed age continuation conditions | https://www.irishstatutebook.ie/eli/2023/act/37/section/32/enacted/en/html | 2026-11-27 |
| Social Welfare Act 2024 s.5; read Class S minimum amendment | https://www.irishstatutebook.ie/eli/2024/act/24/section/5/enacted/en/html | 2026-11-27 |
| Revenue Part 41A; read definition, filing, preliminary tax and payment conditions | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part41a.pdf | 2026-11-27 |
| Revenue 2025 Form 11 guide; read pp.3-11, 17-19, 24-28, 48-49, 62-68 for scope, panels, rates, adjustments, rental and surcharge calculation | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf | 2026-11-27 |
| Revenue rates chart; reused applicable independently checked Irish payroll rate/credit rows and read 2025/2026 columns | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx | 2026-11-27 |
| Revenue EIC; read qualifying income, amount, combined limit and non-transferability | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx | 2026-11-27 |
| Revenue registration; read Form 12 limits and registration methods | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/register-it-self-assessment.aspx | 2026-11-27 |
| Revenue preliminary tax; read comparators, payment methods and ordinary first year | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx | 2026-11-27 |
| Revenue pay/file; read dates, amendments and late returns | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx | 2026-11-27 |
| Revenue eBrief 034/26; read both ROS conditions and date | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx | 2026-11-27 |
| Revenue PRSI; read income/age gates, Class S and base | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/prsi-need-pay.aspx | 2026-11-27 |
| Revenue pension limits; read ordinary age scale and earnings cap | https://www.revenue.ie/en/jobs-and-pensions/pension/relief/tax-relief-limits.aspx | 2026-11-27 |
| Revenue pensions Chapter 26; read aggregate limit, multiple products and source allocation | https://www.revenue.ie/en/tax-professionals/tdm/pensions/chapter-26.pdf | 2026-11-27 |
| Revenue pension overview; read income tax relief and USC/PRSI exclusion | https://www.revenue.ie/en/jobs-and-pensions/pension/relief/index.aspx | 2026-11-27 |
| Revenue Part 18D; read aggregate income, exemptions, surcharge, separate spouses, capital allowances and losses | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part18d.pdf | 2026-11-27 |
| DSP SW14; read Class S annual blends and minimum on pp.15/18 and classification; applicable payroll proof reused | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf | 2026-11-27 |
| Revenue filing steps; read ROS panels, RPF upload, self-assessment and submission | https://www.revenue.ie/en/self-assessment-and-self-employment/filing-your-tax-return/key-steps-in-filing-your-tax-return.aspx | 2026-11-27 |
| Revenue rate band; read spouse increase and Home Carer interaction | https://www.revenue.ie/en/jobs-and-pensions/calculating-your-income-tax/tax-rate-band.aspx | 2026-11-27 |
| Revenue Age Tax Credit; read age and assessment conditions | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/health-and-age/age-tax-credit/index.aspx | 2026-11-27 |
| Revenue tax credits; read non-refundable unused credits | https://www.revenue.ie/en/jobs-and-pensions/calculating-your-income-tax/tax-credits.aspx | 2026-11-27 |
| Official revised Social Welfare Act; read reckonable-income definition and part-year blend mechanism | https://revisedacts.lawreform.ie/eli/2005/act/26/revised/en/html | 2026-11-27 |
| Revenue PAYE/self-assessment TDM; read side-income exclusions and continuing chargeability | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-42/42-04-13.pdf | 2026-11-27 |
| Revenue Employee Tax Credit; read earned-income limit, family exclusions and non-transferability | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/employee-tax-credit/index.aspx | 2026-11-27 |

Not yet confirmed: no unresolved assertion is usable. Foreign-account exemptions, direct-debit scheme conditions, new-trader first-two-years filing concessions, DIRT computations, disputed surcharge bases, home-office allocation, capital-versus-revenue uncertainty, age/class/cross-border PRSI exceptions, specialist reliefs and years outside 2025/2026 require the holds above or below; they are not defaults. Check this point with one of our partner accountants.
