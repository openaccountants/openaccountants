---
name: sri-lanka-withholding-tax
description: ALWAYS read this skill before touching any Sri Lanka withholding tax or Advance Income Tax (AIT) work for the year of assessment 2026/27 (1 April 2026 to 31 March 2027). Use whenever asked to compute, deduct, or reconcile Sri Lanka WHT on interest, dividends, rent, service fees, royalties, winnings, gems or payments to non-residents under the Inland Revenue Act No. 24 of 2017 as amended up to Act No. 11 of 2026. Trigger on phrases like Sri Lanka WHT, Sri Lanka AIT, advance income tax Sri Lanka, interest WHT Sri Lanka 10%, dividend WHT Sri Lanka 15%, rent WHT Sri Lanka, service fee WHT 5%, non-resident WHT 14%, withholding certificate, WHT self-declaration.
version: "2.1"
jurisdiction: LK
tax_year: 2026
tax_year_notes: "Year of assessment 2026/27 (2026-27), 1 April 2026 to 31 March 2027"
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: computation
---

# Sri Lanka Withholding Tax and Advance Income Tax (AIT), v2.1

Built from the law: not yet approved by an accountant. Produced by OpenAccountants (openaccountants.com). Not tax advice. Year of assessment 2026/27.

## Scope and who this is for

| Field | Detail |
| --- | --- |
| Country and authority | Sri Lanka, Inland Revenue Department (IRD) |
| Statute | Inland Revenue Act No. 24 of 2017 (IRA), Part IV Division II (sections 83 to 89), as amended by Act No. 2 of 2025 (rates from 1 April 2025) and Act No. 11 of 2026. Apply sections 73 and 84 to 89 with paragraph 10 of the First Schedule. |
| Mechanism | The payer (withholding agent) deducts tax at source and pays it to the IRD; section 88 governs final withholding and section 89 governs credits for non-final payments |
| Currency | LKR |

- **In:** payers of interest, discount, dividends, rent, service fees, royalties, winnings, gem auction proceeds and payments to non-residents.
- **Not here:** APIT on employment income (section 83): `sri-lanka-payroll` and `sri-lanka-income-tax`. Instalments by the recipient: `sri-lanka-provisional-tax-ait`. VAT and SSCL: their own skills.
- **2026/27 changes (Act No. 11 of 2026, certified 3 June 2026):** the list of resident individual service providers under section 85(1C)(c) was widened (auditors, modellers, personal trainers, coaches, valuers, artists, actors, dancers, singers, musicians, event organizers, photographers, videographers, therapists, counsellors, beauticians, cooks, electricians, dentists, veterinarians, social media specialists, brand ambassadors, sports persons, IT specialists, advertising agents, advisors, translators, writers, debt collectors); interest or discount on a deposit at a financial institution is outside sections 84 and 84A if its resident individual holder has no taxable income and gives the prescribed self-declaration from 1 April 2025 (new section 84(3)(f)); a withholding certificate must be served free of charge (new section 87(6)); the Commissioner-General may prescribe statement formats, with a penalty of up to Rs. 200,000 a year for non-compliance (new sections 86(9) and 178A).

## Ask the client first

1. Payer's TIN; recipient's legal name, TIN and residence status.
2. Nature of the payment: interest, dividend, rent, service fee, royalty, winnings, gem auction, transport or telecom to a non-resident.
3. Gross amount and period; for rent and resident service fees, the aggregate paid to that person in the calendar month.
4. For interest or discount on a resident individual’s deposit: is there a valid self-declaration of no taxable income on file, with the individual’s TIN or the institution assisting with registration under the IRD’s exception?
5. For a non-resident claiming treaty relief: applicable treaty article, tax residence certificate, beneficial ownership, any Sri Lankan permanent establishment and any IRD clearance required for that payment.

## The method, step by step

### Rates, bands and thresholds

Apply the investment and service rates to payments with a Sri Lankan source. Check the exclusions in sections 84(3) and 85(3), including exempt amounts and payments by individuals outside a business. Section 84(3) also excludes interest paid to a financial institution on an ordinary loan and interest or discount on the securities, Treasury bonds and Treasury bills specified in section 84(3)(d). Check the scope of each exclusion before computing withholding.

