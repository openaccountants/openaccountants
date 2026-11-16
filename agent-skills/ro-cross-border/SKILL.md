---
name: ro-cross-border
description: "Use this skill when a person or company crosses Romania's border for tax: tax residence tests for individuals (domicile, centre of vital interests, more than 183 days in any 12 months) and for companies (Romanian legal person or place of effective management), arriving in Romania (the Z015 residence questionnaire, the digital nomad exemption), leaving (the Z017 questionnaire 30 days before departure, the extra three years of worldwide tax after a move to a non-treaty state, and the 16% company exit tax with a five-year instalment option), non-residents with Romanian income, withholding on outbound dividends, interest, royalties and service fees (16%, 10%, 50%), EU directive exemptions and treaty relief. Tax year 2026 (calendar year). Trigger phrases: moving to Romania, leaving Romania, non-resident Romania, expat Romania, exit tax Romania, digital nomad Romania, withholding tax Romania, certificat de rezidenta fiscala. Out of scope: ro-income-tax, ro-corporate-income-tax, ro-payroll-so"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ro-cross-border"
  jurisdiction: "RO"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# Romania cross-border: residence, arriving, leaving, non-residents and withholding (2026)

This is the hub skill for what changes when a person or a company crosses Romania's border. It covers residence, arrival and departure filings, the company exit tax, tax on non-residents' Romanian income, and withholding on payments abroad. The domestic computations live in the sibling skills: ro-income-tax (self-employed individuals), ro-corporate-income-tax (companies), ro-payroll-social (employee contributions and payroll), ro-cas-cass (self-employed contributions). EU social security rules are in eu-social-security-coordination; treaty defaults are in oecd-model-treaty-defaults.

