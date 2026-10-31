---
name: bosnia-tax-optimization
description: Use this skill whenever asked about reducing tax in Bosnia and Herzegovina, tax planning, or legal strategies to minimise tax for a self-employed person or small company, tax year 2026. Trigger on phrases like "reduce tax Bosnia", "flat 10% tax Bosnia", "small entrepreneur 2%", "FBiH vs RS tax", "sole proprietor vs doo Bosnia", "0% dividend Bosnia", "save tax Bosnia", "tax planning Bosnia". This skill covers the flat income tax (FBiH 10%, RS 8% on salary, Brčko 10%) and the monthly allowances, the RS small-entrepreneur 2%-of-revenue option, the FBiH-vs-RS choice for salaries and contributions, the 10% profit tax with no income tax on dividends to FBiH, RS and Brčko residents, and the disguised-employment red line. ALWAYS read this skill before advising on any Bosnia and Herzegovina tax optimisation. The detailed computations are out of scope and sit in bosnia-income-tax, bosnia-payroll, bosnia-social-contributions and ba-corporate-income-tax.
version: 0.2
jurisdiction: BA
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bosnia and Herzegovina Tax Optimization

## Bosnia and Herzegovina Tax Optimization Skill v0.2

**Tier 2. Sources: the FBiH, RS and Brčko District laws and the RS Tax Administration's 2026 guidance, read on 30 October 2026 and listed in Sources below. Figures must agree with `bosnia-income-tax.md`, `bosnia-social-contributions.md`, `bosnia-payroll.md` and `ba-corporate-income-tax.md`; those skills win if they differ. No Bosnian tax adviser has signed this off. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Bosnia and Herzegovina: two entities, the Federation of BiH (FBiH) and Republika Srpska (RS), plus Brčko District (BD) |
| Currency | KM (BAM, convertible mark) |
| Headline levers | Flat low income tax; RS small entrepreneur **2% of revenue**; no income tax on dividends to FBiH, RS and BD residents; choice of entity for salaries and contributions |
| Income tax on salary | **FBiH 10%** after contributions; **RS 8%** of gross; **BD 10%** after contributions |
| Monthly personal allowance | **FBiH KM 300**; **RS KM 1,000**; **BD KM 1,200** |
| Employee contributions | **FBiH 31%** of gross plus **5%** employer (from July 2025); **RS 31%** of gross, all employee-borne |
| Profit tax | **10%** in FBiH, RS and BD |
| Dividends to resident individuals | Not income in FBiH and BD; no income tax in RS |
| VAT | 17%; registration from KM 100,000 turnover |

> **A low, mostly flat system:** 10% profit tax everywhere, 8% to 10% income tax, and no income tax on dividends to FBiH, RS and BD residents. The planning is mostly about regime choice (the RS 2%-of-revenue small entrepreneur, the FBiH flat-rate tax) and the FBiH-vs-RS differences in allowances and contributions.

## Section 2 -- Regime Choice (sole proprietor)

**Regime Choice (sole proprietor)**

| Route | Treatment | Best when |
| --- | --- | --- |
| **RS small entrepreneur: 2% of revenue** | 2% of total revenue, no expense deductions; minimum KM 1,200 a year, or KM 600 if revenue is not above KM 50,000; paid monthly by the 10th | Low real expenses; revenue up to KM 100,000 |
| **RS normal self-employment** | 10% income tax on profit (revenue less expenses) _(RS Zakon o porezu na dohodak art. 4(2), as amended by 119/21)_ | Real expenses high relative to revenue |
| **FBiH flat-rate (paušal) or net-profit basis** | Fixed monthly amounts by activity, or 10% on profit | See `bosnia-income-tax.md` for the flat-rate amounts and entry tests |

- **RS small-entrepreneur entry tests (all year)**: an entrepreneurial activity, not one of the independent professions (such as lawyers, doctors, engineers, accountants, consultants); at most three workers; annual revenue not above KM 100,000 and not registered for VAT; no joint activity; no outside investors _(RS Zakon o porezu na dohodak art. 21, as replaced by 110/24)_
- **RS small-entrepreneur tax**: 2% of total revenue _(art. 23(1))_, at least KM 1,200 a year _(art. 23(2), as amended by 110/24)_, or at least KM 600 if revenue is not above KM 50,000 _(art. 23a, added by 110/24)_. Paid on monthly revenue by the 10th of the next month _(art. 24(1))_
- **When 2% wins**: 2% of revenue costs less than 10% tax on profit when profit is more than 20% of revenue (income tax only; contributions are separate). Example: revenue KM 60,000 gives 2% x 60,000 = KM 1,200, equal to the KM 1,200 minimum for revenue above KM 50,000. On the normal basis the same tax needs a profit of only KM 12,000 (10% x 12,000 = KM 1,200); any higher profit makes the 2% option cheaper.
- **VAT link**: the RS option ends once the business is VAT-registered, and VAT registration is compulsory above KM 100,000 _(Zakon o PDV art. 57(1), as amended by 80/23)_

## Section 3 -- Entity / Region (FBiH vs RS)

