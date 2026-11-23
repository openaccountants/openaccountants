---
name: canada-gst-hst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Canadian GST/HST return (Form GST34) for a self-employed individual or small business in Canada. Trigger on phrases like "prepare GST return", "file HST", "Canadian sales tax", "GST/HST return", "Form GST34", "input tax credits", "ITC claim", or any request involving Canadian GST/HST filing. Also trigger when classifying transactions for GST/HST purposes from bank statements, invoices, or other source data. This skill covers federal GST and harmonized HST provinces only under the regular method. Quebec QST, Saskatchewan PST, Manitoba RST, British Columbia PST, Quick Method, and simplified method for charities are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any Canadian GST/HST work.
version: 2.1
jurisdiction: CA
tax_year: 2025
tax_year_notes: "Retains the original 2025 scope and April 2026 hypothetical examples; the correction distinguishes the 2025 and 2026 vehicle-acquisition limits. This is not a full 2026 source review."
last_updated: 2026-11-23
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: vat-gst
---

# Canada GST HST

## Canada GST/HST Return Skill (Form GST34) v2.1

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content.**

**Quick reference field table**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Canada |
| Federal GST rate | 5% |
| HST rates by province | ON 13%, NS 14% (effective Apr 1 2025), NB 15%, NL 15%, PE 15% |
| GST-only provinces | AB, BC, SK, MB, QC, NT, NU, YT (5% GST; BC/SK/MB/QC have separate provincial sales taxes) |
| Zero rate | 0% (basic groceries, prescription drugs, medical devices, qualifying exports (Schedule VI conditions)) |
| Exempt | Financial services, long-term residential rent, most health/dental/legal aid, childcare |
| Return form | GST34 (GST/HST Return for Registrants) |
| Filing portal | CRA My Business Account (canada.ca) |
| Authority | Canada Revenue Agency (CRA) |
| Currency | CAD only |
| Filing frequencies | Annual (taxable supplies <= $1.5M), Quarterly ($1.5M–$6M), Monthly (> $6M or voluntary election) |
| Deadline | Monthly/quarterly: one month after period end; ordinary annual: three months after fiscal year-end. June 15 filing / April 30 payment applies to an annual-filer individual with business income and a December 31 year-end; weekends/recognized holidays move the deadline to the next business day. [dates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html). |
| Small supplier threshold | $30,000 in any single calendar quarter or in the last four consecutive calendar quarters (ETA s.148) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Community |
| Validation date | April 2026 |

**Key GST34 lines**

| Line | Meaning |
| --- | --- |
| 101 | Total sales and other revenue (before GST/HST) |
| 103 | GST/HST collected or collectible |
| 104 | Adjustments to GST/HST (e.g., bad debt recovery, change-in-use) |
| 105 | Total GST/HST and adjustments (= 103 + 104) |
| 106 | Input tax credits (ITCs) |
| 107 | Adjustments deducted in determining net tax, including eligible bad-debt relief; not a recaptured-ITC debit. [lines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html). |
| 108 | Total ITCs and adjustments (= 106 + 107) |
| 109 | Net tax (= 105 − 108; positive = owing, negative = refund) |
| 110 | Instalments paid |
| 111 | Rebates claimed |
| 112 | Total other credits (= 110 + 111) |
| 113A / 113B / 113C | 113A = 109 − 112; 113B = 205 + 405; final balance 113C = 113A + 113B. [form](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf). |
| 114 | Refund claimed when final line 113C is negative |
| 115 | Amount owing when final line 113C is positive |

**GST/HST rates by province (complete)**

| Province/Territory | Rate | Components | Effective |
| --- | --- | --- | --- |
| Alberta (AB) | 5% | GST only | — |
| British Columbia (BC) | 5% GST + 7% PST | Separate PST (not on GST34) | — |
| Manitoba (MB) | 5% GST + 7% RST | Separate RST (not on GST34) | — |
| New Brunswick (NB) | 15% HST | Harmonized | — |
| Newfoundland & Labrador (NL) | 15% HST | Harmonized | — |
| Northwest Territories (NT) | 5% | GST only | — |
| Nova Scotia (NS) | 14% HST | Harmonized | Apr 1, 2025 |
| Nunavut (NU) | 5% | GST only | — |
| Ontario (ON) | 13% HST | Harmonized | — |
| Prince Edward Island (PE) | 15% HST | Harmonized | — |
| Quebec (QC) | 5% GST + 9.975% QST | Separate QST (filed with Revenu Quebec) | — |
| Saskatchewan (SK) | 5% GST + 6% PST | Separate PST (not on GST34) | — |
| Yukon (YT) | 5% | GST only | — |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Hold the rate and affected return allocation until place of supply is established; do not default to Ontario. [place](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html). |
| Unknown GST/HST status of a purchase | Not eligible for ITC |
| Unknown province of supply | Obtain supply/delivery/recipient-address evidence; registration province alone is insufficient. [place](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html). |
| Unknown business-use proportion (vehicle, phone, home office) | 0% ITC |
| Unknown whether personal or business expense | Personal (no ITC) |
| Unknown blocked-input status (club dues, personal) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | CAD 5,000 |
| HIGH tax-delta on a single conservative default | CAD 400 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net tax position | CAD 10,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Canadian or international business bank: RBC, TD, Scotiabank, BMO, CIBC, National Bank, Desjardins, Tangerine, Simplii, EQ Bank, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices for the period, especially for exports/interprovincial supplies, the GST/HST account number and purchase documents for every claimed ITC. CAD 400 is only an internal review flag; the statutory documentation tiers are under CAD 100, CAD 100–499.99 and CAD 500 or more (Section 5.6). [docs](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html).

**Ideal** — complete sales journal, purchase journal, prior period GST34, Quick Method election (if applicable — but then R-CA-3 fires).

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. A bank-only working paper is provisional: hold every unsupported ITC and unestablished place-of-supply conclusion. The reviewer brief must identify the missing invoice/source documents for each affected claim; the CAD 400 internal flag does not excuse documentation below that amount. [docs](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html); [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html).

