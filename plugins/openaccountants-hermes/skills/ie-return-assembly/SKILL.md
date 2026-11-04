---
name: ie-return-assembly
description: "Use this skill last, to put together an Irish individual's income tax return for tax year 2026 from the work done in the other Ireland skills. It decides Form 11 or Form 12, lists the 2026 figures each part uses (rate bands EUR 44,000 single and EUR 53,000 married at 20%, then 40%; main credits EUR 2,000; USC bands to 8%; PRSI Class S at 4.2375%; CGT 33% or 31% by disposal date), adds income tax, USC and PRSI, takes off PAYE and preliminary tax, and sets out the pay and file dates (31 October 2027 for the 2026 Form 11), the late filing surcharge and interest. Trigger on: assemble Irish return, Form 11 2026, Form 12 2026, ROS pay and file, Statement of Liability, balance due Ireland. Out of scope: companies and CT1 (ie-corporation-tax), VAT (ireland-vat-return), CAT (ie-cat)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ie-return-assembly"
  jurisdiction: "IE"
  tax_year: "2026"
  last_updated: "2026-10-27"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Ireland: assembling the 2026 individual tax return (Form 11 and Form 12), v1.2

Built by Michael Cutajar and the OpenAccountants team. Source-cited draft: not reviewed by an accountant.

This skill is the last step for an individual's Irish return for tax year 2026. The tax year is the calendar year. The authority is the Revenue Commissioners. It does not redo the work of the other skills. It takes their results, checks that they fit together, adds them up, and produces a working paper, the amount to pay and the dates. It does not file anything: the taxpayer or their agent files on ROS or myAccount.

The detail lives in these skills. Read them first and link to them; do not copy their rules here.

| Part of the return | Skill |
|---|---|
| Trading income, rates, bands, credits, Form 11 panels | [ie-income-tax-form11](ie-income-tax-form11.md) |
| PAYE workers with side income (Form 12), rental income (Case V), non-residents | [ie-paye-rental-nonresident](ie-paye-rental-nonresident.md) |
| Universal Social Charge | [ie-usc](ie-usc.md) |
| PRSI for the self-employed (Class S) | [ie-prsi-class-s](ie-prsi-class-s.md) |
| Capital gains tax | [ie-cgt](ie-cgt.md) |
| Preliminary tax | [ie-preliminary-tax](ie-preliminary-tax.md) |
| Non-domiciled individuals, remittance basis | [ie-non-dom](ie-non-dom.md) |
| Arriving, leaving, SARP, treaties | [ie-cross-border](ie-cross-border.md), [ie-foreign-tax-and-withholding](ie-foreign-tax-and-withholding.md) |
| Companies (CT1) | [ie-corporation-tax](ie-corporation-tax.md) |

## Who this applies to

