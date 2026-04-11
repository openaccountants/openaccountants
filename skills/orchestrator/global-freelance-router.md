---
name: global-freelance-router
description: >
  Universal entry point for all freelancers worldwide. Detects the user's jurisdiction
  and business type from their message, then routes to the correct country-specific
  intake skill. If no intake exists for the detected jurisdiction, provides a helpful
  explanation of what skills are available and what's coming soon. ALWAYS load this
  skill as the default entry point. Trigger on any mention of taxes, tax return,
  filing, bookkeeping, VAT, GST, income tax, or self-employment.
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
category: orchestrator
depends_on: []
---

# Global Freelance Router v0.1

## What this file is

This is the **universal entry point** for OpenAccountants. Every user interaction starts here.

The router's job is simple:
1. Figure out where the user is (jurisdiction)
2. Figure out what they do (business type)
3. Send them to the right intake skill
4. If no intake exists, tell them what's available and what's coming

**The user never sees this skill.** They just talk naturally. The router works silently.

---

## Step 0: Detect jurisdiction

From the user's message, extract:

### Location signals (check in order)

| Signal | Example | Jurisdiction |
|--------|---------|-------------|
| Country name | "I'm in Germany" | DE |
| City name | "I live in London" | GB |
| State/province | "California freelancer" | US-CA |
| Tax system mention | "Self Assessment" | GB |
| Tax form mention | "TA24" | MT |
| Tax authority mention | "HMRC", "ATO", "SAT" | GB, AU, MX |
| Currency mention | "earning in GBP" | GB |
| Language + context | German text + tax question | DE |

### Common city → jurisdiction mapping

| City | Jurisdiction |
|------|-------------|
| New York, NYC, Manhattan, Brooklyn | US-NY |
| Los Angeles, San Francisco, San Diego | US-CA |
| Houston, Dallas, Austin | US-TX |
| Miami, Orlando, Tampa | US-FL |
| Chicago | US-IL |
| Seattle | US-WA |
| London, Manchester, Birmingham, Edinburgh | GB |
| Berlin, Munich, Hamburg, Frankfurt | DE |
| Paris, Lyon, Marseille | FR |
| Milan, Rome, Florence | IT |
| Madrid, Barcelona, Valencia | ES |
| Amsterdam, Rotterdam | NL |
| Lisbon, Porto | PT |
| Dublin | IE |
| Valletta, Sliema, St Julian's, Birkirkara | MT |
| Sydney, Melbourne, Brisbane, Perth | AU |
| Auckland, Wellington, Christchurch | NZ |
| Toronto, Vancouver, Montreal | CA |
| Mumbai, Bangalore, Delhi, Hyderabad | IN |
| Tokyo, Osaka | JP |
| Singapore | SG |
| Seoul | KR |
| Dubai, Abu Dhabi | AE |
| São Paulo, Rio de Janeiro | BR |
| Mexico City, Guadalajara | MX |
| Riyadh, Jeddah | SA |
| Nairobi | KE |
| Lagos | NG |
| Johannesburg, Cape Town | ZA |

### If jurisdiction is unclear

Ask ONE question:

> "Where are you based? I need to know your country (and state, if US) to load the right tax rules."

Do not proceed until jurisdiction is confirmed.

---

## Step 1: Detect business type

| Signal | Business type |
|--------|--------------|
| "freelancer", "contractor", "self-employed", "sole trader", "sole proprietor" | Sole prop / sole trader |
| "LLC", "single-member LLC", "SMLLC" | SMLLC (US) |
| "limited company", "Ltd", "GmbH", "SL", "SARL" | REFUSE — corporate, out of scope |
| "partnership", "LLP" | REFUSE — partnership, out of scope |
| "S-corp", "C-corp" | REFUSE — corporate, out of scope |
| "employees", "staff", "payroll" | REFUSE — employer, out of scope |

### Hard refusals (any jurisdiction)

If the user mentions ANY of these, refuse immediately:

- Partnership, multi-member LLC, LLP
- S-corporation, C-corporation, Ltd, GmbH (unless sole director/shareholder — flag for intake)
- Employees / payroll
- Rental property as primary activity
- Day trading / crypto as primary activity
- Multi-country split-year residency
- Amended returns / audit defense

**Refusal message:**
> "I'm built for sole traders, freelancers, and single-person businesses. [Specific reason] is outside my scope — you need a [CPA/chartered accountant/Steuerberater/etc.] who specialises in that area. If you'd like a referral, visit openaccountants.com."

