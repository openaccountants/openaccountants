---
name: ro-income-tax
description: "Use this skill for Romanian income tax on self-employed individuals for tax year 2026: PFA (persoană fizică autorizată), II (întreprindere individuală), IF (întreprindere familială) and liberal professions. Covers the flat 10% tax on net income in the real system (sistem real), income norms (norma de venit) and when they are barred, gross income and deductible, capped and non-deductible expenses, the deduction of CAS and CASS from the base, the 70% five-year loss carry-forward, the Declarația unică filed and paid by 25 May 2027 on actual 2026 figures, and the interest, penalties and fines for late filing or payment. Trigger phrases: impozit pe venit PFA, sistem real, norma de venit, cheltuieli deductibile PFA, Declarația unică 2027, PFA tax Romania, freelancer tax Romania. Out of scope: ro-cas-cass (contribution rules in depth), ro-employee-income-tax (salary, rent, investments), ro-corporate-income-tax (SRL), ro-vat-return, ro-cross-border."
version: 2.1
jurisdiction: RO
category: international
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
tier: 2
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Romania: income tax for the self-employed (PFA, II, IF, liberal professions), 2026

This skill computes the income tax a self-employed individual owes for 2026 on income from independent activities (venituri din activități independente). The tax year is the calendar year. The authority is ANAF and the currency is the leu (RON).

The law is Legea 227/2015 (Codul fiscal, "the Fiscal Code"), Title IV, and Legea 207/2015 (Codul de procedură fiscală, "the Procedure Code"). Articles were read on 23 October 2026 in ANAF's consolidated texts, both shown as last updated by Legea 170/2026. ANAF notes these consolidations are not an official republication.

The pension (CAS) and health (CASS) contributions on the same income are set out in full in ro-cas-cass. This skill uses their results, because both are deducted before the 10% tax is applied.

## Who this applies to

- **In scope.** An individual who earns income from production, trade, services or a liberal profession, alone or in an association without legal personality (Fiscal Code art. 67(1)). In practice: a PFA, an II, a member of an IF, and liberal professionals such as doctors, architects, accountants, translators or consultants practising in their own name. Liberal profession income is income from professional services under the special law that governs that profession (art. 67(2)).
- **Also in scope.** Accommodation services by registered operators, and short-term rental of more than 7 rooms in personal homes. These count as independent activities but use a 30% flat expense rate (art. 67(1^1), art. 68^3). This skill notes them only.
- **Source.** Independent activity carried on in Romania is Romanian-source income wherever the payment comes from (art. 67^1). A Romanian resident is taxed on worldwide income. Residence rules are in ro-cross-border.
- **Out of scope.** Companies (an SRL pays corporate tax or micro-enterprise tax: ro-corporate-income-tax). Salaries, rent, dividends, interest and gains on shares (ro-employee-income-tax). Intellectual property income with its 40% flat expense deduction (art. 72, 72^1). Sports contracts taxed at source (art. 68^1). Agricultural income. VAT (ro-vat-return).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Income tax on net income from independent activities | 10% | 2026 | Fiscal Code art. 64(1)(a), https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Tax on an income norm | 10% of the norm, adjusted where allowed | 2026 | art. 69^2(1), same page |
| National gross minimum wage used for 2026 thresholds (wage in force on 1 January 2026) | RON 4,050 a month | 2026 | art. 135^1(3), same page; HG 1506/2024 art. 1, https://static.anaf.ro/static/10/Anaf/legislatie/HG_1506_2024.pdf |
| Minimum wage from 1 July 2026 (does not change 2026 thresholds or norm floors) | RON 4,325 a month | 2026 | HG 146/2026 art. 1, https://static.anaf.ro/static/10/Anaf/legislatie/HG_146_2026.pdf |
| Floor for any income norm: 12 minimum wages in force on 1 January | RON 48,600 | 2026 | art. 69(3); ANAF DGRFP Brașov 2026 summary, p. 33, https://static.anaf.ro/static/10/Brasov/Brasov/modificari_fiscale_2026.pdf |
| Gross income above which norm taxpayers must move to the real system the next year | EUR 25,000 equivalent, at the BNR average annual rate | 2026 | art. 69(9), Fiscal Code page |
| Lock-in after opting for the real system | 2 consecutive fiscal years, renewed automatically | 2026 | art. 69^1(2), same page |
| CAS (pension), self-employed: base chosen by the taxpayer, at least 12 or 24 minimum wages | 25%; minimum CAS RON 12,150 (12 wages) or RON 24,300 (24 wages) | 2026 | art. 138(a), art. 148; see ro-cas-cass |
| CASS (health), self-employed: base is actual net income or norm, floor 6 and cap 72 minimum wages | 10%; floor RON 2,430, cap RON 29,160 | 2026 | art. 156, art. 170(1), art. 174(6); ANAF Brașov summary, p. 38 |
| Loss carry-forward (real system) | 70% of the same source's net income, 5 following years | 2026 | art. 118(4)-(5), Fiscal Code page |
| Protocol (entertainment) expenses | up to 2% of the calculation base | 2026 | art. 68(5)(b), (6) |
| Private scholarships | up to 5% of the calculation base | 2026 | art. 68(5)(a), (6) |
| Voluntary or occupational pension contributions; voluntary health insurance | EUR 400 a year each, per person | 2026 | art. 68(5)(g), (g^1), (h) |
| Sports subscriptions | EUR 100 a year per person | 2026 | art. 68(5)(r) |
| Membership of professional associations (voluntary) | EUR 4,000 a year | 2026 | art. 68(5)(p) |
| Compulsory professional body contributions | up to 5% of gross income | 2026 | art. 68(5)(q) |
| Cars not used only for the business (up to 3,500 kg, up to 9 seats) | 50% of running costs not deductible | 2026 | art. 68(7)(k) |
| Income from an unidentified source | 70% | 2026 | art. 117 |

