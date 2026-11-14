---
name: global-productivity-tools
description: "Use this cross-country method in 2026 to investigate productivity and collaboration purchase classification. Treat bank strings as historical recognition hints, confirm the invoice and business purpose, separate personal use and timing, and apply the owning country tax method before posting. The output is a proposed accounting workpaper, not a verified merchant directory."
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

# Productivity and collaboration purchase classification v1.0

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
5. Resolve VAT/GST from the actual supply and parties, not the logo, payment currency or a remembered billing entity. For UK general-rule services from an overseas supplier, test Notice 741A sections 3-6, including the establishment connected with the supply, exemption and input-tax restriction. Its section 5.7 can affect registration for an unregistered buyer. A fully creditable reverse charge may be neutral; an exempt or partly exempt buyer can bear a cost. Do not apply the UK rule to another country. [HMRC Notice 741A](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a).
6. For an EU, Canadian, Australian or other-country buyer, load that country's VAT/GST method and official law before assigning its tax code. This global hint library supplies no universal EU reverse-charge exemption, US state sales-tax result, export zero rate or Australian imported-service self-assessment rule. Domestic versus cross-border status requires the actual supplying establishment. Keep unresolved tax separate in the working paper.
7. Apply the functional-currency policy, retaining both original and settled amounts. Under an applicable AASB 121/IFRS-equivalent financial-reporting policy, distinguish recognition-date translation, closing-rate monetary balances and settlement differences; do not use payment date for every accrual. Do not impose that reporting policy on a cash-basis tax return. [AASB 121 paragraphs 21-23,28-29](https://standards.aasb.gov.au/sites/default/files/2025-03/AASB 121_08-15_COMPoct23_01-25.pdf).
8. Produce proposed accounts, net/tax/gross, business/private allocation, expense/prepayment/capital split, book/tax adjustments and remaining questions, each linked to its evidence. If the ledger is read-only, deliver an import file or list of postings for a human to approve. A draft is not a posted journal. Reconcile the approved posting to the statement and retain the approval/import reference.

## When to refuse or refer

- Missing invoice, supplier, purpose, period, currency, duplicate status or business-use evidence: hold the final posting. Do not turn an unrecognised merchant into a confident expense.
- Capitalisation, mixed use, related-party charges, withholding, recoverability or a fixed establishment that changes the tax result: use the relevant country/subject method and refer unresolved interpretation.
- A payment processor or own-account transfer: use `global-payment-processors`; a purchase of hardware is not a SaaS fee. No blanket Schedule C line, UK box or 'EU bookkeeping' account is certified for every product and basis.
- Current vendor billing entities, ownership, country coverage, plans and exact statement descriptors were not verified under this wave's official-authority-only source policy. The historical hints are not certified live integrations or tax determinations.

### Productivity-specific checks

Confirm single-user Notion, Linear, Figma and Loom; Apple One/iCloud+ family plans; Spotify/Audible; personal Wix/Squarespace portfolio sites; password/VPN subscriptions; and accounting/payroll subscriptions from the actual business evidence. A business-looking tier is not proof of use, and a personal-looking vendor is not an automatic refusal. Distinguish software fees from payroll, client money, contractor/EOR payments and financial transfers. Route cloud, advertising and processors to their named companion methods.

## Recognition hints

These are historical search hints from the existing library, not a verified 2026 merchant directory. Match them to the client's actual invoice and account first. A substring match is neither supplier identification nor permission to post. Suggested accounts remain proposals until the business purpose and accounting policy are known.

### Vendor candidates
- **Microsoft 365 / Office 365**. Possible statement text `MICROSOFT*M365`, `MICROSOFT*365`, `MSFT*M365`, `MICROSOFT IRELAND OPS`. Proposed classification Software subscription / productivity.
- **Google Workspace**. Possible statement text `GOOGLE *G SUITE`, `GOOGLE *WORKSPACE`, `GOOGLE IRELAND LTD`. Proposed classification Software subscription / productivity.
- **Slack**. Possible statement text `SLACK TECHNOLOGIES`, `SLACK*`. Proposed classification Communications / SaaS.
- **Notion**. Possible statement text `NOTION LABS INC`, `NOTION.SO`. Proposed classification Productivity / docs.
- **Linear**. Possible statement text `LINEAR ORBIT INC`, `LINEAR.APP`. Proposed classification Project management.
- **Asana**. Possible statement text `ASANA INC`, `ASANA.COM`. Proposed classification Project management.
- **Trello**. Possible statement text `TRELLO`, `ATLASSIAN`. Proposed classification Project management.
- **Jira / Confluence**. Possible statement text `ATLASSIAN`, `ATLASSIAN US`, `ATLASSIAN PTY LTD`. Proposed classification Software development tools.
- **Figma**. Possible statement text `FIGMA INC`, `FIGMA.COM`. Proposed classification Design / collaboration.
- **Adobe Creative Cloud**. Possible statement text `ADOBE *CREATIVE`, `ADOBE IRELAND LTD`. Proposed classification Software subscription / creative.
- **Canva**. Possible statement text `CANVA*`, `CANVA PTY LTD`. Proposed classification Design.
- **Dropbox**. Possible statement text `DROPBOX INC`, `DROPBOX*`. Proposed classification File storage.
- **Box**. Possible statement text `BOX INC`, `BOX.COM`. Proposed classification File storage / content management.
- **Zoom**. Possible statement text `ZOOM.US`, `ZOOM VIDEO COMMS`, `ZOOM VOICE COMMS`. Proposed classification Video conferencing.
- **Calendly**. Possible statement text `CALENDLY INC`, `CALENDLY.COM`. Proposed classification Scheduling.
- **HubSpot**. Possible statement text `HUBSPOT INC`, `HUBSPOT.COM`. Proposed classification CRM / marketing.
- **Salesforce**. Possible statement text `SALESFORCE.COM`, `SALESFORCE*`, `SALESFORCE EMEA LTD`. Proposed classification CRM.
- **Intercom**. Possible statement text `INTERCOM INC`, `INTERCOM.COM`. Proposed classification Customer messaging.
- **Zendesk**. Possible statement text `ZENDESK INC`, `ZENDESK.COM`. Proposed classification Customer support.
- **Loom**. Possible statement text `LOOM INC`, `LOOM.COM`. Proposed classification Video messaging.
- **Miro**. Possible statement text `MIRO INC`, `RTBI INC`. Proposed classification Whiteboarding.
- **ClickUp**. Possible statement text `CLICKUP`, `MANGO TECHNOLOGIES`. Proposed classification Project management.
- **Monday.com**. Possible statement text `MONDAY.COM`, `MONDAY.COM LTD`. Proposed classification Project management.
- **Airtable**. Possible statement text `AIRTABLE INC`, `AIRTABLE.COM`. Proposed classification Database / collaboration.
- **Webflow**. Possible statement text `WEBFLOW INC`, `WEBFLOW.COM`. Proposed classification Website builder.
- **Squarespace**. Possible statement text `SQUARESPACE INC`, `SQUARESPACE.COM`. Proposed classification Website builder.
- **Wix**. Possible statement text `WIX.COM`, `WIX*`. Proposed classification Website builder.
- **OpenAI / ChatGPT**. Possible statement text `OPENAI`, `OPENAI LLC`, `OPENAI INC`. Proposed classification AI / software subscription.
- **Anthropic / Claude**. Possible statement text `ANTHROPIC`, `ANTHROPIC PBC`. Proposed classification AI / software subscription.
- **Cursor / Anysphere**. Possible statement text `CURSOR`, `ANYSPHERE INC`. Proposed classification AI dev tools.
- **1Password**. Possible statement text `1PASSWORD`, `AGILEBITS INC`. Proposed classification Password manager.
- **Bitwarden**. Possible statement text `BITWARDEN INC`, `8BIT SOLUTIONS LLC`. Proposed classification Password manager.
- **LastPass**. Possible statement text `LASTPASS`, `LOGMEIN INC`. Proposed classification Password manager.
- **NordVPN**. Possible statement text `NORDVPN`, `NORDSEC LTD`. Proposed classification VPN.
- **Surfshark**. Possible statement text `SURFSHARK`, `SURFSHARK LTD`. Proposed classification VPN.
- **ExpressVPN**. Possible statement text `EXPRESSVPN INC`. Proposed classification VPN.
- **Apple One / iCloud+**. Possible statement text `APPLE COM BILL`, `APPLE.COM/BILL`, `APPLE IRELAND`. Proposed classification Software subscription / personal.
- **Spotify (Business)**. Possible statement text `SPOTIFY USA`, `SPOTIFY AB`. Proposed classification Music streaming.
- **Audible (Business)**. Possible statement text `AUDIBLE.COM`, `AUDIBLE INC`. Proposed classification Audiobook subscription.
- **Xero**. Possible statement text `XERO LTD`, `XERO PTY LTD`, `XERO LIMITED`. Proposed classification Accounting software.
- **QuickBooks Online**. Possible statement text `INTUIT QBKS`, `INTUIT QUICKBOOKS`. Proposed classification Accounting software.
- **FreeAgent**. Possible statement text `FREEAGENT CENTRAL LTD`. Proposed classification Accounting software.
- **Sage**. Possible statement text `SAGE GROUP PLC`, `SAGE SOFTWARE`. Proposed classification Accounting software.
- **Gusto**. Possible statement text `GUSTO INC`. Proposed classification Payroll.
- **Rippling**. Possible statement text `RIPPLING PEOPLE CENTER`, `RIPPLING INC`. Proposed classification HR / payroll.
- **Deel**. Possible statement text `DEEL INC`. Proposed classification Global contractor / payroll.
- **Remote**. Possible statement text `REMOTE TECHNOLOGY`, `REMOTE.COM`. Proposed classification Global EOR / payroll.
- **Wise Business**. Possible statement text `WISE`, `TRANSFERWISE`, `WISE PAYMENTS LTD`. Proposed classification Multi-currency banking.
- **Mercury**. Possible statement text `MERCURY*`, `MERCURY TECHNOLOGIES`. Proposed classification Business banking (US).
- **Brex**. Possible statement text `BREX INC`. Proposed classification Business banking + cards (US).
- **Ramp**. Possible statement text `RAMP BUSINESS CORP`. Proposed classification Business cards + spend mgmt.

## Worked cases

### Mixed-use annual productivity plan

Assume a supplied EUR 300 annual invoice, supported 60% business use, an approved accrual policy and six service months used in the reporting year. The business cost is EUR 180, split EUR 90 current/EUR 90 prepayment; EUR 120 remains personal. The supplier's name does not override that allocation.

```oa-check
name: Productivity plan, supported mixed use
inputs:
  invoice: 300
  business_share: 0.60
  elapsed_months: 6
steps:
  - business_cost: invoice * business_share
  - current_expense: business_cost * elapsed_months / 12
  - prepayment: business_cost - current_expense
  - personal: invoice - business_cost
expected:
  business_cost: 180
  current_expense: 90
  prepayment: 90
  personal: 120
```



## Sources

| Official source | Read on | Read scope |
|---|---|---|
| https://www.gov.uk/self-employed-records/what-records-to-keep | 2026-11-14 | Read for sales/expense proof, accurate records, distinguishing business transactions and accrual records. |
| https://www.gov.uk/expenses-if-youre-self-employed | 2026-11-14 | Read for sole-trader/partner business-purpose allocation, ordinary expenses versus equipment and cash/traditional basis. |
| https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-11-14 | Read for sections 2-6 and 13, actual supply, belonging, reverse-charge conditions, input-tax limits and unregistered recipients. |
| https://standards.aasb.gov.au/sites/default/files/2025-03/AASB 121_08-15_COMPoct23_01-25.pdf | 2026-11-14 | Read for paragraphs 20-23 and 27-30, initial recognition, monetary closing balances and settlement exchange differences; Australian IFRS-equivalent financial reporting, not universal tax translation. |

Not yet confirmed: the current legal billing entity, country, ownership, descriptor availability and VAT/GST assertion formerly attached to each historical candidate below. These old assertions are recorded for comparison only and must not be used to compute or post tax. Official EU legislation could not be reopened during the current EUR-Lex outage; use the selected country's actual official source. No vendor source was used.

- Historical, not usable guidance, **Microsoft 365 / Office 365**: VAT/GST notes: EU B2B reverse charge (Microsoft Ireland Operations)
- Historical, not usable guidance, **Google Workspace**: VAT/GST notes: EU B2B reverse charge
- Historical, not usable guidance, **Slack**: VAT/GST notes: Salesforce subsidiary; EU B2B reverse charge
- Historical, not usable guidance, **Notion**: VAT/GST notes: US supplier
- Historical, not usable guidance, **Linear**: VAT/GST notes: US supplier
- Historical, not usable guidance, **Asana**: VAT/GST notes: US supplier
- Historical, not usable guidance, **Trello**: VAT/GST notes: Atlassian; AU + EU operations
- Historical, not usable guidance, **Jira / Confluence**: VAT/GST notes: Australia HQ; EU B2B reverse charge
- Historical, not usable guidance, **Figma**: VAT/GST notes: US supplier; Adobe acquisition terminated 2023
- Historical, not usable guidance, **Adobe Creative Cloud**: VAT/GST notes: EU B2B reverse charge
- Historical, not usable guidance, **Canva**: VAT/GST notes: Australia supplier
- Historical, not usable guidance, **Dropbox**: VAT/GST notes: US supplier
- Historical, not usable guidance, **Box**: VAT/GST notes: US supplier
- Historical, not usable guidance, **Zoom**: VAT/GST notes: US supplier; EU B2B reverse charge
- Historical, not usable guidance, **Calendly**: VAT/GST notes: US supplier
- Historical, not usable guidance, **HubSpot**: VAT/GST notes: US supplier; Ireland branch for EU
- Historical, not usable guidance, **Salesforce**: VAT/GST notes: EU B2B reverse charge (Ireland)
- Historical, not usable guidance, **Intercom**: VAT/GST notes: US supplier; Ireland EU operations
- Historical, not usable guidance, **Zendesk**: VAT/GST notes: US supplier; Ireland EU operations
- Historical, not usable guidance, **Loom**: VAT/GST notes: Atlassian subsidiary
- Historical, not usable guidance, **Miro**: VAT/GST notes: US supplier
- Historical, not usable guidance, **ClickUp**: VAT/GST notes: US supplier (Mango Technologies)
- Historical, not usable guidance, **Monday.com**: VAT/GST notes: Israel supplier
- Historical, not usable guidance, **Airtable**: VAT/GST notes: US supplier
- Historical, not usable guidance, **Webflow**: VAT/GST notes: US supplier
- Historical, not usable guidance, **Squarespace**: VAT/GST notes: US supplier; Ireland EU
- Historical, not usable guidance, **Wix**: VAT/GST notes: Israel supplier
- Historical, not usable guidance, **OpenAI / ChatGPT**: VAT/GST notes: US supplier; OpenAI Ireland Ltd for EU
- Historical, not usable guidance, **Anthropic / Claude**: VAT/GST notes: US supplier; Anthropic Ireland for EU
- Historical, not usable guidance, **Cursor / Anysphere**: VAT/GST notes: US supplier
- Historical, not usable guidance, **1Password**: VAT/GST notes: Canada supplier
- Historical, not usable guidance, **Bitwarden**: VAT/GST notes: US supplier
- Historical, not usable guidance, **LastPass**: VAT/GST notes: LogMeIn / GoTo
- Historical, not usable guidance, **NordVPN**: VAT/GST notes: Panama HQ; EU operations
- Historical, not usable guidance, **Surfshark**: VAT/GST notes: Netherlands / Nord parent
- Historical, not usable guidance, **ExpressVPN**: VAT/GST notes: BVI HQ
- Historical, not usable guidance, **Apple One / iCloud+**: VAT/GST notes: EU: Apple Distribution International (Ireland)
- Historical, not usable guidance, **Spotify (Business)**: VAT/GST notes: Sweden HQ
- Historical, not usable guidance, **Audible (Business)**: VAT/GST notes: Amazon subsidiary
- Historical, not usable guidance, **Xero**: VAT/GST notes: New Zealand HQ; Australia operations
- Historical, not usable guidance, **QuickBooks Online**: VAT/GST notes: US supplier
- Historical, not usable guidance, **FreeAgent**: VAT/GST notes: UK HQ (RBS subsidiary)
- Historical, not usable guidance, **Sage**: VAT/GST notes: UK HQ
- Historical, not usable guidance, **Gusto**: VAT/GST notes: US supplier
- Historical, not usable guidance, **Rippling**: VAT/GST notes: US supplier
- Historical, not usable guidance, **Deel**: VAT/GST notes: US HQ; entities worldwide
- Historical, not usable guidance, **Remote**: VAT/GST notes: US HQ
- Historical, not usable guidance, **Wise Business**: VAT/GST notes: UK HQ; EMI in EU
- Historical, not usable guidance, **Mercury**: VAT/GST notes: US (Choice Financial backs)
- Historical, not usable guidance, **Brex**: VAT/GST notes: US supplier
- Historical, not usable guidance, **Ramp**: VAT/GST notes: US supplier
