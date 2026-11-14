---
name: global-saas-vendors
description: "Use this cross-country method in 2026 to investigate saas purchase investigation and classification. Treat bank strings as historical recognition hints, confirm the invoice and business purpose, separate personal use and timing, and apply the owning country tax method before posting. The output is a proposed accounting workpaper, not a verified merchant directory."
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

# SaaS purchase investigation and classification v1.0

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

### SaaS-specific checks

Preserve separate cloud/hosting, development, design, communications, project management, marketing, accounting/finance, AI/ML, legal/compliance, security, storage, media, education and automation candidates below. Training, professional memberships and subscriptions need their local eligibility test; payment-platform subscriptions differ from transactions. Never infer business music use or licensing from a consumer subscription. Keep annual-versus-monthly and changed billing-entity checks, and route cloud, advertising, productivity and payment processor work to their companion skills instead of double-classifying it.

## Recognition hints

These are historical search hints from the existing library, not a verified 2026 merchant directory. Match them to the client's actual invoice and account first. A substring match is neither supplier identification nor permission to post. Suggested accounts remain proposals until the business purpose and accounting policy are known.

### Cloud and hosting
- **AWS**. Possible statement text `AMAZON WEB SERVICES`. Proposed classification IT expenses / Cloud infrastructure.
- **AWS**. Possible statement text `AWS EMEA SARL`. Proposed classification IT expenses / Cloud infrastructure.
- **AWS**. Possible statement text `AWS *SERVICES`. Proposed classification IT expenses / Cloud infrastructure.
- **AWS**. Possible statement text `AMAZON WEB SERVI`. Proposed classification IT expenses / Cloud infrastructure.
- **Google Cloud Platform**. Possible statement text `GOOGLE CLOUD`. Proposed classification IT expenses / Cloud infrastructure.
- **Google Cloud Platform**. Possible statement text `GOOGLE *CLOUD`. Proposed classification IT expenses / Cloud infrastructure.
- **Google Cloud Platform**. Possible statement text `GOOGLE *GCP`. Proposed classification IT expenses / Cloud infrastructure.
- **Microsoft Azure**. Possible statement text `MICROSOFT *AZURE`. Proposed classification IT expenses / Cloud infrastructure.
- **Microsoft Azure**. Possible statement text `MICROSOFT AZURE`. Proposed classification IT expenses / Cloud infrastructure.
- **Microsoft Azure**. Possible statement text `MSFT *AZURE`. Proposed classification IT expenses / Cloud infrastructure.
- **DigitalOcean**. Possible statement text `DIGITALOCEAN`. Proposed classification IT expenses / Cloud infrastructure.
- **DigitalOcean**. Possible statement text `DIGITALOCEAN.COM`. Proposed classification IT expenses / Cloud infrastructure.
- **Heroku (Salesforce)**. Possible statement text `HEROKU`. Proposed classification IT expenses / Cloud infrastructure.
- **Heroku (Salesforce)**. Possible statement text `HEROKU *`. Proposed classification IT expenses / Cloud infrastructure.
- **Vercel**. Possible statement text `VERCEL INC`. Proposed classification IT expenses / Cloud infrastructure.
- **Vercel**. Possible statement text `VERCEL`. Proposed classification IT expenses / Cloud infrastructure.
- **Netlify**. Possible statement text `NETLIFY`. Proposed classification IT expenses / Cloud infrastructure.
- **Cloudflare**. Possible statement text `CLOUDFLARE`. Proposed classification IT expenses / Cloud infrastructure.
- **Cloudflare**. Possible statement text `CLOUDFLARE.COM`. Proposed classification IT expenses / Cloud infrastructure.
- **Linode (Akamai)**. Possible statement text `LINODE`. Proposed classification IT expenses / Cloud infrastructure.
- **Linode (Akamai)**. Possible statement text `AKAMAI *LINODE`. Proposed classification IT expenses / Cloud infrastructure.
- **Hetzner**. Possible statement text `HETZNER`. Proposed classification IT expenses / Cloud infrastructure.
- **Hetzner**. Possible statement text `HETZNER ONLINE`. Proposed classification IT expenses / Cloud infrastructure.
- **OVHcloud**. Possible statement text `OVH`. Proposed classification IT expenses / Cloud infrastructure.
- **OVHcloud**. Possible statement text `OVHCLOUD`. Proposed classification IT expenses / Cloud infrastructure.
- **Vultr**. Possible statement text `VULTR`. Proposed classification IT expenses / Cloud infrastructure.
- **Render**. Possible statement text `RENDER.COM`. Proposed classification IT expenses / Cloud infrastructure.
- **Fly.io**. Possible statement text `FLY.IO`. Proposed classification IT expenses / Cloud infrastructure.
- **Railway**. Possible statement text `RAILWAY.APP`. Proposed classification IT expenses / Cloud infrastructure.

