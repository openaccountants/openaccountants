---
name: ro-tax-overview
description: "Use this skill to identify the Romanian tax regime for 2026 and load its detailed skill: calendar or elected modified tax year, resident/nonresident scope, default individual income tax at 10% with category exceptions, CAS 25%, CASS 10%, employer CAM 2.25%, ordinary profit tax 16%, conditional micro-enterprise tax 1% with EUR 100,000 ceiling, 16% dividend tax and protected 2025 interim distributions, VAT 21%/11% with transitional exceptions, annual return deadlines, filing fines and transfer-pricing documentation timing. Includes two recomputing base/rate cases. This is an orientation skill, not complete filing instructions or a claim that every linked sibling is current."
version: 0.4
type: situation-rules
jurisdiction: RO
tax_year: 2026
last_updated: 2026-11-15
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Romania: tax overview and routing for 2026

Start with the taxpayer, income category, tax period and the base. A headline rate does not determine liability without those facts. This skill maps the Romanian rules to their detailed skills and shows why the same gross amount can produce different tax bases. It is general reference, not accountant approval or complete return preparation.

## Who this applies to

Individuals and businesses identifying Romanian tax obligations for the 2026 tax year. The authority is ANAF, Agenția Națională de Administrare Fiscală. The currency is the Romanian leu (RON); membership of the EU does not make the euro Romania's tax-payment currency. The [official EU country profile](https://european-union.europa.eu/principles-countries-history/eu-countries/romania_en) confirms membership and currency; Fiscal Code art. 9 requires tax payment and declaration figures in national currency, with the applicable statutory conversion rule.

The main laws are Legea 227/2015, Codul fiscal (CF), and Legea 207/2015, Codul de procedură fiscală (CPF). ANAF's electronic consolidations are not official republications. The Fiscal Code page now identifies Law 204/2026; the Procedure Code page identifies Law 170/2026. An updated header does not prove every intervening amendment or future effective date is correctly reflected. Read the operative rule and commencement for the actual transaction.

Resident individuals generally have worldwide income within CF art. 59. Residence start/exit dates, domicile, treaty proof and special transition rules matter; do not equate citizenship with residence. Nonresident independent activity through a Romanian permanent establishment uses the net income attributable to that establishment; other Romanian-source categories have their own rules. Load ro-cross-border before deciding residence, source, treaty relief or foreign tax credits.

Individuals normally use the calendar year, with a shorter period on death (CF art. 65). Companies normally use the calendar year but may elect a tax year corresponding to an eligible different financial year; start, cessation and liquidation periods need their own treatment (CF art. 16). The source rules are linked in the table below.

## Rates, bands and thresholds

Each percentage applies to its statutory base, not automatically to the amount appearing on an invoice or bank statement.

