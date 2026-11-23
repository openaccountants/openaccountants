---
name: sri-lanka-stamp-duty
description: Central Sri Lankan stamp duty for instruments executed in 2026 under the Stamp Duty (Special Provisions) Act No. 12 of 2006. Covers instrument rates and exemptions, payment, compounding and the boundary with provincial duty.
version: "1.1"
jurisdiction: LK
tax_year: 2026
tax_year_notes: "Instruments executed in 2026; year of assessment 2026/27 (2026-27)"
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: estate-wealth-tax
type: situation-rules
---

# Sri Lanka Stamp Duty (instruments executed in 2026)

Built from the law: not yet approved by an accountant. Not tax advice.

## Scope and who this is for

- **Background:** stamp duty was first imposed by the Stamp Duty Ordinance of 1909 and re-enacted by the Stamp Duty Act No. 43 of 1982. Under the 13th Amendment to the Constitution, stamp duty on immovable property and certain movable property was devolved to the Provincial Councils, and stamp duty administered by the central government was suspended from 1 May 2002.
- **Central government regime:** sections 3 to 5 of the Stamp Duty (Special Provisions) Act No. 12 of 2006, as amended by Act No. 10 of 2008, charge duty at Gazette rates on specified instruments. Section 4 includes share certificates and allows the Minister to specify further instruments by Gazette Order. Duty applies to specified instruments executed, drawn or presented in Sri Lanka, and to instruments executed abroad relating to Sri Lankan property when presented in Sri Lanka, subject to Gazette exemptions. Revenue collected is transferred to the Provincial Councils from 31 March 2011.
- **Provincial duty:** refer land transfers and gifts to the Provincial Council revenue department for the applicable rates and valuation rules.
- **Related TIN requirement:** section 103(6) of the Inland Revenue Act has effect from 1 April 2026. It covers specified persons and transactions, with verification routes and exceptions under sections 103(6)(c) and 103(7). The IRD deferred implementation of mandatory TIN certificate submission for individuals in the specified transactions until 1 April 2027.

## Ask the client first

1. What is the instrument (lease, mortgage, promissory note, insurance policy, licence, receipt, affidavit)?
2. What is the chargeable value, including any lease or hire premium?
3. For a lease, the lease term (over 20 years?).
4. Does the instrument concern immovable property, or does the issuer have written permission to compound? For an employer, check whether it employs more than 100 people and accepts receipts for employee payments.
5. Where and when was it executed or presented in Sri Lanka?

## The method, step by step

### Rates, bands and thresholds

| Instrument | Rate | Conditions | Source |
| --- | --- | --- | --- |
| Affidavit | Rs. 50 | Check the exemptions for specified affidavits. | Gazette 1809/19 |
| Policy of insurance | Rs. 1 for every Rs. 1,000 or part | On aggregate premiums payable. Exemptions include life and medical insurance. | Gazettes 1789/09 and 2007/24 |
| Warrant to act as a notary public | Rs. 2,000 | | Gazette 1789/09 |
| Licence for a liquor trade or business | Rs. 20,000 | For the period specified in the licence. Apply the separate rate below to the listed arrack and bottled toddy licences. | Gazette 2104/05 |
| Arrack licence AFL1 to AFL4 issued with a foreign liquor licence, or licence for the sale of bottled toddy | Rs. 2,000 or 10% of the licence fee, whichever is higher | Apply per licence. | Gazette 2104/05 |
| Licence to carry on a trade, business, profession or vocation, other than liquor | Rs. 2,000 or 10% of the licence fee, whichever is lower | For the period specified in the licence. | Gazette 2104/05 |
| Credit card payment claim for a transaction with a merchant country outside Sri Lanka | Rs. 25 for every Rs. 1,000 or part | Exclude finance and service charges. Applies to card-present and card-not-present transactions in any currency. | Gazette 1947/45 |
| Share certificate issued on an issue, transfer or assignment of shares | Rs. 5 for every Rs. 1,000 or part | On the aggregate open-market value on that date as determined by the revenue officer. Check exemptions, including where the Share Transaction Levy was charged. | Gazettes 1882/17 and 1465/20 |
| Bond or mortgage for a definite sum affecting any property | Rs. 1 for every Rs. 1,000 or part | Check exemptions including qualifying housing loans. | Gazette 1465/19 as amended |
| Promissory note | Rs. 1 for every Rs. 1,000 or part | On the amount payable. | Gazette 1465/19 |
| Lease or hire of any property | Rs. 20 for every Rs. 1,000 or part of the aggregate lease or hire payments including premium | Use the amount payable for the first 20 years if the term exceeds 20 years. A building lease or rent of Rs. 5,000 a month or less is exempt. | Gazettes 2429/39 and 1465/20 |
| Hire purchase agreement under the Consumer Credit Act No. 29 of 1982 | Rs. 10 for every Rs. 1,000 or part of the aggregate amount payable | Check the vehicle and other exemptions. | Gazettes 2429/39 and 2007/24 |
| Receipt or discharge for money or other property | Rs. 25 | Amount over Rs. 25,000 and no exemption applies. | Gazettes 1530/13 and 1465/20 |
| Compounded duty remittance | Quarterly, within 15 days after the end of the calendar quarter | Applies to permitted compounding authorities unless the Commissioner-General directs otherwise. | Act, section 7 |