### Canada-specific refusal catalogue

- **R-CA-1 — Quebec QST** — Quebec Sales Tax (QST) is administered by Revenu Quebec and filed separately from the federal GST return. This skill covers federal GST/HST (Form GST34) only. For QST, please use a CPA familiar with Quebec tax administration. (Trigger: client is in Quebec or asks about QST filing.)
- **R-CA-2 — Provincial sales tax (BC PST, SK PST, MB RST)** — Provincial sales taxes (BC PST, SK PST, MB RST) are separate from GST/HST and filed with the respective provincial authority. This skill covers the federal GST/HST return only. (Trigger: client asks about BC PST, Saskatchewan PST, or Manitoba RST filing.)
- **R-CA-3 — Quick Method** — The Quick Method calculates GST/HST remittance as a percentage of GST/HST-included revenue rather than tracking actual ITCs. This skill covers the regular method only. For Quick Method returns, apply the prescribed remittance rate for your sector and province. (Trigger: client has elected the Quick Method of accounting (GST74).)
- **R-CA-4 — Simplified method for charities/NPOs** — Charities, NPOs, and public service bodies have special GST/HST rules including the net tax calculation and public service body rebates. Out of scope. (Trigger: client is a registered charity, NPO, or public service body using the simplified method or net tax calculation.)
- **R-CA-5 — First Nations exemptions** — First Nations tax exemptions under the Indian Act (section 87) have specific rules that are outside the scope of this skill. Please consult a tax professional experienced in Indigenous tax matters. (Trigger: client asks about tax exemptions under the Indian Act or supplies on reserve.)
- **R-CA-6 — GST/HST groups (closely related corporations)** — Closely related group elections under s.156 involve intercompany supply rules that are out of scope. Please use a CPA. (Trigger: client is part of a GST/HST group election under ETA s.156.)
- **R-CA-7 — Non-resident simplified registration** — The simplified registration framework for non-resident digital economy businesses has different rules. Out of scope. (Trigger: non-resident registrant under the simplified registration framework.)
- **R-CA-8 — Real property transactions** — Real property transactions involve self-supply rules (s.191), change-of-use rules, and rebate calculations that are too fact-sensitive for this skill. Please use a CPA. (Trigger: client is buying/selling real property (land, buildings) with self-supply or change-of-use implications.)

## Section 3 — Supplier pattern library (the lookup table)

Use these counterparty patterns to identify transactions requiring classification. A name match alone does not prove the supply, registration regime, exemption, rate or ITC entitlement. Hold an affected return allocation until the invoice, supply facts and applicable rule support it. [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html); [place](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html).

**How to read this table.** Match by case-insensitive substring on the counterparty name. If multiple patterns match, use the most specific.

### 3.1 Canadian banks (fees exempt — exclude)

**Canadian banks table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RBC, ROYAL BANK OF CANADA | EXCLUDE for bank charges/fees | ETA Schedule V, Part VII: financial service, exempt |
| TD, TORONTO-DOMINION, TD CANADA TRUST | EXCLUDE for bank charges/fees | Same |
| SCOTIABANK, BANK OF NOVA SCOTIA | EXCLUDE for bank charges/fees | Same |
| BMO, BANK OF MONTREAL | EXCLUDE for bank charges/fees | Same |
| CIBC, CANADIAN IMPERIAL | EXCLUDE for bank charges/fees | Same |
| NATIONAL BANK, BNC, BANQUE NATIONALE | EXCLUDE for bank charges/fees | Same |
| DESJARDINS, CAISSE POPULAIRE | EXCLUDE for bank charges/fees | Same |
| TANGERINE, SIMPLII, EQ BANK | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTEREST, INTERET | EXCLUDE | Interest income/expense, exempt |
| MORTGAGE, HYPOTHEQUE, LOAN | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Canadian government and statutory bodies (exclude entirely)

**Government bodies table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CRA, CANADA REVENUE AGENCY, RECEIVER GENERAL | EXCLUDE | Tax payment (GST remittance, income tax instalment) |
| REVENU QUEBEC | EXCLUDE | QST or income tax payment |
| CPP, CANADA PENSION PLAN | EXCLUDE | Pension contribution, not a supply |
| EI, EMPLOYMENT INSURANCE | EXCLUDE | Employment insurance premium |
| WSIB, WCB, CNESST | EXCLUDE | Workers compensation |
| SERVICE CANADA, SERVICE ONTARIO | EXCLUDE | Government fees, sovereign act |
| CITY OF, VILLE DE, MUNICIPAL | EXCLUDE | Municipal tax/fee |

### 3.3 Canadian utilities

**Canadian utilities table**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| HYDRO ONE, TORONTO HYDRO, BC HYDRO, HYDRO-QUEBEC | Taxable | GST/HST at provincial rate | Electricity — overhead |
| ENBRIDGE, FORTISBC, ATCO GAS | Taxable | GST/HST at provincial rate | Gas — overhead |
| TELUS | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| ROGERS, ROGERS COMMUNICATIONS | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| BELL, BELL CANADA, BELL MOBILITY | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| SHAW, COGECO, VIDEOTRON | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| FIDO, KOODO, VIRGIN PLUS, FREEDOM MOBILE | Taxable | GST/HST at provincial rate | Telecoms — overhead |

### 3.4 Insurance (exempt — exclude)

**Insurance table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MANULIFE, SUN LIFE, GREAT-WEST LIFE, CANADA LIFE | EXCLUDE | Insurance, exempt (ETA Schedule V, Part VII) |
| INTACT, AVIVA, DESJARDINS ASSURANCE | EXCLUDE | Same |
| CO-OPERATORS, WAWANESA, ECONOMICAL | EXCLUDE | Same |
| INSURANCE, ASSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

