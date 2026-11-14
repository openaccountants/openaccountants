---
name: global-cloud-infrastructure
description: "Use this cross-country method in 2026 to investigate cloud and infrastructure purchase classification. Treat bank strings as historical recognition hints, confirm the invoice and business purpose, separate personal use and timing, and apply the owning country tax method before posting. The output is a proposed accounting workpaper, not a verified merchant directory."
version: 1.0
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-14
category: bookkeeping
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: bookkeeping
type: cross-country-method
checked_on: 2026-11-14
---

# Cloud and infrastructure purchase classification v1.0

## Scope

Classify supported purchases and prepare the workpaper for the correct entity and period. The method is checked on 2026-11-14. Country tax rules remain country-specific. Preserve the old recognition coverage while replacing automatic tax/account mappings with evidence-based decisions. No accountant approval is asserted.

## Ask the client first

1. Which legal entity, country, reporting period, accounting framework and cash/accrual basis are being prepared?
2. Which invoice, contract and actual issuing legal entity support this charge, and is it a purchase, reimbursement, refund, transfer or finance item?
3. What service or asset was bought, what dates does it cover, and what evidence supports the business/private-use split?
4. What is the buyer's VAT/GST status and actual input-tax entitlement, and where do the parties and relevant establishments belong?
5. Which invoice, source transaction and account identifiers establish that the event was not already booked through a feed, bill or card import?
6. What are the invoice, settlement and functional currencies, dates and documented exchange-rate policy?

## The method, step by step

