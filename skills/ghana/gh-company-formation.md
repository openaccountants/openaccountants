---
name: gh-company-formation
description: >
  Use this skill to choose an entity and register a business in Ghana in 2026: entity types, Office of the Registrar of Companies steps, forms, fees, 1% capital duty, beneficial ownership, annual returns, the Ghana Investment Promotion Authority Act, 2026 (Act 1173) minimum foreign capital for trading enterprises, tax registration and the first tax dates. Trigger on "register a company in Ghana", "ORC Ghana", "foreign company Ghana", "GIPC minimum capital", "annual returns Ghana", "external company Ghana". Tax computations sit in the other Ghana skills.
version: 0.2
jurisdiction: GH
category: formation
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ghana Company Formation and Entity Choice v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone setting up in Ghana in 2026. Authority: Office of the Registrar of Companies (ORC), under the Companies Act, 2019 (Act 992). Foreign investors also deal with the Ghana Investment Promotion Centre under Act 1173. Entity types on the ORC site: company limited by shares, by guarantee, unlimited company, external company, sole proprietorship or business name, partnership, each public or private where relevant.

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Company limited by shares, registration | GHS 585 | Includes constitution, Form 3, BO profile | 2026 | https://orc.gov.gh/fees.php |
| Company limited by guarantee | GHS 490 | | 2026 | same |
| Business name or sole proprietorship | GHS 130 | | 2026 | same |
| Partnership | GHS 270 | | 2026 | same |
| External company | USD 1,400, cedi equivalent | Foreign company operating in Ghana | 2026 | same |
| Capital duty | 1% of stated capital | | 2026 | same |
| Prestige service, companies | GHS 1,300 additional | Optional | 2026 | same |
| Annual return | GHS 175 | Service page shows GHS 100; 2026 schedule followed | 2026 | same |
| Renewal, business name | GHS 70 | Yearly | 2026 | same |
| Renewal, partnership | GHS 100 | Yearly | 2026 | same |
| Late annual returns | GHS 1,000 (1 to 4 years); GHS 2,000 (5 years and above) | | 2026 | same |
| Beneficial ownership not filed | GHS 500 | Penalty | 2026 | same |
| Foreign capital, trading | USD 500,000 | Wholly foreign, joint venture, or Ghanaian-owned with a foreign owner or director | 2026 | https://gipc.gov.gh/minimum-equity-requirements/ |
| Skilled Ghanaians, trading | At least 75% | Trading enterprise | 2026 | same |

## The base

Act 1173 limits the minimum foreign capital to trading enterprises, paid in cash as equity. Trading means buying and reselling goods. Enterprises outside trading have no general minimum, though sector rules can apply. The old USD 200,000, 500,000 and 1,000,000 tiers no longer apply. Portfolio investment is outside it.

Capital duty is on stated capital. A limited company limits liability and can raise equity, and carries annual returns and an auditor. A sole proprietor costs least and may use the [Modified Taxation Scheme](ghana-pit.md). An external company is a foreign company's presence in Ghana.

## Deadlines and filing

Incorporation steps ([ORC](https://orc.gov.gh/service-incorporation-of-company-limited-by-shares.php), [forms](https://orc.gov.gh/forms.php)). The page read is for a public company; the private pack carries Form 3 in place of Form 3C.

1. Search the name at ORC.
2. Complete the company form pack.
3. Get a consent letter from a licensed chartered accountant of ICAG as auditor.
4. Directors each sign a statutory declaration and consent; the secretary signs a consent.
5. Give stated capital details and beneficial ownership information.
6. Submit at the Company Registration Counter for verification and capture.
7. Pay GHS 585 at the in-house bank, and capital duty.
8. Receive the Certificate of Incorporation, certified constitution, certified form and BO profiles.

Then register for tax with the certificate, owners' or directors' Ghana Cards, location details and financial statements ([GRA](https://gra.gov.gh/domestic-tax/tax-registration/)), and activate ETAX. Register staff with SSNIT. Service providers register for VAT within 30 days ([ghana-vat](ghana-vat.md)).

Annual returns with financial statements: first after 18 months of incorporation, then every year ([ORC](https://orc.gov.gh/service-incorporation-of-company-limited-by-shares.php)). Collect the form, submit it signed at the Annual Returns Counter and pay ([ORC](https://orc.gov.gh/service-annual-returns.php)). Income tax dates are in [gh-corporate-income-tax](gh-corporate-income-tax.md).

## Penalties and interest

Late annual returns and missing beneficial ownership filings carry the ORC amounts in the table above.

## Cross-border points

Foreign investors open foreign and local corporate accounts, transfer the capital bank to bank and have the Bank of Ghana confirm it. Physical cash needs Bank of Ghana Form T5 on arrival ([GIPC](https://gipc.gov.gh/minimum-equity-requirements/)). A branch pays 8% on repatriated profit ([gh-cross-border](gh-cross-border.md)).

## Two worked examples that recompute

**Example 1: registration cost.** Stated capital GHS 100,000. Fee 585 plus 1% duty of 1,000: GHS 1,585.

```oa-check
name: Registration at 100,000 capital
inputs:
  capital: 100000
steps:
  - duty: capital * 0.01
  - total: duty + 585
expected:
  total: 1585.00
```

**Example 2: is the capital requirement needed?** A foreign software consultancy resells nothing, so it is not trading and the USD 500,000 does not apply. A foreign importer reselling goods with USD 300,000 of cash equity is USD 200,000 short.

```oa-check
name: Trading capital shortfall
inputs:
  equity: 300000
steps:
  - short: max(500000 - equity, 0)
expected:
  short: 200000.00
```

## Ask the client first

1. Will the business buy and resell goods.
2. Any non-Ghanaian owner or director.
3. Stated capital.
4. Public or private, and how many directors.
5. Existing foreign parent.

## Sources

| Source | URL | Read on |
|---|---|---|
| Office of the Registrar of Companies, Fees (2026), page read in full | https://orc.gov.gh/fees.php | 2026-11-01 |
| ORC, Incorporation of Company Limited by Shares (public company page), page read in full | https://orc.gov.gh/service-incorporation-of-company-limited-by-shares.php | 2026-11-01 |
| ORC, Annual Returns service page, page read in full | https://orc.gov.gh/service-annual-returns.php | 2026-11-01 |
| ORC, Forms, page read in full | https://orc.gov.gh/forms.php | 2026-11-01 |
| GIPC, Minimum Foreign Capital Requirements (Act 1173), page read in full | https://gipc.gov.gh/minimum-equity-requirements/ | 2026-11-01 |
| GRA, Tax Registration page, page read in full | https://gra.gov.gh/domestic-tax/tax-registration/ | 2026-11-01 |

Not yet confirmed: (1) Act 992 itself was not opened. Minimum directors for a private company and a resident director (old skill: two, one resident), and minimum stated capital (old skill: about GHS 500 for Ghanaian-owned companies, from a US trade page) are not confirmed; ORC confirms two directors for a public company only. (2) Typical timeline of 10 to 15 working days came from a private firm blog and is not confirmed. (3) Whether the ORC online platform replaces any counter step. (4) Name-search fee.

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