- **Allowance and rate**: RS taxes salary at 8% of gross less a KM 1,000 monthly allowance, and contributions are not deducted from the tax base. FBiH taxes salary at 10% after contributions and a KM 300 monthly allowance _(RS Tax Administration, Form 1002 notice, 2026; FBiH Zakon o porezu na dohodak arts. 9, 24(1))_
- **Contributions**: RS contributions are 31% of gross, all withheld from the employee (pension 18.5%, health 10.2%, unemployment 0.6%, child protection 1.7%). FBiH employees pay 31% and the employer adds 5% for pay from 1 July 2025 _(RS Zakon o doprinosima art. 22(1) as amended; FBiH Zakon o doprinosima art. 10 as amended by 33/25)_. See `bosnia-payroll.md`.
- **Brčko District**: 10% income tax with a KM 1,200 monthly allowance _(BD Zakon o porezu na dohodak art. 10; art. 25(1) as amended by 21/22)_. BD contribution rates are in `bosnia-payroll.md` and `bosnia-social-contributions.md`.
- **Region of registration materiality**: where the person is genuinely free to choose, the entity of the employer's seat changes net pay and employer cost. AUDIT FLASH POINT: registering in an entity without genuine presence is challengeable.

**Illustration: gross salary KM 2,000 a month, single employee with no dependants, no tax-free parts**

FBiH: employee contributions 31% are KM 620. The tax base is 2,000 - 620 - 300 = KM 1,080, and tax at 10% is KM 108. Net pay is KM 1,272. The employer adds 5%, KM 100, so the cost is KM 2,100.

RS: contributions 31% are KM 620. The tax base is 2,000 - 1,000 = KM 1,000, and tax at 8% is KM 80. Net pay is KM 1,300. The employer pays no contributions on top, so the cost is KM 2,000.

```oa-check
name: Gross KM 2,000 salary, FBiH vs RS, 2026
inputs:
  gross: 2000
  fbih_allowance: 300
  rs_allowance: 1000
steps:
  - fbih_contrib: gross * 0.31
  - fbih_base: gross - fbih_contrib - fbih_allowance
  - fbih_tax: fbih_base * 0.10
  - fbih_net: gross - fbih_contrib - fbih_tax
  - fbih_employer_cost: gross + gross * 0.05
  - rs_contrib: gross * 0.31
  - rs_base: gross - rs_allowance
  - rs_tax: rs_base * 0.08
  - rs_net: gross - rs_contrib - rs_tax
  - rs_employer_cost: gross
expected:
  fbih_contrib: 620
  fbih_base: 1080
  fbih_tax: 108
  fbih_net: 1272
  fbih_employer_cost: 2100
  rs_contrib: 620
  rs_base: 1000
  rs_tax: 80
  rs_net: 1300
  rs_employer_cost: 2000
```

The minimum contribution bases, tax-free parts and dependant allowances change these numbers. Use `bosnia-payroll.md` for a real payslip.

## Section 4 -- Company Extraction (doo)

- **Profit tax and dividends**: profit tax is 10% in all three parts of the country _(FBiH Zakon o porezu na dobit art. 31; RS art. 36(1); BD art. 20(1))_. Dividends paid to an FBiH resident individual are not income for income tax _(FBiH Zakon o porezu na dohodak art. 5(1)(1))_. In the RS, income tax is not paid on dividends and profit shares _(RS Zakon o porezu na dohodak art. 8(4)(14): art. 8(3)(13) of 60/15, renumbered by 105/19 and 112/23)_. In BD, dividends and profit shares are not income _(BD Zakon o porezu na dohodak art. 6(a))_. For a resident owner, 10% profit tax is then the whole tax on distributed profit.
- **Foreign owner**: withholding tax applies on dividends paid abroad: FBiH 5%, RS 10%, BD none, unless a treaty lowers it _(FBiH art. 38(7); RS art. 44 as amended by 1/17; BD art. 29(2)(d))_. See `ba-corporate-income-tax.md`.
- **No dividend while in arrears**: a company cannot pay a dividend while it owes direct taxes or contributions (FBiH) or overdue taxes (RS) _(FBiH Zakon o porezu na dobit art. 55(1); RS art. 54)_
- **Salary vs dividends balance**: the owner balances a contribution-bearing salary against dividends. The salary must be genuine.

## Section 5 -- Red Lines (do not cross)

- **Disguised employment**: a single-client sole proprietor working under employer-like control risks reclassification. AUDIT FLASH POINT.
- **Region shopping**: registering in a region without genuine presence or substance is challengeable.
- **No double-counting of expenses**: the RS 2%-of-revenue option allows no expense deductions. Do not also deduct real expenses.
- **Independent professions**: lawyers, health workers, engineers, accountants, consultants and the other independent professions cannot use the RS small-entrepreneur option _(RS art. 21 as replaced by 110/24, referring to art. 14)_

## PROHIBITIONS