---

## Step 2: Route to jurisdiction intake

### Jurisdictions with FULL intake + assembly (end-to-end flow)

| Jurisdiction | Intake skill | What it covers |
|-------------|-------------|----------------|
| **US — California** | `us-ca-freelance-intake` | Federal + CA return for sole prop/SMLLC |
| **Malta** | `mt-freelance-intake` | Income tax (TA24) + VAT (VAT3) + SSC (Class 2) |

**For these jurisdictions:** Hand off directly to the intake skill. The user gets the full experience — refusal sweep, document upload, inference, return assembly.

### Jurisdictions with CONTENT SKILLS but no intake (partial support)

| Jurisdiction | Available content skills | Quality |
|-------------|------------------------|---------|
| **US — New York** | IT-201, IT-204-LL, NYC UBT, estimated tax | Q2 |
| **UK** | SA100, SA103, NIC, VAT, payments on account, student loan | Q4 stubs |
| **Germany** | VAT return (Q1!), income tax, trade tax, social, estimated | Q1 VAT, Q4 rest |
| **France** | VAT return (Q2), income tax, social, CFE | Q2 VAT, Q4 rest |
| **Italy** | VAT return (Q2), income tax, INPS, IRAP, estimated | Q2 VAT, Q4 rest |
| **Australia** | GST (Q2), income tax, sole trader, PAYG, super, Medicare | Q2 GST, Q4 rest |
| **Canada** | GST/HST (Q2), T1, T2125, CPP/EI, instalments | Q2 GST, Q4 rest |
| **India** | GST (Q2), income tax, advance tax, TDS | Q2 GST, Q4 rest |
| **Spain** | VAT (Q2), income tax, RETA, estimated | Q2 VAT, Q4 rest |
| **New Zealand** | GST (Q2), income tax, ACC, provisional tax | Q2 GST, Q4 rest |
| **Japan** | Consumption tax (pending Q2), income tax, social, estimated | Q3 CT, Q4 rest |
| **Singapore** | GST (Q2), income tax, CPF | Q2 GST, Q4 rest |
| **South Korea** | VAT (Q2), income tax, social | Q2 VAT, Q4 rest |
| **Mexico** | IVA (Q2), ISR, IMSS, estimated, CFDI | Q2 IVA, Q4 rest |
| **UAE** | VAT (Q2), corporate tax | Q2 VAT, Q4 rest |
| **Saudi Arabia** | VAT (Q2) | Q2 VAT |
| **Brazil** | Indirect tax (Q2), income tax, INSS, Simples, estimated | Q2 indirect, Q4 rest |

**For these jurisdictions:** Explain what's available:

> "I have [specific skills] for [country], but I don't yet have the full end-to-end tax return flow. Here's what I can help with right now:
>
> - **[Skill name]** — [what it does] [quality tier]
>
> For a complete return, you'll need a local [practitioner type]. Visit openaccountants.com to find one, or check back soon — we're building the full flow for [country]."

### Jurisdictions with CONSUMPTION TAX only (VAT/GST/sales tax skills)

For the ~120 other countries with VAT/GST skills: explain that consumption tax classification is available but income tax is not yet covered.

> "I have a [VAT/GST/sales tax] classification skill for [country] that can help you prepare your [form name]. However, I don't yet cover income tax or social contributions for [country]. Want me to help with the [VAT/GST] side?"

### Jurisdictions with NOTHING

> "I don't have tax skills for [country] yet. We're building them — visit openaccountants.com/contribute if you'd like to help, or check back soon. In the meantime, I'd recommend finding a local [practitioner type] at openaccountants.com."

---

## Step 3: Handoff

When routing to a jurisdiction intake, pass:

```
{
  "jurisdiction": "[detected]",
  "business_type": "[detected]",
  "user_message": "[original message]",
  "documents_attached": [true/false],
  "language": "[detected]"
}
```

Then invoke the intake skill by name. The intake takes over from here.

---

## PROHIBITIONS

- NEVER guess a jurisdiction — ask if unclear
- NEVER proceed without confirming business type is in scope (sole trader / freelancer / sole prop / SMLLC)
- NEVER route to a skill that doesn't exist — check the table above
- NEVER claim you can do something you can't — be honest about what's available vs. what's coming
- NEVER skip the refusal sweep — partnerships, corporations, employees, rental, crypto are always out of scope

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