| Item | 2026 position and conditions | Act/article and official source |
|---|---|---|
| Individual tax period | Calendar year; death can shorten it | CF art. 65, https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Corporate tax period | Calendar year unless an eligible different financial year is elected as tax year; start/cessation/liquidation exceptions apply | CF art. 16, https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Default individual income tax | 10% of the relevant taxable income; express category-specific rates and exemptions override it | CF art. 64(1)-(2), https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Employee pension contribution, CAS | 25% of the statutory insured salary base; international coordination/exclusions apply. Additional employer contributions for special working conditions are separate | CF arts. 138(a)-(c) and 139, https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Health contribution, CASS | 10% where the law imposes it, on the income category's base with its exemptions and limits; not an automatic contribution on every receipt | CF arts. 156-157 and the relevant category provisions, https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Employer work-insurance contribution, CAM | 2.25% of the applicable employer base; not a deduction from the employee's pay | CF arts. 220^3(1) and 220^4, https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Ordinary profit tax | 16% of taxable profit after fiscal adjustments; minimum, sector, group and special regimes require the corporate-tax skill | CF arts. 17 and 19, https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Micro-enterprise regime | 1% of the statutory revenue base. The prior-year ceiling is the RON equivalent of EUR 100,000, including linked-enterprise rules; private capital, employee/equivalent condition, shareholder restriction, timely accounts, excluded-sector tests, election and exit rules also apply. The ceiling alone does not establish eligibility | CF arts. 47-53, https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Dividends to a Romanian company | 16% of gross dividends for distributions from 1 January 2026, or the first day of an applicable modified tax year beginning in 2026; the cumulative corporate-recipient exemption can apply | CF art. 43; Law 141/2025 art. VII(1)(a), https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf |
| Corporate dividend exemption | At least 10% holding for a full year through payment, plus the statutory payer/recipient legal-form and compulsory-tax conditions; not every corporate holding qualifies | CF art. 43(4), https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Dividends to resident individuals | 16% final income tax for distributions from 1 January 2026; separate CASS analysis may remain | CF art. 97(7); Law 141/2025 art. VII(1)(c), https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf |
| Protected prior interim dividends | Distributions based on 2025 interim accounts keep the 10% dividend rate without recalculation after annual regularisation; do not decide the rate from payment date alone | Law 141/2025 art. VII(2), https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf |
| VAT headline rates | 21% standard; 11% only for specified reduced-rate supplies, from 1 August 2025. Exemption, reverse charge, tax point and special transitions must be checked separately | CF art. 291; Law 141/2025 art. II point 42 and VII(1), https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf |
| Qualified housing VAT transition | A 9% transition remained for specified housing deliveries through 31 July 2026, subject to the complete property, buyer, prior-contract and advance-payment conditions; route the actual transaction rather than extending it to every home | Law 141/2025 art. III(1)-(4), https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf |
| Annual individual return for 2026 income | 25 May 2027, derived from the statutory following-year date, where a return is required. Final withholding/salary and other filing exceptions apply; contributions can create a separate filing duty | CF arts. 122-123, https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Ordinary annual profit-tax return for calendar 2026 | 25 June 2027, derived; elected modified year: the 25th of the sixth month after year end. Liquidation/dissolution exceptions have separate dates | CF arts. 42(1)-(2) and 41(16)-(17), https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm |
| Transfer-pricing annual file | Large taxpayers prepare the file for qualifying individual transactions with each affiliate by the annual profit-tax return deadline; annual duty covers transactions from 2026. Electronic SPV submission is due within 30 working days after that deadline | Order 828/2026 arts. 2(1)-(6) and 15(1), https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_828_2026.pdf |
| Transfer-pricing procedure timing | New administration procedures apply after 1 January 2027; procedures started earlier retain prior law. Small/medium taxpayers generally prepare/present on request during control, with threshold, risk-request and other statutory qualifications | Order 828/2026 arts. 2(7)-(11), 4, 6 and 15(2)-(3), https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_828_2026.pdf |

## The base

Choose the detailed skill before computing or giving filing instructions:

| Job | Load | Boundary |
|---|---|---|
| Self-employed PFA, II, IF or liberal-profession income | ro-income-tax and ro-cas-cass | Income tax, pension and health contributions have different bases and deductions |
| Employee income, rent or investments | ro-employee-income-tax; ro-payroll-social for employer payroll | The default income-tax percentage does not replace dividend/other special rates or contribution rules |
| Ordinary company profit, micro regime and corporate distributions | ro-corporate-income-tax | Eligibility, fiscal adjustments, minimum taxes, losses, interest, credits, instalments and distributions need detailed treatment |
| VAT, EU transactions and returns | ro-vat-return and romania-einvoice | The passing VAT sibling has obsolete e-TVA notice instructions; do not use those instructions as current law (see below) |
| Social contributions and employer payroll | ro-cas-cass or ro-payroll-social, according to taxpayer | A salary base and a self-employed base are not interchangeable |
| Transfer pricing | ro-transfer-pricing | The skill exists despite the older corporate-tax sibling's contrary router sentence; identify transaction year and procedure start separately |
| Residence, source, withholding and treaty relief | ro-cross-border | Exact residence/treaty facts and certificates matter; no universal treaty rate |
| Formation and reference software | ro-company-formation and references | Entity choice, registration and technical tools do not establish the tax treatment of a transaction |

Romania's EU VAT context is retained; this short map does not reproduce Directive 2006/112/EC or certify that every product list in the linked VAT skill reflects all later amendments. The official EUR-Lex text could not be read during this pass and no Directive article-specific instruction is based on that failed response.