### Developer tools
- **GitHub**. Possible statement text `GITHUB`. Proposed classification IT expenses / Software subscriptions.
- **GitHub**. Possible statement text `GITHUB INC`. Proposed classification IT expenses / Software subscriptions.
- **GitLab**. Possible statement text `GITLAB`. Proposed classification IT expenses / Software subscriptions.
- **GitLab**. Possible statement text `GITLAB INC`. Proposed classification IT expenses / Software subscriptions.
- **GitLab**. Possible statement text `GITLAB B.V.`. Proposed classification IT expenses / Software subscriptions.
- **Bitbucket / Jira / Confluence**. Possible statement text `ATLASSIAN`. Proposed classification IT expenses / Software subscriptions.
- **Bitbucket / Jira / Confluence**. Possible statement text `ATLASSIAN *`. Proposed classification IT expenses / Software subscriptions.
- **JetBrains**. Possible statement text `JETBRAINS`. Proposed classification IT expenses / Software subscriptions.
- **JetBrains**. Possible statement text `JETBRAINS S.R.O`. Proposed classification IT expenses / Software subscriptions.
- **Docker**. Possible statement text `DOCKER`. Proposed classification IT expenses / Software subscriptions.
- **Docker**. Possible statement text `DOCKER INC`. Proposed classification IT expenses / Software subscriptions.
- **HashiCorp (Terraform Cloud)**. Possible statement text `HASHICORP`. Proposed classification IT expenses / Software subscriptions.
- **Datadog**. Possible statement text `DATADOG`. Proposed classification IT expenses / Software subscriptions.
- **Datadog**. Possible statement text `DATADOG INC`. Proposed classification IT expenses / Software subscriptions.
- **Sentry**. Possible statement text `SENTRY`. Proposed classification IT expenses / Software subscriptions.
- **Sentry**. Possible statement text `SENTRY.IO`. Proposed classification IT expenses / Software subscriptions.
- **Sentry**. Possible statement text `GETSENTRY`. Proposed classification IT expenses / Software subscriptions.
- **New Relic**. Possible statement text `NEW RELIC`. Proposed classification IT expenses / Software subscriptions.
- **PagerDuty**. Possible statement text `PAGERDUTY`. Proposed classification IT expenses / Software subscriptions.
- **Postman**. Possible statement text `POSTMAN`. Proposed classification IT expenses / Software subscriptions.
- **npm (GitHub)**. Possible statement text `NPMJS.COM`. Proposed classification IT expenses / Software subscriptions.
- **CircleCI**. Possible statement text `CIRCLECI`. Proposed classification IT expenses / Software subscriptions.
- **Travis CI**. Possible statement text `TRAVIS-CI`. Proposed classification IT expenses / Software subscriptions.

### Design tools
- **Figma**. Possible statement text `FIGMA`. Proposed classification IT expenses / Software subscriptions.
- **Figma**. Possible statement text `FIGMA INC`. Proposed classification IT expenses / Software subscriptions.
- **Adobe Creative Cloud**. Possible statement text `ADOBE`. Proposed classification IT expenses / Software subscriptions.
- **Adobe Creative Cloud**. Possible statement text `ADOBE CREATIVE`. Proposed classification IT expenses / Software subscriptions.
- **Adobe Creative Cloud**. Possible statement text `ADOBE *CREATIVE`. Proposed classification IT expenses / Software subscriptions.
- **Adobe Creative Cloud**. Possible statement text `ADOBE SYSTEMS`. Proposed classification IT expenses / Software subscriptions.
- **Canva**. Possible statement text `CANVA`. Proposed classification IT expenses / Software subscriptions.
- **Canva**. Possible statement text `CANVA.COM`. Proposed classification IT expenses / Software subscriptions.
- **Canva**. Possible statement text `CANVA PTY`. Proposed classification IT expenses / Software subscriptions.
- **Sketch**. Possible statement text `SKETCH B.V.`. Proposed classification IT expenses / Software subscriptions.
- **Sketch**. Possible statement text `SKETCH`. Proposed classification IT expenses / Software subscriptions.
- **InVision**. Possible statement text `INVISIONAPP`. Proposed classification IT expenses / Software subscriptions.
- **Miro**. Possible statement text `MIRO`. Proposed classification IT expenses / Software subscriptions.
- **Miro**. Possible statement text `MIRO.COM`. Proposed classification IT expenses / Software subscriptions.
- **Miro**. Possible statement text `REALTIMEBOARD`. Proposed classification IT expenses / Software subscriptions.

### Communication
- **Slack (Salesforce)**. Possible statement text `SLACK`. Proposed classification IT expenses / Software subscriptions.
- **Slack (Salesforce)**. Possible statement text `SLACK TECHNOLOG`. Proposed classification IT expenses / Software subscriptions.
- **Zoom**. Possible statement text `ZOOM.US`. Proposed classification IT expenses / Software subscriptions.
- **Zoom**. Possible statement text `ZOOM VIDEO`. Proposed classification IT expenses / Software subscriptions.
- **Zoom**. Possible statement text `ZOOM *`. Proposed classification IT expenses / Software subscriptions.
- **Microsoft 365**. Possible statement text `MICROSOFT *365`. Proposed classification IT expenses / Software subscriptions.
- **Microsoft 365**. Possible statement text `MICROSOFT *OFFIC`. Proposed classification IT expenses / Software subscriptions.
- **Microsoft 365**. Possible statement text `MSFT *M365`. Proposed classification IT expenses / Software subscriptions.
- **Microsoft 365**. Possible statement text `MICROSOFT *MICRO`. Proposed classification IT expenses / Software subscriptions.
- **Google Workspace**. Possible statement text `GOOGLE *GSUITE`. Proposed classification IT expenses / Software subscriptions.
- **Google Workspace**. Possible statement text `GOOGLE *WORKSPAC`. Proposed classification IT expenses / Software subscriptions.
- **Google Workspace**. Possible statement text `GOOGLE WORKSPACE`. Proposed classification IT expenses / Software subscriptions.
- **Discord Nitro**. Possible statement text `DISCORD`. Proposed classification IT expenses / Software subscriptions.
- **Discord Nitro**. Possible statement text `DISCORD NITRO`. Proposed classification IT expenses / Software subscriptions.
- **Loom**. Possible statement text `LOOM`. Proposed classification IT expenses / Software subscriptions.
- **Loom**. Possible statement text `LOOM INC`. Proposed classification IT expenses / Software subscriptions.
- **Calendly**. Possible statement text `CALENDLY`. Proposed classification IT expenses / Software subscriptions.
- **Twilio**. Possible statement text `TWILIO`. Proposed classification IT expenses / Software subscriptions.
- **Twilio**. Possible statement text `TWILIO INC`. Proposed classification IT expenses / Software subscriptions.

