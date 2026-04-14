---
name: global-saas-vendors
description: >
  Deterministic lookup table of 100+ common SaaS/tech vendors that appear on freelancer
  bank statements worldwide. Maps bank statement text to vendor, category, default
  classification, and VAT/GST treatment for instant transaction recognition.
version: 0.1
category: patterns
depends_on: []
---

# Global SaaS Vendor Pattern Library v0.1

## What this file is

**Functional role:** Transaction pattern recognition lookup table
**Status:** Active reference data

This file provides deterministic matching rules for classifying SaaS and technology vendor charges that commonly appear on freelancer and small-business bank statements. Each entry maps one or more bank statement text patterns to a vendor identity, expense category, default classification, and cross-border VAT/GST treatment.

**How to use this table.** When classifying a bank transaction, search the "Bank statement text" column for a substring match against the transaction description. If matched, apply the default classification. Always confirm with the client if the subscription is genuinely for business use.

---

## Lookup table

### Cloud and hosting

| Bank statement text | Vendor | Category | Default classification | VAT/GST treatment | Notes |
|---|---|---|---|---|---|
| `AMAZON WEB SERVICES` | AWS | Cloud/Hosting | IT expenses / Cloud infrastructure | Reverse charge if billed by AWS EMEA SARL (Luxembourg) to non-LU EU businesses. US: no sales tax on most cloud services. AU: GST on invoice. | AWS bills from multiple entities depending on region. |
| `AWS EMEA SARL` | AWS | Cloud/Hosting | IT expenses / Cloud infrastructure | EU reverse charge applies (B2B). VAT number required on invoice. | European billing entity. |
| `AWS *SERVICES` | AWS | Cloud/Hosting | IT expenses / Cloud infrastructure | Check invoice for billing entity. | Card statement abbreviation. |
| `AMAZON WEB SERVI` | AWS | Cloud/Hosting | IT expenses / Cloud infrastructure | Check invoice for billing entity. | Truncated card statement. |
| `GOOGLE CLOUD` | Google Cloud Platform | Cloud/Hosting | IT expenses / Cloud infrastructure | Billed by Google Cloud EMEA Ltd (Ireland) for EU. Reverse charge for EU B2B. | Also appears as `GOOGLE *CLOUD`. |
| `GOOGLE *CLOUD` | Google Cloud Platform | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | Card statement variant. |
| `GOOGLE *GCP` | Google Cloud Platform | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | Older card format. |
| `MICROSOFT *AZURE` | Microsoft Azure | Cloud/Hosting | IT expenses / Cloud infrastructure | Billed by Microsoft Ireland Operations Ltd for EU. Reverse charge B2B. | |
| `MICROSOFT AZURE` | Microsoft Azure | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | |
| `MSFT *AZURE` | Microsoft Azure | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | Shortened card format. |
| `DIGITALOCEAN` | DigitalOcean | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity (DigitalOcean LLC). No VAT charged to non-US. EU: reverse charge on import of services. | |
| `DIGITALOCEAN.COM` | DigitalOcean | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | |
| `HEROKU` | Heroku (Salesforce) | Cloud/Hosting | IT expenses / Cloud infrastructure | Billed by Salesforce. Check invoice entity. | Now part of Salesforce. |
| `HEROKU *` | Heroku (Salesforce) | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | |
| `VERCEL INC` | Vercel | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge on import. | |
| `VERCEL` | Vercel | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | |
| `NETLIFY` | Netlify | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge on import. | |
| `CLOUDFLARE` | Cloudflare | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge. UK: reverse charge. | Also covers Cloudflare Workers, R2, etc. |
| `CLOUDFLARE.COM` | Cloudflare | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | |
| `LINODE` | Linode (Akamai) | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge on import. | Now part of Akamai. |
| `AKAMAI *LINODE` | Linode (Akamai) | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | Post-acquisition branding. |
| `HETZNER` | Hetzner | Cloud/Hosting | IT expenses / Cloud infrastructure | German entity. EU B2B: reverse charge if buyer outside DE and provides VAT ID. DE domestic: 19% VAT. | |
| `HETZNER ONLINE` | Hetzner | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | |
| `OVH` | OVHcloud | Cloud/Hosting | IT expenses / Cloud infrastructure | French entity. EU B2B: reverse charge if buyer outside FR. FR domestic: 20% TVA. | |
| `OVHCLOUD` | OVHcloud | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | |
| `VULTR` | Vultr | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge on import. | |
| `RENDER.COM` | Render | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge on import. | |
| `FLY.IO` | Fly.io | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge on import. | |
| `RAILWAY.APP` | Railway | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge on import. | |

