---
name: my-company-formation
description: Use this skill whenever asked how to set up a company in Malaysia in 2026, choose between a sole proprietorship, partnership, LLP and Sdn Bhd, incorporate through the SSM Corporate Registry System (CRS), or keep a Malaysian private company compliant. Trigger on phrases like Sdn Bhd registration, incorporate company Malaysia, SSM, Companies Commission of Malaysia, CRS, MyCoID migration, company secretary Malaysia, annual return SSM, audit exemption Malaysia, Practice Directive 10/2024, resident director Malaysia. Covers the Companies Act 2016 minimums (one director ordinarily resident, a licensed secretary within 30 days), SSM fees (RM1,000 incorporation, RM150 annual return), financial statements timing, the phased audit exemption thresholds for 2025 to 2027, and the tax and payroll registrations after incorporation.
version: "2.1"
jurisdiction: MY
tax_year: 2026
tax_year_notes: "Rules and fees in force in 2026; audit exemption Phase 2 applies to financial periods starting in 2026."
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Malaysia company formation and entity choice, 2026

> **General reference only.** This skill is general reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to form a company or take a position without review by a qualified professional in Malaysia.

## Scope

How to form and keep compliant a Malaysian private company limited by shares (Sendirian Berhad, Sdn Bhd) under the Companies Act 2016, registered with the Companies Commission of Malaysia (SSM) through its Corporate Registry System (CRS). Phase 1 began on 14 July 2026 and moved incorporation from MyCoID to CRS. Other vehicles: public company (Berhad), limited liability partnership (PLT, LLP Act 2012), partnership and sole proprietorship (registered under the Registration of Businesses Act 1956). How each is taxed: `my-income-tax` (individuals and partners) and `my-corporate-income-tax` (companies).

## Ask the client first

1. **Who are the owners and directors**, and does at least one director have a principal place of residence in Malaysia?
2. **Activity**: does it need a licence or face foreign-ownership limits in its sector?
3. **Expected revenue, assets and staff** for the first years (audit exemption and SST, e-invoice and payroll registrations).
4. **Proposed name** and financial year end.
5. **Who will be company secretary** (must be licensed or a member of a listed body).

## The method, step by step

