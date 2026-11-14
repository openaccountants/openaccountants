---
name: nt-payroll-tax
description: "Calculate and prepare the Northwest Territories employee payroll tax withheld by employers for calendar 2026. Establish fixed-place, employee, remuneration, normally-outside and low-remuneration scope; register, select the assigned reporting class, prepare remittance and annual returns, reconcile under/over collections and handle cessation. Separate GNWT payroll tax from CRA payroll, T4 income-tax fields and the independent refundable personal NT479 credit."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nt-payroll-tax"
  jurisdiction: "CA-NT"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Northwest Territories employee payroll tax v2.0

## Scope

Use for an employer's workpaper for the separate GNWT employee payroll tax. The **employee** is liable for the tax; the employer must deduct/withhold, file and remit and can be liable for failing to do so. It is not an employer-only levy with an employee contribution hidden in an exception. Residence, age, a CRA payroll account or a federal income-tax outcome does not on its own settle this separate statute. Self-employed drawings without an employment/office relationship are not automatically employment remuneration. [Payroll Tax Act ss.1,3-7,11-12](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [GNWT incidence](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax).

| Quick reference | Entry |
|---|---|
| Place/currency | Northwest Territories, Canada; CAD |
| Period | Calendar 2026 remuneration and actual assigned reporting periods |
| Administrator/account | GNWT Department of Finance, separate payroll-tax registration; not the CRA RP account |
| Main law | Payroll Tax Act, S.N.W.T. 1993, c.11, as amended; not the old file's incorrect R.S.N.W.T. 1988, c.P-2 citation |
| Subordinate law | Payroll Tax Regulations, R-049-93, including R-093-2024; not the old R.R.N.W.T. 1990, c.P-9 citation |
| Forms | Official registration, remittance return and NWT Payroll Tax Annual Return. The actual annual form read is not identified as “NWT401” |
| Personal-return owner | `nt-individual-return`, separate NT428/NT479 and benefit eligibility |

