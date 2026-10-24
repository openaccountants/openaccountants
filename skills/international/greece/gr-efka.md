---
name: gr-efka
description: "Greek e-EFKA social insurance contributions of the self-employed for 2026: freelancers (ελεύθεροι επαγγελματίες), the self-employed (αυτοαπασχολούμενοι) and farmers insured under the former OGA. Covers the six insurance categories and their 2026 monthly amounts under e-EFKA circular 6/2026 (main pension, health in cash and in kind), the special category for the first five years of insurance, the EUR 10 unemployment (DYPA, former OAED) charge, the three supplementary and three lump-sum categories, farmers' six categories, the annual category choice, parallel employment, the payment deadline (last working day of the following month), late payment and KEAO, and how paid contributions reduce business profit. Trigger on: EFKA contributions, εισφορές μη μισθωτών 2026, ασφαλιστική κατηγορία, ειδική κατηγορία νέων, ελεύθερος επαγγελματίας ΕΦΚΑ, Greek freelancer social security. Out of scope: gr-employee-contributions (employees and employers), gr-income-tax (the tax computation), gr-cross-border (A1 and residence)."
version: 2.1
jurisdiction: GR
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Greece: social insurance contributions of the self-employed (e-EFKA), 2026

Since 1 January 2020 the self-employed in Greece do not pay contributions on their income. Each person is placed in an insurance category and pays a fixed monthly amount for it, whatever they earn ([e-EFKA circular 3/2020](https://www.e-efka.gov.gr/sites/default/files/2021-08/%CE%95%CE%93%CE%9A%CE%A5%CE%9A%CE%9B%CE%99%CE%9F%CE%A3%203-2020.pdf)). The 2026 amounts are in [e-EFKA circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026). This skill links to the pack's other skills rather than repeating them:

- `gr-employee-contributions`: contributions on employees' pay (employer and employee shares, the APD return).
- `gr-income-tax`: income tax on business profit, where paid contributions are deducted.
- `gr-cross-border`: tax residence, the inbound regimes and EU social security (Regulation 883/2004, A1).

## Who this applies to

- **Freelancers and the self-employed** with a compulsory insurance obligation to e-EFKA and on its non-salaried register, including traders (former OAEE) and liberal professions such as engineers, lawyers and doctors ([circular 3/2020](https://www.e-efka.gov.gr/sites/default/files/2021-08/%CE%95%CE%93%CE%9A%CE%A5%CE%9A%CE%9B%CE%99%CE%9F%CE%A3%203-2020.pdf), section 3).
- **Farmers** insured under the former OGA rules. They have their own six categories ([circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026), section A.2).
- **Choice of category.** Being placed in a category is compulsory. Which category is a free choice. It does not depend on years of activity or income ([e-EFKA FAQ, contributions of freelancers, the self-employed and farmers](https://www.e-efka.gov.gr/el/nees-eisphores-eleytheron-epaggelmation-aytotelos-apascholoymenon-kai-agroton)). Older material that ties a minimum category to years in business does not describe the system in force since 2020.
- **New entrants.** In the first five years of insurance a freelancer or self-employed person may choose the special category instead (see the table). Pensioners who take up self-employment cannot (circular 3/2020, section 4.B).

Out of this skill:

- Freelancers paid on service invoices (ΔΠΥ) whose income comes from no more than two clients. Under art. 39(9) ν. 4387/2016 they are insured under employee rules and their contributions go on the client's APD. See `gr-employee-contributions` (same FAQ; circular 3/2020, section Z).
- Paid board members of an AE. Their board fees are insured under employee rules (same FAQ).
- Professional chamber fees (bar association, TEE, medical associations). They are separate from e-EFKA.

## Rates, bands and thresholds

All amounts are monthly, in euro, from 1 January 2026. They are the 2025 amounts raised by 2.5%, the 2025 rise in the consumer price index, under ministerial decision Δ.15/Δ΄/1865/2026 (ΦΕΚ Β΄ 318/29.01.2026) ([circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026)).

**Freelancers and the self-employed: main pension and health**

| Category | Main pension | Health, cash | Health, in kind | Total a month | Year | Source |
|---|---|---|---|---|---|---|
| 1st | 185.09 | 5.97 | 59.71 | 250.77 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |
| 2nd | 222.12 | 7.16 | 71.65 | 300.93 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |
| 3rd | 281.82 | 7.16 | 71.65 | 360.63 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |
| 4th | 354.66 | 7.16 | 71.65 | 433.47 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |
| 5th | 440.64 | 7.16 | 71.65 | 519.45 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |
| 6th | 597.06 | 7.16 | 71.65 | 675.87 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |
| Special category (first five years of insurance) | 111.06 | 3.58 | 35.82 | 150.46 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |

**Collected with the main contribution**

| Item | Amount a month | Year | Source |
|---|---|---|---|
| Unemployment branch (DYPA, still named OAED in the circular), freelancers and the self-employed, every category including the special one | EUR 10 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026); [circular 3/2020](https://www.e-efka.gov.gr/sites/default/files/2021-08/%CE%95%CE%93%CE%9A%CE%A5%CE%9A%CE%9B%CE%99%CE%9F%CE%A3%203-2020.pdf), section 4.B |
| Health professionals' housing fund (Στέγη Υγειονομικών), health professionals only | EUR 2 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |

**Supplementary pension and lump-sum branches** (only for activities compulsorily insured in those branches; supplementary goes to e-EFKA or TEKA)

| Category | Supplementary | Lump sum (εφάπαξ) | Year | Source |
|---|---|---|---|---|
| 1st | 46.57 | 31.05 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026), sections B and Γ |
| 2nd | 56.13 | 37.02 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026), sections B and Γ |
| 3rd | 66.88 | 44.18 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026), sections B and Γ |

**Farmers (former OGA)**

| Category | Main pension | Health, cash | Health, in kind | Farmers' housing (ΛΑΕ) | Total a month | Year | Source |
|---|---|---|---|---|---|---|---|
| 1st | 108.67 | 3.58 | 34.63 | 2.39 | 149.27 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |
| 2nd | 131.35 | 3.58 | 41.79 | 2.39 | 179.11 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |
| 3rd | 165.99 | 3.58 | 41.79 | 3.58 | 214.94 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |
| 4th | 208.98 | 3.58 | 41.79 | 3.58 | 257.93 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |
| 5th | 260.33 | 3.58 | 41.79 | 4.78 | 310.48 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |
| 6th | 352.28 | 3.58 | 41.79 | 7.16 | 404.81 | 2026 | [circular 6/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026) |

**Reductions and floors**

| Item | Rule | Year | Source |
|---|---|---|---|
| Mothers | Main pension contribution cut by 50% for the first 12 months after the birth. This covers freelancers, the self-employed and farmers. Apply to the local e-EFKA office with the birth certificate; there is no deadline, and the 12 months are recalculated once the application is recorded. A mother already in the special category gets the cut on the 1st category pension amount instead, as only the larger reduction applies | 2026 | [e-EFKA FAQ, reduced contributions for mothers](https://www.e-efka.gov.gr/el/sychnes-eroteseis/asphalisi-eisphores/asphalismenoi/me-misthotoi-0/meiomenes-eisphores-gia-meteres-me-misthotes); [circular 3/2020](https://www.e-efka.gov.gr/sites/default/files/2021-08/%CE%95%CE%93%CE%9A%CE%A5%CE%9A%CE%9B%CE%99%CE%9F%CE%A3%203-2020.pdf), section ΣΤ |
| Parallel employment | Contributions on all activities together must reach at least the 2nd category. Employee contributions already paid count towards it, and only the shortfall is paid. In the special category the floor is the 1st category. In the supplementary and lump-sum branches the floor is the category chosen in that branch, and only the difference is paid | 2026 | [circular 3/2020](https://www.e-efka.gov.gr/sites/default/files/2021-08/%CE%95%CE%93%CE%9A%CE%A5%CE%9A%CE%9B%CE%99%CE%9F%CE%A3%203-2020.pdf), section Δ; [e-EFKA FAQ, supplementary contributions](https://www.e-efka.gov.gr/el/eisphores-0); [e-EFKA FAQ, lump-sum contributions](https://www.e-efka.gov.gr/el/sychnes-eroteseis/asphalisi-eisphores/asphalismenoi/me-misthotoi-0/epikoyrike-asphalise-kai-ephapax-paroche-pronoia-sychnes-erotapan/ephapax-paroche-pronoia/ephapax-paroche-pronoia-eisphores) |

## The taxable base

There is no income base. The contribution is the fixed monthly amount for the chosen category in each branch, plus the amounts collected with it.

- **How the category is set.** Main pension and health go together: the health amount follows the pension category. The supplementary and lump-sum categories are chosen separately and need not match the main category ([circular 3/2020](https://www.e-efka.gov.gr/sites/default/files/2021-08/%CE%95%CE%93%CE%9A%CE%A5%CE%9A%CE%9B%CE%99%CE%9F%CE%A3%203-2020.pdf); [e-EFKA FAQ, supplementary contributions](https://www.e-efka.gov.gr/el/eisphores-0)).
- **Changing category.** A person may move up or down once a year through the e-EFKA online service. The service is open in December and January, and the new category applies from 1 January of the following year. Anyone who does not apply stays in last year's category ([e-EFKA general document 1811441/13.07.2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/geniko-eggrafo-181144113-07-2026), section 7).
- **The special category.** It can be chosen at the start of insurance or later, for whatever remains of the first five years, and only once. During those five years the person may move to one of the six categories for a year and come back. When the five years are complete the person moves to the 1st category until the end of that year, unless they had chosen a higher one. Someone with more than one self-employed activity cannot use it ([circular 3/2020](https://www.e-efka.gov.gr/sites/default/files/2021-08/%CE%95%CE%93%CE%9A%CE%A5%CE%9A%CE%9B%CE%99%CE%9F%CE%A3%203-2020.pdf), section 4.B; [e-EFKA FAQ](https://www.e-efka.gov.gr/el/nees-eisphores-eleytheron-epaggelmation-aytotelos-apascholoymenon-kai-agroton)).
- **More than one self-employed activity.** One contribution is paid, in one of the six categories, chosen freely. Farmers who must stay under the former OGA rules choose from the farmers' table ([circular 3/2020](https://www.e-efka.gov.gr/sites/default/files/2021-08/%CE%95%CE%93%CE%9A%CE%A5%CE%9A%CE%9B%CE%99%CE%9F%CE%A3%203-2020.pdf), section Δ.3).
- **Income tax.** Contributions are a business expense when computing business profit (art. 22 ν. 4172/2013). Contributions that were not paid cannot be deducted, and neither can surcharges for late payment (art. 23(γ) and (ε) ν. 4172/2013) ([Income Tax Code codification to ν. 5264/2025](https://minfin.gov.gr/koinopoiisi-kodikopoiisis-tou-kodika-forologias-eisodimatos-symfona-me-to-arthro-83-par-55-tou-n-5104-2024/)). The tax computation is in `gr-income-tax`.

## Deadlines and filing

- **No return.** The self-employed file no monthly return. e-EFKA posts a monthly payment notice (ειδοποιητήριο) in the person's account in the "Εισφορές Μη Μισθωτών" online service ([e-EFKA FAQ](https://www.e-efka.gov.gr/el/nees-eisphores-eleytheron-epaggelmation-aytotelos-apascholoymenon-kai-agroton)).
- **Payment deadline.** Each month's contributions are due by the last working day of the following month ([circular 3/2020](https://www.e-efka.gov.gr/sites/default/files/2021-08/%CE%95%CE%93%CE%9A%CE%A5%CE%9A%CE%9B%CE%99%CE%9F%CE%A3%203-2020.pdf), section 1). January 2026 contributions were due by Friday 27 February 2026. December 2026 contributions are due by Friday 29 January 2027.
- **One notice for everything.** Supplementary and lump-sum contributions are on the same notice as main pension and health, and are paid with the same RF payment code ([e-EFKA FAQ, supplementary contributions](https://www.e-efka.gov.gr/el/eisphores-0)). TEKA members see their supplementary contributions in TEKA's own online services (same page).
- **How to pay.** Through any bank or ELTA via DIAS, by payment order or standing order. From a SEPA bank, by euro transfer to IBAN GR16 0110 0400 0000 0400 1384 017 (BIC ETHNGRAA), quoting the RF code on the notice ([e-EFKA FAQ](https://www.e-efka.gov.gr/el/nees-eisphores-eleytheron-epaggelmation-aytotelos-apascholoymenon-kai-agroton)).
- **Category choice.** December to January, for the following year (see the base section).

## Penalties and interest

- **Late payment.** Contributions paid after the deadline carry interest at an annual rate equal to the European Central Bank refinancing rate plus 800 basis points (art. 2(4) ν. 4158/2013, as set out in [circular 3/2020](https://www.e-efka.gov.gr/sites/default/files/2021-08/%CE%95%CE%93%CE%9A%CE%A5%CE%9A%CE%9B%CE%99%CE%9F%CE%A3%203-2020.pdf), section 6). The surcharges appear on the next monthly notice, are paid with the current RF code and are cleared first ([e-EFKA FAQ](https://www.e-efka.gov.gr/el/nees-eisphores-eleytheron-epaggelmation-aytotelos-apascholoymenon-kai-agroton)).
- **Transfer to KEAO.** Unpaid contributions become overdue debt once e-EFKA issues a debt assessment act (ΠΒΟ). It is drawn up in the month after the deadline and in any case within six months. The act goes to KEAO, the social security debt collection centre, within a month (same FAQ).
- **Missed instalments on a settlement.** Under the ν. 4152/2013 settlement as amended by ν. 4997/2022, one late instalment in each twelve months of the plan costs a 15% surcharge on that instalment. Under the art. 54 ν. 4305/2014 settlement, a late instalment costs 2% a month ([e-EFKA FAQ for debtors, KEAO](https://www.e-efka.gov.gr/el/sychnes-eroteseis/opheiletes-keao/themata-diakanonismoy-opheilon-sychn-erotapan-keao/genika)).
- **72-instalment scheme for old debt.** Debts for periods up to 31 December 2023 that were not in a settlement on 21 April 2026 can be spread over up to 72 monthly instalments (minimum EUR 30) under art. 22 ν. 5313/2026. Apply online to KEAO by 31 December 2026. Debts from 1 January 2024 must be settled at the same time under the standing settlement ([e-EFKA circular 15/2026](https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-152026)).
- **Tax.** Surcharges are not deductible for income tax (art. 23(ε) ν. 4172/2013).

## Cross-border points

- **One system at a time.** Under Regulation (EC) 883/2004, a self-employed person active in more than one EU/EEA state or Switzerland is insured in one state only. A person who holds an A1 from another state pays no e-EFKA contributions for the activity it covers. A Greek freelancer working temporarily in another member state needs an A1 from e-EFKA to stay in Greek insurance. See `gr-cross-border`.
- **Paying from abroad.** Contributions can be paid by SEPA transfer quoting the RF code (see Deadlines).

## Worked examples

### Example 1: established consultant in the 1st category, no supplementary branch

Eleni is a management consultant, a former OAEE trader with eight years of insurance and no supplementary or lump-sum obligation. She stayed in the 1st category for 2026. Each month she pays 250.77 for main pension and health plus EUR 10 for unemployment, EUR 260.77 in all. Over 2026 she pays EUR 3,129.24. Her January contributions were due by 27 February 2026. The contributions she actually pays are a business expense; any she leaves unpaid are not (art. 23(γ) ν. 4172/2013). Her December contributions fall due in January 2027, so which tax year they are deducted in is a question for `gr-income-tax`.

```oa-check
name: Freelancer, 1st category, 12 months of 2026, no supplementary
inputs:
  main_and_health_monthly: 250.77
  unemployment_monthly: 10
  months: 12
steps:
  - monthly_total: main_and_health_monthly + unemployment_monthly
  - annual_total: monthly_total * months
expected:
  monthly_total: 260.77
  annual_total: 3129.24
```

### Example 2: new engineer whose five years end mid-year, with supplementary and lump sum

Giorgos is a civil engineer. He was first insured on 1 July 2021 and chose the special category. His activity is compulsorily insured in the supplementary and lump-sum branches, where he is in the 1st category of each. His five years of insurance end on 30 June 2026. The edge case is the switch: from July to December 2026 he moves to the 1st category, as he did not choose a higher one.

From January to June he pays 150.46 plus EUR 10, EUR 160.46 a month. From July to December he pays 250.77 plus EUR 10, EUR 260.77 a month. Every month he also pays 46.57 supplementary and 31.05 lump sum, EUR 77.62. His total for 2026 is 6 x 160.46 + 6 x 260.77 + 12 x 77.62 = EUR 3,458.82.

```oa-check
name: Special category to 1st category on 1 July 2026, plus supplementary and lump sum
inputs:
  special_monthly: 150.46
  first_cat_monthly: 250.77
  unemployment_monthly: 10
  supplementary_monthly: 46.57
  lump_sum_monthly: 31.05
  months_special: 6
  months_first: 6
steps:
  - special_period: (special_monthly + unemployment_monthly) * months_special
  - first_period: (first_cat_monthly + unemployment_monthly) * months_first
  - other_branches: (supplementary_monthly + lump_sum_monthly) * (months_special + months_first)
  - annual_total: special_period + first_period + other_branches
expected:
  special_period: 962.76
  first_period: 1564.62
  other_branches: 931.44
  annual_total: 3458.82
```

## Ask the client first

1. When were you first insured anywhere in Greece, and are you a pensioner? (This decides whether the special category is open.)
2. Which category did you choose for 2026 for main pension and, if your activity has them, for supplementary and lump sum?
3. Are you also employed, or do you bill only one or two clients on service invoices? (Parallel insurance floor, or employee rules under art. 39(9).)
4. Do you carry on more than one self-employed activity, or farm under the former OGA rules?
5. Have you had a child in the last 12 months? (50% cut in the main pension contribution.)
6. Do you have unpaid contributions, a KEAO settlement, or an A1 from another country?

## Sources

| Source | URL | Read on |
|---|---|---|
| e-EFKA circular 6/2026, 2026 contributions of freelancers, the self-employed and farmers (all category tables, EUR 10 unemployment, EUR 2 health professionals, in force 1.1.2026) | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-62026 | 2026-10-23 |
| e-EFKA circular 3/2020, new contributions of freelancers, the self-employed and farmers (free choice, special category rules, parallel insurance, payment deadline, mothers, late-payment interest) | https://www.e-efka.gov.gr/sites/default/files/2021-08/%CE%95%CE%93%CE%9A%CE%A5%CE%9A%CE%9B%CE%99%CE%9F%CE%A3%203-2020.pdf | 2026-10-23 |
| e-EFKA FAQ, contributions of freelancers, the self-employed and farmers (category choice, special category, payment, late payment, KEAO transfer) | https://www.e-efka.gov.gr/el/nees-eisphores-eleytheron-epaggelmation-aytotelos-apascholoymenon-kai-agroton | 2026-10-23 |
| e-EFKA FAQ, supplementary contributions of the non-salaried | https://www.e-efka.gov.gr/el/eisphores-0 | 2026-10-23 |
| e-EFKA FAQ, lump-sum contributions of the non-salaried | https://www.e-efka.gov.gr/el/sychnes-eroteseis/asphalisi-eisphores/asphalismenoi/me-misthotoi-0/epikoyrike-asphalise-kai-ephapax-paroche-pronoia-sychnes-erotapan/ephapax-paroche-pronoia/ephapax-paroche-pronoia-eisphores | 2026-10-23 |
| e-EFKA FAQ, reduced contributions for mothers | https://www.e-efka.gov.gr/el/sychnes-eroteseis/asphalisi-eisphores/asphalismenoi/me-misthotoi-0/meiomenes-eisphores-gia-meteres-me-misthotes | 2026-10-23 |
| e-EFKA general document 1811441/13.07.2026, new non-salaried online services (category choice window December to January) | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/geniko-eggrafo-181144113-07-2026 | 2026-10-23 |
| e-EFKA circular 15/2026, 72-instalment settlement under art. 22 ν. 5313/2026 | https://www.efka.gov.gr/el/egkyklioi-kai-genika-eggrapha/egkyklios-152026 | 2026-10-23 |
| e-EFKA FAQ for debtors, KEAO (settlement surcharges) | https://www.e-efka.gov.gr/el/sychnes-eroteseis/opheiletes-keao/themata-diakanonismoy-opheilon-sychn-erotapan-keao/genika | 2026-10-23 |
| Income Tax Code (ν. 4172/2013), Ministry of Finance codification to ν. 5264/2025, arts. 22 and 23 | https://minfin.gov.gr/koinopoiisi-kodikopoiisis-tou-kodika-forologias-eisodimatos-symfona-me-to-arthro-83-par-55-tou-n-5104-2024/ | 2026-10-23 |

Not yet confirmed: the text of art. 2(4) ν. 4158/2013 itself (the late-payment rate is taken from e-EFKA circular 3/2020, section 6, and the law was not fetched), and the ECB refinancing rate in force on any given day; the exact dates of the December 2026 to January 2027 window for choosing 2027 categories; which professions are compulsorily insured in the supplementary and lump-sum branches beyond the former OAEE groups the e-EFKA FAQ lists (check the client's e-EFKA record); whether an engineer such as the one in Example 2 is compulsorily insured in both branches (the example assumes it).

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