## The taxable base

**Two ways to set net income.**

1. **Real system (sistem real).** Net income is gross income less deductible expenses (art. 68(1)). This is compulsory for liberal professions, which can never use a norm (art. 69(1)). It is also compulsory when the person carries on a norm activity together with another independent activity (art. 69(7)).
2. **Income norm (norma de venit).** For activities on the Ministry of Finance list (OMFP 925/2017), net income is a fixed annual amount set by each county's regional finance directorate for the place where the work is done (art. 69(1)-(2)). Rules:
   - each norm is at least 12 minimum wages in force on 1 January, so RON 48,600 for 2026 (art. 69(3));
   - two or more norm activities: add the norms together (art. 69(6));
   - activity for part of the year: cut the norm pro rata to the time worked (art. 69(5), art. 122(2));
   - the taxpayer may apply the county's published correction coefficients in the Declarația unică (art. 69(10));
   - only the income part of the tax register is kept, no accounts (art. 69(8));
   - gross income above EUR 25,000 in a year means the real system from the next year (art. 69(9));
   - a norm taxpayer may opt for the real system; the option binds for 2 years (art. 69^1).

**Gross income (real system)** is cash received, plus the RON value of payments in kind (art. 68(2)). It includes interest on trade receivables, gains on business assets, non-compete payments and debts written off. It excludes capital contributions, loans, compensation received, and sponsorship or donations received (art. 68(3)). It is cash basis: income counts when collected.

**Deductible expenses** must be incurred for the activity, backed by documents and paid in the year (art. 68(4)(a)-(b)). They include staff costs, depreciation under the corporate tax rules, business insurance, business travel, and compulsory professional contributions. Mixed personal and business costs are deductible only for the business share (art. 68(5)(i)). The capped items are in the table above. For the 2% and 5% caps the calculation base is gross income less deductible expenses other than protocol and scholarships (art. 68(6)).

**Not deductible** (art. 68(7)): personal or family spending; the income tax itself; fines, late-payment interest and penalties owed to authorities; donations; loan principal repayments; the purchase price of depreciable assets (they are depreciated instead); sponsorship; 50% of running costs of a car not used only for the business, unless it is in one of the listed categories (taxi, sales agents, couriers, driving schools and others).

**Records.** Real-system taxpayers keep the tax register (Registrul de evidență fiscală, OMFP 3254/2017) (art. 68(8)-(9)).

**From net income to taxable income (real system)** (art. 118(2)):

1. Net income for each source, less losses brought forward from that source.
2. Add the recalculated net incomes of all real-system sources.
3. Deduct CAS and CASS due for the year under Title V. The CASS top-up a person pays only to reach the 6-wage floor (art. 174(6)) is not deductible.
4. Where the CAS or CASS base also covers income outside the real system (for example a norm, or intellectual property income), deduct only the share that matches real-system income (art. 118(2^2)-(2^3)).
5. The deduction cannot exceed the recalculated net income (art. 118(2^4)).

Tax is 10% of the result (art. 123(1)).

**Norm taxpayers** pay 10% of the norm, adjusted where allowed (art. 69^2(1)). The CAS and CASS deduction in art. 118(2) is only for real-system income, so it does not reduce a norm.

