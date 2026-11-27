---
name: de-payroll
description: "German employee payroll for 2026: PAP wage-tax computation, ordinary full-month social contributions, commercial Minijob arithmetic and basic filing. Trigger on Lohnsteuer, Lohnabrechnung, Brutto Netto, Steuerklasse, Sozialversicherung, Minijob, Midijob, Aktivrente and DEÜV. Establish actual payroll inputs first; specialist and historical cases have explicit referral holds."
version: 2.0
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# German payroll 2026: wage tax, social insurance and filing

> General reference for payroll preparation. Establish actual ELStAM, insurance and pay facts before producing a usable payslip. The worked cases are conditional arithmetic checks, not permission to fill missing facts with defaults.

## Who this applies to

This Guide computes ordinary full-month employment pay once tax and social-insurance status are established. Commercial Minijobs have a separate worksheet below. Part months, special insurance populations and the specialist topics listed below require their own determination.

A domestic employer includes one with a German residence, habitual abode, management, seat, permanent establishment or permanent representative; a foreign commercial labour supplier placing employees in Germany is also within § 38(1). For international secondments, the German receiving company is a domestic employer if it economically bears, or at arm's length should bear, the wages; direct payment is unnecessary. The employee owes wage tax and the employer withholds at each payment ([§ 38 EStG](https://www.gesetze-im-internet.de/estg/__38.html)).

Use [de-employee-income-tax](de-employee-income-tax.md) for the employee's annual return; [de-social-contributions](de-social-contributions.md) and [de-einkommensteuer-freelancer](de-einkommensteuer-freelancer.md) for self-employment; [de-non-resident-tax](de-non-resident-tax.md), [de-uk-employer-first-hire](de-uk-employer-first-hire.md) and [germany-to-switzerland-cross-border-tax](germany-to-switzerland-cross-border-tax.md) for the corresponding intake routes. Loading a sibling does not establish eligibility.

## Rates, bands and thresholds

The [final 2026 PAP](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2), pages 1–7, covers pay periods ending after 31 December 2025 and before 1 January 2027, and other payments received in that window. These are annual wage-tax parameters, not gross-pay exemptions.

