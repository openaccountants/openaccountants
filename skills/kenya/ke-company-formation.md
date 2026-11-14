---
name: ke-company-formation
description: 'Kenya private-company formation and entity choice in 2026: BRS forms and fees, legal form, directors, capital, beneficial owners and separate registry/tax compliance.'
jurisdiction: KE
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
version: 0.1
type: situation-rules
category: formation
---

# Kenya company formation and entity choice (2026)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this for choosing and registering an ordinary Kenyan private company and setting its legal compliance calendar. The Business Registration Service (BRS) administers the Companies Act, business names and LLPs; [its live registry page](https://brs.go.ke/companies-registry/) confirms these routes. A company limited by shares is a distinct legal person on incorporation under Companies Act s19. Public companies, companies limited by guarantee, business names/sole proprietorships, partnerships, LLPs and a foreign-company branch are alternative forms with different liability and registration rules, not interchangeable names.

For foreign founders or a branch, load [set-up-your-company-in-kenya-we-handle-it-from-abroad](set-up-your-company-in-kenya-we-handle-it-from-abroad.md) for the distinct execution workflow. This file does not decide immigration, tax residence, sector licences or a foreign shareholder's treaty position.

## Ask the client first

- Intended activity and any regulated-sector restrictions.
- Private company, public/guarantee company, LLP, partnership, business name or foreign branch; desired liability and future investors.
- Shareholders, voting rights, beneficial owners, proposed directors and their identity/address documents.
- Proposed company name, Kenyan registered office and postal address.
- Proposed capital and whether it is actually paid up; do not confuse nominal capital with cash invested.
- Financial year, employees, expected supplies and tax registration needs.

## The method, step by step

### Rates, bands and thresholds

