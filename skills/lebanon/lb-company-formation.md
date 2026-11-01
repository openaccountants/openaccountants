---
name: lb-company-formation
description: "Company formation and entity choice in Lebanon, tax year 2026. Sources and unverified rows are marked per row."
version: 1.1
jurisdiction: LB
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lebanon Company Formation and Entity Choice

Companies are registered with the Commercial Registry at the relevant court; capital requirements and a Lebanese-lawyer retainer apply to SAL/SARL. Figures should be confirmed against current Commercial Registry fee schedules.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Holding and offshore taxes | see corporate income tax | 2026 | https://www.investinlebanon.gov.lb/en/doing_business/tax_system |
| Overview of entity types | The Lebanese Code of Commerce provides for several company forms; the joint-stock company (SAL) and limited-liability company (SARL) are the most common vehicles for business, alongside partnerships and the holding/offshore regimes. | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Lebanese Code of Commerce |
| Limited liability company (SARL) | Société à Responsabilité Limitée : members' liability limited to capital contributions | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Lebanese Code of Commerce |
| Joint-stock company (SAL) | Société Anonyme Libanaise : shareholding company, minimum 3 shareholders | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Lebanese Code of Commerce |
| Holding and Offshore companies | Special SAL regimes governed by Decree-Law No. 45 and No. 46 of 1983 with preferential tax treatment | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Decree-Law No. 45 of 1983 (Holding) |
| Sole proprietorship / partnership | Individual trader or general partnership taxed under personal business-income rules (4%-25%) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Lebanese Code of Commerce |
| Minimum share capital : SARL | LL 5,000,000 (approx : nominal statutory figure; confirm current requirement) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Lebanese Code of Commerce |
| Minimum share capital : SAL | LL 30,000,000 (approx : nominal statutory figure; confirm current requirement) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Lebanese Code of Commerce |
| Minimum shareholders : SAL | 3 shareholders | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Lebanese Code of Commerce |
| Registration authority | Commercial Registry at the competent first-instance court | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Lebanese Code of Commerce |
| Mandatory lawyer retainer | SAL/SARL must retain a Lebanese lawyer (annual retainer) as a registration condition (approx : confirm thresholds requiring a retainer) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Law Regulating the Legal Profession |
| Typical incorporation timeline | Approximately 2 to 4 weeks (approx : confirm current timeline) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; IDAL |
| Core annual compliance | Audited financial statements, annual income tax return, payroll declarations, quarterly VAT returns (if registered), and NSSF declarations | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Income Tax Law (Decree-Law No. 144 of 1959) |
| Statutory auditor | SAL must appoint a statutory auditor; SARL above thresholds also require one (approx : confirm SARL audit thresholds) | 2026 | unverified: Ministry of Finance site showed a CAPTCHA, law text not opened; Lebanese Code of Commerce |

## Two worked examples that recompute

Entity choice: an SAL or SARL pays 17% on profit; a holding pays no income tax on profits, so a holding only fits if its activity is holding. On LL 1,000,000,000 of operating-style profit the SAL figure is below. Second case: 15% on a LL 200,000,000 gain on fixed assets.

```oa-check
name: SAL tax on profit
inputs:
  profit: 1000000000
steps:
  - tax: profit * 0.17
expected:
  tax: 170000000
```

```oa-check
name: Gain on fixed assets
inputs:
  gain: 200000000
steps:
  - tax: gain * 0.15
expected:
  tax: 30000000
```

## Sources

| Source | URL | Read on |
|---|---|---|
| IDAL, Doing Business, Tax System (whole page) | https://www.investinlebanon.gov.lb/en/doing_business/tax_system | 2026-11-01 |
| Ministry of Finance, finance.gov.lb tax pages | unverified: CAPTCHA, not read | not read |

Not yet confirmed: every row marked unverified. finance.gov.lb returned a CAPTCHA during this refresh, which we did not solve; only archive indexes of it were read, and the text of 2026 Budget Law No. 40 of 10 Feb 2026 was not opened (the law number comes from a search summary, not an official page). Citizen Budget wording covers measures only, so anything else in that law is unread.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
