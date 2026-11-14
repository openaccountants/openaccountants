---
name: bd-formation
description: "Bangladesh 2026 business setup and entity-choice routing: TIN, local trade licence, banking evidence, VAT registration and online-selling/partnership referrals, distinct from company incorporation."
version: 1.1
jurisdiction: BD
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: formation
type: filing-howto
---

# Bangladesh sole-trader and business registrations v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For a person starting freelancing or a small business. This file organizes registrations; bd-company-formation owns company incorporation. Do not infer that a solo operator is incorporated or that every online activity has identical licensing requirements.

## Ask the client first

- Activity, owners, customers and location/local licensing authority.
- Legal form, residence/NID and existing TIN.
- Expected and actual turnover, imports/exports and bank arrangements.
- Staff, regulated activities, online selling and any foreign owners.

## The method, step by step

1. Compare sole proprietorship (individual owner and personal liability), partnership (deed/partners and separate firm tax reporting), and company (incorporation, governance and accounts/audit). Do not choose solely on a headline tax rate. Route company setup to [company formation](bd-company-formation.md); the Companies Act defines the separate legal forms (https://bdlaws.minlaw.gov.bd/act-788/section-32006.html, https://bdlaws.minlaw.gov.bd/act-788/section-32025.html).
2. Obtain taxpayer registration/TIN through the NBR's official e-TIN service linked from https://nbr.gov.bd; use the actual entity identity and documents. The individual e-Return at https://etaxnbr.gov.bd is a filing service, not a substitute for incorporation. Keep the certificate and login under the taxpayer's control.
3. Obtain the applicable trade licence from the city corporation, paurashava or union parishad. The official investment FAQ describes OSS services for participating city corporations, or the local form, supporting documents/NOC, enquiry and assessed fee route elsewhere. Collect the issued licence and track renewals; no universal fee is asserted (https://investbangladesh.gov.bd/faq).
4. Open the appropriate business banking arrangement and retain remittance/encashment certificates for export receipts. An account does not by itself prove tax exemption or an incentive award.
5. Apply [VAT](bangladesh-vat.md) to registration/enlistment, including turnover-independent activity triggers and voluntary registration. Do not use the old turnover amounts or assume every unregistered freelancer is outside all obligations. Preserve the certificate/BIN and effective date.
6. Online selling needs a separate check of the currently applicable DBID/e-commerce and sector rules. Do not assume that a trade licence replaces every activity permission. Keep this unresolved check in the setup checklist rather than inventing a DBID mandate for all freelancers.
7. File applicable annual income-tax returns and retain proof of filing using [PIT](bangladesh-pit.md) or corporate tax, as appropriate. TIN, trade licence, VAT and income-tax return are separate obligations.

## Worked cases

### Documented setup budget

Illustrative authority-assessed licence/registration fees 5,000 and bank/other setup costs 2,000 produce a 7,000 cash budget. These are assumed client-specific assessed costs, not published statutory fees or a promise of total incorporation cost.

```oa-check
name: Actual assessed setup costs
inputs:
  assessed_fees: 5000
  other_setup_costs: 2000
steps:
  - cash_budget: assessed_fees + other_setup_costs
expected:
  cash_budget: 7000
```

### Edge: shared capital does not determine entity tax

Two partners fund a business with 300,000 and 200,000. Record capital 500,000 and shares 60%/40%, derived. The deed and legal registration still determine the vehicle and liability; do not label the partnership a company just because it has shared capital.

```oa-check
name: Partners capital reconciliation
inputs:
  partner_a: 300000
  partner_b: 200000
steps:
  - capital: partner_a + partner_b
  - share_a: partner_a / capital
  - share_b: partner_b / capital
expected:
  capital: 500000
  share_a: 0.6
  share_b: 0.4
```

## When to refuse or refer

Refer partnership deed/registration specifics, online-seller DBID scope, foreign ownership, regulated sectors and unclear local licence conditions. Never omit a confirmed licence or BIN duty, use a guessed threshold, or assume a legal form without the documents.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for official incorporation/post-incorporation and trade-licence process, authorities and documents | https://investbangladesh.gov.bd/faq | 2026-11-14 |
| Read for separate company forms and membership definition | https://bdlaws.minlaw.gov.bd/act-788/section-32006.html | 2026-11-14 |
| Read for company formation | https://bdlaws.minlaw.gov.bd/act-788/section-32025.html | 2026-11-14 |
| Read for NBR official service links including e-TIN/e-Return | https://nbr.gov.bd/regulations/acts/finance-acts/eng/contents/eng | 2026-11-14 |

Not yet confirmed: Activity-specific DBID/e-commerce duty, local licence fees/renewals, partnership registration details and live registration fields for the individual; these are checks to resolve, not a universal exemption or mandate.
