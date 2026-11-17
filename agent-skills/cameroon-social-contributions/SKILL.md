---
name: cameroon-social-contributions
description: "Cameroon CNPS contributions for 2026: mandatory and voluntary coverage, capped pension/family branches, uncapped occupational risk, registration, declarations, remittance, surcharges and payroll reconciliation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/cameroon-social-contributions"
  jurisdiction: "CM"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# Cameroon social contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026. The prior file credited **Nkinyam Courage Ndasi** with a 2026-06-21 review. That historical attribution remains; it does not approve this rewrite, which has not been reviewed by an accountant. The original identifier 3472800 is retained solely as an unverified historical identifier, not a current credential or approval.

## Who this applies to

Employers and workers covered by the Cameroon Labour Code, including permanent, seasonal, temporary, occasional and domestic workers. Mandatory registration begins with the first worker; it is not conditional on a larger headcount. CNPS (Caisse Nationale de Prévoyance Sociale) manages pension/vieillesse-invalidité-décès, family/prestations familiales and occupational-risk/risques professionnels branches. Do not treat a salaried person as self-employed merely because payroll records are missing.

Voluntary insurance is a separate election for eligible independent, rural, informal and own-account workers, artisans, professionals and business promoters with contributory capacity. CNPS agrees the base; the ordinary employee/employer split does not apply. Public-service pension schemes, foreign detachments and specific bilateral agreements need their own coverage review. Obtain the actual registration/coverage record rather than infer an exemption from nationality or employer label.

The current contribution rates live here. The companion [payroll skill](cameroon-payroll.md) owns salary IRPP, CFC/FNE, local development tax, audiovisual royalty and minimum wages; load it for a gross-to-net payroll. The four passing siblings are unchanged. Their unresolved CNPS wording does not replace the decree actually read here.

## Rates, bands and thresholds

| Item | Rule / amount in XAF unless stated | Official source |
|---|---|---|
| Employee pension | 4.2% of the contributory pension base; employer separately pays 4.2%, total 8.4%. Only this pension branch has an employee CNPS share. | Decree 2016/072 arts 3,10: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Pension/family ceiling | 750,000/month;9,000,000/year. This ceiling applies to the pension and family branches, not occupational risk. | Decree 2016/072 art 4: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Family allowance, general | 7% employer-only, including domestic employees. Agriculture 5.65%; private education 3.7%, using the actual regime. | Decree 2016/072 arts 2,10: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Occupational risk | Group A1.75%, B2.5%, C5%, employer-only on all contributory remuneration after professional costs; no 750,000 ceiling. Use the actual classification. | Decree 2016/072 arts 7-10: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Mixed activities | Under the same legal entity with distinct risk activities, classification follows the highest-risk activity. CNPS may change a class after checking actual activity. | Decree 2016/072 art 9: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Voluntary insurance | 8.4%, entirely borne by the voluntary insured, on a CNPS-agreed base within the remuneration ceiling. The current CNPS agency page states declared income 720,000-9,000,000/year, or 60,000-750,000/month; monthly contributions 5,040-63,000 (also recomputed at 8.4%). It describes both monthly and flexible quarter/semester/year payments: confirm the actual CNPS agreement/process, not a self-chosen exemption from payment. The old 36,270 floor is not current proof. | Decree 2016/072 art 5: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf; CNPS voluntary insurance:declaration/payment guidance: https://www.cnps.cm/fr/?id=90&option=com_sppagebuilder&view=page |
| General-regime arithmetic | Derived below the ceiling and equal assessed bases: employer CNPS 12.95%/13.7%/16.2% forA/B/C; excluding risk 11.2%. These are not flat rates on all high salaries. | Decree 2016/072 arts 2-4,8: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Maximum pension/family shares | Derived: employee pension 31,500/month, employer pension 31,500; family 52,500 general,42,375 agriculture,27,750 education. No corresponding maximum accident amount. | Decree 2016/072 arts 2-4,8: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Registration | Employer affiliation within 8 days of first hire; request worker registration under the decree. Hire/cessation notices separately within 8 days to CNPS and tax administration. | Decree 2015/2517 arts 3,8: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Monthly declaration/payment | Declare all permanent, seasonal, temporary and occasional workers, periods and paid/due wages. Contributions paid in first 15 days of following month with declaration receipt. | Decree 2015/2517 arts 6-7,15: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CNPS late payment | 10% initial surcharge, increased by 3% of contributions for each quarter/part after 3 months from due date; official notification/payment facts control. This differs from DGI interest. | Decree 2015/2517 art 20: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CNPS notices/remission | Notified late surcharges payable within 7 days. Written remission request requires evidence of material/financial impossibility and reasoned force-majeure/good-faith decision. | Decree 2015/2517 arts 20(3),21: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Salary withholding exemption | Gross salary below 62,000/month relieves employer salary-IRPP withholding under 81. It does not exempt CNPS or the separately governed CFC/CRTV levies. | CGI 81: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Tax records | Keep controlled books/registers/support 10 years from last operation recorded or document creation; keep CNPS statements and reconciliations as supporting records. | LPF L5: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |


