---
name: hu-payroll
description: "Hungarian payroll for tax year 2026: what an employer withholds and pays on an employee's wage. Covers the 15% personal income tax advance (szja-előleg), the 18.5% employee social security contribution (társadalombiztosítási járulék, TB), the 13% employer social contribution tax (szociális hozzájárulási adó, szocho), the 2026 minimum wage (HUF 322,800) and guaranteed minimum wage (HUF 373,200), the family tax allowance (családi kedvezmény) at HUF 133,340, 266,660 and 440,000 per child a month, the family contribution allowance, the under-25 exemption (cap HUF 715,765 a month), the mothers' exemptions (under 30, two, three, four or more children), the monthly 08 return (form 2608) by the 12th, and penalties. Trigger phrases: Hungarian payroll, bérszámfejtés, nettó bér, családi kedvezmény, szocho munkáltató, TB járulék munkavállaló, 08-as bevallás, employer cost Hungary. Out of scope: hu-income-tax and hu-social-contributions (self-employed), hu-corporate-tax, hu-transfer-pricing."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/hu-payroll"
  jurisdiction: "HU"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Hungary payroll (bérszámfejtés): 2026

Source-cited draft: not reviewed by an accountant, not for filing.

This skill covers a Hungarian employer paying wages under an employment contract (munkaviszony). The employer withholds personal income tax and the employee's social security contribution, pays its own social contribution tax, and reports all three on one monthly return. Self-employed contributions are in `hu-social-contributions`; the self-employed income tax is in `hu-income-tax`; both still carry 2025 figures. Company tax is in `hu-corporate-tax`. This skill does not repeat them.

All statute text was read on the Nemzeti Jogszabálytár at njt.jog.gov.hu on 2026-10-23, in the version in force from 1 October 2026. The short address njt.hu refused connections.

**What changed for 2026.**
- The family tax allowance rose on 1 January 2026 to HUF 133,340, 266,660 and 440,000 per child a month for one, two and three or more children (Szja tv. 29/A. § (2), as set by Act LV of 2024, 4. § (2); in force 1 January 2026 under 217. § (11) of that Act).
- A new exemption for mothers of two children applies from 1 January 2026, in 2026 only to mothers who turn 40 after 31 December 2025 (Act XIV of 2025, 4. § a)). Mothers of three children have been exempt since 1 October 2025 (Act XV of 2025, 3.-4. §).
- The under-30 mothers' exemption has no cap from 2026 and now covers mothers whose entitlement began before 2023 (Act XIII of 2025; NAV information sheet 73).
- The minimum wage is HUF 322,800 and the guaranteed minimum wage HUF 373,200 a month from 1 January 2026 (Government Decree 426/2025. (XII. 23.), 2. §).
- New employees are registered on form 08E from 1 January 2026; it replaced form T1041 (NAV form page for 08E).

## Who this applies to