### Project management
- **Jira / Confluence**. Possible statement text `ATLASSIAN`. Proposed classification IT expenses / Software subscriptions.
- **Asana**. Possible statement text `ASANA`. Proposed classification IT expenses / Software subscriptions.
- **Asana**. Possible statement text `ASANA INC`. Proposed classification IT expenses / Software subscriptions.
- **Monday.com**. Possible statement text `MONDAY.COM`. Proposed classification IT expenses / Software subscriptions.
- **Monday.com**. Possible statement text `MONDAY COM`. Proposed classification IT expenses / Software subscriptions.
- **Notion**. Possible statement text `NOTION`. Proposed classification IT expenses / Software subscriptions.
- **Notion**. Possible statement text `NOTION LABS`. Proposed classification IT expenses / Software subscriptions.
- **ClickUp**. Possible statement text `CLICKUP`. Proposed classification IT expenses / Software subscriptions.
- **ClickUp**. Possible statement text `CLICKUP.COM`. Proposed classification IT expenses / Software subscriptions.
- **Linear**. Possible statement text `LINEAR`. Proposed classification IT expenses / Software subscriptions.
- **Linear**. Possible statement text `LINEAR APP`. Proposed classification IT expenses / Software subscriptions.
- **Basecamp**. Possible statement text `BASECAMP`. Proposed classification IT expenses / Software subscriptions.
- **Basecamp**. Possible statement text `37SIGNALS`. Proposed classification IT expenses / Software subscriptions.
- **Trello (Atlassian)**. Possible statement text `TRELLO`. Proposed classification IT expenses / Software subscriptions.
- **Trello (Atlassian)**. Possible statement text `TRELLO.COM`. Proposed classification IT expenses / Software subscriptions.

### Marketing
- **Mailchimp (Intuit)**. Possible statement text `MAILCHIMP`. Proposed classification Marketing / Advertising.
- **Mailchimp (Intuit)**. Possible statement text `MAILCHIMP *`. Proposed classification Marketing / Advertising.
- **ConvertKit (Kit)**. Possible statement text `CONVERTKIT`. Proposed classification Marketing / Advertising.
- **ConvertKit (Kit)**. Possible statement text `KIT.COM`. Proposed classification Marketing / Advertising.
- **HubSpot**. Possible statement text `HUBSPOT`. Proposed classification Marketing / Advertising.
- **HubSpot**. Possible statement text `HUBSPOT INC`. Proposed classification Marketing / Advertising.
- **Ahrefs**. Possible statement text `AHREFS`. Proposed classification Marketing / Advertising.
- **Ahrefs**. Possible statement text `AHREFS PTE`. Proposed classification Marketing / Advertising.
- **SEMrush**. Possible statement text `SEMRUSH`. Proposed classification Marketing / Advertising.
- **SEMrush**. Possible statement text `SEMRUSH INC`. Proposed classification Marketing / Advertising.
- **Buffer**. Possible statement text `BUFFER`. Proposed classification Marketing / Advertising.
- **Buffer**. Possible statement text `BUFFER INC`. Proposed classification Marketing / Advertising.
- **Hootsuite**. Possible statement text `HOOTSUITE`. Proposed classification Marketing / Advertising.
- **Hootsuite**. Possible statement text `HOOTSUITE INC`. Proposed classification Marketing / Advertising.
- **ActiveCampaign**. Possible statement text `ACTIVECAMPAIGN`. Proposed classification Marketing / Advertising.
- **Brevo (Sendinblue)**. Possible statement text `SENDINBLUE`. Proposed classification Marketing / Advertising.
- **Brevo (Sendinblue)**. Possible statement text `BREVO`. Proposed classification Marketing / Advertising.

### Accounting and finance
- **Xero**. Possible statement text `XERO`. Proposed classification Office expenses / Accounting software.
- **Xero**. Possible statement text `XERO LTD`. Proposed classification Office expenses / Accounting software.
- **Xero**. Possible statement text `XERO UK LTD`. Proposed classification Office expenses / Accounting software.
- **QuickBooks (Intuit)**. Possible statement text `INTUIT *QUICKBOOK`. Proposed classification Office expenses / Accounting software.
- **QuickBooks (Intuit)**. Possible statement text `QUICKBOOKS`. Proposed classification Office expenses / Accounting software.
- **QuickBooks (Intuit)**. Possible statement text `INTUIT *QB`. Proposed classification Office expenses / Accounting software.
- **FreshBooks**. Possible statement text `FRESHBOOKS`. Proposed classification Office expenses / Accounting software.
- **Wave**. Possible statement text `WAVE FINANCIAL`. Proposed classification Office expenses / Accounting software.
- **Wave**. Possible statement text `WAVE APPS`. Proposed classification Office expenses / Accounting software.
- **Stripe**. Possible statement text `STRIPE`. Proposed classification Bank charges / Payment processing fees.
- **Stripe**. Possible statement text `STRIPE PAYMENTS`. Proposed classification Bank charges / Payment processing fees.
- **PayPal**. Possible statement text `PAYPAL`. Proposed classification Bank charges / Payment processing fees.
- **PayPal**. Possible statement text `PAYPAL *`. Proposed classification Bank charges / Payment processing fees.
- **Wise**. Possible statement text `WISE`. Proposed classification Bank charges / Transfer fees.
- **Wise**. Possible statement text `TRANSFERWISE`. Proposed classification Bank charges / Transfer fees.
- **Revolut**. Possible statement text `REVOLUT`. Proposed classification Bank charges.
- **Revolut**. Possible statement text `REVOLUT *`. Proposed classification Bank charges.

### AI and ML
- **OpenAI**. Possible statement text `OPENAI`. Proposed classification IT expenses / Software subscriptions.
- **OpenAI**. Possible statement text `OPENAI *CHATGPT`. Proposed classification IT expenses / Software subscriptions.
- **OpenAI**. Possible statement text `OPENAI *`. Proposed classification IT expenses / Software subscriptions.
- **Anthropic**. Possible statement text `ANTHROPIC`. Proposed classification IT expenses / Software subscriptions.
- **Anthropic**. Possible statement text `ANTHROPIC *`. Proposed classification IT expenses / Software subscriptions.
- **Midjourney**. Possible statement text `MIDJOURNEY`. Proposed classification IT expenses / Software subscriptions.
- **Midjourney**. Possible statement text `MIDJOURNEY INC`. Proposed classification IT expenses / Software subscriptions.
- **Stability AI**. Possible statement text `STABILITY AI`. Proposed classification IT expenses / Software subscriptions.
- **Stability AI**. Possible statement text `STABILITY.AI`. Proposed classification IT expenses / Software subscriptions.
- **Hugging Face**. Possible statement text `HUGGING FACE`. Proposed classification IT expenses / Software subscriptions.
- **Hugging Face**. Possible statement text `HUGGINGFACE`. Proposed classification IT expenses / Software subscriptions.
- **Replicate**. Possible statement text `REPLICATE`. Proposed classification IT expenses / Software subscriptions.
- **Replicate**. Possible statement text `REPLICATE INC`. Proposed classification IT expenses / Software subscriptions.
- **Perplexity AI**. Possible statement text `PERPLEXITY`. Proposed classification IT expenses / Software subscriptions.
- **Cursor (Anysphere)**. Possible statement text `CURSOR`. Proposed classification IT expenses / Software subscriptions.
- **Cursor (Anysphere)**. Possible statement text `ANYSPHERE`. Proposed classification IT expenses / Software subscriptions.

