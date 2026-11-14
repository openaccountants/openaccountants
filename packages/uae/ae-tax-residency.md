---
name: ae-tax-residency
description: "UAE tax residency for individuals in 2026 under Cabinet Decision No. 85 of 2022 (in force since 1 March 2023). Covers the three tests (centre of life, 183 days, 90 days with a residence permit or nationality plus a permanent home or work in the UAE), how days are counted, the tax residency certificate (domestic or treaty), its evidence and FTA fees, what residency means (no personal income tax, Corporate Tax only on business turnover above AED 1,000,000) and why a UAE visa does not end residency in another country. Use for UAE tax resident, Dubai tax residency, UAE residency certificate, 183 days UAE, moving to Dubai taxes, centre of vital interests UAE, leaving the UAE, Emirates ID and tax."
version: 2.0
jurisdiction: AE
tax_year: 2026
last_updated: 2026-11-14
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: situation-rules
---

# UAE tax residency for individuals, 2026

UAE tax residency matters for two things: whether the UAE will certify a person as resident for a double tax agreement (the certificate many people moving to Dubai need to stop being taxed at home), and the few UAE rules that turn on residence (Corporate Tax on a resident individual's business). It does **not** switch on any personal income tax: the UAE has none. The UAE income tax position of an individual, including business income, is in `ae-income-tax`; the wider system is in `ae-tax-overview`.

## Who this applies to

- Individuals moving to, living in, or leaving the UAE who need to know whether they are UAE tax resident in 2026, or need a tax residency certificate.
- Advisers in the other country checking whether a treaty tie-breaker can make the person resident in the UAE only.

Out of scope: companies' residence (Cabinet Decision No. 85 of 2022 Art. 3, see `ae-corporate-tax`); immigration rules for visas (each visa's conditions belong to the immigration authorities, not the FTA); the other country's exit rules.

## Rates, bands and thresholds

| Item | Figure, 2026 | Source |
| --- | --- | --- |
| Residency rules in force from | 1 March 2023 | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%2085%20of%202022%20-%20For%20publishing.pdf |
| Test 1: centre of life | Usual or primary place of residence and the centre of financial and personal interests in the UAE | same |
| Test 2: day count | Physically present 183 days or more within the relevant 12 consecutive months | same |
| Test 3: day count plus status and ties | Present 90 days or more within the relevant 12 consecutive months, and a UAE national, holder of a valid UAE Residence Permit or a GCC national, and has a Permanent Place of Residence in the UAE or carries on employment or business in the UAE | same |
| Personal income tax on wages, investment income and personal real estate income | None | https://tax.gov.ae/Datafolder/Files/Guides/CT/Taxation%20of%20natural%20persons%20-%2025%2011%202023.pdf |
| Corporate Tax for an individual in business | Applies only where business turnover exceeds AED 1,000,000 in a Gregorian calendar year | https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf |
| Corporate Tax rate on taxable income up to AED 375,000 | 0% | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf |
| Corporate Tax rate above AED 375,000 | 9% | https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf ; https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf |
| VAT standard rate (on consumption, not income) | 5% | https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf |
| TRC application fee, non-refundable | AED 50 | https://tax.gov.ae/Datafolder/Files/Legislation/2025/Cabinet%20Decision%20No.%2065%20of%202020%20on%20FTA%20Services%20Fees%20and%20its%20amendments%20-%20for%20publishing%20%2003%2012%202025.docx.pdf |
| TRC review and electronic certificate, applicant registered with the FTA | AED 500 | same |
| TRC review and electronic certificate, natural person not registered with the FTA | AED 1,000 | same |
| Printed copy of a TRC | AED 250 each | same |
| FTA response time to a complete TRC application | Generally 10 business days | https://tax.gov.ae/Datafolder/Files/Guides/VAT/VAT%20Guides/Tax-Resident-and-TRC--18-10-2024.pdf |

## The base

### The three tests

A natural person is UAE tax resident if they meet **any one** test (Cabinet Decision No. 85 of 2022, Art. 4):

1. **Centre of life.** Their usual or primary place of residence **and** the centre of their financial and personal interests are in the UAE. Usual residence is where they spend most of their time as part of a settled routine; the centre of interests looks at job, family and social ties, business, and where property is managed (Ministerial Decision No. 27 of 2023).
2. **183 days.** Physically present for 183 days or more within the relevant 12 consecutive months. What they did there does not matter.
3. **90 days.** Physically present for 90 days or more within the relevant 12 consecutive months, **and** a UAE national, a holder of a valid UAE Residence Permit or a GCC national, **and** either a Permanent Place of Residence in the UAE or employment or business carried on in the UAE.

