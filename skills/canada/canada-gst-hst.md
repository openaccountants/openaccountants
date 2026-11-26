---
name: canada-gst-hst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Canadian GST/HST return (Form GST34) for a self-employed individual or small business in Canada. Trigger on phrases like "prepare GST return", "file HST", "Canadian sales tax", "GST/HST return", "Form GST34", "input tax credits", "ITC claim", or any request involving Canadian GST/HST filing. Also trigger when classifying transactions for GST/HST purposes from bank statements, invoices, or other source data. This skill covers federal GST and harmonized HST provinces only under the regular method. Quebec QST, Saskatchewan PST, Manitoba RST, British Columbia PST, Quick Method, and simplified method for charities are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any Canadian GST/HST work.
version: 2.2
jurisdiction: CA
tax_year: 2026
tax_year_notes: "2026 regular-method workflow and preserved April 2026 hypothetical examples. The stated 2025 vehicle-acquisition limit is historical; 2026 vehicle-limit cases are referred for accountant determination."
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Nathan Wiebe"
reviewed_on: 2026-11-03
tier: 1
domain: vat-gst
---

# Canada GST HST

## Canada GST/HST Return Skill (Form GST34) v2.2

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content.**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Canada |
| Federal GST rate | 5%  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |
| HST rates by province | ON 13%, NS 14% (effective Apr 1 2025), NB 15%, NL 15%, PE 15%  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |
| GST-only provinces | AB, BC, SK, MB, QC, NT, NU, YT (5% GST; BC/SK/MB/QC have separate provincial sales taxes)  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |
| Zero rate | 0% only where the specific Schedule VI entry applies; see Section 5.4. [165(3)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html) |
| Exempt | Apply the particular Schedule V entry and its conditions; see Section 5.5. [123](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html) |
| Return form | GST34 (GST/HST Return for Registrants) |
| Filing portal | CRA My Business Account (canada.ca) |
| Authority | Canada Revenue Agency (CRA) |
| Currency | CAD only |
| Filing frequencies | Obtain the actual CRA-assigned period and elections. Ordinary annual eligibility uses the section 249 threshold not exceeding CAD 1,500,000; the ordinary monthly threshold is over CAD 6,000,000, with quarterly periods otherwise, subject to 245/247/248 and effective elections. The 249 threshold annualizes the relevant prior fiscal year and includes associates; it excludes financial services, capital-real-property sales, Part V Schedule VI supplies and business goodwill as specified there. [245](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-245.html); [248](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-248.html); [249](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-249.html) |
| Deadline | Monthly/quarterly: one month after period end; ordinary annual: three months after fiscal year-end. June 15 filing / April 30 payment applies to an annual-filer individual with business income, a December 31 year-end and an income-tax filing-due date of June 15 under 238(1)(a)(ii); weekends/recognized holidays move the deadline to the next business day. [dates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html). |
| Small supplier threshold | $30,000 in any single calendar quarter or in the last four consecutive calendar quarters (ETA s.148) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Community |

**Key GST34 lines**

These are official working-copy line references. The working copy is for records, not for filing or payment. Use the actual return interface: the electronic instructions calculate105 from 103/104 and108 from 106/107; TELEFILE omits some component fields. [Working copy](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf); [CRA instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html).

| Line | Meaning |
| --- | --- |
| 101 | Total sales and other revenue (before GST/HST) |
| 103 | GST/HST collected or collectible |
| 104 | Adjustments to GST/HST (e.g., bad debt recovery, change-in-use) |
| 105 | Total GST/HST and adjustments (= 103 + 104) |
| 106 | Input tax credits (ITCs) |
| 107 | Adjustments deducted in determining net tax, including eligible bad-debt relief; not a recaptured-ITC debit. [lines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html). |
| 108 | Total ITCs and adjustments (= 106 + 107) |
| 109 | Net tax (= 105 − 108), before other credits and debits; use 113C for the final payable/refundable balance. [Working copy](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) |
| 110 | Instalments paid |
| 111 | Rebates only where the rebate form permits claiming them on this line. [Working copy](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) |
| 112 | Total other credits (= 110 + 111) |
| 113A / 113B / 113C | 113A = 109 − 112; 113B = 205 + 405; final balance 113C = 113A + 113B. [form](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf). |
| 114 | Refund claimed when final line 113C is negative |
| 115 | Amount owing when final line 113C is positive |

**Ordinary non-zero-rated GST/HST supplies: standard rates after establishing the province**

