---
name: kz-formation
description: "Kazakhstan 2026 individual business registration: government notification, eligibility, regime election, company alternatives and Astana Hub boundaries."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/kz-formation"
  jurisdiction: "KZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Kazakhstan individual business registration v1.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

People choosing/registering an individual entrepreneur (ИП) business in Kazakhstan, with ТОО as the company alternative. A distinct non-ИП self-employed regime may be available under `kz-simplified-regime`; do not register someone unnecessarily before checking it. Corporate charter/capital work belongs to `kz-company-formation`. Liability, co-ownership, business risk, residence and actual eligibility decide the vehicle; “solo freelancer” alone is not enough.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| ИП notification service | Free through the government/eLicense notification service | https://www.gov.kz/services/3886?lang=ru |
| ИП registration basis | Notification of commencement under Tax Code art. 97; special-regime selection at registration under art. 716 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Change of ИП registration particulars | Notify within 10 working days; 10 in words on the page (art. 97) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| ТОО liability | Separate legal entity; participant risk generally limited to contributions, with statutory exceptions and unpaid-contribution exposure (LLP Law art. 2) | https://adilet.zan.kz/rus/docs/Z980000220_ |
| Astana Hub threshold condition | Tax Code art. 17 requires a registered participant legal entity and at least 90% qualifying priority ICT income, including specifically associated income counted under art. 17, plus own-production conditions when goods are produced/sold | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |

## The base

Before registration establish IIN/identity, residence/eligibility, actual activities/ОКЭД, ownership, employees, projected income and desired liability structure. ИП is personal entrepreneurship; ТОО is a separate legal entity. Partners/investors, liability protection and higher-risk operations call for the company analysis, not an automatic regime election.

For ИП use the government “Уведомление о начале деятельности в качестве индивидуального предпринимателя” service: open “Заказать онлайн”, enter eLicense, authenticate/register, choose the notification, complete the actual form fields and sign with ЭЦП. Track “Мои заявления” and retain the acknowledgement under “Мои уведомления”. The fee is free; do not promise instant/same-day completion or treat a draft screen as registration. Select a special regime only if eligible under `kz-simplified-regime`; otherwise the general regime applies under art. 716. Keep the accepted notification/status and activity codes.

After registration establish business-bank/recordkeeping arrangements, assess ККМ/ЭСФ obligations under `kz-bookkeeping`/`kz-einvoice`, and load `kz-payroll` if staff are engaged. VAT registration belongs to `kazakhstan-vat`: it can be compulsory on the general regime, while special-regime status cannot coexist with ordinary VAT registration. Do not recommend staying unregistered after the applicable trigger.

Astana Hub is a separate eligibility/registration exercise. The old promise that an ordinary freelance ИП automatically qualifies was incorrect: art. 17 describes a legal entity satisfying participant and qualifying-income conditions. Art. 738 contains different CIT, VAT, employee-tax and social-tax provisions, each subject to its own conditions. Do not promise a blanket CIT/ИПН/VAT/payroll exemption, presume accreditation or combine it with simplified taxation (art. 723 exclusion). Escalate the actual activity, contracts, accreditation and income mix for that assessment.

## Deadlines and filing

Keep notification/registration confirmation, identifiers, regime election and effective date before commencing the downstream filing setup. A newly formed legal entity chooses its special regime by notification no later than 5 working days after registration if eligible (art. 716; 5 in words on the page); an ИП chooses in the commencement notification. Refer late/missing elections and historic patent/retail transitions rather than assuming a cure. Tax and financial-reporting calendars are in the owning skills.

## Penalties and interest

Non-registration, invalid activity, wrong regime or late registration-data updates can create separate consequences. Do not quote an unconfirmed fee, penalty or completion guarantee.

## Cross-border points

Foreign founders/residents must establish their entitlement and documents, not assume “any nationality” is sufficient. Branches, representative offices and immigration/residence permissions require their own legal analysis. Registration does not by itself establish tax residence or treaty rights.

## Two worked examples that recompute

Case 1: hypothetical eligible solo business receives KZT 15,000,000 and expects KZT 3,000,000 allowable costs. Reviewed candidate simplified rate is 4% and general-regime lower band 10%, subject to owning-skill eligibility. Income-tax comparison is KZT 600,000 versus KZT 1,200,000; liability, VAT, contributions and customer deductibility can change the overall decision.

```oa-check
name: Vehicle and regime preliminary comparison
inputs:
  income: 15000000
  costs: 3000000
steps:
  - simplified: income * 0.04
  - general: (income - costs) * 0.10
  - difference: general - simplified
expected:
  simplified: 600000
  general: 1200000
  difference: 600000
```

Case 2: hypothetical proposed Astana Hub company has qualifying ICT income KZT 8,000,000 out of total KZT 10,000,000. Its ratio is 80%, short of the art. 17 condition by 10 percentage points. Incorporation/registration alone cannot establish the tax preference.

```oa-check
name: Astana Hub income-condition screen
inputs:
  qualifying: 8000000
  total: 10000000
steps:
  - ratio_percent: qualifying / total * 100
  - shortfall_points: max(90 - ratio_percent, 0)
expected:
  ratio_percent: 80
  shortfall_points: 10
```

## Ask the client first

- Individual/company, residence and legal registration entitlement?
- Liability, partners/investors and exact business activity?
- Income/costs, staff, customers, imports and VAT needs?
- IIN/ЭЦП, current notification/election and accepted status?
- For IT relief: actual participant/legal-entity status and qualifying income documents?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for ИП notification, signing, tracking and free service | https://www.gov.kz/services/3886?lang=ru | 2026-11-14 |
| Read for Tax Code arts. 17, 97, 99–101, 716, 723 and 738 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |
| Read for current LLP Law art. 2, ordinary browser | https://adilet.zan.kz/rus/docs/Z980000220_ | 2026-11-14 |

Not yet confirmed: Current guaranteed ИП processing time, alternative biometric/bank-app authentication channels and exact current portal fields; foreign-founder/residence restrictions; complete Astana Hub application/benefit tests. Old near-instant timing, minimal ТОО cost and blanket ИП IT-relief claims are not usable instructions.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `kz-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/kz-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
