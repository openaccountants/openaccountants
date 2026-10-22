# Vendor Pattern Library

Global vendor classification cheatsheets. Each file maps common bank-statement strings to default classification, VAT/GST treatment, and any notable gotchas.

## Files

| File | What it covers |
|---|---|
| [`global-cloud-infrastructure.md`](global-cloud-infrastructure.md) | AWS, Azure, GCP, Cloudflare, DigitalOcean, Hetzner, OVHcloud, Vercel, Netlify, Datadog, GitHub, Twilio, MongoDB Atlas, Snowflake, Databricks and more |
| [`global-productivity-tools.md`](global-productivity-tools.md) | Microsoft 365, Google Workspace, Slack, Notion, Linear, Asana, Figma, Adobe, Dropbox, Zoom, HubSpot, Salesforce, Intercom, OpenAI, Anthropic, Xero, QuickBooks and more |
| [`global-ad-platforms.md`](global-ad-platforms.md) | Google Ads, Meta, LinkedIn, TikTok, X, Microsoft Ads, Amazon Ads, Reddit, Pinterest, Spotify Ads and more — includes India 6% EL withholding |
| [`global-marketplaces-banking-fees.md`](global-marketplaces-banking-fees.md) | Etsy, eBay, Amazon Seller, Fiverr, Upwork, Patreon, Gumroad, OnlyFans plus all bank fee patterns (wire, FX, ATM, overdraft) |
| [`global-saas-vendors.md`](global-saas-vendors.md) | Legacy SaaS catalogue (subsumed by global-productivity-tools) |
| [`global-payment-processors.md`](global-payment-processors.md) | Stripe, PayPal, Wise, Adyen, Square, Razorpay and more |
| [`global-home-office.md`](global-home-office.md) | Home office expense patterns (utilities, internet, supplies) |
| [`global-travel-expenses.md`](global-travel-expenses.md) | Airlines, hotels, ride-sharing, conference fees |
| [`global-vehicle-expenses.md`](global-vehicle-expenses.md) | Fuel, insurance, leasing, mileage tracking |

---

## How to use

Pattern files are loaded automatically by country packages. They make classification faster: instead of asking "what is `STRIPE PAYMENTS UK LTD`?" the AI already knows it's a payment processor and classifies the fee correctly.

If you find a vendor missing or misclassified, that's the easiest contribution to make — submit a PR with the vendor name, the bank-statement variations you've seen, and the correct default classification.

See the [README](../../README.md) for how to load skills into your AI.