1. **Choose the vehicle.** A sole proprietor and individual partners are taxed on their business profits or allocated shares at the applicable individual rates; a Sdn Bhd is a separate taxpayer with limited liability; a PLT gives limited liability with partnership-style management.
2. **Choose a name route.** Use direct incorporation through CRS, which includes the name search, or reserve the name separately under s. 27 and file the incorporation within the reservation period.
3. **Incorporate** in CRS under s. 14 with the constitution (optional), director and shareholder details and consents. A private company needs at least one director (s. 196(1)), a natural person aged 18 or over (s. 196(2)), and the minimum number of directors must ordinarily reside in Malaysia without counting an alternate or substitute (s. 196(4)). One shareholder is enough, and may be the director.
4. **Appoint the first secretary within 30 days** of incorporation (s. 236(2)). The secretary must be a natural person, 18 or over, a citizen or permanent resident ordinarily residing in Malaysia (s. 235(1)), and licensed or a member of a body in the current Fourth Schedule (s. 235(2)). Obtain written consent and confirm SSM registration and a valid practising certificate. Notify SSM through CRS within 14 days of the appointment under s. 58(1)(d).
5. **Register for taxes and payroll.** Verify the corporate TIN and employer file with LHDN. File e-C annually. The 2026 filing programme also requires e-E and CP8D for dormant companies. Register for EPF, SOCSO and EIS when the employment rules apply (`my-pcb`, `my-epf-socso`). Check SST liability with RMCD if the applicable threshold is exceeded or another registration rule applies (`malaysia-sst`). Check e-invoicing separately (`malaysia-einvoice`). [LHDN registration](https://www.hasil.gov.my/syarikat/pendaftaran-fail-cukai/), [2026 filing programme](https://www.hasil.gov.my/media/02mbu5fw/program-memfail-bn-bagi-tahun-2026.pdf), [Service Tax Act s. 12](https://www.mysst.customs.gov.my/assets/document/SST%20Act/Service%20Tax%20Act%202018.pdf).
6. **Each year**: prepare financial statements (first within 18 months of incorporation, then within 6 months of the year end, s. 248); circulate them within 6 months of the year end (s. 258); lodge within 30 days of circulation (s. 259); lodge the annual return within 30 days of each incorporation anniversary, not in the year of incorporation (s. 68).
7. **Audit**: every private company appoints an auditor (s. 267(1)) unless exempt by the Registrar (s. 267(2)) under Practice Directive 10/2024 (see the table).

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| Incorporation, company limited by shares (s. 14) | RM1,000 | https://www.ssm.com.my/Pages/Services/Registration-of-Company-(ROC)/Table-of-Fees.aspx |
| Incorporation, company limited by guarantee | RM3,000 | https://www.ssm.com.my/Pages/Services/Registration-of-Company-(ROC)/Table-of-Fees.aspx |
| Separate name reservation (s. 27), for each 30 days or part thereof, up to 180 days | RM50 | https://www.ssm.com.my/Pages/Services/Registration-of-Company-(ROC)/Table-of-Fees.aspx |
| Change of name (s. 28) | RM100 | https://www.ssm.com.my/Pages/Services/Registration-of-Company-(ROC)/Table-of-Fees.aspx |
| Annual return, private company (s. 68) | RM150 | https://www.ssm.com.my/Pages/Services/Registration-of-Company-(ROC)/Table-of-Fees.aspx |
| Annual return, public company | RM500 | https://www.ssm.com.my/Pages/Services/Registration-of-Company-(ROC)/Table-of-Fees.aspx |
| Minimum directors, private company (s. 196(1)) | 1 | https://www.ssm.com.my/Pages/Legal_Framework/Document/Companies%20Act%202016_as%20at%2031%20January%202025.pdf |
| First secretary appointed within (s. 236(2)) | 30 days | https://www.ssm.com.my/Pages/Legal_Framework/Document/Companies%20Act%202016_as%20at%2031%20January%202025.pdf |
| Annual return due after the anniversary (s. 68(1)) | 30 days | https://www.ssm.com.my/Pages/Legal_Framework/Document/Companies%20Act%202016_as%20at%2031%20January%202025.pdf |
| Circulation of financial statements after year end (s. 258) | 6 months | https://www.ssm.com.my/Pages/Legal_Framework/Document/Companies%20Act%202016_as%20at%2031%20January%202025.pdf |
| Lodging after circulation (s. 259) | 30 days | https://www.ssm.com.my/Pages/Legal_Framework/Document/Companies%20Act%202016_as%20at%2031%20January%202025.pdf |
| Audit exemption, periods starting 1 Jan 2025 to 31 Dec 2025 (Phase 1): revenue / assets / employees | RM1,000,000 / RM1,000,000 / 10 | https://www.ssm.com.my/Pages/Legal_Framework/Document/NEW%20PD%2010-2024%20-%20Qualifying%20Criteria%20for%20Audit%20Exemption%20for%20Certain%20Categories%20of%20Private%20Companies%20(Portal).pdf |
| Audit exemption, periods starting in 2026 (Phase 2) | RM2,000,000 / RM2,000,000 / 20 | https://www.ssm.com.my/Pages/Legal_Framework/Document/NEW%20PD%2010-2024%20-%20Qualifying%20Criteria%20for%20Audit%20Exemption%20for%20Certain%20Categories%20of%20Private%20Companies%20(Portal).pdf |
| Audit exemption, periods starting from 1 Jan 2027 (Phase 3) | RM3,000,000 / RM3,000,000 / 30 | https://www.ssm.com.my/Pages/Legal_Framework/Document/NEW%20PD%2010-2024%20-%20Qualifying%20Criteria%20for%20Audit%20Exemption%20for%20Certain%20Categories%20of%20Private%20Companies%20(Portal).pdf |

An eligible private company must meet at least two of the three criteria across the current and two previous financial years, using the current period’s phase limits for all three. A company can also qualify under the dormancy rule if dormant since incorporation or in both the current and immediately preceding financial year. Check the exclusions in paragraph 12 and any qualifying written audit request from members or the Registrar under paragraph 14. Lodge unaudited statements with the audit exemption certificate and required reports. [SSM Practice Directive 10/2024](https://www.ssm.com.my/Pages/Legal_Framework/Document/NEW%20PD%2010-2024%20-%20Qualifying%20Criteria%20for%20Audit%20Exemption%20for%20Certain%20Categories%20of%20Private%20Companies%20(Portal).pdf), [SSM audit exemption FAQ](https://www.ssm.com.my/Pages/Legal_Framework/Document/PART%20Q%20%2819.5.2026%29.pdf).

## Worked cases

Case 1, audit exemption. A private company incorporated in 2024 has revenue of RM1.8 million, RM1.6 million and RM1.2 million for its 2026, 2025 and 2024 financial years. Assets are RM2.4 million and employee headcount at year end is 12 in each year. The 2026 period begins in 2026. Apply Phase 2 limits to all three years. Revenue meets the RM2 million limit in each year and headcount meets the 20-person limit. Assets exceed RM2 million in each year. The company meets two criteria and can elect audit exemption if no exclusion applies and no qualifying audit notice was received. [SSM audit exemption FAQ, Q23](https://www.ssm.com.my/Pages/Legal_Framework/Document/PART%20Q%20%2819.5.2026%29.pdf).

```oa-check
name: Audit exemption for a financial year starting in 2026
inputs:
  revenue_max: 1800000
  assets_max: 2400000
  staff_max: 12
steps:
  - revenue_ok: min(max(2000000 - revenue_max + 1, 0), 1)
  - assets_ok: min(max(2000000 - assets_max + 1, 0), 1)
  - staff_ok: min(max(20 - staff_max + 1, 0), 1)
  - criteria_met: revenue_ok + assets_ok + staff_ok
expected:
  criteria_met: 2
```

Case 2, incorporation fees. A new private company limited by shares uses a separate 30-day reservation in 2026. The prescribed fees for those two applications total RM1,000 + RM50 = RM1,050. Direct incorporation combines the name search and incorporation for a registration fee of RM1,000. The first ordinary private-company annual return is due within 30 days of its 2027 anniversary and costs RM150. Budget any separate financial-statement lodgement fees. [SSM fees](https://www.ssm.com.my/Pages/Services/Registration-of-Company-(ROC)/Table-of-Fees.aspx), [SSM incorporation steps](https://www.ssm.com.my/Pages/Register_Business_Company_LLP/Company/Submitting-Incorporation-Company.aspx).

```oa-check
name: Incorporation fees with a separate reservation
inputs:
  incorporation: 1000
  separate_name_reservation: 50
steps:
  - incorporation_and_reservation: incorporation + separate_name_reservation
expected:
  incorporation_and_reservation: 1050
```

## When to refuse or refer

| Code | Trigger | Message |
| --- | --- | --- |
| R-F-1 | Regulated or restricted sector (finance, telecoms, energy, distributive trade) | "This sector needs a licence or has ownership limits. Refer before incorporating." |
| R-F-2 | No director with a principal residence in Malaysia | "The Act requires the minimum number of directors to ordinarily reside in Malaysia. A resident director must be found first." |
| R-F-3 | Labuan entity or public company | "Out of scope; refer." |

## Filing and payment

| Filing | Where | When |
| --- | --- | --- |
| Incorporation and optional separate name reservation | SSM CRS | Before trading as the company |
| First secretary | Board resolution and notice to SSM through CRS | Appoint within 30 days of incorporation. Notify within 14 days after appointment |
| Annual return | SSM (MBRS) | Within 30 days of each anniversary, starting the calendar year after incorporation |
| Financial statements | SSM (MBRS) | Lodge within 30 days after circulation. Circulate within 6 months of year end, subject to any Registrar-approved extension |
| Income tax return | LHDN, Form e-C | See `my-corporate-income-tax` |

## Completion checklist

- Vehicle chosen with tax effect noted.
- Resident director and qualified secretary identified.
- Fees budgeted from the SSM table.
- Year end, first financial statements date and annual return date diarised.
- Audit exemption tested for each year with two-of-three criteria.
- LHDN, payroll, SST and e-invoice registrations listed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the SSM table of fees: incorporation, name reservation and change, annual return | https://www.ssm.com.my/Pages/Services/Registration-of-Company-(ROC)/Table-of-Fees.aspx | 2026-11-14 |
| Read for the Companies Act 2016 as at 31 January 2025: ss. 14, 68, 196, 235, 236, 248, 258, 259 and 267 | https://www.ssm.com.my/Pages/Legal_Framework/Document/Companies%20Act%202016_as%20at%2031%20January%202025.pdf | 2026-11-14 |
| Read for Practice Directive 10/2024: two-of-three criteria and the phased thresholds | https://www.ssm.com.my/Pages/Legal_Framework/Document/NEW%20PD%2010-2024%20-%20Qualifying%20Criteria%20for%20Audit%20Exemption%20for%20Certain%20Categories%20of%20Private%20Companies%20(Portal).pdf | 2026-11-14 |

| Current CRS company registration, optional name reservation and secretary appointment | https://www.ssm.com.my/Pages/Register_Business_Company_LLP/Company/Submitting-Incorporation-Company.aspx | 2026-11-22 |
| SSM annual returns and financial statements through MBRS | https://www.ssm.com.my/Pages/Register_Business_Company_LLP/Company/Annual-Submission.aspx | 2026-11-22 |
| Audit phase tests, prior years and newly incorporated companies | https://www.ssm.com.my/Pages/Legal_Framework/Document/PART%20Q%20%2819.5.2026%29.pdf | 2026-11-22 |
| Fourth Schedule update effective 30 October 2026, P.U. (A) 368/2026 | https://www.ssm.com.my/bm/Pages/Legal_Framework/document/PUA%20368_2026.pdf | 2026-11-22 |
| LHDN corporate and employer tax files | https://www.hasil.gov.my/syarikat/pendaftaran-fail-cukai/ | 2026-11-22 |
| LHDN 2026 filing programme and dormant-company e-E and CP8D | https://www.hasil.gov.my/media/02mbu5fw/program-memfail-bn-bagi-tahun-2026.pdf | 2026-11-22 |

Not yet confirmed: the client’s foreign ownership limits, sector-specific paid-up capital and licence conditions. SSM’s incorporation service charter targets one working day from complete payment. It does not set a statutory approval deadline. [SSM service charter](https://www.ssm.com.my/Pages/Legal_Framework/GUIDELINES/Guidelines-For-Incorporation-of-A-Local-Company.pdf).
