# Nigeria pack: source notes (wyktor33, issue #478)

Working notes for the NG pack (SC, TP, XB missing). Started 2026-10-29.

## Key context
- Nigeria Tax Act 2025 (Act No. 7 of 2025, Official Gazette No. 117 Vol. 112, 26 June 2025, pp. A387–A596) is
  the principal substantive tax law from 1 January 2026, replacing the federal tax statutes (CITA, PITA, etc.).
  The Nigeria Tax Administration Act 2025 (Act No. 5) covers procedure, enforcement and penalties. FIRS became the
  Nigeria Revenue Service (NRS). All 13 existing NG skills carry tax_year 2025 and cite the repealed Acts.

## Nigeria Tax Act 2025 (NASS gazette PDF)
URL: https://nass.gov.ng/documents/download/11249  Read on: 2026-10-29
- s190: artificial or fictitious transactions may be disregarded/adjusted; a transaction between connected persons
  is deemed artificial if not at arm's length (s190(3)(b)); objections/appeals under NTAA Chapter Four.
- s191(1): a company in an arrangement with a related party must (a) ensure arm's length terms and (b) report the
  arrangement in the form and manner the relevant tax authority prescribes. (2) adjustments to arm's length terms
  "as provided under the Transfer Pricing Regulations". (3) authority may make rules. (4) "arrangement" defined
  widely; "arm's length terms and conditions" = terms obtainable between unrelated parties in comparable
  circumstances.
- "connected persons" defined at text line ~4983 (s. on interpretation); "related parties" has the same meaning
  as connected persons. NOT YET READ IN FULL.
- Sections of interest for XB (not yet read): s17 non-resident person, s18 shipping/air, s19 dividends to
  non-residents, s119–121 double taxation relief and agreements; s12 resident individual.

## Nigeria Tax Administration Act 2025 (NASS gazette PDF; NRS copy is a scan)
URL: https://nass.gov.ng/documents/download/11250  Read on: 2026-10-29
- s46: artificial transactions; transactions between persons connected under NTA s193 deemed artificial if not
  at arm's length; right of appeal; authority may issue guidelines/regulations on connected persons.
- s147 (interpretation): "Transaction at Arm's Length" = a related party transaction on normal open market terms.

## Transfer Pricing Regulations — NOT REACHABLE FROM AN OFFICIAL SOURCE
- NTA s191(2) relies on "the Transfer Pricing Regulations". The known text is the Income Tax (Transfer Pricing)
  Regulations 2018, hosted at https://old.firs.gov.ng/wp-content/uploads/2021/06/Income-Tax-Transfer-Pricing-Regulations-2018-2.pdf
- 2026-10-29: old.firs.gov.ng refuses connections (curl timeout; built-in browser navigation denied). nrs.gov.ng
  has no TP regulations page found. Internet Archive: latest content capture 2025-04-18 (revisit 2025-09-11),
  none in 2026, so rule 3 (current-year archive copy) is not met.
- Secondary sources (not citable) mention documentation within 21 days of request and NGN 10m + 10k/day penalties;
  NOT USED.

## NTA 2025: cross-border provisions (same gazette PDF, read 2026-10-29)
- s12: income of a resident individual deemed to accrue in Nigeria and taxable wherever arising, remitted or not.
- s13(1): employment income derived from Nigeria where (a) employee resident, or (b) duties wholly/partly performed
  in Nigeria and the remuneration accruing while in Nigeria is not duly liable to tax in the employee's country of
  residence. (2) Government employment deemed Nigerian where foreign country exempts under agreement/privilege.