### Developer tools

| Bank statement text | Vendor | Category | Default classification | VAT/GST treatment | Notes |
|---|---|---|---|---|---|
| `GITHUB` | GitHub | Dev Tools | IT expenses / Software subscriptions | US entity (Microsoft). EU: reverse charge. | Free tier exists; charges indicate paid plan. |
| `GITHUB INC` | GitHub | Dev Tools | IT expenses / Software subscriptions | Same as above. | |
| `GITLAB` | GitLab | Dev Tools | IT expenses / Software subscriptions | US entity. EU: reverse charge. NL entity for some EU billing. | Check invoice entity. |
| `GITLAB INC` | GitLab | Dev Tools | IT expenses / Software subscriptions | Same as above. | |
| `GITLAB B.V.` | GitLab | Dev Tools | IT expenses / Software subscriptions | NL entity. EU B2B: reverse charge if outside NL. | EU billing entity. |
| `ATLASSIAN` | Bitbucket / Jira / Confluence | Dev Tools | IT expenses / Software subscriptions | AU entity for some billing; US for others. Check invoice. | Atlassian owns Bitbucket, Jira, Confluence, Trello. |
| `ATLASSIAN *` | Bitbucket / Jira / Confluence | Dev Tools | IT expenses / Software subscriptions | Same as above. | |
| `JETBRAINS` | JetBrains | Dev Tools | IT expenses / Software subscriptions | CZ entity (JetBrains s.r.o.). EU B2B: reverse charge if outside CZ. | IntelliJ, PyCharm, WebStorm, etc. |
| `JETBRAINS S.R.O` | JetBrains | Dev Tools | IT expenses / Software subscriptions | Same as above. | |
| `DOCKER` | Docker | Dev Tools | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Docker Desktop paid plans. |
| `DOCKER INC` | Docker | Dev Tools | IT expenses / Software subscriptions | Same as above. | |
| `HASHICORP` | HashiCorp (Terraform Cloud) | Dev Tools | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Terraform, Vault, etc. |
| `DATADOG` | Datadog | Dev Tools | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Monitoring/observability. |
| `DATADOG INC` | Datadog | Dev Tools | IT expenses / Software subscriptions | Same as above. | |
| `SENTRY` | Sentry | Dev Tools | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Error tracking. |
| `SENTRY.IO` | Sentry | Dev Tools | IT expenses / Software subscriptions | Same as above. | |
| `GETSENTRY` | Sentry | Dev Tools | IT expenses / Software subscriptions | Same as above. | Legal entity name. |
| `NEW RELIC` | New Relic | Dev Tools | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Observability. |
| `PAGERDUTY` | PagerDuty | Dev Tools | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Incident management. |
| `POSTMAN` | Postman | Dev Tools | IT expenses / Software subscriptions | US entity. EU: reverse charge. | API development. |
| `NPMJS.COM` | npm (GitHub) | Dev Tools | IT expenses / Software subscriptions | US entity. EU: reverse charge. | npm paid plans. |
| `CIRCLECI` | CircleCI | Dev Tools | IT expenses / Software subscriptions | US entity. EU: reverse charge. | CI/CD. |
| `TRAVIS-CI` | Travis CI | Dev Tools | IT expenses / Software subscriptions | DE entity (Travis CI GmbH). EU B2B: reverse charge if outside DE. | CI/CD. |