- **Prohibition 1**: NEVER combine the 2%-of-revenue regime with real-expense deductions.
- **Prohibition 2**: NEVER register in RS or FBiH purely for the rate without genuine presence.
- **Prohibition 3**: NEVER present single-client work as safe self-employment.
- **Prohibition 4**: NEVER contradict the rates in bosnia-income-tax.md, bosnia-social-contributions.md, bosnia-payroll.md and ba-corporate-income-tax.md (RS contributions 31% employee-borne; FBiH employer 5% from 1 July 2025).
- **Prohibition 5**: NEVER present items on the "Not yet confirmed" line as confirmed, nor optimisation as definitive advice. Route to a licensed Bosnian tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Bosnia and Herzegovina) before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Sources

| Source | URL | Read on |
|---|---|---|
| RS Zakon o porezu na dohodak 60/15: arts. 4, 8(3)(13), 14, 21 to 24 | https://www.poreskaupravars.org/dokumenti/zakoni/zakonoporezunadohodak6015.pdf | 2026-10-30 |
| RS amendment 119/21 to the income tax law (art. 4(2): 10% on self-employment income; art. 10(3)(1): KM 12,000 allowance) | https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20doprinosima.pdf | 2026-10-30 |
| RS amendment 105/19 to the income tax law (art. 8 paragraphs renumbered) | https://www.poreskaupravars.org/dokumenti/zakoni/sluzbeni%20glasnik%20105-zakon%20o%20izmjenama%20i%20dopuni%20zakona%20o%20porezu%20na%20dohodak.pdf | 2026-10-30 |
| RS amendment 112/23 to the income tax law (art. 8(4) points renumbered) | https://poreskaupravars.org/wp-content/uploads/2023/12/Scan26122023.pdf | 2026-10-30 |
| RS amendment 110/24 to the income tax law (arts. 21, 23(2), 23a) | https://poreskaupravars.org/wp-content/uploads/2025/01/Scan29012025.pdf | 2026-10-30 |
| Poreska uprava RS, notice on Form 1002 from 1 January 2026 (8% tax, KM 1,000 allowance, 31% contributions) | https://poreskaupravars.org/izmjene-u-podnosenju-obrasca-1002-od-01-01-2026-godine-3/ | 2026-10-30 |
| RS Zakon o doprinosima 114/17, art. 22, as amended by 112/19 and 119/21 | https://www.poreskaupravars.org/dokumenti/zakoni/Zakon-o-doprinosima-SLGL-114_17.pdf | 2026-10-30 |
| RS amendment 119/21 to the contributions law (health 10.2%) | https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20doprinosima.pdf | 2026-10-30 |
| RS Zakon o porezu na dobit 94/15 (arts. 36, 44, 54) and 1/17 | https://www.poreskaupravars.org/dokumenti/zakoni/Zakon%20o%20porezu%20na%20dobit%20od%2001_01_2016.pdf | 2026-10-30 |
| FBiH Zakon o porezu na dohodak (consolidated to 65/13): arts. 5, 9, 24 | https://www.pufbih.ba/v1/public/upload/zakoni/d9bf6-zakon-o-porezu-na-dohodak-ispravan-tekst.pdf | 2026-10-30 |
| FBiH Zakon o doprinosima (consolidated to 33/25): art. 10 | https://www.pufbih.ba/v1/public/upload/zakoni/2dcc6-zakon-o-doprinosima-precisceni-tekst-25.pdf | 2026-10-30 |
| FBiH Zakon o porezu na dobit 15/16 and 15/20 (consolidated): arts. 31, 38, 55 | https://ik.imagekit.io/9qcwbg8wl/15-16_i_15-20-zakon-o-porezu-na-dobit-precisceni_07YP9wNd9.pdf | 2026-10-30 |
| BD Zakon o porezu na dohodak (unofficial consolidated text): arts. 6, 10 | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/Nesluz--bena%20prec--is--c-ena%20verzija%20Zakona%20o%20porezu%20na%20dohodak%20B.pdf | 2026-10-30 |
| BD amendment 21/22 to the income tax law: art. 25(1) | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dohodak/04B21-22%20Zakon%20o%20izmjenama%20i%20dopuni%20Zakona%20o%20porezu%20na%20dohodak.pdf | 2026-10-30 |
| BD Zakon o porezu na dobit (consolidated 17/22): arts. 20, 29 | https://skupstinabd.ba/3-zakon/ba/Zakon%20o%20porezu%20na%20dobit/05B17-22%20Zakon%20o%20porezu%20na%20dobit%20-%20prec--is--eni%20tekst.pdf | 2026-10-30 |
| Zakon o porezu na dodanu vrijednost: art. 57; amendment 80/23 (KM 100,000) | https://www.uino.gov.ba/portal/wp-content/uploads/PROPISI/2_Porezi/1_PDV/1_Zakon_o_PDV/B/B-H-S-1-5-Z-o-PDV-sl-list-80-23-24-11-23.pdf | 2026-10-30 |

Not yet confirmed: the RS 8% salary rate in the text of the law itself (RS income tax law art. 4(1) after 119/21 was not on the scanned page; the 8% is taken from the RS Tax Administration's 2026 example); Brčko contribution rates, so no Brčko salary illustration is given; the contributions a self-employed person pays in each entity (left to bosnia-social-contributions); the FBiH flat-rate (paušal) entry tests (amounts are in bosnia-income-tax).

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
