---
name: global-productivity-tools
description: "Pattern library for productivity, collaboration, and creative SaaS tools appearing on bank statements worldwide. Covers Microsoft 365, Google Workspace, Slack, Notion, Linear, Asana, Trello, Jira / Confluence, Figma, Adobe Creative Cloud, Canva, Dropbox, Box, Zoom, Calendly, HubSpot, Salesforce, Intercom, Zendesk, Loom, Miro, ClickUp, Monday.com, Airtable, Webflow, Squarespace, Wix, ChatGPT / OpenAI, Anthropic Claude, Cursor, 1Password, Bitwarden, LastPass, NordVPN, Surfshark, ExpressVPN, Apple One / iCloud+, Spotify (business), Audible (business), and accounting / payroll software (Xero, QuickBooks, FreeAgent, Sage, Gusto, Rippling, Deel, Remote, Wise Business). Provides bank-statement variations, default classification, and VAT/GST notes. Does NOT cover: cloud infrastructure (see global-cloud-infrastructure), ad platforms (see global-ad-platforms), or payment processors (see global-payment-processors)."
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

# Global Productivity Tools

## Global Productivity & SaaS Vendor Patterns v0.1

## Pattern table

**Global Productivity & SaaS Vendor Patterns**  _(Pattern table)_

| Vendor | Bank statement variations | Default category | VAT/GST notes |
| --- | --- | --- | --- |
| **Microsoft 365 / Office 365** | `MICROSOFT*M365`, `MICROSOFT*365`, `MSFT*M365`, `MICROSOFT IRELAND OPS` | Software subscription / productivity | EU B2B reverse charge (Microsoft Ireland Operations) |
| **Google Workspace** | `GOOGLE *G SUITE`, `GOOGLE *WORKSPACE`, `GOOGLE IRELAND LTD` | Software subscription / productivity | EU B2B reverse charge |
| **Slack** | `SLACK TECHNOLOGIES`, `SLACK*` | Communications / SaaS | Salesforce subsidiary; EU B2B reverse charge |
| **Notion** | `NOTION LABS INC`, `NOTION.SO` | Productivity / docs | US supplier |
| **Linear** | `LINEAR ORBIT INC`, `LINEAR.APP` | Project management | US supplier |
| **Asana** | `ASANA INC`, `ASANA.COM` | Project management | US supplier |
| **Trello** | `TRELLO`, `ATLASSIAN` | Project management | Atlassian; AU + EU operations |
| **Jira / Confluence** | `ATLASSIAN`, `ATLASSIAN US`, `ATLASSIAN PTY LTD` | Software development tools | Australia HQ; EU B2B reverse charge |
| **Figma** | `FIGMA INC`, `FIGMA.COM` | Design / collaboration | US supplier; Adobe acquisition terminated 2023 |
| **Adobe Creative Cloud** | `ADOBE *CREATIVE`, `ADOBE IRELAND LTD` | Software subscription / creative | EU B2B reverse charge |
| **Canva** | `CANVA*`, `CANVA PTY LTD` | Design | Australia supplier |
| **Dropbox** | `DROPBOX INC`, `DROPBOX*` | File storage | US supplier |
| **Box** | `BOX INC`, `BOX.COM` | File storage / content management | US supplier |
| **Zoom** | `ZOOM.US`, `ZOOM VIDEO COMMS`, `ZOOM VOICE COMMS` | Video conferencing | US supplier; EU B2B reverse charge |
| **Calendly** | `CALENDLY INC`, `CALENDLY.COM` | Scheduling | US supplier |
| **HubSpot** | `HUBSPOT INC`, `HUBSPOT.COM` | CRM / marketing | US supplier; Ireland branch for EU |
| **Salesforce** | `SALESFORCE.COM`, `SALESFORCE*`, `SALESFORCE EMEA LTD` | CRM | EU B2B reverse charge (Ireland) |
| **Intercom** | `INTERCOM INC`, `INTERCOM.COM` | Customer messaging | US supplier; Ireland EU operations |
| **Zendesk** | `ZENDESK INC`, `ZENDESK.COM` | Customer support | US supplier; Ireland EU operations |
| **Loom** | `LOOM INC`, `LOOM.COM` | Video messaging | Atlassian subsidiary |
| **Miro** | `MIRO INC`, `RTBI INC` | Whiteboarding | US supplier |
| **ClickUp** | `CLICKUP`, `MANGO TECHNOLOGIES` | Project management | US supplier (Mango Technologies) |
| **Monday.com** | `MONDAY.COM`, `MONDAY.COM LTD` | Project management | Israel supplier |
| **Airtable** | `AIRTABLE INC`, `AIRTABLE.COM` | Database / collaboration | US supplier |
| **Webflow** | `WEBFLOW INC`, `WEBFLOW.COM` | Website builder | US supplier |
| **Squarespace** | `SQUARESPACE INC`, `SQUARESPACE.COM` | Website builder | US supplier; Ireland EU |
| **Wix** | `WIX.COM`, `WIX*` | Website builder | Israel supplier |
| **OpenAI / ChatGPT** | `OPENAI`, `OPENAI LLC`, `OPENAI INC` | AI / software subscription | US supplier; OpenAI Ireland Ltd for EU |
| **Anthropic / Claude** | `ANTHROPIC`, `ANTHROPIC PBC` | AI / software subscription | US supplier; Anthropic Ireland for EU |
| **Cursor / Anysphere** | `CURSOR`, `ANYSPHERE INC` | AI dev tools | US supplier |
| **1Password** | `1PASSWORD`, `AGILEBITS INC` | Password manager | Canada supplier |
| **Bitwarden** | `BITWARDEN INC`, `8BIT SOLUTIONS LLC` | Password manager | US supplier |
| **LastPass** | `LASTPASS`, `LOGMEIN INC` | Password manager | LogMeIn / GoTo |
| **NordVPN** | `NORDVPN`, `NORDSEC LTD` | VPN | Panama HQ; EU operations |
| **Surfshark** | `SURFSHARK`, `SURFSHARK LTD` | VPN | Netherlands / Nord parent |
| **ExpressVPN** | `EXPRESSVPN INC` | VPN | BVI HQ |
| **Apple One / iCloud+** | `APPLE COM BILL`, `APPLE.COM/BILL`, `APPLE IRELAND` | Software subscription / personal | EU: Apple Distribution International (Ireland) |
| **Spotify (Business)** | `SPOTIFY USA`, `SPOTIFY AB` | Music streaming | Sweden HQ |
| **Audible (Business)** | `AUDIBLE.COM`, `AUDIBLE INC` | Audiobook subscription | Amazon subsidiary |
| **Xero** | `XERO LTD`, `XERO PTY LTD`, `XERO LIMITED` | Accounting software | New Zealand HQ; Australia operations |
| **QuickBooks Online** | `INTUIT QBKS`, `INTUIT QUICKBOOKS` | Accounting software | US supplier |
| **FreeAgent** | `FREEAGENT CENTRAL LTD` | Accounting software | UK HQ (RBS subsidiary) |
| **Sage** | `SAGE GROUP PLC`, `SAGE SOFTWARE` | Accounting software | UK HQ |
| **Gusto** | `GUSTO INC` | Payroll | US supplier |
| **Rippling** | `RIPPLING PEOPLE CENTER`, `RIPPLING INC` | HR / payroll | US supplier |
| **Deel** | `DEEL INC` | Global contractor / payroll | US HQ; entities worldwide |
| **Remote** | `REMOTE TECHNOLOGY`, `REMOTE.COM` | Global EOR / payroll | US HQ |
| **Wise Business** | `WISE`, `TRANSFERWISE`, `WISE PAYMENTS LTD` | Multi-currency banking | UK HQ; EMI in EU |
| **Mercury** | `MERCURY*`, `MERCURY TECHNOLOGIES` | Business banking (US) | US (Choice Financial backs) |
| **Brex** | `BREX INC` | Business banking + cards (US) | US supplier |
| **Ramp** | `RAMP BUSINESS CORP` | Business cards + spend mgmt | US supplier |

## Default classification rules

- **Software subscription classification** — Schedule C Line 22 (Supplies) for small annual; Line 25 (Utilities) commonly used; Line 27a (Other expenses) with description  _(Default classification rules)_
- **Personal vs business allocation** — confirm with the user; if mixed, allocate by usage percentage  _(Default classification rules)_

## VAT mechanics

Same as `global-cloud-infrastructure.md` Section "Cross-border VAT mechanics".

## Personal-vs-business detection

Many of these vendors have both personal and business tiers. Flag the following for user confirmation:
- Single-user Notion, Linear, Figma, Loom subscriptions
- Apple One, iCloud+ family plans
- Spotify (likely personal)
- Audible (often personal)
- Wix, Squarespace personal portfolio sites

## Self-checks

- [ ] Vendor identified
- [ ] Business vs personal use confirmed
- [ ] EU/UK B2B reverse charge applied where supplier non-resident
- [ ] Recurring billing reflected in monthly accruals

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