**Losses** (real system) carry forward for 5 years and offset up to 70% of later net income from the same source. They are used oldest first, belong to the person only, and lapse after 5 years (art. 118(4)-(5)). A loss does not reduce the CASS base (art. 170(1)).

**Part year.** Income earned in part of a year is annual income; there is no annualising (art. 118(3)).

## Deadlines and filing

- **One annual return.** File the Declarația unică for 2026 income by **25 May 2027** (art. 122(1), (3)). The same date applies when an activity starts, stops or is suspended during the year (art. 122(2)-(3)).
- **Actual figures only.** The return reports income actually earned in 2026 and computes the tax and contributions on it. There is no estimate section and no advance tax for these taxpayers: the estimated-income chapter (art. 120) and the old advance-payment rule (art. 74) are repealed.
- **Payment.** Income tax is paid by the same 25 May 2027 date (art. 69^2(2) for norms; art. 123(7) for the real system). CAS and CASS are paid by the same date (art. 151(1), art. 174(15)). Contributions may be paid early, at any time before the due date (art. 151(13), art. 174(16)).
- **Options in the return.** The option to move from a norm to the real system is made in the Declarația unică filed by 25 May of the following year (art. 69^1(3)). The voluntary CAS option for income below 12 minimum wages is made the same way (art. 148(4)).
- **Where.** The Declarația unică is filed online through ANAF's SPV (Spațiul Privat Virtual) for individuals: https://www.anaf.ro/anaf/internet/ANAF/servicii_online/declaratia_unica. It is itself the tax assessment (titlu de creanță) (art. 122(9)).
- **Early-payment discount.** The law allows a discount of up to 10% of the annual tax, CAS and CASS, set each year by the state budget law (art. 121, art. 151(14), art. 174(17)). The discount for amounts paid in 2027 is not set yet.

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late-payment interest | 0.02% a day, from the day after the due date | Procedure Code art. 174(1), (5), https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Late-payment penalty | 0.01% a day, on top of interest | art. 176(1)-(3), same page |
| Return not filed on time: interest start | Interest on income tax runs from 1 January of the year after the tax year (1 January 2027 for 2026 income), not from 25 May. The same rule applies to contributions | art. 175(1)(d), (4) |
| Non-declaration penalty (tax undeclared or declared wrongly, then assessed by ANAF) | 0.08% a day, instead of the 0.01% penalty; cut by 75% if paid by the due date in the assessment; not charged under RON 50; capped at the tax | art. 181(1)-(2), (6), (11); art. 176(4) |
| Fine for an individual's late Declarația unică | RON 50 to 500 | art. 336(3) |

Where ANAF assesses the tax after a return was not filed, only the non-declaration penalty applies, not the fine (art. 181(9)).

## Cross-border points

- **Foreign clients.** A resident PFA's income from work done in Romania is Romanian income even when paid from abroad (Fiscal Code art. 67^1). Foreign-source independent income of a resident is declared in the same Declarația unică. Relief for foreign tax uses the treaty's credit or exemption method (art. 131); see ro-cross-border.
- **Foreign losses** carry forward only against income of the same kind from the same country, at 70% for 5 years (art. 118(7)).
- **Non-residents** working independently in Romania: withholding, treaty limits and the option for EU and EEA residents to be taxed on net income are in ro-cross-border.
- **Social contributions abroad.** CAS and CASS apply subject to EU coordination rules and social security agreements (art. 137(1), art. 155(1)). For the A1 certificate and which state insures a person working in two states, see eu-social-security-coordination.

## Worked examples

**Example 1. Software developer, PFA, real system.**

Andrei is resident and works as a PFA in 2026. He uses the real system. He collected RON 180,000 from clients and paid RON 40,000 of deductible expenses. He has no other income and no losses brought forward. He chooses the lowest CAS base the law allows.

- Net income: 180,000 − 40,000 = RON 140,000.
- CAS: net income is at least 24 minimum wages (24 × 4,050 = 97,200). So the CAS base is at least RON 97,200. CAS = 25% × 97,200 = RON 24,300.
- CASS: 10% of actual net income, kept between 6 wages (24,300) and 72 wages (291,600). RON 140,000 is inside that range. CASS = RON 14,000.
- Taxable income: 140,000 − 24,300 − 14,000 = RON 101,700.
- Income tax: 10% × 101,700 = RON 10,170.
- Total due by 25 May 2027: 10,170 + 24,300 + 14,000 = RON 48,470.

