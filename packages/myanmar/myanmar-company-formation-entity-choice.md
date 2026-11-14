---
name: myanmar-company-formation-entity-choice
description: "How to form a company in Myanmar in 2026 under the Myanmar Companies Law 2017 through DICA's online MyCO system, and which entity to choose. Covers private and public companies limited by shares, overseas corporations (branches), the 35% foreign ownership line, one shareholder and one director with an ordinarily resident director, no minimum capital, MyCO filing fees (Form A-1 300,000 kyats, annual return 50,000 kyats), payment, then IRD taxpayer registration, commercial tax registration and SSB. Use for questions about company formation in Myanmar, DICA, MyCO, Form A-1, foreign company status or setting up a business in Myanmar."
version: 1.0
jurisdiction: MM
category: formation
tax_year: 2026
tax_year_notes: "FY 2026-27, 1 April 2026 to 31 March 2027"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
type: filing-howto
---

# Myanmar Company Formation and Entity Choice v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Founders and foreign investors setting up a business in Myanmar in 2026. Companies are incorporated under the Myanmar Companies Law 2017 with the Directorate of Investment and Company Administration (DICA), online through MyCO (https://www.myco.dica.gov.mm). Tax registration follows with the Internal Revenue Department (IRD).

**Choosing the vehicle**

| Vehicle | Form and fee | When |
|---|---|---|
| Private company limited by shares | Form A-1, 300,000 kyats | Most businesses; 1 shareholder and 1 director allowed |
| Public company limited by shares | Form A-2, 2,500,000 kyats | Offering shares to the public; at least 3 directors |
| Company limited by guarantee | Form A-3, 300,000 kyats | Non-profit purposes |
| Overseas corporation (branch of a foreign company) | Form A-8, 300,000 kyats | A foreign company trading in Myanmar without a subsidiary |
| Sole proprietorship or partnership | Not registered with DICA | Small local business; the owner is taxed as an individual ([mm-income-tax](mm-income-tax.md)) |

Companies pay income tax at 22% ([mm-corporate-income-tax](mm-corporate-income-tax.md)); individuals pay 0% to 25% after reliefs.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Foreign ownership | A company stays a Myanmar company with foreign ownership up to 35%; above that it is a foreign company; changes in foreign status must be notified to DICA | 2026 | https://www.dica.gov.mm/doing-business/register-your-company/ |
| Shareholders and directors | A single shareholder and a single director are allowed | 2026 | same |
| Ordinarily resident director | Every company needs at least one director ordinarily resident in Myanmar (permanent resident, or in Myanmar at least 183 days in each 12-month period from incorporation) | 2026 | same |
| Public company directors | At least 3, one a Myanmar citizen ordinarily resident in Myanmar | 2026 | same |
| Minimum capital | No minimum capital to incorporate | 2026 | same |
| Form A-1, private company limited by shares | 300,000 kyats | 2026 | https://www.myco.dica.gov.mm/public/fees.aspx |
| Form A-2, public company | 2,500,000 kyats | 2026 | same |
| Form A-8, overseas corporation | 300,000 kyats | 2026 | same |
| Form AR, annual return | 50,000 kyats | 2026 | same |
| Annual return late fee | 100,000 kyats | 2026 | same |
| Late filing fees, other forms | 25,000 kyats (1 to 90 days); 50,000 kyats (91 to 180 days) | 2026 | same |
| Change of company name (Form C-2) | 100,000 kyats | 2026 | same |
| Change of registered office (Form C-4) | 30,000 kyats | 2026 | same |
| Company extract | 10,000 kyats | 2026 | same |

## The base

What the MyCO application collects (DICA how-to):