- **Individuals filing for tax year 2026.** Self-employed people, proprietary directors, landlords, and employees or pensioners with income or gains that PAYE has not dealt with.
- **Form 11 or Form 12.** A person must file Form 11 if they are in self-assessment, are a proprietary director (or the jointly assessed spouse or civil partner of one), or their taxable non-PAYE income is more than EUR 5,000 a year, or their gross non-PAYE income is more than EUR 30,000. A PAYE worker whose taxable non-PAYE income is EUR 5,000 or less (gross EUR 30,000 or less), and who asks Revenue to collect the tax by reducing credits and rate band, files Form 12 ([Revenue: do you need to submit a tax return?](https://www.revenue.ie/en/jobs-and-pensions/end-of-year-process/need-to-submit-a-tax-return.aspx)). Detail: [ie-paye-rental-nonresident](ie-paye-rental-nonresident.md).
- **Capital gains.** A PAYE worker with a gain reports it on the paper Form 12 or on Form CG1; CGT cannot be reported on the online eForm 12. A Form 11 filer reports it on Form 11 ([Revenue: when and how do you pay and file CGT](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx)).
- **Out of scope here.** Companies (CT1: [ie-corporation-tax](ie-corporation-tax.md)), VAT returns ([ireland-vat-return](ireland-vat-return.md)), gift and inheritance tax ([ie-cat](ie-cat.md)), trusts and estates (Form 1). Refer those.

## Rates, bands and thresholds

The figures the assembled return uses for 2026. Each upstream skill has the full table and the conditions.

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Standard rate band, single or widowed, no qualifying child | EUR 44,000 at 20%, balance at 40% | 2026 | [Revenue: tax rates, bands and reliefs](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx) |
| Standard rate band, single with Single Person Child Carer Credit | EUR 48,000 at 20%, balance at 40% | 2026 | same |
| Standard rate band, married or civil partners, one income | EUR 53,000 at 20%, balance at 40% | 2026 | same |
| Standard rate band, married or civil partners, two incomes | EUR 53,000 plus the lower of EUR 35,000 or the lower earner's income | 2026 | same |
| Single Person credit / Married Person or Civil Partner credit | EUR 2,000 / EUR 4,000 | 2026 | same |
| Employee (PAYE) credit / Earned Income credit (maximum) | EUR 2,000 / EUR 2,000 | 2026 | same |
| USC: first EUR 12,012 / next EUR 16,688 / next EUR 41,344 / balance | 0.5% / 2% / 3% / 8% | 2026 | [Revenue: USC standard rates](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx) |
| USC exemption limit (total income above it: USC on all of it) | EUR 13,000 | 2026 | [Revenue: USC](https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx) |
| USC surcharge on non-PAYE income over EUR 100,000 | 3% | 2026 | [Revenue: other USC rates](https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx) |
| PRSI Class S, rate on 2026 income returned through self-assessment | 4.2375%, minimum EUR 650 | 2026 | [DSP: Class S rates](https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/) |
| PRSI Class S, weekly rate (directors paying through PAYE) | 4.20% to 30 September 2026; 4.35% from 1 October 2026 | 2026 | same |
| CGT, most gains | 33% on disposals to 6 October 2026; 31% from 7 October 2026 (provisional); development land 33% | 2026 | [Revenue: how to calculate CGT](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx) |
| CGT personal exemption | EUR 1,270 | 2026 | [Revenue: what is exempt from CGT](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx) |
| Form 12 limit on non-PAYE income | Taxable EUR 5,000 or less and gross EUR 30,000 or less | 2026 | [Revenue: do you need to submit a tax return?](https://www.revenue.ie/en/jobs-and-pensions/end-of-year-process/need-to-submit-a-tax-return.aspx) |
| Preliminary tax: the lowest of | 90% of the current year, 100% of the previous year, or 105% of the pre-preceding year (direct debit only) | 2026 and 2027 | [Revenue: preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx) |

The 31% CGT rate comes from Financial Resolution No. 3 of 6 October 2026 and is provisional until the Finance (No. 2) Act 2026 is in force. [ie-cgt](ie-cgt.md) explains when it would lapse. In a year with gains at 33% and 31%, the EUR 1,270 exemption comes off the 33% gains first (section 601(3), [section 601](https://www.irishstatutebook.ie/eli/1997/act/39/section/601/enacted/en/html)). Budget 2027 changes announced on 6 October 2026 do not change the 2026 bands, credits, USC or PRSI above.

## The taxable base

Build the working paper in this order. Each line comes from the skill named.

1. **Income by source.** Trading profit (Case I and II) after adjustments and capital allowances ([ie-income-tax-form11](ie-income-tax-form11.md)); employment income and PAYE deducted from the year-end employment detail summary; net rent (Case V) and other non-PAYE income ([ie-paye-rental-nonresident](ie-paye-rental-nonresident.md)); foreign income ([ie-non-dom](ie-non-dom.md) for the remittance basis, [ie-foreign-tax-and-withholding](ie-foreign-tax-and-withholding.md) for credits).
2. **Income tax.** Apply the band for the person's status at 20% and the balance at 40%, then subtract credits. Credits reduce tax; they are not deductions from income. The Earned Income credit is the lower of EUR 2,000 or 20% of earned income, and with the Employee credit cannot exceed EUR 2,000 in total ([Revenue: Earned Income Credit](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx)).
3. **USC.** On total income, a different base from income tax. Use [ie-usc](ie-usc.md) for exempt income, reduced rates and the surcharge.
4. **PRSI.** Class S on reckonable self-employed income of EUR 5,000 or more ("Self-employed contributors with annual income of €5,000 or over pay Class S PRSI", [DSP SW14](https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf); detail in [ie-prsi-class-s](ie-prsi-class-s.md)). Employees' PRSI on pay is already deducted through payroll.
5. **Capital gains.** A separate computation with its own payment dates ([ie-cgt](ie-cgt.md)). It goes on the same Form 11 or paper Form 12, but the CGT is paid on the CGT dates, not with the income tax balance.
6. **Credits for tax paid.** Subtract PAYE and USC deducted through payroll, professional services withholding tax, and preliminary tax paid for 2026. What is left is the 2026 balance.
7. **Preliminary tax for the next year.** Form 11 filers pay preliminary tax for 2027 with the 2026 balance ([ie-preliminary-tax](ie-preliminary-tax.md)).

Checks before the paper goes to review: the trading turnover agrees with the VAT returns for the year, allowing for timing and exempt sales; the PAYE figures agree with the employment detail summary in myAccount; and every credit claimed has its certificate or statement. Flag any difference of more than EUR 1 rather than rounding it away.

## Deadlines and filing

| What | Date | Source |
|---|---|---|
| File the 2026 Form 11, pay the 2026 balance and 2027 preliminary tax | 31 October 2027 | [Revenue: pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx) |
| ROS pay and file extension for the 2026 return | Not yet announced. For the 2025 return it was 18 November 2026, only where both the return and the payment go through ROS | [eBrief 034/26](https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx) |
| Preliminary tax for 2026 (already due) | 31 October 2026, or 18 November 2026 through ROS | [Revenue: pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx) |
| Form 12 for 2026 | Within four years after the end of 2026. Done in myAccount: request the Statement of Liability, then complete the return | [Revenue: PAYE Income Tax Return](https://www.revenue.ie/en/jobs-and-pensions/end-of-year-process/paye-income-tax-return.aspx) |
| CGT on disposals 1 January to 30 November 2026 | Pay by 15 December 2026 | [Revenue: CGT pay and file](https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx) |
| CGT on disposals 1 to 31 December 2026 | Pay by 31 January 2027 | same |
| CGT return for 2026 disposals | 31 October 2027 | same |

Most people filing Form 11 must do so through ROS ([Revenue: do you need to submit a tax return?](https://www.revenue.ie/en/jobs-and-pensions/end-of-year-process/need-to-submit-a-tax-return.aspx)). Keep the ROS acknowledgement.

How filing and paying on ROS works ([Revenue, Guide to Completing 2025 Pay and File Self-Assessment Returns, pages 7 to 8 and 10](https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf); the 2026 guide is not yet published):

- **Registering.** A taxpayer filing their own return registers for ROS in three steps: apply for a ROS Access Number (RAN), apply for a digital certificate using the RAN, then download and save the certificate with a login password.
- **Agents.** An agent files through ROS under its TAIN and must have the client linked on the TAIN Services page. Linking a new client can take 2 to 3 working days, so do it before the deadline week.
- **Paying.** ROS takes payment by ROS Debit Instruction, online banking, or debit or credit card. The return can be filed early with a payment date chosen up to the filing date.
- **Attachments.** Do not send supporting documents with the return unless Revenue asks. Keep them for six years for an assurance check or audit.

## Penalties and interest

| Item | Amount | Source |
|---|---|---|
| Return filed less than two months after the deadline | Surcharge of 5% of the tax due, up to EUR 12,695 | [Revenue: pay and file](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx) |
| Return filed more than two months after the deadline | Surcharge of 10% of the tax due, up to EUR 63,485 | same |
| Local Property Tax obligations not met | A 10% surcharge can apply to the final liability, even if the return is on time | same |
| Late payment of income tax or CGT | Interest of 0.0219% per day | [Revenue: guidelines for charging interest on late payment](https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf) |

The surcharge is for late filing and applies even where the tax is paid. Revenue charges interest where preliminary tax is underpaid, for each day or part of a day past the deadline ([Revenue: preliminary tax](https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx); detail in [ie-preliminary-tax](ie-preliminary-tax.md)).

## Cross-border points

- **Non-residents** with Irish income: what is taxed, the section 1032 credits and the 75% test are in [ie-paye-rental-nonresident](ie-paye-rental-nonresident.md). Rent paid to a non-resident landlord has 20% withheld by the tenant; that skill covers how it is reported.
- **Arriving or leaving in 2026**: residence, split-year treatment for employment income and SARP are in [ie-cross-border](ie-cross-border.md). Assemble the return only after that skill fixes residence for 2026.
- **Not domiciled in Ireland**: foreign income and foreign gains on the remittance basis ([ie-non-dom](ie-non-dom.md)). Report only the amounts brought into Ireland.
- **Foreign tax paid**: the credit and treaty rates are in [ie-foreign-tax-and-withholding](ie-foreign-tax-and-withholding.md). Without the foreign tax statement, leave the credit out and flag it.

Refer treaty tie-breaker cases and dual-resident years.

## Worked examples

### Example 1: sole trader, Form 11 for 2026

Aoife is single, resident and Irish domiciled, with no children. Her adjusted trading profit for 2026 is EUR 60,000. She has no other income. She paid EUR 14,000 preliminary tax for 2026 on 31 October 2026.

- Income tax: EUR 44,000 at 20% is EUR 8,800. EUR 16,000 at 40% is EUR 6,400. Gross EUR 15,200, less the Single Person credit EUR 2,000 and the Earned Income credit EUR 2,000: EUR 11,200.
- USC: EUR 12,012 at 0.5% is EUR 60.06. EUR 16,688 at 2% is EUR 333.76. The rest, EUR 31,300, at 3% is EUR 939.00. Total EUR 1,332.82.
- PRSI Class S at 4.2375%: EUR 2,542.50. That is above the EUR 650 minimum.
- Total for 2026: EUR 15,075.32. Less preliminary tax paid, EUR 14,000: balance EUR 1,075.32, due with the Form 11 by 31 October 2027.
- Preliminary tax for 2027 is due the same day. On the 100% test it is EUR 15,075.32.

```oa-check
name: Single sole trader, profit EUR 60,000, Form 11 for 2026
inputs:
  profit: 60000
  band: 44000
  credits: 4000
  prelim_paid: 14000
steps:
  - income_tax: band * 0.20 + (profit - band) * 0.40 - credits
  - usc: 12012 * 0.005 + 16688 * 0.02 + (profit - 12012 - 16688) * 0.03
  - prsi: profit * 0.042375
  - total: income_tax + usc + prsi
  - balance: total - prelim_paid
expected:
  income_tax: 11200.00
  usc: 1332.82
  prsi: 2542.50
  total: 15075.32
  balance: 1075.32
```

### Example 2: employee with share sales either side of 7 October 2026

Ciarán is a PAYE employee. Payroll has dealt with his salary in full. He sold listed shares twice in 2026: on 15 September, a gain of EUR 6,000, and on 10 November, a gain of EUR 10,000. He has no losses. He has no other non-PAYE income, so he stays on Form 12.

- The September gain is before 7 October 2026, so 33% applies. The November gain is after, so 31% applies ([ie-cgt](ie-cgt.md)).
- The EUR 1,270 exemption comes off the 33% gain: where gains are taxed at more than one rate, section 601(3) gives the exemption against the gains at the higher rate first ([section 601](https://www.irishstatutebook.ie/eli/1997/act/39/section/601/enacted/en/html)).
- CGT: (EUR 6,000 less EUR 1,270) at 33% is EUR 1,560.90. EUR 10,000 at 31% is EUR 3,100.00. Total EUR 4,660.90.
- Both disposals are in the 1 January to 30 November period, so the whole EUR 4,660.90 is due by 15 December 2026.
- He reports the gains on the paper Form 12 or on Form CG1 by 31 October 2027, not on the online eForm 12.
- If the 31% resolution lapses before the Finance (No. 2) Act 2026 is in force, the November gain goes back to 33%, and the CGT on it rises to EUR 3,300.00.

```oa-check
name: Two 2026 share gains either side of 7 October 2026, exemption against the 33% gain (section 601(3))
inputs:
  gain_before: 6000
  gain_after: 10000
  exemption: 1270
steps:
  - cgt_33: (gain_before - exemption) * 0.33
  - cgt_31: gain_after * 0.31
  - total_cgt: cgt_33 + cgt_31
  - cgt_after_if_lapsed: gain_after * 0.33
expected:
  cgt_33: 1560.90
  cgt_31: 3100.00
  total_cgt: 4660.90
  cgt_after_if_lapsed: 3300.00
```

## Ask the client first

- Were you resident in Ireland for all of 2026, and are you Irish domiciled? This decides which income is taxed and which skills apply.
- Are you a proprietary director, or in self-assessment already? Either one means Form 11.
- What non-PAYE income did you have in 2026, gross and after expenses? Over EUR 5,000 taxable or EUR 30,000 gross means Form 11.
- Are you single, married or in a civil partnership, and are you assessed jointly? This sets the rate band and credits.
- Did you sell or give away any asset in 2026, and on what contract date? The date sets the CGT rate and payment date.
- How much preliminary tax did you pay for 2026, and how much PAYE, USC and withholding tax was deducted?

## Sources

| Source | URL | Read on |
|---|---|---|
| Revenue, tax rates, bands and reliefs (2026 bands and credits) | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx | 2026-10-23 |
| Revenue, USC standard rates and thresholds 2026 | https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx | 2026-10-23 |
| Revenue, USC overview (EUR 13,000 exemption limit) | https://www.revenue.ie/en/jobs-and-pensions/usc/index.aspx | 2026-10-23 |
| Revenue, other USC rates (3% surcharge) | https://www.revenue.ie/en/jobs-and-pensions/usc/other-rates.aspx | 2026-10-23 |
| Department of Social Protection, PRSI Class S rates | https://www.gov.ie/en/department-of-social-protection/publications/prsi-class-s-rates/ | 2026-10-23 |
| Revenue, how to calculate CGT (31%, 33%, development land) | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/how-to-calculate-cgt.aspx | 2026-10-23 |
| Dáil Éireann debate, 6 October 2026, Financial Resolution No. 3 | https://data.oireachtas.ie/akn/ie/debateRecord/dail/2026-10-06/debate/mul@/main.xml | 2026-10-23 |
| Revenue, what is exempt from CGT (EUR 1,270) | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/what-is-exempt-from-cgt.aspx | 2026-10-23 |
| Revenue, when and how do you pay and file CGT | https://www.revenue.ie/en/gains-gifts-and-inheritance/transfering-an-asset/when-and-how-do-you-pay-and-file-cgt.aspx | 2026-10-23 |
| Revenue, do you need to submit a tax return? (Form 11 and Form 12) | https://www.revenue.ie/en/jobs-and-pensions/end-of-year-process/need-to-submit-a-tax-return.aspx | 2026-10-23 |
| Revenue, PAYE Income Tax Return (four-year limit) | https://www.revenue.ie/en/jobs-and-pensions/end-of-year-process/paye-income-tax-return.aspx | 2026-10-23 |
| Revenue, pay and file (31 October, extension, surcharges) | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/pay-file-system.aspx | 2026-10-23 |
| Revenue, preliminary tax | https://www.revenue.ie/en/self-assessment-and-self-employment/guide-to-self-assessment/preliminary-tax.aspx | 2026-10-23 |
| Revenue, eBrief 034/26 (ROS extension to 18 November 2026) | https://www.revenue.ie/en/tax-professionals/ebrief/2026/no-0342026.aspx | 2026-10-23 |
| Revenue, guidelines for charging interest on late payment | https://www.revenue.ie/en/tax-professionals/tdm/collection/debt-management/guidelines-for-charging-interest-on-late-payment.pdf | 2026-10-23 |
| Revenue, Earned Income Credit | https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/income-and-employment/earned-income-credit/index.aspx | 2026-10-23 |
| Revenue, Guide to Completing 2025 Pay and File Self-Assessment Returns (ROS registration, payment methods, six-year retention) | https://www.revenue.ie/en/self-assessment-and-self-employment/documents/guide-pay-file.pdf | 2026-10-27 |
| Taxes Consolidation Act 1997, section 601 as enacted (exemption against the higher-rate gains first, subsection (3)) | https://www.irishstatutebook.ie/eli/1997/act/39/section/601/enacted/en/html | 2026-10-23 |
| Department of Social Protection, SW14 (January 2026): Class S from EUR 5,000 | https://assets.gov.ie/static/documents/cb168977/PRSI_C20260116_Contribution_Rates_and_User_Guide_-_SW_14_-_English_Version_-_January_2026_.pdf-web.pdf | 2026-10-23 |

Not yet confirmed: the ROS pay and file extension date for 2026 returns (due in 2027), which Revenue has not announced; whether the Finance (No. 2) Act 2026 is enacted with the 31% CGT rate unchanged; the earlier version's rule that credits above the year's liability are refunded only where they are PAYE or professional services withholding tax backed by the employment detail summary or Form F45 or F50 certificates, which no saved Revenue source or section of the Taxes Consolidation Act 1997 checked here states in those terms.

> Contributed by Michael Cutajar.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-27. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ie-return-assembly` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ie-return-assembly. If neither is available, confirm every figure against the official source pages cited above before relying on it.
