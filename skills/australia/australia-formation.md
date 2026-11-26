---
name: australia-formation
description: Use this skill whenever asked about forming, incorporating, or registering a company in Australia. Trigger on phrases like "set up a company in Australia", "Pty Ltd", "ASIC registration", "Australian company formation", "register a business Australia", "ABN", "ACN", "proprietary limited", "sole trader Australia", "partnership Australia", or any question about starting a business entity in Australia. Covers entity types (Pty Ltd, Ltd, sole trader, partnership, trust), registration process, costs, post-formation compliance, and bank account opening. ALWAYS read this skill before advising on Australian company formation.
version: 1.3
jurisdiction: AU
tax_year: 2025
last_updated: 2026-11-26
depends_on:
  - company-formation-workflow-base
category: formation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: formation
---

# Australia Formation

## Australia Formation

## Australia Company Formation Skill v1.3

Australia Company Formation Skill v1.3

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Currency | AUD |
| Company registrar | Australian Securities and Investments Commission (ASIC) -- asic.gov.au |
| Key legislation | Corporations Act 2001 (Cth) |
| Typical formation time | ASIC service target of 1 business day for online applications. Individual processing times vary |
| Corporate tax rate | Ordinary rates are 25% for base rate entities and 30% for other companies. Test aggregated turnover below $50 million and base rate entity passive income of no more than 80% of assessable income |
| Skill version | 1.3 |

## Section 2 -- Entity Types Comparison

**Entity Types Comparison**

| Feature | Sole Trader | Partnership | Pty Ltd (Proprietary) | Public Company (Ltd) | Trust (with corporate trustee) |
| --- | --- | --- | --- | --- | --- |
| Legal personality | No | No | Yes | Yes | No (trustee is legal person) |
| Liability | Unlimited | Generally personally liable. Check jurisdiction, partnership type and nature of liability | Shareholder liability generally limited to unpaid amounts on shares | Depends on company type. For a company limited by shares, shareholders generally owe unpaid amounts on shares | The trustee may be liable on trust obligations. Check indemnity and director liability |
| Min. participants | 1 individual | 2 partners | 1 member and 1 director ordinarily resident in Australia, subject to CSF requirements | 1 member, 3 directors excluding alternates (at least 2 ordinarily resident in Australia) and 1 secretary ordinarily resident in Australia | Depends on the deed and method of creating the trust |
| Min. share capital | N/A | N/A | No general minimum dollar amount | No general minimum dollar amount for a company limited by shares | N/A |
| Max. shareholders | N/A | N/A | 50 counting shareholders, subject to employee and qualifying CSF exclusions | No general 50-member limit | N/A |
| Tax treatment | Personal income tax | Partners generally include their share of net income | Company tax rate | Company tax rate | Allocated income may be assessed to beneficiaries or the trustee, depending on present entitlement and other conditions |
| Admin burden | Very low | Low | Medium | High | Medium--High |
| ASIC company registration | No | No. Check ABN, business name and other registrations | Yes | Yes | Corporate trustee registers as a company. Check separate registrations relevant to the trust |
| Audit required | Check industry obligations | Check industry obligations | Large proprietary companies generally require audit. Also check small company reporting triggers and audit exemptions | Generally yes. Check the separate rules for companies limited by guarantee and charities | Check deed and industry obligations |

**Recommended default:** Proprietary company limited by shares (Pty Ltd) for most commercial purposes.

- **Choose the structure before registering** — Compare ownership, funding, liability, profit distribution and ongoing administration; a company is not automatically the best structure for a small business. Shareholders' liability is generally limited to unpaid amounts on their shares, but directors can be personally liable through guarantees, breaches of duties, insolvent trading and tax obligations, and a corporate trustee does not remove every trustee or director risk.  _([ASIC, Becoming a company director](https://www.asic.gov.au/for-business-and-companies/small-business-director-essentials/becoming-a-company-director))_

## Section 3 -- Registration Process

### Step 1: Choose Company Name

