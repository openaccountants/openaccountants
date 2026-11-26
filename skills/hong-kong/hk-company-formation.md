---
name: hk-company-formation
description: "Use this skill to set up a Hong Kong private company limited by shares in 2026 (year of assessment 2026/27) and keep it compliant. It covers entity choice, the one-stop incorporation and business registration with the Companies Registry and IRD (HKD 1,545 electronic incorporation fee, HKD 2,350 one-year business registration fee and levy from 1 April 2026), director and company secretary rules, the annual return within 42 days of the anniversary (HKD 105 on time), business registration renewal and audited accounts. Built from the law, not reviewed by an accountant."
jurisdiction: HK
tax_year: 2026
tax_year_notes: "Calendar 2026 and year of assessment 2026/27. Business registration fee and levy for 1 April 2026 to 31 March 2027."
version: "2.1"
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: formation
type: filing-howto
---

# Hong Kong company formation and annual compliance (2026)

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file or act on it without review by a qualified professional in Hong Kong.

## Scope

The most common vehicle is a private company limited by shares incorporated under the Companies Ordinance (Cap. 622) and administered by the Companies Registry (CR), with a Business Registration Certificate from the Inland Revenue Department (IRD) issued together with the Certificate of Incorporation under the one-stop service. Other forms: public company, company limited by guarantee, sole proprietorship, partnership, and a registered non-Hong Kong company (branch). A private company limited by shares may be wholly foreign-owned. Profits tax: `hk-corporate-income-tax`. MPF for staff: `hk-mpf`.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Incorporation fee, local company with share capital, electronic | HKD 1,545 | Includes a non-refundable lodgment fee of HKD 265 | https://www.cr.gov.hk/en/faq/local-company/incorporation.htm |
| Incorporation fee, hard copy | HKD 1,720 | Includes a non-refundable lodgment fee of HKD 295. The HKD 1,425 registration fee is refundable if the application is unsuccessful | same |
| Certificate issue time, private company limited by shares | Normally within 1 hour (electronic), or within 4 working days (hard copy) | Count from delivery. The electronic turnaround assumes no further name review and successful validation | same |
| Directors | At least one director who is a natural person | Private company; the sole director must not also be the company secretary | same |
| Company secretary | Required. An individual must ordinarily reside in Hong Kong. A body corporate must have its registered or principal office there | A private company with one director must not have a body corporate secretary whose sole director is that director | same |
| Business registration fee and levy, 1-year certificate | HKD 2,350 (fee 2,200, levy 150) | 1 April 2026 to 31 March 2027. For a local company's first certificate, use the incorporation submission date. For renewals, use the renewal certificate start date | https://www.ird.gov.hk/eng/pdf/brfee_table.pdf |
| Business registration, 3-year certificate | HKD 6,170 (fee 5,720, levy 450) | Same | same |
| Business registration for a new business | Within one month of commencement | Non-company businesses register with the Business Registration Office | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf |
| Change or cessation of business particulars | Notify within one month | Unless covered by the one-stop change notification | same |
| Annual return (NAR1), private company | HKD 105 if delivered within 42 days after the anniversary of incorporation | Late fees from the anniversary: HKD 870 through 3 months, HKD 1,740 through 6 months, HKD 2,610 through 9 months and HKD 3,480 thereafter | https://www.cr.gov.hk/en/compliance/annual-return/private-company.htm |

## Ask the client first

1. Who the shareholders and directors are, and whether one is a natural person.
2. Who will act as company secretary (Hong Kong resident individual or Hong Kong body corporate).
3. The registered office address in Hong Kong.
4. The business to be carried on and whether it starts at once (business registration date).
5. Whether the business needs a licence from a sector regulator.
6. Who will audit the accounts and file the profits tax return.

## The method, step by step