The levy is withheld from employment remuneration for work in the territory; normally-outside work, the statutory low-remuneration exemption, prescribed-territory interactions and deemed-employer provisions can change the base. Do not decide from a postal address alone. Do not call the personal living credit an automatic refund of the levy. [Act ss.1,3-4](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [GNWT employees](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees).

## Ask the client first

1. Obtain employer legal/trade name, structure, address, CRA business number where applicable, GNWT registration/effective date, assigned reporting class, prior returns, assessments and remittances. Establish each fixed-place/deemed-employer fact from actual business activities and contracts.
2. Obtain for each employee the identity/SIN held securely in the workpaper, position/office, employer relationship, dates employed, actual days/part-days worked in each territory, normal-work pattern, all annual earnings and the local-work portion. Year-end residence is a separate personal-return question.
3. Reconcile wages, overtime, shift/on-call pay, bonuses, commissions/honoraria, vacation pay and travel assistance, options, allowances, benefits, employer RRSP payments, expense reimbursements and termination amounts to the actual payroll ledger and federal inclusion/exclusion classification. An accrual is not automatically an amount received or deemed received.
4. Obtain non-cash benefit valuations, grant/vesting/exercise/service dates, reimbursement documents, pension/clergy/religious-order facts, any specific treaty or Indigenous exemption determination, related-party service arrangements and other prescribed-territory taxes.
5. Obtain current and preceding-year remuneration estimates, seasonal dates, any reporting-period variation approval, paid/withheld amounts by period, cessation/successor dates, and prior penalty/interest notices.
6. What filing and payment authority has the human given? Prepare the return, proposed payroll correction and settlement instruction for approval; do not represent an export as filed or a payment as received.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount and conditions for the supported current method | Official source |
|---|---|---|
| Employee payroll rate | 2% of remuneration within the statutory base, after the actual scope/exemption/allocation analysis | [Act s.3](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [GNWT](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees) |
| Normally-outside low-remuneration exemption | Annual remuneration from that employer does not exceed CAD 5,000 **and** the employee normally works outside the territory under the statute. The threshold is not just the allocated territorial amount and is not an unconditional employee exemption | [Act s.3(2.2)](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [Reg.2](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf) |
| Monthly class | Estimated remuneration over CAD 1,000,000; each calendar month. Seasonal employers report monthly during their season | [Reg.8 and Schedule A](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf), [GNWT](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employers) |
| Quarterly class | Over CAD 600,000 and not over CAD 1,000,000; periods ending March, June, September and December | [Reg.8 and Schedule A](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf), [GNWT class table](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employers) |
| Semi-annual class | Over CAD 200,000 and not over CAD 600,000; periods ending June and December | [Reg.8 and Schedule A](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf), [GNWT class table](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employers) |
| Annual class | Not over CAD 200,000; period ending December. The separate annual employee return is still required | [Reg.8 and Schedule A](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf), [GNWT class table](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employers) |
| Registration | Before expiry of 21 days after the first remuneration payment to an employee | [Act s.39](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [GNWT registration](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employers) |
| Remittance return and payment | By the 20th of the month after the assigned period ends; apply the statutory weekend/holiday extension | [Regs.9(2),12](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf), [GNWT](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employers) |
| Annual return | By 28 February following the calendar year; apply the statutory weekend/holiday extension | [Regs.10,12](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf), [actual annual form](https://www.fin.gov.nt.ca/sites/fin/files/resources/nwt_annual_payroll_tax_return_fillable.pdf) |
| Cessation | Notify Finance within seven days; remittance return, tax and annual return no later than the thirtieth day after cessation of the fixed place or employee, subject to the actual extension rule | [Act s.7(2)](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [Regs.11-12](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf) |

### Establish the legal employer and work location

1. Apply the Act's actual employee/employer and fixed-place definitions. Fixed place includes, among others, agency/branch, construction or exploration site, factory, farm, mine/well, office, warehouse and workshop. The deeming rules cover incorporation/required registration, premises, equipment, stock/order fulfilment and conducting business in the territory. The old unsupported construction-site “more than 30 days” threshold is not a safe harbour. A remote worker can create an obligation on the actual facts; neither “no formal office” nor any territorial address alone determines it. [Act s.1](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf).
2. Check related-party supplied personnel. Under s.4 the territorial resident can be the deemed employer where the non-resident supplier has no fixed place, the services are performed in the territory, the relationship condition applies and the work is of the nature described by the Minister test. Do not transfer an account or liability merely because one company invoices another. [Act s.4](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf).
3. Use the full-year, same-employer work/office pattern. Where the employee normally works outside, s.3(2) allocates annual remuneration using territorial work days/part-days over the total relevant employment days, subject to the statutory exceptions. Where that rule does not apply, merely working some days elsewhere does not automatically permit proportional exclusion. GNWT explains that a worker normally working in the territory is taxed on the annual earnings, regardless of home province. [Act s.3(2)-(2.21)](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [GNWT employee guidance](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees).
4. The English s.3(2.1) uses **more than half** outside, while the French printed text uses **au moins la moitié**. The GNWT summary says more than half inside. Do not silently invent an exact-half outcome from these non-identical wordings. An exact-half or disputed pattern needs a documented legal determination; record this specific uncertainty rather than asking the client to choose a rule. Clear patterns away from that boundary can continue. [Act bilingual s.3(2.1)](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [GNWT summary](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees).
5. Apply the normally-outside low-remuneration exemption to the annual remuneration from that employer before assuming every short assignment is taxable. Check s.3(2.21)'s prescribed-territory/similar-tax conditions before omitting a day; paying another province's ordinary income tax is not automatically this exception. The current prescribed-territory list is not certified here. [Act s.3](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [Reg.2](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf).

### Classify and reconcile the remuneration base

6. The statutory ordinary definition ties remuneration to payments/benefits included by reason of federal ITA 5(1),6 or7, with its express pension and deduction exclusions. Include the value of supported taxable wages, bonuses, commissions, allowances, benefits, options and employer RRSP contributions according to that legal analysis. Reimbursements or non-taxable allowances do not become taxable merely because evidence is incomplete. Accrued vacation expense is not automatically paid/received remuneration. [Act s.1](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [GNWT income list](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees).
7. The Act expressly excludes the specified post-retirement pension/annuity/superannuation benefits and amounts deductible under the named clergy/religious-order provisions. Obtain the actual legal character and documents, not a blanket “all payments taxable” fallback. Workers' compensation, travel per diems, controlled tips and termination payments need their proper inclusion/exclusion basis; do not assume every ledger label proves it. [Act s.1](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [GNWT exemptions](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees).
8. GNWT's general list includes retiring allowances/severance. Distinguish employment wages/pay in lieu from an actual retiring allowance and test the statute's definition and possible ministerial deeming in s.3(3). This method has not resolved every federal classification/deeming case. Keep a disputed retiring-allowance amount separate pending that determination, naming both the Act and the guidance, rather than treating either the payroll label or generic list as a blanket answer. [Act ss.1,3(3)](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [GNWT list](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees).
9. Assign a reasonable value to non-monetary remuneration as soon as reasonably possible. Where it cannot be valued in-year, the regulation requires valuation by the following annual deadline and provides later collection. Revisit the return and collection workpaper as the year-end pattern/amount becomes determinable; Reg.5 provides specific uncertain-normal-work and low-remuneration collection/catch-up rules, not a general highest-tax guess. Get written permission for a varied recovery period where required. [Regs.4-7](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf).
10. Compute the tax from each employee's supported taxable remuneration; reconcile deductions, remittances and annual liability. Keep disputed/exempt/allocated amounts visible with their documents. Do not cap the tax by a personal credit or reduce gross employment income merely because this levy was withheld. [Act ss.3,5-7](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [actual annual form](https://www.fin.gov.nt.ca/sites/fin/files/resources/nwt_annual_payroll_tax_return_fillable.pdf).

### Register and select the assigned reporting class

11. Prepare the official registration application with the actual legal name/entity, business/contact/address, books location, first-payment date, seasonal facts, business description and estimated remuneration. Apply the statutory registration deadline independently of the first remittance date; it is not “before the twentieth next month.” Retain the Finance registration number, effective date and assigned period. [Act ss.39-40](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [Reg.17](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf), [actual registration form](https://www.fin.gov.nt.ca/en/files/payrolltaxregistrationform2016pdf).
12. On first registration the period-class estimate comes from the application. For later years Reg.8 uses the greater of the immediately preceding year's actual remuneration and the current estimate. Apply Schedule A's inclusive boundaries, not the vague overlaps in a short web summary. A smaller class is not an informal election; a variation requires the applicable ministerial approval. Seasonal employers have their distinct class. [Reg.8 and Schedule A](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf).
13. Calendar the **period end**, filing due date, payment receipt due date and operational bank/approval cut-off separately. The period ends on its last day; filing/payment are due afterwards. Registered nil periods still require the remittance return. The annual employee return is additional to the period remittance, including for an annual reporter. Do not collapse the two forms. [Act ss.6-9](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [Regs.9-12](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf), [GNWT](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employers).

### Prepare the period and annual returns

For a remittance return, reconcile the payroll schedule to employer/customer identification, reporting period, gross remuneration used in the calculation, tax calculated and amount paid. The actual published remittance form carries the employer identification and payment allocation instructions; it is separate from CRA PD7A. Retain the return, approved settlement instruction and evidence of Finance's receipt, not just mailing or a generated PDF. [Actual remittance form, both pages](https://www.fin.gov.nt.ca/sites/fin/files/resources/nwt_payroll_tax_remittance_form_fillable.pdf), [Act s.9](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf).

For the annual employee return, retain a row for each employee with name/SIN, days worked in the territory, territorial earnings, total annual gross earnings, taxable earnings and payroll tax due/collected. Explain differences between annual and taxable earnings. Total the tax; subtract actual remittances; identify the balance or overpayment. Get the authorised certification and any attached employee listing. The actual form says nil filing is needed if there were no employees, and copies of T4s are not currently required. It is not the old invented seven-part “NWT401” layout. [Actual annual form, both pages](https://www.fin.gov.nt.ca/sites/fin/files/resources/nwt_annual_payroll_tax_return_fillable.pdf), [Reg.10](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf).

Reconcile under/over-collection by employee. Collect/remit supported shortfalls; a refund received for excess employee tax must be passed to the affected employee without delay. The annual form describes crediting an overpayment to the following year unless a written reimbursement request is given. Do not treat an employee's over-collection as employer income or an NT479 payment. Keep the application, account adjustment and actual employee reimbursement. [Act ss.11,17](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [Reg.7](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf), [annual form](https://www.fin.gov.nt.ca/sites/fin/files/resources/nwt_annual_payroll_tax_return_fillable.pdf), [GNWT](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employers).

Where an error or late valuation changes a filed return, prepare the prescribed amendment without delay with correct facts, reason, period/year, amounts collected and tax due. On cessation of a fixed place or employee, use the specific notification and early-return rules above rather than waiting for the ordinary annual date. A sale/successor, receivership, liquidator or related company needs its own account and liability determination; do not assume the old registration transfers. [Act ss.6-7](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [Regs.11,13](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf).

### Separate federal payroll, T4 and personal living credits

- CRA payroll income-tax deductions, CPP/EI and their employer shares remain separate obligations using the CRA RP account and actual federal remitter schedule. This levy uses the GNWT account and period/annual forms. Use `canada-payroll` and `ca-fed-cpp-ei` for their current mechanics, not a duplicated stale rate table here.
- The GNWT explicitly says this levy does not appear on the T4 slip. Do not put it in box22 or invent an “Other information code80” for it; retain the payroll deduction/employee statement and separate annual GNWT listing. Gross employment remuneration is not reduced by this withholding. The old claim that the T4 code is needed to obtain NT479 is false. [GNWT T4 explanation](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees).
- NT(S2) transfers specified spouse credit amounts; it is not the territorial tax return. `nt-individual-return` owns NT428 and the separate refundable NT479. Residence and adjusted net income, not the amount withheld, drive that credit. [Actual CRA NT479 and household rules](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf), [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html).
- For the latest actual 2025-2026 filing cycle read, NT479's basic living credit is capped at CAD942 and does not phase out at high income. A separate eligible-adult/family supplement can top up low basic amounts under its own rule. These actual prior-cycle figures are not final 2026 annual amounts. Neither “low-income workers are always made whole” nor “high income loses the entire credit” is safe advice. [Actual 2025 NT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf).
- A non-resident of this territory working here does not obtain its resident credit merely because the payroll tax was withheld. But do not infer every other tax/foreign-credit or treaty consequence from this one rule. [GNWT work scope](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees), [CRA credit residence](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html).
- For employer accounting, properly withheld employee tax is a payroll liability cleared on remittance, not an additional employer levy deduction. Gross remuneration expense remains separate. Failure-to-collect liability, unrecoverable amounts and a contractual gross-up need their own accounting/tax classification; do not promise zero employer cost for all circumstances. [Act ss.5,11-12](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf).

## Boundary and exception table

| Original refusal/default or fact | Correct response |
|---|---|
| R-NT-PAY-1, sole proprietor without employees | No employee levy on drawings alone; route the self-employed income to the individual/business return, but examine any office or actual employees |
| R-NT-PAY-2, disputed allocation | Obtain same-employer full-year days, normally-outside rule, actual remuneration and exception evidence; refer the disputed legal outcome, including exact-half language conflict |
| R-NT-PAY-3, treaty/non-resident of Canada | Analyse the specific taxpayer, source and controlling treaty/statute; no blanket federal exemption or blanket treaty-override assertion |
| R-NT-PAY-4, Indian Act/status/reserve issue | Obtain actual income connection and controlling exemption/deeming law; status alone is not the answer |
| R-NT-PAY-5, cross-jurisdiction options | Obtain grant/vesting/exercise/service periods and valuation/source analysis before inclusion/allocation |
| R-NT-PAY-6, successor/asset purchase | Obtain transaction, employees, dates and Finance account determination; no assumed account transfer |
| Unknown remuneration classification, old default1 | Investigate and isolate disputed amounts; do not tax everything on the promise of a personal refund |
| Any territorial connection, old default2 | Apply actual employee/fixed-place/work-pattern tests; address/supervisor is evidence, not automatic liability |
| Possible registration, old default3 | Establish actual statutory trigger and deadline; prepare an application for an authorised filer, do not register speculatively |
| Unknown period, old default4 | Obtain assigned Schedule A class and variation; monthly is not universal |
| Registered nil year/period, old default5 | Prepare the required nil returns while checking any cessation/closure decision |
| Foreign employee, old default6 | Retain the R-NT-PAY-3 specialist workpaper, continue supported ordinary employees |
| Personal-credit year, old default7 | Check the actual NT479 edition, income/family facts and separate tax systems; no invented offset/phase-out |

## Penalties and interest

| Failure | Statutory consequence within the stated conditions | Official source |
|---|---|---|
| Failure to collect | 10% of the amount that should have been collected;20% where the specified previous assessment/preceding twelve-month condition is met; tax liability and interest are separate | [Act s.11](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf) |
| Failure to remit/pay collected amounts | 10%;20% for the specified previous assessment/failure within the preceding twelve-month period; tax and interest remain due | [Act s.12](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf) |
| Failure to file period/annual return | CAD100 penalty | [Act s.13](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf) |
| Failure to comply with return demand | Greater of CAD250 and 5% of specified uncollected/unremitted tax, under the demand's actual conditions | [Act s.14](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [GNWT](https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employers) |
| Failure to register when demanded | CAD250 for each failure under that demand; this is not an automatic generic registration fine for every late application | [Act s.39(4)-(5)](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf) |

Use the actual statutory failure and prior-assessment history. Do not add a fictional minimum to an ordinary remittance penalty. Interest follows the law's prescribed rate; this method has not confirmed the current debtor rate, compounding or exact interest period, so do not insert a guessed percentage. Refund interest under Reg.21 is a separate rule and is not the debtor rate by analogy. Criminal prosecution/fines and contested assessments require the actual notice and legal advice, not an automatic payroll journal. [Act ss.11-14,18](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [Reg.21](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf).

## Worked cases

### Case 1: retain the Yellowknife mining-services company and reconcile exactly

“Arctic Drill Services Ltd.” remains the hypothetical company with a Yellowknife yard/office and fifty employees: thirty-five territorial residents earning CAD3.5m and fifteen Alberta/Saskatchewan fly-in workers earning CAD1.5m. For calendar 2026, stipulate that all CAD5m is remuneration within the actual territorial base after each employee's normal-work/exemption analysis. Residence alone is not that proof. Tax withheld/remitted is CAD100,000, consisting of CAD70,000 from the resident group and CAD30,000 from the fly-in group. These are employee deductions, not an additional employer-only charge. [Act ss.3,5](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [annual return](https://www.fin.gov.nt.ca/sites/fin/files/resources/nwt_annual_payroll_tax_return_fillable.pdf).

An illustrative cash schedule can be eleven remittances of CAD8,333.33 and one of CAD8,333.37, reconciling exactly to CAD100,000; dividing and paying twelve rounded equal amounts would leave a difference. Actual period tax comes from actual payroll and approved rounding, not an invented even gross payroll. The class is monthly at this scale. The ordinary annual date following 2026 falls on a Sunday; apply the regulations' next eligible day, subject to the actual local holiday calendar. Reconcile and retain the separate annual employee listing, without a false T4 code. [Reg.8 Schedule A and Reg.12](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf), [annual form](https://www.fin.gov.nt.ca/sites/fin/files/resources/nwt_annual_payroll_tax_return_fillable.pdf).

```oa-check
name: NWT 2026 original fifty-employee company and exact settlement
inputs:
  resident_taxable_pay: 3500000
  fly_in_taxable_pay: 1500000
  first_eleven_remittances_each: 8333.33
  final_remittance: 8333.37
steps:
  - total_taxable_pay: resident_taxable_pay + fly_in_taxable_pay
  - resident_employee_tax: resident_taxable_pay * 0.02
  - fly_in_employee_tax: fly_in_taxable_pay * 0.02
  - total_tax: total_taxable_pay * 0.02
  - paid: first_eleven_remittances_each * 11 + final_remittance
  - balance: total_tax - paid
expected:
  total_taxable_pay: 5000000
  resident_employee_tax: 70000
  fly_in_employee_tax: 30000
  total_tax: 100000
  paid: 100000
  balance: 0
```

### Case 2: the living credit is not a refund of the exact withholding

Retain the original resident-worker CAD80,000 example but label the actual annual credit edition: in the 2025-2026 filing cycle a resident with supported taxable payroll earnings and adjusted net income both CAD80,000 has CAD1,600 employee payroll tax. NT479's basic credit is CAD942, not the old approximate CAD1,500-1,600. Stipulate no family supplement or other adjustment; the difference between those two separate amounts is CAD658. That is not the final T1 tax/refund, nor a current 2026 credit promise. [Act s.3](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [actual 2025 NT479](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf).

```oa-check
name: NWT actual 2025 cycle payroll and independent living credit
inputs:
  taxable_pay: 80000
  adjusted_net_income: 80000
steps:
  - payroll_tax: taxable_pay * 0.02
  - basic_living: min(942, 312 + 36000 * 0.0125 + max(0, adjusted_net_income - 48000) * 0.01)
  - single_adult_supplement: max(0, 350 - basic_living)
  - component_difference: payroll_tax - basic_living - single_adult_supplement
expected:
  payroll_tax: 1600
  basic_living: 942
  single_adult_supplement: 0
  component_difference: 658
```

### Case 3: normally-outside allocation and the correct exemption threshold

For calendar 2026 stipulate a valid employer and an employee normally working outside the territory: two hundred relevant employment days, ten territorial days, no overlapping prescribed-territory exclusion and CAD40,000 annual remuneration from that employer. The allocated base is CAD2,000 and tax CAD40. The employee is **not** exempt just because the allocated base is below the prescribed threshold: the actual threshold tests annual remuneration from that employer. A second otherwise identical worker with CAD4,000 annual remuneration is exempt under the stipulated normally-outside condition. These inputs are away from the exact-half issue and do not decide a real contract's day denominator without evidence. [Act s.3(2)-(2.21)](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf), [Reg.2](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf).

```oa-check
name: NWT 2026 normally-outside base and annual-remuneration threshold
inputs:
  annual_remuneration: 40000
  low_annual_remuneration: 4000
  relevant_employment_days: 200
  territorial_days: 10
steps:
  - allocated_base: annual_remuneration * territorial_days / relevant_employment_days
  - ordinary_tax: allocated_base * 0.02
  - low_allocated_base: low_annual_remuneration * territorial_days / relevant_employment_days
  - low_tax_without_exemption: low_allocated_base * 0.02
  - low_tax_after_stipulated_exemption: 0
expected:
  allocated_base: 2000
  ordinary_tax: 40
  low_allocated_base: 200
  low_tax_without_exemption: 4
  low_tax_after_stipulated_exemption: 0
```

### Contractual gross-up job

Where an employment contract requires the employer to absorb only this levy, additional remuneration can itself enter the levy base. Solve the specified net-pay target algebraically and reconcile cents; do not add the levy percentage once and assume the target is met. A real gross-up must also include the separate federal/territorial income-tax, CPP/EI and other benefit consequences where applicable; this method is not that complete net-pay engine. Obtain the contract and classify the actual pay before posting. [Act ss.1,3,5](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf).

## When to refuse or refer

Do not finalise with unknown employer/employee scope, unsupported taxable benefits, a disputed exact-half/denominator, an unconfirmed exemption or missing assigned period. Continue supported employees while isolating the specific issue. Refer treaty/Indigenous, cross-jurisdiction option, related-party/deemed-employer, successor/cessation and disputed assessment cases with the relevant documents. No automatic taxable-base default is justified by a promised personal-credit refund.

## Completion checklist

- Legal employer, employee, fixed place and any deemed employer established.
- Same-employer annual days, remuneration, low-remuneration and prescribed-territory exceptions checked; residence not substituted for work scope.
- Federal inclusion/exclusion and actual received/deemed-received benefits reconciled; non-cash values and contested termination amounts separately documented.
- Registration effective date, period class, seasonal/variation approvals and nil returns recorded.
- Period and annual returns reconcile by employee to tax withheld, remittances, balance and actual employee refunds.
- Correct calendar due dates and actual receipt/cut-off tracked, including cessation and weekend/holiday rules.
- CRA payroll/T4 and independent personal NT479/benefits separated; no invented reporting code, layout or current credit amount.
- Penalty history, unconfirmed debtor interest and retained records documented; authorised accepted filing and payment receipt retained.

## Records and delivery

Keep payroll source records, activity/day evidence, benefit valuations, exclusions, period/annual workpapers, registration/variation notices, approved journals, returns and remittance receipts. The Act's ordinary minimum is six years from remittance; missing returns, objections/appeals and a ministerial retention demand can extend it. Do not treat a general employment-record rule as the shorter tax-retention period. [Act s.19](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf).

Provide an approval-ready return and, where correction is needed, proposed journal/import or employee adjustment list. Keep preparation, authorised submission, acceptance and Finance's actual receipt distinct. The actual forms provide submission/payment instructions; do not promise an unverified live e-portal or send personal employee data to a guessed endpoint. This method does not register, submit, email, deduct wages or transfer money on the human's behalf. [Actual remittance](https://www.fin.gov.nt.ca/sites/fin/files/resources/nwt_payroll_tax_remittance_form_fillable.pdf), [annual instructions](https://www.fin.gov.nt.ca/sites/fin/files/resources/nwt_annual_payroll_tax_return_fillable.pdf), [Act s.9](https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf).

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| Read for Actual official Payroll Tax Act PDF linked by the new GNWT legislation page: header; ss.1-9,11-14,17-19 and39-40 for scope, tax, collection, returns, receipt, penalties, refunds, records and registration; not every unrelated enforcement provision | https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.a.pdf | 2026-11-14 |
| Read for Official Payroll Tax Regulations R-049-93 including 2024 amendment: ss.2-13,17-19,21 and Schedule A for exemption amount, valuation/collection, period classes, deadlines, cessation, amendments and refund-interest distinction | https://gnwt.ca/sites/default/files/legacy_justice/files/legislation/payroll-tax/payroll-tax.r1.pdf | 2026-11-14 |
| Read for GNWT current employer page for registration, reporting, deadlines, nil returns, reconciliation and conditional penalties; Schedule A resolves its ambiguous threshold wording | https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employers | 2026-11-14 |
| Read for GNWT current employee page for incidence, paystub, income examples/exclusions, normal-work summary, refunds and explicit no-T4 explanation | https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax-employees | 2026-11-14 |
| Read for GNWT payroll-tax overview for employee levy and territory/work scope, not an employer-only tax | https://www.fin.gov.nt.ca/en/services/licences-taxes-et-droits/payroll-tax | 2026-11-14 |
| Read for Actual one-page registration form for employer identification, business/first-payment details and authorised certification, not a speculative account submission | https://www.fin.gov.nt.ca/en/files/payrolltaxregistrationform2016pdf | 2026-11-14 |
| Read for Actual two-page remittance form for identification, remuneration/rate/payment and change/contact instructions | https://www.fin.gov.nt.ca/sites/fin/files/resources/nwt_payroll_tax_remittance_form_fillable.pdf | 2026-11-14 |
| Read for Actual two-page annual return for employee/day/earnings/tax listing, nil filing, reconciliation, certification and actual submission instructions; invented NWT401 layout not used | https://www.fin.gov.nt.ca/sites/fin/files/resources/nwt_annual_payroll_tax_return_fillable.pdf | 2026-11-14 |
| Read for Actual 2025 NT479, entire page, for independent refundable-credit formula and family supplement/cap; explicitly the 2025-2026 filing cycle, not current final annual fields | https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-tc/5012-tc-25e.pdf | 2026-11-14 |
| Read for CRA actual 2025 territorial scope, household credit rule, spouse-transfer purpose and separate ended carbon-offset information; current optional amounts remain with the individual-return method | https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package/northwest-territories/5012-pc.html | 2026-11-14 |

Not yet confirmed: exact-half normal-work outcome where the Act's English/French text and abbreviated GNWT summary differ; current prescribed-territory/similar-tax list; case-specific federal classification and ministerial deeming of retiring allowances/severance or other disputed remuneration; debtor-interest rate/compounding/current period; exact approved payroll/annual rounding; final 2026 NT479 and other personal-credit fields/amounts. Actual treaty/Indigenous exemptions, option allocation, related-party/successor liabilities, complete net-pay gross-up and any current online filing channel need their specific controlling evidence. The source-read scopes above are bounded, not a claim to have read every enforcement provision or to hold accountant approval.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nt-payroll-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nt-payroll-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
