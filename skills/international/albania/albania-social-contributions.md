---
name: albania-social-contributions
description: "Albanian compulsory social insurance and health insurance contributions for tax year 2026 under Law 7703/1993, Law 10383/2011 and Council of Ministers Decision 77/2015. Covers employees (employer 15% and employee 9.5% social, 1.7% and 1.7% health; part-time and short-contract rates), the ALL 50,000 minimum base and ALL 186,416 social ceiling, the self-employed (23% social on at least the minimum wage, 3.4% health on double the minimum wage), unpaid family workers, technology-park staff, people with two jobs, declaration and payment by the 20th, and Law 9920/2008 penalties and interest. Trigger on 'Albania social insurance', 'sigurime shoqërore', 'sigurime shëndetësore', 'self-employed contributions Albania', 'paga maksimale 2026', 'contribution ceiling Albania'. Out of scope: running the monthly payroll and income tax withholding (albania-payroll), income tax (albania-income-tax), farmers insured through ISSH, treaties (al-cross-border)."
version: 0.2
jurisdiction: AL
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
verified_by: pending
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Albania social and health contributions, tax year 2026

> **Source-cited draft.** Built by Michael Cutajar and the OpenAccountants team from Law No. 7703/1993, Law No. 10383/2011, Council of Ministers Decisions No. 77/2015 and No. 776/2025, Instruction No. 23/2014, Law No. 9920/2008 and notices of the General Directorate of Taxes and the Social Insurance Institute, read on 2026-10-23. No accountant has reviewed it. Do not file from it without review by a qualified Albanian professional.

Currency: Albanian lek (ALL). Contributions are monthly. The General Directorate of Taxes (tatime.gov.al) collects social and health contributions together with employment income tax on the listëpagesa, and passes them to the Social Insurance Institute (ISSH, issh.gov.al) and the Compulsory Health Insurance Fund (FSDKSH, fsdksh.gov.al) (Law 10383/2011 art. 9(1); Law 7703/1993 art. 13).

See also: `albania-payroll` (gross to net, the listëpagesa, income tax withholding), `albania-income-tax`, `al-cross-border`.

## Who this applies to

