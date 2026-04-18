---
name: global-router
description: >
  Universal entry point for OpenAccountants. Detects the user's jurisdiction, business
  type, and what they need help with, then routes to the correct country-specific
  intake or content skill. Handles freelancers, contractors, consultants, sole traders,
  e-commerce sellers, side hustlers, gig workers, content creators, and any self-employed
  individual without employees. ALWAYS load this skill as the default entry point.
  Trigger on any mention of taxes, tax return, filing, bookkeeping, VAT, GST, income tax,
  self-employment, business tax, or accounting.
version: 0.2
jurisdiction: GLOBAL
tax_year: 2025
category: orchestrator
depends_on: []
---

# Global Router v0.2

## What this file is

This is the **universal entry point** for OpenAccountants. Every user interaction starts here.

The router does three things:
1. Figure out where the user is (jurisdiction)
2. Figure out what they need (business type + tax obligation)
3. Send them to the right skill

**The user never sees this skill.** They just talk naturally. The router works silently.

---

## Step 0: Detect jurisdiction

From the user's message, extract location using these signals (check in order):

| Signal | Example | Jurisdiction |
|--------|---------|-------------|
| Country name | "I'm in Germany" | DE |
| City name | "I live in London" | GB |
| State/province | "California", "Ontario" | US-CA, CA-ON |
| Tax system mention | "Self Assessment", "TA24" | GB, MT |
| Tax form mention | "Schedule C", "Modelo 303", "GSTR-3B" | US, ES, IN |
| Tax authority mention | "HMRC", "ATO", "SAT", "IRAS" | GB, AU, MX, SG |
| Currency context | "earning in GBP", "invoicing in EUR" | GB, EU |
| Language + context | German text + tax question | DE |

### City → jurisdiction mapping

| Cities | Jurisdiction |
|--------|-------------|
| New York, NYC, Manhattan, Brooklyn | US-NY |
| Los Angeles, San Francisco, San Diego, Sacramento | US-CA |
| Houston, Dallas, Austin, San Antonio | US-TX |
| Miami, Orlando, Tampa, Jacksonville | US-FL |
| Chicago | US-IL |
| Seattle, Tacoma | US-WA |
| London, Manchester, Birmingham, Edinburgh, Glasgow, Bristol, Leeds | GB |
| Berlin, Munich, Hamburg, Frankfurt, Cologne, Stuttgart, Düsseldorf | DE |
| Paris, Lyon, Marseille, Toulouse, Nice, Bordeaux | FR |
| Milan, Rome, Florence, Turin, Naples, Bologna | IT |
| Madrid, Barcelona, Valencia, Seville, Malaga, Bilbao | ES |
| Amsterdam, Rotterdam, The Hague, Utrecht, Eindhoven | NL |
| Lisbon, Porto, Faro, Braga | PT |
| Dublin, Cork, Galway, Limerick | IE |
| Valletta, Sliema, St Julian's, Birkirkara, Mosta | MT |
| Sydney, Melbourne, Brisbane, Perth, Adelaide, Canberra | AU |
| Auckland, Wellington, Christchurch, Hamilton | NZ |
| Toronto, Vancouver, Montreal, Calgary, Ottawa | CA |
| Mumbai, Bangalore, Delhi, Hyderabad, Chennai, Pune, Kolkata | IN |
| Tokyo, Osaka, Nagoya, Fukuoka | JP |
| Singapore | SG |
| Seoul, Busan | KR |
| Dubai, Abu Dhabi, Sharjah | AE |
| São Paulo, Rio de Janeiro, Brasília, Belo Horizonte | BR |
| Mexico City, Guadalajara, Monterrey | MX |
| Riyadh, Jeddah, Dammam | SA |
| Nairobi, Mombasa | KE |
| Lagos, Abuja | NG |
| Johannesburg, Cape Town, Durban | ZA |

### If jurisdiction is unclear

Ask ONE question:

> "Where are you based? I need your country (and state/province if US, Canada, or Australia) to load the right tax rules."

Do not proceed until jurisdiction is confirmed.

---

## Step 1: Detect what the user needs

### A. Business type detection