### Legal and compliance
- **DocuSign**. Possible statement text `DOCUSIGN`. Proposed classification Office expenses / Legal services.
- **DocuSign**. Possible statement text `DOCUSIGN INC`. Proposed classification Office expenses / Legal services.
- **HelloSign (Dropbox)**. Possible statement text `HELLOSIGN`. Proposed classification Office expenses / Legal services.
- **Dropbox Sign**. Possible statement text `DROPBOX SIGN`. Proposed classification Office expenses / Legal services.
- **PandaDoc**. Possible statement text `PANDADOC`. Proposed classification Office expenses / Legal services.
- **PandaDoc**. Possible statement text `PANDADOC INC`. Proposed classification Office expenses / Legal services.
- **Termly**. Possible statement text `TERMLY`. Proposed classification Office expenses / Legal services.
- **Termly**. Possible statement text `TERMLY.IO`. Proposed classification Office expenses / Legal services.

### Other SaaS
- **1Password**. Possible statement text `1PASSWORD`. Proposed classification IT expenses / Software subscriptions.
- **1Password**. Possible statement text `AGILEBITS`. Proposed classification IT expenses / Software subscriptions.
- **LastPass**. Possible statement text `LASTPASS`. Proposed classification IT expenses / Software subscriptions.
- **LastPass**. Possible statement text `LASTPASS.COM`. Proposed classification IT expenses / Software subscriptions.
- **Bitwarden**. Possible statement text `BITWARDEN`. Proposed classification IT expenses / Software subscriptions.
- **Bitwarden**. Possible statement text `BITWARDEN INC`. Proposed classification IT expenses / Software subscriptions.
- **Dropbox**. Possible statement text `DROPBOX`. Proposed classification IT expenses / Software subscriptions.
- **Dropbox**. Possible statement text `DROPBOX *`. Proposed classification IT expenses / Software subscriptions.
- **Apple (iCloud+)**. Possible statement text `APPLE.COM/BILL`. Proposed classification IT expenses / Software subscriptions.
- **Apple (iCloud+)**. Possible statement text `APPLE.COM *`. Proposed classification IT expenses / Software subscriptions.
- **Spotify**. Possible statement text `SPOTIFY`. Proposed classification NOT deductible unless business use proven.
- **Spotify**. Possible statement text `SPOTIFY AB`. Proposed classification NOT deductible unless business use proven.
- **LinkedIn Premium**. Possible statement text `LINKEDIN`. Proposed classification Marketing / Professional development.
- **LinkedIn Premium**. Possible statement text `LINKEDIN *`. Proposed classification Marketing / Professional development.
- **Grammarly**. Possible statement text `GRAMMARLY`. Proposed classification IT expenses / Software subscriptions.
- **Grammarly**. Possible statement text `GRAMMARLY INC`. Proposed classification IT expenses / Software subscriptions.
- **Zapier**. Possible statement text `ZAPIER`. Proposed classification IT expenses / Software subscriptions.
- **Zapier**. Possible statement text `ZAPIER INC`. Proposed classification IT expenses / Software subscriptions.
- **Make (Integromat)**. Possible statement text `MAKE.COM`. Proposed classification IT expenses / Software subscriptions.
- **Make (Integromat)**. Possible statement text `INTEGROMAT`. Proposed classification IT expenses / Software subscriptions.
- **Typeform**. Possible statement text `TYPEFORM`. Proposed classification IT expenses / Software subscriptions.
- **Typeform**. Possible statement text `TYPEFORM S.L.`. Proposed classification IT expenses / Software subscriptions.
- **Intercom**. Possible statement text `INTERCOM`. Proposed classification IT expenses / Software subscriptions.
- **Intercom**. Possible statement text `INTERCOM INC`. Proposed classification IT expenses / Software subscriptions.
- **Zendesk**. Possible statement text `ZENDESK`. Proposed classification IT expenses / Software subscriptions.
- **Zendesk**. Possible statement text `ZENDESK INC`. Proposed classification IT expenses / Software subscriptions.
- **SendGrid (Twilio)**. Possible statement text `TWILIO SENDGRID`. Proposed classification IT expenses / Software subscriptions.
- **SendGrid (Twilio)**. Possible statement text `SENDGRID`. Proposed classification IT expenses / Software subscriptions.
- **Namecheap**. Possible statement text `NAMECHEAP`. Proposed classification IT expenses / Domain registration.
- **Namecheap**. Possible statement text `NAMECHEAP INC`. Proposed classification IT expenses / Domain registration.
- **GoDaddy**. Possible statement text `GODADDY`. Proposed classification IT expenses / Domain registration.
- **GoDaddy**. Possible statement text `GODADDY.COM`. Proposed classification IT expenses / Domain registration.
- **Cloudways (DigitalOcean)**. Possible statement text `CLOUDWAYS`. Proposed classification IT expenses / Cloud infrastructure.
- **Webflow**. Possible statement text `WEBFLOW`. Proposed classification IT expenses / Software subscriptions.
- **Webflow**. Possible statement text `WEBFLOW INC`. Proposed classification IT expenses / Software subscriptions.
- **Squarespace**. Possible statement text `SQUARESPACE`. Proposed classification IT expenses / Software subscriptions.
- **Squarespace**. Possible statement text `SQUARESPACE IRE`. Proposed classification IT expenses / Software subscriptions.
- **Shopify**. Possible statement text `SHOPIFY`. Proposed classification IT expenses / Software subscriptions.
- **Shopify**. Possible statement text `SHOPIFY *`. Proposed classification IT expenses / Software subscriptions.
- **Vercel**. Possible statement text `VERCEL INC`. Proposed classification IT expenses / Cloud infrastructure.
- **Supabase**. Possible statement text `SUPABASE`. Proposed classification IT expenses / Cloud infrastructure.
- **Supabase**. Possible statement text `SUPABASE INC`. Proposed classification IT expenses / Cloud infrastructure.
- **PlanetScale**. Possible statement text `PLANETSCALE`. Proposed classification IT expenses / Cloud infrastructure.
- **Neon**. Possible statement text `NEON TECH`. Proposed classification IT expenses / Cloud infrastructure.
- **Elastic**. Possible statement text `ELASTIC`. Proposed classification IT expenses / Software subscriptions.
- **Elastic**. Possible statement text `ELASTIC N.V.`. Proposed classification IT expenses / Software subscriptions.
- **Cloudinary**. Possible statement text `CLOUDINARY`. Proposed classification IT expenses / Cloud infrastructure.
- **Algolia**. Possible statement text `ALGOLIA`. Proposed classification IT expenses / Software subscriptions.
- **Twitch**. Possible statement text `TWITCH`. Proposed classification NOT deductible unless business use proven.
- **Udemy**. Possible statement text `UDEMY`. Proposed classification Professional development / Training.
- **Coursera**. Possible statement text `COURSERA`. Proposed classification Professional development / Training.

