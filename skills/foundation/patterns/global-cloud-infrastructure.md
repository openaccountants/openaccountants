---
name: global-cloud-infrastructure
description: "Pattern library for cloud, infrastructure, and developer tool vendors that appear on bank statements and ledger detail worldwide. Use when classifying an unknown transaction line. Provides the canonical vendor name, common bank statement variations, default Schedule C / category mapping, VAT treatment (B2B reverse charge for most cross-border digital services), and notes on currency, billing cycle, and any sector-specific gotchas. Covers AWS, Azure, GCP, Cloudflare, DigitalOcean, Linode/Akamai, Hetzner, OVHcloud, Vultr, Render, Vercel, Netlify, Fly.io, Railway, Heroku, Backblaze, Wasabi, Datadog, New Relic, PagerDuty, GitHub, GitLab, Sentry, LaunchDarkly, Twilio, SendGrid, Mailgun, Resend, Postmark. Does NOT cover: SaaS productivity tools (see global-productivity-tools), ad platforms (see global-ad-platforms), or payment processors (see global-payment-processors)."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: pattern
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Global Cloud Infrastructure

## Global Cloud & Infrastructure Vendor Patterns v0.1

## How to use

When a bank statement / ledger line contains one of the variations below, apply the default classification. Override only with documentary evidence.

## Pattern table

**Pattern table**

| Vendor | Bank statement variations | Default category | VAT/GST notes | Notes |
| --- | --- | --- | --- | --- |
| **Amazon Web Services** | `AWS EMEA SARL`, `AMAZON WEB SERVICES`, `AWS BILLING`, `AWS EMEA SARL LUX`, `AMAZON DATA SERVICES IRELAND` | Cloud hosting / IT services | EU B2B: reverse charge (supplier in IE/LU). US: no VAT. UK B2B: reverse charge. Most non-EU: zero-rated export from supplier. | Monthly USD billing; consolidated invoice. Some accounts use AWS EMEA SARL (Luxembourg) for EU customers; AWS Inc for US. |
| **Microsoft Azure** | `MICROSOFT IRELAND OPS`, `MICROSOFT*AZURE`, `MSFT*AZURE`, `MICROSOFT AZURE` | Cloud hosting / IT services | EU B2B: reverse charge (supplier in IE — Microsoft Ireland Operations Ltd). | Monthly USD/EUR billing. |
| **Google Cloud Platform** | `GOOGLE *CLOUD`, `GOOGLE CLOUD`, `GOOGLE PAYMENT`, `GOOGLE CLOUD EMEA`, `GOOGLE IRELAND LTD` | Cloud hosting / IT services | EU B2B: reverse charge. | Monthly USD/EUR. |
| **Cloudflare** | `CLOUDFLARE INC`, `CLOUDFLARE.COM`, `CLOUDFLARE *`, `Cloudflare London` | CDN / network services | EU B2B: reverse charge (Cloudflare London Ltd for UK; Cloudflare Inc for US). | Monthly USD or annual. |
| **DigitalOcean** | `DIGITALOCEAN.COM`, `DIGITALOCEAN INC`, `DO *DIGITALOCEAN` | Cloud hosting | EU B2B: reverse charge (Netherlands BV). | Monthly USD. |
| **Linode (Akamai)** | `LINODE`, `AKAMAI TECH`, `LINODE LLC` | Cloud hosting | US supplier; EU B2B reverse charge. | Monthly USD. |
| **Hetzner** | `HETZNER ONLINE GMBH`, `HETZNER.COM` | Cloud hosting | Germany supplier; EU B2B reverse charge for EU customers; UK customers may face local VAT depending on supply rules. | Monthly EUR. |
| **OVHcloud** | `OVH*`, `OVHCLOUD`, `OVH SAS` | Cloud hosting | France supplier; EU B2B reverse charge. | Monthly EUR. |
| **Vultr** | `VULTR HOLDINGS`, `VULTR.COM` | Cloud hosting | US supplier (Vultr Holdings LLC). | Monthly USD. |
| **Render** | `RENDER SERVICES`, `RENDER.COM`, `RENDER` | Cloud hosting / PaaS | US supplier. | Monthly USD. |
| **Vercel** | `VERCEL INC`, `VERCEL.COM`, `VERCEL` | Cloud hosting / PaaS | US supplier. | Monthly USD. |
| **Netlify** | `NETLIFY INC`, `NETLIFY.COM` | Cloud hosting / PaaS | US supplier. | Monthly USD. |
| **Fly.io** | `FLY.IO`, `FLY INC` | Cloud hosting / edge | US supplier. | Monthly USD. |
| **Railway** | `RAILWAY.APP`, `RAILWAY INC` | Cloud hosting / PaaS | US supplier. | Monthly USD. |
| **Heroku** | `HEROKU`, `SALESFORCE HEROKU` | Cloud hosting / PaaS | Now Salesforce subsidiary; same classification. | Monthly USD. |
| **Backblaze** | `BACKBLAZE INC`, `BACKBLAZE B2` | Cloud storage / backup | US supplier. | Monthly USD. |
| **Wasabi** | `WASABI TECHNOLOGIES`, `WASABI.COM` | Cloud storage | US supplier. | Monthly USD. |
| **Datadog** | `DATADOG INC`, `DATADOG.COM` | Observability / monitoring | US supplier; EU B2B reverse charge. | Monthly USD (often annual contract). |
| **New Relic** | `NEW RELIC INC`, `NEWRELIC.COM` | Observability / monitoring | US supplier. | Monthly USD. |
| **PagerDuty** | `PAGERDUTY INC`, `PAGERDUTY.COM` | Incident management | US supplier. | Monthly USD. |
| **GitHub** | `GITHUB INC`, `GITHUB.COM`, `MICROSOFT*GITHUB` | Source control / CI / CD | GitHub Inc (Microsoft subsidiary). EU B2B reverse charge. | Monthly USD. |
| **GitLab** | `GITLAB INC`, `GITLAB.COM` | Source control / CI / CD | US supplier. | Monthly USD. |
| **Sentry** | `SENTRY.IO`, `FUNCTIONAL SOFTWARE` | Error tracking | US supplier (Functional Software Inc dba Sentry). | Monthly USD. |
| **LaunchDarkly** | `LAUNCHDARKLY INC` | Feature flags | US supplier. | Monthly USD. |
| **Twilio** | `TWILIO INC`, `TWILIO.COM`, `TWILIO IRELAND` | Communications API | Twilio Inc for US; Twilio Ireland for EU. EU B2B reverse charge. | Monthly USD/EUR usage-based. |
| **SendGrid** | `SENDGRID`, `TWILIO SENDGRID` | Email API | Twilio subsidiary; classify with Twilio. | Monthly USD. |
| **Mailgun** | `MAILGUN INC`, `MAILGUN TECHNOLOGIES` | Email API | US supplier. | Monthly USD. |
| **Resend** | `RESEND INC` | Email API | US supplier (newer). | Monthly USD. |
| **Postmark** | `POSTMARK`, `WILDBIT LLC` | Email API | US supplier (Wildbit LLC). | Monthly USD. |
| **MongoDB Atlas** | `MONGODB INC`, `MONGODB ATLAS` | Cloud database | US supplier. | Monthly USD. |
| **Snowflake** | `SNOWFLAKE INC`, `SNOWFLAKE COMPUTING` | Cloud data warehouse | US supplier. | Annual contract; consumption pricing. |
| **Databricks** | `DATABRICKS INC` | Cloud data platform | US supplier. | Annual contract. |
| **Pulumi** | `PULUMI CORP` | IaC | US supplier. | Monthly USD. |
| **HashiCorp / Terraform Cloud** | `HASHICORP INC` | IaC | US supplier; acquired by IBM 2024. | Monthly/annual USD. |