1. Preserve the source statement and invoice, original strings, currency, dates and reference. Use the recognition hints to find a candidate, then resolve the actual counterparty and transaction. A shared merchant string, an unknown credit or a round amount cannot establish a deductible cost.
2. Read the invoice and service period. Separate ordinary service, equipment/software rights or other capital cost, deposit, refund and own-account transfer. Match an existing supplier bill before creating an expense, so its payment clears the liability instead of duplicating the cost. Keep credits linked to the original invoice.
3. Confirm business purpose and private use. Allocate only on supported facts. For a UK sole trader/partner, HMRC's expense method separates personal use and distinguishes equipment/cash-basis treatment; it is not a universal rule for every company or country. Elsewhere use the owning country method. [UK expenses](https://www.gov.uk/expenses-if-youre-self-employed).
4. Apply the agreed timing policy. Under an accrual policy, allocate an annual service to periods received and carry the unused business portion as a prepayment where appropriate. A cash-basis taxpayer may have a different tax deduction. Keep the book/tax adjustment, not a blanket 'all annual payments accrue' instruction. [UK records, traditional accounting](https://www.gov.uk/self-employed-records/what-records-to-keep).
5. Resolve VAT/GST from the actual supply and parties, not the logo, payment currency or a remembered billing entity. For UK general-rule services from an overseas supplier, test Notice741A sections3-6, including the establishment connected with the supply, exemption and input-tax restriction. Its section5.7 can affect registration for an unregistered buyer. A fully creditable reverse charge may be neutral; an exempt or partly exempt buyer can bear a cost. Do not apply the UK rule to another country. [HMRC Notice741A](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a).
6. For an EU, Canadian, Australian or other-country buyer, load that country's VAT/GST method and official law before assigning its tax code. This global hint library supplies no universal EU reverse-charge exemption, US state sales-tax result, export zero rate or Australian imported-service self-assessment rule. Domestic versus cross-border status requires the actual supplying establishment. Keep unresolved tax separate in the working paper.
7. Apply the functional-currency policy, retaining both original and settled amounts. Under an applicable AASB121/IFRS-equivalent financial-reporting policy, distinguish recognition-date translation, closing-rate monetary balances and settlement differences; do not use payment date for every accrual. Do not impose that reporting policy on a cash-basis tax return. [AASB121 paragraphs21-23,28-29](https://standards.aasb.gov.au/sites/default/files/2025-03/AASB121_08-15_COMPoct23_01-25.pdf).
8. Produce proposed accounts, net/tax/gross, business/private allocation, expense/prepayment/capital split, book/tax adjustments and remaining questions, each linked to its evidence. If the ledger is read-only, deliver an import file or list of postings for a human to approve. A draft is not a posted journal. Reconcile the approved posting to the statement and retain the approval/import reference.

## When to refuse or refer

- Missing invoice, supplier, purpose, period, currency, duplicate status or business-use evidence: hold the final posting. Do not turn an unrecognised merchant into a confident expense.
- Capitalisation, mixed use, related-party charges, withholding, recoverability or a fixed establishment that changes the tax result: use the relevant country/subject method and refer unresolved interpretation.
- A payment processor or own-account transfer: use `global-payment-processors`; a purchase of hardware is not a SaaS fee. No blanket ScheduleC line, UK box or 'EU bookkeeping' account is certified for every product and basis.
- Current vendor billing entities, ownership, country coverage, plans and exact statement descriptors were not verified under this wave's official-authority-only source policy. The historical hints are not certified live integrations or tax determinations.

### Cloud-specific checks

Separate consumption-based hosting, reserved-capacity commitments, support, developer licences, communications/email services, storage and consultancy. The invoice can consolidate projects or entities; establish the actual purchaser and service period. Keep usage and contract evidence for recurring estimates. The old 'most non-EU customers receive zero-rated exports' and automatic ScheduleC utilities mapping were not valid universal rules. VIES identity evidence, where relevant, does not by itself establish all VAT conditions.

## Recognition hints

These are historical search hints from the existing library, not a verified 2026 merchant directory. Match them to the client's actual invoice and account first. A substring match is neither supplier identification nor permission to post. Suggested accounts remain proposals until the business purpose and accounting policy are known.

### Vendor candidates
- **Amazon Web Services**. Possible statement text `AWS EMEA SARL`, `AMAZON WEB SERVICES`, `AWS BILLING`, `AWS EMEA SARL LUX`, `AMAZON DATA SERVICES IRELAND`. Proposed classification Cloud hosting / IT services.
- **Microsoft Azure**. Possible statement text `MICROSOFT IRELAND OPS`, `MICROSOFT*AZURE`, `MSFT*AZURE`, `MICROSOFT AZURE`. Proposed classification Cloud hosting / IT services.
- **Google Cloud Platform**. Possible statement text `GOOGLE *CLOUD`, `GOOGLE CLOUD`, `GOOGLE PAYMENT`, `GOOGLE CLOUD EMEA`, `GOOGLE IRELAND LTD`. Proposed classification Cloud hosting / IT services.
- **Cloudflare**. Possible statement text `CLOUDFLARE INC`, `CLOUDFLARE.COM`, `CLOUDFLARE *`, `Cloudflare London`. Proposed classification CDN / network services.
- **DigitalOcean**. Possible statement text `DIGITALOCEAN.COM`, `DIGITALOCEAN INC`, `DO *DIGITALOCEAN`. Proposed classification Cloud hosting.
- **Linode (Akamai)**. Possible statement text `LINODE`, `AKAMAI TECH`, `LINODE LLC`. Proposed classification Cloud hosting.
- **Hetzner**. Possible statement text `HETZNER ONLINE GMBH`, `HETZNER.COM`. Proposed classification Cloud hosting.
- **OVHcloud**. Possible statement text `OVH*`, `OVHCLOUD`, `OVH SAS`. Proposed classification Cloud hosting.
- **Vultr**. Possible statement text `VULTR HOLDINGS`, `VULTR.COM`. Proposed classification Cloud hosting.
- **Render**. Possible statement text `RENDER SERVICES`, `RENDER.COM`, `RENDER`. Proposed classification Cloud hosting / PaaS.
- **Vercel**. Possible statement text `VERCEL INC`, `VERCEL.COM`, `VERCEL`. Proposed classification Cloud hosting / PaaS.
- **Netlify**. Possible statement text `NETLIFY INC`, `NETLIFY.COM`. Proposed classification Cloud hosting / PaaS.
- **Fly.io**. Possible statement text `FLY.IO`, `FLY INC`. Proposed classification Cloud hosting / edge.
- **Railway**. Possible statement text `RAILWAY.APP`, `RAILWAY INC`. Proposed classification Cloud hosting / PaaS.
- **Heroku**. Possible statement text `HEROKU`, `SALESFORCE HEROKU`. Proposed classification Cloud hosting / PaaS.
- **Backblaze**. Possible statement text `BACKBLAZE INC`, `BACKBLAZE B2`. Proposed classification Cloud storage / backup.
- **Wasabi**. Possible statement text `WASABI TECHNOLOGIES`, `WASABI.COM`. Proposed classification Cloud storage.
- **Datadog**. Possible statement text `DATADOG INC`, `DATADOG.COM`. Proposed classification Observability / monitoring.
- **New Relic**. Possible statement text `NEW RELIC INC`, `NEWRELIC.COM`. Proposed classification Observability / monitoring.
- **PagerDuty**. Possible statement text `PAGERDUTY INC`, `PAGERDUTY.COM`. Proposed classification Incident management.
- **GitHub**. Possible statement text `GITHUB INC`, `GITHUB.COM`, `MICROSOFT*GITHUB`. Proposed classification Source control / CI / CD.
- **GitLab**. Possible statement text `GITLAB INC`, `GITLAB.COM`. Proposed classification Source control / CI / CD.
- **Sentry**. Possible statement text `SENTRY.IO`, `FUNCTIONAL SOFTWARE`. Proposed classification Error tracking.
- **LaunchDarkly**. Possible statement text `LAUNCHDARKLY INC`. Proposed classification Feature flags.
- **Twilio**. Possible statement text `TWILIO INC`, `TWILIO.COM`, `TWILIO IRELAND`. Proposed classification Communications API.
- **SendGrid**. Possible statement text `SENDGRID`, `TWILIO SENDGRID`. Proposed classification Email API.
- **Mailgun**. Possible statement text `MAILGUN INC`, `MAILGUN TECHNOLOGIES`. Proposed classification Email API.
- **Resend**. Possible statement text `RESEND INC`. Proposed classification Email API.
- **Postmark**. Possible statement text `POSTMARK`, `WILDBIT LLC`. Proposed classification Email API.
- **MongoDB Atlas**. Possible statement text `MONGODB INC`, `MONGODB ATLAS`. Proposed classification Cloud database.
- **Snowflake**. Possible statement text `SNOWFLAKE INC`, `SNOWFLAKE COMPUTING`. Proposed classification Cloud data warehouse.
- **Databricks**. Possible statement text `DATABRICKS INC`. Proposed classification Cloud data platform.
- **Pulumi**. Possible statement text `PULUMI CORP`. Proposed classification IaC.
- **HashiCorp / Terraform Cloud**. Possible statement text `HASHICORP INC`. Proposed classification IaC.

## Worked cases

### Annual cloud service with private use

Assume a client's approved accrual policy, a genuine 12-month USD1,200 service, supported 75% business use and four months received by year end. There is no confirmed input tax in these supplied facts. The business portion is USD900, current expense USD300, prepayment USD600 and personal portion USD300. Do not post the whole card charge as utilities or claim a tax deduction without the country method.

```oa-check
name: Cloud contract, period and business-use split
inputs:
  invoice: 1200
  business_share: 0.75
  elapsed_months: 4
steps:
  - business_cost: invoice * business_share
  - current_expense: business_cost * elapsed_months / 12
  - prepayment: business_cost - current_expense
  - personal: invoice - business_cost
  - control_total: current_expense + prepayment + personal
expected:
  business_cost: 900
  current_expense: 300
  prepayment: 600
  personal: 300
  control_total: 1200
```



## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.gov.uk/self-employed-records/what-records-to-keep | 2026-11-14 | Read for sales/expense proof, accurate records, distinguishing business transactions and accrual records. |
| https://www.gov.uk/expenses-if-youre-self-employed | 2026-11-14 | Read for sole-trader/partner business-purpose allocation, ordinary expenses versus equipment and cash/traditional basis. |
| https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-11-14 | Read for sections2-6 and13, actual supply, belonging, reverse-charge conditions, input-tax limits and unregistered recipients. |
| https://standards.aasb.gov.au/sites/default/files/2025-03/AASB121_08-15_COMPoct23_01-25.pdf | 2026-11-14 | Read for paragraphs20-23 and27-30, initial recognition, monetary closing balances and settlement exchange differences; Australian IFRS-equivalent financial reporting, not universal tax translation. |

Not yet confirmed: the current legal billing entity, country, ownership, descriptor availability and VAT/GST assertion formerly attached to each historical candidate below. These old assertions are recorded for comparison only and must not be used to compute or post tax. Official EU legislation could not be reopened during the current EUR-Lex outage; use the selected country's actual official source. No vendor source was used.

- Historical, not usable guidance, **Amazon Web Services**: VAT/GST notes: EU B2B: reverse charge (supplier in IE/LU). US: no VAT. UK B2B: reverse charge. Most non-EU: zero-rated export from supplier.; Notes: Monthly USD billing; consolidated invoice. Some accounts use AWS EMEA SARL (Luxembourg) for EU customers; AWS Inc for US.
- Historical, not usable guidance, **Microsoft Azure**: VAT/GST notes: EU B2B: reverse charge (supplier in IE , Microsoft Ireland Operations Ltd).; Notes: Monthly USD/EUR billing.
- Historical, not usable guidance, **Google Cloud Platform**: VAT/GST notes: EU B2B: reverse charge.; Notes: Monthly USD/EUR.
- Historical, not usable guidance, **Cloudflare**: VAT/GST notes: EU B2B: reverse charge (Cloudflare London Ltd for UK; Cloudflare Inc for US).; Notes: Monthly USD or annual.
- Historical, not usable guidance, **DigitalOcean**: VAT/GST notes: EU B2B: reverse charge (Netherlands BV).; Notes: Monthly USD.
- Historical, not usable guidance, **Linode (Akamai)**: VAT/GST notes: US supplier; EU B2B reverse charge.; Notes: Monthly USD.
- Historical, not usable guidance, **Hetzner**: VAT/GST notes: Germany supplier; EU B2B reverse charge for EU customers; UK customers may face local VAT depending on supply rules.; Notes: Monthly EUR.
- Historical, not usable guidance, **OVHcloud**: VAT/GST notes: France supplier; EU B2B reverse charge.; Notes: Monthly EUR.
- Historical, not usable guidance, **Vultr**: VAT/GST notes: US supplier (Vultr Holdings LLC).; Notes: Monthly USD.
- Historical, not usable guidance, **Render**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **Vercel**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **Netlify**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **Fly.io**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **Railway**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **Heroku**: VAT/GST notes: Now Salesforce subsidiary; same classification.; Notes: Monthly USD.
- Historical, not usable guidance, **Backblaze**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **Wasabi**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **Datadog**: VAT/GST notes: US supplier; EU B2B reverse charge.; Notes: Monthly USD (often annual contract).
- Historical, not usable guidance, **New Relic**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **PagerDuty**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **GitHub**: VAT/GST notes: GitHub Inc (Microsoft subsidiary). EU B2B reverse charge.; Notes: Monthly USD.
- Historical, not usable guidance, **GitLab**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **Sentry**: VAT/GST notes: US supplier (Functional Software Inc dba Sentry).; Notes: Monthly USD.
- Historical, not usable guidance, **LaunchDarkly**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **Twilio**: VAT/GST notes: Twilio Inc for US; Twilio Ireland for EU. EU B2B reverse charge.; Notes: Monthly USD/EUR usage-based.
- Historical, not usable guidance, **SendGrid**: VAT/GST notes: Twilio subsidiary; classify with Twilio.; Notes: Monthly USD.
- Historical, not usable guidance, **Mailgun**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **Resend**: VAT/GST notes: US supplier (newer).; Notes: Monthly USD.
- Historical, not usable guidance, **Postmark**: VAT/GST notes: US supplier (Wildbit LLC).; Notes: Monthly USD.
- Historical, not usable guidance, **MongoDB Atlas**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **Snowflake**: VAT/GST notes: US supplier.; Notes: Annual contract; consumption pricing.
- Historical, not usable guidance, **Databricks**: VAT/GST notes: US supplier.; Notes: Annual contract.
- Historical, not usable guidance, **Pulumi**: VAT/GST notes: US supplier.; Notes: Monthly USD.
- Historical, not usable guidance, **HashiCorp / Terraform Cloud**: VAT/GST notes: US supplier; acquired by IBM 2024.; Notes: Monthly/annual USD.