- s17(1): non-resident's income accruing in or derived from Nigeria chargeable. (2) non-resident gains taxable if
  relating to a Nigerian trade, an asset located (or deemed located) in Nigeria.
  (3) profits taxable where: (a) PE or significant economic presence (SEP), to the extent attributable;
  (b) payment by a Nigerian resident/PE for services furnished from outside Nigeria to a Nigerian resident/PE
  (except employee under contract of employment; teaching by/at educational institution; foreign PE of a Nigerian
  resident bearing the expense); (c) payment by Nigerian resident/PE for insurance premiums/risks insured from
  Nigeria (text of (c) partly cut across page; reads "...in respect of insurance premiums or risks insured from the
  territory of Nigeria").
  (4) deduction at source on (3)(b),(c) payments is the final tax unless attributable to a PE or SEP.
  (5) PE profit rules: same credit rating as head company; equity/loan capital as reasonably expected under s191;
  force of attraction for same/similar sales and services by the non-resident or connected persons; only costs
  incurred for the PE's profits; NO deduction for royalties, fees or similar payments to the non-resident or
  connected persons for patents/other rights, except reimbursement of actual expenses.
  (6)-(7) if profits cannot be ascertained, or are lower than, the non-resident's profit margin x Nigerian income,
  use profit margin (EBIT/revenue per s17(9)(e)) x total income from Nigeria.
  (8) tax payable not less than tax withheld at source; where income not subject to deduction at source, not less
  than 4% of total income generated from Nigeria.
  (9)(a) PE definition: place of business; dependent agent; stock of goods for delivery; projects (surveys,
  construction, installation, supervision etc.) irrespective of split; services through employees/agents/
  subcontractors. (b) SEP: digital/electronic activities to Nigeria with attributable profit, subject to Minister's
  regulations. (c) employing Nigerian residents alone is not a PE/SEP if duties not primarily for Nigerian customers.
  (d) "place" list. (e) profit margin = EBIT / income per published audited accounts (or comparable company).
- s18: non-resident shipping/air transport: profits from carriage loaded in Nigeria; global ratios; minimum 2% of
  gross revenue from Nigerian carriage, computed and paid monthly (s18(6)).
- s19(1): no further tax on dividends received by a non-resident from a Nigerian company beyond tax deducted at
  source under NTAA; (2) no repayment right.
- s56: companies: small company 0%; any other company 30% from commencement; proviso: reduced to 25% from a date set
  by Presidential order on NEC advice (order NOT CHECKED).
- s57: 15% minimum effective tax rate for MNE constituent entities (group turnover >= EUR 750m) and companies with
  turnover >= NGN 50 billion.
- s119: unilateral relief for residents: credit for foreign tax, lower of Nigerian tax attributable (foreign income
  / total income x Nigerian tax) and foreign tax paid.
- s120: DTAs effective on ratification/domestication; extant DTAs deemed under s120, apply from 1 January after
  entry into force; anti-treaty-shopping; benefit only to treaty-partner residents who are beneficial owners;
  (8) no relief for GMT top-up of a PE.
- s121: credit method under a DTA: lower of Nigerian tax attributable and treaty-partner tax; no credit for a
  person not resident in Nigeria in the year; no deduction for foreign tax; gross-up on remittance basis; claim
  within two years after the end of the year of assessment.
- Interpretation: "Nigerian company" = formed/registered/incorporated in Nigeria, or central or effective place of
  management or control in Nigeria; "resident company" = Nigerian company. "resident individual" = in the year
  (a) domiciled in Nigeria; (b) permanent place available for domestic use; (c) habitual abode; (d) substantial
  economic and immediate family ties; (e) 183+ days in a 12-month period incl. annual leave/temporary absence, or
  (f) Nigerian diplomat abroad. "non-resident individual" = none of those (all of (a)-(f) negated, joined by "and").
  "small company" = gross turnover <= NGN 100 million and total fixed assets <= NGN 250 million.

## NTAA 2025 s11 (returns for companies)
- s11(2): non-resident company taxable in Nigeria files audited group accounts and Nigerian operations' statements
  attested by a Nigerian accountant, tax computations, statement of Nigerian profits, self-assessment forms,
  evidence of payment, ETR computation. (3) not required where only income with final deduction at source.
  (5) filing: not more than six months after accounting year end (company > 18 months in business); new company
  within 18 months of incorporation or 6 months after first period end, whichever earlier; cessation within 6 months.

## NTA 2025: individuals (same gazette, read 2026-10-29)
- s30: chargeable income = total income less eligible deductions: (i) National Housing Fund contributions;
  (ii) National Health Insurance Scheme contributions; (iii) Pension Reform Act contributions; (iv) interest on
  loans for an owner-occupied house; (v) life assurance/deferred annuity premiums (spouse included); (vi) rent relief
  20% of annual rent paid, max NGN 500 000. s31: deductions must be claimed in writing.
- s58 + Fourth Schedule: individuals' rates (individuals on the Minimum Wage excluded): first 800 000 at 0%;
  next 2 200 000 at 15%; next 9 000 000 at 18%; next 13 000 000 at 21%; next 25 000 000 at 23%; above 50 000 000 at 25%.
- s59: development levy 4% of assessable profits of companies (not small or non-resident companies).

## PenCom, Frequently Asked Questions on the Contributory Pension Scheme (2020 edition, PenCom PDF)
URL: https://pencom.gov.ng/wp-content/uploads/2020/06/FREQUENTLY-ASK-QUESTION-2020-ENGLISH-MAIN-VISUAL.pdf
Read on: 2026-10-29 (Pension Reform Act 2014 full text not found on an official URL; pencom.gov.ng Act PDF 404)
- Minimum contribution 18% of monthly emoluments: employer 10%, employee 8%; employer may bear all (>= 18%).
- Additional voluntary contributions allowed if total contributions and other deductions <= one-third of monthly
  emoluments.
- Monthly emoluments as defined in the contract but not less than basic salary + housing + transport allowances;
  where pay is not split, use the salary payable (casual/contract staff covered).
- Mandatory coverage: public service (Federation, FCT, States, LGs) and private organisations with 3 or more
  employees; fewer than 3 and self-employed may join voluntarily (Micro Pension Plan).
- Exempt: judicial officers, armed forces, intelligence and secret services, pre-2004 retirees, those with 3 years
  or less to retire at 30 June 2004. Foreigners working in Nigeria are not mandated.
- Employers with 3+ employees must obtain an employer code from PenCom.
- Employer deducts and remits to the RSA not later than 7 working days from the date salaries are paid.
- Failure to remit: pay the contribution plus a penalty of at least 2% of total unpaid contributions, into RSAs.
- Pension contributions are not taxed (PRA 2014); income on voluntary contributions taxed if withdrawn within 5 years.
- Group Life Insurance at least 3 times Annual Total Emolument (basic + all allowances for a year).

## National Housing Fund Act Cap. N45 (FMBN-hosted PDF)
URL: https://fmbn.gov.ng/backend/storage/uploads/37UNgpzsyASabzhQCnHuyzFtIpnsfmW2ODvAmQSG.pdf (linked from
https://fmbn.gov.ng/products/nhf-scheme/legal-framework, which notes the Act is being amended)
Read on: 2026-10-29
- s4(a): Nigerian worker earning NGN 3 000+ a year contributes 2.5% of basic monthly salary; (b) 4% interest payable.
- s9(1): employer deducts 2.5% of the monthly salary of such an employee; (2) remits to FMBN within one month of
  deduction. s10: self-employed contribute the same and remit within one month.
- s20: employer failing to deduct, or deducting and not remitting, commits an offence: body corporate fine
  NGN 50 000; authorised staff NGN 20 000 or five years or both; self-employed NGN 5 000 or one year.

## NSITF (Employees' Compensation Scheme), nsitf.gov.ng
URLs: https://nsitf.gov.ng/ and https://nsitf.gov.ng/services/  Read on: 2026-10-29
- Monthly contribution: 1% of total monthly payroll, employer-funded, by every registered employer, under the
  Employees' Compensation Act 2010; paid through ecsonline.nsitf.gov.ng. Penalty rates NOT read (FAQ collapsed).

## Industrial Training Fund, Revenue department page
URL: https://itf.gov.ng/departments/revenue.html  Read on: 2026-10-29
- Statutory training contribution: 1% of annual payroll from employers; 50% reimbursable for training under the Act.
- Liability threshold (5+ employees or turnover >= NGN 50m) NOT read from an official page (brochure download
  failed: 406 / forced download). NOT CONFIRMED.