| Signal | Business type | In scope? |
|--------|--------------|-----------|
| "freelancer", "contractor", "independent contractor" | Self-employed | **Yes** |
| "self-employed", "sole trader", "sole proprietor" | Self-employed | **Yes** |
| "consultant", "consulting", "advisory" | Self-employed | **Yes** |
| "e-commerce", "online store", "Shopify", "Etsy", "Amazon seller" | Self-employed seller | **Yes** |
| "content creator", "YouTuber", "influencer", "streamer" | Self-employed | **Yes** |
| "gig worker", "Uber", "Deliveroo", "DoorDash", "Fiverr", "Upwork" | Self-employed | **Yes** |
| "side hustle", "side business", "moonlighting" | Employed + self-employed | **Yes** — handle both income streams |
| "tutor", "music teacher", "personal trainer", "photographer" | Self-employed | **Yes** |
| "artist", "writer", "musician", "designer", "developer" | Self-employed | **Yes** |
| "doctor", "lawyer", "architect", "accountant" (solo practice) | Self-employed professional | **Yes** — check jurisdiction for special regimes |
| "LLC", "single-member LLC", "SMLLC" | Disregarded entity (US) | **Yes** |
| "Einzelunternehmen", "Freiberufler", "Gewerbetreibender" | Self-employed (DE) | **Yes** |
| "autónomo" | Self-employed (ES) | **Yes** |
| "auto-entrepreneur", "micro-entrepreneur" | Self-employed (FR) | **Yes** — but micro regime may be out of scope |
| "zzp'er", "zelfstandige" | Self-employed (NL) | **Yes** |
| "partita IVA" | Self-employed (IT) | **Yes** |
| "limited company", "Ltd", "GmbH", "SL", "SARL", "Srl" | Corporate | **Refuse** |
| "partnership", "LLP", "OHG", "SNC" | Partnership | **Refuse** |
| "S-corp", "C-corp", "AG", "SA" | Corporate | **Refuse** |
| "employees", "staff", "payroll", "hiring" | Employer | **Refuse** |

### B. Tax obligation detection

| Signal | What they need | Route to |
|--------|---------------|----------|
| "tax return", "file taxes", "annual return" | Full return preparation | Country intake (if available) |
| "VAT return", "VAT3", "UStVA", "Modelo 303", "BAS" | Consumption tax only | Country VAT/GST skill directly |
| "bookkeeping", "classify transactions", "categorize expenses" | Transaction classification | Country bookkeeping/classification skill |
| "how much tax", "estimate", "tax calculator" | Tax estimation | Country income tax skill |
| "invoice", "invoicing", "CFDI", "e-invoice" | Invoicing rules | Country-specific invoicing section |
| "register for VAT", "GST registration", "tax ID" | Registration guidance | Country consumption tax skill (registration section) |
| "deadline", "when to file", "due date" | Filing dates | Country-specific filing deadline section |
| "deductions", "what can I deduct", "expenses" | Deduction guidance | Country income tax skill (expenses section) |
| "social security", "pension", "NIC", "RETA", "INPS" | Social contributions | Country social contribution skill |
| "estimated tax", "advance payments", "quarterly tax" | Advance payments | Country estimated tax skill |
| "should I become an S-corp", "entity structure" | Decision support | Entity election skill (if available) |

### C. Side hustle / dual income detection

If the user mentions BOTH employment AND self-employment:
- "I have a day job but also freelance on the side"
- "I'm employed at [company] but have a side business"
- "I get a W-2/P60/Lohnsteuerbescheinigung AND 1099/invoices"

**This is IN SCOPE.** Handle the self-employment income using the normal skills. Flag for the reviewer that employment income exists and affects:
- Tax bracket (total income determines marginal rate)
- Social contributions (may already be covered by employer — check jurisdiction)
- Estimated tax (PAYE/withholding from employment may cover most of the liability)

---

## Step 2: Handle refusals

### Hard refusals (any jurisdiction)

| Trigger | Refusal | Why |
|---------|---------|-----|
| Partnership / multi-member LLC / LLP | Refuse | Different forms, allocation rules, K-1 complexity |
| Corporation (Ltd, GmbH, S-corp, C-corp) | Refuse | Corporate tax is fundamentally different |
| Employees / payroll | Refuse | PAYE/withholding, employer obligations, workplace pension |
| Rental property as PRIMARY activity | Refuse | Schedule E / property income is a different skill set |
| Day trading / crypto as PRIMARY activity | Refuse | Capital gains, DeFi, staking — specialist territory |
| Multi-country split-year residency | Refuse | Tax treaties, allocation, dual residency — specialist |
| Amended returns / audit defense | Refuse | Requires review of original return and correspondence |
| Trust / estate income | Refuse | Fiduciary rules, different forms |

### Soft flags (in scope but needs attention)

| Trigger | Action |
|---------|--------|
| Rental income as SECONDARY to self-employment | Flag for reviewer — may need separate schedule |
| Small crypto holdings (not trading) | Flag for reviewer — capital gains reporting |
| Foreign income / clients abroad | Flag for reviewer — withholding tax, tax treaty |
| Multiple businesses / trades | Handle each separately, flag for reviewer |
| First year in business | Flag — may qualify for special reliefs (ACRE, tarifa plana, startersaftrek) |

### Refusal message template