## The base

### Keep contribution bases separate

Start with actual contributory remuneration and documentary exclusions, not automatically the salary-IRPP base or net bank payment. Decree 2016/072 caps the family and pension bases; occupational risk uses the full relevant remuneration less professional costs. Decree 2015/2517 arts 25-26 exclude specified benefits in kind within CGI limits and expressly listed professional costs/end-of-career indemnities, with excess brought back in. Do not simply import the 30% IRPP lump sum as a universal CNPS expense deduction. The detailed excluded-cost list, applicable floor and special month calculations still require the missing implementing material listed under Sources.

For an all-cash, fully contributory monthly baseS in an ordinary covered case: employee pension=min(S, ceiling)×employee pension rate. Employer CNPS=min(S, ceiling)×employer pension rate + min(S, ceiling)×actual family rate + full assessed occupational-risk base×actual risk rate. Above the ceiling these bases differ. The old payroll file's capped accident maxima are wrong. Its 13,125/18,750/37,500 figures are accident amounts at an assessed base exactly 750,000, not legal maxima. Salary above the cap does not stop further accident contributions.

At/below the ceiling, a combined percentage is only an arithmetic shortcut if each levy really has the same assessed base. Above it, compute each branch. The old 15.20% CNPS headline is not an additional statutory rate: general employer pension+family+mid risk totals 13.70%; adding employer CFC1.5% gives 15.20%, which mixes a tax levy into CNPS. Do not silently substitute that mixed total. CFC/FNE remain separate Treasury obligations with their own bases/exemptions/deadlines in payroll. An employee combined CNPS+CFC shortcut 5.2% or general low-risk employer total 15.45% is likewise only derived below-cap, equal-base arithmetic, never a universal rate.

### No invented defaults

The old social file defaulted an unknown risk to the lowest rate; payroll defaulted to the middle. Neither establishes the enterprise's legal class. Request the classification/notification and actual activity; for an estimate show labelledA/B/C alternatives. Family status must be confirmed for agricultural/private-education employers; a general-regime scenario is not evidence of their regime. Pay frequency, currency and salary/benefit components must be stated. Do not label a low estimate conservative.

### Bank patterns and terminology

Common records include Afriland First Bank, SGBC (Société Générale Cameroun), BICEC, Ecobank Cameroun, UBA Cameroun and Commercial Bank of Cameroon. Match French/English descriptions case-insensitively as clues, then reconcile amount, direction, beneficiary and return. A label alone never proves a tax exemption or payroll deduction.