## Default classification rules

- **Schedule C (US sole prop)** — Line 25 — Utilities (cloud hosting); Line 22 — Supplies (small one-off); Line 17 — Legal/professional (consulting); Line 27a — Other expenses (with description)  _(Default classification rules)_
- **UK self-employment** — Box 22 (Other allowable expenses) or Box 21 (Phone/computer/internet)  _(Default classification rules)_
- **EU bookkeeping** — "Sonstige Aufwendungen — IT" / "Frais informatiques" / etc.  _(Default classification rules)_

## Cross-border VAT mechanics (B2B customer)

- **EU customer ← non-EU supplier** — Article 196 reverse charge; VAT self-assessed on local return  _(Cross-border VAT mechanics (B2B customer))_
- **EU customer ← EU supplier in different MS** — Article 196 reverse charge; VIES check on supplier VAT number  _(Cross-border VAT mechanics (B2B customer))_
- **UK customer ← non-UK supplier** — reverse charge per Section 8 VATA 1994  _(Section 8 VATA 1994)_
- **US customer** — no federal VAT; some states (NY, TX) impose sales/use tax on cloud services  _(Cross-border VAT mechanics (B2B customer))_
- **Australia customer ← non-AU supplier** — GST self-assessed if customer not GST-registered for these services  _(Cross-border VAT mechanics (B2B customer))_

## Self-checks

- [ ] Vendor identified from bank statement string
- [ ] EU/UK B2B reverse charge applied where supplier is non-resident
- [ ] Sales tax US state nexus checked where supplier has nexus
- [ ] Currency conversion applied to local books at appropriate rate
- [ ] Recurring billing cycle reflected in accrual / cash basis

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