### Design tools

| Bank statement text | Vendor | Category | Default classification | VAT/GST treatment | Notes |
|---|---|---|---|---|---|
| `FIGMA` | Figma | Design | IT expenses / Software subscriptions | US entity (now Adobe). EU: reverse charge. | |
| `FIGMA INC` | Figma | Design | IT expenses / Software subscriptions | Same as above. | |
| `ADOBE` | Adobe Creative Cloud | Design | IT expenses / Software subscriptions | IE entity for EU (Adobe Systems Software Ireland). Reverse charge EU B2B outside IE. | Photoshop, Illustrator, Premiere, etc. |
| `ADOBE CREATIVE` | Adobe Creative Cloud | Design | IT expenses / Software subscriptions | Same as above. | |
| `ADOBE *CREATIVE` | Adobe Creative Cloud | Design | IT expenses / Software subscriptions | Same as above. | |
| `ADOBE SYSTEMS` | Adobe Creative Cloud | Design | IT expenses / Software subscriptions | Same as above. | |
| `CANVA` | Canva | Design | IT expenses / Software subscriptions | AU entity. AU domestic: GST included. EU: reverse charge on import. | Canva Pro/Teams. |
| `CANVA.COM` | Canva | Design | IT expenses / Software subscriptions | Same as above. | |
| `CANVA PTY` | Canva | Design | IT expenses / Software subscriptions | Same as above. | |
| `SKETCH B.V.` | Sketch | Design | IT expenses / Software subscriptions | NL entity. EU B2B: reverse charge if outside NL. NL domestic: 21% BTW. | macOS design tool. |
| `SKETCH` | Sketch | Design | IT expenses / Software subscriptions | Same as above. | |
| `INVISIONAPP` | InVision | Design | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Prototyping (winding down). |
| `MIRO` | Miro | Design / Collaboration | IT expenses / Software subscriptions | NL entity (RealtimeBoard B.V.). EU B2B: reverse charge if outside NL. | Collaborative whiteboard. |
| `MIRO.COM` | Miro | Design / Collaboration | IT expenses / Software subscriptions | Same as above. | |
| `REALTIMEBOARD` | Miro | Design / Collaboration | IT expenses / Software subscriptions | Same as above. | Former name. |

### Communication

| Bank statement text | Vendor | Category | Default classification | VAT/GST treatment | Notes |
|---|---|---|---|---|---|
| `SLACK` | Slack (Salesforce) | Communication | IT expenses / Software subscriptions | US entity. IE entity for some EU billing. Check invoice. | |
| `SLACK TECHNOLOG` | Slack (Salesforce) | Communication | IT expenses / Software subscriptions | Same as above. | |
| `ZOOM.US` | Zoom | Communication | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Video conferencing. |
| `ZOOM VIDEO` | Zoom | Communication | IT expenses / Software subscriptions | Same as above. | |
| `ZOOM *` | Zoom | Communication | IT expenses / Software subscriptions | Same as above. | |
| `MICROSOFT *365` | Microsoft 365 | Communication / Productivity | IT expenses / Software subscriptions | IE entity for EU (Microsoft Ireland Operations). Reverse charge EU B2B. | Word, Excel, Outlook, Teams. |
| `MICROSOFT *OFFIC` | Microsoft 365 | Communication / Productivity | IT expenses / Software subscriptions | Same as above. | |
| `MSFT *M365` | Microsoft 365 | Communication / Productivity | IT expenses / Software subscriptions | Same as above. | |
| `MICROSOFT *MICRO` | Microsoft 365 | Communication / Productivity | IT expenses / Software subscriptions | Same as above. | Various Microsoft products. |
| `GOOGLE *GSUITE` | Google Workspace | Communication / Productivity | IT expenses / Software subscriptions | IE entity for EU (Google Ireland Ltd). Reverse charge EU B2B. | Legacy name. |
| `GOOGLE *WORKSPAC` | Google Workspace | Communication / Productivity | IT expenses / Software subscriptions | Same as above. | |
| `GOOGLE WORKSPACE` | Google Workspace | Communication / Productivity | IT expenses / Software subscriptions | Same as above. | |
| `DISCORD` | Discord Nitro | Communication | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Only deductible if genuine business use (e.g., community management). |
| `DISCORD NITRO` | Discord Nitro | Communication | IT expenses / Software subscriptions | Same as above. | Personal use is NOT deductible. |
| `LOOM` | Loom | Communication | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Screen recording. |
| `LOOM INC` | Loom | Communication | IT expenses / Software subscriptions | Same as above. | |
| `CALENDLY` | Calendly | Communication | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Scheduling. |
| `TWILIO` | Twilio | Communication | IT expenses / Software subscriptions | US entity. EU: reverse charge. | SMS/voice API. |
| `TWILIO INC` | Twilio | Communication | IT expenses / Software subscriptions | Same as above. | |

