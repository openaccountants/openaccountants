---
name: ro-cross-border
description: "Use this skill when a person or company crosses Romania's border for tax: tax residence tests for individuals (domicile, centre of vital interests, more than 183 days in any 12 months) and for companies (Romanian legal person or place of effective management), arriving in Romania (the Z015 residence questionnaire, the digital nomad exemption), leaving (the Z017 questionnaire 30 days before departure, the extra three years of worldwide tax after a move to a non-treaty state, and the 16% company exit tax with a five-year instalment option), non-residents with Romanian income, withholding on outbound dividends, interest, royalties and service fees (16%, 10%, 50%), EU directive exemptions and treaty relief. Tax year 2026 (calendar year). Trigger phrases: moving to Romania, leaving Romania, non-resident Romania, expat Romania, exit tax Romania, digital nomad Romania, withholding tax Romania, certificat de rezidenta fiscala. Out of scope: ro-income-tax, ro-corporate-income-tax, ro-payroll-so"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ro-cross-border"
  jurisdiction: "RO"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Romania cross-border: residence, arriving, leaving, non-residents and withholding (2026)

This is the hub skill for what changes when a person or a company crosses Romania's border. It covers residence, arrival and departure filings, the company exit tax, tax on non-residents' Romanian income, and withholding on payments abroad. The domestic computations live in the sibling skills: ro-income-tax (self-employed individuals), ro-corporate-income-tax (companies), ro-payroll-social (employee contributions and payroll), ro-cas-cass (self-employed contributions). EU social security rules are in eu-social-security-coordination; treaty defaults are in oecd-model-treaty-defaults.

The law is Legea 227/2015 (Codul fiscal, "the Fiscal Code") and Legea 207/2015 (Codul de procedură fiscală, "the Procedure Code"). Every article below was read on 22 October 2026 in ANAF's consolidated texts, both shown as last updated by Legea 170/2026. ANAF notes that these consolidations are not an official republication.

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
- A newcomer who meets the 183-day test is taxed on worldwide income from the first day of arrival in Romania (art. 59(2^1)). Before the 183 days are reached, they are taxed as a non-resident; once the test is met, worldwide liability runs back to the arrival date.
- The centre of vital interests rule gives way to a tax treaty where the person proves residence in the treaty state (art. 59(3)). For every residence test, a treaty provision prevails over the Fiscal Code (art. 1(3)).
- A newcomer who became resident stays resident until they leave Romania (art. 59(4)).

**Companies.** A company is resident if it is (art. 7 point 37):
- a Romanian legal person;
- a foreign legal person with its place of effective management in Romania;
- an EU-law legal person (for example an SE) with its registered office in Romania.

A resident is taxed on worldwide profit.

Place of effective management (art. 7 point 18) means the foreign company carries out real economic operations in Romania, unless shown otherwise, and either:
- its strategic decisions are taken in Romania by its executive directors or board; or
- at least 50% of its executive directors or board members are Romanian residents.

ANAF decides residence from a questionnaire and supporting documents (art. 8^1(2)-(3)). A company found resident must register within 30 days of the notice, keep its accounts in Romania and stay resident for at least one fiscal year (art. 8^1(4)). Where a treaty state also claims the company, the treaty decides (art. 8^1(1)).

## Rates, bands and thresholds

| Item | Rate or figure | Tax year | Source |
|---|---|---|---|
| Personal income tax on salary, self-employment, rent, investment and most other income (residents and non-residents taxed under Title IV) | 10% | 2026 | Fiscal Code art. 64(1), [ANAF consolidated Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) |
| Dividends paid to resident individuals | 16% final, for dividends distributed from 1 January 2026 (10% on 2025 interim dividends) | 2026 | art. 97(7) and the Legea 141/2025 art. VII note, same page |
| Employee pension contribution (CAS) | 25% | 2026 | art. 138(a), same page |
| Employee health contribution (CASS) | 10% | 2026 | art. 156, same page |
| Corporate income tax, including the company exit tax | 16% | 2026 | art. 17 and art. 40^3(1)(b), same page |
| Company exit tax payment by instalments (moves to an EU state, or to an EEA state that has a recovery assistance agreement with Romania or the EU) | equal instalments over 5 years | 2026 | art. 40^3(4) and (5), same page |
| Withholding on dividends paid to non-residents | 16% on dividends distributed from 1 January 2026 (or from the first day of a modified fiscal year starting in 2026); 10% on dividends distributed on 2025 interim financial statements | 2026 | art. 224(4)(b), same page; Legea 141/2025 art. II point 41 and art. VII(1)(h) and (2), [ANAF copy of Legea 141/2025](https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf) |
| Withholding on interest, royalties, commissions, management or consultancy fees, services performed in Romania, and other listed income paid to individuals resident in the EU or in a treaty state | 10% | 2026 | art. 224(4)(c^1), same page |
| Withholding on any other Romanian-source income of non-residents (including payments to companies) | 16% | 2026 | art. 224(4)(d), same page |
| Withholding on interest, royalties, commissions, management or consultancy fees, services performed in Romania, independent professions and liquidation proceeds paid to an account in a state with no exchange-of-information instrument, where the transaction is artificial | 50% | 2026 | art. 224(4)(c), same page |
| Dividends to an EU parent company (Parent-Subsidiary Directive) | exempt with at least 10% held for an unbroken year ending on the payment date | 2026 | art. 229(1)(c), same page |
| Dividends to a company resident in Iceland, Liechtenstein or Norway | exempt on the same conditions as for a Romanian parent (art. 43) | 2026 | art. 229(1)(c^1), same page |
| Interest and royalties to an associated EU company (Interest and Royalties Directive) | exempt with a direct holding of at least 25% held for at least 2 years | 2026 | art. 255(1), (10) and art. 258(b), same page |
| Salary of a person with digital nomad status (OUG 194/2002) working remotely for a foreign employer or own foreign company | not taxable, if present in Romania for not more than 183 days in any 12 months | 2026 | art. 228(d), same page |

