---
name: bn-company-formation
description: "How to incorporate a private company (Sendirian Berhad, Sdn Bhd) in Brunei Darussalam in 2026 through the One Common Portal (OCP) of the Registry of Companies and Business Names (ROCBN). Covers entity choice, the minimum BND 25,000 authorised share capital, two to fifty shareholders, at least two directors with the ordinarily-resident rule, Form X and director consents, the register of controllers, payment, the certificate of incorporation, and the tax and TAP registrations that follow. Use for questions about company formation in Brunei, Sdn Bhd registration, ROCBN, OCP or setting up a business in Brunei."
version: 1.0
jurisdiction: BN
category: formation
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Brunei Company Formation and Entity Choice v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Founders setting up a business in Brunei Darussalam in 2026. Registration is with the Registry of Companies and Business Names (ROCBN), Ministry of Finance and Economy, on the One Common Portal (OCP), https://www.ocp.mofe.gov.bn. Company law: Companies Act (Chapter 39); business names: Business Names Act (Chapter 92).

**Choosing the vehicle**

| Vehicle | Tax | When |
|---|---|---|
| Sole proprietorship or partnership registered as a business name | No income tax on the business profit | Small local trade by citizens and residents; personal liability |
| Private company, Sendirian Berhad (Sdn Bhd) | Corporate income tax 18.5% after the section 35 threshold or new-company exemption ([bn-corporate-income-tax](bn-corporate-income-tax.md)) | Limited liability; foreign shareholders; contracts that require a company |
| Public company, Berhad (Bhd) | Same | Offering shares to the public |
| Branch of a foreign company | Same, on Brunei income | Foreign company trading without a subsidiary |

The worked tax comparison of sole proprietor against company is in [bn-income-tax](bn-income-tax.md).

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Minimum authorised share capital | BND 25,000 ("Companies in Brunei Darussalam must have a minimum of 25000 Authorised Share Capital") | 2026 | https://ocp.mofe.gov.bn/downloads/eServices%20User%20Guides%20-%20Companies%20PDF/01%20OCP_CM_ES_Incorporating%20a%20Private%20Company_UG%20v1.0.pdf |
| Shareholders, private company | At least 2, at most 50; individuals, registered companies or other incorporated entities; not bankrupt | 2026 | same |
| Directors, private company | At least 2 individuals, aged 18 or over, not bankrupt | 2026 | same |
| Ordinarily resident directors | With 2 directors, at least 1 Brunei ordinarily resident; with more than 2, at least 2 | 2026 | same |
| Business sector | One business sector per company | 2026 | same |
| Name | Must include "Sendirian Berhad" (Sdn Bhd); checked automatically for availability, restricted words and similarity | 2026 | same |
| Stamp duty on Memorandum and Articles and share certificates on incorporation | Not required from 4 May 2017 (Stamp Act (Amendment) Order 2017) | 2026 | https://www.mof.gov.bn/div_revenue_typesoftaxes_stampduty/ |
| TAP employer registration | Automatic on registration with ROCBN (companies registered before 2009 register in e-Amanah) | 2026 | https://www.tap.com.bn/employers-responsibilities |

## The base

What the OCP application needs, in the order the screens ask for it:

1. **General details:** proposed company name ending "Sdn Bhd", one business sector, authorised share capital of at least BND 25,000. If the name is similar to an existing one, upload consent to use it.
2. **Addresses:** one registered office address in Brunei.
3. **Directors:** at least 2 individuals with identification documents; upload the List of Directors (Form X), each director's Consent to Act as Director, ID evidence and, for green IC holders, evidence of ordinary residence. Non-Brunei nationals give a non-Brunei address.
4. **Shareholders:** 2 to 50, with number of shares; ID evidence for individuals, a board resolution for corporate shareholders (which must already be registered in OCP if a Brunei company).
5. **Register of controllers:** the individuals who ultimately control the company, with ID details.
6. **Review and declaration.**

## Deadlines and filing

**How to incorporate, step by step**