```oa-check
name: PFA real system, net RON 140,000, 2026
inputs:
  gross: 180000
  expenses: 40000
  min_wage: 4050
steps:
  - net: gross - expenses
  - cas_base: 24 * min_wage
  - cas: cas_base * 0.25
  - cass_base: clamp(net, 6 * min_wage, 72 * min_wage)
  - cass: cass_base * 0.10
  - taxable: net - cas - cass
  - tax: taxable * 0.10
  - total: tax + cas + cass
expected:
  net: 140000.00
  cas: 24300.00
  cass: 14000.00
  taxable: 101700.00
  tax: 10170.00
  total: 48470.00
```

**Example 2. Income norm, started part way through the year (edge case).**

Elena registers a PFA on 1 April 2026 for an activity on the norm list. The annual norm for her activity in her county is RON 60,000. She has no other income, takes no correction coefficient and does not opt in to CAS. She worked 9 months, so her norm is cut pro rata (art. 69(5)).

- Norm for 2026: 60,000 × 9 / 12 = RON 45,000.
- CAS: RON 45,000 is below 12 minimum wages (48,600), so CAS is not due (art. 148(1)). She may opt in (art. 148(4)). The 48,600 floor in art. 69(3) applies to the annual norm, before the pro rata cut.
- CASS: the base is the norm, RON 45,000, inside the 6 to 72 wage range. CASS = RON 4,500.
- Income tax: 10% × 45,000 = RON 4,500. Nothing is deducted from a norm.
- Total due by 25 May 2027: RON 9,000.

```oa-check
name: Income norm, 9 months, annual norm RON 60,000, 2026
inputs:
  annual_norm: 60000
  months: 9
  min_wage: 4050
steps:
  - norm: annual_norm * months / 12
  - cas_threshold: 12 * min_wage
  - cass_base: clamp(norm, 6 * min_wage, 72 * min_wage)
  - cass: cass_base * 0.10
  - tax: norm * 0.10
  - total: tax + cass
expected:
  norm: 45000.00
  cas_threshold: 48600.00
  cass: 4500.00
  tax: 4500.00
  total: 9000.00
```

## Ask the client first

1. Are you a PFA, II, IF member or a liberal professional, or do you work through an SRL? An SRL is out of scope here.
2. Real system or income norm? For a norm: the activity code, the county and the months worked. For the real system: gross income collected and expenses paid in 2026.
3. Were you on a norm with gross income above EUR 25,000 in 2025? If yes, 2026 must be in the real system.
4. Do you also have a salary, a pension, intellectual property income or other independent income? This changes the CAS threshold, the CASS floor and the deduction share (see ro-cas-cass).
5. Losses from earlier years from the same activity, and the year each arose?
6. Any income from abroad, or an A1 certificate from another EU state?

## Sources

| Source | URL | Read on |
|---|---|---|
| Legea 227/2015, Codul fiscal, ANAF consolidated text (last update Legea 170/2026): art. 64, 67, 67^1, 68, 68^3, 69, 69^1, 69^2, 117, 118, 120, 121, 122, 123, 131, 135^1, 137, 138, 148, 151, 155, 156, 170, 174 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-10-23 |
| Legea 207/2015, Codul de procedură fiscală, ANAF consolidated text (last update Legea 170/2026): art. 174, 175, 176, 181, 336 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm | 2026-10-23 |
| HG 1506/2024, minimum wage RON 4,050 from 1 January 2025 | https://static.anaf.ro/static/10/Anaf/legislatie/HG_1506_2024.pdf | 2026-10-23 |
| HG 146/2026, minimum wage RON 4,325 from 1 July 2026 | https://static.anaf.ro/static/10/Anaf/legislatie/HG_146_2026.pdf | 2026-10-23 |
| ANAF DGRFP Brașov, summary of 2026 tax changes (21 July 2026), pp. 33 and 38: norms set on RON 4,050; CASS cap 72 wages, RON 291,600 | https://static.anaf.ro/static/10/Brasov/Brasov/modificari_fiscale_2026.pdf | 2026-10-23 |
| ANAF, Declarația unică online filing (SPV) | https://www.anaf.ro/anaf/internet/ANAF/servicii_online/declaratia_unica | 2026-10-23 |

Not yet confirmed: the early-payment discount (art. 121) for amounts paid in 2027 is not set yet. The 2026 norm amounts for each county and activity were not read; use the regional directorate's published list. The norm activity list is cited as OMFP 925/2017 from the reference note in the Fiscal Code; the order itself was not read.
