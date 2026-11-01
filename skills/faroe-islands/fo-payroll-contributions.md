---
name: fo-payroll-contributions
description: >
  Prepare 2026 Faroese payroll with separate tax, contribution, pension and
  holiday schedules. Classify A-income, check the employee and employer payer
  rules, and reconcile statutory health, parental, ALS, labour-market pension,
  occupational-disease and guarantee charges. Apply employee age, residence,
  foreign-coverage and FAS exceptions separately from employer liability. Check
  the annual ALS and pension limits, pension-tax withholding and final rates,
  holiday accruals, payslips, information reporting and invoice deadlines,
  including mid-year ALS procedure changes. Use for Faroese payroll, employer
  contributions, mandatory pension, social insurance, holiday pay and foreign
  workers. Includes proved employee-payment and car-mileage benefit adjustments and dated
  2026 pension rules. Other specified benefit transitions and operational cases
  remain open. Independent AI review accepted partial draft publication;
  professional attestation is pending.
version: 0.3
jurisdiction: FO
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Faroe Islands payroll and mandatory contributions v0.3

> **Checked against the law.** Income year 2026; selected current statutes and authority guidance read 25 October 2026; benefit, dated pension and contribution provisions re-read 28 October 2026. This Guide prepares payroll working papers, with professional review pending.

## Who this applies to

Apply to payers of Faroese A-income, employees and self-employed persons where each named contribution applies. Wages, holiday pay, board fees, specified replacement benefits and employer cash gifts have A-income classification under Tax Act §60. A foreign payer, a statutory exception or non-cash benefit needs its own classification; §62 makes TAKS the decision-maker in doubt. The distinction is not settled by a payslip label. [Tax Act §§57, 60–62][tax]

Before paying A-income, route it through an authorised settlement institution under §63. Supply the payee's P-tal/temporary identification, name/address, earnings period and amount, and deliver the statutory written payslip information with each payment. Reconcile the institution's itemised tax withholding to the wage ledger. A tax computed from annual bands alone is not a substitute for the live cumulative withholding instruction. [Tax Act §§63–64][tax]

Income tax, statutory worker charges, employer charges, pension funding and holiday entitlement are separate. An employee-side age or foreign-coverage exception does not automatically exempt the employer. A pension contribution transferred by the employer is not necessarily an additional employer-funded benefit: establish the employment contract and statutory minimum separately. [Pension Act §§1–3][pension]; [AMEG Act §2][ameg]; [ALS Act §§7–9][als]; [Parental Act §§17–19][parental]

## Rates, bands and thresholds