### Steps

1. Identify the instrument and confirm it is one of the specified instruments; if it is a land transfer or gift deed, stop and refer to the provincial regime.
2. Find the value base and round up to the next Rs. 1,000 where the rate is "per Rs. 1,000 or part".
3. Check the exemptions, then apply the rate to the chargeable amount. Include any lease or hire premium and apply the 20-year cap where required.
4. Use the payment mode below. Check the statutory timing for the instrument and the IRD instructions for current payment details.
5. Compounding registrants keep a separate schedule per instrument category and period (serial number, instrument reference, date, person, value, duty compounded).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Deed of transfer or gift of land | Provincial stamp duty; outside this skill; refer |
| Lease or hire term over 20 years | Duty on the aggregate lease or hire amount payable for the first 20 years, including any premium |
| Instrument executed abroad about Sri Lankan property | Liable when presented in Sri Lanka |
| Insurer, licensing authority, credit card service provider or employer with more than 100 staff that accepts employee payment receipts | Compound with written permission, register and enter into a bond. Authorised compounders other than those employers issue a certificate when compounded duty is paid. |
| Unstamped or under-stamped instrument | Duty remains payable; an unstamped instrument may face enforcement problems in court; non-payment is pursued by the IRD; the penalty rates were not confirmed |
| Gift deed at an artificially low value | Provincial valuation matter; refer |

## Worked cases

### Case 1: two-year lease

Assume a taxable building lease with no premium. Rent is Rs. 10,000 a month for 2 years. Aggregate rent is Rs. 240,000, or 240 blocks of Rs. 1,000 at Rs. 20.

```oa-check
name: Two-year lease, Rs. 10,000 a month
inputs:
  monthly_rent: 10000
  months: 24
steps:
  - aggregate: monthly_rent * months
  - blocks: ceil(aggregate / 1000)
  - duty: blocks * 20
expected:
  aggregate: 240000
  blocks: 240
  duty: 4800
```

### Case 2: a 30-year lease and a mortgage, with the 20-year cap

A taxable 30-year ground lease at Rs. 50,000 a month has no premium. A taxable mortgage bond secures Rs. 1,000,500, which counts as 1,001 blocks of Rs. 1,000 or part. The first 20 years give lease duty of Rs. 240,000. Using the whole term would give Rs. 360,000.

```oa-check
name: Long lease capped at 20 years, plus mortgage rounding
inputs:
  monthly_rent: 50000
  term_years: 30
  mortgage: 1000500
steps:
  - capped_years: min(term_years, 20)
  - lease_duty: ceil(monthly_rent * 12 * capped_years / 1000) * 20
  - uncapped_duty: ceil(monthly_rent * 12 * term_years / 1000) * 20
  - mortgage_duty: ceil(mortgage / 1000) * 1
expected:
  capped_years: 20
  lease_duty: 240000
  uncapped_duty: 360000
  mortgage_duty: 1001
```

## When to refuse or refer

- Land transfer or gift deeds, or any provincial stamp duty: refer to the Provincial Council revenue department and a Sri Lankan professional.
- Exemption claims: identify the instrument and check the exemption order and its amendments. Refer if the necessary facts or the current order cannot be established.
- Share transfer: distinguish a chargeable share certificate from the transfer instrument and check whether the Share Transaction Levy exemption applies. Refer where liability on the transfer instrument itself is uncertain.
- Penalties for non-payment: refer.

