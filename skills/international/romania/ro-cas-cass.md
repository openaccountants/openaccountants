---
name: ro-cas-cass
description: "Use this skill for the Romanian pension contribution (CAS) and health contribution (CASS) owed by the self-employed for tax year 2026: PFA, II, IF members and liberal professions, on net income in the real system or on an income norm. Covers CAS at 25% on a base the taxpayer chooses, at least 12 or 24 minimum wages, once income reaches 12 minimum wages; CASS at 10% of actual net income with a floor of 6 and a cap of 72 minimum wages; the RON 4,050 minimum wage that sets every 2026 threshold; who is exempt; the CAS and CASS opt-ins; how both reduce the income tax base; the Declarația unică filed and paid by 25 May 2027; and penalties. Trigger phrases: CAS PFA 2026, CASS PFA 2026, contribuții sociale PFA, plafon 72 salarii minime, pensie PFA, asigurare sănătate PFA. Out of scope: ro-income-tax (the 10% tax), ro-payroll-social (employee and employer contributions), ro-employee-income-tax (CASS on rent and investments), ro-cross-border."
version: 2.1
jurisdiction: RO
category: international
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Romania: CAS and CASS for the self-employed (PFA, II, IF, liberal professions), 2026

This skill computes the two social contributions a self-employed individual owes on 2026 income from independent activities: CAS (contribuția de asigurări sociale, the pension contribution) and CASS (contribuția de asigurări sociale de sănătate, the health contribution). Both are set and paid through the Declarația unică. The income tax on the same income is in ro-income-tax.

The law is Legea 227/2015 (Codul fiscal, "the Fiscal Code"), Title V, and Legea 207/2015 (Codul de procedură fiscală, "the Procedure Code"). Articles were read on 23 October 2026 in ANAF's consolidated texts, both shown as last updated by Legea 170/2026. ANAF notes these consolidations are not an official republication.

**The two rules in one line each.** CAS is 25% of a base you choose, never less than 12 or 24 minimum wages, and only once net income reaches 12 minimum wages. CASS is 10% of your actual net income, never more than 72 minimum wages and, in most cases, never less than 6.

## Who this applies to

- **In scope.** Individuals with income from independent activities (Fiscal Code art. 137(1)(b), art. 155(1)(b)): a PFA, an II, an IF member, and liberal professionals, whether net income is set in the real system or by an income norm. Contributions are due on income from Romania and from abroad, subject to EU coordination rules and social security agreements (art. 137(1), art. 155(1)).
- **CAS exemptions** (art. 150):
  - people insured in their own professional pension system who are not required to join the public pension system;
  - pensioners.
  An employee is not exempt from CAS on PFA income. The salary exemption in art. 150(2) covers only intellectual property income.
- **CASS exemptions.** The categories in art. 154(1) (for example pupils and students up to age 26, pregnant women and new mothers, cancer patients in national programmes) are exempt. Under art. 154(2), people in categories (d) to (ș) still pay CASS on income outside their exemption. Check art. 154 before applying any exemption.
- **Out of scope.** Employee and employer contributions on salaries (ro-payroll-social). CASS on rent, investments and other non-business income, which uses fixed bases of 6, 12 or 24 minimum wages (art. 170(2)-(3)): see ro-employee-income-tax. Intellectual property and sports contracts where the payer withholds contributions (art. 151(5)-(11), art. 174(4)-(5)). Agricultural income.

## Rates, bands and thresholds

