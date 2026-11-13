---
jurisdiction: US-ID
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
covered_by:
  IT-IND: id-income-tax
  IT-CORP: id-corporate-tax
  VAT: id-sales-tax
  SC: id-payroll
  PR: id-payroll
partial:
  IT-IND: "Verified 2025-2026 filing cycle; final annual 2026 figures/forms, full credits/modifications and Form 43 allocation remain unconfirmed."
  IT-CORP: "Verified 2025-2026 filing cycle; final annual 2026 forms, full apportionment/combined reporting and pass-through/ABE computations remain unconfirmed."
  VAT: "Core state sales/use rules; current local rates, general service/SaaS bundles and penalty computations remain unconfirmed."
  SC: "Ordinary UI coverage and 2026 rates/base; complete special-employer, multistate and successor computations remain unconfirmed."
  PR: "Published July 2026 tables and returns; periodic Form 910 due dates, earlier-year tables and complete wage exclusions remain unconfirmed."
  TP: "No standalone Idaho related-party/transfer-pricing computation in this pack."
  XB: "Residency and multistate boundaries only; no complete cross-border return computation."
---

# Idaho: tax skills

Idaho has individual and corporate income taxes, corporate franchise tax as an alternative to income tax, sales/use tax and resort-city taxes, payroll withholding and employer unemployment insurance. Currency is USD. Load the relevant federal owner skill alongside the state skill; federal figures are not repeated here.

## Skills and ownership

| Job | Skill | Coverage and status |
|---|---|---|
| Individual income | [id-income-tax](id-income-tax.md) | Form 40 basics for the 2025-2026 filing cycle; partial annual 2026 coverage |
| Corporate income/franchise | [id-corporate-tax](id-corporate-tax.md) | Form 41 basics, minimum and PBF; partial annual 2026 coverage |
| Sales/use | [id-sales-tax](id-sales-tax.md) | 2026 state collection, transactions and filing; local and specialist gaps explicit |
| Payroll withholding and unemployment | [id-payroll](id-payroll.md) | Published 2026 payroll tables, UI rates/base and account filing; confirmation gaps explicit |

All four skills are **Built from the law; Not yet approved**. The income skill listed by the old README did not exist; it is now present. A file's presence does not mean partial domains are complete.

## Outside this pack

Property, fuel and mine-license taxes; detailed partnership/S corporation returns and ABE elections; comprehensive Form 43 allocations; specialist exemptions; international treaty work and separate related-party computations. Estate/inheritance treatment was not checked in this pass; the old README's blanket no-tax statement is not relied upon. Idaho's corporate franchise alternative is explained in the corporate skill; no separate comprehensive gross-receipts-tax skill is supplied.

## Official sources

The [Idaho State Tax Commission](https://tax.idaho.gov/taxes/income-tax/business-income/online-guide/) supplies the annual 2025 business-rate history and return framework. The [2026 Labor array](https://www.labor.idaho.gov/wp-content/uploads/2024/12/AO.682.pdf) supplies unemployment rates/base. Both were read on 2026-11-13; each skill records exact sources, read scope and unresolved items.