## Filing and payment

| Mode | Detail |
| --- | --- |
| Revenue stamps | Affix before or at execution and state the amount on the face of the instrument. Cancel in ink at execution and perforate adhesive stamps of Rs. 50 or more. A chargeable share transfer executed in Sri Lanka must be stamped within one month. |
| Mortgage or lease of immovable property | The prescribed bank route is available before or at execution. If payment then is impossible for reasons beyond the payer's control, pay the bank within 7 days after execution. Attach the bank certificate. |
| Compounded duty | Use the IRD's current pay-in slip and period code. For July to September 2026 the statement code was 2630 and the payment period code was 26090. Both were due 15 October 2026. |

## Completion checklist

- [ ] Instrument is a specified instrument, not a provincial land deed
- [ ] Value base found and rounded to Rs. 1,000 or part
- [ ] 20-year cap applied to long leases
- [ ] Payment mode and account chosen; certificate attached where needed
- [ ] Compounding registrants: quarterly schedule and remittance

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the charging rule, the schedule of ten instruments and rates, compounding registration, payment modes, bank accounts and period codes on the IRD stamp duty page | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/StampDuty.aspx?menuid=1209 | 2026-11-14 |
| Read for the stamp duty rows (affidavit, insurance, notary, trade and liquor licences) of the IRD tax chart, the latest on the site | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx | 2026-11-14 |
| Read for section 24 of the Inland Revenue (Amendment) Act No. 11 of 2026 (new section 103(6), TIN certificate for share transfers from 1 April 2026) | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf | 2026-11-14 |
| Stamp Duty (Special Provisions) Act, sections 3 to 13 | https://www.ird.gov.lk/en/Type%20of%20Taxes/Stamp%20Duty_Acts/SDActNo.12%5BE%5D2006ConsolFinal.pdf | 2026-11-24 |
| Gazette 1465/19, base rates | https://www.ird.gov.lk/en/publications/Gazette_Documents/2006_1465-19_E.pdf | 2026-11-24 |
| Gazette 1789/09, insurance and notary warrants | https://www.ird.gov.lk/en/publications/Gazette_Documents/2012_1789_09%20(E).pdf | 2026-11-24 |
| Gazette 1809/19, affidavit rate | https://www.ird.gov.lk/en/publications/Gazette_Documents/2013_1809_19%20(E).pdf | 2026-11-24 |
| Gazette 2104/05, licence rates | https://www.ird.gov.lk/en/publications/Gazette_Documents/2018_2104-05_E.pdf | 2026-11-24 |
| Gazette 1882/17, share certificates | https://www.ird.gov.lk/en/publications/Gazette_Documents/2014_1882-17_E.pdf | 2026-11-24 |
| Gazette 2429/39, lease, hire and hire purchase rates | https://www.ird.gov.lk/en/publications/Gazette_Documents/2025_2429-39_E.pdf | 2026-11-24 |
| Gazette 1947/45, foreign credit card transactions | https://www.ird.gov.lk/en/publications/Gazette_Documents/2016_1947_45_E.pdf | 2026-11-24 |
| Gazette 1465/20, exemptions | https://www.ird.gov.lk/en/publications/Gazette_Documents/2006_1465-20_E.pdf | 2026-11-24 |
| Gazette 1530/13, receipt rate and exemption | https://www.ird.gov.lk/en/Type%20of%20Taxes/Stamp%20Duty_Gazette/20081530_13%5BE%5D.pdf | 2026-11-24 |
| Gazette 2007/24, finance lease and hire purchase exemptions | https://www.ird.gov.lk/en/publications/Gazette_Documents/2017_2007_24_E.pdf | 2026-11-24 |
| IRD 5 October 2026 stamp duty notice, quarter-end payment and statement codes | https://www.ird.gov.lk/ta/Lists/Latest%20News%20and%20Notices/Attachments/800/SD_05102026_26090_T.pdf | 2026-11-24 |
| IRD 5 November 2026 TIN certificate notice | https://www.ird.gov.lk/en/Lists/Latest%20News%20%20Notices/Attachments/823/SEC_PN_IT_2026-06_E.pdf | 2026-11-24 |

Not yet confirmed: a separate Rs. 875 per person employer compounding rate, residual duty under the 1982 Act on cheques and bills of exchange, and the applicable penalty amount for a specific default.
