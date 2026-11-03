# kw-payroll-social: figure and rule ledger

Guide: `skills/kuwait/kw-payroll-social.md`. Read date 2026-11-01. The source IDs, blob hashes and precise reading boundaries are preserved in [sources](../sources.md). [Immutable old-topic destinations](../old-topic-destinations.md) also preserve every substantive merge-base row and non-operative hold.

| ID | Guide section / rule or figure | Act, article, page | Exact decisive original-language quote | Official URL | Read date / SHA-256 / read scope |
|---|---|---|---|---|---|
| R8 | The base / Who this applies to: Only-trading Kuwait stock-exchange gains exemption; own natural-person work/trade income exempt unless corporate-body share; statutory/international exemptions retain their stated terms. | art.8, PDF p.8 | الدخل الذي يحققه الشخص الطبيعي من مزاولة التجارة أو العمل في دولة الكويت ما لم يثبت أنه يمثل حصة لهيئة مؤسسة | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf | 2026-11-01; `218254a7ab7405afb26d0b26c336ecb3cce7b5fcfa363b88c21b7a0180da2229`; Arabic reg. arts. 1 to 3, 7 to 14, 19 to 20, 24 to 28, 29 to 34, 37 to 42, 46 with neighbouring clauses; OCR and PDF pp. 8, 22 images read. Prior writer reported all 23 pages OCR. |

## Worked-case recomputation and non-legal instructions

The example inputs are stipulated facts, not legal thresholds. These exact cases are executed by `scripts/check-examples.py --require` and re-read by the fresh reviewer:

**Example 1.** An employee receives KWD 2,000 as their own salary, not a corporate body's share. Art. 8(2) exempts that salary from Kuwait income tax. The income-tax component is zero. KWD 2,000 remains before social deductions; this is not approved net pay.

```oa-check
name: Own salary, income-tax component only
inputs:
  salary: 2000
steps:
  - income_tax: salary * 0
  - before_social_deductions: salary - income_tax
expected:
  income_tax: 0.00
  before_social_deductions: 2000.00
```

**Example 2 (decision).** A payroll record specifies gross salary KWD 3,000, an employee deduction of KWD 200 and employer contribution of KWD 250 for that month. Reconcile the supplied amounts: net cash KWD 2,800 and employer cash cost KWD 3,250. The KWD 200 and KWD 250 are example document inputs, not legal rates. Release only after their current legal basis and coverage are checked. If the supporting assessment is missing, hold the payroll rather than assume expatriate contributions are zero or apply historical percentages.

```oa-check
name: Reconcile documented payroll amounts before release decision
inputs:
  gross_salary: 3000
  documented_employee_deduction: 200
  documented_employer_contribution: 250
steps:
  - net_cash: gross_salary - documented_employee_deduction
  - employer_cash_cost: gross_salary + documented_employer_contribution
expected:
  net_cash: 2800.00
  employer_cash_cost: 3250.00
```

Intake questions collect facts, not legal answers. Portal URLs are entry points only: current authenticated screens, form fields, acknowledgement and payment-reference instructions are not claimed as read. Bank patterns in the routing Guide are search cues and exclude only automatic computation, never transaction history. Metadata, team attribution and general-reference notice are not accountant attestation.

## Non-operative source holds

NON-OPERATIVE HOLDS. Social Security Law 61 of 1976 and amendments; historical employer 11.5%, employee basic 8% plus additional 2.5% (10.5% total), KWD 2,750 monthly ceiling, claimed remittance by the following month's 15th; no current statutory text read supports using these. Historical claims that non-GCC expatriates are outside PIFSS, GCC nationals use home-state schemes, and social insurance applies only to Kuwaiti nationals are not operational conclusions. Labour Law 6 of 2010: historical 15 days per year for the first five years, then one month per year, all calculation caps and entitlement conditions, not verified. Current PIFSS penalties and any unemployment contribution. Prior writer reports only PIFSS homepage opened and manpower.gov.kw failed on 2026-11-01; those are access reports, not law readings. Historical calculation examples KWD 2,000 yielding employer 230/employee 210 and KWD 3,000 yielding employer 316.25, and the Kuwaiti-versus-expatriate hiring comparison, are withdrawn from operative use pending those checks.