1. **Choose the vehicle.** Limited company for liability protection and the two-tiered profits tax rate (`hk-corporate-income-tax` compares sole proprietor and company). No minimum share capital is required; companies are often formed with one share (no par value regime under Cap. 622).
2. **Reserve nothing; check the name** on the CR's search before filing.
3. **File the incorporation form (NNC1)** through the CR e-Services Portal with the Notice to Business Registration Office (IRBR1). Pay the electronic incorporation fee of HKD 1,545 and the business registration fee and levy of HKD 2,350 for a one-year certificate if the submission date falls in 2026/27.
4. **Receive** the Certificate of Incorporation and Business Registration Certificate together, normally within an hour for electronic filings.
5. **After incorporation:** keep the required registers, including the significant controllers register (Part 12, Division 2A), at the registered office or another permitted location. File IR56E within 3 months for employees likely to be chargeable to salaries tax. Enrol regular employees covered by MPF within 60 days and check the separate casual employee rules (`hk-mpf`).
6. **Every year:** file the annual return within 42 days after the anniversary of incorporation (HKD 105); renew the business registration certificate (annually or every three years); prepare audited financial statements and file the profits tax return (`hk-corporate-income-tax`).

### Boundary and exception table

| Situation | Rule |
| --- | --- |
| Dormant company | A private company that becomes statutorily dormant under Cap. 622 s. 5 by delivering its special resolution to the Registrar can qualify for the audited financial statement exception |
| Company, whether trading or not | Deemed to carry on business: must hold business registration until dissolved or deregistered |
| Internet business with servers abroad | Must register if daily operations are carried out in Hong Kong |
| Business not yet started | The IRD will not register a business that has never existed or has not commenced (non-company businesses) |
| Foreign company with a place of business in Hong Kong | Register as a non-Hong Kong company within 1 month of establishing the place of business under Cap. 622 s. 776 |

## Worked cases

**Setting up a company electronically in June 2026.** Incorporation fee HKD 1,545 plus one-year business registration fee and levy HKD 2,350 = HKD 3,895 paid at filing. The first annual return falls due within 42 days after the first anniversary (June 2027) at HKD 105 if on time; a late return costs HKD 870 or more, rising with lateness to HKD 3,480.

```oa-check
name: HK 2026 incorporation fees and first annual return
inputs:
  incorporation: 1545
  br_one_year: 2350
  ar_on_time: 105
steps:
  - setup_total: incorporation + br_one_year
  - total_with_first_annual_return: setup_total + ar_on_time
expected:
  setup_total: 3895
  total_with_first_annual_return: 4000
```

## When to refuse or refer

- Licensed businesses (banking, insurance, securities, money services, trust or company service providers) need the sector regulator's licence: refer.
- Nominee or "shelf" structures meant to hide the significant controllers: refuse.
- For Mainland China operations, check the applicable entity and licensing requirements in `cn-formation`.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Companies Registry FAQ, incorporation of local companies. Read for the HKD 1,545 and 1,720 fees, issue times, director and secretary rules | https://www.cr.gov.hk/en/faq/local-company/incorporation.htm | 2026-11-14 |
| Companies Registry e-Services FAQ, electronic issue time and validation conditions | https://www.cr.gov.hk/en/electronic/e-servicesportal/faq/business-registration.htm | 2026-11-26 |
| Companies Registry, annual return for local private companies. Read for the 42-day rule, HKD 105 and the late fees | https://www.cr.gov.hk/en/compliance/annual-return/private-company.htm | 2026-11-14 |
| IRD, business registration fee and levy table (PDF). Read for the 2026/27 one-year and three-year amounts | https://www.ird.gov.hk/eng/pdf/brfee_table.pdf | 2026-11-14 |
| IRD, A brief guide to taxes 2025/26 (PDF). Read for business registration within one month, the one-stop service, deemed business of companies and change notices | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf | 2026-11-14 |
| IRD, block extension letter 2025/26 (PDF). Read for audited financial statements with profits tax returns and the dormant company exception | https://www.ird.gov.hk/eng/pdf/bel26e.pdf | 2026-11-14 |
| Companies Registry, significant controllers register obligations and location | https://www.cr.gov.hk/en/legislation/scr/faq.htm | 2026-11-26 |
| Companies Registry, registration of non-Hong Kong companies | https://www.cr.gov.hk/en/faq/non-hk-company/registered.htm | 2026-11-26 |
| IRD, employer notifications and IR56E deadline | https://www.ird.gov.hk/eng/tax/ere_obl.htm | 2026-11-26 |
| MPFA, employer enrolment requirements | https://www.mpfa.org.hk/en/info-centre/faq/employer/mpf-employer | 2026-11-26 |

Not yet confirmed: sector and Mainland registration requirements for a specific business without its activity and place of operation.