### Project management

| Bank statement text | Vendor | Category | Default classification | VAT/GST treatment | Notes |
|---|---|---|---|---|---|
| `ATLASSIAN` | Jira / Confluence | Project Management | IT expenses / Software subscriptions | AU/US entity. Check invoice. | See Dev Tools section for Atlassian. |
| `ASANA` | Asana | Project Management | IT expenses / Software subscriptions | US entity. EU: reverse charge. | |
| `ASANA INC` | Asana | Project Management | IT expenses / Software subscriptions | Same as above. | |
| `MONDAY.COM` | Monday.com | Project Management | IT expenses / Software subscriptions | IL entity (monday.com Ltd). EU: reverse charge on import. | |
| `MONDAY COM` | Monday.com | Project Management | IT expenses / Software subscriptions | Same as above. | |
| `NOTION` | Notion | Project Management | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Notes, wikis, project management. |
| `NOTION LABS` | Notion | Project Management | IT expenses / Software subscriptions | Same as above. | |
| `CLICKUP` | ClickUp | Project Management | IT expenses / Software subscriptions | US entity. EU: reverse charge. | |
| `CLICKUP.COM` | ClickUp | Project Management | IT expenses / Software subscriptions | Same as above. | |
| `LINEAR` | Linear | Project Management | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Issue tracking. |
| `LINEAR APP` | Linear | Project Management | IT expenses / Software subscriptions | Same as above. | |
| `BASECAMP` | Basecamp | Project Management | IT expenses / Software subscriptions | US entity. EU: reverse charge. | |
| `37SIGNALS` | Basecamp | Project Management | IT expenses / Software subscriptions | Same as above. | Parent company name. |
| `TRELLO` | Trello (Atlassian) | Project Management | IT expenses / Software subscriptions | See Atlassian. | |
| `TRELLO.COM` | Trello (Atlassian) | Project Management | IT expenses / Software subscriptions | Same as above. | |

### Marketing

