---
name: ls-cross-border
description: "Lesotho cross-border income tax for the 2026-27 year of assessment (1 April 2026 to 31 March 2027) under Part X (International Taxation) of the Income Tax Act 1993 as amended. Covers residence of individuals (normal place of abode, more than 182 days, officials posted abroad) and companies (incorporation, management and control, majority of operations), the domestic branch definition, Lesotho-source income rules (s.103), 25% final withholding on dividends, interest, royalties, natural resource payments and management charges to non-residents, 15% for concessional manufacturing, 10% on non-resident services contracts, the election to be assessed at 40%, the s.110 statement before paying a non-resident, branch profits tax on repatriated income, the foreign tax credit, the foreign employment exemption, tax havens and treaties, with the South Africa treaty as the worked case. Trigger on: Lesotho non-resident tax, Lesotho withholding tax non-resident, branch profits tax Lesotho, Lesotho tax"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ls-cross-border"
  jurisdiction: "LS"
  tax_year: "2026"
  last_updated: "2026-11-02"
---

# Lesotho cross-border: residence, source, withholding on non-residents, branch profits and foreign tax credit (2026-27) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Part X (International Taxation, ss.103 to 112A) of the Income Tax Act 1993 (Act No. 9 of 1993, as amended) sets how non-residents are taxed on Lesotho income and how residents are relieved for foreign tax. Revenue Services Lesotho (RSL) administers it. The year of assessment runs from 1 April to 31 March, so this skill covers the 2026-27 year of assessment, 1 April 2026 to 31 March 2027. The text used is RSL's consolidated copy "Updated up to 1 April 2012"; later amendments it does not show are on the "Not yet confirmed" line.

## Who this applies to

- **Resident individuals (s.5(1)).** An individual is resident for the whole year of assessment if they:
  - have a normal place of abode in Lesotho and are present for part of the year;
  - are present in Lesotho on more than 182 days in any consecutive twelve months that includes all or part of the year;
  - are a Lesotho Government official posted overseas; or
  - are otherwise resident.

  In the year of arrival, residence does not cover the days before first presence (s.5(2)). In the year of departure, it ends on the last day present if the person is not resident in the following year and, for the rest of the year, had a closer connection to a foreign country than to Lesotho (s.5(3)). The personal income tax rules are in ls-income-tax.
- **Resident companies (s.6(1)).** A company is resident if it is incorporated or formed under Lesotho law, has its management and control in Lesotho, or undertakes the majority of its operations in Lesotho. A company that is also resident in South Africa has no treaty tie-breaker: the competent authorities try to settle it by mutual agreement, and without agreement the company gets no relief or exemption under that treaty (Lesotho and South Africa agreement, Article 4(3)).
- **Branches (s.3, s.6(2)).** A branch is a place where a person carries on business, including a place where it carries on business through an agent (other than a general agent of independent status acting in the ordinary course of its business), has, uses or is installing substantial equipment or machinery, or is engaged in a construction, assembly or installation project. The domestic definition has no minimum duration. A Lesotho branch of a non-resident company is treated as a separate person which is a resident company.
- **Partnerships (s.7).** Resident for a year if any partner was resident at any time in it.
- **Non-residents.** Their gross income includes only Lesotho-source income (s.17(3)). It is taxed through a branch (25% plus branch profits tax), by final withholding on gross payments (ss.107 to 109), or by assessment at the standard rate (s.12).

## Rates, bands and thresholds