The law is Legea 227/2015 (Codul fiscal, "the Fiscal Code") and Legea 207/2015 (Codul de procedură fiscală, "the Procedure Code"). The usable operative articles and neighbouring exceptions identified in Sources were read in ANAF's texts on 15 November 2026. ANAF's Fiscal Code header names Legea 204/2026 and its Procedure Code header Legea 170/2026; ANAF warns that its computer-updated texts are not an official republication. The retained [legislative portal](https://legislatie.just.ro/Public/DetaliiDocument/171282) capture's 25 October 2026 version label is historical research provenance. Fresh ordinary portal access and version confirmation remain unrecovered; the current usable residence and exit rules below rely on the actually read ANAF provisions. This skill produces a residence/withholding/exit working paper, with evidence and unresolved conditions, for professional review.

## Who this applies to

**Individuals.** A person is resident in Romania if they meet at least one of four tests (Fiscal Code art. 7 point 28):

1. their domicile is in Romania;
2. their centre of vital interests is in Romania;
3. they are present in Romania for one or more periods of more than 183 days in total in any 12 consecutive months ending in the calendar year in question;
4. they are a Romanian citizen working abroad as an official or employee of the Romanian state.

Anyone who meets none of these is non-resident (art. 7 point 27). Foreign nationals with diplomatic or consular status in Romania, foreign officials or employees of an international organisation registered in Romania or of a foreign state in Romania, and their families are non-resident.

The "centre of vital interests" is where the person's personal and economic relations are closer. Family, a Romanian employer, business activity and property in Romania all count (art. 7 point 6).

**Part-year rules (no split year by election; the start date is fixed by the law).**
- A Romanian resident with a Romanian domicile is taxed on worldwide income (art. 59(1)(a)).
- A newcomer who meets the centre of vital interests test is taxed on worldwide income from the first day they declare their centre of vital interests is in Romania (art. 59(2)).
- A newcomer who meets the 183-day test is taxed on worldwide income from the first day of arrival in Romania (art. 59(2^1)). The presence test requires more than 183 days; once it is met, worldwide liability runs back to arrival, subject to the applicable treaty. Do not use a universal 183-or-more shortcut.
- The centre of vital interests rule gives way to a tax treaty where the person proves residence in the treaty state (art. 59(3)). For every residence test, a treaty provision prevails over the Fiscal Code (art. 1(3)).
- A newcomer covered by art. 59(4) remains resident until departure and must follow its departure questionnaire rule for a foreign stay exceeding 183 days in a consecutive 12-month interval.

**Companies.** A company is resident if it is (art. 7 point 37):
- a Romanian legal person;
- a foreign legal person with its place of effective management in Romania;
- an EU-law legal person (for example an SE) with its registered office in Romania.

A resident is taxed on worldwide profit.

Place of effective management (art. 7 point 18) means the foreign company carries out real economic operations in Romania, unless shown otherwise, and either:
- its strategic decisions are taken in Romania by its executive directors or board; or
- at least 50% of its executive directors or board members are Romanian residents.

ANAF decides residence from a questionnaire and supporting documents (art. 8^1(2)-(3)). A company found resident must register within 30 days of the notice, keep its accounts in Romania and stay resident for at least one fiscal year (art. 8^1(4)). Where a treaty state also claims the company, the treaty decides (art. 8^1(1)). Retain the supporting board/incorporation/register/premises/director documents in art. 8^1(2), including the 45-calendar-day notification of changes to the foreign-register extract. Artificial arrangements must not be used to manufacture low or no taxation (art. 8^1(7)). A Romanian-incorporated company remains domestically resident under art. 7 points 29 and 37; moving its board alone does not establish an actual residence transfer or loss of Romanian taxing rights.

## Rates, bands and thresholds

| Item | Rate or figure | Tax year | Source |
|---|---|---|---|
| General personal income tax under Title IV; express category-specific rates override it (art. 64(2)); consult the domestic income skills for each category | 10% | 2026 | Fiscal Code art. 64(1), [ANAF consolidated Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Dividends paid to resident individuals | 16% final, for dividends distributed from 1 January 2026 (10% on 2025 interim dividends) | 2026 | art. 97(7) and the Legea 141/2025 art. VII note, same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Employee pension contribution (CAS) | 25% | 2026 | art. 138(a), same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Employee health contribution (CASS) | 10% | 2026 | art. 156, same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Corporate income tax, including the company exit tax | 16% | 2026 | art. 17 and art. 40^3(1)(b), same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Company exit tax payment by instalments (moves to an EU state, or to an EEA state that has a recovery assistance agreement with Romania or the EU) | equal instalments over 5 years | 2026 | art. 40^3(4) and (5), same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Withholding on dividends paid to non-residents | 16% on dividends distributed from 1 January 2026 (or from the first day of a modified fiscal year starting in 2026); 10% on dividends distributed on 2025 interim financial statements | 2026 | art. 224(4)(b), same page; Legea 141/2025 art. II point 41 and art. VII(1)(h) and (2), [ANAF copy of Legea 141/2025](https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf) |
| Withholding on interest, royalties, commissions, management or consultancy fees, services performed in Romania, and other listed income paid to individuals resident in the EU or in a treaty state | 10% | 2026 | art. 224(4)(c^1), same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Withholding on any other Romanian-source income of non-residents (including payments to companies) | 16% | 2026 | art. 224(4)(d), same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Withholding on interest, royalties, commissions, management or consultancy fees, services performed in Romania, independent professions and liquidation proceeds paid to an account in a state with no exchange-of-information instrument, where the transaction is artificial | 50% | 2026 | art. 224(4)(c), same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Dividends to an EU parent company (Parent-Subsidiary Directive) | exempt with at least 10% held for an unbroken year ending on the payment date, qualifying legal form, residence and tax status, qualifying payer and anti-abuse conditions | 2026 | art. 229(1)(c), same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Dividends to a company resident in Iceland, Liechtenstein or Norway | exempt on the same conditions as for a Romanian parent (art. 43) | 2026 | art. 229(1)(c^1), same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Interest and royalties to an associated EU company (Interest and Royalties Directive) | exempt with statutory association of at least 25%, including a third EU company directly holding at least 25% in each company, for 2 uninterrupted years; qualifying EU company/PE, beneficial ownership and payment-date attestation | 2026 | art. 255(1), (10) and art. 258(b), same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Salary of a person with digital nomad status (OUG 194/2002) working remotely for a foreign employer or own foreign company | not taxable under art. 228(d) only with statutory digital-nomad status, qualifying foreign-company ICT work and presence not exceeding 183 days in a consecutive 12-month interval ending in the tax year | 2026 | art. 228(d), same page  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |

**Digital-nomad contributions.** The statutory exceptions in art. 136(b) and art. 153(1)(b) have their own contributor-category, status and presence conditions. A tax residence conclusion alone does not establish pension/health coverage. EU coordination and applicable social-security agreements must be resolved before payroll is computed ([Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm)).

## The base

- **Residents** are taxed on worldwide income (art. 7 point 37; art. 59(1)(a) and (b)). There is no remittance basis.
- **Non-resident individuals** are taxed only on Romanian income (art. 59(1)(c)-(e)):
  - work done in Romania (salary), even if paid from abroad (art. 223(2)(d), art. 127);
  - the net income of a permanent establishment in Romania (art. 126);
  - the income types listed in art. 223(1), taxed by withholding at the rates above.
- **What counts as Romanian-source income for non-residents** (art. 223(1)):
  - dividends, interest, royalties and commissions paid by a resident (or by a non-resident's Romanian permanent establishment where the payment is its expense);
  - management and consultancy fees paid by a resident;
  - services performed in Romania;
  - independent professions carried on in Romania in the alternatives stated in art. 223(1)(l): otherwise than through a permanent establishment or for periods not exceeding 183 days in the relevant consecutive 12-month interval;
  - directors' fees paid to foreign companies;
  - prizes;
  - liquidation proceeds.

  This applies whether the income is received in Romania or abroad.
- **Income that is not withheld under Title VI** is taxed under the corporate or individual tax rules instead (art. 223(2)). This covers:
  - income of a Romanian permanent establishment;
  - a foreign company's income from Romanian real estate, including rent, and from natural resources;
  - non-resident individuals' employment income;
  - directors' fees paid to non-resident individuals.
- **Withholding is the final tax** unless the law lets the non-resident opt to regularise (art. 224(9)). The relevant options depend on the beneficiary and treaty/information-exchange conditions in each article, rather than EU/EEA status alone:
  - companies on interest (art. 225);
  - individuals on independent activities (art. 226);
  - artists and sportspeople (art. 227).

  EU and EEA individuals get the corresponding resident deductions with supporting evidence, no duplicate home-state deduction and the art. 128(3) information-exchange condition for relevant EEA states.
- **Not taxable in Romania** (art. 228):
  - gains of foreign collective investment undertakings on Romanian securities;
  - gains made by non-residents on foreign capital markets from shares in residents or securities issued by Romanian residents;
  - the digital nomad salary described above.
- **Company exit tax base** (art. 40^3(1)): the market value of the assets transferred, minus their tax value. A gain is taxed at 16%. A loss is recovered against gains of the same kind using art. 31. Article 40^3(11) excludes specified financing/security/prudential-capital/liquidity transfers where return to Romania within 12 months is established; do not charge an excluded temporary transfer.

  The charge applies when a company:
  - moves assets from its Romanian head office to a permanent establishment abroad;
  - moves assets from a Romanian permanent establishment abroad;
  - moves its tax residence out of Romania, except assets that stay effectively connected with a Romanian permanent establishment;
  - moves a business carried on through a Romanian permanent establishment abroad.

  In each case the charge applies only where Romania loses the right to tax (art. 40^3(3)). Assets moving in from another EU state take the value set by that state, unless it is not market value (art. 40^3(9)).
- **Individuals who leave.** Apply the actual income/disposal rules for each asset; this skill does not compute a hypothetical charge on all unrealised personal gains. The continuing worldwide-liability rules in art. 59(5) and (7) are:
  - a resident with a Romanian domicile who moves to a treaty state stays taxable on worldwide income until the date residence changes;
  - one who moves to a non-treaty state stays taxable on worldwide income for the calendar year of the move and the next 3 calendar years.

## Deadlines and filing

| Event | What to file | When | Source |
|---|---|---|---|
| Arrival, more than 183 days in any 12 months | Z015 "Chestionar pentru stabilirea rezidenței fiscale a persoanei fizice la sosirea în România", with passport, Romanian residence or tax registration document, and proof of a home in Romania | within 30 days after completing 183 days of presence under OMFP 1099/2016 art. 14; ANAF replies within 30 days under art. 16(3). | [OMFP 1099/2016, arts. 14–16](https://static.anaf.ro/static/10/Anaf/legislatie/OMFP1099_2016.pdf); current form-download steps are held below |
| Departure for more than 183 days in any 12 months | Z017 "Chestionar pentru stabilirea rezidenței fiscale a persoanei fizice la plecarea din România", plus a foreign residence certificate where available | 30 days before leaving. ANAF replies within 15 days. | art. 59(4), (5), (7); [OMFP 1099/2016, arts. 6, 19 and 20](https://static.anaf.ro/static/10/Anaf/legislatie/OMFP1099_2016.pdf) |
| Filing method for Z015 and Z017 | post with acknowledgement, counter, or lawful remote electronic transmission under OMFP 1099/2016 art. 6; current Z015/Z017 portal steps remain held below | n/a | [OMFP 1099/2016, arts. 6, 19 and 20](https://static.anaf.ro/static/10/Anaf/legislatie/OMFP1099_2016.pdf) |
| Foreign employer not running Romanian payroll | monthly return and payment of the salary tax by the employee | by the 25th of the following month | art. 82(2)  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Romanian host entity of such a worker | tells ANAF the start and end dates of the work | within 30 days of each event, except where the host fulfils the art. 82(4) withholding duty | art. 82(5)  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Stay extended beyond the treaty period | tax declared and paid for the whole period of work in Romania | by the 25th of the month after the treaty limit is passed | art. 82(3)  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Withholding on payments to non-residents | withheld at payment, declared and paid in lei | by the 25th of the month after payment | art. 224(5)  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Treaty or directive rate | non-resident gives the payer a tax residence certificate (original or legalised copy with an authorised Romanian translation; an electronic certificate counts as an original) | at payment. A certificate given later lets the payer correct the tax within the limitation period. A certificate presented for the payment year remains valid for the first 60 calendar days of the next year unless residence changes. For EU relief retain the required beneficiary declaration and legal-form, tax-status, holding and period evidence. | art. 230(2)  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Annual withholding information return | one return per beneficiary | by the last day of February for the previous year | art. 231(1)  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Foreign company with place of effective management in Romania | register with ANAF | within 30 days of being notified it is resident | art. 8^1(4)(a)  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Company exit tax | declare and pay for the reference period under art. 40^3(2), read with arts. 41 and 42; art. 42(5) expressly excludes this exit amount from the annual CIT return | establish the applicable reference-period deadline and special declaration route; do not automatically file it in the ordinary annual return | art. 40^3(2), art. 41 and art. 42(5)  [Official Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |

**Distributed but unpaid nonresident dividends (art. 224(5)).** If a lawful distribution remains unpaid at the end of the year in which it was approved, declare and pay the dividend tax by 25 January of the following year, or by the 25th of the first month of the following modified fiscal year, as applicable. No tax is calculated, withheld or paid if, on the last day of that calendar or modified fiscal year, the foreign legal-person beneficiary meets art. 229(1)(c) or (c^1). This specific rule qualifies the ordinary payment-date/month-after-payment row above.

For the 5-year exit tax instalment plan, a guarantee is required where there is a real and demonstrable risk of non-collection. The law defines that risk as the company's ANAF record showing, on the date it files the return containing the exit tax, overdue budget obligations more than 90 days old "and/or" with a total value over RON 20,000, including the exit tax (art. 40^3(4^1)). The guarantee must be given within 10 days of ANAF's agreement in principle.

The plan is not granted where the company is in bankruptcy or liquidation, or where the exit tax is set off against amounts ANAF owes the company (art. 40^3(4^4)).

The plan ends immediately if any of these happens (art. 40^3(6)):
- the assets or the business are sold;
- the assets or the company's residence move on to a third country (except an EEA state with a recovery assistance agreement, art. 40^3(7));
- the company goes bankrupt or into liquidation;
- an instalment is more than 90 days late.

Interest runs on the instalments (art. 40^3(4^3), Procedure Code art. 197).

## Penalties and interest

All from the Procedure Code ([ANAF consolidated text](https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm)):

- **Late payment interest:** 0.02% for each day late, from the day after the due date to the day of payment (art. 174(1) and (5)).
- **Late payment penalty:** 0.01% for each day late, on top of interest (art. 176(2) and (3)). It does not apply where the non-declaration penalty applies (art. 176(4)).
- **Non-declaration penalty:** 0.08% a day on tax that was not declared or was declared wrongly and is then assessed by ANAF (art. 181(1)). It falls by 75% if the assessed tax is paid or set off by the due date in the assessment (art. 156(1)), or put into an instalment plan, in which case the reduction is given when the plan ends (art. 181(2)). It is not charged below RON 50 and cannot ordinarily exceed the principal tax (art. 181(6) and (11)); judicially established tax evasion has the art. 181(3) increase and exception. The art. 181(7) exception applies where the treatment follows the central tax authority's communicated interpretation. Where inspection assesses because no return was filed, art. 181(9) excludes an additional nonfiling fine.
- **Late filing of a company return or a registration:** a fine of RON 1,000 to 5,000 for medium and large companies, and RON 500 to 1,000 for other companies. The general RON 500 to 1,000 band for individuals applies to the ordinary registration/declaration offences in art. 336(1)(a)-(b) and (2)(d), subject to the specific income-return and residence-questionnaire bands below.
- **Late arrival or departure residence questionnaire (Z015/Z017):** RON 50 to 100 for a person required to file it under the Fiscal Code (art. 336(3^1)); the general registration/declaration band above does not apply to this specific offence.
- **Late filing of an individual's income return or Declarația unică:** a fine of RON 50 to 500 (art. 336(3)).
- **Failing to withhold, or withholding and not paying over:** a fine, by the amount of tax involved (art. 336(1)(o)-(p) and (2)(f)-(h)):
  - up to RON 50,000: RON 4,000 to 6,000 for medium and large companies; RON 1,000 to 1,500 for other companies and individuals;
  - above RON 50,000 up to RON 100,000 inclusive: RON 12,000 to 14,000; RON 4,000 to 6,000;
  - over RON 100,000: RON 25,000 to 27,000; RON 6,000 to 8,000.
- **Interest on instalment plans:** at the art. 174 rate, or 0.015% a day where the whole guarantee is a bank guarantee letter, a guarantee insurance policy or cash held at the State Treasury (art. 197(1)).

## Cross-border points

- **Treaty tie-breaker.** For individuals, a treaty overrides the domestic tests where the person proves residence in the other state with a residence certificate (Fiscal Code art. 59(3) and (6)). For companies, the treaty decides dual residence (art. 8^1(1)). Treaty texts and tie-breaker order are not repeated here; see oecd-model-treaty-defaults and the specific treaty.
- **Treaty and EU rates.** On withholding, the lower of the domestic, treaty or EU-law rate applies, if the non-resident proves residence and, for EU-law relief, beneficial ownership (art. 230(1) and (2)). Tax withheld above the treaty rate is refunded under the Procedure Code (art. 230(4)).
- **Anti-abuse.** The EU dividend exemption does not apply to non-genuine arrangements set up mainly for the tax advantage (art. 229(2)). The general anti-abuse rule applies to corporate tax (art. 40^4).
- **Foreign tax relief for residents.** A resident individual gets a credit where the treaty uses that method, limited to Romanian tax on the foreign income, separately by country and income type, with actual foreign-tax payment proof (art. 131(1), (3) and (4)). The exemption method still requires the stated evidence and annual reporting (art. 131(2)). Foreign amounts use the art. 131(6) annual-average exchange rules.
- **Social-security boundary.** The Fiscal Code applies Romanian contributions subject to EU coordination and social-security agreements (arts. 135^2, 136 and 153, [official text](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm)). Do not infer competent coverage merely from tax residence or a posting label. The prior detailed Regulation 883/2004 propositions and A1 procedure are held under Not yet confirmed until the original EU text is recovered; route the case to eu-social-security-coordination with the actual work/state/coverage evidence.
- **Domestic computations:** employee salary tax and contributions are in ro-payroll-social. Self-employed income tax is in ro-income-tax and its CAS/CASS in ro-cas-cass. Corporate tax is in ro-corporate-income-tax.

## Two worked examples that recompute

### Historical fixture 1: an EU national moves to Bucharest for a Romanian job

The following original case record and arithmetic are retained. Its treaty, coverage and payroll assumptions are not a current residence or filing conclusion; obtain the evidence and resolve the held EU/portal points before applying it.

Ana, a Portuguese national, arrives on 1 March 2026 to work for a Romanian company at a gross salary of RON 20,000 a month. She rents a flat and stays.

1. **Residence.** Ana passes 183 days in Romania at the end of August 2026. She must file Z015 within 30 days of that date. Unless Portugal is shown to be her treaty residence, she is resident from 1 March 2026, her arrival date (art. 59(2^1)). Her worldwide income from that date is taxable in Romania.
2. **Social security.** She works in Romania for a Romanian employer, so Romanian contributions apply (Reg. 883/2004 art. 11(3)(a)).
3. **Monthly payroll.**
   - CAS: 25% of RON 20,000 = RON 5,000.
   - CASS: 10% = RON 2,000.
   - Taxable base: RON 13,000.
   - Income tax: 10% = RON 1,300 (art. 78(2)(a)).

   No personal deduction applies. Ana is over 26 and has no children in school. The basic deduction is available only where gross pay is no more than RON 2,000 above the national minimum gross wage (art. 77(3)), and RON 20,000 is above that limit at any minimum wage below RON 18,000. A parent would get RON 100 a month for each child under 18 enrolled in school, whatever the salary (art. 77(10)(b)).
4. **Net pay:** RON 11,700 a month.

```oa-check
name: RO inbound employee, gross RON 20,000 a month (2026)
inputs:
  gross: 20000
steps:
  - cas: gross * 0.25
  - cass: gross * 0.10
  - base: gross - cas - cass
  - income_tax: base * 0.10
  - net: gross - cas - cass - income_tax
expected:
  cas: 5000.00
  cass: 2000.00
  base: 13000.00
  income_tax: 1300.00
  net: 11700.00
```

### Historical fixture 2: a Romanian company moves its tax residence to another EU state

The original raw scenario and computations follow unchanged. Moving management alone is insufficient under the incorporation test; this example is usable only after an actual tax-residence transfer and loss of Romanian taxing rights are established. The final third-country sentence is subject to the qualifying EEA exception in art. 40^3(7), and all bankruptcy, offset and guarantee conditions apply.

A Romanian SRL moves its place of effective management to Austria in 2026. No Romanian permanent establishment remains.

1. **Exit tax.** Its assets have a market value of RON 5,000,000 and a tax value of RON 3,000,000. The gain is RON 2,000,000. Exit tax at 16% is RON 320,000 (art. 40^3(1) and (3)(c)).
2. **Instalments.** Austria is an EU state, so the company can pay in equal instalments over five years (art. 40^3(4)(c)). If the schedule is one instalment a year, each one is RON 64,000, plus interest under Procedure Code art. 197.
3. **Guarantee.** Art. 40^3(4^1) requires a guarantee where there is a real risk of non-collection. It defines that risk as overdue budget obligations more than 90 days old "and/or" with a total value over RON 20,000, including the exit tax. The text is unclear on whether an exit tax that is not yet overdue counts towards the RON 20,000 on its own. Check the company's ANAF record, and confirm with ANAF before relying on no guarantee.
4. **Ending the plan.** The plan ends if the company later sells the assets or moves on to a third country.

```oa-check
name: RO company exit tax on residence transfer to an EU state (2026)
inputs:
  market_value: 5000000
  tax_value: 3000000
  rate: 0.16
  years: 5
steps:
  - gain: market_value - tax_value
  - exit_tax: gain * rate
  - annual_instalment: exit_tax / years
expected:
  gain: 2000000.00
  exit_tax: 320000.00
  annual_instalment: 64000.00
```

### Current case 1: individual versus company recipient of a service fee

Assume a Romanian payer owes RON 100,000 gross for consultancy within art. 223(1)(i). In the first alternative the beneficiary is an individual resident in an EU state, evidenced for art. 224(4)(c^1), with no lower treaty relief established. In the second it is a foreign company with no PE attribution, directive exemption, treaty reduction or artificial-transaction condition established. Gross withholding is RON 10,000 versus RON 16,000; the remaining payment is RON 90,000 versus RON 84,000. This is a classification comparison, not an election to change the recipient's actual identity. Withhold at payment and declare/pay by the 25th of the next month (art. 224(5)).

```oa-check
name: RO 2026 consultancy withholding, qualifying individual versus company
inputs:
  gross: 100000
steps:
  - individual_wht: gross * 0.10
  - company_wht: gross * 0.16
  - individual_paid: gross - individual_wht
  - company_paid: gross - company_wht
  - difference: company_wht - individual_wht
expected:
  individual_wht: 10000
  company_wht: 16000
  individual_paid: 90000
  company_paid: 84000
  difference: 6000
```

### Current case 2: chargeable asset transfer versus qualifying temporary return

A company transfers an asset from its Romanian head office to its EU PE. Market value is RON 800,000 and tax value RON 500,000. If Romania loses its taxing right and the temporary-return exception does not apply, the RON 300,000 gain yields RON 48,000 exit tax. If a qualifying five-year schedule is granted, equal annual principal is RON 9,600, plus applicable interest and any required guarantee. If instead the transfer is a qualifying article 40^3(11) liquidity-management transfer whose return within 12 months is established, that exception removes this exit charge. A plan or exception cannot be assumed merely because the destination is in the EU.

```oa-check
name: RO 2026 exit transfer compared with statutory temporary-return exception
inputs:
  market: 800000
  fiscal_value: 500000
steps:
  - gain: market - fiscal_value
  - tax_chargeable: gain * 0.16
  - annual_principal_if_granted: tax_chargeable / 5
  - tax_if_temporary_exception_established: tax_chargeable * 0
expected:
  gain: 300000
  tax_chargeable: 48000
  annual_principal_if_granted: 9600
  tax_if_temporary_exception_established: 0
```

## Ask the client first

1. Where is your domicile, where does your family live, and where are your home, job and assets? Those facts decide the domicile and centre of vital interests tests.
2. Exact arrival and departure dates, and days in Romania in each 12-month window. Those dates decide the 183-day test and when worldwide liability starts or ends.
3. Which country are you moving from or to, and does Romania have a tax treaty with it? Do you hold a residence certificate from it? That decides the tie-breaker, and whether the extra three years of worldwide tax applies.
4. Who pays you (Romanian or foreign employer, your own foreign company), and are you posted with an A1 certificate? That decides payroll, the art. 82 monthly return, the digital nomad rule and which social security system applies.
5. For companies: where are the board meetings held and where do the directors live? What assets or business are moving, at what market and tax values, and to which state? That decides residence, the exit tax and the instalment option.
6. For payments abroad: what type of income is paid, and to whom (company or individual)? Which country is the recipient in, and is there a residence certificate and, for EU relief, a beneficial ownership statement? That decides the 16%, 10%, 50%, treaty or nil rate.

## Sources

| Source | URL | Read on |
|---|---|---|
| Fiscal Code, official portal: retained capture labelled 25 October 2026, including art. 7, 59, 40^3 and amendment annotations; historical provenance only. Fresh ordinary access/version confirmation remains unrecovered; usable operative rules are sourced to ANAF below. | https://legislatie.just.ro/Public/DetaliiDocument/171282 | 2026-11-15 retained-source read; fresh ordinary portal read unconfirmed |
| Fiscal Code, ANAF consolidation, header Legea 204/2026; arts. 1, 7, 8^1, 14, 17, 40^3, 40^4, 41–42, 59, 64, 77–78, 82, 97, 126–127, 135^2, 128, 131, 136, 138, 153, 156, 223–231, 255 and 258 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-11-15, read for residence, source, withholding, directive conditions, exit tax and filing; ANAF warns it is not an official republication |
| Procedure Code, ANAF consolidation, header Legea 170/2026; arts. 156, 174–176, 181, 197 and 336 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm | 2026-11-15, read for assessment payment, interest, nondeclaration, instalment interest and fine bands |
| Legea 141/2025, II.41 and VII(1)(h),(2) | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf | 2026-11-15, read for nonresident dividend commencement and 2025 interim treatment |
| OMFP 1099/2016, July residence order, arts. 1–26 | https://static.anaf.ro/static/10/Anaf/legislatie/OMFP1099_2016.pdf | 2026-11-15, read for questionnaires, evidence, arrival/departure deadlines and notification; not the unrelated March ANAF order with the same number |
| Legea 204/2026, arts. I–II | https://legislatie.just.ro/Public/DetaliiDocument/315641 | 2026-11-15, read for approval of OG 22/2025 and traditional-alcohol excise amendment; no broad income-rate inference |

Not yet confirmed:
- Research boundary recorded 2026-11-15: current official Z015/Z017 download, SPV and e-guvernare.ro screen/field/submission steps, and the old form-list assertion that both were published 07.04.2020. The original ANAF form list was https://static.anaf.ro/static/10/Anaf/Declaratii_R/descarcare_declaratii.htm and its 16.12.2020 assistance note was https://static.anaf.ro/static/10/Brasov/Brasov/chestionar_rezidenta.pdf. Their old paths and dates are preserved as provenance, not live filing instructions. Use the statutory electronic-filing route only after confirming the current implementation.
- Research boundary recorded 2026-11-15: Regulation 883/2004 originals and amendments were not recovered in this run: EUR-Lex returned a robot check or an unrelated journal page. The old asserted rules are held, not usable instructions: one state's coverage (art. 11(1)); work-state default (11(3)(a)); employed posting for no more than 24 months without replacing a posted worker (12(1)); self-employed posting for 24 months (12(2)); multi-state work (13). The original link was https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02004R0883-20190731. The Romanian A1 issuing body/procedure remains unconfirmed.
- The historical salary fixture's current payroll deduction/wage and competent-coverage assumptions, and the specific Portugal treaty outcome, have not been freshly established here. Its raw facts and arithmetic remain, but must not be applied as a completed current filing result.
- The old blanket assertion that no special low-rate inbound regime exists, and that the only inbound relief is digital nomad relief, is not established by a comprehensive current-law search. Do not use that negative assertion to rule out fact-specific relief. Likewise, the old assertion of no personal exit charge on all unrealised gains is not a comprehensive asset-by-asset conclusion.
- The original ordinary-CIT comparator was the 25th after quarters 1 to 3 and 25 June for the annual return. Article 42(5) expressly excludes the art. 40^3 exit amount from that annual return. The exact special form and period-specific implementation have not been confirmed; do not use the old automatic 25-June annual exit-return instruction.
- The precise treatment of a not-yet-overdue exit-tax amount within the RON 20,000 guarantee-risk wording is not established. Do not rely on a no-guarantee result; retain the actual ANAF record and obtain the determination. Partner-specific treaty rates, tie-breakers, limitation periods and the actual calendar-day roll-over for particular filing dates require their operative texts.
- The former October 2026 source-access failures and Legea 170/2026 amendment gap remain historical research limitations. The retained portal capture labels its version 25 October 2026, but fresh ordinary access and version confirmation remain unrecovered. Usable art. 7, 59 and 40^3 rules are established from the actually read ANAF text. The earlier portal annotation attributed art. 59(2^1)'s insertion from 1 January 2021 to Legea 296/2020 I.27; that annotation remains historical provenance. The operative first-arrival rule is separately present in ANAF art. 59(2^1), so the earlier 2020 note's prospective-residence wording must not override it. No claim is made that every later implementing order or treaty was read.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ro-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ro-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