| Bank statement text | Vendor | Category | Default classification | VAT/GST treatment | Notes |
|---|---|---|---|---|---|
| `MAILCHIMP` | Mailchimp (Intuit) | Marketing | Marketing / Advertising | US entity. EU: reverse charge. | Email marketing. |
| `MAILCHIMP *` | Mailchimp (Intuit) | Marketing | Marketing / Advertising | Same as above. | |
| `CONVERTKIT` | ConvertKit (Kit) | Marketing | Marketing / Advertising | US entity. EU: reverse charge. | Rebranded to "Kit" in 2024. |
| `KIT.COM` | ConvertKit (Kit) | Marketing | Marketing / Advertising | Same as above. | New brand name. |
| `HUBSPOT` | HubSpot | Marketing | Marketing / Advertising | US entity. IE entity for some EU billing. Check invoice. | CRM + marketing. |
| `HUBSPOT INC` | HubSpot | Marketing | Marketing / Advertising | Same as above. | |
| `AHREFS` | Ahrefs | Marketing | Marketing / Advertising | SG entity (Ahrefs Pte. Ltd.). EU: reverse charge on import. | SEO tool. |
| `AHREFS PTE` | Ahrefs | Marketing | Marketing / Advertising | Same as above. | |
| `SEMRUSH` | SEMrush | Marketing | Marketing / Advertising | US entity. EU: reverse charge. | SEO/marketing tool. |
| `SEMRUSH INC` | SEMrush | Marketing | Marketing / Advertising | Same as above. | |
| `BUFFER` | Buffer | Marketing | Marketing / Advertising | US entity. EU: reverse charge. | Social media scheduling. |
| `BUFFER INC` | Buffer | Marketing | Marketing / Advertising | Same as above. | |
| `HOOTSUITE` | Hootsuite | Marketing | Marketing / Advertising | CA entity. EU: reverse charge on import. | Social media management. |
| `HOOTSUITE INC` | Hootsuite | Marketing | Marketing / Advertising | Same as above. | |
| `ACTIVECAMPAIGN` | ActiveCampaign | Marketing | Marketing / Advertising | US entity. EU: reverse charge. | Email marketing / CRM. |
| `SENDINBLUE` | Brevo (Sendinblue) | Marketing | Marketing / Advertising | FR entity. EU B2B: reverse charge if outside FR. FR: 20% TVA. | Rebranded to Brevo. |
| `BREVO` | Brevo (Sendinblue) | Marketing | Marketing / Advertising | Same as above. | |

### Accounting and finance

| Bank statement text | Vendor | Category | Default classification | VAT/GST treatment | Notes |
|---|---|---|---|---|---|
| `XERO` | Xero | Accounting | Office expenses / Accounting software | NZ entity. AU: GST. EU: reverse charge on import. UK: reverse charge. | |
| `XERO LTD` | Xero | Accounting | Office expenses / Accounting software | Same as above. | |
| `XERO UK LTD` | Xero | Accounting | Office expenses / Accounting software | UK entity. UK domestic: 20% VAT. | UK billing entity. |
| `INTUIT *QUICKBOOK` | QuickBooks (Intuit) | Accounting | Office expenses / Accounting software | US entity. EU: reverse charge. | |
| `QUICKBOOKS` | QuickBooks (Intuit) | Accounting | Office expenses / Accounting software | Same as above. | |
| `INTUIT *QB` | QuickBooks (Intuit) | Accounting | Office expenses / Accounting software | Same as above. | |
| `FRESHBOOKS` | FreshBooks | Accounting | Office expenses / Accounting software | CA entity. EU: reverse charge on import. | |
| `WAVE FINANCIAL` | Wave | Accounting | Office expenses / Accounting software | CA entity. EU: reverse charge on import. | Invoicing and accounting. |
| `WAVE APPS` | Wave | Accounting | Office expenses / Accounting software | Same as above. | |
| `STRIPE` | Stripe | Payment Processing | Bank charges / Payment processing fees | IE entity for EU. US entity for US. Check invoice. | See global-payment-processors.md for classification rules. |
| `STRIPE PAYMENTS` | Stripe | Payment Processing | Bank charges / Payment processing fees | Same as above. | |
| `PAYPAL` | PayPal | Payment Processing | Bank charges / Payment processing fees | LU entity for EU. US entity for US. | See global-payment-processors.md. |
| `PAYPAL *` | PayPal | Payment Processing | Bank charges / Payment processing fees | Same as above. | |
| `WISE` | Wise | Payment Processing / FX | Bank charges / Transfer fees | UK/EU entity. | See global-payment-processors.md. Formerly TransferWise. |
| `TRANSFERWISE` | Wise | Payment Processing / FX | Bank charges / Transfer fees | Same as above. | Legacy name. |
| `REVOLUT` | Revolut | Banking | Bank charges | LT entity (EU). UK entity for UK. | Business account fees. |
| `REVOLUT *` | Revolut | Banking | Bank charges | Same as above. | |