All thresholds for 2026 use the minimum wage in force on 1 January 2026, RON 4,050, for the whole year. The July 2026 rise to RON 4,325 does not change them (art. 135^1(3)).

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| CAS rate | 25% | 2026 | Fiscal Code art. 138(a), https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| CASS rate | 10% | 2026 | art. 156, same page |
| Minimum wage that sets the 2026 thresholds and bases (in force 1 January 2026) | RON 4,050 a month | 2026 | art. 135^1(3), same page; HG 1506/2024 art. 1, https://static.anaf.ro/static/10/Anaf/legislatie/HG_1506_2024.pdf; ANAF DGRFP Brașov 2026 summary, p. 38, https://static.anaf.ro/static/10/Brasov/Brasov/modificari_fiscale_2026.pdf |
| Minimum wage from 1 July 2026 (not used for these contributions) | RON 4,325 a month | 2026 | HG 146/2026 art. 1, https://static.anaf.ro/static/10/Anaf/legislatie/HG_146_2026.pdf |
| CAS threshold: 12 minimum wages | RON 48,600 | 2026 | art. 148(1), Fiscal Code page |
| CAS minimum base, net income from 12 up to 24 minimum wages | 12 wages, RON 48,600; minimum CAS RON 12,150 | 2026 | art. 148(2)(a) |
| CAS minimum base, net income of 24 minimum wages or more | 24 wages, RON 97,200; minimum CAS RON 24,300 | 2026 | art. 148(2)(b) |
| CAS opt-in below 12 minimum wages | base at least RON 48,600; CAS at least RON 12,150 | 2026 | art. 148(4) |
| CASS base | actual net income or norm, all independent sources added | 2026 | art. 170(1) |
| CASS cap: 72 minimum wages | base RON 291,600; CASS at most RON 29,160 | 2026 | art. 170(1); ANAF Brașov summary, p. 38 (cap raised from 60 to 72 wages by Legea 239/2025 and Legea 141/2025) |
| CASS floor: 6 minimum wages | base RON 24,300; CASS at least RON 2,430 | 2026 | art. 174(6) |
| CASS opt-in (no income, a loss, or starting during the year) | 10% of 6 wages, RON 2,430; 25% when the option is filed, 75% by 25 May of the next year | 2026 | art. 180(1)-(2), art. 182 |
| Early-payment discount | up to 10%, only if the annual budget law sets it | 2026 | art. 151(14), art. 174(17) |

## The taxable base

**CAS (art. 148, 151).**

1. **Test the threshold.** Add up, for 2026 (art. 148(3)):
   - net income or norms from independent activities (art. 68, 68^3, 69);
   - gross income from sports contracts (art. 68^1);
   - net intellectual property income (art. 72, 72^1, 73).
   Salary and pension do not count.
2. **Below RON 48,600:** CAS is not due. The person may opt in, on a base of at least RON 48,600 (art. 148(4)).
3. **From RON 48,600 up to RON 97,200:** the base is a figure the taxpayer chooses, at least RON 48,600 (art. 148(2)(a)).
4. **RON 97,200 or more:** the base is at least RON 97,200 (art. 148(2)(b)).
5. **Compute.** CAS = 25% × the chosen base (art. 151(1)). The law sets a floor, not a cap, on the chosen base. A higher base buys more pension rights.
6. **No pro rata.** A person who starts, suspends or stops during the year applies the same full-year thresholds to the income actually earned (art. 151(2)).
7. **Becoming exempt mid-year.** A person who becomes a pensioner during the year uses a lower floor: one minimum wage for each month up to the event. If their income for those months is below that floor, no CAS is due (art. 151(3)).
8. **No refunds.** CAS paid early is not refunded if income ends below the threshold; it counts towards the pension instead (art. 151(4)).

**CASS (art. 170, 174).**

1. **Base.** Add up net income from all real-system sources, plus norms (adjusted where allowed), from independent activities (art. 170(1)). Losses carried forward under art. 118 do not reduce it.
2. **Cap.** The base cannot exceed 72 minimum wages, RON 291,600, so CASS is at most RON 29,160 (art. 170(1)).
3. **Loss or zero.** If the result is a loss or zero, no CASS is due. The person may opt in under art. 180 (art. 174(2)).
4. **Floor.** If the base is below 6 minimum wages (RON 24,300), the person pays CASS on RON 24,300, so RON 2,430 (art. 174(6)). There is no floor top-up when, in 2026, the person also had (art. 174(7)):
   - salary of at least 6 minimum wages;
   - other income (rent, investments and similar) on which CASS is due on at least 6 minimum wages;
   - pension income.
   The top-up is also not due for people who were in certain exempt categories in the previous year, or who opted in under art. 180 (art. 174(8)).