## Worked cases

### Duplicate feed versus supplier bill

A client provides a USD600 annual invoice and a matching USD600 bank-feed debit for that same paid invoice. They are two records of one purchase, not USD1,200 of expenses. With an approved accrual policy and three service months used, the USD600 business cost splits USD150 current expense/USD450 prepayment. Link the payment to the existing supplier bill; retain both source records and the duplicate decision.

```oa-check
name: SaaS bill and bank-feed control
inputs:
  bill: 600
  bank_debit: 600
  elapsed_months: 3
steps:
  - raw_records_total: bill + bank_debit
  - duplicate_representation: bank_debit
  - unique_cost: raw_records_total - duplicate_representation
  - expense: unique_cost * elapsed_months / 12
  - prepayment: unique_cost - expense
expected:
  raw_records_total: 1200
  unique_cost: 600
  expense: 150
  prepayment: 450
```

## Existing review requirement

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.gov.uk/self-employed-records/what-records-to-keep | 2026-11-14 | Read for sales/expense proof, accurate records, distinguishing business transactions and accrual records. |
| https://www.gov.uk/expenses-if-youre-self-employed | 2026-11-14 | Read for sole-trader/partner business-purpose allocation, ordinary expenses versus equipment and cash/traditional basis. |
| https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-11-14 | Read for sections2-6 and13, actual supply, belonging, reverse-charge conditions, input-tax limits and unregistered recipients. |
| https://standards.aasb.gov.au/sites/default/files/2025-03/AASB121_08-15_COMPoct23_01-25.pdf | 2026-11-14 | Read for paragraphs20-23 and27-30, initial recognition, monetary closing balances and settlement exchange differences; Australian IFRS-equivalent financial reporting, not universal tax translation. |

Not yet confirmed: the current legal billing entity, country, ownership, descriptor availability and VAT/GST assertion formerly attached to each historical candidate below. These old assertions are recorded for comparison only and must not be used to compute or post tax. Official EU legislation could not be reopened during the current EUR-Lex outage; use the selected country's actual official source. No vendor source was used.

