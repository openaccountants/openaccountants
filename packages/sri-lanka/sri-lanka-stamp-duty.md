---
name: sri-lanka-stamp-duty
description: Sri Lanka stamp duty on the instruments specified under the Stamp Duty (Special Provisions) Act No. 12 of 2006, as listed by the Inland Revenue Department, for instruments executed in 2026 (year of assessment 2026/27). Covers affidavits, insurance policies, notary warrants, liquor and trade licences, foreign credit card transactions, bonds and mortgages, promissory notes, leases and hire, hire purchase and receipts; who registers to compound; payment by stamps or to the Commissioner-General's bank accounts; and the provincial immovable property duty, which is outside this skill.
version: "1.0"
jurisdiction: LK
tax_year: 2026
tax_year_notes: "Instruments executed in 2026; year of assessment 2026/27 (2026-27)"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: estate-wealth-tax
type: situation-rules
---

# Sri Lanka Stamp Duty (instruments executed in 2026)

Built from the law: not yet approved by an accountant. Not tax advice.

## Scope and who this is for

- **Background:** stamp duty was first imposed by the Stamp Duty Ordinance of 1909 and re-enacted by the Stamp Duty Act No. 43 of 1982. Under the 13th Amendment to the Constitution, stamp duty on immovable property and certain movable property was devolved to the Provincial Councils, and stamp duty administered by the central government was suspended from 1 May 2002.
- **Central government regime today:** the Stamp Duty (Special Provisions) Act No. 12 of 2006, as amended by Act No. 10 of 2008, reintroduced stamp duty on ten specified instruments only, at rates set by Gazette Order. It applies to every specified instrument executed, drawn or presented in Sri Lanka, and to one executed abroad in relation to property in Sri Lanka, when it is presented in Sri Lanka, subject to the exemptions published in the Gazette. Revenue collected is transferred to the Provincial Councils from 31 March 2011.
- **Out of scope:** stamp duty on deeds of transfer and gift of land, which each Provincial Council's revenue department charges under provincial law. Rates for those were not confirmed on an official page (see Not yet confirmed); refer.
- **Related:** share transfers need a TIN certificate from 1 April 2026 (Inland Revenue (Amendment) Act No. 11 of 2026, new section 103(6)), and the Registrar-General of Companies must check it; the stamp duty rate for a share transfer instrument was not confirmed.

## Ask the client first

1. What is the instrument (lease, mortgage, promissory note, insurance policy, licence, receipt, affidavit)?
2. The value on which duty is charged: sum secured, note amount, aggregate rent or hire over the term, aggregate hire purchase payments, premiums, licence fee, receipt amount.
3. For a lease, the lease term (over 20 years?).
4. Is the instrument about immovable property (bank payment route) or is the issuer a compounding registrant (insurer, licensing authority, credit card provider, employer of over 100 staff)?
5. Where and when was it executed or presented in Sri Lanka?

## The method, step by step

### Rates, bands and thresholds

| Instrument | Rate | Conditions | Source |
| --- | --- | --- | --- |
| Affidavit | Rs. 50 | Gazette 1809/19 | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/StampDuty.aspx?menuid=1209 |
| Policy of insurance | Rs. 1 for every Rs. 1,000 or part | On the aggregate premia payable | same |
| Warrant to act as a notary public | Rs. 2,000 | | same |
| Foreign liquor licence for a calendar year or less | Rs. 20,000 | | same |
| Liquor licences AFL1 to AFL4 issued with a foreign liquor licence | Rs. 2,000 per licence or 10% of the licence fee, whichever is higher | IRD schedule item 4(ii) | same |
| Licence for the sale of bottled toddy | Rs. 2,000 per licence or 10% of the licence fee, whichever is higher | | same |
| AFL1 to AFL4 licences listed in item 4(iv) | Rs. 2,000 per licence or 10% of the licence fee, whichever is lower | The IRD schedule repeats the item 4(ii) description here; read with the Gazette | same |
| Licence to carry on a trade, business, profession or vocation, other than liquor | Rs. 2,000 or 10% of the licence fee, whichever is lower | IRD tax chart stamp duty rows | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx |
| Credit card transactions in foreign countries | Rs. 25 for every Rs. 1,000 or part | | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/StampDuty.aspx?menuid=1209 |
| Bond or mortgage for a definite sum affecting any property | Rs. 1 for every Rs. 1,000 or part | | same |
| Promissory note | Rs. 1 for every Rs. 1,000 or part | | same |
| Lease or hire of any property | Rs. 20 for every Rs. 1,000 or part of the aggregate rent or hire | Capped at the sum for the first 20 years where the term exceeds 20 years | same |
| Hire purchase agreement under the Consumer Credit Act No. 29 of 1982 | Rs. 10 for every Rs. 1,000 or part of the aggregate amount payable | | same |
| Receipt or discharge for money or other property | Rs. 25 | Amount over Rs. 25,000 | same |
| Compounded duty remittance | Quarterly, within 15 days from the end of the quarter | Registered compounding authorities | same |