| Narrative family | Investigate / classification after reconciliation |
|---|---|
| CNPS, CAISSE NATIONALE DE PREVOYANCE, PREVOYANCE SOCIALE, COTISATION CNPS | Outgoing contribution settlement; separate employee liability and employer expense, not a fresh VAT supply |
| PENSION, VIEILLESSE, INVALIDITE | Pension contribution or benefit depending on direction and actual counterparty |
| PRESTATIONS FAMILIALES, ALLOCATIONS FAMILIALES | Family contribution or incoming benefit; do not automatically treat a credit as a contribution |
| RISQUES PROFESSIONNELS, ACCIDENT TRAVAIL | Occupational-risk branch or compensation; inspect supporting record |
| DGI, IMPOTS, DIRECTION GENERALE DES IMPOTS, IRPP, IR SALAIRES, PRECOMPTE | Treasury tax/PAYE settlement, separate from CNPS |
| TVA, TAXE VALEUR AJOUTEE | VAT settlement, separate liability; not CNPS |
| CAC, CENTIMES ADDITIONNELS | Tax surcharge, part of appropriate tax reconciliation |
| CFC, CREDIT FONCIER; FNE, FONDS NATIONAL EMPLOI | Housing/employment fund tax levies, not CNPS |
| TAXE COMMUNALE, TAXE DEVELOPPEMENT LOCAL | Local development tax under actual salary band, not a universal top-band charge |
| RAV, REDEVANCE AUDIOVISUELLE, CRTV | Audiovisual royalty under actual gross-salary band/exemption |
| SALAIRE, PAIE, VIREMENT SALAIRE | Outgoing net wages or incoming employee pay; not a social contribution |
| PENSION CNPS, RENTE, PENSION VIEILLESSE (credit); ALLOCATION FAMILIALE (credit) | Benefit received, not employer contribution payment |

Remittances may recur monthly but timing alone is not proof. Refund/reversal credits can occur; the old statement that statutory contributions are “never credits” is not a valid posting rule. Exclude liability settlement from a second income/VAT-supply posting, while retaining the correct underlying employer expense. A consolidated employer remittance cannot be reverse-engineered as one worker's employee share.

### Workpaper and statement-only fallback

Maintain Client/Employer, CNPS employer number, Employee name, Tax Year (calendar 1 January–31 December), Prepared date, employee number, worker status/coverage, gross and each pay component, contribution exclusions, actual family regime, CNPS risk class/evidence, uncapped base and capped pension/family base. Show each employee/employer branch, then separate CFC/FNE, salary IRPP, local levies, net wages and cost through payroll. Include reference, amount/date paid, return/receipt, due date, reconciliation differences and reviewer flags/defaults. Keep tax residence/day counts as evidence for the separate residence analysis, not a tick-box 183-day conclusion.

With only a bank statement, identify possible CNPS versus DGI/CFC/FNE and benefits. If a debit is proved to be solely one worker's employee pension, divide by its actual rate to infer a capped base; reaching the ceiling shows only salary at least that ceiling. It cannot reveal an uncapped salary. Provide a provisional workpaper, flag missing risk/regime/coverage, and obtain payslips, DIPE, nominative declarations and official account statements before a filing conclusion.

## Deadlines and filing

Decree 2015/2517 arts 3-10 require employer/worker identification, timely first-hire and hire/cessation notices, and a monthly nominative declaration including new/leaving workers. Multi-branch employers separately list each establishment with a consolidated recap. The electronic preliminary registration must be completed with the physical supporting dossier under the implementing process; CNPS FAQ says confirm it within a month and lists professional/domestic employer and worker documents. This does not displace the statutory 8-day hire/notice deadlines.

The FAQ lists employer registration request, commercial register/status, current business-tax/taxpayer documentation, location plan, staff list and education opening approval where relevant. Domestic employers use identity/residence documents, location and staff list. Worker records include a request, hire notice and certified birth/identity document. Actual current screen-by-screen submission and later document changes were not verified; do not invent them.

Keep the nominative declaration receipt and payment evidence. Pay the actual CNPS account, not the DGI income-tax ledger by inference from a bank narration. Arts 15-19 set monthly timing, permitted payment evidence, specialised-centre procedures and exceptional authorised modes. Salary tax, CFC/FNE and CRTV deadlines are separately governed in payroll; annual income recap is not the monthly CNPS return.

## Penalties and interest

For CNPS, use the 2015 decree's separate surcharge rule in the table. Its 13 applies the fiscal late-declaration regime mutatis mutandis;12 provides a 7-day notice before default assessment for a missing declaration, and 14 governs correction/notice before recovery. Do not import DGI's 1.5% monthly interest as if it were the CNPS late-payment formula. A precise arrears bill requires due dates, principal by month, notices, payments, applicable remission and the official account; refuse to certify one from a bank statement alone.