- Historical, not usable guidance, AWS: VAT/GST treatment: Reverse charge if billed by AWS EMEA SARL (Luxembourg) to non-LU EU businesses. US: no sales tax on most cloud services. AU: GST on invoice.; Notes: AWS bills from multiple entities depending on region.
- Historical, not usable guidance, AWS: VAT/GST treatment: EU reverse charge applies (B2B). VAT number required on invoice.; Notes: European billing entity.
- Historical, not usable guidance, AWS: VAT/GST treatment: Check invoice for billing entity.; Notes: Card statement abbreviation.
- Historical, not usable guidance, AWS: VAT/GST treatment: Check invoice for billing entity.; Notes: Truncated card statement.
- Historical, not usable guidance, Google Cloud Platform: VAT/GST treatment: Billed by Google Cloud EMEA Ltd (Ireland) for EU. Reverse charge for EU B2B.; Notes: Also appears as `GOOGLE *CLOUD`.
- Historical, not usable guidance, Google Cloud Platform: VAT/GST treatment: Same as above.; Notes: Card statement variant.
- Historical, not usable guidance, Google Cloud Platform: VAT/GST treatment: Same as above.; Notes: Older card format.
- Historical, not usable guidance, Microsoft Azure: VAT/GST treatment: Billed by Microsoft Ireland Operations Ltd for EU. Reverse charge B2B.
- Historical, not usable guidance, Microsoft Azure: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Microsoft Azure: VAT/GST treatment: Same as above.; Notes: Shortened card format.
- Historical, not usable guidance, DigitalOcean: VAT/GST treatment: US entity (DigitalOcean LLC). No VAT charged to non-US. EU: reverse charge on import of services.
- Historical, not usable guidance, DigitalOcean: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Heroku (Salesforce): VAT/GST treatment: Billed by Salesforce. Check invoice entity.; Notes: Now part of Salesforce.
- Historical, not usable guidance, Heroku (Salesforce): VAT/GST treatment: Same as above.
- Historical, not usable guidance, Vercel: VAT/GST treatment: US entity. EU: reverse charge on import.
- Historical, not usable guidance, Vercel: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Netlify: VAT/GST treatment: US entity. EU: reverse charge on import.
- Historical, not usable guidance, Cloudflare: VAT/GST treatment: US entity. EU: reverse charge. UK: reverse charge.; Notes: Also covers Cloudflare Workers, R2, etc.
- Historical, not usable guidance, Cloudflare: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Linode (Akamai): VAT/GST treatment: US entity. EU: reverse charge on import.; Notes: Now part of Akamai.
- Historical, not usable guidance, Linode (Akamai): VAT/GST treatment: Same as above.; Notes: Post-acquisition branding.
- Historical, not usable guidance, Hetzner: VAT/GST treatment: German entity. EU B2B: reverse charge if buyer outside DE and provides VAT ID. DE domestic: 19% VAT.
- Historical, not usable guidance, Hetzner: VAT/GST treatment: Same as above.
- Historical, not usable guidance, OVHcloud: VAT/GST treatment: French entity. EU B2B: reverse charge if buyer outside FR. FR domestic: 20% TVA.
- Historical, not usable guidance, OVHcloud: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Vultr: VAT/GST treatment: US entity. EU: reverse charge on import.
- Historical, not usable guidance, Render: VAT/GST treatment: US entity. EU: reverse charge on import.
- Historical, not usable guidance, Fly.io: VAT/GST treatment: US entity. EU: reverse charge on import.
- Historical, not usable guidance, Railway: VAT/GST treatment: US entity. EU: reverse charge on import.
- Historical, not usable guidance, GitHub: VAT/GST treatment: US entity (Microsoft). EU: reverse charge.; Notes: Free tier exists; charges indicate paid plan.
- Historical, not usable guidance, GitHub: VAT/GST treatment: Same as above.
- Historical, not usable guidance, GitLab: VAT/GST treatment: US entity. EU: reverse charge. NL entity for some EU billing.; Notes: Check invoice entity.
- Historical, not usable guidance, GitLab: VAT/GST treatment: Same as above.
- Historical, not usable guidance, GitLab: VAT/GST treatment: NL entity. EU B2B: reverse charge if outside NL.; Notes: EU billing entity.
- Historical, not usable guidance, Bitbucket / Jira / Confluence: VAT/GST treatment: AU entity for some billing; US for others. Check invoice.; Notes: Atlassian owns Bitbucket, Jira, Confluence, Trello.
- Historical, not usable guidance, Bitbucket / Jira / Confluence: VAT/GST treatment: Same as above.
- Historical, not usable guidance, JetBrains: VAT/GST treatment: CZ entity (JetBrains s.r.o.). EU B2B: reverse charge if outside CZ.; Notes: IntelliJ, PyCharm, WebStorm, etc.
- Historical, not usable guidance, JetBrains: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Docker: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Docker Desktop paid plans.
- Historical, not usable guidance, Docker: VAT/GST treatment: Same as above.
- Historical, not usable guidance, HashiCorp (Terraform Cloud): VAT/GST treatment: US entity. EU: reverse charge.; Notes: Terraform, Vault, etc.
- Historical, not usable guidance, Datadog: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Monitoring/observability.
- Historical, not usable guidance, Datadog: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Sentry: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Error tracking.
- Historical, not usable guidance, Sentry: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Sentry: VAT/GST treatment: Same as above.; Notes: Legal entity name.
- Historical, not usable guidance, New Relic: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Observability.
- Historical, not usable guidance, PagerDuty: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Incident management.
- Historical, not usable guidance, Postman: VAT/GST treatment: US entity. EU: reverse charge.; Notes: API development.
- Historical, not usable guidance, npm (GitHub): VAT/GST treatment: US entity. EU: reverse charge.; Notes: npm paid plans.
- Historical, not usable guidance, CircleCI: VAT/GST treatment: US entity. EU: reverse charge.; Notes: CI/CD.
- Historical, not usable guidance, Travis CI: VAT/GST treatment: DE entity (Travis CI GmbH). EU B2B: reverse charge if outside DE.; Notes: CI/CD.
- Historical, not usable guidance, Figma: VAT/GST treatment: US entity (now Adobe). EU: reverse charge.
- Historical, not usable guidance, Figma: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Adobe Creative Cloud: VAT/GST treatment: IE entity for EU (Adobe Systems Software Ireland). Reverse charge EU B2B outside IE.; Notes: Photoshop, Illustrator, Premiere, etc.
- Historical, not usable guidance, Adobe Creative Cloud: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Adobe Creative Cloud: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Adobe Creative Cloud: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Canva: VAT/GST treatment: AU entity. AU domestic: GST included. EU: reverse charge on import.; Notes: Canva Pro/Teams.
- Historical, not usable guidance, Canva: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Canva: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Sketch: VAT/GST treatment: NL entity. EU B2B: reverse charge if outside NL. NL domestic: 21% BTW.; Notes: macOS design tool.
- Historical, not usable guidance, Sketch: VAT/GST treatment: Same as above.
- Historical, not usable guidance, InVision: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Prototyping (winding down).
- Historical, not usable guidance, Miro: VAT/GST treatment: NL entity (RealtimeBoard B.V.). EU B2B: reverse charge if outside NL.; Notes: Collaborative whiteboard.
- Historical, not usable guidance, Miro: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Miro: VAT/GST treatment: Same as above.; Notes: Former name.
- Historical, not usable guidance, Slack (Salesforce): VAT/GST treatment: US entity. IE entity for some EU billing. Check invoice.
- Historical, not usable guidance, Slack (Salesforce): VAT/GST treatment: Same as above.
- Historical, not usable guidance, Zoom: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Video conferencing.
- Historical, not usable guidance, Zoom: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Zoom: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Microsoft 365: VAT/GST treatment: IE entity for EU (Microsoft Ireland Operations). Reverse charge EU B2B.; Notes: Word, Excel, Outlook, Teams.
- Historical, not usable guidance, Microsoft 365: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Microsoft 365: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Microsoft 365: VAT/GST treatment: Same as above.; Notes: Various Microsoft products.
- Historical, not usable guidance, Google Workspace: VAT/GST treatment: IE entity for EU (Google Ireland Ltd). Reverse charge EU B2B.; Notes: Legacy name.
- Historical, not usable guidance, Google Workspace: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Google Workspace: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Discord Nitro: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Only deductible if genuine business use (e.g., community management).
- Historical, not usable guidance, Discord Nitro: VAT/GST treatment: Same as above.; Notes: Personal use is NOT deductible.
- Historical, not usable guidance, Loom: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Screen recording.
- Historical, not usable guidance, Loom: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Calendly: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Scheduling.
- Historical, not usable guidance, Twilio: VAT/GST treatment: US entity. EU: reverse charge.; Notes: SMS/voice API.
- Historical, not usable guidance, Twilio: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Jira / Confluence: VAT/GST treatment: AU/US entity. Check invoice.; Notes: See Dev Tools section for Atlassian.
- Historical, not usable guidance, Asana: VAT/GST treatment: US entity. EU: reverse charge.
- Historical, not usable guidance, Asana: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Monday.com: VAT/GST treatment: IL entity (monday.com Ltd). EU: reverse charge on import.
- Historical, not usable guidance, Monday.com: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Notion: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Notes, wikis, project management.
- Historical, not usable guidance, Notion: VAT/GST treatment: Same as above.
- Historical, not usable guidance, ClickUp: VAT/GST treatment: US entity. EU: reverse charge.
- Historical, not usable guidance, ClickUp: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Linear: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Issue tracking.
- Historical, not usable guidance, Linear: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Basecamp: VAT/GST treatment: US entity. EU: reverse charge.
- Historical, not usable guidance, Basecamp: VAT/GST treatment: Same as above.; Notes: Parent company name.
- Historical, not usable guidance, Trello (Atlassian): VAT/GST treatment: See Atlassian.
- Historical, not usable guidance, Trello (Atlassian): VAT/GST treatment: Same as above.
- Historical, not usable guidance, Mailchimp (Intuit): VAT/GST treatment: US entity. EU: reverse charge.; Notes: Email marketing.
- Historical, not usable guidance, Mailchimp (Intuit): VAT/GST treatment: Same as above.
- Historical, not usable guidance, ConvertKit (Kit): VAT/GST treatment: US entity. EU: reverse charge.; Notes: Rebranded to "Kit" in 2024.
- Historical, not usable guidance, ConvertKit (Kit): VAT/GST treatment: Same as above.; Notes: New brand name.
- Historical, not usable guidance, HubSpot: VAT/GST treatment: US entity. IE entity for some EU billing. Check invoice.; Notes: CRM + marketing.
- Historical, not usable guidance, HubSpot: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Ahrefs: VAT/GST treatment: SG entity (Ahrefs Pte. Ltd.). EU: reverse charge on import.; Notes: SEO tool.
- Historical, not usable guidance, Ahrefs: VAT/GST treatment: Same as above.
- Historical, not usable guidance, SEMrush: VAT/GST treatment: US entity. EU: reverse charge.; Notes: SEO/marketing tool.
- Historical, not usable guidance, SEMrush: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Buffer: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Social media scheduling.
- Historical, not usable guidance, Buffer: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Hootsuite: VAT/GST treatment: CA entity. EU: reverse charge on import.; Notes: Social media management.
- Historical, not usable guidance, Hootsuite: VAT/GST treatment: Same as above.
- Historical, not usable guidance, ActiveCampaign: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Email marketing / CRM.
- Historical, not usable guidance, Brevo (Sendinblue): VAT/GST treatment: FR entity. EU B2B: reverse charge if outside FR. FR: 20% TVA.; Notes: Rebranded to Brevo.
- Historical, not usable guidance, Brevo (Sendinblue): VAT/GST treatment: Same as above.
- Historical, not usable guidance, Xero: VAT/GST treatment: NZ entity. AU: GST. EU: reverse charge on import. UK: reverse charge.
- Historical, not usable guidance, Xero: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Xero: VAT/GST treatment: UK entity. UK domestic: 20% VAT.; Notes: UK billing entity.
- Historical, not usable guidance, QuickBooks (Intuit): VAT/GST treatment: US entity. EU: reverse charge.
- Historical, not usable guidance, QuickBooks (Intuit): VAT/GST treatment: Same as above.
- Historical, not usable guidance, QuickBooks (Intuit): VAT/GST treatment: Same as above.
- Historical, not usable guidance, FreshBooks: VAT/GST treatment: CA entity. EU: reverse charge on import.
- Historical, not usable guidance, Wave: VAT/GST treatment: CA entity. EU: reverse charge on import.; Notes: Invoicing and accounting.
- Historical, not usable guidance, Wave: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Stripe: VAT/GST treatment: IE entity for EU. US entity for US. Check invoice.; Notes: See global-payment-processors.md for classification rules.
- Historical, not usable guidance, Stripe: VAT/GST treatment: Same as above.
- Historical, not usable guidance, PayPal: VAT/GST treatment: LU entity for EU. US entity for US.; Notes: See global-payment-processors.md.
- Historical, not usable guidance, PayPal: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Wise: VAT/GST treatment: UK/EU entity.; Notes: See global-payment-processors.md. Formerly TransferWise.
- Historical, not usable guidance, Wise: VAT/GST treatment: Same as above.; Notes: Legacy name.
- Historical, not usable guidance, Revolut: VAT/GST treatment: LT entity (EU). UK entity for UK.; Notes: Business account fees.
- Historical, not usable guidance, Revolut: VAT/GST treatment: Same as above.
- Historical, not usable guidance, OpenAI: VAT/GST treatment: US entity. EU: reverse charge.; Notes: ChatGPT Plus, API usage.
- Historical, not usable guidance, OpenAI: VAT/GST treatment: Same as above.; Notes: ChatGPT subscription.
- Historical, not usable guidance, OpenAI: VAT/GST treatment: Same as above.; Notes: API charges.
- Historical, not usable guidance, Anthropic: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Claude API / Pro subscription.
- Historical, not usable guidance, Anthropic: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Midjourney: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Image generation. Business use only.
- Historical, not usable guidance, Midjourney: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Stability AI: VAT/GST treatment: UK entity. EU: reverse charge on import if outside UK.; Notes: Stable Diffusion API.
- Historical, not usable guidance, Stability AI: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Hugging Face: VAT/GST treatment: US entity. EU: reverse charge.; Notes: ML model hosting.
- Historical, not usable guidance, Hugging Face: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Replicate: VAT/GST treatment: US entity. EU: reverse charge.; Notes: ML inference API.
- Historical, not usable guidance, Replicate: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Perplexity AI: VAT/GST treatment: US entity. EU: reverse charge.; Notes: AI search.
- Historical, not usable guidance, Cursor (Anysphere): VAT/GST treatment: US entity. EU: reverse charge.; Notes: AI code editor.
- Historical, not usable guidance, Cursor (Anysphere): VAT/GST treatment: Same as above.; Notes: Legal entity name.
- Historical, not usable guidance, DocuSign: VAT/GST treatment: US entity. EU: reverse charge.; Notes: E-signatures.
- Historical, not usable guidance, DocuSign: VAT/GST treatment: Same as above.
- Historical, not usable guidance, HelloSign (Dropbox): VAT/GST treatment: US entity. EU: reverse charge.; Notes: Now part of Dropbox Sign.
- Historical, not usable guidance, Dropbox Sign: VAT/GST treatment: Same as above.; Notes: Rebranded from HelloSign.
- Historical, not usable guidance, PandaDoc: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Document automation.
- Historical, not usable guidance, PandaDoc: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Termly: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Privacy policy generator.
- Historical, not usable guidance, Termly: VAT/GST treatment: Same as above.
- Historical, not usable guidance, 1Password: VAT/GST treatment: CA entity. EU: reverse charge on import.; Notes: Password manager.
- Historical, not usable guidance, 1Password: VAT/GST treatment: Same as above.; Notes: Legal entity name.
- Historical, not usable guidance, LastPass: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Password manager.
- Historical, not usable guidance, LastPass: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Bitwarden: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Password manager.
- Historical, not usable guidance, Bitwarden: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Dropbox: VAT/GST treatment: IE entity for EU (Dropbox International). Reverse charge EU B2B.; Notes: Cloud storage.
- Historical, not usable guidance, Dropbox: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Apple (iCloud+): VAT/GST treatment: IE entity for EU (Apple Distribution International). Reverse charge EU B2B.; Notes: iCloud+, Apple One. Verify business use.
- Historical, not usable guidance, Apple (iCloud+): VAT/GST treatment: Same as above.
- Historical, not usable guidance, Spotify: VAT/GST treatment: SE entity.; Notes: Only deductible if genuinely used for business (e.g., background music for retail, podcast hosting). Personal listening is NOT deductible.
- Historical, not usable guidance, Spotify: VAT/GST treatment: Same as above.
- Historical, not usable guidance, LinkedIn Premium: VAT/GST treatment: IE entity for EU (LinkedIn Ireland). Reverse charge EU B2B.; Notes: Premium, Sales Navigator, Recruiter, Learning.
- Historical, not usable guidance, LinkedIn Premium: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Grammarly: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Writing assistant.
- Historical, not usable guidance, Grammarly: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Zapier: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Workflow automation.
- Historical, not usable guidance, Zapier: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Make (Integromat): VAT/GST treatment: CZ entity. EU B2B: reverse charge if outside CZ.; Notes: Formerly Integromat.
- Historical, not usable guidance, Make (Integromat): VAT/GST treatment: Same as above.; Notes: Legacy name.
- Historical, not usable guidance, Typeform: VAT/GST treatment: ES entity. EU B2B: reverse charge if outside ES. ES domestic: 21% IVA.; Notes: Form/survey builder.
- Historical, not usable guidance, Typeform: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Intercom: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Customer messaging.
- Historical, not usable guidance, Intercom: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Zendesk: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Help desk.
- Historical, not usable guidance, Zendesk: VAT/GST treatment: Same as above.
- Historical, not usable guidance, SendGrid (Twilio): VAT/GST treatment: US entity. EU: reverse charge.; Notes: Transactional email.
- Historical, not usable guidance, SendGrid (Twilio): VAT/GST treatment: Same as above.
- Historical, not usable guidance, Namecheap: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Domain registration, SSL.
- Historical, not usable guidance, Namecheap: VAT/GST treatment: Same as above.
- Historical, not usable guidance, GoDaddy: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Domain registration, hosting.
- Historical, not usable guidance, GoDaddy: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Cloudways (DigitalOcean): VAT/GST treatment: US entity. EU: reverse charge.; Notes: Managed hosting.
- Historical, not usable guidance, Webflow: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Website builder.
- Historical, not usable guidance, Webflow: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Squarespace: VAT/GST treatment: IE entity for EU. Reverse charge EU B2B.; Notes: Website builder.
- Historical, not usable guidance, Squarespace: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Shopify: VAT/GST treatment: CA entity. IE entity for some EU billing. Check invoice.; Notes: E-commerce platform.
- Historical, not usable guidance, Shopify: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Vercel: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Frontend cloud.
- Historical, not usable guidance, Supabase: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Backend-as-a-service.
- Historical, not usable guidance, Supabase: VAT/GST treatment: Same as above.
- Historical, not usable guidance, PlanetScale: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Database platform.
- Historical, not usable guidance, Neon: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Serverless Postgres.
- Historical, not usable guidance, Elastic: VAT/GST treatment: NL entity (Elastic N.V.). EU B2B: reverse charge if outside NL.; Notes: Elasticsearch, Kibana.
- Historical, not usable guidance, Elastic: VAT/GST treatment: Same as above.
- Historical, not usable guidance, Cloudinary: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Media management.
- Historical, not usable guidance, Algolia: VAT/GST treatment: US entity. FR entity for some billing. Check invoice.; Notes: Search API.
- Historical, not usable guidance, Twitch: VAT/GST treatment: US entity (Amazon).; Notes: Only deductible if used for business streaming/marketing.
- Historical, not usable guidance, Udemy: VAT/GST treatment: IE entity for EU. US entity for US.; Notes: Online courses. Deductible if business-related.
- Historical, not usable guidance, Coursera: VAT/GST treatment: US entity. EU: reverse charge.; Notes: Same as Udemy.