| Item | Figure | Conditions | Official URL |
|---|---|---|---|
| Withholding on Lesotho-source dividends, interest, royalties, natural resource payments and management charges paid to a non-resident | 25% of the gross amount (standard rate) | s.107(1); charged to the non-resident | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Dividend paid out of manufacturing income taxed at the concessional rate | 0% (no withholding) | s.107(2) | same |
| Interest, royalty or management charge used solely for concessional manufacturing income | 15% of the gross amount | s.107(3) | same |
| Lesotho-source services contract paid to a non-resident (not management charges) | 10% of the gross amount | s.108; covers artistes, entertainers, sportspersons and professional services, RSL ruling | same |
| Nature of the s.107 and s.108 tax | final tax, unless the non-resident files a return and elects to be assessed | s.109(1) | same |
| Electing non-resident assessed under s.109 | 40% on net Lesotho-source income | Fourth Schedule item 1; deductions limited by s.109(2) | same |
| Non-resident taxed by assessment | 25% (standard rate) | s.12(1); an individual living permanently abroad who works or trades full-time in Lesotho pays the Second Schedule resident bands on that employment or business income, s.12(2) (the 2012 Act copy still shows 22% and 35%; the 2026-27 bands are in ls-income-tax) | same |
| Branch chargeable income | 25% | s.10, Third Schedule item 4; the manufacturing rate does not apply to a branch of a non-resident company, s.10(2) | same |
| Branch profits tax on repatriated income | 25% | s.111(1); in addition to tax on the branch's chargeable income | same |
| Branch profits tax, South African company with a Lesotho branch | capped at 10% of repatriated income | Lesotho and South Africa agreement Article 10(6) | https://www.rsl.org.ls/sites/default/files/2024-07/Agreement%20between%20Lesotho%20and%20Republic%20of%20South%20Africa.pdf |
| Dividends to a South African resident beneficial owner | 10% (company holding at least 10% of capital); 15% otherwise | Article 10(2) | same |
| Interest to a South African resident beneficial owner | 10% | Article 11(2); only the arm's length amount where a special relationship inflates it, Article 11(6) | same |
| Royalties to a South African resident beneficial owner | 10% | Article 12(2); only the arm's length amount, Article 12(6) | same |
| Technical, managerial or consultancy fees to a South African resident beneficial owner | 7.5% | Article 13(2), (6); RSL applies it from 27 June 2016 | https://www.rsl.org.ls/sites/default/files/2024-07/Guideline%20on%20Technical%20Services.pdf |
| Treaty permanent establishment, South Africa: construction or installation project | more than six months | Article 5(3)(a) | https://www.rsl.org.ls/sites/default/files/2024-07/Agreement%20between%20Lesotho%20and%20Republic%20of%20South%20Africa.pdf |
| Treaty permanent establishment, South Africa: services through employees or personnel, or an individual's independent professional services | more than 90 days in aggregate in any twelve months commencing or ending in the fiscal year | Article 5(3)(b), (c) | same |
| Additional tax (failing to withhold or remit) | specified rate; RSL's most recent statement is 3% a month, compounded monthly (older guide: 22% per twelve months) | s.192, s.196; RSL Tax Guide on Provisional Tax, question 8 (file dated November 2023, stated for unpaid instalments); RSL Corporate Income Tax Guide 1.4 (file dated May 2017) | https://www.rsl.org.ls/sites/default/files/2024-05/Tax%20Guide%20on%20Provisional%20Tax%20%281%29.pdf |

## The base

