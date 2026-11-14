---
name: sri-lanka-withholding-tax
description: ALWAYS read this skill before touching any Sri Lanka withholding tax or Advance Income Tax (AIT) work for the year of assessment 2026/27 (1 April 2026 to 31 March 2027). Use whenever asked to compute, deduct, or reconcile Sri Lanka WHT on interest, dividends, rent, service fees, royalties, winnings, gems or payments to non-residents under the Inland Revenue Act No. 24 of 2017 as amended up to Act No. 11 of 2026. Trigger on phrases like Sri Lanka WHT, Sri Lanka AIT, advance income tax Sri Lanka, interest WHT Sri Lanka 10%, dividend WHT Sri Lanka 15%, rent WHT Sri Lanka, service fee WHT 5%, non-resident WHT 14%, withholding certificate, WHT self-declaration.
version: "2.0"
jurisdiction: LK
tax_year: 2026
tax_year_notes: "Year of assessment 2026/27 (2026-27), 1 April 2026 to 31 March 2027"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: computation
---

# Sri Lanka Withholding Tax and Advance Income Tax (AIT), v2.0

Built from the law: not yet approved by an accountant. Produced by OpenAccountants (openaccountants.com). Not tax advice. Year of assessment 2026/27.

## Scope and who this is for

| Field | Detail |
| --- | --- |
| Country and authority | Sri Lanka, Inland Revenue Department (IRD) |
| Statute | Inland Revenue Act No. 24 of 2017 (IRA), Part IV Division II (sections 83 to 89), as amended by Act No. 2 of 2025 (rates from 1 April 2025) and Act No. 11 of 2026 |
| Mechanism | The payer (withholding agent) deducts tax at source and pays it to the IRD; the withholdee credits it against its income tax |
| Currency | LKR |

- **In:** payers of interest, discount, dividends, rent, service fees, royalties, winnings, gem auction proceeds and payments to non-residents.
- **Not here:** APIT on employment income (section 83): `sri-lanka-payroll` and `sri-lanka-income-tax`. Instalments by the recipient: `sri-lanka-provisional-tax-ait`. VAT and SSCL: their own skills.
- **2026/27 changes (Act No. 11 of 2026, certified 3 June 2026):** the list of resident individual service providers under section 85(1C)(c) was widened (auditors, modellers, personal trainers, coaches, valuers, artists, actors, dancers, singers, musicians, event organizers, photographers, videographers, therapists, counsellors, beauticians, cooks, electricians, dentists, veterinarians, social media specialists, brand ambassadors, sports persons, IT specialists, advertising agents, advisors, translators, writers, debt collectors); interest paid by a financial institution to a resident individual with no taxable income who gives a self-declaration is outside section 84 from 1 April 2025 (new section 84(3)(f)); a withholding certificate must be served free of charge (new section 87(6)); the Commissioner-General may prescribe statement formats, with a penalty of up to Rs. 200,000 a year for non-compliance (new sections 86(9) and 178A).

## Ask the client first

1. Payer's TIN; recipient's legal name, TIN and residence status.
2. Nature of the payment: interest, dividend, rent, service fee, royalty, winnings, gem auction, transport or telecom to a non-resident.
3. Gross amount and period; for rent and resident service fees, the aggregate paid to that person in the calendar month.
4. For interest to an individual: is there a self-declaration of no taxable income on file?
5. For a non-resident claiming treaty relief: tax residence certificate and beneficial ownership.

## The method, step by step

### Rates, bands and thresholds

| Payment | Rate | Conditions | Source |
| --- | --- | --- | --- |
| Interest or discount | 10% | From 1 April 2025 | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx |
| Dividend | 15% | From 1 April 2025 | same |
| Rent to a resident person | 10% on the full payment | Only if aggregate rent exceeds Rs. 100,000 in the calendar month | same |
| Service fee to a resident individual who is not an employee (teaching, lecturing, invigilating, exam supervision; commission or brokerage to an insurance, sales or canvassing agent; independent service providers) | 5% on the full payment | Only if aggregate payment exceeds Rs. 100,000 in the calendar month | same |
| Winnings from a lottery, reward, betting or gambling | 14% | | same |
| Charge, natural resource payment or premium (section 195) | 14% | | same |
| Royalty (section 195) | 14% | | same |
| Rent to a non-resident | 14% | Treaty may reduce | same |
| Service fee or insurance premium to a non-resident | 14% | Treaty may reduce | same |
| Land, sea or air transport or telecom service by a non-resident | 2% | Section 85(2); Gazette 2064/51 of 1 April 2018 | same |
| Sale price of a gem sold at a National Gem and Jewellery Authority auction | 2.5% | | same |
| Payment of tax withheld | Within 15 days after the end of each calendar month | Section 86(1) | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf |
| Annual statement | Within 30 days after 31 March | Section 86(2) | same |
| Late payment penalty | 20% of tax due but not paid | Not paid within 14 days of the due date; section 179(1) | same |
| Late payment interest | 1.5% per month or part month | Sections 157, 159(1) | same |
| Statement format non-compliance | Up to Rs. 200,000 a year, after a warning notice not complied with within 14 days | New sections 86(9), 178A(1), (2) | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf |
| False self-declaration by an individual (interest) | Up to Rs. 200,000 | New section 178A(3) | same |

### Steps

