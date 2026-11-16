---
name: ng-payroll
description: "Run Nigerian employee payroll for 2026 from gross cash and benefits through approved contribution inputs, current personal income tax, net cash, employer cost, payslip and remittance reconciliation. Preserves the named 2025 sample separately, corrects CRA and non-cash treatment, and flags scheme, jurisdiction, termination and unconfirmed portal or levy deadlines."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ng-payroll"
  jurisdiction: "NG"
  tax_year: "2026"
  last_updated: "2026-11-16"
---

# Nigeria payroll computation v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For ordinary Nigerian employee payroll paid in2026. This file owns the sequence, payslip, net cash and employer-cost reconciliation. [ng-personal-income-tax](ng-personal-income-tax.md) owns the personal rate bands, deductions and residence method; [ng-pension-nhf-social-contributions](ng-pension-nhf-social-contributions.md) owns the contribution assessment. Load their limits before using any result. The nonexistent old links ng-paye and ng-statutory-deductions are replaced by these actual files. [ng-wht](ng-wht.md) handles a director or contractor payment that is not employment.

The new income-tax method applies to current employment earnings, including paid bonuses. It has no CRA deduction or old personal minimum-tax floor. Do not use the historical sample as a2026 payroll. Employer contributions are extra employer cost; they are not deductions from employee cash. Non-cash taxable benefits increase taxable earnings but cannot be paid again as net cash. [NTA sections 13,14,26,28,30 and58](https://nass.gov.ng/documents/download/11249).

| Rate or deadline control | Verified boundary or deadline | Source |
| --- | --- | --- |
| PAYE remittance | Within10 days after month-end, to the employee's correct authority | [JRB2026 Guidelines paragraphs 5/6/12](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf) |
| Employer annual return | By31 January for the preceding year's employees; employee annual filing remains separate | [NTAA section 14](https://nass.gov.ng/documents/download/11250) |
| Pension remittance | Employee plus employer amounts within 7 WORKING days of salary payment | [PRA section 11(3)](https://ngfrepository.org.ng:8443/bitstream/123456789/968/1/PENSION%20REFORM%20ACT%202014%20-%20GAZETTED%20COPY.pdf) |
| Pension late remittance | In addition to arrears, Commission penalty not less than2% of unpaid contribution per month or part | [PRA section 11(6)/(7)](https://ngfrepository.org.ng:8443/bitstream/123456789/968/1/PENSION%20REFORM%20ACT%202014%20-%20GAZETTED%20COPY.pdf) |
| NHF remittance | Within1 month of deduction, for liable contributors | [NHF Act sections 9/10](https://fmbn.gov.ng/backend/storage/uploads/37UNgpzsyASabzhQCnHuyzFtIpnsfmW2ODvAmQSG.pdf) |
| ECS employer funding | NSITF currently describes1% of monthly payroll as employer-funded. The Act's initial1% provision covered its first2 years and later risk assessments are authorised; check the actual employer assessment. | [NSITF services](https://nsitf.gov.ng/services/); [ECA sections 33 to38](https://nsitf.gov.ng/api/uploads/documents/cd29f838-1f78-450d-8650-9d1a6ada54aa.pdf) |

## Ask the client first

1. Pay month/date, employee residence and allocation history, Tax ID, employer registration/code, prior payroll and year-to-date earnings/PAYE, other employments and start/leave dates.
2. Contract cash split, bonus/commission/overtime, arrears, non-cash benefits and employee contributions, asset acquisition/rental values, accommodation and occupied period.
3. Actual pension scheme coverage and contractual pensionable emoluments, employer/employee rates, RSA/PFA/PFC, NHF contributor status/private-sector election and monthly income, approved health scheme and actual eligible remittances.
4. Claimed rent and other personal deductions with receipts/period/landlord information; loans, union/subscription or other authorised voluntary deductions kept separately.
5. Employer ECS assessment, ITF applicability and assessment, group life cover and scheme-specific health cost; each body's actual payment instruction/calendar.

## The method, step by step

### Establish schemes and employee records

Use the contribution owner's assessment, not a default for everyone. PRA section 2(2) expressly applies the private-sector scheme to organisations with15 or more employees; its definition of employer and PenCom guidance use other counts, so an employer below that express threshold requires the applicable current guidance, not a universal3-person conclusion here. Section4 prescribes minimum employee8% and employer10% of contractual monthly emoluments, with the basic/housing/transport floor in section 120. An employer electing to fund everything must contribute at least20%; simply adding8% and10% is not that election. Higher agreed rates and voluntary contributions need scheme/tax treatment checked. These rules are implementation context; the contribution home owns the rate decision. [PRA sections 2,4,11 and120](https://ngfrepository.org.ng:8443/bitstream/123456789/968/1/PENSION%20REFORM%20ACT%202014%20-%20GAZETTED%20COPY.pdf).

The Act also requires group life cover of at least3 times annual total emoluments for covered employees; record premium and cover as employer cost rather than salary deduction. Missing RSA is not permission to invent one: section 11(5) provides a nominal-account route subject to Commission guidelines after6 months. Obtain actual identifiers and remittance evidence. Foreign staff and exempt schemes need their own coverage determination. [PRA sections 4(5),5 and11](https://ngfrepository.org.ng:8443/bitstream/123456789/968/1/PENSION%20REFORM%20ACT%202014%20-%20GAZETTED%20COPY.pdf).

Business Facilitation Act 2022 Schedule paragraphs 44 to 46, effective 8 February 2023, replaced NHF section 4: public-sector employees earning the national minimum wage or above SHALL contribute 2.5% of MONTHLY INCOME; private-sector employees at that threshold MAY contribute 2.5% of monthly income; qualifying self-employed persons SHALL contribute 2.5% of monthly income. Paragraph 46 also replaces section 9's old basic-salary threshold with minimum wage. Record actual private-sector participation/election and income base; do not compel an opt-out employee or calculate statutory NHF on basic salary alone. The old NGN 3,000 annual threshold/basic-only wording is superseded. [Business Facilitation Act Schedule 44 to 46](https://nipc.gov.ng/assets/resources/business-facilitation-miscellaneous-provisions-act-2022/business-facilitation-misc-provisions-act-2022.pdf). The protected contribution companion has not been rewritten here; any conflicting old NHF base in it must not override this amendment. No universal NHIS/NHIA employee or employer percentage is established here. [NHF sections 4,9 and10](https://fmbn.gov.ng/backend/storage/uploads/37UNgpzsyASabzhQCnHuyzFtIpnsfmW2ODvAmQSG.pdf).

### Compute gross taxable income and PAYE

1. Total cash basic, housing, transport, other taxable allowances, bonuses/commission and arrears actually taxable in the period. Identify genuine expense reimbursements separately; a label alone does not exempt cash.
2. Value non-cash benefits under the personal-tax home's section 14 method. Owned assets use cost, falling back to acquisition market value only if cost is unknown; hired assets use rent/hire. Apply the actual exclusions and accommodation cap. Keep taxable value separate from cash paid.
3. Aggregate taxable income, then subtract actual eligible deductions under the personal-tax home. Pension/NHF/qualifying NHIS are not automatic estimated deductions, and employee loans are not tax relief. Apply properly evidenced rent/other deductions and the correct year rules. Do not deduct employer pension from employee income.
4. Apply current personal bands to the appropriate annual/period computation, reconciling cumulative taxable income, prior PAYE, starts/leavers, other employers and non-periodic payments. A steady full-year salary may use annual tax divided by 12 as the illustration below; that shortcut is not a universal rule for a bonus, termination or partial year. JRB paragraph 13 taxes non-periodic amounts in the month paid, and NTA section 26 fixes the relevant payment-year rules. Keep the exact cumulative worksheet and the authority's prescribed procedure. [NTA sections 13,14,26,28,30 and58](https://nass.gov.ng/documents/download/11249); [JRB paragraphs 6 to13](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf).

### Net cash and employer cost

Net cash = cash earnings minus actual employee contributions, PAYE and authorised voluntary cash deductions. Taxable non-cash benefits are not added to cash earnings in that formula. Show any reimbursement separately. Employer cost = cash pay plus employer pension, assessed ECS, applicable ITF, employer health, group life and actual benefit costs; do not substitute taxable benefit value for its actual employer cost. Accrue employer liabilities without deducting them a second time from employee net pay. ECA section 14 prohibits employees funding the compensation scheme. [ECA section 14](https://nsitf.gov.ng/api/uploads/documents/cd29f838-1f78-450d-8650-9d1a6ada54aa.pdf); [PRA sections 4/11](https://ngfrepository.org.ng:8443/bitstream/123456789/968/1/PENSION%20REFORM%20ACT%202014%20-%20GAZETTED%20COPY.pdf). Development levy is a company assessable-profit item in ng-cit, not an extra flat payroll charge.

Business Facilitation Act Schedule paragraph 41 replaces ITF Act section 6: an employer with 25 OR MORE employees and outside a free trade zone contributes 1% of annual payroll. A supplier, contractor or consultant with MORE THAN 25 employees bidding for/soliciting contracts from government or the stated public/private entities has the related compliance duty. Check employee count, zone status and any Minister/FEC-approved Gazette variation. The older 5-staff OR NGN 50m FAQ threshold is withdrawn as current coverage. The 31 March versus 1 April payment wording and purported 5% monthly compound penalty remain held pending operative primary authority. Never deduct ITF from staff. [Business Facilitation Act Schedule 40/41](https://nipc.gov.ng/assets/resources/business-facilitation-miscellaneous-provisions-act-2022/business-facilitation-misc-provisions-act-2022.pdf).

### Payslip, postings and reconciliation

Use a clear recommended payslip with employer name/address/Tax ID, employee name/Tax ID/state/RSA where applicable, period and pay date, cash components, non-cash taxable benefits separately, itemised employee deductions/PAYE, voluntary deductions and net cash. Show employer contributions for transparency and year-to-date gross, PAYE and employee pension. This is a recommended control layout, not a verified assertion that every listed item is a statutory payslip field. Post gross wages, each employer expense and separate liabilities; tie net cash to the bank file and each payment to its authority/scheme receipt.

The original illustrative identity is retained: **ACME NIGERIA LTD**,12 Awolowo Road, Ikoyi, Lagos; **Adaeze Okafor**; employer TIN12345678-0001, employee TIN98765432-0001, RSA PIN PEN100123456789. These are fictional sample identifiers, not prescribed formats. The original pay date is28 May2025, period1 to31 May2025. Use the historical case below for that payslip and change the date only when actually preparing a different payroll. The old placeholder "56,xxx.xx" is not a computed PAYE value.

## Boundary and exception table

| Situation | Required handling |
| --- | --- |
| Bonus, salary arrears, joiner/leaver, multiple employers or negative true-up | Reconcile actual year/month and prior tax. No automatic12-month bonus spread or unapproved refund in the next year. |
| Expatriate, split payroll, foreign currency, treaty or cross-border work | Obtain residence/duties, contract and conversion evidence; route the non-resident skill and refer an unresolved tax point. |
| Director fees or contractor | Determine employment first; a withholding contract is not payroll solely because paid monthly. |
| Stock options, accommodation, company car, domestic staff | Obtain valuation and actual availability/use; no invented higher-of-cost-and-market rule or blanket exemption. |
| Redundancy, gratuity, pension, loss of office | Separate the legal components; use ng-cgt to distinguish the separate death/injury exemption from section 50 compensation and ng-wht for deduction, then annual reconciliation. |
| Voluntary pension above ordinary minimum or missing RSA | Verify scheme terms and tax conditions. No invented20% employee cap or presumed automatic account. |
| Unresolved scheme or levy deadline | Show assessed liability and held filing step; do not publish the old conflicting ECS15th/14-day/month-end dates as law. |

## Worked cases

**Current full-year steady-pay scenario, 2026.** Monthly cash NGN 500,000: basic250,000/housing100,000/transport50,000/utility50,000/meal50,000; no non-cash benefit. Assume a covered pension basis400,000, employee pension32,000 and NHIS0; a private-sector employee who opts into NHF contributes12,500 (2.5% of monthly income500,000). Annual chargeable income before rent is5,466,000. Current annual tax773,880, monthly64,490; net391,010. With evidenced annual tenant rent2.5m, rent relief500k produces annual tax683,880, monthly56,990, net398,510, saving7,500 monthly. If the private-sector employee does not opt into NHF, annual chargeable income is5,616,000, tax800,880, monthlyPAYE66,740 and net401,260 before rent. These amounts assume steady deductions/earnings all year, no other income or prior adjustment. Assume the employer has25+ staff outside a free trade zone and an unchanged1% ITF rate: employer pension40,000, assessed ECS5,000 and ITF accrual5,000 make monthly employer cost550,000. These current assumptions do not alter the original2025 facts.

```oa-check
name: Nigeria steady payroll tenant decision current law
inputs:
  monthly_cash: 500000
  employee_pension: 32000
  employee_nhf: 12500
  annual_rent: 2500000
  employer_pension: 40000
  assessed_ecs: 5000
  given_itf_accrual: 5000
steps:
  - annual_before_rent: (monthly_cash - employee_pension - employee_nhf) * 12
  - rent_relief: min(annual_rent * 0.20, 500000)
  - tax_no_rent: 2200000 * 0.15 + (annual_before_rent - 3000000) * 0.18
  - tax_tenant: 2200000 * 0.15 + (annual_before_rent - rent_relief - 3000000) * 0.18
  - paye_no_rent: tax_no_rent / 12
  - paye_tenant: tax_tenant / 12
  - net_no_rent: monthly_cash - employee_pension - employee_nhf - paye_no_rent
  - net_tenant: monthly_cash - employee_pension - employee_nhf - paye_tenant
  - opt_out_chargeable: (monthly_cash - employee_pension) * 12
  - opt_out_tax: 2200000 * 0.15 + (opt_out_chargeable - 3000000) * 0.18
  - opt_out_monthly_paye: opt_out_tax / 12
  - opt_out_net: monthly_cash - employee_pension - opt_out_monthly_paye
  - employer_cost: monthly_cash + employer_pension + assessed_ecs + given_itf_accrual
expected:
  annual_before_rent: 5466000
  rent_relief: 500000
  tax_no_rent: 773880
  tax_tenant: 683880
  paye_no_rent: 64490
  paye_tenant: 56990
  net_no_rent: 391010
  net_tenant: 398510
  opt_out_chargeable: 5616000
  opt_out_tax: 800880
  opt_out_monthly_paye: 66740
  opt_out_net: 401260
  employer_cost: 550000
```

**Original May2025 sample corrected.** Retain the original monthly split and GIVEN contributions32,000/6,250, no NHIS or other deductions, and assume full-year steady earnings. The6,250 NHF amount is an original scenario input, not the statutory2.5%-of-monthly-income result after8 February2023; actual contribution entitlement/base must be resolved before using this as a real2025 payroll. Historical defined gross after eligible contributions is5,541,000; CRA1,308,200; chargeable4,232,800; annual tax807,872; monthly67,322.67; net394,427.33. This corrects the raw-gross CRA approach and placeholder in the original. Five identical months give cash gross2.5m, pension160k and PAYE336,613.33 before actual payroll rounding reconciliation. This is historical PITA arithmetic under conditional original contribution inputs, not a2026 CRA.

```oa-check
name: Adaeze Okafor original historical payroll CRA corrected
inputs:
  monthly_cash: 500000
  monthly_pension: 32000
  monthly_nhf: 6250
steps:
  - historical_gross_base: (monthly_cash - monthly_pension - monthly_nhf) * 12
  - cra: max(200000, historical_gross_base * 0.01) + historical_gross_base * 0.20
  - chargeable: historical_gross_base - cra
  - annual_tax: 300000 * 0.07 + 300000 * 0.11 + 500000 * 0.15 + 500000 * 0.19 + 1600000 * 0.21 + (chargeable - 3200000) * 0.24
  - monthly_paye: annual_tax / 12
  - monthly_net: monthly_cash - monthly_pension - monthly_nhf - monthly_paye
  - five_month_paye: monthly_paye * 5
expected:
  historical_gross_base: 5541000
  cra: 1308200
  chargeable: 4232800
  annual_tax: 807872
  monthly_paye: 67322.67
  monthly_net: 394427.33
  five_month_paye: 336613.33
```

**Non-cash control.** Cash salary500k, taxable non-cash benefit20k, actual employee contributions38,250 and given PAYE69,215 produce net cash392,535, not412,535. The benefit affects the tax computation upstream; it is not cash due to the employee. This case tests posting, not a legal valuation or tax calculation.

```oa-check
name: Payroll noncash benefit must not inflate cash payable
inputs:
  cash: 500000
  taxable_noncash: 20000
  actual_employee_contributions: 38250
  computed_paye_input: 69215
steps:
  - taxable_gross: cash + taxable_noncash
  - net_cash: cash - actual_employee_contributions - computed_paye_input
expected:
  taxable_gross: 520000
  net_cash: 392535
```

## When to refuse or refer

Do not finalise pay where residence, benefit value, lawful deduction authority, current-year tax, scheme coverage or actual remittance cannot be established. Produce a labelled working paper with missing fields and preserve earned-pay evidence. Refer the boundary cases; do not silently default to a higher tax bracket, disallow every disputed credit or fabricate pension identifiers. This reference does not authorise portal filing or payment.

## Filing and payment

After payroll approval, keep separate instructions for employee net pay, PAYE by authority, pension/PFC, NHF/FMBN, ECS/NSITF and applicable ITF. Save payroll schedules, bank proof and authority/scheme receipts separately; a bank transfer alone does not prove the return filed or the employee account credited. Use the table's verified deadlines. For ECS the Act sets assessment and instalment machinery; obtain the employer-specific monthly instruction rather than choose one of the old unsourced dates. For ITF the current operative deadline remains held. No universal unified TaxProMax payroll module or phased2025/2026 activation date was verified.

At year-end tie employee gross, deductions, net, PAYE and scheme liabilities across every month, bank payment and ledger; resolve December true-ups. File the employer annual return with each appropriate authority by the table's date, showing each employee's gross including benefits, deductions, net and tax deducted. Give an employee a reconciliation statement with income, PAYE and relevant authority/reference; do not import Kenyan "P9A/P9B" as Nigerian official form names. Confirm whether the actual authority uses H1 or monthly FormG rather than claim universal nomenclature. [NTAA section 14](https://nass.gov.ng/documents/download/11250); [JRB paragraph 7/12](https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf).

Current tax late-return/deduction/remittance sanctions are in NTAA sections 101/105/107 and ng-wht; pension penalties appear above. NHF section 20 distinguishes corporate50k and responsible payroll-officer20k/five-year sanctions from self-employed5k/one-year sanctions on conviction; it is not a generic employee5k fine for every employer. No unsourced fixed NHIA/ECS/ITF penalty is added. [NHF section 20](https://fmbn.gov.ng/backend/storage/uploads/37UNgpzsyASabzhQCnHuyzFtIpnsfmW2ODvAmQSG.pdf). Retain records under [NTAA section 31](https://nass.gov.ng/documents/download/11250) and the relevant scheme obligations.

## Sources

| Source and actual read scope | URL | Read on |
| --- | --- | --- |
| NTA sections 13/14,20 to32,58,162,201 and Fourth Schedule | https://nass.gov.ng/documents/download/11249 | 2026-11-16 |
| NTAA sections 3,14,31,100 to107 | https://nass.gov.ng/documents/download/11250 | 2026-11-16 |
| JRB PIT Guidelines paragraphs 5 to15 and computation Appendix1 | https://cms-api.jrb.gov.ng/api/publication-assets/file/2026-pit-guidelines-TJG3n9-T%20%281%29.pdf | 2026-11-16 |
| PRA2014 Gazette, NGF repository: sections 1 to5,10/11 and section 120 monthly-emoluments definition; relevant scan pages OCR and image inspection | https://ngfrepository.org.ng:8443/bitstream/123456789/968/1/PENSION%20REFORM%20ACT%202014%20-%20GAZETTED%20COPY.pdf | 2026-11-16 |
| FMBN original Act: sections 4,9,10 and20, read subject to the Business Facilitation amendments below | https://fmbn.gov.ng/backend/storage/uploads/37UNgpzsyASabzhQCnHuyzFtIpnsfmW2ODvAmQSG.pdf | 2026-11-16 |
| Business Facilitation Act2022, Schedule40/41 and44 to46; ITF and NHF amendments read in full | https://nipc.gov.ng/assets/resources/business-facilitation-miscellaneous-provisions-act-2022/business-facilitation-misc-provisions-act-2022.pdf | 2026-11-16 |
| NSITF ECA: sections 14 and33 to38, employee-funding prohibition and assessment machinery | https://nsitf.gov.ng/api/uploads/documents/cd29f838-1f78-450d-8650-9d1a6ada54aa.pdf | 2026-11-16 |
| NSITF services page, current employer-funded monthly payroll statement | https://nsitf.gov.ng/services/ | 2026-11-16 |
| Historical PITA2011 Gazette consolidated-relief allowance/bands and Finance Act 2020 gross-income amendment, as detailed in personal-tax home | https://lirs.gov.ng/assets/docs/PITA-Ammendment.pdf | 2026-11-16 |
| Finance Act 2020 section 29 | https://www.iirs.im.gov.ng/document/docs/FINANCE_ACT_2020.pdf | 2026-11-16 |

Not yet confirmed: ITF31March versus1April and5% monthly compound penalty; actual ECS monthly remittance due date and employer risk assessment; actual NHF election/administration for a disputed contributor; universal NHIS/NHIA rates or1.75% employee claim; PenCom implementation for employers below 15 and foreign staff; authenticated state payroll fields, compulsory payslip fields or standard H1/FormG labels; a universal P9A/P9B form, employee tax-clearance issuance, automatic next-year refund/offset, statutory maximum voluntary employee pension deduction or unfetched minimum-wage changes. The original sample's statutory amounts remain given facts, not proof of scheme coverage.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ng-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ng-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