| Charge | Rate / boundary and payer | Tax year / official source |
|---|---|---|
| Health insurance | Eligible resident person aged at least 18: DKK 175/month plus 0.70% of taxable income | 2026; [Health Act §§1, 24](https://logir.fo/Logtingslog/178-fra-22-12-2009-um-almenna-heilsutrygd-sum-seinast-broytt-vid-logtingslog-nr-129-fra) |
| Parental contribution | 0.86% of the statutory A-income base, separately for liable recipient and payer | 2026; [Parental Act §§17–19](https://logir.fo/Logtingslog/48-fra-03-04-2001-um-barsilsskipan-sum-seinast-broytt-vid-logtingslog-nr-123-fra-22) |
| ALS unemployment | 0.6% of the statutory base, recipient and payer subject to their own rules | 2026; [ALS Act §§7–9](https://logir.fo/Logtingslog/113-fra-13-06-1997-um-arbeidsloysistrygging-og-arbeidsavising-sum-seinast-broytt-vid-logtingslog-nr-79); [Regulation 203/2020 §1](https://logir.fo/Kunngerd/203-fra-18-12-2020-um-ALSgjald) |
| Employee ALS annual base ceiling | DKK 650,000, giving DKK 3,900 at 0.6%; do not apply the insured-person cap to an employer automatically | 2026; [ALS Act §8(2)](https://logir.fo/Logtingslog/113-fra-13-06-1997-um-arbeidsloysistrygging-og-arbeidsavising-sum-seinast-broytt-vid-logtingslog-nr-79); [ALS 2026 notice](https://www.als.fo/fo/um-als/tidindi/als-gjaldid-laekkadi-1-januar-1) |
| Labour-market pension, AMEG | 3% of person's statutory taxable base; separate employer 3% of paid A-income | 2026; [AMEG Act §2](https://logir.fo/Logtingslog/39-fra-07-05-1991-um-arbeidsmarknadareftirlonargrunn-sum-seinast-broytt-vid-logtingslog-nr149-fra-20-desember); [Regulation 45/2024 §§1–3](https://logir.fo/Kunngerd/45-fra-21-05-2024-um-gjald-til-arbeidsmarknadareftirlonargrunn) |
| Mandatory individual pension | At least 12% of combined eligible A/B income; annual mandatory gross contribution capped at DKK 150,000 | 2026; [Pension Act §2(1), (4)](https://logir.fo/Logtingslog/49-fra-14-05-2013-um-eftirlonarsamansparing-og-skatt-af-eftirlon-og-rentutryggingum) |
| Small mandatory-pension amounts | A-income contribution below DKK 30 / B-income contribution below DKK 500 not charged under the current rule; equality is not below | From 28 February 2026; [Act 23/2026 §1(6), §2](https://logir.fo/Logtingslog/23-fra-26-02-2026-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin) and publication 27 February |
| Provisional pension contribution tax | 40%, settled separately from ordinary wage income tax | 2026; [Pension Act §12(2), annex 1](https://logir.fo/Logtingslog/49-fra-14-05-2013-um-eftirlonarsamansparing-og-skatt-af-eftirlon-og-rentutryggingum) |
| Occupational-disease fund | Employer 0.05% of paid A-income; self-employed 0.05% of prior-year statutory taxable income | 2026; [Work Injury Act §79(2)–(3)](https://logir.fo/Logtingslog/67-fra-25-05-2009-um-trygging-moti-avleidingunum-av-arbeidsskada-sum-broytt-vid-logtingslog-nr) |
| Guarantee fund | Published operating rate 2 per thousand of paid A-income; statutory ceiling is also 2 per thousand, with specified foreign FAS exceptions | 2026; [TAKS employer table](https://www.taks.fo/fo/vinna/studul/almenn-gjoeld-hja-arbeidsgevarum); [Guarantee Act §7](https://logir.fo/Logtingslog/68-fra-09-06-1988-um-trygdargrunn-fyri-avreidingar-og-lonir-vm-sum-seinast-broytt-vid) |
| Ordinary holiday pay | 12% of eligible earned wages | 2026; [Holiday Act §§10, 12–13](https://logir.fo/Logtingslog/30-fra-07-04-1986-um-fritid-vid-lon-sum-seinast-broytt-vid-logtingslog-nr-56) |
| Monthly-paid holiday route | Paid leave plus 1.5% supplement on eligible prior-earning-year wages; statutory departures use §11(2) | 2026; [Holiday Act §§11–13](https://logir.fo/Logtingslog/30-fra-07-04-1986-um-fritid-vid-lon-sum-seinast-broytt-vid-logtingslog-nr-56) |

The pension annex's final contribution tax is **30%** where statutory annual income is above zero and at most **DKK 235,000**, then rises by **0.5 percentage point** for each successive **DKK 5,000** band, with upper endpoints included: above DKK 325,000 through DKK 330,000 is **39.5%**, above DKK 330,000 **40%**. This is a rate on the **whole contribution**, not marginal income bands. Excess provisional tax is returned to the pension account without interest under §12(2). Check the annex row against the final statutory income. [Pension Act §12 and annex 1][pension]

Employer broadcasting is a separate annual prior-year payroll-based invoice, not a percentage deducted from every worker. Personal broadcasting also has its own age/scope rules; retrieve the current assessment rather than treating it as employer pension or insurance. [TAKS employer broadcasting][broadcast]

## The base

### Separate base and payer schedules

For every component record cash compensation, taxable non-cash benefits, A-income, ordinary taxable income, exclusions, age/residence/coverage evidence, cumulative annual base, rate, payer and settlement route. The Health and employee AMEG bases are statutory taxable income; employer AMEG uses paid A-income. ALS and parental contributions use their own inclusion/exclusion lists. Do not add all published percentages and apply the sum to gross wages. [Health Act §24][health]; [AMEG Act §2][ameg]; [ALS Act §§7–8][als]; [Parental Act §§17–18][parental]

Health liability is tied to residence/coverage under §§1, 24, not merely A-income. Under Regulation 76/2024, qualifying Nordic social-insurance payment and the statutory no-deduction condition can support an application for exemption. Keep foreign coverage/payment, work-country/employer and Faroese-work-share evidence. Partial-year relief distinguishes monthly fixed charges and the income earned during the exempt period; a blanket annual exemption is not inferred. Notify cessation of foreign payment. [Health Act §24(2)][health]; [Regulation 76/2024 §§1–4][healthreg]

Employee AMEG ceases under the retirement-age rule, with Regulation 45/2024 §1(2) applying exemption from the start of the year the person reaches statutory pension age. A newcomer within three years of that age who has never previously had a Faroese home has a separate exception. Employer age does not exempt staff wages; employer liability remains on A-income under §2. Specified foreign FAS wages have their separate worker/employer exclusions. Nordic social-security coordination requires its actual application, not a generic EU assumption. [AMEG Act §2(2), (6)–(7)][ameg]; [Regulation §§1–3][amegreg]

ALS recipient liability starts at 16 and runs to statutory pension age. Payer liability has a different limb. Sections 7–8 address treaty-foreign social coverage, specified pension/adapted-work exemptions, benefit exclusions and foreign FAS categories. Temporary residence/work permits can support an application for up to one year at a time under §8(3), from receipt of the written application. Track the insured person's DKK 650,000 ceiling cumulatively across payers. Employer charges require their own base; do not transfer that personal limit to the employer. [ALS Act §§2, 7–9][als]

Parental recipient liability requires full Faroese tax liability, age at least 16 and below statutory pension age. The payer limb covers A-income paid in the Faroes, with §18's exclusions, including the specified pension/benefit and limited-tax-liability FAS income. Certain fully liable persons without a fixed Faroese home can apply for exemption from receipt of their application. Self-employed business income has a separate voluntary insurance route under §20, rather than automatically being the A-income charge. [Parental Act §§17–20][parental]

The occupational-disease contribution does not replace required work-injury insurance. Work Injury Act §79 distinguishes paid A-income for employers from prior-year taxable income for the self-employed. The wage-guarantee Act's foreign FAS exclusions and government-benefit payer exception must also be checked. [Work Injury Act §79][injury]; [Guarantee Act §7][guarantee]

### Mandatory pension and contribution tax

Pension Act §1 covers a fully tax-liable person below statutory pension age, subject to civil-service-pension, qualifying student-foreign-income and other express exceptions. Section 3 excludes listed pensions, support/insurance amounts and qualifying foreign-pension/NAV situations. Section 17 separately addresses persons born before 1 January 1954 and the approved legacy Danish-provider transition. Do not replace those tests with a blanket “all adults pay 12%”. [Pension Act §§1–3, 17][pension]

Compute eligible combined A/B income, the statutory minimum, qualifying contributions already made and the DKK 150,000 annual mandatory ceiling. A contract can fund or require more. The employer must transfer pension with salary through TAKS's withholding system; incompatible transfers can be rejected. B-income has its own payment/part-year rules. Eligible paid contributions have ordinary income deduction/exclusion under §12(3)–(4), while pension contribution tax is withheld under §12(2). Keep gross pension, contribution tax, credited savings and any insurance allocation separate. [Pension Act §§2, 12][pension]

Use the operative pension rule for the event, not the latest consolidation alone. The contribution rate is **12% throughout 2026**. Keep the following dated ledger. [Pension Act §2(1)][pension]; [payment Regulation 60/2021 §1][pensionreg]

| Period | Ordinary contribution / exemption method | Own official source |
|---|---|---|
| 1 January–27 February 2026 | The prior small-contribution rule excludes amounts **below DKK 30**, including B-income under the then §2(10). An A-income transfer of DKK 249 produces DKK 29.88 and is below that limit; DKK 250 produces DKK 30 and is not below. A temporary-job arrival could apply to TAKS for exemption for one or more periods, at most **60 months in total**. Use the actual approval and covered income; an intended short stay alone is insufficient. | [Act 78/2020 §1(2)](https://logir.fo/Logtingslog/78-fra-07-06-2020-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin-og-logtingslog-um-skatt); [Regulation 60/2021 §§1–3](https://logir.fo/Kunngerd/60-fra-05-05-2021-um-rindan-av-eftirlon-og-eftirlonarskatti); [original Pension Act §1(5)](https://logir.fo/GetFile/getpdf.aspx?objType=File&objId=12289) |
| From 28 February 2026 | Act 23/2026 changes the B-income small-contribution limit to **below DKK 500** while retaining **below DKK 30** for A-income. It replaces §1(5)'s temporary-job exemption with a departure-refund provision for a person whose aggregate Faroese stay was at most **60 months**; the new refund is not a payroll exemption. A repeat refund after returning has the separate **ten-year** condition in §1(6). Keep an existing exemption crossing this date separate from a new application. | [Act 23/2026 §1(2), (3), (6), §2, published 27 February](https://logir.fo/Logtingslog/23-fra-26-02-2026-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin) |
| Foreign-plan income, 1 January–27 February 2026 | Former §3(18) excludes qualifying foreign-employer income with NAV payments or a foreign pension arrangement TAKS regards as satisfactory. For the foreign-plan branch, original Regulation 52/2023 requires at least **75% for continuing payouts**, employer certification of the compulsory contractual plan, inability to choose a Faroese provider, and the application/evidence below. That original text contains no numeric 12% funding floor. Other income remains subject to the ordinary rules. | [Act 35/2021 §1(2)](https://logir.fo/Logtingslog/35-fra-26-03-2021-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin); [original Regulation 52/2023 §§1–4](https://logir.fo/GetFile/getpdf.aspx?objType=File&objId=38060) |
| Foreign-plan income, 28 February–24 August 2026 | New §3(17) additionally requires contributions, alone or together with Faroese contributions, at the level in §2(1), **12% in 2026**. Apply this statutory condition alongside the continuing-payout and approval/evidence conditions; the unchanged regulation does not postpone the Act. | [Act 23/2026 §1(12), §2](https://logir.fo/Logtingslog/23-fra-26-02-2026-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin); [original Regulation 52/2023 §§1–3](https://logir.fo/GetFile/getpdf.aspx?objType=File&objId=38060) |
| Foreign-plan income, from 25 August 2026 | Regulation 72/2026 expressly requires the **75%** continuing-payout test plus foreign contributions of at least **12% of foreign income**, or foreign/Faroese contributions together of at least **12% of total income**. Keep other income in the combined reconciliation. | [Regulation 72/2026 §§1–2, published 24 August](https://logir.fo/Kunngerd/72-fra-20-08-2026-um-broyting-i-kunngerd-um-undantak-eftir-eftirlonarlogini-fyri-personar-sum); [current Regulation 52/2023 §1](https://logir.fo/Kunngerd/52-fra-19-04-2023-um-undantak-eftir-eftirlonarlogini-fyri-personar-sum-arbeida-hja-utlendskum-arbeidsgevara) |

For the foreign-plan route, send the personal or collective application to TAKS by **1 May following the contribution year**, with employer certification and the pension contract; send the provider's electronic prior-year contribution statement with the return. Two separate claimant illustrations each assume no other income and isolate foreign employment income of **DKK 30,000** and a compulsory foreign contribution of **DKK 2,700**, with 75% continuing payouts, all other conditions satisfied and actual TAKS acceptance. For a January event the selected pre-amendment provisions do not impose the later numeric funding floor. For a March event, DKK 2,700 alone is below the DKK 3,600 statutory minimum; **DKK 900** of qualifying Faroese contribution brings the combined funding to 12%. This is a contribution reconciliation, not permission to assume approval or use another income's contribution twice. [Regulation 52/2023 §§1–3][foreign2023]; [Act 35/2021][pension2021]; [Act 23/2026][pensionfeb]

For an ordinary B-income-only person subject to contribution duty for part of 2026, §2(5) expressly reduces the annual mandatory contribution by **days without duty / 365**. First identify the actual duty dates and eligible annual B-income. With DKK 100,000 eligible B-income and 73 days without duty, DKK 12,000 × (365 − 73) / 365 gives **DKK 9,600**, before existing qualifying contributions and the applicable small-amount/cap checks. This statutory fraction does not establish a benefit-valuation or other scheme's fraction. The current ordinary B-income payment date is **1 November following the year**. A pre-28-February assessment versus later settlement of a B-income obligation needs its actual assessment history; do not manufacture a monthly B-income test or apply the new DKK 500 limit retroactively by assumption. [Pension Act §2(5)–(6), (10)][pension]

Act 86/2026, published 12 October and effective **13 October 2026**, adds the confirmed early/disability pension payout route after the statutory approval, with renumbering. It does not change the 12% contribution rate. Review payout-start/contribution-stop facts against the applicable date; do not calculate a withdrawal from the payroll contribution example. [Act 86/2026 §§1–2][pensionoct]

### Holiday pay and benefits

The ordinary earning year is 1 April–31 March, unless an agreed calendar year applies; full qualifying service gives 30 statutory days, proportionate for shorter service. Distinguish the 2 May–1 May leave year and the statutory continuous-leave period. Apply the correct cash-holiday-pay or paid-leave/supplement route. Wages paid during leave, holiday pay itself and holiday supplement are excluded from the statutory holiday calculation by §12; a collective agreement can give better terms. Taxable wage benefits enter under §13, with official valuation or the higher agreed value as specified. [Holiday Act §§1–13][holiday]

On monthly-paid departure, §11(2) requires holiday pay for outstanding entitlement using the statutory route; do not simply pay both 12% and 1.5% on the same basis. Current §20a places the holiday-pay account administration with TAKS through an approved settlement institution. The older linked Regulation 14/1987 still describes the former fund/accounts and cannot override the later statute abolishing that fund. Current operational details need the checks in Sources. [Holiday Act §§10–13, 20a–21][holiday]

### Ordinary benefit valuation

Tax Act §25 includes money's-worth benefits, subject to §29's express exemptions. Establish the actual benefit, private availability, coverage period, employer/employee funding and exemption evidence separately from cash wages. TAKS publishes these **2026** annual values, VAT included; meals have a daily value. Do not use a 2025 column or one flat percentage of car cost. [Tax Act §§25, 29][tax]; [TAKS annual valuations, 2026 column][values]

| Benefit | Published 2026 value in DKK | Official source |
|---|---|---|
| Free housing | 1,644 per square metre annually | [TAKS 2026 housing row](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/arligar-virdisasetingar-hja-taks) |
| Free electricity | 12,400 annually | [TAKS 2026 electricity row](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/arligar-virdisasetingar-hja-taks) |
| Free heat, oil/district heating | 31,500 annually | [TAKS 2026 heat row](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/arligar-virdisasetingar-hja-taks) |
| Free heat, electric/geothermal/other energy | 14,700 annually | [TAKS 2026 heat row](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/arligar-virdisasetingar-hja-taks) |
| Free meals | 47 / 61 / 81 per day for one / two / three meals | [TAKS 2026 meal rows](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/arligar-virdisasetingar-hja-taks) |
| Electric passenger car, including plug-in hybrid | 56,800 up to 1,300 kg; 65,900 at 1,301–1,500 kg; 79,700 at 1,501–1,700 kg; 86,000 from 1,701 kg | [TAKS 2026 electric-car rows](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/arligar-virdisasetingar-hja-taks) |
| Other passenger car, including non-plug-in hybrid | 62,400 up to 1,100 kg; 71,900 at 1,101–1,300 kg; 86,300 at 1,301–1,500 kg; 96,800 from 1,501 kg | [TAKS 2026 other-car rows](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/arligar-virdisasetingar-hja-taks) |
| Taxi up to ten persons | 23,000 annually | [TAKS 2026 taxi row](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/arligar-virdisasetingar-hja-taks) |
| Van/other vehicle | 60% of the corresponding electric/non-electric passenger-car value | [TAKS 2026 van row](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/arligar-virdisasetingar-hja-taks) |

The schedule supplies annual standard values. Apply these separate **TAKS administrative valuation methods**, using the current annual column with VLS D's benefit guidance:

- **Proved employee payment:** reduce the relevant benefit value by the amount the employee proves was paid **to the employer for use of the employer's asset**, with a floor of **zero**. Record the asset, actual payment and proof. A payroll deduction or employee expense is not automatically that payment. Thus a full-year DKK 56,800 car benefit with DKK 5,000 proved qualifying payment gives **DKK 51,800**; payment of DKK 60,000 gives **zero**, not a negative benefit.
- **Proved lower private car use:** VLS D states that the standard car value corresponds to **10,000 private kilometres annually**. If actual private use is proved or substantiated below that figure, reduce proportionately, with a clear private/business mileage split. With a DKK 56,800 annual car value, use `56,800 × proved private km / 10,000` within this below-10,000-km route. A worker provided that car only from July through December, with a complete log proving **4,000 private km** over the year and no employee payment, has **DKK 22,720** under this route. Six months alone does not establish DKK 28,400: this example uses proved mileage, not a six-twelfths or 365-day convention. Missing logs do not establish zero private use. This source does not supply an above-standard-mileage uplift or the ordering of combined mileage and employee-payment adjustments.

[VLS D, Fríir ágóðar and Koyribók][vlsd]; [TAKS 2026 car values][values]

For an ordinary exemption, employer-owned work computer/equipment and telephone made available in connection with work have the express §29 exclusions. Free travel and housing for a person resident abroad on temporary Faroese work require an aggregate stay **shorter than 180 days in a twelve-month period**, counting interrupted stays, and TAKS states that the benefit must be additional to wages rather than deducted from them. Test those facts before treating housing as exempt; 180 days is not shorter than 180. Faroese-home/foreign-work travel has its separate §29(27) route. [Tax Act §29(20), (22), (27)–(28)][tax]; [TAKS employer benefits][benefits]

Calendar-only part-year proration of annual housing, electricity and heat values, and the combined car-mileage/payment ordering, remain the precise valuation branches in Sources. Tax Act §29 contains work-computer/telecom and specified travel/accommodation exceptions; they are not universal benefit exclusions. TAKS requires both taxable benefits and exempt employee reimbursements to be reported on Vinnugluggin by **31 January following the year**, with the stated exceptional paper route. The employee reports corresponding information on the return. Reconcile the benefit schedule to the employer's records and employee statement rather than assuming noncash items pass through ordinary cash withholding automatically. [Tax Act §§25, 29, 118(1)(b)][tax]; [TAKS employer-benefits reporting][benefits]

## Deadlines and filing

| Obligation | Rule | Official source |
|---|---|---|
| A-income settlement/payslip | Before payment, use authorised settlement; provide statutory information and employee notice each payment | [Tax Act §63](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) |
| Employer AMEG invoice | Within 20 days after TAKS sends the invoice; alternative authorised debit route | [Regulation 45/2024 §2](https://logir.fo/Kunngerd/45-fra-21-05-2024-um-gjald-til-arbeidsmarknadareftirlonargrunn) |
| ALS invoice, 1 January–23 July 2026 | Previous §3: within seven days after invoice sent, with the DKK 100 invoice administration fee | [Pre-change regulation reproduced by ALS](https://www.als.fo/um-als/kunngerdir); [Regulation 69/2026 §§1–2](https://logir.fo/Kunngerd/69-fra-21-07-2026-um-broyting-i-kunngerd-um-ALSgjald) |
| ALS invoice, from 24 July 2026 | Current month plus seven working days after the invoice is sent, under the new §3(3)(2); DKK 100 per invoice | [Regulation 69/2026 §1(3), §2; publication 23 July](https://logir.fo/Kunngerd/69-fra-21-07-2026-um-broyting-i-kunngerd-um-ALSgjald); [current §3](https://logir.fo/Kunngerd/203-fra-18-12-2020-um-ALSgjald) |
| Parental contribution | Due when the liable person pays/receives A-income; settled before payout | [Parental Act §19](https://logir.fo/Logtingslog/48-fra-03-04-2001-um-barsilsskipan-sum-seinast-broytt-vid-logtingslog-nr-123-fra-22) |
| A-income pension | Transfer pension with salary through withholding system | [Pension Act §2(2)](https://logir.fo/Logtingslog/49-fra-14-05-2013-um-eftirlonarsamansparing-og-skatt-af-eftirlon-og-rentutryggingum) |
| B-income pension | By 1 November following the income year under the current rule; apply part-year reduction where required | [Pension Act §2(5)–(6)](https://logir.fo/Logtingslog/49-fra-14-05-2013-um-eftirlonarsamansparing-og-skatt-af-eftirlon-og-rentutryggingum) |
| Health Nordic exemption | Application by 1 May following the year; supporting evidence by the end of that following year | [Regulation 76/2024 §2](https://logir.fo/Kunngerd/76-fra-26-06-2024-um-undantoku-fyri-gjaldsskyldu-av-heilsutrygdargjaldi) |
| Annual wage/benefit information | By 31 January, with ledger reconciliation and current required forms/process | [Tax Act §118](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) |
| Holiday pay | Earned holiday pay is due with wages; remit through the current authorised TAKS route | [Holiday Act §§10, 20a](https://logir.fo/Logtingslog/30-fra-07-04-1986-um-fritid-vid-lon-sum-seinast-broytt-vid-logtingslog-nr-56) |

Keep the actual invoice/withholding dates and receipts; the AMEG and ALS invoice periods are different. Reconcile annual A-income, pensions, contributions, deductions, employer expense and the general ledger, including changes and leavers. Bookkeeping Act §§9–15 requires traceable corrections and safe records for five years from financial-year end, including after closure/management change. This is a retention duty, not permission to delete other records. [Bookkeeping Act][books]

## Penalties and interest

| Failure | Statutory consequence | Official source |
|---|---|---|
| Tax withholding/remittance or information failure | Tax Act §135 supplies 0.7% per commenced month for the stated late tax liabilities; intentional/grossly negligent failures have §§139–141 sanctions, with no invented fixed fine | [Tax Act §§129, 135, 139–141](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) |
| ALS late contribution | 1% per commenced month; statutory recovery applies | [ALS Act §9(3)](https://logir.fo/Logtingslog/113-fra-13-06-1997-um-arbeidsloysistrygging-og-arbeidsavising-sum-seinast-broytt-vid-logtingslog-nr-79) |
| Employer AMEG late contribution | 0.7% per commenced month, including booked interest as specified | [AMEG Act §2(4)](https://logir.fo/Logtingslog/39-fra-07-05-1991-um-arbeidsmarknadareftirlonargrunn-sum-seinast-broytt-vid-logtingslog-nr149-fra-20-desember) |
| Health late contribution | 0.7% per commenced month, including booked interest as specified; incorrect exemption can be recovered | [Health Act §§24(4), 26](https://logir.fo/Logtingslog/178-fra-22-12-2009-um-almenna-heilsutrygd-sum-seinast-broytt-vid-logtingslog-nr-129-fra) |
| Occupational-disease late contribution | 0.7% per commenced month including booked interest as specified | [Work Injury Act §79(4)](https://logir.fo/Logtingslog/67-fra-25-05-2009-um-trygging-moti-avleidingunum-av-arbeidsskada-sum-broytt-vid-logtingslog-nr) |
| Guarantee-fund late contribution | 0.7% per commenced month from due date, with statutory fine liability for specified failure to pay/provide information | [Guarantee Act §§7(4), 11](https://logir.fo/Logtingslog/68-fra-09-06-1988-um-trygdargrunn-fyri-avreidingar-og-lonir-vm-sum-seinast-broytt-vid) |
| Late holiday pay | 1.5% per commenced month from the due date | [Holiday Act §16](https://logir.fo/Logtingslog/30-fra-07-04-1986-um-fritid-vid-lon-sum-seinast-broytt-vid-logtingslog-nr-56) |
| Unjustified failure to pay holiday amounts / prohibited waiver | Fine; legal-person liability as specified | [Holiday Act §22](https://logir.fo/Logtingslog/30-fra-07-04-1986-um-fritid-vid-lon-sum-seinast-broytt-vid-logtingslog-nr-56) |

Pension Act §16's DKK 20,000 daily provisions concern the specified provider reporting/administrative breaches, not a universal employee or employer late-pension fine. Unpaid pension/tax has the separate recovery provisions in §§2, 12. Assess the actual liable party and breach before applying any penalty. [Pension Act §§2, 6, 12, 16][pension]

## Cross-border points

Keep work-country, residence, treaty social-security coverage, FAS/bareboat status, payer, contract and exemption decisions together. Tax residence does not settle every social contribution. ALS's treaty-foreign coverage exception, Health's application regime, AMEG's FAS exceptions and mandatory pension's full-liability/foreign-plan conditions differ. A foreign or temporary worker is not automatically outside all schemes. [ALS Act §§7–8][als]; [Health Act §24][health]; [AMEG Act §2][ameg]; [Pension Act §§1–3][pension]

Foreign-employer non-A wages can fall within ALS §2's domestic-work or Nordic-coverage routes. Ordinary wage income tax and foreign-tax/treaty relief remain in the personal/cross-border Guides; do not substitute the contribution percentage for the income-tax result. [ALS Act §2][als]; [Tax Act §§1–2, 60–66][tax]

## Two worked examples that recompute

### 1. Ordinary salary and employer-funded pension

Assume a fully liable 30-year-old resident with no exemption. A normal non-leave month's A-income and each statutory taxable-income base used here are independently established at DKK 30,000. The contract adds an employer-funded gross pension of DKK 3,600, outside that cash wage; assume the pension follows the 12% minimum and 40% provisional pension-tax route. Worker Health is DKK 385, AMEG DKK 900, parental DKK 258 and ALS DKK 180, totalling DKK 1,723. Employer AMEG/parental/ALS/occupational-disease/guarantee charges total DKK 1,413. Pension tax is DKK 1,440, leaving DKK 2,160 credited before any permitted insurance allocation. The statutory 1.5% holiday-supplement accrual on this eligible salary is DKK 450. Selected labour expense is DKK 35,463. This excludes wage income tax, broadcasting, other insurance and any later charges on holiday payouts; it is not a full net-pay calculation. [Health §24][health]; [AMEG §2][ameg]; [Parental §19][parental]; [ALS regulation §1][alsreg]; [Work Injury §79][injury]; [TAKS guarantee rate][employer]; [Pension §§2, 12][pension]; [Holiday §§11–12][holiday]

```oa-check
name: Faroese salary component bases and separate employer pension
inputs:
  base: 30000
  employer_funded_pension: 3600
steps:
  health: 175 + base * 0.007
  worker_ameg: base * 0.03
  worker_parental: base * 0.0086
  worker_als: base * 0.006
  worker_selected_charges: health + worker_ameg + worker_parental + worker_als
  employer_ameg: base * 0.03
  employer_parental: base * 0.0086
  employer_als: base * 0.006
  employer_injury: base * 0.0005
  employer_guarantee: base * 0.002
  employer_charges: employer_ameg + employer_parental + employer_als + employer_injury + employer_guarantee
  provisional_pension_tax: employer_funded_pension * 0.40
  pension_credited: employer_funded_pension - provisional_pension_tax
  holiday_accrual: base * 0.015
  selected_labour_expense: base + employer_funded_pension + employer_charges + holiday_accrual
expected:
  health: 385
  worker_selected_charges: 1723
  employer_charges: 1413
  provisional_pension_tax: 1440
  pension_credited: 2160
  holiday_accrual: 450
  selected_labour_expense: 35463
```

### 2. Annual limits belong to different schemes

Assume a fully eligible worker's annual ALS income is DKK 700,000 and no other payer has used the limit. Employee ALS is 0.6% of DKK 650,000, or DKK 3,900. The employer's independently established liable wage base is DKK 700,000, giving DKK 4,200; the personal cap is not duplicated for the employer. Separately, assume an individual's eligible annual pension base is DKK 1,500,000 and no contribution has yet been credited. Twelve percent is DKK 180,000, but the mandatory gross ceiling is DKK 150,000. If paid at a verified 40% final pension-tax rate, tax is DKK 60,000 and credited pension DKK 90,000 before insurance allocation. The DKK 30,000 excess is outside the statutory minimum, not an automatically permitted unpaid contractual contribution. These are two independent limit checks; no total net pay is claimed. [ALS Act §8(2)][als]; [ALS regulation §1][alsreg]; [Pension Act §2(4), §12 and annex 1][pension]

```oa-check
name: Faroese personal ALS ceiling and separate annual pension ceiling
inputs:
  worker_als_income: 700000
  employer_als_base: 700000
  als_ceiling: 650000
  als_rate: 0.006
  pension_base: 1500000
  pension_rate: 0.12
  mandatory_pension_cap: 150000
steps:
  worker_als: min(worker_als_income, als_ceiling) * als_rate
  employer_als: employer_als_base * als_rate
  unbounded_pension: pension_base * pension_rate
  mandatory_pension: min(unbounded_pension, mandatory_pension_cap)
  outside_mandatory_minimum: unbounded_pension - mandatory_pension
  pension_tax: mandatory_pension * 0.40
  pension_credited: mandatory_pension - pension_tax
expected:
  worker_als: 3900
  employer_als: 4200
  unbounded_pension: 180000
  mandatory_pension: 150000
  outside_mandatory_minimum: 30000
  pension_tax: 60000
  pension_credited: 90000
```

## Ask the client first

- What are the employee's date of birth, residence/full-liability dates, work countries and social-coverage or FAS evidence?
- What are gross pay, benefits, A/B classification and the contract's pension/holiday funding terms?
- Which contribution bases, annual totals and other payers affect caps, and what pension payments already exist?
- What exemptions, foreign-pension approvals, temporary permits or provider decisions apply, with dates?
- What payments, leaver/leave events and invoice-send dates fall before or after the 2026 changes?
- What withholding statements, payslips, account records, annual information filings and receipts support reconciliation?

## Sources

| Source | Provisions / purpose | Read on |
|---|---|---|
| [Current Tax Act](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) | §§25, 29, 57, 60–66, 118, 135, 139–141; classification, settlement, payslip, information and sanctions | 2026-10-25 |
| [Pension Act](https://logir.fo/Logtingslog/49-fra-14-05-2013-um-eftirlonarsamansparing-og-skatt-af-eftirlon-og-rentutryggingum) | §§1–3, 6, 12, 16–17, annex 1; liability, base, funding, tax, limits | 2026-10-25 |
| [Act 23/2026](https://logir.fo/Logtingslog/23-fra-26-02-2026-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin) | §§1–2; February changes and publication/effect | 2026-10-25 |
| [Act 86/2026](https://logir.fo/Logtingslog/86-fra-09-10-2026-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin) | §§1–2; October payout changes and publication/effect | 2026-10-25 |
| [Regulation 72/2026](https://logir.fo/Kunngerd/72-fra-20-08-2026-um-broyting-i-kunngerd-um-undantak-eftir-eftirlonarlogini-fyri-personar-sum) | §§1–2; August foreign-pension condition and publication/effect | 2026-10-25 |
| [AMEG Act](https://logir.fo/Logtingslog/39-fra-07-05-1991-um-arbeidsmarknadareftirlonargrunn-sum-seinast-broytt-vid-logtingslog-nr149-fra-20-desember) | §2; separate employee/employer contributions and exceptions | 2026-10-25 |
| [Regulation 45/2024](https://logir.fo/Kunngerd/45-fra-21-05-2024-um-gjald-til-arbeidsmarknadareftirlonargrunn) | §§1–5; pension-age year, FAS, invoice, assessment | 2026-10-25 |
| [Health Act](https://logir.fo/Logtingslog/178-fra-22-12-2009-um-almenna-heilsutrygd-sum-seinast-broytt-vid-logtingslog-nr-129-fra) | §§1, 24–26; coverage, rate, exemption and interest | 2026-10-25 |
| [Regulation 76/2024](https://logir.fo/Kunngerd/76-fra-26-06-2024-um-undantoku-fyri-gjaldsskyldu-av-heilsutrygdargjaldi) | §§1–4; Nordic exemption, dates and partial-year method | 2026-10-25 |
| [ALS Act](https://logir.fo/Logtingslog/113-fra-13-06-1997-um-arbeidsloysistrygging-og-arbeidsavising-sum-seinast-broytt-vid-logtingslog-nr-79) | §§2, 7–9; bases, persons, exclusions, cap and interest | 2026-10-25 |
| [Current ALS regulation 203/2020](https://logir.fo/Kunngerd/203-fra-18-12-2020-um-ALSgjald) | §§1–3; rate and current invoice route | 2026-10-25 |
| [Regulation 69/2026](https://logir.fo/Kunngerd/69-fra-21-07-2026-um-broyting-i-kunngerd-um-ALSgjald) | §§1–2; July procedure change, publication/effect | 2026-10-25 |
| [ALS pre-change regulation reproduction](https://www.als.fo/um-als/kunngerdir) | Previous seven-day invoice text, compared with enacted amendment | 2026-10-25 |
| [ALS 2026 rate/cap notice](https://www.als.fo/fo/um-als/tidindi/als-gjaldid-laekkadi-1-januar-1) | Cross-check personal DKK 3,900 ceiling | 2026-10-25 |
| [Parental Act](https://logir.fo/Logtingslog/48-fra-03-04-2001-um-barsilsskipan-sum-seinast-broytt-vid-logtingslog-nr-123-fra-22) | §§17–20; persons, base, rate and collection | 2026-10-25 |
| [Work Injury Act](https://logir.fo/Logtingslog/67-fra-25-05-2009-um-trygging-moti-avleidingunum-av-arbeidsskada-sum-broytt-vid-logtingslog-nr) | §79; employer/self-employed bases and rate | 2026-10-25 |
| [Guarantee Act](https://logir.fo/Logtingslog/68-fra-09-06-1988-um-trygdargrunn-fyri-avreidingar-og-lonir-vm-sum-seinast-broytt-vid) | §§7, 11; ceiling, exclusions, collection and sanction | 2026-10-25 |
| [Holiday Act](https://logir.fo/Logtingslog/30-fra-07-04-1986-um-fritid-vid-lon-sum-seinast-broytt-vid-logtingslog-nr-56) | §§1–13, 16, 20a–22; entitlement, bases, late-payment interest and current administration | 2026-10-25 |
| [Bookkeeping Act](https://logir.fo/Logtingslog/23-fra-20-03-2018-um-bokhald) | §§9–15; traceability and retention | 2026-10-25 |
| [TAKS 2026 employer table](https://www.taks.fo/fo/vinna/studul/almenn-gjoeld-hja-arbeidsgevarum) | Published employer rates, including operating guarantee rate | 2026-10-25 |
| [TAKS annual valuations](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/arligar-virdisasetingar-hja-taks) | Actual 2026 column; ordinary housing, utilities, meals and vehicle values | 2026-10-25 |
| [TAKS employer-benefits reporting](https://www.taks.fo/fo/vinna/skattur/friir-agodar-og-skattafriar-veitingar-til-starvsfolk) | Annual employer/employee reporting and exceptional paper route | 2026-10-25 |
| [TAKS employer broadcasting](https://www.taks.fo/fo/vinna/skattur/kringvarpsgjald) | Separate annual prior-year payroll invoice | 2026-10-25 |
| [TAKS VLS D](https://www.taks.fo/fo/log/vegleidingarskriv-vls-2015/d-skattskyldug-inntoeka-hja-loentakararum) | Fríir ágóðar / Koyribók: proved payment, zero floor and private-mileage method; current-hosted administrative guidance, not a new 2026 enactment | 2026-10-28 |
| [Original Pension Act](https://logir.fo/GetFile/getpdf.aspx?objType=File&objId=12289); [Acts 78/2020 and 35/2021](https://logir.fo/Logtingslog/78-fra-07-06-2020-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin-og-logtingslog-um-skatt) [pension2021]; [Regulation 60/2021](https://logir.fo/Kunngerd/60-fra-05-05-2021-um-rindan-av-eftirlon-og-eftirlonarskatti) | Selected earlier operative provisions, not the superseded original rate table | 2026-10-28 |
| [Original and current Regulation 52/2023](https://logir.fo/GetFile/getpdf.aspx?objType=File&objId=38060) [foreign2023] | §§1–4 and actual 2023 gazette; February statutory overlay and August amendment read separately | 2026-10-28 |
| [Current contribution laws, 2026 values and employer guidance](https://www.taks.fo/fo/vinna/studul/almenn-gjoeld-hja-arbeidsgevarum) | Rate/payer, selected base, penalty and deadline provisions re-read; full rule/figure receipts in the research ledger | 2026-10-28 |

Not yet confirmed: calendar-only part-year annual housing/electricity/heat valuation, combined car-mileage/employee-payment ordering and full exemption execution; treatment after 28 February of an already approved temporary-stay exemption and the assessment/settlement cutover for old B-income small-payment obligations; guarantee-fund operative regulation and exact invoice calendar, parental/occupational-disease invoice implementation, detailed current holiday transmission/benefit reconciliation, unusual contribution-base/rounding cases and zero-income pension-tax annex treatment. Private broadcasting rates/age assessment and full special-worker/foreign-coverage procedures require their own review. Those are real gaps; payroll/social-contribution domains remain partial. Independent whole-pack AI review accepted this material for partial tier-2 draft publication on 25 October 2026. Professional attestation remains pending.

[tax]: https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt
[pension]: https://logir.fo/Logtingslog/49-fra-14-05-2013-um-eftirlonarsamansparing-og-skatt-af-eftirlon-og-rentutryggingum
[pensionfeb]: https://logir.fo/Logtingslog/23-fra-26-02-2026-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin
[pensionoct]: https://logir.fo/Logtingslog/86-fra-09-10-2026-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin
[foreignaug]: https://logir.fo/Kunngerd/72-fra-20-08-2026-um-broyting-i-kunngerd-um-undantak-eftir-eftirlonarlogini-fyri-personar-sum
[ameg]: https://logir.fo/Logtingslog/39-fra-07-05-1991-um-arbeidsmarknadareftirlonargrunn-sum-seinast-broytt-vid-logtingslog-nr149-fra-20-desember
[amegreg]: https://logir.fo/Kunngerd/45-fra-21-05-2024-um-gjald-til-arbeidsmarknadareftirlonargrunn
[health]: https://logir.fo/Logtingslog/178-fra-22-12-2009-um-almenna-heilsutrygd-sum-seinast-broytt-vid-logtingslog-nr-129-fra
[healthreg]: https://logir.fo/Kunngerd/76-fra-26-06-2024-um-undantoku-fyri-gjaldsskyldu-av-heilsutrygdargjaldi
[als]: https://logir.fo/Logtingslog/113-fra-13-06-1997-um-arbeidsloysistrygging-og-arbeidsavising-sum-seinast-broytt-vid-logtingslog-nr-79
[alsreg]: https://logir.fo/Kunngerd/203-fra-18-12-2020-um-ALSgjald
[alsjuly]: https://logir.fo/Kunngerd/69-fra-21-07-2026-um-broyting-i-kunngerd-um-ALSgjald
[alsold]: https://www.als.fo/um-als/kunngerdir
[alsnotice]: https://www.als.fo/fo/um-als/tidindi/als-gjaldid-laekkadi-1-januar-1
[parental]: https://logir.fo/Logtingslog/48-fra-03-04-2001-um-barsilsskipan-sum-seinast-broytt-vid-logtingslog-nr-123-fra-22
[injury]: https://logir.fo/Logtingslog/67-fra-25-05-2009-um-trygging-moti-avleidingunum-av-arbeidsskada-sum-broytt-vid-logtingslog-nr
[guarantee]: https://logir.fo/Logtingslog/68-fra-09-06-1988-um-trygdargrunn-fyri-avreidingar-og-lonir-vm-sum-seinast-broytt-vid
[holiday]: https://logir.fo/Logtingslog/30-fra-07-04-1986-um-fritid-vid-lon-sum-seinast-broytt-vid-logtingslog-nr-56
[books]: https://logir.fo/Logtingslog/23-fra-20-03-2018-um-bokhald
[employer]: https://www.taks.fo/fo/vinna/studul/almenn-gjoeld-hja-arbeidsgevarum
[broadcast]: https://www.taks.fo/fo/vinna/skattur/kringvarpsgjald
[values]: https://www.taks.fo/fo/borgari/gjoeld-og-agodar/arligar-virdisasetingar-hja-taks
[benefits]: https://www.taks.fo/fo/vinna/skattur/friir-agodar-og-skattafriar-veitingar-til-starvsfolk

[vlsd]: https://www.taks.fo/fo/log/vegleidingarskriv-vls-2015/d-skattskyldug-inntoeka-hja-loentakararum
[pensionoriginal]: https://logir.fo/GetFile/getpdf.aspx?objType=File&objId=12289
[pension2020]: https://logir.fo/Logtingslog/78-fra-07-06-2020-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin-og-logtingslog-um-skatt
[pension2021]: https://logir.fo/Logtingslog/35-fra-26-03-2021-um-broyting-i-logtingslog-um-eftirlon-Eftirlonarlogin
[pensionreg]: https://logir.fo/Kunngerd/60-fra-05-05-2021-um-rindan-av-eftirlon-og-eftirlonarskatti
[foreignoriginal]: https://logir.fo/GetFile/getpdf.aspx?objType=File&objId=38060
[foreign2023]: https://logir.fo/Kunngerd/52-fra-19-04-2023-um-undantak-eftir-eftirlonarlogini-fyri-personar-sum-arbeida-hja-utlendskum-arbeidsgevara

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