| Wage-tax parameter | Amount or rule | Year | Official source |
| --- | --- | --- | --- |
| Basic allowance (Grundfreibetrag): no tax up to | EUR 12,348 | 2026 | [§ 32a(1) EStG](https://www.gesetze-im-internet.de/estg/__32a.html) |
| First progressive zone: (914.51 y + 1,400) y | EUR 12,349 to 17,799 | 2026 | § 32a(1) EStG, https://www.gesetze-im-internet.de/estg/__32a.html |
| Second progressive zone: (173.10 z + 2,397) z + 1,034.87 | EUR 17,800 to 69,878 | 2026 | § 32a(1) EStG, https://www.gesetze-im-internet.de/estg/__32a.html |
| Third zone: 0.42 x less 11,135.63 | EUR 69,879 to 277,825 | 2026 | § 32a(1) EStG, https://www.gesetze-im-internet.de/estg/__32a.html |
| Top zone: 0.45 x less 19,470.38 | from EUR 277,826 | 2026 | § 32a(1) EStG, https://www.gesetze-im-internet.de/estg/__32a.html |
| Employee lump sum (ANP), classes I to V | EUR 1,230 | 2026 | [§ 9a EStG](https://www.gesetze-im-internet.de/estg/__9a.html) |
| Special expenses lump sum (SAP), classes I to V | EUR 36 | 2026 | [§ 10c EStG](https://www.gesetze-im-internet.de/estg/__10c.html) |
| Single parent relief (EFA), class II, first child; each further child adds EUR 240 (only through an ELStAM allowance) | EUR 4,260 | 2026 | [§ 24b(2) EStG](https://www.gesetze-im-internet.de/estg/__24b.html) |
| Child allowances per counter, classes I to III (surcharge and church tax base only) | EUR 9,756 | 2026 | [PAP 2026](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2) |
| Child allowances per counter, class IV | EUR 4,878 | 2026 | PAP 2026, https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2 |
| Classes V and VI: minimum tax as share of the taxable amount | 14% | 2026 | [§ 39b(2) sentence 7 EStG](https://www.gesetze-im-internet.de/estg/__39b.html) |
| Classes V and VI: at most 42% above EUR 14,071; exactly 42% above EUR 34,939; 45% above EUR 222,260 | thresholds as stated | 2026 | § 39b(2) sentence 7 EStG; PAP 2026 (W1STKL5, W2STKL5, W3STKL5), https://www.gesetze-im-internet.de/estg/__39b.html |
| Vorsorgepauschale: the unemployment part counts only so far as it and the health and care parts together stay within | EUR 1,900 | 2026 | [§ 39b(2) sentence 5 no. 3(e) EStG](https://www.gesetze-im-internet.de/estg/__39b.html); PAP 2026 (VSPHB) |
| Reduced health rate used in the Vorsorgepauschale (PAP: KVSATZAN = KVZ/2/100 + 0.07) | 14.0% | 2026 | [§ 243 SGB V](https://www.gesetze-im-internet.de/sgb_5/__243.html); PAP 2026 |
| Solidarity surcharge on the wage tax | 5.5% | 2026 | [§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html) |
| Surcharge capped at this share of the excess over the exemption limit (phase-in) | 11.9% | 2026 | § 4 SolzG, https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Surcharge exemption limit, all classes except III | EUR 20,350 | 2026 | [§ 3(3) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) |
| Surcharge exemption limit, class III | EUR 40,700 | 2026 | § 3(3) SolzG, https://www.gesetze-im-internet.de/solzg_1995/__3.html |

| Ordinary contribution or employment parameter | Ceiling or amount | Official source |
| --- | --- | --- |
| Pension, ordinary insured employee: 18.6% total, derived 9.3% each | EUR 101,400/year; EUR 8,450/month | https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html ; https://www.gesetze-im-internet.de/sgb_6/__168.html ; https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html |
| Unemployment: 2.6% total, derived 1.3% each; same ceiling as pension | EUR 101,400/year; EUR 8,450/month | https://www.gesetze-im-internet.de/sgb_3/__341.html ; https://www.gesetze-im-internet.de/sgb_3/__346.html ; https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html |
| Statutory health: 14.6% plus the actual fund's additional rate, ordinarily half each | EUR 69,750/year; EUR 5,812.50/month | https://www.gesetze-im-internet.de/sgb_5/__241.html ; https://www.gesetze-im-internet.de/sgb_5/__249.html ; https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2 |
| Care: 3.6% total; derived employer 1.8% outside Saxony or 1.3% in Saxony, before employee adjustments below | EUR 69,750/year; EUR 5,812.50/month | https://www.gesetze-im-internet.de/pbav_2025/__1.html ; https://www.gesetze-im-internet.de/sgb_11/__58.html ; https://www.gesetze-im-internet.de/sgb_11/__55.html ; https://www.gesetze-im-internet.de/svbezgrv_2026/__2.html |
| Minimum hourly wage | EUR 13.90 in 2026; EUR 14.60 from 1 January 2027 | https://www.gesetze-im-internet.de/milov5/__1.html |
| Minijob regular monthly earnings limit, derived: ceil(13.90 × 130 / 3) | EUR 603 | https://www.gesetze-im-internet.de/milov5/__1.html ; https://www.gesetze-im-internet.de/sgb_4/__8.html |

Care shares below are derived from the regulation and §§ 55/58. The surcharge starts after the month of the 23rd birthday, not on that birthday. It does not apply to parents within the statutory definition, people born before 1 January 1940, military/civilian service personnel or the specified basic-income-support recipients. Adoptive and step-parent exclusions in § 55(4) must be checked. Each reduction from the second to fifth child lasts through the month that child turns, or would have turned, 25; a child already 25 is not counted for the reduction. Parenthood and child counts require proof. Automated proof, or other proof within six months of birth or a comparable qualifying event, works from that month; later other proof works from the following month ([§ 55 SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html)). Saxony depends on the place of employment ([§ 58 SGB XI](https://www.gesetze-im-internet.de/sgb_11/__58.html)).

| Children | Outside Saxony: employee | Outside Saxony: employer | Saxony: employee | Saxony: employer | Source |
| --- | --- | --- | --- | --- | --- |
| Childless surcharge applies (derived shares) | 2.4% | 1.8% | 2.9% | 1.3% | https://www.gesetze-im-internet.de/pbav_2025/__1.html ; https://www.gesetze-im-internet.de/sgb_11/__55.html ; https://www.gesetze-im-internet.de/sgb_11/__58.html |
| One qualifying child (any age); or childless with no surcharge (derived shares) | 1.8% | 1.8% | 2.3% | 1.3% | https://www.gesetze-im-internet.de/pbav_2025/__1.html ; https://www.gesetze-im-internet.de/sgb_11/__55.html ; https://www.gesetze-im-internet.de/sgb_11/__58.html |
| Two under 25 (derived shares) | 1.55% | 1.8% | 2.05% | 1.3% | https://www.gesetze-im-internet.de/pbav_2025/__1.html ; https://www.gesetze-im-internet.de/sgb_11/__55.html ; https://www.gesetze-im-internet.de/sgb_11/__58.html |
| Three under 25 (derived shares) | 1.3% | 1.8% | 1.8% | 1.3% | https://www.gesetze-im-internet.de/pbav_2025/__1.html ; https://www.gesetze-im-internet.de/sgb_11/__55.html ; https://www.gesetze-im-internet.de/sgb_11/__58.html |
| Four under 25 (derived shares) | 1.05% | 1.8% | 1.55% | 1.3% | https://www.gesetze-im-internet.de/pbav_2025/__1.html ; https://www.gesetze-im-internet.de/sgb_11/__55.html ; https://www.gesetze-im-internet.de/sgb_11/__58.html |
| Five or more under 25 (derived shares) | 0.8% | 1.8% | 1.3% | 1.3% | https://www.gesetze-im-internet.de/pbav_2025/__1.html ; https://www.gesetze-im-internet.de/sgb_11/__55.html ; https://www.gesetze-im-internet.de/sgb_11/__58.html |

## The taxable base

Use actual taxable pay, allowances, added amounts, tax class and factor. For ordinary active pay without pensions or age relief: annualise monthly pay × 12, weekly × 360/7 or daily × 360. Apply period ELStAM allowances/added amounts on the same annual basis. Deduct the class-specific lump sums, class-II relief and Vorsorgepauschale; apply the tariff; then take 1/12, 7/360 or 1/360 of annual wage tax, dropping excess cent fractions. Class VI has no employee or special-expense lump sum. Do not apply the basic tariff directly to class V or VI ([§ 39b(2) EStG](https://www.gesetze-im-internet.de/estg/__39b.html)).

Use the recorded class; do not infer a spouse's election or non-resident eligibility. Under [§ 39c(1) EStG](https://www.gesetze-im-internet.de/estg/__39c.html), culpably missing ID/date of birth or a refused ELStAM notification requires class VI. A technical retrieval failure or an ID omission without employee fault permits expected actual data for at most three calendar months. If ID/date of birth remains missing after that period, apply class VI retrospectively. On receipt of actual data in those temporary-data cases, review/correct earlier months and settle the difference at the next payroll. The separate missing-certificate/application cases in § 39c(2) require their own check.

**Vorsorgepauschale** (the employee's insurance, inside the tax; [§ 39b(2) sentence 5 no. 3 EStG](https://www.gesetze-im-internet.de/estg/__39b.html), PAP 2026):

- Pension: pay up to EUR 101,400 x 9.3% for employees compulsorily insured in the statutory pension scheme or exempt under § 6(1) no. 1 SGB VI for a professional pension scheme ([§ 39b(2) sentence 5 no. 3(a) EStG](https://www.gesetze-im-internet.de/estg/__39b.html)). Apply the PAP marker KRV: 0 for compulsory cover in the statutory or a professional pension scheme, or voluntary cover after exemption from compulsory insurance; 1 otherwise.
- Health and care: pay up to EUR 69,750 x (half the fund's additional rate + 7.0% + the employee care rate). The PAP uses the full additional rate of the employee's own fund: "Der durchschnittliche Zusatzbeitragssatz ist unmaßgeblich", except for the § 242(3) SGB V groups. The statutory health and care parts apply in classes I to VI ([§ 39b(2) sentence 5 no. 3(b), (c) EStG](https://www.gesetze-im-internet.de/estg/__39b.html)); the ministry's class VI test figures include them. Privately insured (PKV = 1): the private premiums from the ELStAM less the tax-free employer subsidy, classes I to V only; in class VI a privately insured employee gets no health or care part.
- Unemployment (new in 2026, ALV = 0 if insured, not in class VI): the PAP compares pension + health + care with pension + the lower of EUR 1,900 and (unemployment + health + care), and takes the higher. Once health and care alone pass EUR 1,900, unemployment adds nothing.
- The total is rounded up to whole euros (PAP 2026, MVSPKVPV and MVSPHB). There is no minimum Vorsorgepauschale in 2026. Severance under § 24 no. 1 EStG is left out of the insurance parts.

**The tariff and the class V and VI method as the 2026 PAP writes them** (UPTAB26, UP5-6 and MST5-6; [PAP 2026, Anlage 1](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2); W1STKL5 = 14071, W2STKL5 = 34939, W3STKL5 = 222260):

~~~
X = taxable amount, rounded down to whole euros (class III: half of it)
X up to 12348:            ST = 0
X up to 17799:            Y = (X - 12348) / 10000;  ST = (914.51 * Y + 1400) * Y
X up to 69878:            Z = (X - 17799) / 10000;  ST = (173.10 * Z + 2397) * Z + 1034.87
X up to 277825:           ST = 0.42 * X - 11135.63
above:                    ST = 0.45 * X - 19470.38
ST is rounded down to whole euros; class III: ST times 2

UP5-6(Z):  ST = 2 * (tariff(floor(Z * 1.25)) - tariff(floor(Z * 0.75)))
           ST = the higher of ST and floor(Z * 0.14)
MST5-6(X): if X > W2STKL5:
               ST = UP5-6(W2STKL5)
               if X > W3STKL5: ST = ST + floor((W3STKL5 - W2STKL5) * 0.42) + floor((X - W3STKL5) * 0.45)
               else:           ST = ST + floor((X - W2STKL5) * 0.42)
           else:
               ST = UP5-6(X)
               if X > W1STKL5: ST = the lower of ST and UP5-6(W1STKL5) + floor((X - W1STKL5) * 0.42)
~~~

**Children and surcharge.** The PAP deducts child allowances only when recalculating the surcharge/church base: EUR 9,756 per recorded counter in I–III, EUR 4,878 in IV; none in V/VI. Do not reduce wage tax itself for those counters. For ordinary running wages, compare the child-adjusted annual base with EUR 40,700 in III or EUR 20,350 in other classes. At or below the limit the surcharge is zero; above it take the lower of 5.5% of the base and 11.9% of the excess, then allocate to the pay period and drop excess cents. Other payments have a distinct threshold and no phase-in, so use their PAP routine rather than this running-pay shortcut ([§§ 3–4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html), [§ 4](https://www.gesetze-im-internet.de/solzg_1995/__4.html); PAP pages 21–22, 31).

**Ordinary contributions.** For established full-month insurance, use contribution pay up to each branch ceiling. Keep intermediate calculations unrounded; round final contributions to cents, with a third decimal of 5–9 rounding up. For equally shared contributions, calculate the half-rate share, round, then double for the total. Unequal shares are separately rounded and added ([§§ 1–2 BVV](https://www.gesetze-im-internet.de/beitrvv/__1.html), [§ 2](https://www.gesetze-im-internet.de/beitrvv/__2.html)). Do not treat the wage-tax Vorsorgepauschale as a payslip contribution.

**Commercial Minijob worksheet.** Establish the earnings/aggregation classification first; the regular limit is inclusive. The unforeseeable-overrun exception allows at most two calendar months within the relevant rolling year, each exceeding the limit by no more than the limit itself. Multiple Minijobs and a main job require the § 8(2) aggregation test and its notification/non-investigation rules; do not simply test each contract in isolation ([§ 8 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html)).

For an ordinary pension-insured commercial Minijob, the employer's pension share is 15% of actual pay; the employee bears the remainder ([§ 168(1) no. 1b SGB VI](https://www.gesetze-im-internet.de/sgb_6/__168.html)). At EUR 603, that is employer EUR 90.45 and employee EUR 21.71 (derived 3.6%); if statutory health membership and the § 249b conditions hold, employer health is 13%, EUR 78.39 ([§ 249b SGB V](https://www.gesetze-im-internet.de/sgb_5/__249b.html)). Where the employer owes the specified Minijob pension contributions, it may elect the 2% combined tax instead of ELStAM withholding: EUR 12.06 here ([§ 40a(2) EStG](https://www.gesetze-im-internet.de/estg/__40a.html)). These are component amounts, not total employer cost.

For an isolated full-month insured commercial Minijob, without another insured job, exemption or aggregation/part-month interaction, apply the EUR 175 pension minimum ([§ 163(8) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__163.html)). At actual pay EUR 100, total pension is 175 × 18.6% = EUR 32.55, employer 100 × 15% = EUR 15 and employee remainder EUR 17.55; applying 3.6% directly would be wrong ([§ 2(1) BVV](https://www.gesetze-im-internet.de/beitrvv/__2.html)).

**Specialist topics — non-usable holds.** The following topics remain in scope for referral; this Guide supplies no legal entitlement or filing result for them:

- Tax-class population/elections, single-parent eligibility and extra-child ELStAM allowance; professional pension exemptions, private-insurance ELStAM and exceptional PAP settings beyond the stated statutory framework. Check this point with one of our partner accountants.
- One-time pay, severance, earlier-employer certificates/code S, special surcharge computation and annual-return relief. Check this point with one of our partner accountants.
- Aktivrente: age/month, qualifying employer contributions, concurrent jobs/class VI, unused room, bonuses, prior-period pay, part months and continued contributions. Check this point with one of our partner accountants.
- Night, Sunday and holiday surcharges: actual work, additional pay, percentages, time windows, local holidays, tax versus contribution caps and overlapping surcharges. Check this point with one of our partner accountants.
- Multiple insured jobs above ceilings, one-time contribution allocation including the March rule, and miners/general-pension interaction. Check this point with one of our partner accountants.
- General/special JAEG eligibility, voluntary/private cover, health/care subsidies, retirement pension versus unemployment exemptions and the 2027 health ceiling. Check this point with one of our partner accountants.
- Midijobs: band, factor F, total versus employee bases, care surcharge/reductions, Saxony allocation, apprentices and low-pay training contribution rules. Check this point with one of our partner accountants.
- Minijob pension exemption and changes, private-household procedure/rates, short-term work versus its separate flat-tax tests, agricultural limits, other flat-tax routes and collection offices. Check this point with one of our partner accountants.
- Minimum-wage coverage, internships and other exclusions, sector rates, due dates, working-time accounts and working-time records. Check this point with one of our partner accountants.
- Continued sick pay, recurring illness, overtime/expense exclusions, performance pay, maternity protection/top-ups, net-input determination and special paying-agency/non-resident cases. Check this point with one of our partner accountants.
- U1/U2 coverage, fund tariffs, levy/reimbursement bases and exclusions, insolvency levy and accident insurance. Check this point with one of our partner accountants.
- Directors, shareholders/family, civil servants, students, pensions/old-age relief, benefits in kind/company cars, short-time pay, Krankengeld, parental leave/Elterngeld, annual leave and part-month payroll. Check this point with one of our partner accountants.

## Deadlines and filing

| Ordinary duty | Rule | Official source |
| --- | --- | --- |
| Wage-tax return and payment to the Betriebsstättenfinanzamt | By the 10th after the filing period; electronic return, subject to the approved hardship exception | https://www.gesetze-im-internet.de/estg/__41a.html |
| Filing period, based on prior-year wage tax payable | Monthly above EUR 5,000; quarterly above EUR 1,080 through EUR 5,000; annual up to EUR 1,080. Annualise a prior part-year business or the first full month of a new business | https://www.gesetze-im-internet.de/estg/__41a.html |
| Ordinary tax deadline on Saturday, Sunday or public holiday | Next working day; check a specific authority order | https://www.gesetze-im-internet.de/ao_1977/__108.html |
| Employment contributions | Expected liability by the third-last bank working day of the work month; remainder by that day next month. The statutory prior-month simplification excludes the prior month's one-time-pay contributions | https://www.gesetze-im-internet.de/sgb_4/__23.html |
| Contribution statement | Electronically two working days before contributions fall due; household-cheque exception. Missing statements permit an estimate | https://www.gesetze-im-internet.de/sgb_4/__28f.html |
| Ordinary DEÜV start/end report | First following payroll, at latest six weeks after start/end | https://www.gesetze-im-internet.de/de_v/__6.html ; https://www.gesetze-im-internet.de/de_v/__8.html |
| 2026 DEÜV annual report | For those insured on 31 December: first following payroll, by 15 February 2027; omitted if a §§ 8/9/12 report is due at 31 December. Report only pay not already reported | https://www.gesetze-im-internet.de/de_v/__10.html |
| Payslip | Text form at payment, showing period and pay components/deductions; no repeat needed if unchanged from the last proper statement. Complete the separate EBV content check | https://www.gesetze-im-internet.de/gewo/__108.html |

In the original filing case, EUR 4,200 payable for 2025 places the employer in quarterly filing for 2026. Its ordinary Q3 date of Saturday 10 October 2026 moves to Monday 12 October ([§ 41a EStG](https://www.gesetze-im-internet.de/estg/__41a.html), [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html)).

Before the first run, establish the collecting office, employer whole-contribution remittance and employee-deduction duties, employer number, monthly ELStAM-change retrieval, payroll accounts and record retention. Immediate sector reports, interruption/change reports, employee report copies, accident-insurance annual reports, electronic wage certificates, annual wage-tax adjustment eligibility/exclusions and EBV fields/redaction need their complete operative checks; the ordinary DEÜV dates above do not replace them. Check this point with one of our partner accountants.

**2025 corrections — non-usable hold.** Preserve the original 2025 periods and use their applicable law/PAP, not the 2026 worksheet. The previous worksheet's inputs were basic allowance EUR 12,096, surcharge threshold EUR 19,950 outside III, pension ceiling EUR 96,600, health ceiling EUR 66,150, minimum wage EUR 12.82 and Minijob limit EUR 556. Its nominal annual-report date was 15 February 2026 and certificate date 28 February 2026, with proposed moved dates 16 February and 2 March. Those amounts/dates are retained solely to identify the old case; none is a cleared 2025 payroll or filing instruction here. Check this point with one of our partner accountants.

## Penalties and interest

Late wage-tax payment ordinarily costs 1% of the arrears rounded down to a EUR 50 multiple for each started month; arrears must first have been assessed or declared. The up-to-three-day grace excludes § 224(2) no. 1 cash/cheque payment. Thus the original EUR 1,275 case, assuming an assessed/declared amount one month late and no relief, gives 1% × EUR 1,250 = EUR 12.50 ([§ 240 AO](https://www.gesetze-im-internet.de/ao_1977/__240.html)).

Late employment contributions ordinarily cost 1% of arrears rounded down to a EUR 50 multiple for each started month; a surcharge on arrears below EUR 150 is omitted if it would need separate demand. For retroactive assessment, no surcharge insofar as the debtor credibly shows lack of fault in not knowing the liability. The original EUR 3,480 case, assuming no exception, gives EUR 34.50 per started month ([§ 24 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__24.html)).

Missed employee contribution deductions are ordinarily recoverable at the next three wage payments, then only if the employer was not at fault. The deduction-only and three-payment restrictions do not apply to the specified intentional/grossly negligent information breach, employee-only full contribution or benefits-in-kind-only cases ([§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html)). Late-filing discretion/formula and employer tax-liability exceptions need case-specific determination. Check this point with one of our partner accountants.

## Cross-border points

Apply the § 38 employer test above. Non-resident class/ID office, § 1a eligibility, short assignments/flat tax, treaty exemption data, A1/posting or treaty certificates, and foreign-income effects on annual adjustment are non-usable holds pending their actual facts and operative conditions. Check this point with one of our partner accountants.

## Worked examples

Both original numerical input sets are retained. These computations assume no unlisted taxable benefits, allowances, added amounts, pension/age relief, exemptions or special payroll events. Validate every marker before use; unknown inputs stop a usable payroll result.

### Example 1: class I, EUR 5,000 a month, childless, outside Saxony

Original facts: age 30, no church/children, Hesse, statutory fund additional rate 2.9%, EUR 5,000 monthly, no one-time payments. Conditional ordinary insurance computation: annual EUR 60,000; pension VSP EUR 5,580 plus health/care EUR 6,510 gives VSP EUR 12,090. Taxable annual amount 60,000 − 1,230 − 36 − 12,090 = EUR 46,644. The tariff gives EUR 9,389/year and EUR 782.41/month; surcharge zero. Employee contributions EUR 465 + 65 + 437.50 + 120 = EUR 1,087.50; net before any other deductions EUR 3,130.09. Ordinary employer shares are EUR 465 + 65 + 437.50 + 90 = EUR 1,057.50; employer levies are additional and held above. Sources: [§ 39b](https://www.gesetze-im-internet.de/estg/__39b.html), [PAP pages 26–28 and 39](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2) and the contribution rows.

```oa-check
name: DE 2026 class I, EUR 5,000 a month, childless, fund rate 2.9%
inputs:
  monthly_pay: 5000
  fund_rate: 2.9
steps:
  - annual: monthly_pay * 12
  - vsp_pension: min(annual, 101400) * 0.093
  - vsp_health_care: min(annual, 69750) * (fund_rate / 2 / 100 + 0.07 + 0.024)
  - vsp_unemp_cap: min(1900, min(annual, 101400) * 0.013 + vsp_health_care)
  - vsp: ceil(max(vsp_pension + vsp_health_care, vsp_pension + vsp_unemp_cap))
  - zve: floor(annual - 1230 - 36 - vsp)
  - z: (zve - 17799) / 10000
  - annual_tax: floor((173.10 * z + 2397) * z + 1034.87)
  - monthly_tax: floor(annual_tax / 12 * 100) / 100
  - soli: min(annual_tax * 0.055, max(0, annual_tax - 20350) * 0.119)
  - ee_pension: round(monthly_pay * 0.093, 2)
  - ee_unemp: round(monthly_pay * 0.013, 2)
  - ee_health: round(monthly_pay * (14.6 + fund_rate) / 2 / 100, 2)
  - ee_care: round(monthly_pay * 0.024, 2)
  - ee_total: ee_pension + ee_unemp + ee_health + ee_care
  - net: monthly_pay - monthly_tax - ee_total
expected:
  vsp: 12090
  zve: 46644
  annual_tax: 9389
  monthly_tax: 782.41
  soli: 0
  ee_total: 1087.50
  net: 3130.09
```

### Example 2: class III, EUR 9,000 a month, two children, church member, above the ceilings

Original facts: married, spouse V, two recorded child counters, children aged 8 and 12, church membership with an assumed 8% rate, employment outside Saxony, fund additional rate 2.5%, EUR 9,000/month (EUR 108,000/year), voluntary statutory membership. Age, actual ELStAM, qualifying voluntary health/care status and the applicable church calculation still require confirmation: **the final payslip/subsidy/church result is a non-usable hold.** Check this point with one of our partner accountants.

Conditional arithmetic: capped pension VSP EUR 9,430.20; health/care EUR 6,835.50; total EUR 16,265.70 rounds up to EUR 16,266. Taxable amount EUR 90,468; splitting tax EUR 17,826/year, EUR 1,485.50/month. Child-adjusted base gives EUR 11,626, so no surcharge. Multiplying that annual base by the stipulated 8% gives EUR 930.08 as arithmetic only, not actual annual church withholding. Component shares EUR 785.85 + 109.85 + 496.97 + 90.09 total EUR 1,482.76; the hypothetical employer care share rounds to EUR 104.63. They do not establish the real voluntary contribution or subsidy entitlement. Sources: [PAP](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2), [§ 39b](https://www.gesetze-im-internet.de/estg/__39b.html) and the contribution/rounding rows.

```oa-check
name: DE 2026 class III, EUR 9,000 a month, two children, church 8%, capped
inputs:
  monthly_pay: 9000
  fund_rate: 2.5
  child_counters: 2
  church_rate: 8
steps:
  - annual: monthly_pay * 12
  - care_ee_rate: 0.018 - (child_counters - 1) * 0.0025
  - vsp_pension: min(annual, 101400) * 0.093
  - vsp_health_care: min(annual, 69750) * (fund_rate / 2 / 100 + 0.07 + care_ee_rate)
  - vsp_unemp_cap: min(1900, min(annual, 101400) * 0.013 + vsp_health_care)
  - vsp: ceil(max(vsp_pension + vsp_health_care, vsp_pension + vsp_unemp_cap))
  - zve: floor(annual - 1230 - 36 - vsp)
  - x: floor(zve / 2)
  - z: (x - 17799) / 10000
  - annual_tax: floor((173.10 * z + 2397) * z + 1034.87) * 2
  - monthly_tax: floor(annual_tax / 12 * 100) / 100
  - x_child: floor((zve - child_counters * 9756) / 2)
  - z_child: (x_child - 17799) / 10000
  - jbmg: floor((173.10 * z_child + 2397) * z_child + 1034.87) * 2
  - soli: min(jbmg * 0.055, max(0, jbmg - 40700) * 0.119)
  - church_tax_year: jbmg * church_rate / 100
  - ee_pension: round(min(monthly_pay, 8450) * 0.093, 2)
  - ee_unemp: round(min(monthly_pay, 8450) * 0.013, 2)
  - ee_health: round(min(monthly_pay, 5812.50) * (14.6 + fund_rate) / 2 / 100, 2)
  - ee_care: round(min(monthly_pay, 5812.50) * care_ee_rate, 2)
  - ee_total: ee_pension + ee_unemp + ee_health + ee_care
  - er_care: round(min(monthly_pay, 5812.50) * 0.018, 2)
expected:
  vsp: 16266
  zve: 90468
  annual_tax: 17826
  monthly_tax: 1485.50
  jbmg: 11626
  soli: 0
  church_tax_year: 930.08
  ee_total: 1482.76
  er_care: 104.63
```

**Original ancillary cases — arithmetic audits with non-usable legal outcomes.** Preserve these inputs; none establishes the missing entitlement, classification or base. Check this point with one of our partner accountants.

- Midijob AE EUR 1,000, G EUR 603, stipulated F 0.6619: the former two formulas give EUR 854.06 and EUR 568.36; a stipulated 0.6% surcharge on the first is EUR 5.12, not EUR 3.41 on the second. This does not clear factor F, the band or Saxony allocation.
- Multiple-job pension pay EUR 10,000 and EUR 2,000, ceiling EUR 8,450: the former capped-input allocation gives EUR 6,832.78 and EUR 1,617.22. The allocation's legal applicability remains held.
- Stipulated eligible sick pay EUR 1,000: 80% is EUR 800 and 60% is EUR 600. No U1 tariff or eligible reimbursement base is assumed.
- Independently established maternity daily net inputs EUR 60 and EUR 40: (60 + 40 − 13) = EUR 87; proportions give EUR 52.20 and EUR 34.80. No actual net input/top-up eligibility is established.
- Hourly basic pay EUR 30, stipulated 25% night premium, former tax/contribution caps EUR 50/EUR 25: EUR 7.50 premium, EUR 6.25 on the lower cap and EUR 1.25 difference. Actual hours, exemption and contribution treatment remain held.
- Aktivrente from May 2026, EUR 2,500/month, stipulated monthly room EUR 2,000 and annual EUR 24,000: EUR 500 difference per month and EUR 16,000 over eight qualifying months. At pay EUR 1,500 plus December bonus EUR 800, stipulated unused room EUR 500 leaves EUR 300. Eligibility, exemption and contribution treatment remain held.

**Original PAP test table.** These annual test values are from page 39, with ALV/KRV/PKV = 0, KVZ = 2.90, PVZ = 0 in II and 1 otherwise, and other test settings as in the PAP. They are not a second-job liability estimate for unstated facts. Annual-return duties for simultaneous employers require the separate § 46 exceptions check. Check this point with one of our partner accountants.

| Annual gross test input | I (= IV) | II | III | V | VI | Source |
| --- | --- | --- | --- | --- | --- | --- |
| EUR 20,000 | EUR 380 | EUR 0 | EUR 0 | EUR 2,234 | EUR 2,766 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2 |
| EUR 60,000 | EUR 9,389 | EUR 8,091 | EUR 4,822 | EUR 15,364 | EUR 15,895 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2 |
| EUR 100,000 | EUR 23,248 | EUR 21,634 | EUR 15,012 | EUR 30,157 | EUR 30,689 | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2 |

## Ask the client first

Obtain actual ELStAM class/counters/church/allowance/factor and first/further-job designation; actual health fund/rate or private premiums and voluntary status; age, retirement date, parent/child proof; place of employment; all jobs/status decisions; prior-year wage tax; ordinary/one-time pay and benefits; hours/surcharges; and sickness/maternity/other absences. Missing facts remain missing: do not default to class I, no church, no children, outside Saxony or insurance in every branch. A planning average is not the actual fund rate.

## Sources

Retained law was read on 27 November 2026 except the unchanged § 32a tariff and § 9a employee lump sum, reused from the completed 26 November claims read. Exact original-language proof and the complete historical-topic dispositions are in the private claims ledger. Referral holds make no positive legal determination.

| Source | Official URL | Read on |
| --- | --- | --- |
| Final PAP 2026, scope/inputs/tax flow/test table | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2 | 2026-11-27 |
| Wage-tax collection, computation, missing-data and filing | https://www.gesetze-im-internet.de/estg/__38.html ; https://www.gesetze-im-internet.de/estg/__39b.html ; https://www.gesetze-im-internet.de/estg/__39c.html ; https://www.gesetze-im-internet.de/estg/__41a.html | 2026-11-27 |
| Tariff and employee lump sum, unchanged completed proof reused; payroll effect also read in PAP | https://www.gesetze-im-internet.de/estg/__32a.html ; https://www.gesetze-im-internet.de/estg/__9a.html | 2026-11-26 |
| Special-expense and single-parent payroll parameters | https://www.gesetze-im-internet.de/estg/__10c.html ; https://www.gesetze-im-internet.de/estg/__24b.html ; https://www.gesetze-im-internet.de/estg/__39a.html | 2026-11-27 |
| Solidarity base, limit and rate | https://www.gesetze-im-internet.de/solzg_1995/__3.html ; https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-11-27 |
| Pension rate, allocation and minimum base | https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html ; https://www.gesetze-im-internet.de/sgb_6/__168.html ; https://www.gesetze-im-internet.de/sgb_6/__163.html | 2026-11-27 |
| Unemployment and health rates/allocation | https://www.gesetze-im-internet.de/sgb_3/__341.html ; https://www.gesetze-im-internet.de/sgb_3/__346.html ; https://www.gesetze-im-internet.de/sgb_5/__241.html ; https://www.gesetze-im-internet.de/sgb_5/__249.html | 2026-11-27 |
| Care rate, children, proof and sharing | https://www.gesetze-im-internet.de/pbav_2025/__1.html ; https://www.gesetze-im-internet.de/sgb_11/__55.html ; https://www.gesetze-im-internet.de/sgb_11/__58.html | 2026-11-27 |
| 2026 social values; contribution rounding | https://www.gesetze-im-internet.de/svbezgrv_2026/__2.html ; https://www.gesetze-im-internet.de/svbezgrv_2026/__4.html ; https://www.gesetze-im-internet.de/beitrvv/__1.html ; https://www.gesetze-im-internet.de/beitrvv/__2.html | 2026-11-27 |
| Minimum wage, minor employment, Minijob health and flat tax | https://www.gesetze-im-internet.de/milov5/__1.html ; https://www.gesetze-im-internet.de/sgb_4/__8.html ; https://www.gesetze-im-internet.de/sgb_5/__249b.html ; https://www.gesetze-im-internet.de/estg/__40a.html | 2026-11-27 |
| Employment contribution payment/statements/recovery/late payment | https://www.gesetze-im-internet.de/sgb_4/__23.html ; https://www.gesetze-im-internet.de/sgb_4/__28f.html ; https://www.gesetze-im-internet.de/sgb_4/__28g.html ; https://www.gesetze-im-internet.de/sgb_4/__24.html | 2026-11-27 |
| Basic reports and payslip | https://www.gesetze-im-internet.de/de_v/__6.html ; https://www.gesetze-im-internet.de/de_v/__8.html ; https://www.gesetze-im-internet.de/de_v/__10.html ; https://www.gesetze-im-internet.de/gewo/__108.html | 2026-11-27 |
| Tax weekend rule (unchanged completed read reused) and late payment | https://www.gesetze-im-internet.de/ao_1977/__108.html ; https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-11-26; 2026-11-27 respectively |

Non-usable holds include the unacquired Federal Gazette factor-F notice, actual state church-tax rules/caps, actual U1/U2/accident rates and the 2027 health ceiling. The original factor 0.6619, planning additional rate 2.9%, general JAEG EUR 77,400/year (EUR 6,450/month), special JAEG EUR 69,750 and proposed 2027 EUR 3,600 addition are not substitutes for those missing operative determinations. Check this point with one of our partner accountants.