| Payment | Rate | Conditions | Source |
| --- | --- | --- | --- |
| Interest or discount | 10% | From 1 April 2025 | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx |
| Dividend | 15% | From 1 January 2023, subject to the section 84(3) exclusions | [First Schedule, paragraph 10](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf) |
| Rent to a resident person | 10% on the full payment | Only if aggregate rent exceeds Rs. 100,000 in the calendar month | [First Schedule, paragraph 10](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf) |
| Service fee under section 85(1C) to a resident individual who is not an employee (teaching, lecturing, examining, invigilating, exam supervision; commission or brokerage to an insurance, sales or canvassing agent; listed or prescribed independent service providers) | 5% on the full payment | Only if aggregate payment exceeds Rs. 100,000 in the calendar month | [First Schedule, paragraph 10](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf) |
| Winnings from a lottery, reward, betting or gambling | 14% | | [First Schedule, paragraph 10](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf) |
| Charge, natural resource payment or premium (section 195) | 14% | | [First Schedule, paragraph 10](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf) |
| Royalty (section 195) | 14% | | [First Schedule, paragraph 10](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf) |
| Rent to a non-resident | 14% | Treaty may reduce | [First Schedule, paragraph 10](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf) |
| Service fee or insurance premium to a non-resident | 14% | Treaty may reduce | [First Schedule, paragraph 10](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf) |
| Land, sea or air transport or telecom service by a non-resident | 2% | Resident payer and a payment within section 73(h) or (i); section 85(2) | https://www.ird.gov.lk/en/publications/gazette_documents/2018_2064-51_e.pdf |
| Sale price of a gem sold at a National Gem and Jewellery Authority auction | 2.5% | | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx |
| Payment of tax withheld | Within 15 days after the end of each calendar month | Section 86(1) | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf |
| Annual statement | Within 30 days after 31 March | Section 86(2) | [Income Tax Act s 86(2)](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf) |
| Late payment penalty | 20% of tax due but not paid | Unpaid 14 days after the due date, or by the date on the assessment notice if later; section 179(1) | [Income Tax Act s 179(1)](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf) |
| Late payment interest | one and one-half per cent per month or part month | Computed monthly from the original due date, disregarding extensions; sections 157 and 159(1) | [Income Tax Act ss 157 and 159](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf) |
| Statement format non-compliance | Up to two hundred thousand rupees a year, after a warning notice not complied with within 14 days | New sections 86(9), 178A(1), (2) | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf |
| False self-declaration by an individual (interest) | Up to two hundred thousand rupees | Prior notice must specify the false or misleading particulars. After a penalty, no substitute declaration may be given for the declaration in the notice; sections 178A(3)–(5) | [Act No. 11 of 2026, s 30](https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf) |

### Steps

1. Identify the payment type and the recipient's residence.
2. For resident rent and resident service fees, test the Rs. 100,000 monthly aggregate for that payee; if exceeded, withhold on the full payment, not the excess.
3. For a resident individual’s deposit, check for a valid section 84(3)(f) self-declaration before deduction. For 2026/27, the IRD accepts the declaration for later years until the depositor tells the institution they have taxable income. Reassess eligibility if circumstances change. Apply 10% to interest or discount within the withholding rules after checking the statutory exclusions.
4. For non-residents, identify the domestic rate by payment type and confirm entitlement and evidence under the applicable treaty and IRD procedure before reducing it. For deposit interest below the domestic 10% rate under a treaty, obtain the IRD tax clearance certificate before the institution applies the reduced rate.
5. Deduct at payment, serve the withholding certificate free of charge and pay the IRD by the statutory deadlines below.
6. File the annual statement and applicable quarterly statements or gem auction returns under the reporting deadlines below.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Payment type unclear | Most specific matching category; if still unclear, flag |
| Residence of recipient unconfirmed | Verify residence and Sri Lankan source before selecting a rate. Refer the payment for review if facts remain unresolved. |
| Rent or service fee near Rs. 100,000 a month | Withhold if the monthly aggregate exceeds Rs. 100,000 |
| Interest self-declaration not on file | Withhold 10% if the payment falls within section 84A and no statutory exclusion applies |
| Reduced treaty rate claimed without required evidence or clearance | Use the applicable domestic rate pending verification |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Old 5% interest rate | Applied before 1 April 2025 only; 10% now |
| Payer fails to withhold | Payer still pays the tax (section 86(3)); withholdee jointly liable and must pay within 15 days after the month of receipt (section 86(4)); payer may recover from the withholdee (section 86(6)) |
| Interest or discount on a resident individual’s deposit with a financial institution | No withholding under section 84(3)(f) if the individual has no taxable income and gives the prescribed self-declaration |
| Individual within section 94(1)(c) with interest income of Rs. 5,000 or less for the year | Section 94(1)(d) exempts the individual from filing. Section 94(1)(c) requires qualifying employment income with APIT deducted and no liability under section 82(2)(b) or (c). Comply with any return notice under section 94(2). |
| Credit or final tax | Under section 88(1A), final withholding covers resident-company dividends, non-business lottery, reward, betting and gambling winnings, covered payments to non-resident non-citizens or entities outside a Sri Lankan permanent establishment and non-resident Sri Lankan citizens’ interest subject to the personal relief exceptions. Apply section 89 to non-final payments. |
| Banking, insurance, capital markets special regimes | Out of scope |