### Counting rules (Ministerial Decision No. 27 of 2023)

- Any part of a day in the UAE counts as a full day, so travel days count. The days need not be consecutive.
- The FTA may disregard days spent in the UAE because of exceptional circumstances beyond the person's control that arose while they were in the UAE and stopped them leaving as planned.
- A Residence Permit does not include a temporary permit for travel, tourism, sport, medical treatment or a similar purpose.
- A Permanent Place of Residence is a furnished dwelling continuously available to the person, rented or owned; a place for occasional short stays does not qualify.
- Employment means a contract with a UAE employer for pay, or a continuing relationship in which all or substantially all of the person's income for their labour comes from one party for work in the UAE. Unpaid voluntary roles do not count.

### What UAE residency means for tax

| Income | UAE federal tax on the individual |
| --- | --- |
| Wages and employment income | None |
| Personal investment income (dividends, interest, gains on personal investments) | None |
| Rent from personal real estate investment without a licence | None |
| Business income under a licence or that needs one | Corporate Tax only if business turnover exceeds AED 1,000,000 in the calendar year (`ae-income-tax`) |
| Spending | VAT at 5% on most supplies |

Local fees charged by individual emirates on property (for example housing or municipality fees in rent) are not federal taxes and are outside this file.

## Deadlines and filing

- **Tax residency certificate:** apply on EmaraTax under "other services", then "Tax Residency Certificate". Two kinds: a **domestic** certificate, which applies the Art. 4 tests, and a **treaty** certificate for a named double tax agreement, which applies that treaty's residence article and names the other country (Cabinet Decision No. 85 of 2022 Art. 6; Ministerial Decision No. 247 of 2023).
- **Period:** a current or past period of no more than 12 months, never a future one. An individual can apply for the current period as soon as a test is met.
- **Evidence (FTA guide TPGTR1):** 183 days or more: Emirates ID and residence visa, or passport copy with an entry and exit report from the Federal Authority for Identity and Citizenship; 90 to 182 days: the same, plus proof of employment or business, or of a permanent home (certified tenancy contract or title deed with a utility bill); centre of life: identity evidence, a written statement with supporting documents, proof of the main home and of income.
- There is no UAE personal income tax return to file.

## Penalties and interest

There is no personal income tax, so no personal filing penalty. A certificate obtained on facts that turn out wrong or change can be withdrawn by the FTA. An individual whose business turnover passes AED 1,000,000 and who does not register for Corporate Tax faces the late registration penalty set out in `ae-income-tax`.

## Cross-border points

- **A UAE visa does not end residency anywhere else.** Each country applies its own rules. Many people move to Dubai, get a residence visa and remain tax resident at home (UK, EU, Australia, South Africa) on worldwide income because they have not broken ties under that country's rules.
- **To benefit from the UAE position:** cease residency in the prior country under its rules (see, for example, `leaving-south-africa-tax-emigration`); meet a UAE test; obtain a treaty certificate if the other country's tie-breaker is to be applied.
- **Treaty tie-breakers** look at permanent home, centre of vital interests, habitual abode and nationality in that order; the other country's tax authority examines the substance behind a UAE certificate.
- **Leaving the UAE:** there is no UAE exit tax for individuals. Residency simply stops being met on the tests for the relevant 12 months.

## Two worked examples that recompute

### Example 1: the 90-day test, decision to rely on it or on 183 days

An employee of a Dubai company with a valid UAE Residence Permit was in the UAE on 140 days in the 12 months to 31 December 2026, counting every part day.

- 183-day test: 140 is 43 days short, so it fails.
- 90-day test: 140 is 50 days over 90, she holds a Residence Permit, and she carries on employment in the UAE, so she is resident under test 3.
- Decision: apply for a domestic certificate on test 3, with employment evidence, rather than waiting to reach 183 days.

```oa-check
name: 90-day test margin, 140 days present in 12 months
inputs:
  days_present: 140
  test_183: 183
  test_90: 90
steps:
  - short_of_183: test_183 - days_present
  - over_90: days_present - test_90
expected:
  short_of_183: 43
  over_90: 50
```

### Example 2: a UAE resident freelancer in Corporate Tax

A resident freelancer with a licence has 2026 business turnover of AED 1,200,000 and taxable income of AED 500,000, and does not elect Small Business Relief.