DGI/PAYE enforcement is separate: LPF L106 self-assessed filing/payment penalty and collection interest; L95-L98 understatement interest and good/bad-faith/fraud uplifts. Load payroll for that table. CNPS remission requires a written supported request and decision, not an automatic waiver. Current individual circumstances and any subsequent statutory change must be checked before applying historical-period sanctions.

## Cross-border points

CGI 25 uses home/main stay, professional activity (unless accessory) or economic interests for fiscal domicile, subject to treaty. The old foreign-national “more than 183 days automatically resident/worldwide-taxed” shortcut is not established by 25. Count days and obtain residence/treaty evidence, but do not decide tax residence or CNPS coverage from the count alone. Foreign salary for work in Cameroon and treaty relief belong to payroll/cross-border review; nationality alone gives no contribution exemption.

Non-salary investment/business income and self-employed minimum tax are separate income-tax jobs. Preserve the distinction between salary IRPP progressive bands, investment schedular treatment and business/IGS regimes by routing to their current owner, rather than treating every inbound bank credit as salary or applying payroll CNPS to business turnover.

## Two worked examples that recompute

### Below the ceiling: general regime, actual low-risk classification

All-cash contributory salary 300,000/month; actual general family regime and Group A. Employee pension 12,600. Employer pension 12,600+family 21,000+risk 5,250=38,850. The old line `15.02.2025 ; CNPS COTISATION JANVIER ; DEBIT ; PENSION SALARIE ; -12 600 ; XAF` is a historical scenario only; classification requires proof it is that employee share.

```oa-check
name: Below cap, general regime and actual Group A
inputs:
  salary: 300000
  cap: 750000
steps:
  - capped: min(salary, cap)
  - employee: capped * 0.042
  - employer_pension: capped * 0.042
  - family: capped * 0.07
  - risk: salary * 0.0175
  - employer: employer_pension + family + risk
expected:
  employee: 12600
  family: 21000
  risk: 5250
  employer: 38850
```

### Above the ceiling: correct risk base versus the old capped error

Salary 1,200,000 with the same actual regime/class: employee pension 31,500. Employer 31,500+52,500+21,000=105,000. Capping risk incorrectly at 750,000 gives 13,125 rather than 21,000, understating cost by 7,875. The historical line `15.04.2025 ; CNPS PREVOYANCE SOCIALE ; DEBIT ; PENSION PLAFONNE ; -31 500 ; XAF` identifies only an assumed pension share, not full employer cost.

```oa-check
name: Above cap, uncapped accident branch prevents understatement
inputs:
  salary: 1200000
  cap: 750000
steps:
  - capped: min(salary, cap)
  - employee: capped * 0.042
  - pension: capped * 0.042
  - family: capped * 0.07
  - risk: salary * 0.0175
  - employer: pension + family + risk
  - wrong_risk: capped * 0.0175
  - understatement: risk - wrong_risk
expected:
  employee: 31500
  risk: 21000
  employer: 105000
  understatement: 7875
```

Retained boundary/regime regressions: at salary 750,000 and Group A/general, employee 31,500 and employer 97,125. Agriculture 400,000 and actualA gives pension 16,800+family 22,600+risk 7,000=46,400. These are derived using the above decree rates. At a confirmed all-cash 6,000,000 annual salary with actual employee pension 252,000, the payroll owner's gross-based professional deduction 1,800,000 and salary abatement 500,000 give net 3,448,000 and annual IRPP508,200 including CAC. Net taxable 5,000,000 gives 935,000;8,000,000 gives 2,090,000. These preserve the old salary cases and are derived from CGI 29/34/69/71, not separate salary rules owned here.