## Worked cases

### Case 1: interest and rent paid by a company

A company pays Rs. 1,000,000 of Sri Lankan-source interest subject to AIT to a resident company and Rs. 150,000 of Sri Lankan-source rent each month for 12 months to a resident landlord. The monthly rent exceeds Rs. 100,000.

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

A resident independent photographer receives a Sri Lankan-source service fee as their only payment from that payer in the month. Act No. 11 of 2026 added photographers to section 85(1C)(c). Withhold zero on Rs. 90,000 and 5% of the full Rs. 120,000 if that higher fee is paid. A Rs. 2,000,000 Sri Lankan-source service fee to a non-resident consultant bears 14% under section 85(1B), assuming it falls outside section 85(2), no statutory exclusion applies and no treaty reduces it.

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
- R-LK-WHT-2: treaty rate claim with incomplete eligibility or evidence. Apply the category’s statutory rate pending verification. Refer the treaty question for review.
- R-LK-WHT-3: sector special regimes (banking, insurance, capital markets). Escalate.
- R-LK-WHT-4: VAT or SSCL withholding. Different regimes: `sri-lanka-vat`, `sri-lanka-sscl`.
- Never file or instruct filing; produce a working paper for practitioner review.

## Filing and payment

| Step | Detail |
| --- | --- |
| Deduct | At the time of payment |
| Certificate | Serve the prescribed certificate free of charge within 30 days after the calendar month covered. See sections 87(3) and (6), and section 87(5) for additional dividend certification. |
| Pay | Within 15 days after the end of the calendar month (section 86(1)), through the Online Tax Payment Platform or the bank and payment reference specified by the IRD |
| Annual statement | Within 30 days after 31 March (30 April 2027 for 2026/27), in the specified format (section 86(2), (9)) |
| Quarterly AIT statement | For section 84A withholding, file within 30 days after the quarters ending 30 June, 30 September and 31 December (sections 86(8) and (9)). |
| Gem auction return | The National Gem and Jewellery Authority also files a monthly return within 30 days after month end from 2026/27 (section 84(2)(b)). |
| Recipient | Claim a credit under section 89 for non-final withholding in the calculation of income tax. Treat section 88 final payments under their own rules. |

## Completion checklist

- [ ] Payment type and residence confirmed
- [ ] Monthly Rs. 100,000 test applied to rent and resident service fees
- [ ] Self-declaration checked for interest to individuals
- [ ] Treaty eligibility and required evidence or clearance verified
- [ ] Certificate served, monthly tax paid and applicable statements and returns diarised

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the withholding tax and AIT rate table, with effect from 1 April 2025, in the IRD tax chart | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx | 2026-11-24 |
| Read for sections 84 to 87, 94, 157, 159 and 179 in the IRD consolidated Act | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf | 2026-11-24 |
| Read for sections 12 to 15 (sections 84 to 87), 19 (section 94) and 30 (new section 178A) of the Inland Revenue (Amendment) Act No. 11 of 2026 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf | 2026-11-24 |
| Read for the 2% transport and telecommunications rate in Gazette 2064/51 | https://www.ird.gov.lk/en/publications/gazette_documents/2018_2064-51_e.pdf | 2026-11-24 |
| Read for the 10% interest deduction and treaty clearance in circular SEC/2025/E/02 | https://www.ird.gov.lk/en/publications/Circulars_Circulars/SEC_2025_E_02_E.pdf | 2026-11-24 |
| Read for the earlier procedure and self-declaration annex in circular SEC/2025/E/03 | https://www.ird.gov.lk/en/publications/Circulars_Circulars/SEC_2025_E_03_e.pdf | 2026-11-24 |
| Read for resident deposit declaration validity, updates and the TIN exception in the 24 March 2026 notice | https://www.ird.gov.lk/en/Lists/Latest%20News%20%20Notices/Attachments/779/SEC_PN_IT_2026-01_E.pdf | 2026-11-24 |
| IRD notice of 3 November 2026, payment channels and payment references | https://www.ird.gov.lk/en/Lists/Latest%20News%20%20Notices/Attachments/822/AIT_WHT_APIT_03112026_E.pdf | 2026-11-24 |
| Circular SEC/2026/E/01, resident deposit self-declarations from 2026/27 | https://www.ird.gov.lk/en/publications/Circulars_Circulars/SEC_2026_E_01_E.pdf | 2026-11-24 |

Not yet confirmed: a non-resident's treaty rate and final withholding treatment without the treaty country, source, permanent establishment and other eligibility facts.