| Province/Territory | Rate | Components | Effective |
| --- | --- | --- | --- |
| Alberta (AB) | 5% | GST only | —  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |
| British Columbia (BC) | 5% GST | Separate PST is outside this return | —  [ETA165](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html) |
| Manitoba (MB) | 5% GST | Separate RST is outside this return | —  [ETA165](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html) |
| New Brunswick (NB) | 15% HST | Harmonized | —  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |
| Newfoundland & Labrador (NL) | 15% HST | Harmonized | —  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |
| Northwest Territories (NT) | 5% | GST only | —  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |
| Nova Scotia (NS) | 14% HST | Harmonized | Apr 1, 2025  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |
| Nunavut (NU) | 5% | GST only | —  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |
| Ontario (ON) | 13% HST | Harmonized | —  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |
| Prince Edward Island (PE) | 15% HST | Harmonized | —  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |
| Quebec (QC) | 5% GST | Separate QST is outside this return | —  [ETA165](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html) |
| Saskatchewan (SK) | 5% GST | Separate PST is outside this return | —  [ETA165](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html) |
| Yukon (YT) | 5% | GST only | —  [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Hold the rate and affected return allocation until place of supply is established; do not default to Ontario. [place](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html). |
| Unknown GST/HST status of a purchase | Obtain the invoice and applicable rule before claiming an ITC |
| Unknown province of supply | Obtain supply/delivery/recipient-address evidence; registration province alone is insufficient. [place](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html). |
| Unknown business-use proportion (vehicle, phone, home office) | Establish and document the applicable use test before claiming |
| Unknown whether personal or business expense | Obtain the purpose/use evidence before allocating tax |
| Unknown blocked-input status (club dues, personal) | Apply the actual restriction and its exceptions |
| Unknown whether transaction is in scope | Establish the supply and scope before allocating |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — a usable bank/payment-account statement for the full period in CSV, PDF or pasted text, plus the sales and purchase records needed to establish the tax treatment and tax point. Inspect the supplied format rather than assuming a provider-specific layout.

**Recommended** — sales invoices for the period, especially for exports/interprovincial supplies, the GST/HST account number and purchase documents for every claimed ITC. The statutory documentation tiers are under CAD 100, CAD 100–499.99 and CAD 500 or more (Section 5.6). [docs](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html).

**Ideal** — complete sales journal, purchase journal, prior period GST34, Quick Method election (if applicable — but then R-CA-3 fires).

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. A bank-only working paper is provisional: hold every unsupported ITC and unestablished place-of-supply conclusion. The reviewer brief must identify the missing invoice/source documents for each affected claim; no internal review threshold excuses the statutory information requirements. [docs](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html); [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html).

### Canada-specific refusal catalogue

These are scope referrals, not a substitute for a transaction’s statutory classification. For any triggered case below, check this with one of our partner accountants.

- **R-CA-1 — Quebec QST / Quebec-specific filing routes:** QST is outside this CRA GST34 workflow. For a Quebec-based filer, establish the correct filing route with the partner before preparing the return.
- **R-CA-2 — Provincial sales taxes:** BC PST, Saskatchewan PST and Manitoba RST calculations/returns are outside this federal GST/HST workflow.
- **R-CA-3 — Quick Method:** this skill uses the regular method; obtain the actual election rather than assuming the method.
- **R-CA-4 — Special charity/NPO/public-service-body calculations:** their special net-tax methods and rebates are outside this ordinary-business workflow.
- **R-CA-5 — Indigenous-specific treatment:** obtain the relevant facts and refer rather than assigning an exemption from a name or address.
- **R-CA-6 — Closely related group elections:** refer the group’s special intercompany treatment.
- **R-CA-7 — Non-resident simplified-regime returns:** do not prepare those returns with this skill. An ordinary registrant’s purchases from such a supplier follow Section 3.8.
- **R-CA-8 — Real-property transactions:** self-supply, property change-of-use and rebate calculations require the partner’s applicable treatment before their resulting amounts enter the working paper.

## Section 3 — Classify the supply, not the supplier name

A bank description is an evidence lead, not a tax determination. Use the invoice, contract, tax point, registration details, commercial use and applicable statutory provision before allocating tax. ETA 169(4) requires “sufficient evidence” before the credit is claimed; section 169(1) limits the credit by commercial use. [169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html).

### 3.1 Canadian banks

Identify the actual fee or financial transaction. A financial service within ETA 123(1), after its exclusions, is exempt under Schedule V Part VII section 1 unless included in Schedule VI Part IX. A bank name alone establishes neither classification. For an unfamiliar fee or an export of financial services, check this with one of our partner accountants. [123](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html); [Schedule V](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-sched200860.html).

### 3.2 Government and statutory bodies

Obtain the tax notice, assessment, fee invoice or grant agreement and reconcile the payment. A government payee is not sufficient evidence of a particular supply or tax treatment.

### 3.3 Utilities and telecommunications

Use the actual invoice and supply location. Separate commercial use from private use before considering an ITC; do not assign a rate from a utility or telephone company’s name.

### 3.4 Insurance

Separate the insurance contract from any additional service or charge. For a classification beyond the verified ordinary rules in this skill, check this with one of our partner accountants.

### 3.5 Post and logistics

Obtain the postage or courier invoice, delivery details and applicable supply rule. Standard letter mail is not categorically exempt: CRA’s Ontario stamp example charges Ontario HST. [CRA postage](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html).

### 3.6 Transport

Municipal transit qualifying under Schedule V Part VI sections 1 and 24 is exempt: the defined service is public passenger transportation, or an exclusive right to use it, supplied by a qualifying transit authority; charters and tour services are excluded. Section 24 excludes supplies made to a transit authority and separately covers the specified passenger rights and Minister-designated services. For a reseller, transit-authority transaction, international journey, charter or tour, check this with one of our partner accountants. Do not infer zero-rating from a carrier’s name or the word “international”. [Schedule V](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-sched200860.html).

### 3.7 Food retail

Separate invoice lines and establish the business purpose. A supermarket or restaurant name does not identify a Schedule VI product or establish an eligible business meal; use Section 5.10 for the ordinary meal rule.

### 3.8 Non-resident software and services

Establish the actual supplier and registration regime from the invoice and supporting records. Apply Section 5.7 to the actual supply and use.

A normal GST/HST registrant cannot claim an ITC for a charge under the simplified digital-economy regime. ETA 211.17(1) prohibits an “input tax credit”; the section’s specified refund/correction exceptions are separate. Give the supplier the recipient’s normal registration details and address an incorrect charge with the supplier. [211.17](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-211.17.html).

### 3.9 Domestic software and suppliers

Check the actual invoice, place of supply, registration and eligible use. A supplier’s headquarters does not determine the customer’s tax rate.

### 3.10 Payment processors

Separate settlement principal, the merchant’s sales, fees, hardware and subscriptions. Do not classify all Interac, Stripe, PayPal or other processor fees as exempt. ETA 123(1), financial-service paragraph (r.6), excludes the specified payment-card-network-operator authorization, clearing/settlement and related services, other than a prescribed service. This does not classify every merchant-acquirer fee. For a fee requiring a separate financial-service analysis, check this with one of our partner accountants. [123](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html).

### 3.11 CRA payments and refunds

Match the amount to the account notice and ledger. Separate tax settlements, refunds, grants and any consideration for supplies rather than applying one treatment to every CRA-labelled entry.

### 3.12 Professional services

Check the service, invoice and commercial use. An accountant’s, lawyer’s or consultant’s title does not establish the customer’s ITC entitlement. Apply Sections 5.6 and 5.9.

### 3.13 Payroll

Reconcile the payroll run to the payroll records and identify any separate processing-service invoice. A payment processor’s name alone does not distinguish wages from fees.

### 3.14 Property and rent

Obtain the lease, invoices and occupancy/use facts. Do not default an unidentified payment to commercial, taxable or ITC-eligible rent. For the applicable residential, short-stay, condominium or real-property exemption, check this with one of our partner accountants.

### 3.15 Internal transfers and owner transactions

Match both sides of a proposed own-account transfer and reconcile the owner/loan accounts. Confirm whether an unidentified receipt or payment is a sale, loan, draw or supplier transaction. A cash withdrawal needs evidence of the eventual expense.

## Section 4 — Worked examples

These six examples preserve the transactions in a hypothetical bank statement of an Ontario-based self-employed software consultant. Where an invoice or use evidence is absent, the result remains a provisional working-paper entry.

### Example 1 — Non-resident SaaS, commercial-use exclusion (Notion)

`2026-04-03 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; CAD 21.89`

Retain the hypothetical USD16.00 / CAD21.89 invoice. Assume the Ontario consultant is a normal regular-method registrant, not a financial institution or special-method registrant; the supply is an ordinary service made outside Canada, with no charged GST/HST and exclusively commercial use. The ordinary service is excluded from imported taxable supplies under s.217: no federal imported-service tax on 405 and no ITC for tax that was neither charged nor payable. On these ordinary regular-method, non-financial, exclusively commercial assumptions, there is also no provincial imported-supply charge under 218.1; the 220.08(3)/Schedule X Part II section 1 exclusion also applies if the separate interprovincial rule is relevant. Section 5.7 states the operative conditions. CAD 21.89 × 13% = CAD 2.85 is arithmetic only, not a liability. If the commercial-use exclusion fails, determine the imported-supply liability and ITC separately before allocating it. [217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html); [rc](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html).

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line (self-assess) | Line (ITC) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-03 | NOTION LABS INC | -21.89 | -21.89 | 0 | — | — | — | Y | Confirm the stated supply/use assumptions | No federal or provincial self-assessment on those assumptions. [ETA s.217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html) |

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

For an ordinary eligible business meal, ETA 236 gives the corresponding adjustment and CRA permits the methods in Section 5.10: ordinary net GST/HST recovery is 50%. [ETA s.236](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-236.html). Without the business-purpose and invoice evidence, claim no ITC in the provisional working paper; this does not establish that the actual expense is personal or that no tax was charged. If confirmed as eligible business entertainment, the ordinary result is 50% net GST/HST recovery.

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-15 | THE KEG STEAKHOUSE | -285.00 | Awaiting invoice | Awaiting invoice | Awaiting invoice | No ITC claimed | Y | Q1 | Purpose/invoice evidence required. [169(4)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html) |

### Example 4 — Capital asset (computer purchase)

`2026-04-18 ; APPLE STORE YORKDALE ; DEBIT ; MacBook Pro 16 ; -3,729.00 ; CAD`

CAD 3,729 including 13% HST: net = 3,729 / 1.13 = 3,300.00 and HST = 429.00. Assume the documented computer is used primarily in commercial activities and meets the ordinary capital-personal-property ITC conditions under s.199; on those assumptions, claim 429.00 on 106. A passenger vehicle instead requires the separate entity/use rules in Section 5.8; do not apply this computer result to a mixed-use vehicle. [199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html); [201](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-201.html); [202](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html).

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-18 | APPLE STORE | -3,729.00 | -3,300.00 | -429.00 | 13% HST | 106 [ETA s.199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html) | N | — | — |

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

Retain the hypothetical CAD 5,500 IT-consulting receipt. Consulting/advisory services fall under Schedule VI, Part V, s.23 if its conditions and exclusions are satisfied; s.5 instead concerns agency/arranging services. For this conditional example, assume the recipient is non-resident, the supply is IT consulting and none of the four section 23 exclusions listed in Section 5.4 applies; obtain that evidence for an actual client before using zero-rating. Under that conditional scenario, report 5,500 on 101 only if it is revenue of the actual reporting period and was not already reported, and no output tax on 103; the April receipt alone does not assign the March services to an April return; related ITCs still need commercial-use and documentation support. [export](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/4-5-3/exports-services-intangible-personal-property.html); [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html).

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-22 | ACME CORP USA | +5,500.00 | +5,500.00 | 0 | 0% | 101, if revenue of this reporting period (zero-rated) | Y | Q2 (HIGH) | "Verify non-resident status and zero-rating conditions"  [PartV23](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-sched201390.html) |

### Example 6 — Vehicle costs, restricted ITC

`2026-04-28 ; PETRO-CANADA ; DEBIT ; Fuel ; -92.00 ; CAD`

For ordinary operating fuel, section 169(1)(c) uses the eligible commercial-use share; do not apply the passenger-vehicle acquisition formula to fuel. Establish the invoice tax and support the commercial-use share with usage records. A supported 60% eligible commercial share gives 60% of otherwise eligible fuel tax. Until the evidence is obtained, claim no ITC in the provisional working paper; do not infer personal use or zero invoice tax. [169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html).

**Output table**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-28 | PETRO-CANADA | -92.00 | Awaiting invoice | Awaiting invoice | Awaiting invoice | No ITC claimed | Y | Q3 | Invoice and eligible commercial-use evidence required. [169(4)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html) |

## Section 5 — Rules used by this workflow

### 5.1 Federal GST

For an ordinary taxable supply made in Canada, ETA 165(1) imposes 5% on the consideration, subject to the Act’s exceptions. Zero-rated supplies instead have the 0% rate under 165(3); do not charge 5% merely because a supply is taxable. [165](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html).

### 5.2 HST

In a participating province,165(2) adds its provincial part to the federal part. Ontario’s 8% provincial part gives 13% combined; the prescribed 9% for Nova Scotia gives 14%, and the prescribed 10% for New Brunswick, Newfoundland and Labrador and Prince Edward Island gives 15%. The prescribed rates take priority over the Schedule VIII fallback under 123(1), definition “tax rate”. Report the combined HST on the federal return. [Ontario/Schedule VIII](https://laws-lois.justice.gc.ca/eng/acts/E-15/page-123.html#h-201840); [NS](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/section-33.6.html); [NB](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/section-33.4.html); [NL](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/section-33.5.html); [PEI](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/section-33.3.html).

### 5.3 Place of supply

Identify the supply type before selecting its rule. For a general service within SOR/2010-117 section 13(1), use the sole Canadian home/business recipient address obtained in the ordinary course, or, if there is more than one, the one most closely connected to the supply; otherwise use the Canadian recipient address obtained in the ordinary course that is most closely connected with the supply. Do not use the supplier’s headquarters or an unsupported customer-province default. The no-address rule in 13(2), special services under 14–17, goods, leases, intangible rights and transportation require their applicable tests: check these with one of our partner accountants before assigning a rate. [13](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/section-13.html).

### 5.4 Zero-rated supplies (ETA Schedule VI)

Only a supply that falls within a Schedule VI entry is zero-rated: ETA 123(1) defines it as “a supply included in Schedule VI”, and section 165(3) sets its rate at 0%. A shop, product-category or overseas-customer label does not establish the entry’s conditions. Eligible related ITCs still follow section 169 and its restrictions. For a particular grocery, drug, device, agricultural, transport or financial-service exemption outside the verified rule below, check this with one of our partner accountants. [123](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html); [165](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html); [169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html).

For the consulting example, Schedule VI Part V section 23 covers a qualifying advisory, professional or consulting service to a non-resident. Its exclusions concern: services to an individual for Canadian litigation, except before proceedings commence; Canadian real property; tangible personal property in Canada when the service is performed; and agency/arranging/procuring/soliciting services. Do not substitute the conditions of the separate agency provision in section 5. [Part V23](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-sched201390.html).

### 5.5 Exempt supplies (ETA Schedule V)

ETA 123(1) defines an exempt supply as “a supply included in Schedule V”. Ordinary inputs used only in making exempt supplies do not meet the commercial-activity component of the section 169 ITC test; allocate mixed commercial/exempt use under the applicable rule. Do not classify all financial, health, education, childcare, legal-aid or public-sector supplies by a broad category name. For the particular Schedule V entry and its conditions, check this with one of our partner accountants. Residential, short-stay and condominium transactions follow the referral in Section 3.14. [123](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html); [169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html).

### 5.6 Input tax credits (ETA s.169)

For a person other than a financial institution, apply the actual/intended-use deeming rules in ETA 141(1)–(4): substantially all commercial use is deemed all commercial, and substantially all noncommercial use is deemed all noncommercial. Section 141(5) separately treats a residential complex and the other part of mixed property, limiting related-input deeming to the other part. For that mixed-property calculation, check this with one of our partner accountants; the workspace conditions in 170(1)(a.1) still need their own test. [141](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-141.html).

- **ITC documentation thresholds** — Obtain the prescribed information before claiming an eligible commercial-use ITC on 106. Under CAD 100: supplier/trading name, invoice date (or date tax paid/payable where no invoice) and total paid/payable. CAD 100–499.99: also supplier registration number, the prescribed tax amount/included-tax statement and, where two or more supplies have different status, an indication of the status of each taxable supply that is not zero-rated. Tax-included amounts require the prescribed tax-included statement and total tax rate under s.3(b)(iv). CAD 500 or more: also recipient/trading name, payment terms and a sufficient supply description. The regulation does not prescribe a purchaser-address field. [docs](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html); [itc](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html).

### 5.7 Self-assessment on imported taxable supplies

For an ordinary service or intangible personal property made outside Canada to a Canadian resident, first apply ETA 217, imported-taxable-supply paragraphs (a) or (c). These exclude an acquisition for consumption, use or supply exclusively in commercial activities. Absence of tax on an invoice is not itself a self-assessment test. Section 218 imposes federal 5% tax only on an imported taxable supply; section 218.1(1)(a) likewise requires an imported taxable supply for its provincial charge. [217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html); [218](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.html); [218.1](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.1.html).

Separately, where a service or intangible property is supplied in another Canadian province, test220.08. Section 220.08(3)(a) and Schedule X Part II section 1 exempt a qualifying ordinary registrant’s exclusively commercial acquisition from that provincial charge. The Schedule X condition excludes the specified charity/streamlined-method registrants. Regulation SOR/2010-151 section 14 prescribes the Part II section 4 litigation supply only when it does not also fall in another Part II section; it does not undo the qualifying section 1 exclusion. [220.08](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-220.08.html); [Schedule X](https://laws-lois.justice.gc.ca/eng/acts/E-15/page-125.html#h-201977); [regulation14](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-151/section-14.html).

Thus the exclusively commercial ordinary-service assumptions in Example 1 establish no federal or provincial self-assessment; a matching 106 credit must not be invented. For a noncommercial/mixed-use import, financial institution, prescribed special supply or special accounting regime, check this with one of our partner accountants before computing liability. Where tax is legally payable, determine its reporting and any eligible ITC separately. Before claiming an ITC for tax the recipient must report on a return, that tax must have been reported, as required by 169(4)(b); retain the required evidence too. Simplified-regime charges follow Section 3.8. [169(4)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html).

### 5.8 Capital personal property / passenger vehicles

For a 2025 ordinary passenger-vehicle acquisition, the before-tax capital-cost amount is CAD 38,000 under Income Tax Regulations 7307(1)(b), descriptionA(ix); ETA 201 applies the relevant capital-cost restriction to the tax used in an ITC calculation. For a 2026 acquisition, check the operative limit with one of our partner accountants. [7307](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-7307.html); [201](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-201.html).

For an individual or partnership, section 202(2) bars an acquisition-tax ITC on a capital passenger vehicle/aircraft unless acquired for exclusive commercial use. If acquired for nonexclusive commercial use and tax was payable, section 202(4) instead deems tax paid on the last day of each taxation year using its applicable tax fraction times the CCA actually deducted from commercial-activity income; its B amount is nil in the stated taxable-benefit cases under ITA 6(1)(e) or15(1). Apply169(1)(a),201 and the actual facts; this is not purchase tax multiplied by a private/business-use percentage. Improvements have the separate 202(1)/(3) conditions. For leasing, a taxable-benefit case or a different entity, check this with one of our partner accountants rather than using the computer example’s result. [202](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html); [169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html).

The ordinary capital-personal-property rule in 199(2) gives no acquisition ITC unless acquired primarily for commercial activities, and deems a qualifying primary-commercial acquisition exclusively commercial. Sections 199/200 exclude financial institutions/prescribed registrants and an individual/partnership’s passenger vehicle or aircraft. [199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html); [200](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-200.html).

### 5.9 Blocked ITCs (ETA s.170)

- **Blocked ITCs** — Apply the actual s.170 restrictions, including memberships in clubs whose main purpose is dining, recreation or sport (except acquisition exclusively for supply in the ordinary course of a business supplying such memberships) and personal-consumption/benefit restrictions and their statutory exceptions. For promotional gifts, apply the commercial-use, documentation and actual restriction tests under sections 169 and 170. Food/entertainment and employee-benefit cases require their separate conditions. Passenger vehicles follow Section 5.8. For the employee/related-person benefit and fair-market-value resupply exceptions in 170(1)(b)/(c), check this with one of our partner accountants. Section 170(2) also requires reasonable quality/nature/cost and reasonable consideration or value in the circumstances. [170](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-170.html); [rc](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html); [202](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html).

### 5.10 Meals and entertainment

For an ordinary eligible business meal, the net ITC recovery is 50%. CRA permits either claiming 50% during each reporting period with no year-end adjustment, or claiming 100% during the year and making the ETA 236 adjustment. For a monthly/quarterly filer that adjustment belongs in the first reporting period of the following fiscal year; an annual filer adjusts in that fiscal year’s return. If registration ceases during the year,236(1.1)(a) makes that cessation period the appropriate period. CRA says include the adjustment in electronic line105 or paper line104. [236](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-236.html); [CRA methods](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit/calculate-methods.html).

Qualifying long-haul food/beverage amounts have a 20% rather than 50% adjustment under 236(1); for the ITA 67.1(1.1) driver/travel eligibility and other remote-work, fundraising or reimbursement exceptions, check this with one of our partner accountants. Charities/public institutions are outside this ordinary rule and this skill’s scope. Convention meals do not gain a blanket exception to the ordinary 50% limit. For allocation of a package fee or the treatment of incidental refreshments, check this with one of our partner accountants. [236](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-236.html); [CRA conventions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-expenses/convention-expenses.html).

### 5.11 Change in use — capital property

Identify the property and entity first. For ordinary capital personal property within199/200, beginning primary-commercial use triggers the 199(3) deemed acquisition and tax equal to basic tax content, except on becoming a registrant; ceasing primary-commercial use triggers200(2)’s deemed sale/reacquisition and basic-tax-content tax. A change is not universally taxed on fair market value. Passenger vehicles, aircraft excluded from these rules, real property and special registrants need their own provisions: check these with one of our partner accountants. [199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html); [200](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-200.html).

### 5.12 Small supplier and registration timing

For the ordinary business covered here, ETA 148 uses CAD 30,000 of the specified worldwide taxable consideration, including associates and excluding financial services, capital-property sales and business-sale goodwill. Exactly CAD 30,000 does not exceed the limit. A single-calendar-quarter excess ends small-supplier status immediately before the transaction that causes it. Under the four-quarter test,148(1) preserves status through the first month following the relevant quarter; do not apply single-quarter timing to a cumulative-only breach. Public-service bodies and the special gaming/nonresident-admission cases require separate provisions and are outside this ordinary test. [148](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html).

Under 240(2.1)(b), an ordinary person required to register applies before the day that is 30 days after their first taxable supply in Canada otherwise than as a small supplier. Small taxi-business suppliers have mandatory registration under 240(1.1) and their own first-supply trigger in 240(2.1)(a). Do not infer exemption from registration from revenue alone; for another special registration case, check this with one of our partner accountants. [240](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html).

### 5.13 Bad debts (ETA 231)

For a taxable, non-zero-rated, arm’s-length supply, the reporting entity may deduct relief after the supplier writes the established bad debt off in its books. The original collectible tax must have entered the reported net tax and all remittable net tax on that return must have been remitted. Relief = supply tax × written-off unpaid consideration/tax/applicable provincial tax ÷ total consideration/tax/applicable provincial tax. Claim it on 107 in a return filed within four years after the return due date for the write-off period. On recovery, add recovered amount × supply tax ÷ original total consideration/tax/applicable provincial tax to net tax in the recovery period (104). For an agent/reporting-entity election under 177(1.1), check this with one of our partner accountants. [231](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-231.html).

### 5.14 Reporting sales on Line 101

- **Line 101 reporting rule** — Under the regular method used here, report sales (including zero-rated and exempt supplies) and other revenue excluding GST/HST and provincial sales tax. Do not use the tax-inclusive Quick Method rule. Report collected/collectible GST/HST separately on 103. Keep the supporting allocations to cents, then round the final reported 101 amount to the nearest dollar as CRA instructs; report zero if there is no revenue. Do not apply this whole-dollar rule to every tax line. If optional electronic 90/91/102 fields are selected, use their definitions and the portal-calculated101 rather than duplicating revenue. [lines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html).

## Section 6 — Questions for missing records

Ask only the applicable unanswered questions. Use Sections 3–5 for treatment; missing evidence does not establish a statutory zero rate or permanent ITC block.

| Topic | Obtain before allocating tax |
| --- | --- |
| Vehicle | Is this fuel/operating cost, acquisition or improvement? What usage records support the relevant commercial-use test? |
| Meals | What is the business purpose, invoice tax and chosen claim/adjustment method? |
| Home office | Is this the principal business location, or exclusively business space used regularly and continuously for client/customer/patient meetings? What eligible share is supported? |
| Owner-labelled or round receipts | Is this a sale, contribution, loan or transfer? Match the underlying records. |
| Receipts from individuals | What was supplied and when did its tax become collectible? |
| Interprovincial supplies | What type of supply is it, and what delivery/address/service evidence establishes its province? |
| Potential capital purchase | What asset was bought, by which entity, and for what use? |
| Mixed-use phone/internet | What eligible commercial share do the records support? |
| Payments to individuals | Contractor, salary, refund, purchase or personal transfer? Obtain the supporting record. |
| Cash withdrawals | What eventual expense, if any, do the receipts support? |
| Rent | What does the lease supply, and what treatment has the partner confirmed? |
| Marketplace purchases | What do the individual invoice lines and supplier/tax details establish? |
| Processor settlements | Reconcile gross sales, fees, refunds and transfers to the underlying supplies. |
| Tips | Which amount was freely given, and which charge was mandatory? |
| Foreign currency | What accepted conversion source, date/rate and consistent method support the CAD amount? |

## Section 7 — Excel working paper template (Canada-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Canada-specific overlay.

### Sheet "Transactions"

Keep the base A–L columns: G = rate, H = linked return-allocation IDs, I = treatment label. Do not overwrite I with a rate or use G as a text treatment criterion. Add a linked **Return Allocations** table with stable transaction/allocation IDs, return line and a signed CAD return amount. One transaction may have separate eligible allocations to several lines; prevent duplicates. Source debits may be negative in Transactions, but positive eligible purchase tax must be normalized to a positive 106 credit; recovery/debit adjustments retain the correct return sign. An imported-service liability, when actually due, has its own 405 allocation; any eligible 106 credit is separate. [lines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html); [form](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf).

### Sheet "Line Summary"

- **Line Summary sheet formulas** — Sum the signed **Return Allocations** amounts by return line (for example, `=SUMIFS(ReturnAllocations[ReturnAmountCAD],ReturnAllocations[Line],"106")`). Use separate allocations for tax-exclusive 101 revenue, 103 output tax, eligible 106 ITCs and any 405 liability. Round the final 101 reporting total to the nearest dollar after summing its relevant allocations, while retaining the underlying cents. Compute 105 = 103 + 104; 108 = 106 + 107; 109 = 105 − 108; 112 = 110 + 111; 113A = 109 − 112; 113B = 205 + 405; 113C = 113A + 113B. Do not sum raw bank credits as 101 or negative bank-debit tax directly as 106. [lines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html); [form](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf).

### Sheet "Return Form"

- **Return Form final figures** — Carry final 113C (109 − 110 − 111 + 205 + 405) to the refund/payment decision: positive → amount owing on 115; negative → refund on 114. Do not stop at 113A when other debits exist. [form](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf).

### Mandatory recalc step

Recalculate every formula using the available workbook engine, reopen the result and inspect the return totals and formula errors before presenting it.

## Section 8 — Read the actual bank export

Inspect the supplied file’s headers, date convention, currency and debit/credit signs; confirm them against the statement and opening/closing balances. No bank-specific column order or date format is prescribed here. Preserve the original description and trace every working-paper allocation to its source record.

Reconcile transfers across both accounts and obtain the invoices behind deposits, withdrawals, fees and processor settlements. A bank posting is not proof of the tax point, GST/HST rate or commercial use.

For a documented amount that includes only the identified GST/HST rate, tax = gross × rate ÷ (1 + rate): CAD 113 at 13% contains CAD13. Split mixed-tax, exempt and zero-rated invoice lines before using this arithmetic. Use the accepted, consistently applied foreign-currency method and record the source, date and rate; the Bank of Canada is an accepted source, not the only permitted source. [CRA currency conversion](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/3-6/conversion-foreign-currency.html).

## Section 9 — Confirm the account and period

Collect the entity type, legal account holder, GST/HST account and registration regime, CRA-assigned reporting period and any accounting-method election. Do not infer registration from a request for a return or infer its period from the bank statement’s date range.

Record the actual business activities, supply locations, taxable/exempt activities, cross-provincial sales, payroll and prior-account balances. Obtain the missing facts before making their affected return allocations; this is an evidence requirement, not an unverified tax rule or a guessed conservative tax result.

## Sources

The table identifies the passages read and their dates. Transaction names, dates and amounts in the six examples are hypothetical inputs; the tax results are conditional on their stated eligibility facts.

| Rule / passage actually read | Official source | Short source words | Read on |
| --- | --- | --- | --- |
| Federal ordinary rate and zero rate:165(1)–(3) | [ETA 165](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-165.html) | “rate of 5%”; “is 0%” | 2026-11-26 |
| Definitions: commercial activity, financial-service exclusions, taxable/exempt/zero-rated supply and tax-rate hierarchy; only the identified definitions | [ETA 123](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html) | “but does not include”; “a supply included in Schedule V” | 2026-11-26 |
| Municipal transit: Part VI definitions of municipal transit service/transit authority and sections 24–24.1; financial-service exemption: Part VII sections 1–2 | [Schedule V](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-sched200860.html) | “other than a charter service or a service that is part of a tour”; “A supply of a financial service that is not included in Part IX of Schedule VI.” | 2026-11-26 |
| Province rate chart and NS effective date, corroborating the legislation above | [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) | “As of April 1, 2025, the HST rate has decreased to 14% in Nova Scotia.” | 2026-11-26 |
| Ontario fallback rate, Schedule VIII Ontario row | [Schedule VIII](https://laws-lois.justice.gc.ca/eng/acts/E-15/page-123.html#h-201840) | “Ontario”; “8%” | 2026-11-26 |
| Prescribed provincial parts:33.3–33.6, and NS override2(3) | [PEI](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/section-33.3.html), [NB](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/section-33.4.html), [NL](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/section-33.5.html), [NS](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/section-33.6.html), [NS priority](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-99/section-2.html) | “10%”; “9%”; “do not apply” | 2026-11-26 |
| General service address rule13(1)–(2) | [SOR/2010-117 section 13](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/section-13.html) | “most closely connected with the supply” | 2026-11-26 |
| Small supplier148 and registration240(1)–(3), within the saved bounded240 read | [148](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html), [240](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-240.html) | “$30,000”; “before the day that is 30 days after” | 2026-11-26 |
| Reporting periods and threshold: 245,247,248,249 | [245](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-245.html), [247](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-247.html), [248](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-248.html), [249](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-249.html) | “$6,000,000”; “does not exceed $1,500,000” | 2026-11-26 |
| Filing238; payment228(1)–(3), within the saved bounded228 read; deadline/holiday guidance | [238](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-238.html), [228](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-228.html), [CRA dates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) | “on or before April 30”; “next business day” | 2026-11-26 |
| Commercial-use deeming 141(1)–(5), complete operative provision read through the official page | [141](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-141.html) | “substantially all”; “other than a financial institution” | 2026-11-26 |
| ITC entitlement/evidence169 and restrictions170 | [169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html), [170](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-170.html) | “sufficient evidence”; “reasonable in the circumstances” | 2026-11-26 |
| Prescribed ITC information, complete regulation3 | [SOR/91-45 section 3](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html) | “less than $100”; “$500 or more” | 2026-11-26 |
| Simplified-regime credit restriction 211.17, including its listed exceptions | [211.17](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-211.17.html) | “No amount of an input tax credit” | 2026-11-26 |
| Imported-taxable-supply definition217(a)/(c),218 and218.1; bounded217 definition read, not unrelated definitions | [217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html), [218](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.html), [218.1](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.1.html) | “exclusively in the course of commercial activities” | 2026-11-26 |
| Provincial-service tax 220.08, Schedule X Part II and prescribed-supply rule14 | [220.08](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-220.08.html), [Schedule X](https://laws-lois.justice.gc.ca/eng/acts/E-15/page-125.html#h-201977), [regulation14](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-151/section-14.html) | “No tax is payable”; “included in another section of that Part” | 2026-11-26 |
| Capital property 199/200; vehicle 201/202 | [199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html), [200](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-200.html), [201](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-201.html), [202](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html) | “basic tax content”; “last day of each taxation year” | 2026-11-26 |
|2025 cost amount,7307(1) | [7307(1)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-7307.html) | “after 2024, $38,000” | 2026-11-26 |
| Meals236 and the two CRA calculation methods | [236](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-236.html), [CRA methods](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit/calculate-methods.html) | “20%”; “begins immediately after that fiscal year” | 2026-11-26 |
| Bad-debt entitlement, formula, recovery and time limit 231 | [231](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-231.html) | “filed within four years after” | 2026-11-26 |
| Consulting export, Schedule VI Part V section 23 and its complete four exclusions | [Part V23](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-sched201390.html) | “made to a non-resident person” | 2026-11-26 |
| Form: whole working copy, visually checked; instructions: regular101, component/total lines and nearest-dollar101 rule | [working copy](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf), [instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) | “Balance (add lines 113 A and 113 B)”; “Round off the amount to the nearest dollar.” | 2026-11-26 |
| Postage Ontario example only | [CRA place-of-supply](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) | “postage stamps at the Ontario rate” | 2026-11-26 |
| Freely given tips / mandatory service charge paragraph only | [CRA special cases](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-special-cases.html) | “freely given”; “mandatory amount” | 2026-11-26 |
| Convention meal limitation/incidental items: guidance paragraphs preceding the example and its incidental-items sentence; no deduction of a package fee computed here | [CRA conventions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/sole-proprietorships-partnerships/business-expenses/convention-expenses.html) | “The 50% limit applies”; “incidental items” | 2026-11-26 |
| Currency conversion, accepted sources/documentation/consistency paragraphs 13–15 | [CRA3.6](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/3-6/conversion-foreign-currency.html) | “supported with appropriate documentation” | 2026-11-26 |

The workbook column contract is a workflow specification, not legislation. Its existing Section 3 read is reused from 23November; the relevant source file is unchanged: [companion](https://github.com/openaccountants/openaccountants/blob/993539c4f/skills/global/methods/vat-workflow-base.md), “Rate applied” and “Treatment label”.