5. **Compute.** CASS = 10% × the base (art. 174(1)). For someone who opted in earlier in the year, the RON 2,430 already due counts towards the annual figure (art. 174(9)).
6. **Separate from other CASS.** CASS on rent, investments and other income is a separate computation on fixed bases (art. 170(2)-(3), art. 174^1).

**Deduction from the income tax base.** CAS and CASS due for the year are deducted from real-system net income before the 10% income tax (art. 118(2)(b)). The CASS top-up to the 6-wage floor is not deductible. Where the contribution base also covers norms or intellectual property income, only the real-system share is deductible (art. 118(2^2)-(2^3)). Norm taxpayers get no deduction. Details are in ro-income-tax.

## Deadlines and filing

- **Declare and pay by 25 May 2027.** CAS and CASS for 2026 are worked out on actual 2026 income in the Declarația unică. It is filed by 25 May 2027, and both contributions are paid by the same date (art. 122(3), art. 151(1), art. 174(3), (15)). There is no estimate and no advance instalment. Payments may be made at any time before the due date (art. 151(13), art. 174(16)).
- **Opt-ins.** The CAS option for income below 12 minimum wages is exercised in the same Declarația unică, by 25 May 2027 (art. 148(4)). The CASS option under art. 180 is filed at any time during the year it covers (art. 180(3)). It is paid 25% on filing and 75% by 25 May of the following year (art. 182).
- **Where.** The Declarația unică is filed online through ANAF's SPV (Spațiul Privat Virtual): https://www.anaf.ro/anaf/internet/ANAF/servicii_online/declaratia_unica. It is itself the assessment (art. 151(12), art. 174(14)). ANAF passes the CAS data to the National House of Public Pensions to record pension rights (art. 151(16)).

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late-payment interest | 0.02% a day, from the day after the due date | Procedure Code art. 174(1), (5), https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Late-payment penalty | 0.01% a day, on top of interest | art. 176(1)-(3), same page |
| Annual rules for interest on contributions; interest from 1 January 2027 if the return is filed late | as for annual income tax | art. 175(1)(d), (4) |
| Non-declaration penalty (contributions undeclared or declared wrongly, then assessed by ANAF) | 0.08% a day, instead of the 0.01% penalty; cut by 75% if paid by the due date in the assessment; not charged under RON 50 | art. 181(1)-(2), (6); art. 176(4) |
| Fine for an individual's late Declarația unică | RON 50 to 500 | art. 336(3) |

## Cross-border points

- **Which state insures the person.** Romanian CAS and CASS apply subject to EU Regulation 883/2004 coordination and Romania's social security agreements (Fiscal Code art. 135^2, art. 137(1), art. 155(1)). A self-employed person covered by another EU state, shown by an A1 certificate, does not pay Romanian contributions on that activity. See eu-social-security-coordination.
- **Foreign-source income.** A person insured in Romania counts foreign independent income in the CAS threshold and the CASS base, under the rules for its category (art. 135^2).
- **Who must contribute to CASS.** CASS payers include Romanian citizens living in Romania, foreigners with a right of residence or domicile in Romania, and EU frontier workers working in Romania. Digital nomads present 183 days or less in any 12 months are excluded (art. 153(1)(a)-(d)).
- Tax residence, withholding and treaties: ro-cross-border.

## Worked examples

**Example 1. High-earning consultant, above the CASS cap.**

Ioana is a PFA consultant in the real system. Her 2026 net income is RON 350,000. She has no salary or other income. She chooses the lowest CAS base.

- CAS: 350,000 is above 24 minimum wages (97,200). The base is at least RON 97,200. CAS = 25% × 97,200 = RON 24,300.
- CASS: the base is her net income, capped at 72 minimum wages (72 × 4,050 = 291,600). Base RON 291,600. CASS = RON 29,160.
- Total contributions due by 25 May 2027: RON 53,460. Both reduce her income tax base (art. 118(2)(b)).