- **Choose company name** — Check availability with ASIC and use the legal ending for the company type. A proprietary company limited by shares ordinarily uses ‘Proprietary Limited’ or ‘Pty Ltd’. You can reserve a name for 2 months or register directly. Apply ASIC’s statutory name availability checks. [ASIC company registration](https://www.asic.gov.au/for-business-and-companies/companies/register-a-company)

### Step 2: Obtain Consent from Officeholders

- **Obtain Consent from Officeholders** — All proposed directors and secretaries must consent in writing before registration; At least 1 director must ordinarily reside in Australia (for Pty Ltd)
- **Director eligibility and director ID** — Directors must be at least 18. A person disqualified from managing companies needs ASIC permission or court leave before appointment. A director must apply personally for a director ID before appointment unless they already hold one or a lawful extension applies. Nominee directors have the same duties. A proprietary company needs at least two directors when making a CSF offer and while it has CSF shareholders. At least one must ordinarily reside in Australia if there are two, or a majority if there are more than two. [ASIC Becoming a company director](https://www.asic.gov.au/for-business-and-companies/small-business-director-essentials/becoming-a-company-director) · [ASIC Crowd-sourced funding](https://www.asic.gov.au/crowd-sourced-funding)

### Step 3: Prepare Company Details

- **Prepare Company Details** — Registered office address (must be in Australia; can be accountant's or agent's office); Principal place of business; Share structure (number and class of shares, rights); Details of shareholders, directors, secretary (if any)
- **Governance rules and consents** — Decide whether the company runs on the replaceable rules, a constitution, or both where permitted. Record share classes, rights, numbers and amounts paid or unpaid, obtain members' written consents and the occupier's consent for a registered office the company does not occupy, and open the share register at registration. Registering a company name does not create trade mark rights.  _([ASIC, Register a company](https://www.asic.gov.au/for-business-and-companies/companies/register-a-company))_

### Step 4: Register via Business Registration Service (BRS)

- **Register via BRS** — The Business Registration Service supports eligible company, ABN, TFN, GST and PAYG withholding applications. ASIC processes the company application and issues an Australian Company Number (ACN) if approved. Check the fee for the date you apply. [Business Registration Service](https://register.business.gov.au/) · [ASIC service charter](https://www.asic.gov.au/servicecharter)

### Step 5: Receive Certificate of Registration

- **Receive Certificate of Registration** — Certificate confirms ACN, company name, date of registration, type; Company legally exists from date on certificate
- **After registration** — Retain the certificate and ACN, check the register against the approved details and record the actual registration date. Do not promise a fixed processing or bank-account opening time, and keep access credentials with the authorised officeholder.

### Step 6: Apply for ABN (Australian Business Number)

- **Apply for ABN** — Eligible entities can apply free via the Australian Business Register or as part of the Business Registration Service application. An ABN is required for GST registration and generally shown on tax invoices. A payer's no-ABN withholding obligation depends on the payment and any exceptions. [Australian Business Register](https://www.abr.gov.au/business-super-funds-charities/applying-abn)

### Step 7: Register for GST (if applicable)

- **GST registration threshold** — An enterprise generally registers if projected GST turnover meets AUD 75,000, or AUD 150,000 for a non-profit body. Current GST turnover can also trigger registration if the Commissioner is not satisfied that projected turnover is below the threshold. Voluntary registration may be available below the threshold.
- **GST turnover, not bank receipts** — The threshold uses the GST turnover definition, which differs from every receipt in the bank account. Taxi and ride-sourcing activities must register regardless of turnover, and voluntary registration below the threshold brings reporting obligations.  _([ATO, Registering for GST](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/registering-for-gst))_

### Step 8: Register for PAYG Withholding (if employing)

- **Register for PAYG Withholding** — Required before paying employees or directors; Register via BRS or ATO  _(BRS / ATO)_
- **Payroll obligations from the first payment** — Before the first payment subject to withholding, set up payroll and check worker classification, Single Touch Payroll, awards, leave, workers compensation and state payroll tax. From 1 July 2026, Payday Super requires super guarantee contributions, at 12% of qualifying earnings, to reach the fund within seven business days of payday, subject to specific exceptions.  _([ATO, About Payday Super](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/about-payday-super))_

## Section 4 -- Capital Requirements

**Capital Requirements**

| Entity Type | Min. Share Capital | Min. Paid-Up | Payment Timing | In-Kind Contributions |
| --- | --- | --- | --- | --- |
| Pty Ltd | No general minimum dollar amount | No general minimum | As specified in share terms | Permitted. Check share terms and any valuation and related-party requirements |
| Public Ltd limited by shares | No general minimum dollar amount | No general minimum | As specified | Permitted. A public company must give prescribed particulars or lodge the written contract where the formation rules require it |

Check sector-specific licensing and financial requirements separately. [Corporations Act sections 117 and 254B](https://www.legislation.gov.au/C2004A00818/2025-03-17/2025-03-17/text/original/epub/OEBPS/document_1/document_1.html)

## Section 5 -- Costs Breakdown

**Costs Breakdown**

| Cost Component | Amount (AUD) | Notes |
| --- | --- | --- |
| ASIC company registration | $611 | Australian company having share capital, from 1 July 2025 to 30 June 2026 |
| Name reservation (optional) | $62 | Same period, valid 2 months |
| Business name registration where required | $45 for 1 year or $104 for 3 years | Same period |
| ABN registration | Free | Via ABR |
| GST registration | Free | Via ATO |
| ASIC annual review fee | $329 | Ordinary proprietary company from 1 July 2025 to 30 June 2026 |
| **Company registration and optional company name reservation** | **$611 without reservation or $673 with reservation** | Separate business name and professional fees may apply |
| Legal / accountant setup fees | $500--$2,000 | Indicative estimate. Actual quote depends on scope |

ASIC indexes fees from 1 July. From 1 July 2026 the share capital company registration fee is $636 and the ordinary proprietary annual review fee is $342. Check the fee for the transaction or review date. [Business.gov.au 2026 fee changes](https://business.gov.au/news/changes-for-businesses-from-1-july-2026) · [ASIC fee indexation](https://www.asic.gov.au/for-business-and-companies/forms-and-fees/all-fees/fee-indexation) · [Corporations (Fees) Regulations regulation 3](https://www.legislation.gov.au/F2001B00275/2025-01-01/2025-01-01/text/original/epub/OEBPS/document_1/document_1.html)

### Annual Maintenance

**Annual Maintenance**

| Item | Cost (AUD) |
| --- | --- |
| ASIC annual review fee | $329 for an ordinary proprietary company in 2025-26 |
| Accountant / tax agent fees | $1,500--$5,000/year |
| Business name renewal (if applicable) | $45 for 1 year or $104 for 3 years in 2025-26 |
| Registered office service (if using) | $200--$600/year |
| ASIC late fees | In 2025-26, $98 up to 1 month late or $411 after 1 month. Check the applicable fee period |

## Section 6 -- Post-Formation Compliance

**Post-Formation Compliance**

| Obligation | Deadline | Authority |
| --- | --- | --- |
| ASIC annual review | Generally the registration anniversary. Pay the annual fee within 2 months of the review date. Check the date on the statement | ASIC |
| Company tax return | Apply the entity's ATO due date. Some eligible tax-agent clients have a 15 May lodgement date | ATO |
| BAS (Business Activity Statement) | Determined by the registration, reporting cycle and tax obligation. GST can be monthly, quarterly or annual | ATO |
| PAYG payment summaries / STP finalisation | Generally 14 July, subject to STP concessions including for eligible closely held payees | ATO |
| Superannuation guarantee | For earnings before 1 July 2026, quarterly and generally due by the 28th day after quarter end. From 1 July 2026, apply Payday Super for each payday and its receipt deadlines | Super fund / ATO |
| Change notifications to ASIC | Often 28 days, including some registered detail and officeholder changes. Check the specific notice | ASIC |
| Financial records | Maintain for 7 years | Internal |
| Directors' duties | Ongoing (s180--184 Corporations Act) | ASIC |

- **Keep the company separate and diarised** — Keep company money and transactions apart from personal finances, agree who maintains the share register, accounting records, tax calendar and ASIC correspondence, and diary the annual review, solvency resolution and change notifications. Retain financial records for seven years after the transactions they cover. Tax return and activity statement dates depend on the company's circumstances and lodgement arrangements; they are not all due on one date.  _([ASIC, What books and records should my company keep](https://asic.gov.au/for-business/running-a-company/company-officeholder-duties/what-books-and-records-should-my-company-keep/))_

## Section 7 -- Bank Account Opening

### Documents Typically Required

- **Documents Typically Required** — Certificate of registration (ACN); Company constitution or replaceable rules; ABN confirmation; ID (passport / driver's licence) for all directors; Proof of address for directors and shareholders

### Typical Timeline

- **Typical Timeline** — 1--3 days (Big 4 banks and digital banks for Australian residents); 1--3 weeks (non-resident directors, enhanced KYC)

### Common Banks

Commonwealth Bank (CBA), Westpac, ANZ, NAB (Big 4); Macquarie, Bendigo (mid-tier); Airwallex, Wise Business (digital/international)

## Section 8 -- Foreign Founder Considerations

**Foreign Founder Considerations**

| Question | Answer |
| --- | --- |
| Non-resident directors allowed? | Yes, but at least 1 director must ordinarily reside in Australia |
| Resident director requirement | At least 1 for an ordinary Pty Ltd and at least 2 for a public company. Check the separate CSF residency rules |
| Nominee directors | Permitted (ASIC register shows actual director names) |
| Physical presence required? | No (online registration); resident director must be genuinely resident |
| Foreign ownership restrictions | Foreign Investment Review Board (FIRB) approval may be required for certain sectors and thresholds |
| Registration of existing foreign companies | A foreign company carrying on business in Australia generally registers with ASIC on Form 402 and receives an ARBN. The fee in 2025-26 was $611. Check the separate requirements for ABN entitlement |
| Tax treaty benefits | Australia has extensive DTA network; check withholding rates |

- **Foreign founders** — Examine the resident director requirement, the founders' tax residency, foreign investment rules and the difference between incorporating an Australian company and registering an existing foreign company, and record the chosen structure and the reasons for it before applying.

## Section 9 -- Common Mistakes and Refusals

- **R-AU-F1 -- No Australian-resident director** — Every Pty Ltd must have at least one director who ordinarily resides in Australia. A company cannot be registered without this. Advise the client to appoint a local director or use a resident director service (with proper governance).  _((R-AU-F1))_
- **R-AU-F2 -- Failing to pay ASIC annual review fee** — Pay within 2 months after the review date. Late fees apply. ASIC may deregister a company if the review fee remains unpaid at least 12 months after the due date. [Corporations Act section 601AB(1A)](https://www.legislation.gov.au/C2004A00818/2025-07-09/2025-07-09/text/original/epub/OEBPS/document_3/document_3.html)
- **R-AU-F3 -- GST threshold ignorance** — Apply the enterprise and GST turnover tests under section 23-5 and Division 188. Apply for registration within 21 days of becoming required to register. GST and penalties may apply if registration is late.
- **R-AU-F4 -- Superannuation non-compliance** — The general rate was 11.5% of eligible ordinary time earnings in 2024-25 and 12% in 2025-26. From 1 July 2026 the 12% general rate applies to qualifying earnings under Payday Super. The quarterly super guarantee charge for pre-1 July 2026 periods is non-deductible. Super guarantee charge for qualifying earnings days from that date can generally be deducted when paid. Late payment penalties and interest on the charge remain separately non-deductible. [ATO Super guarantee rates](https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee) · [ATO Payday Super charge](https://www.ato.gov.au/businesses-and-organisations/super-for-employers/missed-or-late-payday-super-payments/what-happens-if-you-dont-pay-super-correctly/what-happens-if-you-dont-pay-the-super-guarantee-charge)
- **R-AU-F5 -- Shell company without substance** — This skill will not assist in forming a company with no genuine business activity in Australia. ASIC and the ATO actively pursue sham structures.  _((R-AU-F5))_

## Section 10 -- Timeline

**Timeline**

| Step | Duration | Cumulative |
| --- | --- | --- |
| Prepare documents and officer consents | 1--2 days | Day 1--2 |
| Register via BRS (ABN + company + GST) | 1 day | Day 2--3 |
| ASIC issues ACN and certificate | Service target of 1 business day for online applications | Depends on processing and information requested |
| Open business bank account | 1--3 days (resident) / 1--3 weeks (non-resident) | Day 4--27 |
| ABN confirmation | Successful automated applications are generally immediate. ABR aims to review applications needing checks within 20 business days | Tax registrations and any licences have separate timing |
| **Ready to trade** |  | **Depends on legal registration, required registrations and licences and banking arrangements** |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute legal, tax, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before acting upon.

> Contributed by Ryan Duguid.