1. Identify the payment type and the recipient's residence.
2. For resident rent and resident service fees, test the Rs. 100,000 monthly aggregate for that payee; if exceeded, withhold on the full payment, not the excess.
3. For interest to a resident individual, check for a self-declaration of no taxable income given to the financial institution (section 84(3)(f)); without it, withhold 10%.
4. For non-residents, apply the statutory rate unless a treaty rate is supported by a residence certificate.
5. Deduct at the time of payment, serve a free withholding certificate (section 87(6)), pay the IRD within 15 days after the month end (section 86(1)).
6. File the annual statement within 30 days after 31 March, in the format the Commissioner-General specifies.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Payment type unclear | Most specific matching category; if still unclear, flag |
| Residence of recipient unconfirmed | Treat as non-resident (14%) and flag |
| Rent or service fee near Rs. 100,000 a month | Withhold if the monthly aggregate exceeds Rs. 100,000 |
| Interest self-declaration not on file | Withhold 10% |
| Treaty rate claimed without certificate | Statutory rate |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Old 5% interest rate | Applied before 1 April 2025 only; 10% now |
| Payer fails to withhold | Payer still pays the tax (section 86(3)); withholdee jointly liable and must pay within 15 days after the month of receipt (section 86(4)); payer may recover from the withholdee (section 86(6)) |
| Interest to an individual with no taxable income, with self-declaration | Not withheld (section 84(3)(f)) |
| Individual with interest income not over Rs. 5,000 for the year | Need not file a return for that reason (new section 94(1)(d)) |
| Credit or final tax | Generally creditable against the recipient's income tax; whether a stream is final depends on the recipient and the payment type: check the IRA for each |
| Banking, insurance, capital markets special regimes | Out of scope |

## Worked cases

### Case 1: interest and rent paid by a company

A company pays Rs. 1,000,000 of interest to a resident company and Rs. 150,000 a month rent to a resident landlord (above the Rs. 100,000 monthly test).

```oa-check
name: Interest and monthly rent withholding, YA 2026/27
inputs:
  interest: 1000000
  monthly_rent: 150000
steps:
  - wht_interest: interest * 0.10
  - wht_rent_month: monthly_rent * 0.10
  - wht_rent_year: wht_rent_month * 12
expected:
  wht_interest: 100000
  wht_rent_month: 15000
  wht_rent_year: 180000
```

### Case 2: decision, one monthly invoice of Rs. 90,000 or Rs. 120,000 to a resident photographer

Photographers were added to the section 85(1C)(c) list by Act No. 11 of 2026. At Rs. 90,000 in a month the aggregate does not exceed Rs. 100,000, so nothing is withheld. At Rs. 120,000 it does, and 5% is withheld on the full Rs. 120,000, not on the Rs. 20,000 excess. For comparison, a Rs. 2,000,000 service fee to a non-resident consultant bears 14% (subject to a treaty with a residence certificate).

```oa-check
name: Resident service fee threshold, and non-resident fee
inputs:
  fee_low: 90000
  fee_high: 120000
  nonresident_fee: 2000000
steps:
  - wht_low: min(fee_low, 0)
  - wht_high: fee_high * 0.05
  - wht_nonresident: nonresident_fee * 0.14
expected:
  wht_low: 0
  wht_high: 6000
  wht_nonresident: 280000
```

## When to refuse or refer

- R-LK-WHT-1: APIT on employment. Not this regime; use `sri-lanka-payroll` or `sri-lanka-income-tax`.
- R-LK-WHT-2: treaty rate claim without a residence certificate. Apply the statutory non-resident rate; escalate treaty analysis.
- R-LK-WHT-3: sector special regimes (banking, insurance, capital markets). Escalate.
- R-LK-WHT-4: VAT or SSCL withholding. Different regimes: `sri-lanka-vat`, `sri-lanka-sscl`.
- Never file or instruct filing; produce a working paper for practitioner review.

## Filing and payment

| Step | Detail |
| --- | --- |
| Deduct | At the time of payment |
| Certificate | Serve a withholding certificate on the withholdee, free of charge (section 87(6)) |
| Pay | Within 15 days after the end of the calendar month (section 86(1)), through IRD e-Services or an authorised bank |
| Annual statement | Within 30 days after 31 March (30 April 2027 for 2026/27), in the specified format (section 86(2), (9)) |
| Recipient | Credits the tax in its instalments (`sri-lanka-provisional-tax-ait`) and return |

## Completion checklist

- [ ] Payment type and residence confirmed
- [ ] Monthly Rs. 100,000 test applied to rent and resident service fees
- [ ] Self-declaration checked for interest to individuals
- [ ] Treaty claims backed by a residence certificate
- [ ] Certificate served, tax paid by the 15th, annual statement diarised

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the withholding tax and AIT rate table, with effect from 1 April 2025, in the IRD tax chart (the latest on the site) | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx | 2026-11-14 |
| Read for sections 84 to 87, 94, 157, 159 and 179 in the IRD consolidated Act | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf | 2026-11-14 |
| Read for sections 12 to 15 (sections 84 to 87), 19 (section 94) and 30 (new section 178A) of the Inland Revenue (Amendment) Act No. 11 of 2026 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf | 2026-11-14 |

Not yet confirmed: IRD Circulars SEC/2025/E/02 and SEC/2025/E/03 (cited by the earlier version, not re-read); the full treaty rate schedule; creditable against final characterisation for each stream; whether the IRD will publish a 2026/27 tax chart with any change to the withholding rates.