- **Employers in Hungary** with staff in a munkaviszony. The employer is the "payer" (kifizető) who computes and withholds the income tax advance (Szja tv. 46.-49. §) and the employee contribution (Tbj. 24. §, 79. §), and pays the social contribution tax (Szocho tv. 1.-2. §).
- **Employees** who are insured under the Tbj. Every employment relationship is insured from day one by law (Tbj. 6. § (1) a)).
- **Foreign employers** with no Hungarian registration who employ insured staff in Hungary still owe the contributions. They file through a fiscal representative or register with NAV themselves; if they do neither, the employee must file and pay (Tbj. 87. § (1)-(3), (6)).
- Not covered here: simplified employment (egyszerűsített foglalkoztatás), household work, fringe benefits (béren kívüli juttatások, SZÉP card), company cars, directors' fees, and the year-end employer tax assessment. Each has its own rules.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Personal income tax (szja), flat | 15% of the tax base | 2026 | [Szja tv. 8. § (1)](https://njt.jog.gov.hu/jogszabaly/1995-117-00-00) |
| Employee social security contribution (TB járulék) | 18.5% of gross, no ceiling (NAV splits it 54% pension, 37.9% health, 8.1% labour market) | 2026 | [Tbj. 25. § (1), 26. § (1)](https://njt.jog.gov.hu/jogszabaly/2019-122-00-00) |
| Employer social contribution tax (szocho) | 13% of the same base as the TB contribution | 2026 | [Szocho tv. 1. § (10), 2. § (1)](https://njt.jog.gov.hu/jogszabaly/2018-52-00-00) |
| Vocational training contribution (szakképzési hozzájárulás) | Abolished. Act CLV of 2011 repealed from 1 January 2021; payments made to that tax heading from 1 February 2022 are booked as szocho | 2026 | [Act CLV of 2011, closing note](https://njt.jog.gov.hu/jogszabaly/2011-155-00-00); [Szocho tv. 36/E. §](https://njt.jog.gov.hu/jogszabaly/2018-52-00-00) |
| Minimum wage (minimálbér), full time, monthly | HUF 322,800 (weekly 74,210; daily 14,850; hourly 1,856) | from 2026-01-01 | [426/2025. (XII. 23.) Korm. rendelet 2. § (1)](https://njt.jog.gov.hu/jogszabaly/2025-426-20-22) |
| Guaranteed minimum wage (garantált bérminimum), jobs needing at least secondary education | HUF 373,200 a month | from 2026-01-01 | [426/2025. Korm. rendelet 2. § (2)](https://njt.jog.gov.hu/jogszabaly/2025-426-20-22) |
| Contribution floor for employees | Contribution base at least 30% of the minimum wage a month (HUF 96,840); the employer pays the TB on the shortfall | 2026 | [Tbj. 27. § (2), 23. § (3)](https://njt.jog.gov.hu/jogszabaly/2019-122-00-00) |
| Family tax allowance (családi kedvezmény), per qualifying child per month | 1 child: HUF 133,340; 2 children: HUF 266,660 each; 3 or more: HUF 440,000 each | from 2026-01-01 | [Szja tv. 29/A. § (2)](https://njt.jog.gov.hu/jogszabaly/1995-117-00-00); [Act LV of 2024, 217. § (11)](https://njt.jog.gov.hu/jogszabaly/2024-55-00-00) |
| Extra family allowance for a long-term ill or severely disabled child | HUF 133,340 per child per month on top | from 2026-01-01 | [Szja tv. 29/A. § (2a)](https://njt.jog.gov.hu/jogszabaly/1995-117-00-00) |
| Family contribution allowance (családi járulékkedvezmény) | 15% of the family allowance the tax base could not absorb, up to the employee's TB (or pension) contribution | 2026 | [Tbj. 79. § (2)](https://njt.jog.gov.hu/jogszabaly/2019-122-00-00) |
| Under-25 exemption (25 év alatti fiatalok kedvezménye) | Wage income exempt up to the July 2025 national average gross wage: HUF 715,765 a month (tax saved up to HUF 107,365) | 2026 | [Szja tv. 29/F. § (2)](https://njt.jog.gov.hu/jogszabaly/1995-117-00-00); [NAV information sheet 73](https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/73.-Szja-adoalap-kedvezmenyek-2026.-03.19) |
| Mothers under 30 (30 év alatti anyák kedvezménye) | Wage income fully exempt from szja, no cap. In 2026: a mother who turns 30 in 2026 or later and is entitled to the family allowance for her own or adopted child, or for a pregnancy from day 91; it runs to the end of the year she turns 30 | from 2026-01-01 | [Act XIII of 2025, 1.-2. §, 5. §](https://njt.jog.gov.hu/jogszabaly/2025-13-00-00); [NAV sheet 73, 2.2](https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/73.-Szja-adoalap-kedvezmenyek-2026.-03.19) |
| Mothers of two children | Wage income fully exempt from szja. In 2026 only if she turns 40 after 2025-12-31 (born 1986 or later); widens in 2027, 2028 and 2029 | from 2026-01-01 | [Act XIV of 2025, 1. §, 4. §](https://njt.jog.gov.hu/jogszabaly/2025-14-00-00) |
| Mothers of three children | Wage income fully exempt from szja, no age limit | from 2025-10-01 | [Act XV of 2025, 1. §, 3.-4. §](https://njt.jog.gov.hu/jogszabaly/2025-15-00-00) |
| Mothers of four or more children | Wage income fully exempt from szja | 2026 | [Szja tv. 29/D. §](https://njt.jog.gov.hu/jogszabaly/1995-117-00-00) |
| First marriage allowance (első házasok kedvezménye) | HUF 33,335 a month off the couple's tax base, for up to 24 months | 2026 | [Szja tv. 29/C. § (3)-(4)](https://njt.jog.gov.hu/jogszabaly/1995-117-00-00) |
| Szocho reduction, labour market entrants | For a Hungarian citizen insured for no more than 92 days in the 365 days before the job starts: up to 13% of the minimum wage a month in year one, then 6.5% for six months (18 months in all) | 2026 | [Szocho tv. 11. § (2)-(3)](https://njt.jog.gov.hu/jogszabaly/2018-52-00-00); [NAV information sheet 49, 3.2](https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/49.-A-szocialis-hozzajarulasi-ado-2026.-01.-16) |
| Late payment interest (késedelmi pótlék) | Central bank base rate plus 5 percentage points, divided by 365, per day. The base rate is 5.50% (held on 20 October 2026), so 10.50% a year | 2026 | [Art. 209. § (1)](https://njt.jog.gov.hu/jogszabaly/2017-150-00-00); [MNB, Monetary Council statement of 20 October 2026](https://www.mnb.hu/monetaris-politika/a-monetaris-tanacs/kozlemenyek/2026/kozlemeny-a-monetaris-tanacs-2026-oktober-20-i-uleserol) |
| Self-revision surcharge (önellenőrzési pótlék) | Central bank base rate divided by 365, per day; 1.5 times that on a repeat self-revision of the same return | 2026 | [Art. 212. § (1)-(1a)](https://njt.jog.gov.hu/jogszabaly/2017-150-00-00) |

## The taxable base

**Gross wage is the base for all three charges.** For an ordinary employee the base for the income tax advance, the TB contribution and the szocho is the same gross monthly wage (bér, Szja tv. 3. § 21.). The TB base is the income counted in the advance tax base (Tbj. 27. § (1) a)); the szocho base for employees equals the TB base (Szocho tv. 1. § (10)). There is no ceiling on any of them. The 89% rule in Szja tv. 29. § does not apply to wages, because the employee does not pay the szocho.

**Order of the base allowances (Szja tv. 29/H. § (1)).** The allowances reduce the consolidated tax base in this order: under-30 mothers; mothers of four or more, three or two children; the maternity and childcare benefit allowance; under-25s; the personal allowance for severe disability; first marriage; and family allowance last. The allowances that cut the tax in total cannot exceed the tax (Szja tv. 35. § (1)).

**The exemptions take the szja only.** The under-25 and mothers' exemptions remove income tax. They do not remove the 18.5% TB contribution or the employer's 13% szocho. Neither law changes the contribution or szocho base.

**Family allowance (Szja tv. 29/A.-29/B. §).**
- The parent entitled to family benefit (családi pótlék) claims it, or that parent's spouse living in the same household. Pregnancy counts from the 91st day.
- The amount per child depends on the number of dependants in the family, including children who no longer qualify but still count for family benefit. Two children in the family means HUF 266,660 for each qualifying child.
- Spouses or partners can claim it jointly or share it (29/B. § (1a)-(1d)). A child cared for in alternating weeks gives each parent 50% (29/B. § (1e)).
- In the year the employee claims it monthly through a written advance tax declaration (adóelőleg-nyilatkozat) to the employer (Szja tv. 48. § (2) c)).
- **Family contribution allowance (Tbj. 79. §).** If the family allowance is bigger than the month's tax base, the employer reduces the employee's 18.5% contribution by 15% of the unused part, up to the contribution itself. The employer simply withholds and pays that much less TB (79. § (3)). The employee can opt out (79. § (4)).

**Minimum wage floors.** An employer cannot pay a full-time employee less than HUF 322,800 a month, or HUF 373,200 where the job needs at least secondary education (426/2025. Korm. rendelet 2. §). Part-time pay is reduced in proportion (2. § (5)). Separately, the TB base of an employee is at least HUF 96,840 a month (30% of the minimum wage), with the employer paying the difference (Tbj. 27. § (2), 23. § (3)); the floor does not apply to employees receiving childcare or nursing benefits (such as CSED, GYED, GYES) or to full-time students (27. § (3)).

**Szocho reductions.** The employer may cut its szocho for labour market entrants, mothers of three or more entering the labour market, staff with reduced work capacity, unskilled and farm jobs, researchers and some trainees (Szocho tv. 10.-17. §; NAV sheet 49). The unskilled and farm jobs reduction is 50% of the 13% on the gross wage, up to the minimum wage (Szocho tv. 10. § (2); NAV sheet 49, 3.1).

## Deadlines and filing

| What | When | Where |
|---|---|---|
| Register the employee (biztosítotti bejelentés) | Before work starts, at the latest on the first day of the insurance; end of employment within 8 days | NAV, form 08E (named T1041 until 2025; T1041INT for a foreign employer filing itself) |
| Withhold the szja advance and TB, compute the szocho | Each payroll | Employer's payroll |
| Monthly return on payments to individuals (the '08 return, form 2608 for 2026) | By the 12th of the month after the month the wage is accounted for | NAV, electronically (Art. 50. § (1)) |
| Pay the szja advance, TB and szocho | Same day as the return | NAV accounts |
| Foreign employer filing directly or through the employee | By the 12th of the following month (form 2608INT) | NAV (Tbj. 87. § (6)) |
| Employee's annual szja return | 20 May 2027 for tax year 2026; NAV prepares a draft that becomes the return if not changed | NAV eSZJA |

Sources: Art. 50. § (1); NAV information sheet 24, 2.1 ("by the 12th of the month after the accounted month"); NAV form page for 2608 ("Havi bevallás a kifizetésekkel, juttatásokkal összefüggő adóról, járulékokról és egyéb adatokról"). Registration: Art. 1. melléklet 3. pont, as set out in NAV's 08E filling guide, section 5 ("A foglalkoztatás megkezdése előtt kell bejelenteni ... legkésőbb a biztosítási jogviszony első napján").

## Penalties and interest

- **Late payment interest (Art. 209. § (1)).** For each day late, the central bank base rate plus 5 percentage points, divided by 365.
- **Tax penalty (adóbírság, Art. 215. § (3)-(4)).** 50% of the shortfall found on audit; 200% where income was hidden or records falsified.
- **Default fine (mulasztási bírság, Art. 220. § (1)).** Up to HUF 1,000,000 for a company and HUF 400,000 for an individual for a late, missing or wrong return.
- **Missed return: the warning ladder (Art. 221. §).** NAV first sends a 15-day notice. If the return is still missing, a fixed fine of HUF 200,000 for a company (HUF 50,000 for an individual) and a second notice; then HUF 500,000 (HUF 200,000).
- **Tax not withheld or not paid over (Art. 232. §).** An employer that fails to withhold, or withholds and does not pay, owes late payment interest plus a default fine of up to 50% of the amount.
- **Unregistered employee (Art. 225. § (1)).** Fine up to HUF 2,000,000 per employee. A late registration made before an audit starts is fined only for lateness, and the fine can be waived (225. § (2)). A wrong or incomplete registration: up to HUF 500,000 (225. § (3)).
- **Self-correction (önellenőrzés).** Correcting a return before NAV finds the error carries a self-revision surcharge (Art. 211. §) of the central bank base rate divided by 365 per day (Art. 212. § (1)). No surcharge is due when the employer corrects the '08 return because the employee's declaration was wrong (Art. 211. § (3) b)).

## Cross-border points

- **Who is insured where.** Inside the EU/EEA and Switzerland, Regulation (EC) 883/2004 decides which country's social security applies. A worker posted into Hungary with an A1 certificate from another state does not pay Hungarian TB. No szocho is due on the income of a person insured in another member state under the coordination regulations; the exemption is proven with the foreign authority's certificate (Szocho tv. 5. § (4); for bilateral social security agreements 5. § (4a)). A Hungarian worker sent abroad stays insured in Hungary if the Regulation or a bilateral agreement says so (Tbj. 6. § (3)).
- **Foreign employer.** A foreign employer with no Hungarian registration still owes Hungarian contributions for insured staff working in Hungary (Tbj. 87. §). For a posting where the Hungarian host pays the wage, or for agency work, the Hungarian host or user carries the duty (87. § (5)).
- **Income tax.** A non-resident employee working in Hungary is taxed on the Hungarian-sourced wage unless a tax treaty gives the right to the other state (for example under the 183-day rule). Treaty relief and residence are left to the cross-border skill, which is not written yet.
- **Family allowance for EEA families.** The allowance also applies to families entitled to an equivalent family benefit in another EEA state or a neighbouring non-EEA state (Szja tv. 29/B. § (5)).

## Worked examples

### Example 1: employee on HUF 800,000 gross a month, no allowances

Anna is 35, has no children and earns HUF 800,000 gross a month. The employer withholds 18.5% TB contribution (HUF 148,000) and 15% income tax advance (HUF 120,000). Her net pay is HUF 532,000. The employer also pays 13% szocho on the gross (HUF 104,000), so the monthly cost to the employer is HUF 904,000. All three amounts go on the employer's 2608 return and are paid by the 12th of the next month.

```oa-check
name: HU payroll 2026, HUF 800,000 gross, no allowances
inputs:
  gross: 800000
  tb_rate_pct: 18.5
  szja_rate_pct: 15
  szocho_rate_pct: 13
steps:
  - tb: gross * tb_rate_pct / 100
  - szja: gross * szja_rate_pct / 100
  - net: gross - tb - szja
  - szocho: gross * szocho_rate_pct / 100
  - employer_cost: gross + szocho
expected:
  tb: 148000
  szja: 120000
  net: 532000
  szocho: 104000
  employer_cost: 904000
```

### Example 2: the same wage, two children, family allowance

Bence earns the same HUF 800,000 gross. He has two children who qualify for family benefit and he claims the whole family allowance through his advance tax declaration. With two children in the family the allowance is HUF 266,660 per child, so HUF 533,320 a month comes off his tax base. The tax base falls to HUF 266,680 and the income tax advance to HUF 40,002. The allowance is fully used against the tax base, so there is nothing left for the family contribution allowance and the TB stays at HUF 148,000. Net pay rises to HUF 611,998, a monthly gain of HUF 79,998. The employer's cost does not change: the szocho is still 13% of the gross.

The edge case is a lower wage. On HUF 400,000 gross with the same two children, the allowance is larger than the wage. The tax base is nil, and HUF 133,320 of allowance is unused. The family contribution allowance is 15% of that, HUF 19,998, which comes off his HUF 74,000 TB contribution, so the employer withholds HUF 54,002 of TB.

```oa-check
name: HU payroll 2026, HUF 800,000 gross, two children, family allowance
inputs:
  gross: 800000
  children: 2
  allowance_per_child: 266660
  low_gross: 400000
steps:
  - family_allowance: children * allowance_per_child
  - tax_base: max(gross - family_allowance, 0)
  - szja: tax_base * 15 / 100
  - unused_allowance: max(family_allowance - gross, 0)
  - tb_before_relief: gross * 18.5 / 100
  - contribution_relief: min(unused_allowance * 15 / 100, tb_before_relief)
  - tb: tb_before_relief - contribution_relief
  - net: gross - tb - szja
  - szocho: gross * 13 / 100
  - employer_cost: gross + szocho
  - monthly_gain: 120000 - szja
  - low_unused: max(family_allowance - low_gross, 0)
  - low_tb_before: low_gross * 18.5 / 100
  - low_relief: min(low_unused * 15 / 100, low_tb_before)
  - low_tb: low_tb_before - low_relief
expected:
  family_allowance: 533320
  tax_base: 266680
  szja: 40002
  contribution_relief: 0
  tb: 148000
  net: 611998
  employer_cost: 904000
  monthly_gain: 79998
  low_relief: 19998
  low_tb: 54002
```

If the same household's mother were the employee, born in 1986 or later, her whole wage would be exempt under the two-children mothers' rule (applied before the family allowance). The family allowance would then be unused and would flow to the contribution allowance, or could be shared with her spouse. Run that case on the actual facts.

## Ask the client first

1. Is this a munkaviszony, or another contract (megbízás, simplified employment, director)? The rules here are for employment.
2. Does the job need at least secondary education? That sets the minimum wage at HUF 373,200 instead of HUF 322,800.
3. The employee's date of birth, sex and children: number of children in the family who count for family benefit, how many qualify, any long-term ill child, and the mother's year of birth. These decide the under-25, mothers' and family allowances.
4. Has the employee given an advance tax declaration (adóelőleg-nyilatkozat), and is the family allowance shared with a spouse?
5. Is the employee posted from or to another country, or paid by a foreign employer? Ask for any A1 certificate.
6. Does the employer qualify for a szocho reduction (labour market entrant, unskilled or farm job, reduced work capacity)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Szja tv., Act CXVII of 1995 (personal income tax), 3. § 21., 8. §, 29.-29/H. §, 35. §, 46.-49. §, version in force from 2026-10-01 | https://njt.jog.gov.hu/jogszabaly/1995-117-00-00 | 2026-10-23 |
| Tbj., Act CXXII of 2019 (social security), 6. §, 23.-27. §, 79.-81. §, 87. § | https://njt.jog.gov.hu/jogszabaly/2019-122-00-00 | 2026-10-23 |
| Szocho tv., Act LII of 2018 (social contribution tax), 1.-2. §, 36/E. § | https://njt.jog.gov.hu/jogszabaly/2018-52-00-00 | 2026-10-23 |
| Art., Act CL of 2017 (tax procedure), 50. §, 209. §, 211.-212. §, 215. §, 220.-221. §, 225. §, 232. § | https://njt.jog.gov.hu/jogszabaly/2017-150-00-00 | 2026-10-23 |
| Act LV of 2024, 4. § and 217. § (family allowance amounts and their start dates) | https://njt.jog.gov.hu/jogszabaly/2024-55-00-00 | 2026-10-23 |
| Act XIII of 2025 (mothers under 30) | https://njt.jog.gov.hu/jogszabaly/2025-13-00-00 | 2026-10-23 |
| Act XIV of 2025 (mothers of two children) | https://njt.jog.gov.hu/jogszabaly/2025-14-00-00 | 2026-10-23 |
| Act XV of 2025 (mothers of three children) | https://njt.jog.gov.hu/jogszabaly/2025-15-00-00 | 2026-10-23 |
| Act CLV of 2011 (vocational training contribution), repeal note | https://njt.jog.gov.hu/jogszabaly/2011-155-00-00 | 2026-10-23 |
| Government Decree 426/2025. (XII. 23.) on the 2026 minimum wage and guaranteed minimum wage | https://njt.jog.gov.hu/jogszabaly/2025-426-20-22 | 2026-10-23 |
| NAV information sheet 73, Szja adóalap-kedvezmények (2026-03-19) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/73.-Szja-adoalap-kedvezmenyek-2026.-03.19 | 2026-10-23 |
| NAV information sheet 49, A szociális hozzájárulási adó (2026-01-16) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/49.-A-szocialis-hozzajarulasi-ado-2026.-01.-16 | 2026-10-23 |
| NAV information sheet 24, Bevallási, adófizetési információk (2026-01-26) | https://nav.gov.hu/pfile/file?path=/ugyfeliranytu/nezzen-utana/inf_fuz/2026/24.-Bevallasi-adofizetesi-informaciok-2026.01.26 | 2026-10-23 |
| NAV form 2608, monthly return on payments to individuals | https://nav.gov.hu/nyomtatvanyok/letoltesek/nyomtatvanykitolto_programok/nyomtatvanykitolto_programok_nav/2608 | 2026-10-23 |
| NAV form 08E (registration of insured employees, replaced T1041 from 2026-01-01) and its filling guide, section 5 | https://nav.gov.hu/nyomtatvanyok/letoltesek/nyomtatvanykitolto_programok/nyomtatvanykitolto_programok_nav/08E | 2026-10-23 |
| MNB, Monetary Council statement of 20 October 2026 (base rate 5.50%) | https://www.mnb.hu/monetaris-politika/a-monetaris-tanacs/kozlemenyek/2026/kozlemeny-a-monetaris-tanacs-2026-oktober-20-i-uleserol | 2026-10-23 |

Not yet confirmed: the text of Art. 1. melléklet 3. pont itself (the registration timing is taken from NAV's 08E filling guide; the annex did not load on njt.jog.gov.hu); the conditions of each szocho reduction other than the labour market entrants and the unskilled and farm jobs (read in Szocho tv. 10.-11. §); the employer's year-end tax assessment rules; the rules for fringe benefits, simplified employment and the rehabilitation contribution.

> Contributed by Ryan Duguid.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `hu-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/hu-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