Under [Companies Act ss5-13,19,128-129](https://brs.go.ke/wp-content/uploads/2023/03/CompaniesAct17of2015.pdf), a private company limited by shares has member liability limited by unpaid amounts on shares. Its articles restrict share transfers, prohibit public subscription invitations, require member consent to add a member and limit members subject to the employee/former-employee and joint-holder rules. It may have a single subscriber; a natural-person director is required. Separate sector requirements can impose other conditions.

| Item | Threshold or amount, conditions and period | Official source |
|---|---|---|
| Private-company members | Maximum 50 under s9, excluding employee/former-employee members meeting its conditions; joint holders count as 1, in words on the page | https://brs.go.ke/wp-content/uploads/2023/03/CompaniesAct17of2015.pdf |
| Formation/subscription | At least 1 subscriber under s11; each share subscriber takes at least 1 share under s12, in words on the page | https://brs.go.ke/wp-content/uploads/2023/03/CompaniesAct17of2015.pdf |
| Private-company directors | At least 1 under s128; at least 1 natural person under s129, in words on the page | https://brs.go.ke/wp-content/uploads/2023/03/CompaniesAct17of2015.pdf |
| Private company secretary | Required if paid-up capital is KES 5,000,000 or more, s243, in words on the page | https://brs.go.ke/wp-content/uploads/2023/03/CompaniesAct17of2015.pdf |
| Registry fee for private company | KES 10,650; CR1,CR2,CR8 and statement of nominal capital; certificate of incorporation issued | https://brs.go.ke/fee-schedule-companies-registry/ |
| Published processing time | 3-5 days on BRS schedule, an administrative estimate for complete filings, not a guaranteed statutory deadline | https://brs.go.ke/fee-schedule-companies-registry/ |
| Beneficial owners register | Lodge within 30 days after completing preparation, not automatically after incorporation; non-public-listed company amendment within 14 days after making amendment, s93A, in words on the page | https://brs.go.ke/wp-content/uploads/2023/03/CompaniesAct17of2015.pdf |
| Annual return | Each year made up to return date (incorporation anniversary or anniversary of last different return date), lodged within 28 days after that made-up date, s705, in words on the page | https://brs.go.ke/wp-content/uploads/2023/03/CompaniesAct17of2015.pdf |

The old file's KES 100,000 nominal-capital example was a practice assumption, not a statutory minimum. Sections11-16 require a statement of capital and initial holdings; choose capital for actual governance and funding. The public-company authorised-minimum provisions ss516-518 do not set the private company's capital. Do not import a public-company rule into a private incorporation.

### Register, then separate legal and tax compliance

1. Use BRS on eCitizen (https://accounts.ecitizen.go.ke). Choose the legal form and name; comply with the registrar's name restrictions and current name-reservation/application flow.
2. Provide the application, memorandum, articles or applicable model articles, registered-office location, statement of capital/initial shareholdings and proposed officers required by ss13-16. For a private company BRS lists CR1,CR2,CR8 and the nominal-capital statement. CR8 supplies residential-address particulars; it is not an alternative memorandum replacing CR2.
3. Review the live invoice against BRS's fee schedule, sign/authenticate as required, pay through the available electronic method, submit, and retain the application/payment acknowledgement. Obtain the certificate and verify the registered details.
4. Prepare and lodge the beneficial-ownership register under s93A and maintain evidence of changes. Keep the actual preparation/amendment dates; the filing clock is not simply the incorporation date. Obtain current BO forms and regulations before filing complex ownership.
5. Obtain/verify KRA PIN registration and tax obligations through iTax (https://itax.kra.go.ke), using the company's exact registered identity; tax and registry registrations have separate legal purposes. The reviewed TPA ss8-13 establish taxpayer/PIN registration. Retain the PIN certificate and obligation details.
6. Diary BRS annual returns independently from tax. Use [ke-corporate-income-tax](ke-corporate-income-tax.md) for company return and earlier balance-payment timing, [kenya-vat](kenya-vat.md) for taxable supplies and [ke-payroll-paye-nssf-shif-ahl](ke-payroll-paye-nssf-shif-ahl.md) for staff.

## Boundary and exception table

| Situation | Response |
|---|---|
| Private company with a single shareholder/director | Check natural-person director and subscriber requirements; do not demand a second shareholder without a separate rule |
| Employee members or jointly held shares | Apply s9 member-count exceptions before counting towards limit |
| Public/guarantee company, LLP or partnership | Use the correct statutory route and forms; this private-company workflow is insufficient |
| Regulated activity or foreign ownership | Check sector licences/equity restrictions and professional advice |
| Beneficial ownership, nominee or layered entity | Obtain actual control information; no nominee arrangement to evade disclosure |

## Worked cases

Hypothetical private-company application: published registry fee KES 10,650 plus an assumed professional quote KES 15,000 makes KES 25,650 before other agreed costs. The quote is example input, not a government tariff. Distinguish registry costs from professional fees.

```oa-check
name: Separate government and professional fees
inputs:
  registry_fee: 10650
  professional_quote: 15000
steps:
  - budget: registry_fee + professional_quote
expected:
  budget: 25650
```

Capital decision: hypothetical issued shares of KES 100 each, with 50,000 fully paid shares, give KES 5,000,000 paid-up capital, reaching s243's secretary threshold. If only 40,000 are fully paid the amount is KES 4,000,000; merely authorised or nominal capital does not establish the paid-up figure. Sector and public-company rules remain separate.

```oa-check
name: Paid-up-capital secretary threshold
inputs:
  share_value: 100
  paid_shares_high: 50000
  paid_shares_low: 40000
steps:
  - high_paid: share_value * paid_shares_high
  - low_paid: share_value * paid_shares_low
  - threshold_gap: 5000000 - low_paid
expected:
  high_paid: 5000000
  low_paid: 4000000
  threshold_gap: 1000000
```

## When to refuse or refer

Refer regulated sectors, investment/treaty structuring, disputed ownership, nominee arrangements, guarantees, public fundraising, insolvency and uncertainty about the registrar's current requirements. Do not promise bank acceptance, an immigration permit or a completion date merely because incorporation is possible.

## Filing and payment

BRS's schedule directs company registration online through eCitizen and electronic payment. Save submission, invoice, receipt, certificate and the final registered details. Annual-return and beneficial-ownership filings have distinct deadlines above; registry annual returns are not the corporation tax return.

## Completion checklist

Confirm legal form, agreed share/voting structure, natural-person director, registered office, verified identity, beneficial ownership, fee/payment evidence, incorporation certificate, PIN/obligations and separate registry/tax calendars.

## Sources

| Source and passages actually read | Official URL | Read on |
|---|---|---|
| Read for BRS live company-registry routes and administered laws | https://brs.go.ke/companies-registry/ | 2026-11-14 |
| Read for Companies Act BRS 2021 revision ss5-19,46,48,93A,128-129,243,516-518,705,894,979-981, limited passages for form, governance and ongoing filings | https://brs.go.ke/wp-content/uploads/2023/03/CompaniesAct17of2015.pdf | 2026-11-14 |
| Read for BRS fee schedule private/foreign company rows, forms, fee, output and processing estimate | https://brs.go.ke/fee-schedule-companies-registry/ | 2026-11-14 |
| Read for TPA ss8-13 taxpayer/PIN registration and separate tax obligations | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf | 2026-11-14 |

Not yet confirmed: Any post-2021 amendment affecting the quoted Companies Act passages is not represented by a new consolidation; live BRS confirms the current registration rows. Current BO regulations/forms and detailed beneficial-owner identification rules require checking before filing. The former KES 100,000 customary capital is not a legal minimum; no complete-launch timeline or unlisted professional fee is promised.