The old CFC/FNE line `15.05.2025 ; CREDIT FONCIER CFC + FNE ; DEBIT ; AVRIL 2025 ; -9 000 ; XAF` does not reconcile for a fully liable 300,000 salary: employer CFC4,500+FNE3,000=7,500; employee CFC3,000 makes 10,500. The unexplained difference is 1,500 either way, not a fictitious rounded employee share. Retain the 9000 bank amount as an unmatched item pending the return/payment breakdown. The old `15.03.2025 ; DGI IMPOTS IRPP SALAIRES ; DEBIT ; PRECOMPTE FEVRIER ; -45 000 ; XAF` is a PAYE-classification scenario, not proof 45,000 is the correct tax. The old 55,000 salary scenario remains a withholding-floor versus contribution-coverage distinction; its 2,310 pension calculation assumes an assessed base 55,000 and is not a certified contribution floor or wage-compliance result. The original dated Example 6 line is `28.02.2025 ; VIREMENT SALAIRE ; DEBIT ; PAIE FEVRIER ; -55 000 ; XAF`. It remains a historical assumed-base case, not proof of the current lawful wage or contribution floor.

## Ask the client first

1. Employee versus voluntary/independent status, CNPS coverage and registration evidence?
2. Gross salary, frequency/currency, components and actual contributory exclusions/base?
3. Family regime and CNPS-assigned risk class/activity, including mixed activities?
4. Employee/employer declarations and payslips, payment receipts, notices and arrears statement?
5. Foreign residence/detachment/treaty facts, special public scheme or disputed coverage?

**R-CM-SOC-1:** no gross/base evidence means no exact calculation. **R-CM-SOC-2:** unknown risk class means no precise employer total; show labelled alternatives only. **R-CM-SOC-3:** voluntary eligibility/agreed base requires actual CNPS confirmation. **R-CM-SOC-4:** no official arrears/payment/notice record means no certified penalty bill. **R-CM-SOC-5:** refer foreign residence and treaty decisions with full facts. No unsupported FX, automatic salaried classification, omitted family branch, capped risk, or assumed reduced regime. Never confuse an IRPP withholding exemption with a CNPS exemption. All outputs remain provisional pending qualified review; do not file/sign or present them as professional approval.

## Sources

| Official source | URL | Read on / actual scope |
|---|---|---|
| DGI CGI Edition 2026, annexed decrees | https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf | 2026-11-15. Read for Decree 2016/072 all 12 articles and full risk-class AnnexA/B/C (printed 519-522), Decree 2015/2517 arts 1-27 (registration, declaration, payment, surcharge, base exclusions), CGI 25/29-34/69/71/81-84 for the routed salary cases, LPF L5/L95-L106, and annex CFC laws for the remittance reconciliation. Not the entire collection or every implementing exclusion text. |
| CNPS employer services/FAQs | https://www.cnps.cm/index.php/fr/component/sppagebuilder/?id=85&view=page | 2026-11-15. Read for complete operative coverage, registration, document, cessation, voluntary-eligibility and 2016-rate-change FAQs. No actual account login or filing screens tested. |
| CNPS current voluntary-insurance agency page | https://www.cnps.cm/fr/?id=90&option=com_sppagebuilder&view=page | 2026-11-15. Read for full operative introduction, registration, declared-income range/contribution amounts, declaration/payment and FAQ; benefit descriptions read but no pension-entitlement conclusion adopted. Monthly/flexible-frequency wording requires actual payment-process confirmation. |

Not yet confirmed: current CNPS implementing list/limits of excluded professional costs/end-of-career indemnities, contribution-floor treatment, partial-month/unpaid-leave methods, any individual CNPS voluntary-base approval or payment arrangement beyond the agency range (old 36,270 is not current proof), individual public-scheme/foreign-detachment coverage, actual portal/document changes and the unidentified 9000 CFC/FNE payment. The old 55,000 scenario's 2,310 pension is arithmetic on its assumed base only; do not use it as a current compliant floor. The old>183-day automatic residence shortcut,15.20% CNPS-only headline, unknown-risk minimum/middle defaults and DGI1.5%-interest-as-CNPS rule are replaced by the scoped provisions/referrals above. Earlier standalone CNPS rates/statistics/voluntary/sanctions downloads failed; no failed page is marked read. A different current voluntary page was subsequently recovered and read through the web tool; its rate/range and payment-frequency guidance are attributed above. The official 2026 CGI annexed decree and actually opened CNPS FAQ support the usable scope.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `cameroon-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/cameroon-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
