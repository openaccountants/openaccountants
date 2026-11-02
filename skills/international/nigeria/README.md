---
jurisdiction: NG
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: ng-personal-income-tax
  IT-CORP: ng-cit
  SC: ng-pension-nhf-social-contributions
  XB: ng-non-resident-cross-border
partial:
  IT-IND: "ng-personal-income-tax and ng-income-tax carry tax_year 2025 and cite the Personal Income Tax Act, repealed by the Nigeria Tax Act 2025 from 1 January 2026"
  IT-CORP: "ng-cit carries tax_year 2025 and cites the Companies Income Tax Act, repealed by the Nigeria Tax Act 2025 from 1 January 2026"
  VAT: "ng-vat, ng-vat-return and nigeria-vat carry tax_year 2025 and cite the VAT Act, now replaced by the Nigeria Tax Act 2025"
  PR: "ng-payroll carries tax_year 2025 and uses the repealed PITA bands; ng-pension-nhf-social-contributions gives the 2026 bands for its example only and does not cover PAYE administration"
  SC: "the private-sector pension threshold conflicts (Pension Reform Act s2(2) says 15 employees, PenCom guidance says 3); the ITF liability threshold, ITF and NSITF due dates and NSITF and ITF penalties are not confirmed"
  XB: "deduction-at-source rates on payments to non-residents are set by regulations not yet read; ng-wht carries tax_year 2025"
---

# Nigeria: tax pack

From 1 January 2026, the Nigeria Tax Act 2025 is the principal substantive tax law. It replaced the Companies Income Tax Act, the Personal Income Tax Act, the VAT Act and other statutes. Procedure, returns and penalties are in the Nigeria Tax Administration Act 2025. The Federal Inland Revenue Service is now the Nigeria Revenue Service (NRS). The tax year is the calendar year (a company's accounting year for company tax), and the currency is the naira (NGN).

Under the new Act, individuals pay 0% on the first NGN 800 000 of taxable income, then 15% to 25%. Companies pay 30% (small companies 0%), and most also pay a 4% development levy. Employers also run the pension scheme (10% + 8%), the National Housing Fund (2.5% of basic) and the NSITF and ITF contributions (1% each).

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | ng-personal-income-tax, ng-income-tax (pre-2026 law) | sourced from the law |
| IT-CORP, corporate income tax | ng-cit (pre-2026 law) | sourced from the law |
| VAT | ng-vat, ng-vat-return, nigeria-vat (pre-2026 law) | sourced from the law |
| SC, social contributions | ng-pension-nhf-social-contributions (pension 10% + 8%, threshold 15 staff in the Act and 3 in PenCom guidance; NHF 2.5% of basic, NSITF 1%, ITF 1%, with the 2026 tax interaction); partial, see above | checked against the law |
| PR, payroll withholding | ng-payroll (pre-2026 law) | sourced from the law |
| TP, transfer pricing | (missing) NTA s191 relies on the Transfer Pricing Regulations, whose text was not reachable from an official source on 2026-10-29 | |
| XB, cross-border | ng-non-resident-cross-border (2026: residence tests, s17 non-resident charge, PE and SEP, profit-margin fallback, 4% minimum, s18 shipping, s19 dividends, ss119–121 double tax relief, non-resident company returns, NTAA penalties); partial, see above | checked against the law |

"Checked against the law" applies once the independent review is recorded on the pull request.

## Official sources

- Nigeria Tax Act 2025, Official Gazette No. 117 of 26 June 2025: https://nass.gov.ng/documents/download/11249 (read 2026-10-29)
- Nigeria Tax Administration Act 2025, Official Gazette No. 117 of 26 June 2025: https://nass.gov.ng/documents/download/11250 (read 2026-10-29)
- Pension Reform Act 2014, PenCom copy: https://www.pencom.gov.ng/wp-content/uploads/2018/01/PRA_2014.pdf (read 2026-10-29)
- PenCom, FAQ on the Contributory Pension Scheme (2020): https://pencom.gov.ng/wp-content/uploads/2020/06/FREQUENTLY-ASK-QUESTION-2020-ENGLISH-MAIN-VISUAL.pdf (read 2026-10-29)
- National Housing Fund Act, Cap. N45 (FMBN): https://fmbn.gov.ng/backend/storage/uploads/37UNgpzsyASabzhQCnHuyzFtIpnsfmW2ODvAmQSG.pdf (read 2026-10-29)
- NSITF services: https://nsitf.gov.ng/services/ (read 2026-10-29)
- Industrial Training Fund, Revenue department: https://itf.gov.ng/departments/revenue.html (read 2026-10-29)