- **Employees and their employers.** Both pay social insurance for sickness, maternity and pensions; the employer alone also pays for work accidents and unemployment (Law 7703/1993 art. 9). Both pay health insurance, half each (Law 10383/2011 art. 8(2)). This covers every employee, full or part time, from the first day of work, and foreign nationals working in Albania (Law 7703/1993 art. 7; ISSH, compulsory insurance page).
- **Self-employed persons** (individuals carrying on an economic activity with regular income, including individual traders) are insured compulsorily for maternity, pensions and health. They pay for themselves on at least the minimum wage, and may choose a higher base up to the ceiling (Law 7703/1993 art. 9; Decision 77/2015 ch. III paras. 6, 7). This applies even when their business income is taxed at 0% under Law 29/2023 art. 69(1)(dh).
- **Unpaid family workers** over 16 who work and live lawfully with the self-employed person: the self-employed person pays for them on the minimum wage (Law 7703/1993 art. 9; Decision 77/2015 ch. II para. 3(c)).
- **Individuals over 18 with regular income from movable or immovable property** and no other compulsory health insurance pay health contributions (Decision 77/2015 ch. III para. 10).
- **Not covered here:** self-employed farmers, who pay to ISSH under separate rules (Law 7703/1993 art. 10; ISSH page on compulsory insurance for the self-employed in agriculture); voluntary insurance (Law 7703/1993 art. 11); supplementary schemes for the military, police and state officials.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| National minimum wage, monthly | ALL 50,000 | 2026 (from 1 Jan) | [Council of Ministers Decision 776/2025](https://www.issh.gov.al/wp-content/uploads/2026/08/VKM-NR.-776-DATE-19.12.2025-PER-PERCAKTIMIN-E-PAGES-MINIMALE-NE-SHKALLE-VENDI.pdf) |
| Minimum monthly base, employees (social and health) | ALL 50,000 | 2026 | [tatime.gov.al notice, 14.01.2026](https://tatime.gov.al/nga-1-janari-2026-rritet-paga-minimale-dhe-maksimale/); [ISSH, compulsory insurance](https://www.issh.gov.al/sigurimi-i-detyruar/) |
| Maximum monthly base, social insurance | ALL 186,416 (ALL 176,416 to 31.12.2025) | 2026 | [tatime.gov.al notice, 14.01.2026](https://tatime.gov.al/nga-1-janari-2026-rritet-paga-minimale-dhe-maksimale/); [Law 7703/1993 art. 10](https://www.issh.gov.al/wp-content/uploads/2026/08/LIGJ-NR.-7703-DATE-11.5.1993-PER-SIGURIMET-SHOQERORE-NE-REPUBLIKEN-E-SHQIPERISE-I-NDRYSHUAR-1-1.pdf) |
| Maximum base, health insurance, employees | None: full gross pay | 2026 | [Decision 77/2015 ch. II para. 4(a)](https://www.issh.gov.al/wp-content/uploads/2026/08/VENDIM-NR.-77-DATE-28.1.2015-PER-KONTRIBUTET-E-DETYRUESHME-DHE-PERFITIMET-NGA-SISTEMI-I-SIGURIMEVE-SHOQERORE-DHE-SIGURIMI-I-KUJDESIT-SHENDETESOR.pdf) |
| Employee working more than 87 hours a month, social | Employer 15.0%, employee 9.5% (24.5%) | 2026 | Decision 77/2015 ch. III para. 3(a); Law 7703/1993 art. 10 |
| Employee working less than 87 hours a month, social | Employer 13.9%, employee 9.4% (23.3%) | 2026 | Decision 77/2015 ch. III para. 4(a) |
| Contract shorter than one week, social | 0.3% of gross, employer only | 2026 | Decision 77/2015 ch. III para. 5(a) |
| Health insurance, every employee | Employer 1.7%, employee 1.7% (3.4%) | 2026 | Decision 77/2015 ch. III paras. 3(b) to 5(b); [Law 10383/2011 art. 8](https://fsdksh.gov.al/project/ligji-i-fondit/) |
| Split of the 24.5% by branch | Pensions 21.6%, maternity 1.4%, unemployment 0.9%, sickness 0.3%, work accidents 0.3% | 2026 | Decision 77/2015 ch. III para. 1; ISSH, compulsory insurance |
| Self-employed, social | 23% of a base of at least ALL 50,000, up to ALL 186,416 at the person's choice: at least ALL 11,500 a month | 2026 | Decision 77/2015 ch. III para. 6; [ISSH, compulsory insurance](https://www.issh.gov.al/sigurimi-i-detyruar/); tatime.gov.al notice |
| Self-employed, health | 3.4% of double the minimum wage (ALL 100,000): ALL 3,400 a month | 2026 | Law 10383/2011 arts. 7(3), 8(1); ISSH, compulsory insurance; tatime.gov.al notice |
| Unpaid family worker, social | 23% of the minimum wage (ALL 50,000): ALL 11,500 a month | 2026 | ISSH, compulsory insurance; tatime.gov.al notice |
| Unpaid family worker, health | 3.4% of ALL 100,000: ALL 3,400 a month | 2026 | Law 10383/2011 art. 7(3); tatime.gov.al notice |
| Individual with property income and no other health insurance | 3.4% of double the minimum wage: ALL 3,400 a month | 2026 | Decision 77/2015 ch. III para. 10 |
| Late-payment interest (art. 76) | 7.8% a year from 11.04.2026, confirmed from 08.10.2026 | 2026 | [tatime.gov.al: Normat e interesit](https://tatime.gov.al/institucioni/publikime/normat-e-interesit/) |

**How the 2026 bases were set.** Law 7703/1993 art. 10 ties the social ceiling to the minimum wage: it rises "by the same measure and at the same time". For 2026 the General Directorate applied that as the same ALL 10,000 increase, from ALL 176,416 to ALL 186,416, not the same 25% (tatime.gov.al notice of 14.01.2026). The fixed lek amounts still printed in the consolidated Decision 77/2015 (for example ALL 1,496 for self-employed health, ALL 22,000 for unpaid family workers) were computed on older minimum wages. Use the 2026 bases above.

**Employer rate in the law and in the decision.** Law 7703/1993 art. 10 gives employers 13.8% for sickness, maternity and pensions. Decision 77/2015 adds the employer-only accident (0.3%) and unemployment (0.9%) branches to reach 15.0%.

## The taxable base

**Employees.** The base is monthly gross pay on the listëpagesa, cash and in kind, including the first 14 days of sick pay the employer pays (Decision 77/2015 ch. II; Instruction 26/2023 payroll form items 16 and 24).
- Social: not below ALL 50,000 and not above ALL 186,416. The floor applies to part-time staff too (Decision 77/2015 ch. III para. 4(a)); only absences justified by documents, such as certified sick leave, reduce it in proportion to days worked ([tatime.gov.al payroll Q&A, answer 6](https://tatime.gov.al/pyetje-pergjigje-per-listepagesat/)).
- Health: not below ALL 50,000, no ceiling.
- Left out of the base (Decision 77/2015 ch. II para. 2): court-ordered maintenance, antidotes given in kind under the rules, non-permanent bonuses for family misfortune, long illness, damage or natural disaster, travel costs for work away from home that are not pay, and fees unrelated to the current employment.
- **Technology parks.** Employees in IT working for companies in parks under Law 58/2022 may, with prior written consent in the contract, pay social and health contributions on the minimum wage whatever their gross (Law 7703/1993 art. 10; Law 10383/2011 art. 7(5)).
- **Partly disabled employees** receiving a partial invalidity pension may pay on a lower base by working time, but not below 50% of the minimum wage (Decision 77/2015 ch. II para. 3(ç)).

**Two or more jobs** (Decision 77/2015 ch. III para. 15). Each employer must calculate and pay contributions. Health is paid on each salary. Social contributions in total may not exceed those computed on the ceiling. Where the work at each employer is below the minimum wage (cleaners, maintenance staff and similar), one employer is agreed as the main employer and declares the person; the total base cannot fall below the minimum wage.

**Self-employed.** Social: 23% of the minimum wage, or of a higher base the person chooses up to the ceiling. The person enters the whole amount in the employer column of the listëpagesa (Instruction 26/2023 payroll form item 17). Health: 3.4% of double the minimum wage, a fixed ALL 3,400 a month for 2026, whatever the income (Law 10383/2011 art. 7(3)). In the month of first registration or restart, the General Directorate allows the amount for the days of activity to be entered (tatime.gov.al payroll Q&A, answer 2).

**Ambulant traders and domestic workers** pay fixed monthly amounts set in Decision 77/2015 ch. III paras. 13 and 14. See Not yet confirmed.

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Register a new or returning employee, or an unpaid family worker, on form E-SIG 027/a | At least one calendar day before work starts | [ISSH, compulsory insurance](https://www.issh.gov.al/sigurimi-i-detyruar/); [Instruction 23/2014 paras. 4.1, 6.3](https://www.issh.gov.al/wp-content/uploads/2026/08/UDHEZIM-NR.-23-DATE-09.12.2014-PER-MBLEDHJEN-E-KONTRIBUTEVE-TE-DETYRUESHME-TE-SIGURIMEVE-SHOQERORE-DHE-SHENDETESORE-i-perditesuar.pdf) |
| Declare and pay contributions on the listëpagesa: entities, and individuals registered for VAT | Monthly, by the 20th of the following month | [Law 29/2023 art. 65(1)](https://tatime.gov.al/wp-content/uploads/2026/09/Ligj-Nr.-29-2023-Per-Tatimin-mbi-te-Ardhurat-i-ndryshuar.pdf); Instruction 23/2014 para. 4.3; [tatime.gov.al tax calendar](https://tatime.gov.al/kalendari_tatimor/listepagesa/) |
| Same, self-employed and traders not registered for VAT, ambulant traders, heads of household employing domestic workers | Quarterly, month by month, by the 20th of the month after each quarter (20 January, April, July, October) | Law 29/2023 art. 65(1); Instruction 23/2014 para. 4.3(b); [tatime.gov.al tax calendar](https://tatime.gov.al/kalendari_tatimor/listepagesa/) |
| Report a person leaving, on E-SIG 027/a | Within 10 calendar days of leaving; if late, contributions run until the date it is reported | Instruction 23/2014 paras. 4.1, 6.4 |

The self-employed person files the listëpagesa even with no employees, listing themselves and any unpaid family workers (E-SIG 025/a.1 and 025/a.2 filing notes, [tatime.gov.al form models](https://tatime.gov.al/institucioni/publikime/modele-dokumentash-tatimore/)). Returns are electronic only (Instruction 23/2014 para. 4.2). Payment is made at banks with an agreement with the General Directorate of Taxes, ISSH and FSDKSH, or at Albanian Post (ISSH, compulsory insurance page). The listëpagesa is the record from which ISSH computes each person's benefits (ISSH, compulsory insurance page). A person can check their insured periods on e-Albania.

## Penalties and interest

All under Law No. 9920/2008 "On tax procedures", consolidated to Law No. 79/2025 ([tatime.gov.al copy](https://tatime.gov.al/wp-content/uploads/2026/10/Ligj-Nr-9920-Dt-2008.05.19-perditesuar-1.pdf)).

| Failure | Penalty | Source |
|---|---|---|
| Contributions paid late | 0.06% of the unpaid amount per day, for at most 365 days | Law 9920/2008 art. 114(1) |
| Listëpagesa filed late | ALL 10,000 per return for corporate income taxpayers; ALL 5,000 for other taxpayers except individuals; ALL 3,000 for individuals | Law 9920/2008 art. 113 |
| Incorrect return | 0.06% of the unpaid amount per day, for at most 365 days | Law 9920/2008 art. 115(1) |
| Employee not registered at least one day before work starts, found at an on-site check | ALL 200,000 per employee for taxpayers registered for VAT and corporate income tax; ALL 50,000 for other taxpayers; plus the contributions | Law 9920/2008 art. 119(1) |
| Under-declared pay | 200% of the tax and contributions for legal entities; 100% for other taxpayers; plus the amounts for the whole period | Law 9920/2008 art. 119(3) |
| False returns or documents that understate contributions | 100% of the understated amount | Law 9920/2008 art. 116(1) |

**Late-payment interest** is added under art. 76: 120% of the Bank of Albania interbank rate, from the due date to payment. The published rate is 7.8% a year from 11.04.2026, confirmed from 08.10.2026. It cannot be waived (art. 76(4)). There is no flat 10% late-payment penalty in the law.

An employer that cannot pay all it owes must still pay, in full and on time, the contributions withheld from employees' pay (ISSH, compulsory insurance page). The art. 119(1) fine does not apply to persons over 16 found working who qualify as unpaid family workers of a self-employed person, checked against the family certificate on e-Albania (art. 119(2)).

## Cross-border points

- **Foreign nationals** working in Albania are insured on the same terms as Albanians (Law 7703/1993 art. 7; [ISSH, social insurance for foreigners](https://www.issh.gov.al/sigurimet-shoqerore-per-te-huajt-ne-shqiperi/)).
- **Bilateral agreements.** ISSH lists agreements applied with Turkey, Belgium, North Macedonia, Hungary, Luxembourg, the Czech Republic, Germany, Austria, Canada, Kosovo, Switzerland, Croatia, Bulgaria, Romania, Montenegro and Italy. Each sets the applicable legislation, evidenced by a certificate of coverage; insured periods in both states are added together for benefits, and pensions are exported without reduction ([ISSH, bilateral agreements](https://www.issh.gov.al/shtetet-me-te-cilat-shqiperia-ka-marreveshje/)).
- **No agreement.** A worker sent to Albania from a country without an agreement pays Albanian contributions from the first day, and may also owe contributions at home.
- **Albanians abroad** are protected under the agreements, and Albanian citizens aged 18 to pension age may insure voluntarily (Law 7703/1993 art. 7; ISSH, social insurance for foreigners).

## Worked examples

### Example 1: self-employed consultant on the minimum base

Anila is a self-employed consultant in Durrës, not registered for VAT, with no staff. Her business income is taxed at 0% under art. 69(1)(dh), but contributions are still due. She pays on the minimum base.

Social: 23% × ALL 50,000 = ALL 11,500 a month. Health: 3.4% × ALL 100,000 (double the minimum wage) = ALL 3,400 a month. Total ALL 14,900 a month. As she is not registered for VAT, she files quarterly: ALL 44,700 for July to September 2026, due by 20 October 2026. For the year: ALL 178,800.

```oa-check
name: Anila, self-employed on the 2026 minimum base, quarterly filer
inputs:
  minimum_wage: 50000
  months_in_quarter: 3
  months_in_year: 12
steps:
  - social_month: minimum_wage * 0.23
  - health_month: minimum_wage * 2 * 0.034
  - total_month: social_month + health_month
  - quarter_due: total_month * months_in_quarter
  - year_total: total_month * months_in_year
expected:
  social_month: 11500
  health_month: 3400
  total_month: 14900
  quarter_due: 44700
  year_total: 178800
```

### Example 2: part-time employee paid below the minimum wage

Gentian works 80 hours a month in a shop owned by a company, for ALL 30,000 gross a month. He has signed his personal status declaration there.

He works under 87 hours, so the social rates are 13.9% employer and 9.4% employee. The floor still applies: both bases are ALL 50,000, not his ALL 30,000. Employer social 13.9% × 50,000 = ALL 6,950; employee social 9.4% × 50,000 = ALL 4,700. Health 1.7% × 50,000 = ALL 850 each. His gross is under ALL 50,000, so no income tax (see `albania-payroll`). Net pay ALL 24,450. Employer cost ALL 37,800. Contributions of ALL 13,350 are 44.5% of his actual pay, against 27.9% for a full-time employee at or above the minimum wage.

```oa-check
name: Gentian, part-time under 87 hours, ALL 30,000 gross (2026 floor)
inputs:
  gross: 30000
  social_floor: 50000
  social_ceiling: 186416
steps:
  - social_base: clamp(gross, social_floor, social_ceiling)
  - health_base: max(gross, social_floor)
  - employer_social: social_base * 0.139
  - employee_social: social_base * 0.094
  - employer_health: health_base * 0.017
  - employee_health: health_base * 0.017
  - total_contributions: employer_social + employee_social + employer_health + employee_health
  - net_pay: gross - employee_social - employee_health
  - employer_cost: gross + employer_social + employer_health
  - share_of_pay: total_contributions / gross
expected:
  social_base: 50000
  employer_social: 6950
  employee_social: 4700
  employer_health: 850
  total_contributions: 13350
  net_pay: 24450
  employer_cost: 37800
  share_of_pay: 0.445
```

## Ask the client first

1. **Employee, self-employed, unpaid family worker, or more than one of these?** Each has its own base and rate, and a second job changes the ceiling test.
2. **Monthly gross pay and contract hours.** Under 87 hours, or a contract under one week, changes the rates; the ALL 50,000 floor applies regardless.
3. **For the self-employed: registered for VAT or not, and the base chosen.** VAT status decides monthly or quarterly filing; a base above ALL 50,000 raises both contributions and future pension.
4. **Any foreign element.** A posted worker with a certificate of coverage from an agreement country stays in the home scheme.
5. **Special status:** technology-park employer, partial invalidity pension, farmer, ambulant trader or domestic worker.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law No. 7703/1993 "Për sigurimet shoqërore", consolidated to Law No. 64/2023 (ISSH copy), arts. 7, 9 to 11, 13 | https://www.issh.gov.al/wp-content/uploads/2026/08/LIGJ-NR.-7703-DATE-11.5.1993-PER-SIGURIMET-SHOQERORE-NE-REPUBLIKEN-E-SHQIPERISE-I-NDRYSHUAR-1-1.pdf | 2026-10-23 |
| Law No. 10383/2011 "Për sigurimin e detyrueshëm të kujdesit shëndetësor", consolidated to Law No. 65/2023 (FSDKSH), arts. 6 to 9 | https://fsdksh.gov.al/project/ligji-i-fondit/ | 2026-10-23 |
| Council of Ministers Decision No. 77 of 28.1.2015 on compulsory contributions, consolidated to Decision No. 702 of 13.11.2024 (ISSH copy), chs. II and III | https://www.issh.gov.al/wp-content/uploads/2026/08/VENDIM-NR.-77-DATE-28.1.2015-PER-KONTRIBUTET-E-DETYRUESHME-DHE-PERFITIMET-NGA-SISTEMI-I-SIGURIMEVE-SHOQERORE-DHE-SIGURIMI-I-KUJDESIT-SHENDETESOR.pdf | 2026-10-23 |
| Council of Ministers Decision No. 776 of 19.12.2025 on the national minimum wage (ISSH copy) | https://www.issh.gov.al/wp-content/uploads/2026/08/VKM-NR.-776-DATE-19.12.2025-PER-PERCAKTIMIN-E-PAGES-MINIMALE-NE-SHKALLE-VENDI.pdf | 2026-10-23 |
| Instruction No. 23 of 9.12.2014 on collection of compulsory contributions, consolidated to Instruction No. 16 of 8.7.2026 (ISSH copy), paras. 4 and 6 | https://www.issh.gov.al/wp-content/uploads/2026/08/UDHEZIM-NR.-23-DATE-09.12.2014-PER-MBLEDHJEN-E-KONTRIBUTEVE-TE-DETYRUESHME-TE-SIGURIMEVE-SHOQERORE-DHE-SHENDETESORE-i-perditesuar.pdf | 2026-10-23 |
| General Instruction No. 26 of 8.9.2023 on income tax, consolidated to Instruction No. 9 of 12.3.2026, Annex 2 (listëpagesa filing notes) | https://tatime.gov.al/wp-content/uploads/2026/09/Udhezimi-nr-26-date-8.9.2023-Per-tatimin-mbi-te-ardhuart.pdf | 2026-10-23 |
| Law No. 29/2023 "Për tatimin mbi të ardhurat", consolidated, art. 65(1) | https://tatime.gov.al/wp-content/uploads/2026/09/Ligj-Nr.-29-2023-Per-Tatimin-mbi-te-Ardhurat-i-ndryshuar.pdf | 2026-10-23 |
| Law No. 9920/2008 "Për procedurat tatimore", consolidated to Law No. 79/2025, arts. 76, 113 to 116, 119 | https://tatime.gov.al/wp-content/uploads/2026/10/Ligj-Nr-9920-Dt-2008.05.19-perditesuar-1.pdf | 2026-10-23 |
| General Directorate of Taxes, "Nga 1 janari 2026, rritet paga minimale dhe maksimale" (14.01.2026) | https://tatime.gov.al/nga-1-janari-2026-rritet-paga-minimale-dhe-maksimale/ | 2026-10-23 |
| General Directorate of Taxes, tax calendar: listëpagesa | https://tatime.gov.al/kalendari_tatimor/listepagesa/ | 2026-10-23 |
| General Directorate of Taxes, payroll Q&A | https://tatime.gov.al/pyetje-pergjigje-per-listepagesat/ | 2026-10-23 |
| General Directorate of Taxes, form models (E-SIG 025/a.1, 025/a.2, 027/a) | https://tatime.gov.al/institucioni/publikime/modele-dokumentash-tatimore/ | 2026-10-23 |
| General Directorate of Taxes, interest rates for late-payment interest | https://tatime.gov.al/institucioni/publikime/normat-e-interesit/ | 2026-10-23 |
| Social Insurance Institute, compulsory insurance | https://www.issh.gov.al/sigurimi-i-detyruar/ | 2026-10-23 |
| Social Insurance Institute, social insurance for foreigners | https://www.issh.gov.al/sigurimet-shoqerore-per-te-huajt-ne-shqiperi/ | 2026-10-23 |
| Social Insurance Institute, bilateral agreements in force | https://www.issh.gov.al/shtetet-me-te-cilat-shqiperia-ka-marreveshje/ | 2026-10-23 |

Not yet confirmed: the 2026 fixed monthly amounts for ambulant traders and domestic workers (Decision 77/2015 ch. III paras. 13 and 14 still print ALL 4,696 and ALL 3,948, computed on older minimum wages); the 2026 rules and amounts for self-employed farmers; whether the self-employed person's own contributions are deductible in computing business income under Law 29/2023; how the social ceiling is shared between two employers in practice (listëpagesa categories 8 to 10 and 17 to 19); whether a self-employed person who is also an employee elsewhere at or above the ceiling still owes self-employed social contributions; the start date and scope of each bilateral agreement and the certificate of coverage procedure (the ISSH procedure page returned no text today); the ISSH page still gives ALL 10,000 for every late listëpagesa, while Law 9920/2008 art. 113 gives ALL 10,000, 5,000 or 3,000 by type of taxpayer (this skill follows the law).