**Post and logistics table**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| CANADA POST, POSTES CANADA | Taxable domestic letter mail/postage, subject to actual supply facts | GST/HST | Do not treat standard letter mail as categorically exempt. [place](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html). |
| CANADA POST (courier, Xpresspost, Priority) | Taxable | GST/HST | Non-universal services are taxable |
| PUROLATOR | Taxable | GST/HST | Express courier |
| FEDEX CANADA, UPS CANADA, DHL CANADA | Taxable | GST/HST | Courier services |
| CANPAR, DICOM, LOOMIS | Taxable | GST/HST | Courier services |

### 3.6 Transport

**Transport table**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| VIA RAIL | Taxable | GST/HST | Domestic passenger rail |
| GO TRANSIT, TTC, STM, TRANSLINK, OC TRANSPO | Exempt if a qualifying public-transit service | — | Exempt under Schedule V, not zero-rated. Charters/tours and other services require separate classification. [municipal](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4049/gst-hst-information-municipalities.html). |
| UBER CANADA | Taxable | GST/HST | Ride-sharing; platform is GST-registered |
| LYFT | Taxable | GST/HST | Same |
| AIR CANADA (international) | Zero-rated | 0% | International transport — Schedule VI, Part VII |
| AIR CANADA (domestic) | Taxable | GST/HST | Domestic air |
| WESTJET (international) | Zero-rated | 0% | International |
| WESTJET (domestic) | Taxable | GST/HST | Domestic air |
| ENTERPRISE, HERTZ, AVIS, BUDGET (car rental) | Taxable | GST/HST at location rate | Car rental — ITC restricted if personal use |

### 3.7 Food retail (generally zero-rated basic groceries — but personal)

**Food retail table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TIM HORTONS, TIMS | Default BLOCK ITC | Restaurant/prepared food is taxable at GST/HST, but personal unless hospitality business |
| STARBUCKS, MCDONALDS, SUBWAY, A&W | Default BLOCK ITC | Same — prepared food/beverages are taxable but likely personal |
| LOBLAWS, NO FRILLS, REAL CANADIAN, SUPERSTORE | Default BLOCK ITC | Grocery — mix of zero-rated and taxable items; personal provisioning default |
| METRO, SOBEYS, SAFEWAY, IGA, SAVE-ON-FOODS | Default BLOCK ITC | Same |
| COSTCO, WALMART (grocery) | Default BLOCK ITC | Mixed supply — personal default |
| CANADIAN TIRE (non-food) | Taxable | GST/HST — ITC eligible if business purpose confirmed |

### 3.8 SaaS — non-resident suppliers (self-assessment under ETA s.218)

For non-resident digital-service invoices, establish whether the supplier uses normal or simplified registration and whether the acquisition is an imported taxable supply. Under ETA s.217, ordinary services acquired exclusively in commercial activities are excluded; CRA generally treats 90% or more as exclusive commercial use. No tax on an invoice alone does not trigger self-assessment. Where s.218 actually applies, report the liability on 405 and separately determine any ITC. [217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html); [rc](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html).

**SaaS non-resident table**

| Pattern | Billing entity | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) or Google LLC (US) | Check invoice/regime/use; no automatic self-assessment | Apply Section 5.7 only if its conditions are met |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | Check invoice/regime/use; no automatic self-assessment | Same |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | Check invoice/regime/use; no automatic self-assessment | Same |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | Check invoice/regime/use; no automatic self-assessment | Same |
| NOTION | Notion Labs Inc (US) | Check invoice/regime/use; no automatic self-assessment | Same |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Check invoice/regime/use; no automatic self-assessment | Same |
| OPENAI, CHATGPT | OpenAI Inc (US) | Check invoice/regime/use; no automatic self-assessment | Same |
| FIGMA | Figma Inc (US) | Check invoice/regime/use; no automatic self-assessment | Same |
| CANVA | Canva Pty Ltd (AU) | Check invoice/regime/use; no automatic self-assessment | Same |
| SLACK | Slack Technologies Ltd (various) | Check invoice/regime/use; no automatic self-assessment | Check actual registration and invoice |
| ZOOM | Zoom Video Communications Inc (US) | Check invoice/regime/use; no automatic self-assessment | Same |
| ATLASSIAN | Atlassian Pty Ltd (AU) | Check invoice/regime/use; no automatic self-assessment | Same |
| DROPBOX | Dropbox Inc (US) | Check invoice/regime/use; no automatic self-assessment | Same |

**Note:** A normal GST/HST registrant should give its registration details to a simplified-regime supplier. Tax charged under the simplified regime is not claimable as an ordinary ITC or rebate; seek correction from the supplier. A normal-regime invoice has separate ITC/documentation requirements. No named supplier’s current billing entity or regime is established by this pattern list. [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html).

### 3.9 Canadian SaaS / domestic suppliers (ITC-eligible)

**Canadian SaaS table**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| SHOPIFY | Check actual invoice and supply | Applicable place-of-supply rate | Supplier headquarters alone does not establish 13%; claim ITC only to the eligible commercial-use extent with support. [place](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html); [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html). |
| STRIPE PAYMENTS CANADA | Taxable domestic or exempt | Check invoice | Transaction fees may be exempt financial service; subscription taxable |
| WEALTHSIMPLE | EXCLUDE (exempt) | — | Financial service |
| FRESHBOOKS | Taxable domestic | GST/HST | Accounting software |
| WAVE FINANCIAL | Taxable domestic | GST/HST | Accounting software (now owned by H&R Block) |
| HOOTSUITE | Taxable domestic | GST/HST | Social media management |

### 3.10 Payment processors

**Payment processors table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| SQUARE, MONERIS, GLOBAL PAYMENTS | Check invoice | Transaction fees exempt; hardware/subscription taxable |
| INTERAC | EXCLUDE (exempt) | Interac fees are financial services |

### 3.11 CRA payments and refunds

**CRA payments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CRA GST PAYMENT, RECEIVER GENERAL GST | EXCLUDE | GST remittance — not a supply |
| CRA INCOME TAX, INSTALMENT PAYMENT | EXCLUDE | Income tax — not a supply |
| CRA REFUND, GST REFUND | EXCLUDE | Government refund — not a supply |
| CRA CEBA, CEWS, CERS | EXCLUDE | Government subsidy — not a supply (but may have GST implications on repayment) |