### Steps

1. Identify the instrument and confirm it is one of the specified instruments; if it is a land transfer or gift deed, stop and refer to the provincial regime.
2. Find the value base and round up to the next Rs. 1,000 where the rate is "per Rs. 1,000 or part".
3. Apply the rate. For a lease over 20 years, use the aggregate rent for the first 20 years only.
4. Choose the payment mode: affix and cancel revenue stamps; for a mortgage or lease of immovable property, credit account No. 7041555 of the Commissioner-General of Inland Revenue at Bank of Ceylon, Taprobane Branch, and attach the bank's payment certificate to the instrument; for compounding registrants, credit account No. 4153842 at the same branch using the IRD pay-in slip with the period code.
5. Compounding registrants keep a separate schedule per instrument category and period (serial number, instrument reference, date, person, value, duty compounded).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Deed of transfer or gift of land | Provincial stamp duty; outside this skill; refer |
| Lease term over 20 years | Duty on the first 20 years' aggregate rent only |
| Instrument executed abroad about Sri Lankan property | Liable when presented in Sri Lanka |
| Insurer, licensing authority, credit card provider, employer of over 100 staff | Must register with the IRD to compound and remit quarterly |
| Unstamped or under-stamped instrument | Duty remains payable; an unstamped instrument may face enforcement problems in court; non-payment is pursued by the IRD; the penalty rates were not confirmed |
| Gift deed at an artificially low value | Provincial valuation matter; refer |

## Worked cases

### Case 1: two-year lease

Rent Rs. 10,000 a month for 2 years. Aggregate rent Rs. 240,000; 240 blocks of Rs. 1,000 at Rs. 20.

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

A 30-year ground lease at Rs. 50,000 a month, financed by a mortgage bond of Rs. 1,000,500. The lease duty is capped at the first 20 years of rent. The mortgage of Rs. 1,000,500 counts 1,001 blocks of Rs. 1,000 or part. Without the cap the lease duty would be Rs. 360,000; with it, Rs. 240,000.

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
- Exemption claims: the exemption Gazettes (1465/20 and later) were not read; refer.
- Share transfer instrument duty: rate not confirmed; refer.
- Penalties for non-payment: refer.

## Filing and payment

| Mode | Detail |
| --- | --- |
| Revenue stamps | Affix and cancel on the instrument |
| Mortgage or lease of immovable property | Credit Commissioner-General of Inland Revenue account No. 7041555, Bank of Ceylon, Taprobane Branch; attach the bank certificate |
| Compounded duty | Credit Stamp Duty account No. 4153842, Bank of Ceylon, Taprobane Branch, with the IRD pay-in slip and period code (for example 25120 for the quarter ended 31 December 2025), within 15 days after the quarter |

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

Not yet confirmed: provincial stamp duty on deeds of transfer of land (earlier version gave 3% on the first Rs. 100,000 and 4% above, from non-official pages) and on gift deeds (3% on the first Rs. 50,000 and 2% above); the earlier claim that leases with monthly rent below Rs. 5,000 are exempt (not on the IRD page; may sit in an exemption Gazette); the compound rate of Rs. 875 per person for employers; stamp duty on share transfer instruments, cheques and bills of exchange under the 1982 Act; penalties for non-payment; whether the item 4(iv) row on the IRD page names the correct licences; the 2013 to 2019 rate Gazettes themselves (the rates above are as the IRD page states them).