**There is no special low-rate inbound regime for new arrivals in the Fiscal Code.** The only inbound relief we found is the digital nomad rule above, which ends once the 183-day test is met. The digital nomad is also outside the Romanian pension and health contribution systems within the same 183 days (art. 136(b) and art. 153).

## The taxable base

- **Residents** are taxed on worldwide income (art. 7 point 37; art. 59(1)(a) and (b)). There is no remittance basis.
- **Non-resident individuals** are taxed only on Romanian income (art. 59(1)(c)-(e)):
  - work done in Romania (salary), even if paid from abroad (art. 223(2)(d), art. 127);
  - the net income of a permanent establishment in Romania (art. 126);
  - the income types listed in art. 223(1), taxed by withholding at the rates above.
- **What counts as Romanian-source income for non-residents** (art. 223(1)):
  - dividends, interest, royalties and commissions paid by a resident (or by a non-resident's Romanian permanent establishment where the payment is its expense);
  - management and consultancy fees paid by a resident;
  - services performed in Romania;
  - independent professions carried on in Romania for up to 183 days and not through a permanent establishment;
  - directors' fees paid to foreign companies;
  - prizes;
  - liquidation proceeds.

  This applies whether the income is received in Romania or abroad.
- **Income that is not withheld under Title VI** is taxed under the corporate or individual tax rules instead (art. 223(2)). This covers:
  - income of a Romanian permanent establishment;
  - a foreign company's income from Romanian real estate, including rent, and from natural resources;
  - non-resident individuals' employment income;
  - directors' fees paid to non-resident individuals.
- **Withholding is the final tax** unless the law lets the non-resident opt to regularise (art. 224(9)). EU and EEA residents can opt to be taxed on the net income instead and credit the tax withheld:
  - companies on interest (art. 225);
  - individuals on independent activities (art. 226);
  - artists and sportspeople (art. 227).

  EU and EEA individuals also get the same deductions as residents, where not deducted at home (art. 128).
- **Not taxable in Romania** (art. 228):
  - gains of foreign collective investment undertakings on Romanian securities;
  - gains made by non-residents on foreign capital markets from shares in residents or securities issued by Romanian residents;
  - the digital nomad salary described above.
- **Company exit tax base** (art. 40^3(1)): the market value of the assets transferred, minus their tax value. A gain is taxed at 16%. A loss is recovered against gains of the same kind.

  The charge applies when a company:
  - moves assets from its Romanian head office to a permanent establishment abroad;
  - moves assets from a Romanian permanent establishment abroad;
  - moves its tax residence out of Romania, except assets that stay effectively connected with a Romanian permanent establishment;
  - moves a business carried on through a Romanian permanent establishment abroad.

  In each case the charge applies only where Romania loses the right to tax (art. 40^3(3)). Assets moving in from another EU state take the value set by that state, unless it is not market value (art. 40^3(9)).
- **Individuals who leave** face no exit charge on unrealised gains in the Fiscal Code. Instead the length of worldwide liability depends on where they go (art. 59(5) and (7)):
  - a resident with a Romanian domicile who moves to a treaty state stays taxable on worldwide income until the date residence changes;
  - one who moves to a non-treaty state stays taxable on worldwide income for the calendar year of the move and the next 3 calendar years.

## Deadlines and filing

| Event | What to file | When | Source |
|---|---|---|---|
| Arrival, more than 183 days in any 12 months | Z015 "Chestionar pentru stabilirea rezidenței fiscale a persoanei fizice la sosirea în România", with passport, Romanian residence or tax registration document, and proof of a home in Romania | within 30 days of reaching the 183 days. ANAF replies within 30 days. | art. 230(3) and (7) (the law leaves the deadline to the norms; OMFP 1099/2016); [ANAF assistance note](https://static.anaf.ro/static/10/Brasov/Brasov/chestionar_rezidenta.pdf); Z015 and Z017 are listed as current on [ANAF's form list](https://static.anaf.ro/static/10/Anaf/Declaratii_R/descarcare_declaratii.htm) |
| Departure for more than 183 days in any 12 months | Z017 "Chestionar pentru stabilirea rezidenței fiscale a persoanei fizice la plecarea din România", plus a foreign residence certificate where available | 30 days before leaving. ANAF replies within 15 days. | art. 59(4), (5), (7); ANAF assistance note |
| Filing method for Z015 and Z017 | post, at the counter, e-guvernare.ro, or SPV (ANAF's online private space) | n/a | ANAF assistance note |
| Foreign employer not running Romanian payroll | monthly return and payment of the salary tax by the employee | by the 25th of the following month | art. 82(2) |
| Romanian host entity of such a worker | tells ANAF the start and end dates of the work | within 30 days of each event | art. 82(5) |
| Stay extended beyond the treaty period | tax declared and paid for the whole period of work in Romania | by the 25th of the month after the treaty limit is passed | art. 82(3) |
| Withholding on payments to non-residents | withheld at payment, declared and paid in lei | by the 25th of the month after payment | art. 224(5) |
| Treaty or directive rate | non-resident gives the payer a tax residence certificate (original or certified copy with a sworn Romanian translation; an electronic certificate counts as an original) | at payment. A certificate given later lets the payer correct the tax within the limitation period. A certificate is valid for the first 60 days of the next year unless residence changes. | art. 230(2) |
| Annual withholding information return | one return per beneficiary | by the last day of February for the previous year | art. 231(1) |
| Foreign company with place of effective management in Romania | register with ANAF | within 30 days of being notified it is resident | art. 8^1(4)(a) |
| Company exit tax | declared and paid with corporate income tax: quarterly by the 25th of the month after quarters 1 to 3, and the annual return by 25 June of the next year | for the period of the transfer | art. 40^3(2), art. 41(1), art. 42(1) |

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
- **Non-declaration penalty:** 0.08% a day on tax that was not declared or was declared wrongly and is then assessed by ANAF (art. 181(1)). It falls by 75% if the assessed tax is paid or set off by the due date in the assessment (art. 156(1)), or put into an instalment plan, in which case the reduction is given when the plan ends (art. 181(2)). It is not charged below RON 50 and cannot exceed the tax it is charged on (art. 181(6) and (11)).
- **Late filing of a company return or a registration:** a fine of RON 1,000 to 5,000 for medium and large companies, and RON 500 to 1,000 for other companies. An individual who files a registration or a declaration other than an income return late is fined RON 500 to 1,000 (art. 336(1)(a)-(b) and (2)(d)).
- **Late filing of an individual's income return or Declarația unică:** a fine of RON 50 to 500 (art. 336(3)).
- **Failing to withhold, or withholding and not paying over:** a fine, by the amount of tax involved (art. 336(1)(o)-(p) and (2)(f)-(h)):
  - up to RON 50,000: RON 4,000 to 6,000 for medium and large companies; RON 1,000 to 1,500 for other companies and individuals;
  - RON 50,000 to 100,000: RON 12,000 to 14,000; RON 4,000 to 6,000;
  - over RON 100,000: RON 25,000 to 27,000; RON 6,000 to 8,000.
- **Interest on instalment plans:** at the art. 174 rate, or 0.015% a day where the whole guarantee is a bank guarantee letter, a guarantee insurance policy or cash held at the State Treasury (art. 197(1)).

## Cross-border points

- **Treaty tie-breaker.** For individuals, a treaty overrides the domestic tests where the person proves residence in the other state with a residence certificate (Fiscal Code art. 59(3) and (6)). For companies, the treaty decides dual residence (art. 8^1(1)). Treaty texts and tie-breaker order are not repeated here; see oecd-model-treaty-defaults and the specific treaty.
- **Treaty and EU rates.** On withholding, the lower of the domestic, treaty or EU-law rate applies, if the non-resident proves residence and, for EU-law relief, beneficial ownership (art. 230(1) and (2)). Tax withheld above the treaty rate is refunded under the Procedure Code (art. 230(4)).
- **Anti-abuse.** The EU dividend exemption does not apply to non-genuine arrangements set up mainly for the tax advantage (art. 229(2)). The general anti-abuse rule applies to corporate tax (art. 40^4).
- **Foreign tax relief for residents.** A resident individual gets a credit for foreign tax where the treaty uses the credit method (art. 131(1)). Where the treaty uses the exemption method, the income is exempt but must still be reported on the Declarația unică (art. 131(2)).
- **EU social security.** Under Regulation (EC) 883/2004 a person is covered by one state's social security only (art. 11(1)). The general rule is the state where the work is done (art. 11(3)(a)).

  A worker posted to Romania by an employer that normally operates in another member state stays in the home system if the posting is expected to last no more than 24 months and does not replace another posted worker (art. 12(1)). The same 24-month rule applies to the self-employed (art. 12(2)). Work in two or more states follows art. 13.

  Romania applies its contributions subject to EU coordination rules (Fiscal Code art. 135^2 and 136). For the A1 certificate and multi-state cases, see eu-social-security-coordination.
- **Domestic computations:** employee salary tax and contributions are in ro-payroll-social. Self-employed income tax is in ro-income-tax and its CAS/CASS in ro-cas-cass. Corporate tax is in ro-corporate-income-tax.

## Worked examples

### Example 1: an EU national moves to Bucharest for a Romanian job

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

### Example 2: a Romanian company moves its tax residence to another EU state

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

## Ask the client first

1. Where is your domicile, where does your family live, and where are your home, job and assets? Those facts decide the domicile and centre of vital interests tests.
2. Exact arrival and departure dates, and days in Romania in each 12-month window. Those dates decide the 183-day test and when worldwide liability starts or ends.
3. Which country are you moving from or to, and does Romania have a tax treaty with it? Do you hold a residence certificate from it? That decides the tie-breaker, and whether the extra three years of worldwide tax applies.
4. Who pays you (Romanian or foreign employer, your own foreign company), and are you posted with an A1 certificate? That decides payroll, the art. 82 monthly return, the digital nomad rule and which social security system applies.
5. For companies: where are the board meetings held and where do the directors live? What assets or business are moving, at what market and tax values, and to which state? That decides residence, the exit tax and the instalment option.
6. For payments abroad: what type of income is paid, and to whom (company or individual)? Which country is the recipient in, and is there a residence certificate and, for EU relief, a beneficial ownership statement? That decides the 16%, 10%, 50%, treaty or nil rate.

## Sources

Read on 2026-10-22:

- Legea 227/2015 privind Codul fiscal, ANAF consolidated text with methodological norms, last updated by Legea 170/2026: https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm (art. 1(3); art. 7 points 6, 18, 27, 28, 37; art. 8^1; art. 13; art. 17; art. 40^3; art. 40^4; art. 41; art. 42; art. 59; art. 64; art. 77; art. 78; art. 82; art. 97(7); art. 126-128; art. 131; art. 135^2; art. 136; art. 138; art. 153; art. 156; art. 223-231; art. 255; art. 258; norms to Title VI)
- Legea 141/2025 privind unele măsuri fiscal-bugetare (Monitorul Oficial 699 of 25 July 2025), text hosted by ANAF: https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf (art. II points 5 and 41; art. VII(1)(c), (h) and (2))
- ANAF, list of downloadable forms (Z015 and Z017, published 07.04.2020): https://static.anaf.ro/static/10/Anaf/Declaratii_R/descarcare_declaratii.htm
- Legea 207/2015 privind Codul de procedură fiscală, ANAF consolidated text, last updated by Legea 170/2026: https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm (art. 156, 174, 176, 181, 197, 336)
- ANAF, DGRFP Brașov, "Depunerea chestionarelor pentru stabilirea rezidenței fiscale a persoanei fizice la plecarea/sosirea din/în România" (dated 16.12.2020): https://static.anaf.ro/static/10/Brasov/Brasov/chestionar_rezidenta.pdf
- Regulation (EC) No 883/2004, consolidated text of 31.07.2019, EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02004R0883-20190731 (art. 11, 12, 13)

Not yet confirmed:
- legislatie.just.ro refused connections again on 22 October 2026 (from the command line, a fetch tool and a browser), so the Fiscal Code texts above come from ANAF's consolidations, which ANAF says are not an official republication. Legea 141/2025 was read in the copy ANAF hosts. We did not read Legea 170/2026 itself; ANAF's consolidations show it changing inheritance tax and payment-plan conditions, not the rates above.
- Whether any emergency ordinance (OUG) after Legea 170/2026 changes these rates for 2026.
- The ANAF assistance note (dated 2020) says a newcomer is non-resident from arrival until becoming resident. The current art. 59(2^1) taxes worldwide income from the first day of arrival once the 183-day test is met. We follow the law; the date art. 59(2^1) was inserted was not checked.
- The Romanian body that issues A1 certificates, and its procedure.
- The 2026 national minimum gross wage (used only to confirm that no personal deduction applies in Example 1).
- Treaty withholding rates for individual treaty partners.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ro-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ro-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