**Known sibling boundary.** OUG 13/2026 art. IV point 1 expressly repeals OUG 70/2024 arts. 5, 8 and 16; its art. VII delays other named amendments, not that repeal. The old e-TVA statutory-notice thresholds/procedure in ro-vat-return must not be imported as current instructions. Use the corrected interaction in romania-einvoice and the [actual ordinance](https://static.anaf.ro/static/10/Anaf/legislatie/OUG_13_2026.pdf). The pre-filled-return system and transaction checks are not thereby declared abolished. This rewrite preserves the seven already-passing siblings byte for byte and records that defect separately, rather than conferring blanket legal approval on them.

For an ordinary employee computation, deduct legally due employee contributions and applicable deductions before applying income tax (CF art. 78). CAM belongs to employer cost. For an ordinary company, fiscal profit starts with accounting income less expenses, subtracts non-taxable income/deductions and adds non-deductible expenses, subject to other fiscal adjustments and losses (CF art. 19). Neither base is simply every bank receipt.

## Deadlines and filing

Identify the applicable return, period, filer and payment obligation first. The annual individual deadline does not require every salary-only or final-withholding recipient to submit that return for income tax; CF art. 122(6)-(7) separates exceptions from contribution-reporting duties. The statutory date for 2026 income is sourced above; do not invent fields in an unpublished 2026-income final form.

For the annual corporate return, CF art. 42(1)-(2) governs ordinary calendar/elected modified years. A company dissolved with liquidation follows art. 41(16), linked to the closing financial statements; dissolution without liquidation follows art. 41(17), linked to closure of the taxable period. The annual return deadline does not eliminate instalments or other periodic obligations. Load the corporate-tax skill before assembling D101 or calculating a final balance.

For transfer pricing, distinguish annual preparation, electronic SPV filing and a later presentation request. Order 828/2026 art. 2 contains these different duties; its art. 15 preserves the transaction-year/procedure-start distinction. Small/medium on-request rules and exceptions are in ro-transfer-pricing; a group of affiliates is not automatically one combined threshold amount under the new annual-file test.

This overview gives no complete current login, form-box or payment-account workflow. Load the applicable detailed skill and the actual official form for the reporting period. Historical form instructions and a technical schema are not proof that a return was accepted or tax paid.

## Penalties and interest

| Breach | Amount/rate and conditions | Official source |
|---|---|---|
| Late individual income return or Declarația unică | RON 50 to 500, specific individual offence; not a general registration fine | CPF art. 336(3), https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Covered registration/general declaration breach | RON 1,000 to 5,000 for medium/large legal entities; RON 500 to 1,000 for other legal entities and individuals, subject to the special individual-income-return rule and applicable legal qualifications | CPF art. 336(1)(a)-(b), (2)(d), (3), https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Ordinary late-payment interest | 0.02% per day, normally day after due through extinguishment inclusive; annual-tax/correction rules can qualify the period | CPF arts. 174-175, https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Ordinary late-payment penalty | 0.01% per day plus interest; it does not apply to principal subject to the non-declaration penalty | CPF art. 176, https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |
| Non-declaration penalty | 0.08% per day for undeclared/incorrectly declared principal established by assessment, with reductions, minimum/cap and statutory exceptions; interest remains, ordinary late-payment penalty is not added again | CPF art. 181, https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm |

Local-budget filing breaches follow the separate rules identified in CPF art. 336(5). Do not stack every headline fine and daily rate without identifying the actual obligation, assessment, period and exception. The detailed skills retain their own relevant penalty analysis.

## Cross-border points

Use ro-cross-border for residence, departure, Romanian source, permanent establishments, treaties, withholding and credits. A resident's general worldwide scope does not erase treaty relief; a nonresident's Romanian tax depends on the category and applicable source rule. Dividend rates above describe their specified resident-recipient cases, not every outbound payment. Social-security coverage also needs the relevant EU or international coordination; a Romanian income-tax result alone does not establish Romanian CAS/CASS/CAM liability.

## Two worked examples that recompute

### Ordinary monthly salary: separate employee deductions from employer cost

Assume RON 10,000 is an ordinary fully taxable/insured salary base for a full month. Romanian social insurance applies; no special working-condition employer contributions, exemption, minimum-wage relief, benefits, personal/additional deduction or other deduction applies on the supplied facts. Employee CAS is 10,000 × 25% = RON 2,500; CASS is 10,000 × 10% = RON 1,000. Income-tax base is RON 6,500 and income tax is RON 650. Net pay is RON 5,850. Employer CAM is RON 225 and total employer cost is RON 10,225, all derived under CF arts. 78, 138, 156 and 220^3. This is not the self-employed contribution computation.

```oa-check
name: Ordinary salary separates employee net and employer cost
inputs:
  insured_taxable_gross: 10000
  cas_rate: 0.25
  cass_rate: 0.10
  income_tax_rate: 0.10
  cam_rate: 0.0225
  other_deductions: 0
steps:
  - cas: insured_taxable_gross * cas_rate
  - cass: insured_taxable_gross * cass_rate
  - income_tax_base: insured_taxable_gross - cas - cass - other_deductions
  - income_tax: income_tax_base * income_tax_rate
  - net_pay: insured_taxable_gross - cas - cass - income_tax
  - employer_cam: insured_taxable_gross * cam_rate
  - employer_cost: insured_taxable_gross + employer_cam
expected:
  cas: 2500
  cass: 1000
  income_tax_base: 6500
  income_tax: 650
  net_pay: 5850
  employer_cam: 225
  employer_cost: 10225
```

### Ordinary corporate profit: account for fiscal adjustments

Assume an ordinary profit-tax company, outside micro, minimum/sector/group rules, with no losses, credits or other adjustments. Recorded revenue is RON 500,000 and expenses RON 350,000. The established fiscal classifications identify RON 10,000 non-taxable income and RON 20,000 non-deductible expenses already included in those totals. Accounting profit is RON 150,000; taxable profit is 150,000 − 10,000 + 20,000 = RON 160,000. At 16%, tax is RON 25,600, derived under CF arts. 17 and 19. The example assumes those classifications; it does not decide whether a particular real expense is deductible.

```oa-check
name: Ordinary profit tax reconciles accounting and fiscal profit
inputs:
  revenue: 500000
  expenses: 350000
  non_taxable_income: 10000
  non_deductible_expenses: 20000
  profit_tax_rate: 0.16
steps:
  - accounting_profit: revenue - expenses
  - taxable_profit: accounting_profit - non_taxable_income + non_deductible_expenses
  - profit_tax: taxable_profit * profit_tax_rate
expected:
  accounting_profit: 150000
  taxable_profit: 160000
  profit_tax: 25600
```

## Ask the client first

Establish legal form, residence/domicile and relevant dates, income source/category, fiscal/accounting year, gross/net/base records, exemptions/deductions, insurance coverage, employee facts, ownership/linked enterprises, distribution approval/payment dates and any prior interim accounts. For VAT, obtain supply classification, tax point, registration, place of supply and transitional facts. For transfer pricing, identify each transaction, affiliate, taxpayer class, transaction year, applicable currency conversion and procedure start. For a penalty, obtain the original deadline, filings, payments, assessment and any regularisation or relief facts.

Stop if those inputs or the actual operative source are missing. Do not give a filing position from a rate card alone. Known stale sibling instructions, inaccessible sources and future forms remain outside usable instructions until resolved.

## Sources

All reads below actually occurred on 2026-11-15. A consolidation is not an official republication; legislation and effective dates control.

| Source | Official URL | Read for / actual read date |
|---|---|---|
| Fiscal Code, Legea 227/2015, ANAF consolidation headed Law 204/2026 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-11-15. Read for arts. 9, 16, 17, 19, 41(16)-(17), 42-43, 47-53, 59, 64-65, 78(1)-(2), 97(7), 122-123, 138, 156 and 220^3, the opening base provisions in 139, 157 and 220^4, and 291 with neighboring transitions. |
| Fiscal Procedure Code, Legea 207/2015, ANAF consolidation headed Law 170/2026 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm | 2026-11-15. Read for arts. 174-176, 181 and 336 relevant offence, scope, fine and exception provisions. |
| Law 141/2025 | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf | 2026-11-15. Read for dividend/VAT amendments and art. III housing transition, VII(1)(a),(c) and (2), with relevant commencement conditions. |
| ANAF Order 828/2026 | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_828_2026.pdf | 2026-11-15. Read all operative arts. 1-16, particularly 2, 4, 6 and 15; not a claim to have read every annex detail. |
| OUG 13/2026 | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_13_2026.pdf | 2026-11-15. Read for art. IV point 1 e-TVA repeal, neighboring clauses and VII timing; current e-TVA notice instructions in the VAT sibling remain a deferred defect. |
| European Union, Romania country profile | https://european-union.europa.eu/principles-countries-history/eu-countries/romania_en | 2026-11-15. Read for existing membership/currency topics only. |
| ANAF October 2026 legislative bulletin | https://static.anaf.ro/static/10/Brasov/Brasov/MO_OCT_2026.pdf | 2026-11-15. Read the relevant entries on physical pages 3-4 to identify later amendments, including the reduced-rate list's consolidation gap; not a substitute for the operative amending act's detailed conditions. |

Not yet confirmed: a complete current reduced-rate product list from the ANAF consolidation alone (a later amendment is absent from that captured list); eventual final forms/fields for 2026 income filed in 2027 and authenticated submission/payment flows; article-specific EU Directive instructions after the official EUR-Lex page returned a robot-verification screen; the former overview's blanket historical 19%/9%/5% VAT replacement shorthand, which must not be used as a current rate rule; any case-specific relief, treaty, deduction, micro eligibility, special-regime liability or penalty without its required inputs. Seven structurally passing siblings are preserved rather than freshly approved; their separately recorded VAT notice and corporate-router defects remain explicit. Other detailed open points stay with the relevant skills.