### 3.12 Professional services (Canada)

**Professional services table**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| CPA, CHARTERED PROFESSIONAL ACCOUNTANT | Taxable service subject to actual facts | GST/HST | ITC only for eligible commercial use with required documentation; not automatic. [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html). |
| LAWYER, LAW OFFICE, BARRISTERS | Taxable | GST/HST | ITC-eligible if business purpose |
| NOTARY, NOTAIRE | Taxable | GST/HST | ITC-eligible if business purpose |
| CONSULTANT, CONSULTING | Taxable | GST/HST | ITC-eligible if business purpose |

### 3.13 Payroll (exclude entirely)

**Payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PAYROLL, SALARY, WAGES | EXCLUDE | Wages — outside GST/HST scope |
| CPP CONTRIBUTION | EXCLUDE | Pension contribution |
| EI PREMIUM | EXCLUDE | Employment insurance |
| CERIDIAN, ADP, PAYWORKS | EXCLUDE for payroll runs | Payroll processing fee itself may be taxable |

### 3.14 Property and rent

**Property and rent table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RENT, LOYER (commercial) | Taxable | Commercial lease — GST/HST on rent, ITC eligible |
| RENT, LOYER (residential) | EXCLUDE | Residential lease exempt (ETA Schedule V, Part I) |
| CONDO FEES, STRATA FEES | EXCLUDE if residential | Residential condo fees exempt |
| PROPERTY TAX, MUNICIPAL TAX | EXCLUDE | Government levy, not a supply |

### 3.15 Internal transfers and exclusions

**Internal transfers table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER, E-TRANSFER (own accounts) | EXCLUDE | Internal movement |
| INTERAC E-TRANSFER (to self) | EXCLUDE | Internal movement |
| DIVIDEND | EXCLUDE | Dividend payment, out of scope |
| LOAN REPAYMENT | EXCLUDE | Loan principal, out of scope |
| ATM WITHDRAWAL | TIER 2 — ask | Default exclude; ask what cash was spent on |
| OWNER DRAW, SHAREHOLDER LOAN | EXCLUDE | Owner withdrawal |

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of an Ontario-based self-employed software consultant.

### Example 1 — Non-resident SaaS, commercial-use exclusion (Notion)

`2026-04-03 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; CAD 21.89`

Retain the hypothetical USD 16.00 / CAD 21.89 invoice and assume normal registration, no charged GST/HST and exclusively commercial software use by the Ontario consultant. The ordinary service is excluded from imported taxable supplies under s.217: no self-assessment on 405 and no ITC for tax that was neither charged nor payable. CAD 21.89 × 13% = CAD 2.85 is arithmetic only, not a liability. If the commercial-use exclusion fails, determine the imported-supply liability and ITC separately before allocating it. [217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html); [rc](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html).

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line (self-assess) | Line (ITC) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-03 | NOTION LABS INC | -21.89 | -21.89 | 0 | — | — | — | N | — | No tax allocation: exclusively commercial imported service. [ETA s.217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html) |

### Example 2 — Domestic purchase with HST (Shopify)

`2026-04-10 ; SHOPIFY COMMERCE INC ; DEBIT ; Monthly plan ; -49.00 ; CAD`

Assume the hypothetical invoice supports 13% Ontario HST under the applicable place-of-supply rule, normal supplier registration and exclusively eligible commercial use. CAD 49.00 is HST-inclusive: net = 49.00 / 1.13 = 43.36 and HST = 5.64, claimable on 106 if the documentation conditions are met. The supplier’s headquarters alone does not establish the rate. [place](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html); [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html).

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-10 | SHOPIFY | -49.00 | -43.36 | -5.64 | 13% HST | 106 | N | — | — |

```oa-check
name: Ontario software invoice, supported 13% inclusive tax
inputs:
  gross: 49
  rate: 0.13
steps:
  net: round(gross / (1 + rate), 2)
  tax: gross - net
expected:
  net: 43.36
  tax: 5.64
```

### Example 3 — Entertainment, restricted ITC

`2026-04-15 ; THE KEG STEAKHOUSE ; DEBIT ; Client dinner ; -285.00 ; CAD`

Restaurant meal. Under ETA s.236 (which cross-references Income Tax Act s.67.1), meals and entertainment expenses are limited to 50% for income tax purposes. However, the full GST/HST ITC is claimable on the portion that is deductible for income tax (i.e., 50% of the GST/HST). Conservative default: block entirely as likely personal. If confirmed as business entertainment, 50% of ITC is claimable.

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-15 | THE KEG STEAKHOUSE | -285.00 | -285.00 | 0 | — | — | Y | Q1 | "Meals/entertainment: blocked (conservative)" |

### Example 4 — Capital asset (computer purchase)

`2026-04-18 ; APPLE STORE YORKDALE ; DEBIT ; MacBook Pro 16 ; -3,729.00 ; CAD`

CAD 3,729 including 13% HST: net = 3,729 / 1.13 = 3,300.00 and HST = 429.00. Assume the documented computer is used primarily in commercial activities and meets the ordinary capital-personal-property ITC conditions under s.199; on those assumptions, claim 429.00 on 106. A passenger vehicle instead requires the separate entity/use rules in Section 5.8; do not apply this computer result to a mixed-use vehicle. [199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html); [201](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-201.html); [202](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html).

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-18 | APPLE STORE | -3,729.00 | -3,300.00 | -429.00 | 13% HST | 106 | N | — | [ETA s.199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html) |

```oa-check
name: Computer invoice, supported 13% inclusive tax
inputs:
  gross: 3729
  rate: 0.13
steps:
  net: round(gross / (1 + rate), 2)
  tax: gross - net
expected:
  net: 3300
  tax: 429
```

### Example 5 — Export sale (zero-rated)

`2026-04-22 ; ACME CORP USA ; CREDIT ; Invoice CA-2026-018 IT consulting March ; +5,500.00 ; CAD`

