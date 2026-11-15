---
name: mn-company-formation
description: "Source-cited draft: Mongolia company forms, capital tests, incorporation and ongoing compliance in 2026. Not reviewed by an accountant."
jurisdiction: MN
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
version: 0.1
type: situation-rules
---

# Mongolia Company Formation & Entity Choice

## Who this applies to

For choosing an ordinary Mongolian company form, preparing its registration and identifying ongoing obligations in 2026. This is not an approval for a regulated activity or a foreign state-owned investment. An LLC or JSC is a company; a foreign company's branch or representative office is a registered unit without separate legal personality, and the parent bears its obligations. A representative office is not a substitute for a trading licence. [Company Law arts. 3-7](https://legalinfo.mn/mn/detail?lawId=310).

**Quick reference:** there is no general domestic minimum capital under Company Law art. 30.4 unless another law sets one. Foreign-invested status has a separate ownership and investment test. Read the founders, funding and activities before quoting a capital requirement.

## Rates, bands and thresholds

| Rule and conditions | Amount or period | Official source |
| --- | --- | --- |
| Domestic LLC, absent a special sector law | No general statutory minimum capital; the charter fixes capital | Company Law arts. 30.4-30.5 [law](https://legalinfo.mn/mn/detail?lawId=310) |
| LLC at incorporation | At most 50 shareholders | Company Law art. 5.1 [law](https://legalinfo.mn/mn/detail?lawId=310) |
| Foreign-invested legal entity | Foreign ownership at least 25% in aggregate and investment of each foreign investor **more than USD 100,000**, or equivalent MNT; the native wording is “дээш” | Investment Law art. 3.1.5 [law](https://legalinfo.mn/mn/detail?lawId=9491) |
| Submission after founding decision | Within 30 days of the decision | Company Law art. 15.1 [law](https://legalinfo.mn/mn/detail?lawId=310) |
| Approved name | Apply for registration within 30 days; permitted extension up to 60 days; reapply if the approved name expires | Registration Law arts. 13.4-13.6 [law](https://legalinfo.mn/mn/detail?lawId=13591) |
| Complete ordinary registration application | Decision within 2 working days; foreign-invested legal entity within 5 working days, not a guaranteed bank/account-opening timeline | Registration Law art. 12.1 [law](https://legalinfo.mn/mn/detail?lawId=13591) |
| Required paper originals after an electronic approval, where applicable | Within 5 working days after the applicant receives the registration notification | Registration Law art. 12.4 [law](https://legalinfo.mn/mn/detail?lawId=13591) |
| Ordinary annual financial statements | 10 February after year end; full-IFRS entities also have the statutory half-year requirement by 20 July, and consolidated annual statements have a separate 1 March deadline | Accounting Act arts. 4, 10.3-10.5 [law](https://legalinfo.mn/mn/detail?lawId=11191) |

The domestic seed's MNT 100,000 minimum was unsupported and is not a legal requirement. The foreign-investment test does not say that only a foreign shareholder individually holding the ownership percentage must meet the investment test. Do not replace each investor's qualifying investment with a single company-wide deposit. Other laws, licences and the exact investment evidence still need review.

## The base

1. Choose LLC or JSC and document ownership, governance and activity. For a branch/representative office, identify the foreign parent and its authorised representative. Public/closed JSC rules differ from an LLC (Company Law arts. 3-7).
2. Use the state registration authority, the General Authority for State Registration: its [official gateway](https://burtgel.gov.mn) links legal-entity electronic services. Reserve the name and track both the name and founding-decision clocks.
3. Adopt the founding decision, charter and any required founders' agreement. Set capital, ownership and the founders' contribution deadlines in the founding documents (Company Law arts. 14-15, 30). A capital amount in a sample is not a statutory minimum.
4. Assemble the application and registration particulars: name, form, address, founders, capital, activities, duration where relevant, applicant and beneficial-owner information. Supply the decision, charter, agreement where applicable, authorised-agent evidence, payment evidence and address evidence (Registration Law arts. 14-16).
5. For foreign investment, obtain foreign identity/corporate documents, qualifying investment evidence such as transfer/bank, customs or intellectual-property evidence as applicable, and the required Mongolian translations (art. 16.2-16.4). The old temporary-bank-account sequence is not a universal instruction: establish the bank's current KYC and capital-transfer procedure first.
6. Submit the complete application, respond to a documented refusal or request, receive registration evidence and complete required original-document delivery. Statutory decision periods run from receipt of the required documents (art. 12), not from the first bank visit.
7. Establish accounting, tax and, if employing staff, payroll/social-insurance records. Reconcile registered activities and licences before trading. Do not treat entity registration as regulatory authorisation.

## Deadlines and filing

Financial reporting follows the applicable IFRS, IFRS for SMEs or public-sector standard category, not a blanket claim that every entity applies full IFRS. Records are accrual-based and generally in Mongolian and national currency; authorised foreign-currency books still report financial statements in MNT (Accounting Act arts. 4, 6-7). The reporting year is the calendar year; a new entity's first reporting period runs from registration to year end (art. 10). Prepare, approve and electronically submit statements with the responsible executive/accountant signatures under art. 9. [Accounting Act](https://legalinfo.mn/mn/detail?lawId=11191).

For corporate tax, previous-year taxable income determines quarterly or half-year returns, so quarterly filing is not universal. The rules operative before 2027 specify annual CIT filing by 10 February; the enacted amendment substitutes 5 March from 2027. The 2026 return filed in 2027 needs the authority's transition confirmation. Scheduled monthly CIT payments and quarterly settlement are separate from return frequency. Use [mn-corporate-income-tax](mn-corporate-income-tax.md), [mongolia-vat](mongolia-vat.md) and, if staff, [mn-payroll-social](mn-payroll-social.md). [CIT arts. 25-26](https://legalinfo.mn/mn/detail?lawId=14407); [amendment](https://legalinfo.mn/mn/detail?lawId=17438169665392&showType=1).

## Penalties and interest

Do not invent an incorporation fine, audit exemption or arrears rate. An incomplete/refused registration must be corrected under the stated reason and applicable registration procedure. Tax late-payment interest follows the current annual decision under [General Tax Law art. 73](https://legalinfo.mn/mn/detail?lawId=14403); obtain the notice and period before calculating it.

## Cross-border points

Foreign state-owned investment into mining, banking/finance or media/telecommunications can require permission under Investment Law art. 21. Foreign investment, employment/immigration permission, branch/PE treatment, tax residence and treaty protection are separate questions. Refer state-owned investors, regulated business and treaty/PE conclusions rather than promising unrestricted foreign ownership. [Investment Law arts. 3, 21](https://legalinfo.mn/mn/detail?lawId=9491); [Company Law art. 7](https://legalinfo.mn/mn/detail?lawId=310).

## Two worked examples that recompute

### Domestic founders choose capital

Assume an ordinary unregulated LLC's founders agree capital of MNT 2,000,000 split 60%/40%. Contributions are **MNT 1,200,000** and **MNT 800,000**, derived. This is their chosen capital, not a minimum. Record the contribution deadlines in the founding documents.

```oa-check
name: Domestic founders choose capital
inputs:
  capital: 2000000
  founder_a_percent: 60
steps:
  - founder_a: capital * founder_a_percent / 100
  - founder_b: capital - founder_a
expected:
  founder_a: 1200000
  founder_b: 800000
```

### Foreign-investment capital test

Assume each of 2 foreign investors contributes USD 125,000 and a domestic investor USD 250,000, total **USD 500,000**. Foreign ownership is **50%**, derived. Each foreign investment exceeds the statutory threshold, so these stated facts meet the capital/ownership definition. This does not grant a sector licence or other required permission.

```oa-check
name: Foreign-investment ownership and individual funding
inputs:
  foreign_a: 125000
  foreign_b: 125000
  domestic: 250000
steps:
  - total: foreign_a + foreign_b + domestic
  - foreign_percent: (foreign_a + foreign_b) / total * 100
  - each_foreign_percent: foreign_a / total * 100
expected:
  total: 500000
  foreign_percent: 50
  each_foreign_percent: 25
```

## Ask the client first

Obtain the form, proposed name, founders and beneficial owners, residency/nationality, any direct/indirect state ownership, activities and licences, address, capital split and each contribution's timing/evidence, founding-decision date, name-approval date, foreign-document translations, bank KYC requirements, planned staff and relevant accounting/reporting category.

## Sources

| Official source | Read for | Read date |
| --- | --- | --- |
| [Company Law](https://legalinfo.mn/mn/detail?lawId=310) | Read for arts. 3-7, 14-15 and 30-32: entity forms, founders, application timing and capital | 2026-11-15 |
| [Investment Law](https://legalinfo.mn/mn/detail?lawId=9491) | Read for arts. 3 and 21: foreign-investment definition and state-owned investment boundary | 2026-11-15 |
| [Legal Entities State Registration Law](https://legalinfo.mn/mn/detail?lawId=13591) | Read for arts. 12-16: complete applications, name reservation and foreign-investment documents; July amendment leaves the cited periods unchanged | 2026-11-15 |
| [Accounting Act](https://legalinfo.mn/mn/detail?lawId=11191) | Read for arts. 4, 6-7, 9-10 and 13: standards, currency, records, reporting periods and statements | 2026-11-15 |
| [Registration authority gateway](https://burtgel.gov.mn) | Read for agency identity and the public link to legal-entity electronic services, not an authenticated application | 2026-11-15 |
| [CIT Law](https://legalinfo.mn/mn/detail?lawId=14407) and [June amendment](https://legalinfo.mn/mn/detail?lawId=17438169665392&showType=1) | Read for arts. 25-26 and future annual-deadline commencement; detailed treatment in the corporate skill | 2026-11-15 |
| [General Tax Law](https://legalinfo.mn/mn/detail?lawId=14403) | Read for art. 73 late-payment interest framework | 2026-11-15 |

**Not yet confirmed:** current registration fees and live application fields; each bank's temporary-account/KYC/capital-deposit sequence; any registration practice accepting exactly the foreign-investment threshold despite the native “more than” wording; annual CIT transition instructions for the 2026 return submitted in 2027; entity-specific audit or licence obligations. Do not supply an unsourced fee or relax the statutory investment wording.