**Lesotho-source income (s.103(1)).** The main categories:
- income from an activity that occurs in Lesotho;
- income from services performed under a contract with the Lesotho Government (s.103(1)(b); RSL's withholding ruling, Example 1, still treats repairs done outside Lesotho for a Government body as not subject to withholding);
- income from immovable property in Lesotho, including gains on disposing of an interest in it, or of shares in a company whose property consists directly or indirectly principally of such interests;
- a gain of a resident from disposing of movable property (other than business income of a business carried on outside Lesotho);
- a gain from disposing of a membership interest in a resident company;
- rent from movable property used in Lesotho;
- income from the sale or licence of industrial or intellectual property used in Lesotho;
- interest where the debt is secured on Lesotho immovable property, the borrower is resident, or the borrowing relates to a business carried on in Lesotho;
- a dividend, management fee or director's fee paid by a resident company;
- pensions and annuities paid by the Government or a resident, or for services in Lesotho;
- natural resource payments for resources taken from Lesotho;
- income taxable in Lesotho under an international agreement.

Everything else is foreign-source income (s.103(2)). RSL's withholding ruling applies the activity test strictly: services performed wholly outside Lesotho by a non-resident are not Lesotho-source, so no s.108 withholding arises (Example 1 of the ruling).

**Final withholding (ss.107 to 109, s.161).**
- The payer withholds from a s.107 or s.108 payment (s.161(1)). The tax is on the gross amount; RSL's ruling says the gross amount is the amount before VAT.
- The tax is final unless the non-resident files a return and elects to be assessed (s.109(1)). An electing non-resident may deduct only otherwise deductible expenses that are Lesotho-source income of the person paid, and is taxed at 40% (s.109(2), (3); Fourth Schedule).
- The Minister may exempt a particular interest payment, transaction or series by notice in the Gazette (s.107(6)).
- The ruling's "DTA Rate" column gives treaty rates of 5%, 10% and 12.5% (dividends), 15% (interest) and 7.5% or 10% (royalties and management fees); it does not say which treaty each comes from, and its 15% for interest is above the South Africa agreement's 10%, so open the treaty that applies. The ruling's domestic rates (25%, 15%, 10%) match ss.107 and 108; its text names only royalties for the 15% rate, while s.107(3) also covers interest and management charges.

**Other payments to non-residents (s.110).** Before making any other payment that is likely to give rise to Lesotho-source income of a non-resident, the payer must give the Commissioner General a written statement of the amount, receive a notice of the amount (if any) to withhold, and comply with it.

**Branch profits tax (s.111).** A Lesotho branch of a non-resident company pays 25% on its repatriated income, on top of 25% on its chargeable income. Repatriated income is the branch's chargeable income less Lesotho income tax paid on it and less any profit reinvested in the branch. Every repatriation is treated as made first out of branch income, whatever the branch's records show.

**Residents' foreign income.**
- **Foreign tax credit (s.105).** A resident gets a credit for foreign income tax (including foreign withholding) borne directly or indirectly on foreign-source income taxed in Lesotho. The credit is capped at the average rate of Lesotho tax applied to the foreign-source income net of the deductions properly allocated to it, and is computed separately for business income and other income. The average rate is Lesotho tax after the personal credit and before the foreign tax credit, as a percentage of chargeable income. A foreign "soak-up" tax designed to reduce residence-country tax does not count. A company with both an advance corporation tax credit and a foreign tax credit applies the foreign tax credit first (s.105(5)).
- **Foreign employment income (s.104).** A resident individual's foreign-source employment income is exempt if it is chargeable to tax in the foreign country.
- **Tax havens (s.106).** Where a resident's transaction has income arise as foreign-source income through a non-resident company connected to a tax haven (significantly lower effective tax rates, or secrecy laws), the Commissioner General may reverse the tax effect. A treaty partner is never treated as a tax haven.

**Treaties (s.112, s.103(1)(n)).** The Minister may enter into, amend or terminate double taxation agreements, and the Commissioner General may collect foreign tax for a treaty partner on request (s.112(2), (3)). The Act's text read does not itself state that a treaty overrides the Act. RSL's practice note on foreign nationals states that where a treaty exists, its provisions take precedence, and that treaty tie-breaker rules decide residence for a person resident in both States. RSL lists agreements with South Africa, the United Kingdom, Mauritius, Botswana and Eswatini, and information exchange agreements with Guernsey and the Isle of Man. Treaty rates apply only to a beneficial owner resident in the other State.

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Withholding agent pays tax withheld under ss.107 and 108 | within the time prescribed by regulations; RSL says withholding tax is collected monthly or whenever tax has been withheld | ITA s.166(1); RSL Withholding Tax page |
| How to file and pay | register as a withholding agent; complete the Excel WHT schedule RSL emails you (payee legal name, nature of service, payment date, gross amount, tax deducted) and send it to WHTSubmission@rsl.org.ls; pay immediately on submission at a commercial bank or the RSL banking hall and email proof to receipts@rsl.org.ls; the system then issues the electronic WHT certificate | RSL Automated Withholding Tax Guide (file dated February 2023) |
| Tax withholding certificate to a non-resident payee | on the date of payment | ITA s.163(2)(b) |
| Return of Lesotho-source interest, dividends, royalties, management fees and rent paid (company or partnership payer) | within 28 days after the end of the year of assessment | ITA s.130 |
| Statement to the Commissioner General before paying a non-resident a payment not covered by s.107 or s.108 | before the payment is made | ITA s.110 |
| Annual return of a branch or other non-resident taxpayer, and of a non-resident electing under s.109 | last day of the third month after the year end: 30 June 2027 for 2026-27 | ITA s.128(1), s.109(1) |
| Tax payable on assessment | on the date the return is due | ITA s.143(1) |

## Penalties and interest

- **Not withholding.** A withholding agent who fails to withhold is personally liable for the tax not withheld, and may recover it from the payee (s.165(1)). It also owes additional tax at the specified rate on the tax not withheld from its due date (s.196(1)).
- **Not remitting.** Additional tax at the specified rate on tax withheld but not paid over (s.196(2)). Additional tax under s.196 is borne personally and cannot be recovered from the payee or credited against an assessment (s.196(3)). The specified rate is the rate the Commissioner General publishes from normal commercial lending rates (s.192); RSL's most recent statement is 3% a month, compounded monthly (Tax Guide on Provisional Tax, November 2023), against 22% per twelve months in an older guide (Corporate Income Tax Guide, May 2017).
- **Offences.** Failing to withhold or to issue a withholding certificate (s.178), failing to give a s.110 statement (s.179), and failing to remit tax withheld in time (s.180): each a fine up to M10,000, imprisonment up to two years, or both, on conviction.
- **Late returns.** A non-resident taxpayer or branch that files late owes additional tax at the specified rate on the tax payable from the due date (s.193); failing to file is also an offence with a fine up to M5,000, imprisonment up to six months, or both (s.175(1)).

## Cross-border points

This whole skill is about cross-border points. In short:
- residence follows s.5 (individuals) and s.6 (companies), with treaty tie-breakers on top (for companies under the South Africa agreement, mutual agreement only, Article 4(3));
- non-residents are taxed through a branch at 25% plus 25% branch profits tax, or by final withholding of 25% (s.107) or 10% (s.108) on gross payments, cut by a treaty where the beneficial owner is resident in the treaty State;
- residents get a foreign tax credit capped at the average Lesotho rate, basket by basket;
- related-party pricing on any of these payments is in ls-transfer-pricing.

## Two worked examples that recompute

### Example 1, a decision: branch profits tax with and without the South Africa treaty

A non-resident company runs a Lesotho branch. For the year to 31 March 2027 the branch has chargeable income of M4,000,000 and reinvests M600,000 of profit in the branch.

- **Branch income tax at 25%:** M1,000,000.
- **Repatriated income (s.111(2)):** 4,000,000 - 1,000,000 - 600,000 = M2,400,000.
- **Branch profits tax, no treaty:** 25% x 2,400,000 = M600,000. Total Lesotho tax M1,600,000.
- **If the company is South African resident:** Article 10(6) caps branch profits tax at 10%, so M240,000. Total Lesotho tax M1,240,000, a saving of M360,000.

```oa-check
name: Lesotho branch profits tax, chargeable M4.0m, reinvested M0.6m (2026-27)
inputs:
  chargeable: 4000000
  reinvested: 600000
  cit_rate: 0.25
  bpt_domestic: 0.25
  bpt_sa_cap: 0.10
steps:
  - branch_tax: chargeable * cit_rate
  - repatriated: chargeable - branch_tax - reinvested
  - bpt_no_treaty: repatriated * bpt_domestic
  - bpt_sa: repatriated * bpt_sa_cap
  - total_no_treaty: branch_tax + bpt_no_treaty
  - total_sa: branch_tax + bpt_sa
  - saving: total_no_treaty - total_sa
expected:
  branch_tax: 1000000.00
  repatriated: 2400000.00
  bpt_no_treaty: 600000.00
  bpt_sa: 240000.00
  total_no_treaty: 1600000.00
  total_sa: 1240000.00
  saving: 360000.00
```

### Example 2: resident company's foreign tax credit cap

Mohale Holdings (Pty) Ltd (Lesotho resident, ordinary income only) has chargeable income of M10,000,000 for 2026-27. That includes net foreign-source business income of M2,000,000 on which it paid M600,000 of foreign tax.

- **Lesotho tax before credit:** 25% x 10,000,000 = M2,500,000, so the average rate is 25%.
- **Credit cap (s.105(2)):** 25% x 2,000,000 = M500,000.
- **Credit allowed:** the lower of M600,000 paid and the M500,000 cap, M500,000. M100,000 is not relieved.
- **Net Lesotho tax:** 2,500,000 - 500,000 = M2,000,000.

```oa-check
name: Lesotho foreign tax credit cap, s.105 (2026-27)
inputs:
  chargeable_income: 10000000
  net_foreign_income: 2000000
  foreign_tax_paid: 600000
  rate: 0.25
steps:
  - lesotho_tax: chargeable_income * rate
  - average_rate: lesotho_tax / chargeable_income
  - credit_cap: average_rate * net_foreign_income
  - credit: min(foreign_tax_paid, credit_cap)
  - net_tax: lesotho_tax - credit
  - unrelieved: foreign_tax_paid - credit
expected:
  lesotho_tax: 2500000.00
  average_rate: 0.25
  credit_cap: 500000.00
  credit: 500000.00
  net_tax: 2000000.00
  unrelieved: 100000.00
```

## Ask the client first

1. For individuals: a normal place of abode in Lesotho, and days present in each twelve-month period.
2. For companies: where incorporated, where management and control is exercised, and where most operations are carried out.
3. What the non-resident does in Lesotho: agents, equipment, projects or staff on site, and for how long (the domestic branch test and any treaty permanent establishment test).
4. Each payment to non-residents by type (dividend, interest, royalty, natural resource payment, management charge, services, other), with amounts, whether the services were performed in Lesotho, and the withholding deducted.
5. The treaty claimed, and evidence that the recipient is the beneficial owner and resident in that State.
6. For residents with foreign income: foreign tax paid, split between business and other income.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 1993, RSL copy updated to 1 April 2012 (read for s.3 definitions of branch, management charge, royalty and standard rate, ss.5 to 7, s.10, s.12, s.17, ss.103 to 112A, s.128, s.130, s.143, s.161, ss.163 to 166, ss.175 to 180, ss.192 to 196, the Third and Fourth Schedules) | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf | 2026-11-02 |
| RSL Withholding Tax Public Ruling, Issue 1, dated April 2010 in its own text (RSL file uploaded 2025 to 2026; read in full: rates, DTA column, gross amount before VAT, source examples) | https://www.rsl.org.ls/sites/default/files/2026-09/Withholding%20Tax%20Public%20Ruling_2.pdf | 2026-11-02 |
| Agreement between Lesotho and South Africa on double taxation, RSL copy (read for Articles 4, 5, 9, 10, 11, 12, 13 and 29) | https://www.rsl.org.ls/sites/default/files/2024-07/Agreement%20between%20Lesotho%20and%20Republic%20of%20South%20Africa.pdf | 2026-11-02 |
| RSL internal guide on technical fees under Article 13 of the Lesotho and South Africa DTA (read in full) | https://www.rsl.org.ls/sites/default/files/2024-07/Guideline%20on%20Technical%20Services.pdf | 2026-11-02 |
| LRA practice note, Taxation of Foreign Nationals, 27 January 2020 (read for residence tests, treaty relief 4.3.2 and the conclusion on treaty precedence) | https://www.rsl.org.ls/sites/default/files/2026-09/Taxation%20of%20Foreign%20Nationals.pdf | 2026-11-02 |
| RSL Corporate Income Tax Guide, file dated May 2017 (read for section 1.4, additional tax at 22% per twelve months, superseded by the newer guide below) | https://www.rsl.org.ls/sites/default/files/2024-07/Corporate%20Income%20Tax%20Guide.pdf | 2026-11-02 |
| RSL Tax Guide on Provisional Tax, file dated November 2023 (read in full; question 8: additional tax at 3% compounded monthly) | https://www.rsl.org.ls/sites/default/files/2024-05/Tax%20Guide%20on%20Provisional%20Tax%20%281%29.pdf | 2026-11-02 |
| RSL Automated Withholding Tax Guide, file dated February 2023 (read in full: registration, WHT schedule, submission, payment, certificates) | https://www.rsl.org.ls/sites/default/files/2024-05/Automated%20Withholding%20Tax%20Guide_0.pdf | 2026-11-02 |
| RSL Withholding Tax page (read for monthly collection of withholding tax) | https://www.rsl.org.ls/withholding-tax-0 | 2026-11-02 |
| RSL Tax Treaties page (read for the list of agreements) | https://www.rsl.org.ls/tax-treaties | 2026-11-02 |
| RSL 2025-2026 Integrated Annual Report (read for the legislative pipeline: Income Tax Amendment Bill for FY2026/27) | https://www.rsl.org.ls/sites/default/files/2026-10/2025%20-%202026%20Integrated%20Annual%20Report.pdf | 2026-11-02 |

Not yet confirmed:
- Amendments to the Income Tax Act after 1 April 2012 that RSL's consolidated copy does not show, and whether the Income Tax Amendment Bill announced for FY2026/27 has been enacted.
- The regulation fixing the date by which withholding agents remit tax withheld (s.166); RSL's page says only "monthly".
- The statutory basis for treaty precedence; it rests on RSL's 2020 practice note, not on the text of s.112 read.
- The entry-into-force date of the renegotiated Lesotho and South Africa agreement; the 27 June 2016 date comes from RSL's technical services guideline.
- The rates and permanent establishment tests in the United Kingdom, Mauritius, Botswana and Eswatini agreements (texts not read).
- The currently published specified rate under s.192. RSL guides disagree: 3% a month compounded (Provisional Tax guide, November 2023, stated for instalments) against 22% per twelve months (Corporate Income Tax Guide, May 2017); no rate notice was found.
- Whether services performed outside Lesotho under a contract with the Lesotho Government are Lesotho-source under s.103(1)(b): the text does not require performance in Lesotho, but RSL's ruling (Example 1) says no withholding arises.
- Whether any Gazette notice under s.107(6) exempts particular interest payments.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-02. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ls-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ls-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