Retain the hypothetical CAD 5,500 IT-consulting receipt. Consulting/advisory services fall under Schedule VI, Part V, s.23 if its conditions and exclusions are satisfied; s.5 instead concerns agency/arranging services. Confirm non-residency, the service classification and the s.23 exclusions before using zero-rating. Under that conditional scenario, report 5,500 on 101 and no output tax on 103; related ITCs still need commercial-use and documentation support. [export](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/4-5-3/exports-services-intangible-personal-property.html); [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html).

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-22 | ACME CORP USA | +5,500.00 | +5,500.00 | 0 | 0% | 101 (zero-rated) | Y | Q2 (HIGH) | "Verify non-resident status and zero-rating conditions" |

### Example 6 — Vehicle costs, restricted ITC

`2026-04-28 ; PETRO-CANADA ; DEBIT ; Fuel ; -92.00 ; CAD`

Fuel purchase. In Canada, there is no blanket block on vehicle expenses (unlike Malta). ITCs are claimable to the extent of business use. For a passenger vehicle, the taxpayer must track business vs personal kilometers. Conservative default: 0% ITC (personal use assumed). If the taxpayer maintains a logbook showing, say, 60% business use, 60% of the GST/HST is claimable.

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-28 | PETRO-CANADA | -92.00 | -92.00 | 0 | — | — | Y | Q3 | "Vehicle fuel: 0% ITC (no logbook). Provide km logbook for partial ITC." |

### 5.1 GST at 5% (ETA s.165(1))

- **GST rate** — 5%  _(ETA s.165(1))_
- **GST applicability** — Federal component of all taxable supplies. Applies in GST-only provinces (AB, BC, SK, MB, NT, NU, YT). In these provinces, only 5% GST applies on the GST34. Provincial taxes (BC PST, SK PST, MB RST) are separate filings.  _(ETA s.165(1))_

### 5.2 HST at harmonized rates (ETA s.165(2))

- **HST harmonized rule** — In harmonized provinces (ON 13%, NS 14%, NB 15%, NL 15%, PE 15%), the HST replaces GST. The full HST amount is reported on the GST34. There is no separate provincial filing for HST provinces.  _(ETA s.165(2))_

### 5.3 Place of supply (SOR/2010-117)

- **Place of supply rule** — The rate depends on where the supply is made. For tangible personal property: province where delivery occurs. For services: generally the province of the recipient's business address. For intangible personal property: province where the property may be used. Interprovincial supplies require transaction-level place-of-supply determination.  _(SOR/2010-117)_

### 5.4 Zero-rated supplies (ETA Schedule VI)

- **Zero-rated supplies** — Basic groceries (Part III), prescription drugs (Part I), medical devices (Part II), exports of goods (Part V), services to non-residents (the applicable Part V provision and exclusions must be identified; consulting/advisory services use s.23, not the agency provision s.5), international transport (Part VII), agricultural products (Part IV), financial services to non-residents (Part IX). Zero-rated means 0% tax but full ITC eligibility on related inputs.  _(ETA Schedule VI)_

### 5.5 Exempt supplies (ETA Schedule V)

- **Exempt supplies** — Financial services (Part VII; certain supplies to non-residents are zero-rated), long-term residential rent (Part I — short-term accommodation under one month and sales of new housing are taxable), health care services (Part II — but only listed services), educational services (Part III), childcare (Part IV), legal aid (Part V), public sector (Part VI). Exempt means no GST/HST charged and NO ITC on related inputs. If exempt supplies are significant → mixed-use apportionment required.  _(ETA Schedule V)_

### 5.6 Input tax credits (ETA s.169)

- **ITC documentation thresholds** — Obtain the prescribed information before claiming an eligible commercial-use ITC on 106. Under CAD 100: supplier/trading name, invoice date (or date tax paid/payable where no invoice) and total paid/payable. CAD 100–499.99: also supplier registration number, the prescribed tax amount/included-tax statement and exempt/taxable status where mixed. CAD 500 or more: also recipient/trading name, payment terms and a sufficient supply description. The regulation does not prescribe a purchaser-address field. [docs](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html); [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html).

### 5.7 Self-assessment on imported taxable supplies (ETA s.218)

- **Self-assessment on imports** — First apply the imported-taxable-supply definition in s.217. Ordinary services acquired exclusively in commercial activities are excluded (CRA generally uses 90% or more). Only where the applicable imported-supply rules impose tax is 405 used; determine any ITC independently rather than assuming a matching offset. Check normal versus simplified supplier registration; absence of charged tax alone is insufficient. [217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html); [rc](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html); [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html).

### 5.8 Capital personal property / passenger vehicles (ETA s.201–202)

