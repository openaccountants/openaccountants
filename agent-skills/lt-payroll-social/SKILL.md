---
name: lt-payroll-social
description: "Use this skill for Lithuanian payroll and social contributions in tax year 2026. It covers Sodra social insurance (VSD) and compulsory health insurance (PSD) for employees: 19.5% withheld (pension 8.72%, sickness 1.99%, maternity 1.81%, health 6.98%) plus 3% for second-pillar savers; the employer's 1.77% (unemployment 1.31%, accidents 0.14%, Guarantee Fund 0.16%, Long-term Employment Benefit Fund 0.16%) and 2.49% on fixed-term contracts; the 60 average wage ceiling (EUR 138,729), which from 2026 also caps the employer's part; the EUR 1,153 minimum wage and the minimum contribution base; contributions for individual activity (12.52% or 15.52% VSD and 6.98% PSD on 90% of taxable income, capped at EUR 99,422.45, PSD minimum EUR 80.48 a month); PIT withholding at 20%, 25% and 32% with the NPD; GPM313 and SAM returns by the 15th; tax and Sodra payment dates; fines and late interest. Trigger on: Sodra, VSD, PSD, SAM, GPM313, darbo užmokestis, NPD, Lithuanian payroll, self-employed contributi"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/lt-payroll-social"
  jurisdiction: "LT"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Lithuania: payroll and social contributions (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. The law comes from the consolidated texts on e-tar.lt (the Register of Legal Acts) and the guidance from sodra.lt (the State Social Insurance Fund Board, Sodra) and vmi.lt (the State Tax Inspectorate, VMI), all read on 24 October 2026. It prepares working papers; it is not authority to file or pay.

This is the social contributions (SC) and payroll withholding (PR) skill for the Lithuanian pack. It links rather than repeats:

- The annual personal income tax, the NPD formula, individual activity tax and the return by 1 May: [lithuania-pit](lithuania-pit.md).
- Non-residents, residence and tax at source: [lt-cross-border](lt-cross-border.md).
- Corporate income tax, including the deduction of pay: [lt-corporate-income-tax](lt-corporate-income-tax.md).
- Overview of the system: [lt-tax-overview](lt-tax-overview.md).

The law is the Law on State Social Insurance No. I-1336 ("VSDĮ", consolidated version in force from 1 July 2026), as amended by Law No. XV-633 of 9 December 2025; the Law on Health Insurance No. I-1343 ("SDĮ", consolidated version from 1 September 2026); the Law on Personal Income Tax No. IX-1007 ("GPMĮ", consolidated version from 11 June 2026); VMI order VA-121 on the GPM313 return; and the Law on Tax Administration No. IX-2112 ("MAĮ"). The contribution rates themselves are set each year by the law approving the social funds' budget indicators (VSDĮ article 8(2)); this skill takes the 2026 rates from Sodra's published tables. Currency: euro (EUR).

## Who this applies to

**Employers (draudėjai) and their employees.** An employer computes, withholds and pays both its own and the employee's social insurance contributions from the first day of work (VSDĮ article 12(1)), and withholds the employee's health insurance contribution under the same procedure (SDĮ article 17(1) and (2)). It also withholds personal income tax (GPM) from pay as a withholding agent (GPMĮ article 23). Sodra puts it in one line: the employer computes, withholds and pays every contribution due.

**Self-employed people.** People with registered individual activity (individuali veikla) pay their own contributions on 90% of their taxable income from that activity (VSDĮ article 10(3)(2); SDĮ article 17(4)). Business certificate holders, owners of individual enterprises (IĮ), members of small partnerships (MB) and full partners of partnerships have their own bases, shown in the rates table but not worked through here.

**Who is out.** Annual income tax for individuals is in [lithuania-pit](lithuania-pit.md). Agricultural activity, sports and performers' income, author contracts, voluntary insurance and the special pension rules are not covered beyond the rates listed.

**VDU and MMA.** VDU is the national average wage approved for the year in the social funds' budget law (VSDĮ article 2(16)). MMA is the minimum monthly wage approved by the Government. For 2026 Sodra gives the MMA as EUR 1,153 and the 60 VDU ceiling as EUR 138,729, so one VDU is EUR 2,312.15 (138,729 / 60). The same VDU gives VMI's income tax bands in [lithuania-pit](lithuania-pit.md).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Employee: pension insurance (VSD) | 8.72% | 2026 | [Sodra, employee rates](https://sodra.lt/imoku-tarifai/imoku-tarifai-taikomi-uz-samdomus-darbuotojus) |
| Employee: sickness insurance (VSD) | 1.99% | 2026 | same |
| Employee: maternity insurance (VSD) | 1.81% | 2026 | same |
| Employee: compulsory health insurance (PSD) | 6.98% | 2026 | same; [SDĮ art. 17(2)](https://www.e-tar.lt/portal/lt/legalAct/TAR.94F6B680E8B8/asr) |
| Employee total without second pillar | 19.5% (12.52% VSD + 6.98% PSD) | 2026 | sum of the four rates above |
| Employee: extra pension accumulation (second pillar), if enrolled | 3% more, so 22.5% in total | 2026 | [Sodra, employee rates](https://sodra.lt/imoku-tarifai/imoku-tarifai-taikomi-uz-samdomus-darbuotojus) |
| Employer: unemployment insurance | 1.31% (open-ended contract); 2.03% (fixed-term contract) | 2026 | same |
| Employer: accidents at work and occupational diseases | 0.14% (group I, the usual group); 0.49% (II); 0.7% (III); 1.4% (IV) | 2026 | same |
| Employer: Guarantee Fund | 0.16% | 2026 | same |
| Employer: Long-term Employment Benefit Fund | 0.16%, on pay of at least the MMA | 2026 | same |
| Employer total, group I | 1.77% open-ended (1.31 + 0.14 + 0.16 + 0.16); 2.49% fixed-term | 2026 | sum of the rates above |
| Minimum monthly wage (MMA) | EUR 1,153 | 2026 | [Sodra, self-employed rates](https://sodra.lt/imoku-tarifai/imoku-tarifai-taikomi-savarankiskai-dirbantiems-asmenims) |
| Ceiling on employee VSD and, from 2026, employer VSD | 60 VDU a year: EUR 138,729 | 2026 | [Sodra, employers](https://sodra.lt/imokos/idarbinimas-pranesimai-imokos-ir-tarifai?kam=draudejams); [VSDĮ art. 10(9)](https://www.e-tar.lt/portal/lt/legalAct/TAR.0F9036415DBD/asr); [Law XV-633 art. 5(3)](https://www.e-tar.lt/portal/lt/legalAct/2cf13750d9b111f08918e1adc7c5b1ec) |
| Minimum base for employees | Contributions on at least the MMA (pro rata to time worked); the employer pays the shortfall from its own funds | 2026 | [VSDĮ art. 10(1), 10(7)](https://www.e-tar.lt/portal/lt/legalAct/TAR.0F9036415DBD/asr) |
| Individual activity: VSD | 12.52% (15.52% with the 3% second pillar) of 90% of taxable income | 2026 | [Sodra, individual activity](https://sodra.lt/imokos/vykdau-individualia-veikla); [VSDĮ art. 10(3)(2)](https://www.e-tar.lt/portal/lt/legalAct/TAR.0F9036415DBD/asr) |
| Individual activity: PSD | 6.98% of 90% of taxable income | 2026 | [Sodra, individual activity](https://sodra.lt/imokos/vykdau-individualia-veikla); [SDĮ art. 17(4)](https://www.e-tar.lt/portal/lt/legalAct/TAR.94F6B680E8B8/asr) |
| Individual activity: ceiling on the base (VSD and PSD) | 43 VDU: EUR 99,422.45 | 2026 | [Sodra, individual activity](https://sodra.lt/imokos/vykdau-individualia-veikla); [VSDĮ art. 10(5)](https://www.e-tar.lt/portal/lt/legalAct/TAR.0F9036415DBD/asr); [SDĮ art. 17(13)](https://www.e-tar.lt/portal/lt/legalAct/TAR.94F6B680E8B8/asr) |
| Individual activity: maximum VSD | EUR 12,447.69 (EUR 15,430.36 with the second pillar) | 2026 | [Sodra, individual activity](https://sodra.lt/imokos/vykdau-individualia-veikla) |
| Individual activity: monthly PSD minimum (6.98% of the MMA) | EUR 80.48 a month, unless PSD is paid for the person elsewhere | 2026 | same; [SDĮ art. 17(11), 17(12)](https://www.e-tar.lt/portal/lt/legalAct/TAR.94F6B680E8B8/asr) |
| First year of self-employment | VSD optional for one year from the first start of activity after 1 January 2018 (or after a break of at least 10 years); PSD still due | 2026 | [VSDĮ art. 11(3)](https://www.e-tar.lt/portal/lt/legalAct/TAR.0F9036415DBD/asr); [Law XV-633 art. 3(2)](https://www.e-tar.lt/portal/lt/legalAct/2cf13750d9b111f08918e1adc7c5b1ec) |
| Business certificate holders | VSD 8.72% (11.72% with second pillar) and PSD 6.98%, both on the MMA | 2026 | [Sodra, self-employed rates](https://sodra.lt/imoku-tarifai/imoku-tarifai-taikomi-savarankiskai-dirbantiems-asmenims) |
| IĮ owners, MB members, full partners | VSD 13.83% (16.83% with second pillar) and PSD 6.98% on 50% of funds drawn for personal needs (January to June 2026), 90% (July to December 2026) | 2026 | same; [VSDĮ art. 10(3)(1)](https://www.e-tar.lt/portal/lt/legalAct/TAR.0F9036415DBD/asr) |
| PIT on annual income (pay included) up to 36 VDU (EUR 83,237.40) | 20% | 2026 | [GPMĮ art. 6(1)](https://www.e-tar.lt/portal/lt/legalAct/TAR.C677663D2202/asr) |
| PIT on annual income over 36 VDU up to 60 VDU (EUR 138,729) | 25% | 2026 | same |
| PIT on annual income over 60 VDU | 32% | 2026 | same |
| PIT on individual activity income up to EUR 42,500 | 20%, less a credit (5% effective up to EUR 20,000) | 2026 | [GPMĮ art. 6(8), 18-2](https://www.e-tar.lt/portal/lt/legalAct/TAR.C677663D2202/asr) |
| Monthly NPD, monthly employment income up to the MMA | EUR 747 | 2026 | [GPMĮ art. 20(2)](https://www.e-tar.lt/portal/lt/legalAct/TAR.C677663D2202/asr) |
| Monthly NPD above the MMA | 747 - 0.49 x (monthly income - 1,153); nil from EUR 2,677.49 | 2026 | same; [VMI commentary on art. 20](https://www.vmi.lt/evmi/documents/20142/391224/GPM+aktualus+komentaras+%28aktuali+redakcija+2026-10-19%29+.pdf/541c2138-7e9c-3e99-33bf-fc547c5cdc28?t=1792476568043) |
| Late payment interest on tax (delspinigiai) | 0.027% a day from 1 August 2026 | 2026 | [VMI, late interest](https://www.vmi.lt/evmi/delspinigiai-baudos-ir-atleidimas-nuo-ju-96-100-str.-138-143-str.-) |

**What changed for 2026.** Law XV-633 rewrote VSDĮ article 10(9) so that, for 2026 and later years, the 60 VDU ceiling covers the employer's social insurance contributions as well as the employee's (XV-633 article 5(3)). Sodra's employer page still carries the older note that since 2021 the ceiling applied only to the employee's part; that note describes the earlier law. The same law excluded from the base, for 2026 and later years, employer-paid voluntary health insurance premiums that are exempt from income tax (VSDĮ article 11(1)(17)), and raised the base for IĮ owners and partnership members from 50% to 90% of drawings for periods from 1 July 2026. Income tax moved to three bands (20%, 25%, 32%) and individual activity income to 20% with a sliding credit; see [lithuania-pit](lithuania-pit.md).

## The taxable base

**Employees: what counts.** Contributions are computed on all pay and extras worked out for the employee, whatever the source of payment, subject to the exclusions in VSDĮ article 11 (VSDĮ article 10(1)). Health insurance is charged on the same income (SDĮ article 17(2)).

**The minimum base.** Pay below the MMA for a full month does not lower contributions. The employer computes contributions on the actual pay and then pays, from its own funds, both the employee's and the employer's VSD on the gap up to the MMA (VSDĮ article 10(7)). This top-up does not apply in a month in which the employee:

1. was insured with another employer, or is insured for pension at the State's expense;
2. received an old-age, incapacity or disability pension (including one from another EU, EEA or treaty state);
3. was under 24 (until the month they turn 24);
4. has a participation level of 0% to 55%;
5. received maternity, paternity or childcare benefit.

Where pay falls below the MMA because of unpaid leave or sickness benefit, the base is the MMA pro rata to the working days in the month on a five-day week (VSDĮ article 10(8)). The 0.16% Long-term Employment Benefit Fund contribution is always charged on at least the MMA (Sodra).

**The ceiling.** VSD contributions of the employee and, from 2026, of the employer are charged on pay up to 60 VDU in the year (EUR 138,729). Above that the rate is 0%. Once one type of insurance reaches the ceiling, only the other types continue until each has reached it (VSDĮ article 10(9)). Pay from several employers counts together; Sodra recalculates automatically and tells every employer. An employee who has overpaid gets the excess back by 31 May of the next year (VSDĮ article 10(10)). PSD has no ceiling for employees (Sodra).

**Income tax withholding.** The employer withholds GPM from gross pay. The employee's Sodra and health contributions are not deducted first: VMI's NPD example in its commentary on article 20 works from pay before contributions. If the employee asks in writing, the employer deducts the monthly NPD: EUR 747 when monthly employment income is at most the MMA, falling by 0.49 for each euro above it, and nil from EUR 2,677.49 (GPMĮ articles 20(2) and 23(2)). The NPD is given at one place of work only. On each payment the employer applies the article 6 rates by the size of that payment alone; for regular payments, at the employee's request, it applies them by reference to the total it has paid and expects to pay that year (GPMĮ article 23(7)). The annual return then reconciles the bands and the NPD; see [lithuania-pit](lithuania-pit.md).

**Individual activity.** The base is 90% of the year's taxable income from individual activity, before deducting the person's own VSD and PSD (VSDĮ article 10(3)(2); Sodra). Taxable income means income less allowable deductions under GPMĮ article 18: actual documented costs or the flat 30% option (see [lithuania-pit](lithuania-pit.md)). The base is capped at 43 VDU, EUR 99,422.45 for 2026 (VSDĮ article 10(5); Sodra), and the same cap applies to PSD (SDĮ article 17(13)). VSD is 12.52% of the base, or 15.52% for a second-pillar saver; PSD is 6.98%.

**First year of activity.** IĮ owners, MB members, full partners, farmers and people with individual activity may choose not to pay VSD for one year from the day they first become self-employed after 1 January 2018; the same applies to someone who has not been self-employed for at least ten years since that date (VSDĮ article 11(3), as set by Law XV-633). The relief covers social insurance only; the PSD rules below still apply.

**The PSD floor for the self-employed.** A self-employed person not insured through another channel pays PSD of 6.98% of the MMA each month, EUR 80.48 in 2026, and the yearly PSD cannot be less than 6.98% of 12 MMAs (SDĮ article 17(11) and (12)). The monthly payment is not needed when PSD is paid for the person elsewhere (for example as an employee) or the State insures them (for example a full-time student or someone with the full pension record) (Sodra). After the year, the person pays the difference between the PSD paid and 6.98% of the base.

## Deadlines and filing

| What | Who | When | Source |
|---|---|---|---|
| Pay employer and employee Sodra contributions (VSD and PSD) | Employer | By the 15th of the next month | [VSDĮ art. 12(2)](https://www.e-tar.lt/portal/lt/legalAct/TAR.0F9036415DBD/asr) |
| SAM monthly report of pay and contributions to Sodra, signed with a qualified e-signature | Employer | By the 15th of the next month (next working day if the 15th is not one); January 2026 was due 15 February 2026 | [Sodra, employers](https://sodra.lt/imokos/idarbinimas-pranesimai-imokos-ir-tarifai?kam=draudejams) |
| Pay GPM withheld from pay made on days 1 to 15 of a month | Employer | By the 15th of the same month | [GPMĮ art. 23(3)](https://www.e-tar.lt/portal/lt/legalAct/TAR.C677663D2202/asr) |
| Pay GPM withheld from pay made after the 15th | Employer | By the last day of the same month | same |
| GPM313 monthly income tax return | Employer, even with no payments in a month when it had employees | By the 15th of the next month, electronically through deklaravimas.vmi.lt | [VMI order VA-121, paras. 4, 12, 14](https://www.e-tar.lt/portal/lt/legalAct/75345220e61e11e7acd7ea182930b17f/asr) |
| Monthly PSD minimum (EUR 80.48) | Self-employed person not insured elsewhere | By the last day of the month | [Sodra, individual activity](https://sodra.lt/imokos/vykdau-individualia-veikla) |
| Optional monthly VSD on the month's income, with an SAV report | Self-employed person who chooses advance payment | By the last day of the same month | [VSDĮ art. 12(5)](https://www.e-tar.lt/portal/lt/legalAct/TAR.0F9036415DBD/asr); Sodra |
| Annual VSD, and the PSD balance, on 2026 individual activity income | Self-employed person | By the deadline for the 2026 annual income tax return, 1 May 2027 | [VSDĮ art. 12(5)](https://www.e-tar.lt/portal/lt/legalAct/TAR.0F9036415DBD/asr); [GPMĮ art. 27(1)](https://www.e-tar.lt/portal/lt/legalAct/TAR.C677663D2202/asr) |
| Business certificate of 3 months or more | Holder | Quarterly, by the 15th of the first month of the next quarter (shorter certificates: in advance) | [VSDĮ art. 12(6)](https://www.e-tar.lt/portal/lt/legalAct/TAR.0F9036415DBD/asr) |

The GPM313 return splits tax withheld on employment pay paid up to the 15th (field 6) from tax on pay paid after the 15th (field 7) (VMI order VA-121, paras. 9.2 and 9.3). For 2025 income Sodra set the self-employed annual payment date at 4 May 2026, because 1 May 2026 was a public holiday followed by a weekend.

## Penalties and interest

- **Late Sodra contributions from employers.** Late interest (delspinigiai) runs from the day after the due date to the day of payment, for no more than 180 days from the day enforced recovery becomes possible. The rate is set by the Minister of Finance (VSDĮ article 19(1)). Late interest does not apply to contributions of self-employed people under VSDĮ article 5(2) and (3) (same article).
- **Late income tax.** VMI charges 0.027% a day from 1 August 2026 on late tax, under MAĮ articles 96 and 99 and Finance Minister order 1K-188 (VMI page KM2633).
- **Contributions reduced unlawfully.** If an inspection finds contributions were understated, Sodra charges the shortfall plus a fine computed under MAĮ articles 139 and 140, with no late interest on top. MAĮ article 139 sets the fine at 20% to 100% of the shortfall. No fine is imposed where the employer corrected the error, paid the shortfall and refiled before the date of the inspection order; late interest then runs as normal (VSDĮ article 19(2)).
- **Under-withheld income tax.** If an audit finds tax not declared or computed, VMI adds a fine of 20% to 100% of the tax; it is doubled for a repeat breach, and it does not apply if the return was filed or corrected before the audit order (MAĮ article 139(1), (3) and (4)).
- **Deferral.** Sodra may defer a contribution debt, or the late interest on it, for up to a year and allow repayment over up to four years (VSDĮ article 19(3) and (4)). Enforced recovery is barred after five years (VSDĮ article 19(7)).

## Cross-border points

- **Non-resident employees.** Income tax on their Lithuanian pay is withheld at the same bands. A non-resident gets the NPD only after the year, through the annual return (GPMĮ article 20(9)); see [lt-cross-border](lt-cross-border.md).
- **Work abroad by resident employees.** The GPM313 return leaves out employment pay for work in a treaty country where foreign income tax was paid on it (VMI order VA-121, para. 5).
- **Self-employed in another EU state at the same time.** A person employed or self-employed in Lithuania who is also self-employed in another state applying the EU social security coordination regulations, where the type of foreign activity cannot be established, is treated as carrying on individual activity and insured on that basis (VSDĮ article 10(6)).
- **Which country's social insurance applies** to a person working in more than one state is decided under the EU coordination regulations and Sodra's certificates, which this skill does not cover.

## Worked examples

**Example 1: employee on EUR 2,000 a month, open-ended contract, 2026.** The employee is not in the second pillar, has asked for the NPD, and the employer is in accident group I. The employee's contributions are 19.5% of EUR 2,000: EUR 250.40 VSD (12.52%) and EUR 139.60 PSD (6.98%), EUR 390.00 in all. The NPD is 747 - 0.49 x (2,000 - 1,153) = EUR 331.97. Income tax is 20% x (2,000 - 331.97) = EUR 333.61. Net pay is EUR 1,276.39. The employer adds 1.77%, EUR 35.40, so the total cost is EUR 2,035.40. If the pay is made on the 10th, the income tax is due by the 15th of the same month; the Sodra contributions, the SAM report and the GPM313 return are due by the 15th of the next month.

```oa-check
name: Employee EUR 2,000 a month, open-ended contract, NPD claimed, 2026
inputs:
  gross: 2000
  mma: 1153
steps:
  - employee_vsd: gross * 0.1252
  - employee_psd: gross * 0.0698
  - employee_total: employee_vsd + employee_psd
  - npd: max(747 - 0.49 * (gross - mma), 0)
  - pit: round((gross - npd) * 0.20, 2)
  - net: gross - employee_total - pit
  - employer: gross * 0.0177
  - total_cost: gross + employer
expected:
  employee_vsd: 250.40
  employee_psd: 139.60
  employee_total: 390.00
  npd: 331.97
  pit: 333.61
  net: 1276.39
  employer: 35.40
  total_cost: 2035.40
```

**Example 2: a high-earning freelancer hits the 43 VDU cap.** A consultant with registered individual activity has taxable income of EUR 120,000 for 2026 after actual documented costs (before her own contributions). She has been self-employed since 2020, is in the second pillar and has no job. Ninety percent of her income is EUR 108,000, which is above the EUR 99,422.45 cap, so the base is EUR 99,422.45. VSD at 15.52% is EUR 15,430.36, the maximum Sodra publishes. PSD at 6.98% is EUR 6,939.69. During the year she paid the monthly PSD minimum of EUR 80.48, EUR 965.76 in all, so EUR 5,973.93 of PSD is still due, together with the VSD if she did not pay it monthly, by 1 May 2027. Her income tax is separate: at this level there is no individual activity credit and the article 6(1) bands apply (see [lithuania-pit](lithuania-pit.md)).

```oa-check
name: Individual activity, taxable income EUR 120,000, second pillar, 43 VDU cap, 2026
inputs:
  taxable_income: 120000
  vdu: 2312.15
  monthly_psd: 80.48
steps:
  - cap: 43 * vdu
  - base: min(taxable_income * 0.90, cap)
  - vsd: round(base * 0.1552, 2)
  - psd: round(base * 0.0698, 2)
  - psd_paid: monthly_psd * 12
  - psd_due: psd - psd_paid
expected:
  cap: 99422.45
  base: 99422.45
  vsd: 15430.36
  psd: 6939.69
  psd_paid: 965.76
  psd_due: 5973.93
```

## Ask the client first

1. Is each worker on an employment contract (open-ended or fixed-term), a business certificate, individual activity or another contract? It sets the employer rate (1.77% or 2.49%) and who pays.
2. Which accident group has Sodra put the employer in for 2026? Group I gives 0.14%; II to IV give 0.49%, 0.7% or 1.4%.
3. Is the employee in the second pillar (extra 3%)? Has the employee asked this employer to apply the NPD, and does another employer already apply it?
4. Is anyone paid below the MMA for a full month, and does one of the article 10(7) exceptions apply (another employer, a pension, under 24, low participation level, parental benefits)?
5. Will any employee's pay from all employers pass EUR 138,729 in 2026? From that point VSD stops for both sides.
6. For the self-employed: taxable income for the year, whether costs are actual or the 30% option, second pillar status, whether this is the first year of self-employment (VSD optional), and whether PSD is already paid through a job or by the State.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law on State Social Insurance No. I-1336, consolidated version from 1 July 2026: art. 2(16), 8, 10(1), (3), (5) to (10), 12, 19 | https://www.e-tar.lt/portal/lt/legalAct/TAR.0F9036415DBD/asr | 2026-10-24 |
| Law No. XV-633 of 9 December 2025 amending VSDĮ art. 5, 10, 11 and 12: art. 2, 3, 4, 5 | https://www.e-tar.lt/portal/lt/legalAct/2cf13750d9b111f08918e1adc7c5b1ec | 2026-10-24 |
| Law on Health Insurance No. I-1343, consolidated version from 1 September 2026: art. 17 | https://www.e-tar.lt/portal/lt/legalAct/TAR.94F6B680E8B8/asr | 2026-10-24 |
| Law on Personal Income Tax No. IX-1007, consolidated version from 11 June 2026: art. 6, 18-2, 20, 23, 27 | https://www.e-tar.lt/portal/lt/legalAct/TAR.C677663D2202/asr | 2026-10-24 |
| VMI order VA-121 (GPM313 form and filing rules), consolidated version from 21 November 2025 | https://www.e-tar.lt/portal/lt/legalAct/75345220e61e11e7acd7ea182930b17f/asr | 2026-10-24 |
| Law on Tax Administration No. IX-2112, consolidated version from 1 July 2026: art. 139 | https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr | 2026-10-24 |
| Sodra, contribution rates for employees, 2026 | https://sodra.lt/imoku-tarifai/imoku-tarifai-taikomi-uz-samdomus-darbuotojus | 2026-10-24 |
| Sodra, contribution rates for the self-employed, 2026 | https://sodra.lt/imoku-tarifai/imoku-tarifai-taikomi-savarankiskai-dirbantiems-asmenims | 2026-10-24 |
| Sodra, individual activity: bases, cap, PSD, payment dates | https://sodra.lt/imokos/vykdau-individualia-veikla | 2026-10-24 |
| Sodra, employers: SAM report, VSD ceiling | https://sodra.lt/imokos/idarbinimas-pranesimai-imokos-ir-tarifai?kam=draudejams | 2026-10-24 |
| VMI, commentary on the Personal Income Tax Law (version of 19 October 2026), art. 20 | https://www.vmi.lt/evmi/documents/20142/391224/GPM+aktualus+komentaras+%28aktuali+redakcija+2026-10-19%29+.pdf/541c2138-7e9c-3e99-33bf-fc547c5cdc28?t=1792476568043 | 2026-10-24 |
| VMI, late payment interest, answer KM2633 | https://www.vmi.lt/evmi/delspinigiai-baudos-ir-atleidimas-nuo-ju-96-100-str.-138-143-str.- | 2026-10-24 |

Not yet confirmed: the text of the 2026 social funds' budget indicators law that fixes the rates and the 2026 VDU (the figures here come from Sodra's tables and its EUR 138,729 ceiling); the late interest rate Sodra charges on employer contributions in 2026 (the law leaves it to the Minister of Finance; VMI's 0.027% a day is confirmed for tax only, and only from 1 August 2026; the rate for January to July 2026 was not read); whether the Guarantee Fund and Long-term Employment Benefit Fund contributions, which rest on separate laws, also stop at the 60 VDU ceiling from 2026; the monthly band thresholds employers use under GPMĮ article 23(7) when a single payment is large; the exact payment date for 2026 self-employed contributions, given that 1 May 2027 is a Saturday; the administrative fine for filing SAM or GPM313 late (Code of Administrative Offences, not read); and the social insurance rules for posted and multi-state workers under the EU coordination regulations.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `lt-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/lt-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