### AI and ML

| Bank statement text | Vendor | Category | Default classification | VAT/GST treatment | Notes |
|---|---|---|---|---|---|
| `OPENAI` | OpenAI | AI/ML | IT expenses / Software subscriptions | US entity. EU: reverse charge. | ChatGPT Plus, API usage. |
| `OPENAI *CHATGPT` | OpenAI | AI/ML | IT expenses / Software subscriptions | Same as above. | ChatGPT subscription. |
| `OPENAI *` | OpenAI | AI/ML | IT expenses / Software subscriptions | Same as above. | API charges. |
| `ANTHROPIC` | Anthropic | AI/ML | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Claude API / Pro subscription. |
| `ANTHROPIC *` | Anthropic | AI/ML | IT expenses / Software subscriptions | Same as above. | |
| `MIDJOURNEY` | Midjourney | AI/ML | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Image generation. Business use only. |
| `MIDJOURNEY INC` | Midjourney | AI/ML | IT expenses / Software subscriptions | Same as above. | |
| `STABILITY AI` | Stability AI | AI/ML | IT expenses / Software subscriptions | UK entity. EU: reverse charge on import if outside UK. | Stable Diffusion API. |
| `STABILITY.AI` | Stability AI | AI/ML | IT expenses / Software subscriptions | Same as above. | |
| `HUGGING FACE` | Hugging Face | AI/ML | IT expenses / Software subscriptions | US entity. EU: reverse charge. | ML model hosting. |
| `HUGGINGFACE` | Hugging Face | AI/ML | IT expenses / Software subscriptions | Same as above. | |
| `REPLICATE` | Replicate | AI/ML | IT expenses / Software subscriptions | US entity. EU: reverse charge. | ML inference API. |
| `REPLICATE INC` | Replicate | AI/ML | IT expenses / Software subscriptions | Same as above. | |
| `PERPLEXITY` | Perplexity AI | AI/ML | IT expenses / Software subscriptions | US entity. EU: reverse charge. | AI search. |
| `CURSOR` | Cursor (Anysphere) | AI/ML | IT expenses / Software subscriptions | US entity. EU: reverse charge. | AI code editor. |
| `ANYSPHERE` | Cursor (Anysphere) | AI/ML | IT expenses / Software subscriptions | Same as above. | Legal entity name. |

### Legal and compliance

| Bank statement text | Vendor | Category | Default classification | VAT/GST treatment | Notes |
|---|---|---|---|---|---|
| `DOCUSIGN` | DocuSign | Legal/Compliance | Office expenses / Legal services | US entity. EU: reverse charge. | E-signatures. |
| `DOCUSIGN INC` | DocuSign | Legal/Compliance | Office expenses / Legal services | Same as above. | |
| `HELLOSIGN` | HelloSign (Dropbox) | Legal/Compliance | Office expenses / Legal services | US entity. EU: reverse charge. | Now part of Dropbox Sign. |
| `DROPBOX SIGN` | Dropbox Sign | Legal/Compliance | Office expenses / Legal services | Same as above. | Rebranded from HelloSign. |
| `PANDADOC` | PandaDoc | Legal/Compliance | Office expenses / Legal services | US entity. EU: reverse charge. | Document automation. |
| `PANDADOC INC` | PandaDoc | Legal/Compliance | Office expenses / Legal services | Same as above. | |
| `TERMLY` | Termly | Legal/Compliance | Office expenses / Legal services | US entity. EU: reverse charge. | Privacy policy generator. |
| `TERMLY.IO` | Termly | Legal/Compliance | Office expenses / Legal services | Same as above. | |

### Other SaaS