- **CCA Class 10.1 ceiling** — Before-tax passenger-vehicle capital cost limit: CAD 38,000 for 2025 acquisitions and CAD 39,000 for 2026 acquisitions; s.201 links the ITC cost restriction to the applicable ceiling. [201](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-201.html); [car25](https://gazette.gc.ca/rp-pr/p2/2025/2025-10-08/html/sor-dors193-eng.html); [car26](https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html).
- **Passenger vehicle ITC limitation** — Establish the entity type, acquisition year and commercial use. For an individual/partnership, a nonexclusive-use passenger-vehicle purchase generally follows the annual CCA-based deemed-tax mechanism in s.202; do not claim acquisition tax merely by multiplying business-use percentage by the ceiling. Other entities follow their applicable primary-use rules. Leasing is a separate calculation; hold it until its conditions are established. [201](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-201.html); [202](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html).

### 5.9 Blocked ITCs (ETA s.170)

- **Blocked ITCs** — Apply the actual s.170 restrictions, including club memberships (with the exclusively-for-resale exception) and personal-consumption/benefit restrictions and their statutory exceptions. There is no general CAD 50 non-food promotional-gift ITC limit. Commercial-purpose promotional gifts remain subject to ordinary eligibility; food/entertainment and employee-benefit rules are separate. Passenger vehicles follow Section 5.8. [170](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-170.html); [rc](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html); [202](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html).

### 5.10 Meals and entertainment — 50% rule

- **50% ITC restriction on meals and entertainment** — The ordinary rule is 50% under ETA s.236 and ITA s.67.1. Meals included in convention fees do not escape it; allocate the meal portion, including the prescribed daily amount where not separately priced. Remote-work, fundraising and reimbursement exceptions require their particular statutory conditions; a category label alone does not establish full recovery. [236](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-236.html); [convention](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-expenses/convention-expenses.html); [mealsGuide](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-expenses.html).

### 5.11 Change in use — capital property (ETA s.195–199)

- **Change in use rule** — Identify property and entity type before applying a change-of-use rule. For ordinary capital personal property under s.199, primary-commercial-use thresholds and basic tax content govern the relevant deemed acquisition/supply; do not calculate every change as tax on current fair market value. Passenger vehicles and real property have separate rules; hold unresolved calculations for review. [199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html); [202](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html).

### 5.12 Small supplier threshold (ETA s.148)

- **Small supplier threshold** — $30,000 in any single calendar quarter or over four consecutive calendar quarters — measured on the worldwide taxable supplies (before expenses) of the person AND associated persons; excludes capital property, financial services, and goodwill on the sale of a business. Small-supplier status is lost immediately on exceeding $30,000 in a single quarter  _(ETA s.148)_
- **Small supplier registration rule** — For ordinary suppliers, apply the single-quarter or cumulative four-quarter timing in CRA’s registration table, including the following-month rule for a cumulative-only breach. The ordinary 29-day application period runs from the relevant taxable supply/effective date. Below-threshold mandatory-registration exceptions exist; do not infer no obligation solely from revenue. [reg](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html); [required](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/2-1/required-registration.html).

### 5.13 Bad debts (ETA s.231)

- **Bad debt recovery rule** — Section 231 relief on 107 requires, among other conditions, an arm’s-length supply, tax already reported/remitted, a debt written off in the books and the statutory proportional calculation and four-year limit. Include the corresponding adjustment if a relieved debt is recovered. Hold relief until these conditions are supported. [231](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-231.html).

### 5.14 Reporting sales on Line 101

- **Line 101 reporting rule** — Under the regular method used here, report sales and other revenue excluding GST/HST and provincial sales tax. Do not use the tax-inclusive Quick Method rule. Report collected/collectible GST/HST separately on 103. [lines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html).

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs

*Pattern:* Petro-Canada, Shell, Esso, Canadian Tire (auto), car payments. *Default:* 0% ITC (no logbook). *Question:* "Do you have a vehicle logbook showing business vs personal kilometers?"

### 6.2 Meals and entertainment

*Pattern:* restaurants, Tim Hortons, Starbucks, The Keg. *Default:* block. *Question:* "Was this a business meal? If yes, 50% of the GST/HST is claimable as ITC."

### 6.3 Home office expenses

*Pattern:* utility bills, internet at home. *Default:* 0% ITC. *Question:* "Do you work from home? What percentage of your home is used exclusively for business?"

### 6.4 Round-number incoming transfers

*Pattern:* large round credit from owner name. *Default:* exclude as owner injection. *Question:* "Is this a customer payment, owner contribution, or loan?"

### 6.5 Incoming from individuals

*Pattern:* incoming from private names. *Default:* taxable sale at provincial HST rate, Line 101/103. *Question:* "Was it a sale? What was supplied?"

### 6.6 Interprovincial sales

*Pattern:* incoming from counterparty in different province. *Default:* rate of recipient's province. *Question:* "Confirm the province of the customer for place-of-supply determination."

### 6.7 Large purchases (potential capital asset)

*Pattern:* single purchase > CAD 1,000. *Default:* current expense on Line 106. *Question:* "Is this a capital asset with useful life > 1 year?"

### 6.8 Mixed-use phone, internet

*Pattern:* Rogers, Bell, Telus personal lines. *Default:* 0% if mixed. *Question:* "Is this a dedicated business line or mixed-use?"

### 6.9 Outgoing to individuals

*Pattern:* outgoing to private names. *Default:* exclude as draws. *Question:* "Was this a contractor payment, salary, refund, or personal transfer?"

### 6.10 Cash withdrawals

*Pattern:* ATM, cash withdrawal. *Default:* exclude. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* monthly rent to landlord. *Default:* commercial (taxable, ITC eligible). *Question:* "Is this a commercial or residential lease?"

### 6.12 Amazon.ca purchases

*Pattern:* Amazon.ca, AMZN. *Default:* taxable domestic at HST rate. *Question:* "Was this a business purchase? Check invoice for GST/HST breakdown."

### 6.13 Stripe/PayPal incoming

*Pattern:* Stripe payouts, PayPal transfers. *Default:* sales revenue at provincial rate, Line 101/103. *Question:* "Are these customer payments? What province are your customers in?"

### 6.14 Tips and gratuities

*Pattern:* restaurant charges with tip component. *Default:* distinguish voluntary tips (not subject to GST/HST) from mandatory service charges (taxable consideration). *Question:* "Which part is a voluntary tip and which part is a mandatory service charge?" [CRA special cases](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-special-cases.html).

### 6.15 US dollar transactions

*Pattern:* USD amounts on bank statement. *Default:* convert to CAD at Bank of Canada daily rate. *Question:* "Confirm the CAD equivalent shown on the bank statement."

## Section 7 — Excel working paper template (Canada-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Canada-specific overlay.

### Sheet "Transactions"

Keep the base A–L columns: G = rate, H = treatment/allocation IDs, I = treatment label. Do not overwrite I with a rate or use G as a text treatment criterion. Add a linked **Return Allocations** table with stable transaction/allocation IDs, return line and a signed CAD return amount. One transaction may have separate eligible allocations to several lines; prevent duplicates. Source debits may be negative in Transactions, but positive eligible purchase tax must be normalized to a positive 106 credit; recovery/debit adjustments retain the correct return sign. An imported-service liability, when actually due, has its own 405 allocation; any eligible 106 credit is separate. [lines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html); [form](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf).

### Sheet "Line Summary"

- **Line Summary sheet formulas** — Sum the signed **Return Allocations** amounts by return line (for example, `=SUMIFS(ReturnAllocations[ReturnAmountCAD],ReturnAllocations[Line],"106")`). Use separate allocations for tax-exclusive 101 revenue, 103 output tax, eligible 106 ITCs and any 405 liability. Compute 105 = 103 + 104; 108 = 106 + 107; 109 = 105 − 108; 112 = 110 + 111; 113A = 109 − 112; 113B = 205 + 405; 113C = 113A + 113B. Do not sum raw bank credits as 101 or negative bank-debit tax directly as 106. [lines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html); [form](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf).

### Sheet "Return Form"

- **Return Form final figures** — Carry final 113C (109 − 110 − 111 + 205 + 405) to the refund/payment decision: positive → amount owing on 115; negative → refund on 114. Do not stop at 113A when other debits exist. [form](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf).

### Mandatory recalc step

After building the workbook, recalculate every formula and cache the results so the
values can be read back. On a normal machine, recalc with LibreOffice headless:

```bash
soffice --headless --convert-to xlsx --outdir /tmp /mnt/user-data/outputs/canada-gst-hst-<period>-working-paper.xlsx
```

Then re-open the converted file and confirm no cell shows a formula error before
presenting it.

## Section 8 — Canadian bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Canada-specific patterns.

**RBC Royal Bank online export format.** CSV export from RBC Online Banking. Columns: Account Type, Account Number, Transaction Date, Cheque Number, Description 1, Description 2, CAD$, USD$. Date format: MM/DD/YYYY. Amounts are positive for credits, negative for debits. Description 1 contains the transaction type (e.g., "POS Purchase", "Online Banking Transfer", "Direct Deposit"). Description 2 contains the counterparty/payee name.

**TD Canada Trust online export format.** CSV from EasyWeb. Columns: Date, Transaction Description, Debit, Credit, Balance. Date format: MM/DD/YYYY. The Transaction Description field combines type and payee (e.g., "POS W/D SHOPIFY COMMERCE INC", "INTERAC E-TRANSFER FROM JOHN SMITH"). "POS W/D" = point-of-sale withdrawal (debit). "PREAUTH PYMT" = pre-authorized payment.

**Scotiabank export format.** CSV from Scotia OnLine. Columns: Date, Description, Withdrawals, Deposits, Balance. Date format: DD/MM/YYYY (different from RBC/TD).

**BMO export format.** CSV from BMO Online Banking. Columns: Transaction Date, Description, Amount. Single amount column (negative for debits).

**CIBC export format.** CSV or QFX from CIBC Online. Columns: Date, Description, Debit, Credit. Date format: YYYY-MM-DD.

**Common Canadian bank statement patterns**

| Term | Meaning |
| --- | --- |
| POS, POS W/D, POS PURCHASE | Point-of-sale debit card purchase |
| PREAUTH, PREAUTH PYMT, PAP | Pre-authorized payment (direct debit) |
| INTERAC E-TRANSFER | Interac e-Transfer (incoming or outgoing) |
| ONLINE BANKING TRANSFER, TFR | Online transfer |
| DIRECT DEPOSIT, DIR DEP | Direct deposit (incoming) |
| CRA FED, RECEIVER GENERAL | CRA tax payment |
| NSF, NSF FEE | Non-sufficient funds fee (bank charge — exempt) |
| MONTHLY FEE, SERVICE CHARGE | Bank account fees (exempt) |
| INTL PURCHASE, FX FEE | International purchase and foreign exchange fee |
| ABM W/D, ATM | Cash withdrawal |

**Internal transfers.** Own-account transfers between client's RBC, TD, savings accounts. Labelled "online banking transfer", "TFR", or matching account numbers. Always exclude.

**Self-employed draws.** Transfers from business account to personal account labelled with the owner's name. Exclude.

**HST on bank statement lines.** Canadian invoices are GST/HST-inclusive on the bank statement. To extract the GST/HST component: Tax = Gross * Rate / (1 + Rate). Example: CAD 113.00 at 13% HST → Tax = 113 * 0.13 / 1.13 = 13.00.

**Interac e-Transfers.** Very common in Canada for B2B and B2C. The description shows "INTERAC E-TRANSFER FROM [name]" for incoming and "INTERAC E-TRANSFER TO [name]" for outgoing. Default treatment: incoming = potential sale (ask), outgoing = potential contractor payment or personal (ask).

**Foreign currency.** Convert to CAD using the Bank of Canada daily exchange rate. Note the rate in column L.

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type

*Inference rule:* "Inc", "Corp", "Ltd" = corporation; personal name = sole proprietor. *Fallback:* "Are you a sole proprietor, partnership, or corporation?"

### 9.2 GST/HST registration

*Inference rule:* if asking for a GST34, they are registered. *Fallback:* "Are you registered for GST/HST? What is your Business Number (BN)?"

### 9.3 Province

*Inference rule:* bank branch, counterparty mix, area codes in descriptions. *Fallback:* "What province is your principal place of business?"

### 9.4 Filing period

*Inference rule:* transaction date range. *Fallback:* "Is this for a monthly, quarterly, or annual period? What are the period dates?"

### 9.5 Accounting method

*Inference rule:* if no mention of Quick Method, assume regular. *Fallback:* "Are you using the regular method or the Quick Method (election GST74)?"

### 9.6 Industry

*Inference rule:* counterparty mix. *Fallback:* "In one sentence, what does the business do?"

### 9.7 Employees

*Inference rule:* CPP/EI/payroll outgoing. *Fallback:* "Do you have employees?"

### 9.8 Exempt supplies

*Inference rule:* financial/medical/educational/residential rental income patterns. *Fallback:* "Do you make any GST/HST-exempt supplies?"

### 9.9 Interprovincial sales

*Inference rule:* counterparties in multiple provinces. *Fallback:* "Do you sell to customers in provinces other than your own?"

### 9.10 Prior period balance

*Not inferable. Always ask.* "Do you have any GST/HST balance owing or credit from the previous period?"

## Section 10 — Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the three-tier OpenAccountants architecture. Canada-specific content (rates, line mappings, ITC rules, place of supply) is based on the Excise Tax Act as of April 2026 including the Nova Scotia HST rate change to 14% effective April 1, 2025.

### Sources

**Primary legislation:**
1. Excise Tax Act (R.S.C., 1985, c. E-15), Part IX — s.123 (definitions), s.148 (small supplier), s.165 (imposition), s.169 (ITCs), s.170 (restrictions), s.218 (self-assessment), Schedule V (exempt), Schedule VI (zero-rated)
2. Input Tax Credit Information (GST/HST) Regulations — documentation thresholds
3. Place of Supply (GST/HST) Regulations (SOR/2010-117)
4. New Harmonized Value-added Tax System Regulations

**CRA guidance:**
5. GST34 form and guide (RC4022) — canada.ca
6. Quick Method guide (RC4058)
7. GST/HST Memoranda Series — various technical interpretations
8. GST/HST Info Sheets — place of supply, ITCs, specific industries

**Other:**
9. Bank of Canada daily exchange rates — bankofcanada.ca
10. CRA My Business Account — business registration verification

## Sources

### Correction sources (operative reads reused from 21 November 2026)

These linked readings support only the corrected claims, not full clearance of unchanged content. The 2025/2026 vehicle-limit readings were completed in the earlier linked tax research and applied in the 21 November GST/HST report.

| Correction | Official source | Read date |
| --- | --- | --- |
| lines | [lines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) | 2026-11-21 |
| form | [form](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) | 2026-11-21 |
| place | [place](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) | 2026-11-21 |
| itc | [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html) | 2026-11-21 |
| rc | [rc](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html) | 2026-11-21 |
| export | [export](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/4-5-3/exports-services-intangible-personal-property.html) | 2026-11-21 |
| convention | [convention](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-expenses/convention-expenses.html) | 2026-11-21 |
| dates | [dates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) | 2026-11-21 |
| docs | [docs](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html) | 2026-11-21 |
| car25 | [car25](https://gazette.gc.ca/rp-pr/p2/2025/2025-10-08/html/sor-dors193-eng.html) | 2026-11-21 |
| car26 | [car26](https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html) | 2026-11-21 |
| recapture | [recapture](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/gi-165/prince-edward-island-transition-harmonized-sales-tax-builders-recaptured-input-tax-credits.html) | 2026-11-21 |
| municipal | [municipal](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4049/gst-hst-information-municipalities.html) | 2026-11-21 |
| reg | [reg](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html) | 2026-11-21 |
| required | [required](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/2-1/required-registration.html) | 2026-11-21 |
| mealsGuide | [mealsGuide](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-expenses.html) | 2026-11-21 |
| fx | [fx](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/3-6/conversion-foreign-currency.html) | 2026-11-21 |
| 170 | [170](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-170.html) | 2026-11-21 |
| 199 | [199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html) | 2026-11-21 |
| 201 | [201](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-201.html) | 2026-11-21 |
| 202 | [202](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html) | 2026-11-21 |
| 217 | [217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html) | 2026-11-21 |
| 231 | [231](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-231.html) | 2026-11-21 |
| 236 | [236](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-236.html) | 2026-11-21 |

### Known gaps

1. Quebec QST is entirely refused — a separate skill is needed.
2. BC PST, SK PST, MB RST are refused — separate provincial skills needed.
3. Quick Method is refused — could be added as a v2.1 feature.
4. First Nations exemptions are refused — specialized knowledge required.
5. Real property self-supply rules (s.191) are refused — too fact-sensitive.
6. The NS HST rate changed to 14% on April 1, 2025 — verify no further rate changes.
7. Interprovincial place-of-supply for digital services is evolving — flag for reviewer if significant.
8. The s.218 self-assessment landscape is changing as more non-residents register voluntarily — always check the invoice first.

### Change log

- **v2.1 (23 November 2026, draft correction):** Correct return lines, regular-method revenue, imported-service and simplified-regime treatment, documentation tiers, vehicle/gift/meal/change-of-use rules, export authority, examples and return-allocation formulas using the existing 21 November findings. Existing approval fields are preserved for accountant sign-off; this edit does not itself re-attest the changed version.

- **v2.0 (April 2026):** Full rewrite to align with three-tier OpenAccountants architecture. 10-section Malta v2.0 structure adopted. Supplier pattern library added (Section 3). Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue added (Section 6). Excel template added (Section 7). Bank statement guide with RBC/TD/BMO/CIBC formats added (Section 8). Onboarding moved to fallback (Section 9).
- **v2.0 (prior, April 2026):** Previous version with inline tier tags. Superseded.

### Self-check (v2.0)

1. Quick reference at top with rate table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 15 sub-tables).
3. Worked examples (hypothetical ON IT consultant): yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 14 rules).
5. Tier 2 catalogue compressed: yes (Section 6, 15 items).
6. Excel template with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only: yes (Section 9, 10 items).
8. All 8 Canada-specific refusals present: yes (Section 2, R-CA-1 through R-CA-8).
9. Reference material at bottom: yes (Section 10).
10. Self-assessment s.218 explicit: yes (Section 3.8 + Section 5.7 + Example 1).
11. Meals 50% rule explicit: yes (Section 5.10 + Example 3).
12. Vehicle logbook requirement explicit: yes (Example 6).
13. Place of supply rules documented: yes (Section 5.3).
14. HST rate table complete with NS 14%: yes (Section 1).
15. Zero-rated vs exempt distinction explicit: yes (Section 5.4–5.5).

## End of Canada GST/HST Return Skill v2.1

This skill is incomplete without the companion workflow file loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture). Do not attempt to produce a GST34 without it loaded.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