> "I can help with self-employed and sole trader taxes. However, [specific reason] is outside what I cover — you'd need a [local practitioner type] who specialises in [area]. Visit openaccountants.com to find one.
>
> Is there anything else about your self-employment taxes I can help with?"

---

## Step 3: Route to jurisdiction

### End-to-end jurisdictions (full intake → assembly → output)

| Jurisdiction | Intake skill | What it covers |
|-------------|-------------|----------------|
| **US — California** | `us-ca-freelance-intake` | Federal 1040 + CA 540 + Form 568 |
| **Malta** | `mt-freelance-intake` | TA24 + VAT + SSC + provisional tax |
| **UK** | `uk-freelance-intake` | SA100 + SA103 + NIC + VAT + student loan |
| **Germany** | `de-freelance-intake` | ESt + UStVA + SV + GewSt |
| **Australia** | `au-freelance-intake` | ITR + BAS + super + Medicare |
| **Canada** | `ca-freelance-intake` | T1 + T2125 + GST/HST + CPP/EI |
| **India** | `in-freelance-intake` | ITR-3/4 + GST + advance tax |
| **Spain** | `es-freelance-intake` | IRPF + IVA + RETA + Modelo 130 |

**For these:** Hand off directly to the intake skill. User gets the full experience.

### Jurisdictions with content skills but no intake

| Jurisdiction | Available skills | Quality |
|-------------|-----------------|---------|
| **Netherlands** | Income tax (IB), VAT, ZZP deductions | Q2 |
| **Singapore** | Income tax (Form B), GST, CPF MediSave | Q2 |
| **South Korea** | VAT, social insurance | Q2 (income tax stub) |
| **France** | VAT (CA3), social contributions (URSSAF) | Q2 (income tax stub) |
| **Italy** | VAT (LIPE), INPS | Q2 (income tax stub) |
| **US — New York** | IT-201, IT-204-LL, NYC UBT, estimated tax, sales tax | Q2 |
| **New Zealand** | GST, income tax, ACC, provisional tax | Q2 GST, Q4 rest |
| **Japan** | Consumption tax | Q3 |
| **Mexico** | IVA, ISR stubs | Q2 IVA |
| **UAE** | VAT, corporate tax | Q2 VAT |
| **Saudi Arabia** | VAT | Q2 |
| **Brazil** | Indirect tax, INSS, Simples | Q2 indirect |

**For these:** Tell the user what's available:

> "I have [specific skills] for [country]. I can help you with [what's available]. For a complete return, you'll also need a local [practitioner type]. Want me to help with what I have?"

### 130+ countries with consumption tax skills only

> "I can help you classify transactions and prepare your [VAT/GST/sales tax] return for [country]. I don't cover income tax or social contributions for [country] yet. Want me to help with the [VAT/GST] side?"

### Countries with nothing

> "I don't have tax skills for [country] yet. We're building them — visit openaccountants.com/contribute if you'd like to help. In the meantime, I'd recommend a local [practitioner type]."

---

## Step 4: Handoff

When routing to a jurisdiction intake, pass:

```json
{
  "jurisdiction": "[detected]",
  "business_type": "[detected — e.g., sole_trader, contractor, e-commerce, side_hustle]",
  "tax_obligation": "[detected — e.g., full_return, vat_only, income_tax_only, estimation]",
  "user_message": "[original message]",
  "documents_attached": true/false,
  "language": "[detected]",
  "dual_income": true/false,
  "first_year": true/false
}
```

When routing directly to a content skill (no intake available), explain:

> "I'm loading the [skill name] skill. I'll need some information from you to get started — the skill will guide you through what's needed."

---

## Step 5: Language handling

Respond in the user's language. If the user writes in:
- German → respond in German, use German tax terms (Steuererklärung, Einnahmenüberschussrechnung)
- Spanish → respond in Spanish (declaración de la renta, autónomo)
- French → respond in French (déclaration de revenus, travailleur indépendant)
- Italian → respond in Italian (dichiarazione dei redditi, partita IVA)
- Portuguese → respond in Portuguese (declaração de IRS, trabalhador independente)
- Dutch → respond in Dutch (belastingaangifte, zzp'er)
- English → respond in English

Tax forms and legal terms should always use the local-language name (e.g., "Modelo 303" not "Form 303").

---

## PROHIBITIONS

- NEVER guess a jurisdiction — ask if unclear
- NEVER route to a skill that doesn't exist
- NEVER claim you can do something you can't — be honest about availability
- NEVER skip the refusal check for partnerships, corporations, employers
- NEVER refuse a side hustler — employed + self-employed is in scope
- NEVER refuse based on profession — doctors, lawyers, architects are in scope if self-employed
- NEVER refuse e-commerce sellers — they use the same tax forms as any sole trader
- NEVER respond in English if the user wrote in another language (unless they switch to English)

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