| Bank statement text | Vendor | Category | Default classification | VAT/GST treatment | Notes |
|---|---|---|---|---|---|
| `1PASSWORD` | 1Password | Security | IT expenses / Software subscriptions | CA entity. EU: reverse charge on import. | Password manager. |
| `AGILEBITS` | 1Password | Security | IT expenses / Software subscriptions | Same as above. | Legal entity name. |
| `LASTPASS` | LastPass | Security | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Password manager. |
| `LASTPASS.COM` | LastPass | Security | IT expenses / Software subscriptions | Same as above. | |
| `BITWARDEN` | Bitwarden | Security | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Password manager. |
| `BITWARDEN INC` | Bitwarden | Security | IT expenses / Software subscriptions | Same as above. | |
| `DROPBOX` | Dropbox | Storage | IT expenses / Software subscriptions | IE entity for EU (Dropbox International). Reverse charge EU B2B. | Cloud storage. |
| `DROPBOX *` | Dropbox | Storage | IT expenses / Software subscriptions | Same as above. | |
| `APPLE.COM/BILL` | Apple (iCloud+) | Storage / Productivity | IT expenses / Software subscriptions | IE entity for EU (Apple Distribution International). Reverse charge EU B2B. | iCloud+, Apple One. Verify business use. |
| `APPLE.COM *` | Apple (iCloud+) | Storage / Productivity | IT expenses / Software subscriptions | Same as above. | |
| `SPOTIFY` | Spotify | Media | NOT deductible unless business use proven | SE entity. | Only deductible if genuinely used for business (e.g., background music for retail, podcast hosting). Personal listening is NOT deductible. |
| `SPOTIFY AB` | Spotify | Media | NOT deductible unless business use proven | Same as above. | |
| `LINKEDIN` | LinkedIn Premium | Professional Development | Marketing / Professional development | IE entity for EU (LinkedIn Ireland). Reverse charge EU B2B. | Premium, Sales Navigator, Recruiter, Learning. |
| `LINKEDIN *` | LinkedIn Premium | Professional Development | Marketing / Professional development | Same as above. | |
| `GRAMMARLY` | Grammarly | Productivity | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Writing assistant. |
| `GRAMMARLY INC` | Grammarly | Productivity | IT expenses / Software subscriptions | Same as above. | |
| `ZAPIER` | Zapier | Automation | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Workflow automation. |
| `ZAPIER INC` | Zapier | Automation | IT expenses / Software subscriptions | Same as above. | |
| `MAKE.COM` | Make (Integromat) | Automation | IT expenses / Software subscriptions | CZ entity. EU B2B: reverse charge if outside CZ. | Formerly Integromat. |
| `INTEGROMAT` | Make (Integromat) | Automation | IT expenses / Software subscriptions | Same as above. | Legacy name. |
| `TYPEFORM` | Typeform | Productivity | IT expenses / Software subscriptions | ES entity. EU B2B: reverse charge if outside ES. ES domestic: 21% IVA. | Form/survey builder. |
| `TYPEFORM S.L.` | Typeform | Productivity | IT expenses / Software subscriptions | Same as above. | |
| `INTERCOM` | Intercom | Customer Support | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Customer messaging. |
| `INTERCOM INC` | Intercom | Customer Support | IT expenses / Software subscriptions | Same as above. | |
| `ZENDESK` | Zendesk | Customer Support | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Help desk. |
| `ZENDESK INC` | Zendesk | Customer Support | IT expenses / Software subscriptions | Same as above. | |
| `TWILIO SENDGRID` | SendGrid (Twilio) | Email Infrastructure | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Transactional email. |
| `SENDGRID` | SendGrid (Twilio) | Email Infrastructure | IT expenses / Software subscriptions | Same as above. | |
| `NAMECHEAP` | Namecheap | Domain/Hosting | IT expenses / Domain registration | US entity. EU: reverse charge. | Domain registration, SSL. |
| `NAMECHEAP INC` | Namecheap | Domain/Hosting | IT expenses / Domain registration | Same as above. | |
| `GODADDY` | GoDaddy | Domain/Hosting | IT expenses / Domain registration | US entity. EU: reverse charge. | Domain registration, hosting. |
| `GODADDY.COM` | GoDaddy | Domain/Hosting | IT expenses / Domain registration | Same as above. | |
| `CLOUDWAYS` | Cloudways (DigitalOcean) | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge. | Managed hosting. |
| `WEBFLOW` | Webflow | Design / Hosting | IT expenses / Software subscriptions | US entity. EU: reverse charge. | Website builder. |
| `WEBFLOW INC` | Webflow | Design / Hosting | IT expenses / Software subscriptions | Same as above. | |
| `SQUARESPACE` | Squarespace | Hosting / Website | IT expenses / Software subscriptions | IE entity for EU. Reverse charge EU B2B. | Website builder. |
| `SQUARESPACE IRE` | Squarespace | Hosting / Website | IT expenses / Software subscriptions | Same as above. | |
| `SHOPIFY` | Shopify | E-commerce | IT expenses / Software subscriptions | CA entity. IE entity for some EU billing. Check invoice. | E-commerce platform. |
| `SHOPIFY *` | Shopify | E-commerce | IT expenses / Software subscriptions | Same as above. | |
| `VERCEL INC` | Vercel | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge. | Frontend cloud. |
| `SUPABASE` | Supabase | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge. | Backend-as-a-service. |
| `SUPABASE INC` | Supabase | Cloud/Hosting | IT expenses / Cloud infrastructure | Same as above. | |
| `PLANETSCALE` | PlanetScale | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge. | Database platform. |
| `NEON TECH` | Neon | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge. | Serverless Postgres. |
| `ELASTIC` | Elastic | Dev Tools | IT expenses / Software subscriptions | NL entity (Elastic N.V.). EU B2B: reverse charge if outside NL. | Elasticsearch, Kibana. |
| `ELASTIC N.V.` | Elastic | Dev Tools | IT expenses / Software subscriptions | Same as above. | |
| `CLOUDINARY` | Cloudinary | Cloud/Hosting | IT expenses / Cloud infrastructure | US entity. EU: reverse charge. | Media management. |
| `ALGOLIA` | Algolia | Dev Tools | IT expenses / Software subscriptions | US entity. FR entity for some billing. Check invoice. | Search API. |
| `TWITCH` | Twitch | Media | NOT deductible unless business use proven | US entity (Amazon). | Only deductible if used for business streaming/marketing. |
| `UDEMY` | Udemy | Education | Professional development / Training | IE entity for EU. US entity for US. | Online courses. Deductible if business-related. |
| `COURSERA` | Coursera | Education | Professional development / Training | US entity. EU: reverse charge. | Same as Udemy. |