1. Create a personal OCP account (see OCP Resources and Guides, Getting Started).
2. On the OCP dashboard choose Incorporate a Private Company.
3. Complete General Details, Addresses, Directors, Shareholders and Register of Controllers as above, uploading the documents for each.
4. Review every section, tick the declaration and submit.
5. Pay: by credit card online, or note the Application ID and total and pay at the ROCBN counter. After payment the application goes to ROCBN for review, and an email "Submitted - Incorporate a Private Company" arrives with the receipt.
6. On approval the company shows under My Entities, and an email "Incorporation of a Private Company" attaches the Certificate of Incorporation and the Company Extract.
7. Then: open a bank account; in OCP register for income tax e-services; file estimated chargeable income within 3 months of the first accounting period end and the return by 30 June ([bn-corporate-income-tax](bn-corporate-income-tax.md)); register citizen and PR employees for SPK in e-Amanah ([bn-payroll-social](bn-payroll-social.md)).

Changes to a company's general details can be made in OCP after incorporation; ROCBN notifies the Revenue Division of a new registered office automatically.

## Penalties and interest

Penalties for late annual filings under the Companies Act are not covered on the pages read (see Not yet confirmed). For tax penalties see [bn-corporate-income-tax](bn-corporate-income-tax.md).

## Cross-border points

- Foreign individuals and foreign companies may be shareholders; a foreign corporate shareholder enters as "Other Incorporated Entity (Foreign)" with a resolution.
- Foreign directors are allowed, but the ordinarily resident rule above still has to be met (with 2 foreign directors and no local director, at least 1 ordinarily resident must be provided).
- Payments by the new company to foreign shareholders: dividends carry no Brunei withholding on the Revenue Division rate table; management fees, royalties and interest do ([bn-corporate-income-tax](bn-corporate-income-tax.md)).

## Two worked examples that recompute

**Example. Two founders, one Bruneian and one Singaporean, BND 25,000 authorised capital, 25,000 shares of BND 1.** Shares split 60:40 gives 15,000 and 10,000 shares. With 2 directors, 1 must be ordinarily resident in Brunei: the Bruneian founder meets it. Checks: shareholders 2 (within 2 to 50), capital at the BND 25,000 minimum.

```oa-check
name: Brunei Sdn Bhd, two founders, 60:40, BND 25,000 authorised
inputs:
  authorised: 25000
  par: 1
  share_a: 0.6
steps:
  - shares_total: authorised / par
  - shares_a: shares_total * share_a
  - shares_b: shares_total - shares_a
  - capital_shortfall: max(25000 - authorised, 0)
expected:
  shares_a: 15000
  shares_b: 10000
  capital_shortfall: 0
```

## Ask the client first

1. Sole proprietorship, partnership or company? Will there be foreign owners?
2. Who are the directors, and how many are Brunei ordinarily resident?
3. How many shareholders, individuals or companies?
4. What single business sector will the company register under?
5. Will it employ Brunei citizens or permanent residents (SPK)?

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| ROCBN, OCP user guide "Incorporating a Private Company" v1.0 (PDF, 49 pages) | Read for each screen of the application, the BND 25,000 authorised capital minimum, director and shareholder rules, documents, payment and the certificate | https://ocp.mofe.gov.bn/downloads/eServices%20User%20Guides%20-%20Companies%20PDF/01%20OCP_CM_ES_Incorporating%20a%20Private%20Company_UG%20v1.0.pdf | 2026-11-14 |
| Revenue Division, types of taxes: stamp duty | Read for the removal of stamping of Memorandum, Articles and share certificates on incorporation from 4 May 2017 | https://www.mof.gov.bn/div_revenue_typesoftaxes_stampduty/ | 2026-11-14 |
| Revenue Division, types of taxes: income tax | Read for OCP registration of income tax payers and the automatic address update from ROCBN | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ | 2026-11-14 |
| Revenue Division, FAQ corporate tax | Read for no tax on business names (sole proprietorships and partnerships) | https://www.mof.gov.bn/div_revenue_faq_corporatetax/ | 2026-11-14 |
| TAP, employers' responsibilities | Read for automatic TAP registration on ROCBN registration | https://www.tap.com.bn/employers-responsibilities | 2026-11-14 |

Not yet confirmed: ROCBN incorporation and name fees (shown only on the OCP payment screen, not in the guide); the processing time (the old file's 2 to 4 weeks came from a private website and is removed); company secretary requirement; annual return, AGM, audit and audit exemption rules under the Companies Act (Chapter 39), whose text did not open on agc.gov.bn; branch registration steps for foreign companies.