- Turnover exceeds AED 1,000,000, so she is a Taxable Person for 2026.
- Corporate Tax: 0% on the first AED 375,000, 9% on AED 125,000: **AED 11,250**. Her salary from any other job and her personal investments stay untaxed.

```oa-check
name: Resident freelancer, taxable income AED 500,000
inputs:
  taxable_income: 500000
  band: 375000
  rate: 0.09
steps:
  - taxed_part: max(taxable_income - band, 0)
  - corporate_tax: taxed_part * rate
expected:
  taxed_part: 125000.00
  corporate_tax: 11250.00
```

## Ask the client first

1. How many days were you in the UAE (any part of a day counts) in the 12 months you care about?
2. Do you hold a valid UAE Residence Permit, UAE or GCC nationality?
3. Do you have a furnished home continuously available in the UAE, or a job or business here?
4. Where are your family, main home, work and assets?
5. Which other country might still treat you as resident, and have you taken the steps to leave its tax net?
6. Do you need a domestic certificate or one for a named treaty?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Cabinet Decision No. 85 of 2022: read for Arts 3 to 6 (residence tests for natural persons, TRC, international agreements) and the 1 March 2023 effective date | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%2085%20of%202022%20-%20For%20publishing.pdf | 2026-11-14 |
| Ministerial Decision No. 27 of 2023: read for the residency definitions (Permanent Place of Residence, employment, exceptional circumstances, day counting) | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Ministerial%20Decision%20No.%2027%20of%202023%20-%20for%20publishing.pdf | 2026-11-14 |
| FTA guide TPGTR1, Tax Resident and TRC: read for certificate types, periods, evidence and the 10 business day response | https://tax.gov.ae/Datafolder/Files/Guides/VAT/VAT%20Guides/Tax-Resident-and-TRC--18-10-2024.pdf | 2026-11-14 |
| Ministerial Decision No. 247 of 2023: read for the treaty tax residency certificate | https://mof.gov.ae/wp-content/uploads/2023/10/Ministerial-Decision-No247-of-2023-on-the-Issuance-of-Tax-Residency-Certificate-for-the-Purposes-of-International-Agreements.pdf | 2026-11-14 |
| Cabinet Decision No. 65 of 2020 and amendments (FTA fees), December 2025: read for items 6, 7, 9 and 10 (AED 50, 500, 1,000, 250) | https://tax.gov.ae/Datafolder/Files/Legislation/2025/Cabinet%20Decision%20No.%2065%20of%202020%20on%20FTA%20Services%20Fees%20and%20its%20amendments%20-%20for%20publishing%20%2003%2012%202025.docx.pdf | 2026-11-14 |
| FTA guide CTGTNP1, taxation of natural persons: read for wages, personal investment and real estate investment income outside Corporate Tax | https://tax.gov.ae/Datafolder/Files/Guides/CT/Taxation%20of%20natural%20persons%20-%2025%2011%202023.pdf | 2026-11-14 |
| Cabinet Decision No. 49 of 2023: read for Art. 2 (AED 1,000,000 turnover test) | https://tax.gov.ae/DataFolder/Files/Legislation/05-06-2023/3/Cabinet%20Decision%20No.%2049%20of%202023%20-%20for%20publishing.pdf | 2026-11-14 |
| Cabinet Decision No. 116 of 2022: read for Art. 3 (AED 375,000 band) | https://tax.gov.ae/Datafolder/Files/Legislation/Corporate%20Tax/Cabinet%20Decision%20No.%20116%20of%202022%20-%20for%20publishing.pdf | 2026-11-14 |
| Corporate Tax Law, consolidated January 2026: read for Art. 3 (9% rate) | https://mof.gov.ae/wp-content/uploads/2026/01/Federal-Decree-Law-No.-47-of-2022-and-its-amendments-en-v13.1.26.pdf | 2026-11-14 |
| VAT Law, consolidated November 2025: read for Art. 3 (5% standard rate) | https://tax.gov.ae/Datafolder/Files/Legislation/2025/Federal%20Decree-Law%20No.%208%20of%202017%20and%20amendments%20-%20publishing%2028%2011%202025.pdf | 2026-11-14 |

Not yet confirmed: visa types, durations and Golden Visa thresholds (immigration rules, not on an FTA or Ministry of Finance page opened today). The emirate-level property fee the earlier version cited for Dubai (4%). The treaty tie-breaker order is the OECD model order; each UAE treaty must be read for its own article.

> **Working paper only.** UAE tax residency for treaty purposes needs a certificate. Ceasing tax residency in another country needs compliance with that country's exit rules, not only a move to Dubai.