1. Company name and type.
2. Registered office address.
3. Directors and secretary (if any), with a copy of the national registration card (NRC) for Myanmar citizens or the passport for foreigners.
4. Share capital structure and all shareholders; if an ultimate holding company controls the company, its details.
5. The constitution (the model constitution or the company's own).

## Deadlines and filing

**How to incorporate, step by step**

1. Create a MyCO account; the first user becomes the account security administrator and can add directors and secretaries as users.
2. Choose "Register a New Company" and the form for the company type (Form A-1 for a private company limited by shares).
3. Complete the form, upload the ID documents, and pay the fee by credit card or MPU card online, or save the draft and pay cash at a DICA office (the payment credits the account; then submit from Active Filings).
4. Submit to the Registrar for review. On approval, download the electronic certificate of incorporation.
5. **IRD registration:** register on the IRD e-Registration system to get a taxpayer identification number (TIN), then use e-Filing and e-Payments (IRD notice, 28 April 2026). The IRD companies page also has the company contact the Large Taxpayer Office or a Medium Taxpayer Office with the electronic registration certificate.
6. **Commercial tax:** register with the Township Revenue Officer if taxable proceeds will exceed 50 million kyats a year or if the company wants to set off CT ([myanmar-ct](myanmar-ct.md)).
7. **SSB:** register workers with the Social Security Board ([mm-payroll-social](mm-payroll-social.md)).
8. **Each year:** file the annual return on MyCO (Form AR, 50,000 kyats); file the income tax return and annual CT return by 30 June.

## Penalties and interest

Late annual return: 100,000 kyats late fee on MyCO; other late filings 25,000 or 50,000 kyats by delay. Tax penalties: [mm-corporate-income-tax](mm-corporate-income-tax.md).

## Cross-border points

- Foreign shareholders may own up to 35% without the company becoming a foreign company; a foreign company may face sector restrictions under the investment rules (not covered here).
- A company formed in Myanmar with any foreign shareholders is a resident for income tax and taxed on worldwide income.
- A foreign company may instead register an overseas corporation (Form A-8).
- Transfers of shares between local and foreign shareholders are not restricted, but a change of foreign status must be notified to DICA.

## Two worked examples that recompute

**Example. Myanmar founder and a Thai investor, 1,000,000 shares, Thai investor takes 30%.** Foreign ownership 30% is not more than 35%: the company stays a Myanmar company. Incorporation fee Form A-1 300,000 kyats; first annual return 50,000 kyats. If the Thai investor later goes to 40%, foreign ownership exceeds 35% and DICA must be notified.

```oa-check
name: Myanmar company, 30% foreign shareholding, fees
inputs:
  shares: 1000000
  foreign_pct: 0.30
steps:
  - foreign_shares: shares * foreign_pct
  - headroom_to_35: shares * 0.35 - foreign_shares
  - first_year_fees: 300000 + 50000
expected:
  foreign_shares: 300000
  headroom_to_35: 50000
  first_year_fees: 350000
```

## Ask the client first

1. Who are the shareholders, and what share will foreigners hold (over 35%)?
2. Who will be the ordinarily resident director?
3. Private company, public company or a branch (overseas corporation) of a foreign company?
4. What business, and will taxable sales exceed 50 million kyats a year (commercial tax)?
5. Will it employ staff (SSB and salary tax)?

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| DICA, register your company | Read for the 35% foreign ownership line, single shareholder and director, ordinarily resident director and the 183-day test, public company directors, no minimum capital | https://www.dica.gov.mm/doing-business/register-your-company/ | 2026-11-14 |
| MyCO, prescribed forms and fees | Read for the Form A-1, A-2, A-3, A-8, AR, C-2, C-4, extract and late fees | https://www.myco.dica.gov.mm/public/fees.aspx | 2026-11-14 |
| MyCO, how to register a company | Read for the information collected, payment by card, MPU or cash, and submission to the Registrar | https://www.myco.dica.gov.mm/public/howto.aspx?cn=HowTo_RegCompany | 2026-11-14 |
| IRD notice to file returns (28 April 2026) | Read for IRD e-Registration of new companies for a TIN | https://www.ird.gov.mm/announcement-lists/96 | 2026-11-14 |
| IRD, taxes: companies (Burmese) | Read for tax registration after DICA approval and commercial tax registration forms | https://www.ird.gov.mm/tax-knowledge/taxes/companies | 2026-11-14 |

Not yet confirmed: the due dates of the first and later annual returns (the old file's "within two months of incorporation" and "one month after the anniversary" came from a law firm site, not from DICA); incorporation time; sector restrictions on foreign companies; audit requirements and audit exemption; whether filing accounts with the IRD requires audited statements (old file, from a law firm site).

> Contributed by Mr Moe Lwin Tun.