---

## Common mistakes

1. **Assuming all SaaS is deductible.** A subscription is only a business expense if it is used for business. Spotify, Netflix, Disney+, and similar are NOT business expenses unless the client can demonstrate genuine business use (e.g., a cafe playing background music via a business Spotify account).

2. **Missing reverse charge obligations.** When an EU-based business purchases from a non-EU SaaS vendor (or a vendor in a different EU member state), the buyer typically must self-assess VAT via the reverse charge mechanism. Failing to do so creates a VAT compliance gap even though it is usually net-neutral (output VAT = input VAT if fully taxable).

3. **Confusing payment processor charges with SaaS subscriptions.** Stripe, PayPal, and Wise appear in this table for their subscription/platform fees, but their transaction-level entries (payouts, transfers) are covered in `global-payment-processors.md`. Do not double-classify.

4. **Ignoring billing entity changes.** Many vendors restructure their billing entities (e.g., GitHub moving under Microsoft Ireland, Heroku under Salesforce). Always check the actual invoice to determine the billing entity for VAT purposes.

5. **Annual vs. monthly billing.** Large annual charges should be accrued across the period they cover, not expensed in the month of payment, if the client uses accrual accounting.

---

## Disclaimer

This lookup table provides general guidance for transaction classification. Tax rules, billing entities, and VAT treatment change frequently. Always verify against the actual invoice and consult the relevant jurisdiction's tax authority guidance. This is not tax advice. A qualified professional should review all classifications before filing.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