```oa-check
name: PFA net RON 350,000, CAS at 24 wages, CASS capped, 2026
inputs:
  net: 350000
  min_wage: 4050
steps:
  - cas_base: 24 * min_wage
  - cas: cas_base * 0.25
  - cass_cap: 72 * min_wage
  - cass_base: clamp(net, 6 * min_wage, cass_cap)
  - cass: cass_base * 0.10
  - total: cas + cass
expected:
  cas: 24300.00
  cass_cap: 291600.00
  cass: 29160.00
  total: 53460.00
```

**Example 2. Employee with a small PFA on the side (edge case: no CASS floor top-up).**

Mihai is employed full time on a gross salary of RON 90,000 for 2026. He also runs a PFA in the real system with net income of RON 15,000.

- CAS on the PFA: only independent and intellectual property income count towards the threshold. RON 15,000 is below RON 48,600, so CAS is not due. His salary does not change that.
- CASS on the PFA: 10% × 15,000 = RON 1,500. The base is below 6 minimum wages (24,300). But his salary is at least 6 minimum wages, so no top-up is due (art. 174(7)(a)).
- If Mihai had no salary, CASS would be 10% × 24,300 = RON 2,430. The RON 930 top-up above RON 1,500 would not be deductible from his income tax base.

```oa-check
name: Employee plus PFA net RON 15,000, CASS floor waived, 2026
inputs:
  pfa_net: 15000
  salary: 90000
  min_wage: 4050
steps:
  - cas_threshold: 12 * min_wage
  - floor_base: 6 * min_wage
  - cass: pfa_net * 0.10
  - cass_without_salary: max(pfa_net, floor_base) * 0.10
  - topup_not_deductible: cass_without_salary - cass
expected:
  cas_threshold: 48600.00
  floor_base: 24300.00
  cass: 1500.00
  cass_without_salary: 2430.00
  topup_not_deductible: 930.00
```

## Ask the client first

1. What was your 2026 net income from each independent activity (real system), or your norm and the months worked?
2. Do you also have a salary, a pension, rent or investment income? A salary or pension removes the CASS floor top-up. A pension removes CAS.
3. Are you insured in your own professional pension system instead of the public one, or in another EU state (A1 certificate)?
4. Are you in a CASS-exempt category under art. 154 (for example a student under 26, pregnant or a new mother)?
5. Do you want a CAS base above the minimum, or to opt in to CAS below 12 minimum wages, for pension rights?
6. Did you opt in to CASS earlier in 2026, or pay any CAS or CASS before the deadline?

## Sources

| Source | URL | Read on |
|---|---|---|
| Legea 227/2015, Codul fiscal, ANAF consolidated text (last update Legea 170/2026): art. 118, 122, 135^1, 135^2, 137, 138, 148, 150, 151, 153, 154, 155, 156, 170, 174, 174^1, 180, 182 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-10-23 |
| Legea 207/2015, Codul de procedură fiscală, ANAF consolidated text (last update Legea 170/2026): art. 174, 175, 176, 181, 336 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm | 2026-10-23 |
| HG 1506/2024, minimum wage RON 4,050 from 1 January 2025 | https://static.anaf.ro/static/10/Anaf/legislatie/HG_1506_2024.pdf | 2026-10-23 |
| HG 146/2026, minimum wage RON 4,325 from 1 July 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/HG_146_2026.pdf | 2026-10-23 |
| ANAF DGRFP Brașov, summary of 2026 tax changes (21 July 2026), p. 38: CASS cap 72 wages, RON 291,600; RON 4,050 used for 2026; CASS option paid 25% and 75% | https://static.anaf.ro/static/10/Brasov/Brasov/modificari_fiscale_2026.pdf | 2026-10-23 |
| ANAF, Declarația unică online filing (SPV) | https://www.anaf.ro/anaf/internet/ANAF/servicii_online/declaratia_unica | 2026-10-23 |

Not yet confirmed: whether the 2026 state budget law grants an early-payment discount on 2026 CAS and CASS paid in 2027 (art. 151(14), art. 174(17)). The amending texts of Legea 239/2025 and Legea 141/2025 were not read; the 72-wage cap is taken from the consolidated Fiscal Code and the ANAF summary. Which professional pension systems count for the art. 150(1) exemption was not checked.
