---
name: global-router
description: "Universal entry point for OpenAccountants — the open-source accounting skill set covering 10 domains: tax, bookkeeping, e-invoicing, payroll, company formation, financial statements, transfer pricing, tax optimization, cross-border, and platform integrations. Detects the user's jurisdiction, business type, and domain, then routes to the correct country-specific skills. Handles freelancers, contractors, consultants, sole traders, e-commerce sellers, side hustlers, gig workers, content creators, landlords, small companies, employers, and any self-employed individual. ALWAYS load this skill as the default entry point. Trigger on any mention of: taxes, tax return, filing, payroll, payslip, salary, company formation, incorporate, register a business, annual accounts, financial statements, transfer pricing, tax optimization, save tax, e-invoicing, CFDI, FatturaPA, KSeF, Peppol, bookkeeping, chart of accounts, P&L, balance sheet, cross-border, two countries, moved abroad, Stripe, Xero, QuickBooks, VAT, GST, income tax, self-employment, business tax, or accounting."
version: 1.0
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: []
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Global Router

## Global Router v1.0

## What this file is

This is the **universal entry point** for OpenAccountants. Every user interaction starts here.

The router does five things:
1. Figure out where the user is (jurisdiction)
2. Figure out what they need (domain + business type)
3. Check refusal rules (narrow — most things are in scope now)
4. Route to the right skill(s) for their jurisdiction and domain
5. Hand off with structured context

**The user never sees this skill.** They just talk naturally. The router works silently.

## Step 0: Detect jurisdiction

**Jurisdiction detection signals**

| Signal | Example | Jurisdiction |
| --- | --- | --- |
| Country name | "I'm in Germany" | DE |
| City name | "I live in London" | GB |
| State/province | "California", "Ontario" | US-CA, CA-ON |
| Tax system mention | "Self Assessment", "TA24" | GB, MT |
| Tax form mention | "Schedule C", "Modelo 303", "GSTR-3B" | US, ES, IN |
| Tax authority mention | "HMRC", "ATO", "SAT", "IRAS" | GB, AU, MX, SG |
| Currency context | "earning in GBP", "invoicing in EUR" | GB, EU |
| Language + context | German text + tax question | DE |

### City → jurisdiction mapping

**City to jurisdiction mapping**

| Cities | Jurisdiction |
| --- | --- |
| New York, NYC, Manhattan, Brooklyn, Queens, Bronx | US-NY |
| Los Angeles, San Francisco, San Diego, Sacramento, San Jose | US-CA |
| Houston, Dallas, Austin, San Antonio, Fort Worth | US-TX |
| Miami, Orlando, Tampa, Jacksonville, Fort Lauderdale | US-FL |
| Chicago, Springfield IL, Naperville | US-IL |
| Seattle, Tacoma, Bellevue, Spokane | US-WA |
| Philadelphia, Pittsburgh, Allentown | US-PA |
| Phoenix, Tucson, Scottsdale, Mesa | US-AZ |
| Atlanta, Savannah, Augusta | US-GA |
| Denver, Colorado Springs, Boulder | US-CO |
| Boston, Cambridge, Worcester | US-MA |
| Detroit, Grand Rapids, Ann Arbor | US-MI |
| Minneapolis, St. Paul, Rochester MN | US-MN |
| Portland OR, Eugene, Salem OR | US-OR |
| Las Vegas, Reno, Henderson | US-NV |
| Nashville, Memphis, Knoxville, Chattanooga | US-TN |
| Charlotte, Raleigh, Durham, Asheville | US-NC |
| Columbus OH, Cleveland, Cincinnati | US-OH |
| Indianapolis, Fort Wayne | US-IN |
| Baltimore, Annapolis, Bethesda | US-MD |
| Washington DC, Georgetown, Arlington VA | US-DC |
| Salt Lake City, Provo, Park City | US-UT |
| Richmond, Virginia Beach, Norfolk | US-VA |
| New Orleans, Baton Rouge | US-LA |
| Kansas City MO, St. Louis | US-MO |
| Milwaukee, Madison WI | US-WI |
| Honolulu, Maui | US-HI |
| Anchorage, Fairbanks, Juneau | US-AK |
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

- **Unclear jurisdiction handling** — Ask ONE question: "Where are you based? I need your country (and state/province if US, Canada, or Australia) to load the right rules." Do not proceed until jurisdiction is confirmed.

## Step 1: Detect what the user needs

### A. Domain detection

**Domain detection signals**

| Signal | Domain | Route to |
| --- | --- | --- |
| "tax return", "file taxes", "income tax", "VAT", "GST", "annual return", "estimated tax", "deductions" | **Tax** | Country tax skills |
| "bookkeeping", "classify transactions", "chart of accounts", "P&L", "balance sheet", "trial balance", "categorize expenses", "reconcile" | **Bookkeeping** | Country bookkeeping skill + `bookkeeping-workflow-base` |
| "invoice", "e-invoice", "CFDI", "FatturaPA", "KSeF", "Peppol", "invoice compliance", "LIPE", "SII", "MyInvois" | **E-invoicing** | Country einvoice skill + `einvoice-workflow-base` |
| "payroll", "payslip", "salary", "wages", "PAYE", "withholding", "employer", "hire", "employee", "staff", "NIC employer" | **Payroll** | Country payroll skill + `payroll-workflow-base` |
| "set up a company", "register a business", "incorporate", "LLC", "Ltd", "GmbH", "formation", "articles of association" | **Company formation** | Country formation skill + `company-formation-workflow-base` |
| "annual accounts", "financial statements", "year-end", "balance sheet filing", "Companies House", "statutory accounts" | **Financial statements** | Country financial-statements skill + `financial-statements-workflow-base` |
| "transfer pricing", "intercompany", "arm's length", "CbCR", "related party", "TP documentation" | **Transfer pricing** | Country transfer-pricing skill + `transfer-pricing-workflow-base` |
| "save tax", "reduce tax", "optimize", "deductions I'm missing", "tax planning", "restructure" | **Tax optimization** | Country tax-optimization skill |
| "two countries", "cross-border", "moved abroad", "foreign clients", "treaty", "relocated", "digital nomad" | **Cross-border** | `cross-border-workflow-base` + relevant country skills |
| "crypto", "bitcoin", "ethereum", "staking", "mining", "NFT", "DeFi", "airdrop", "token", "Coinbase", "Binance", "Form 8949", "digital assets" | **Crypto tax** | Country crypto-tax skill + `crypto-tax-workflow-base` |
| "Stripe export", "Xero", "QuickBooks", "PayPal download", "bank CSV", "Wise", "Revolut", "Shopify", "FreeAgent", "Sage" | **Platform integration** | Relevant integration skill from `_integrations/` |

### B. Business type detection

**Business type detection signals**

| Signal | Business type | In scope? |
| --- | --- | --- |
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
| "auto-entrepreneur", "micro-entrepreneur" | Self-employed (FR) | **Yes** |
| "zzp'er", "zelfstandige" | Self-employed (NL) | **Yes** |
| "partita IVA" | Self-employed (IT) | **Yes** |
| "landlord", "rental property", "property investor" | Property investor | **Yes** — route to `property-investor` vertical |
| "employees", "staff", "payroll", "hiring" | Employer | **Yes** — route to payroll skills |
| "limited company", "Ltd", "GmbH", "SL", "SARL", "Srl" | Small company | **Yes** for formation, bookkeeping, financial statements, payroll, e-invoicing. **Refuse** only for corporate tax returns |
| "partnership", "LLP", "OHG", "SNC" | Partnership | **Refuse** for partnership tax returns. **Yes** for formation advice, bookkeeping, payroll |
| "S-corp", "C-corp", "AG", "SA" | Corporate | **Refuse** for corporate tax returns |
| "I'm a developer", "software engineer" | Industry vertical | **Yes** — load `freelance-developer` vertical |
| "e-commerce", "online shop" | Industry vertical | **Yes** — load `ecommerce-seller` vertical |
| "content creator", "YouTuber", "influencer" | Industry vertical | **Yes** — load `content-creator` vertical |
| "doctor", "medical", "healthcare practice" | Industry vertical | **Yes** — load `medical-professional` vertical |
| "consultant", "advisory", "professional services" | Industry vertical | **Yes** — load `consultant-professional` vertical |

### C. Multi-domain detection

**Multi-domain detection signals**

| User says | Domains to load |
| --- | --- |
| "I want to start a business" | Formation + bookkeeping + tax overview |
| "I have employees" / "I'm hiring" | Payroll + bookkeeping |
| "End of year" / "year-end" | Financial statements + tax + bookkeeping |
| "I invoice clients in other countries" | E-invoicing + cross-border VAT |
| "How do I pay less tax?" / "tax planning" | Tax optimization + relevant country tax skill |
| "I moved abroad" / "I live in X but work for Y" | Cross-border + tax skills for both countries |
| "I need to set up payroll for my new company" | Formation + payroll |
| "Annual accounts and tax return" | Financial statements + tax |
| "I sell on Shopify to customers in the EU" | E-invoicing + cross-border VAT + `ecommerce-seller` vertical + `shopify-integration` |
| "I have crypto / Bitcoin / staking rewards" | Crypto tax + country tax skill (gains affect total income) |
| "I mine crypto as a side business" | Crypto tax + bookkeeping + tax (business income) |

### D. Side hustle / dual income detection

- **Dual income handling** — If the user mentions BOTH employment AND self-employment: "I have a day job but also freelance on the side"; "I'm employed at [company] but have a side business"; "I get a W-2/P60/Lohnsteuerbescheinigung AND 1099/invoices". **This is IN SCOPE.** Handle the self-employment income using the normal skills. Flag for the reviewer that employment income exists and affects: Tax bracket (total income determines marginal rate); Social contributions (may already be covered by employer — check jurisdiction); Estimated tax (PAYE/withholding from employment may cover most of the liability).

## Step 2: Handle refusals

### Hard refusals (any jurisdiction)

**Hard refusals table**

| Trigger | Refusal | Why |
| --- | --- | --- |
| Partnership TAX RETURNS (multi-member LLC, LLP) | Refuse | Different forms, allocation rules, K-1 complexity |
| Corporate TAX RETURNS (Ltd, GmbH, S-corp, C-corp) | Refuse | Corporate tax is fundamentally different |
| Large corporate groups with complex structures | Refuse | Consolidation, group relief, multi-entity tax — specialist territory |
| Day trading with hundreds of leveraged positions daily | Refuse | Requires real-time portfolio tracking beyond skill scope |
| Multi-country split-year residency | Refuse | Tax treaties, allocation, dual residency — specialist |
| Amended returns / audit defense | Refuse | Requires review of original return and correspondence |
| Trust / estate income | Refuse | Fiduciary rules, different forms |
| Listed / public company compliance | Refuse | SEC/FCA reporting, IFRS audit, board governance — specialist |

### What is NOT a refusal (previously refused, now in scope)

**Not-a-refusal table**

| Trigger | Action |
| --- | --- |
| Employees / staff / payroll / hiring | **IN SCOPE** — route to payroll skills |
| Limited company (Ltd, GmbH) asking about formation | **IN SCOPE** — route to formation skills |
| Limited company asking about bookkeeping | **IN SCOPE** — route to bookkeeping skills |
| Limited company asking about financial statements | **IN SCOPE** — route to financial statements skills |
| Limited company asking about payroll | **IN SCOPE** — route to payroll skills |
| Rental property (any level of activity) | **IN SCOPE** — route to `property-investor` vertical |
| Small company with simple structure | **IN SCOPE** for all domains except corporate tax returns |

### Soft flags (in scope but needs attention)

**Soft flags table**

| Trigger | Action |
| --- | --- |
| Crypto holdings (trading or investment) | **IN SCOPE** — load country crypto-tax skill + crypto-tax-workflow-base |
| Foreign income / clients abroad | Load cross-border skills, flag for reviewer |
| Multiple businesses / trades | Handle each separately, flag for reviewer |
| First year in business | Flag — may qualify for special reliefs (ACRE, tarifa plana, startersaftrek) |
| Partnership asking about formation or bookkeeping | In scope for those domains — refuse only tax return preparation |

### Refusal message template

"I can help with [list of available domains] for your situation. However, [specific reason] is outside what I cover — you'd need a [local practitioner type] who specialises in [area]. Visit openaccountants.com to find one.

Is there anything else I can help with?"

## Step 3: Route to jurisdiction

### End-to-end jurisdictions (full intake → assembly → output)

**End-to-end jurisdictions table**

| Jurisdiction | Intake skill | What it covers |
| --- | --- | --- |
| **US — California** | `us-ca-freelance-intake` | Federal 1040 + CA 540 + Form 568 |
| **US — New York** | `us-ny-freelance-intake` | Federal 1040 + NY IT-201 + NYC UBT |
| **US — Texas** | `us-tx-freelance-intake` | Federal 1040 + TX franchise tax |
| **Malta** | `mt-freelance-intake` | TA24 + VAT + SSC + provisional tax |
| **UK** | `uk-freelance-intake` | SA100 + SA103 + NIC + VAT + student loan |
| **Germany** | `de-freelance-intake` | ESt + UStVA + SV + GewSt |
| **Australia** | `au-freelance-intake` | ITR + BAS + super + Medicare |
| **Canada** | `ca-freelance-intake` | T1 + T2125 + GST/HST + CPP/EI |
| **India** | `in-freelance-intake` | ITR-3/4 + GST + advance tax |
| **Spain** | `es-freelance-intake` | IRPF + IVA + RETA + Modelo 130 |
| **France** | `fr-freelance-intake` | IR + TVA + URSSAF |
| **Netherlands** | `nl-freelance-intake` | IB + BTW + ZZP deductions |
| **Japan** | `jp-freelance-intake` | Shotoku-zei + consumption tax |
| **Mexico** | `mx-freelance-intake` | ISR + IVA + CFDI |
| **Brazil** | `br-freelance-intake` | IRPF + INSS + Simples |

### End-to-end jurisdictions (full intake → assembly → output)

**For these:** Hand off directly to the intake skill. User gets the full experience.

### US states — all 50 states + DC have tax skills

- **US state loading rules** — Every US state has a dedicated folder under `packages/us-[code]/` containing income tax, sales tax, bookkeeping, and specialty tax skills. When a US user is detected: 1. **Always load** the federal skills: `skills/foundation/us-tax-workflow-base.md` + all of `skills/federal/` + `us-federal-return-assembly.md` 2. **Then load the state folder.** Find the user's state by two-letter code and load ALL `.md` files from `packages/us-[code]/`. 3. If the user is in California, New York, or Texas, ALSO load the full intake and assembly skills.

### US states — all 50 states + DC have tax skills

**US state folder coverage**

| State code | State folder | Income tax? | Sales tax? | Specialty |
| --- | --- | --- | --- | --- |
| AL–WY | `packages/us-[code]/` | 42 states + DC have income tax skills | 45 states have sales tax skills | WA: B&O, TX: franchise, OH: CAT, DE: gross receipts, NV: commerce, NY: NYC UBT |

### US states — all 50 states + DC have tax skills

- **No income tax states** — **No income tax states** (load sales/specialty skills only): AK, FL, NV, NH, SD, TN, TX, WA, WY

### US states — all 50 states + DC have tax skills

- **No sales tax states** — **No sales tax states** (load income tax only): DE, MT, NH, OR (Alaska has local-only sales tax) See `skills/us-states/README.md` for the full coverage matrix.

### Domain-specific routing

**Domain coverage table**

| Domain | Countries with skills | Count |
| --- | --- | --- |
| **Tax** | 133+ countries (consumption tax); 15 countries with full guided intake | 133+ |
| **Bookkeeping** | AU, BE, CA, DE, ES, FR, GB, IT, JP, MT, NL, PT, SE + all US states | 13 |
| **E-invoicing** | BE, BR, DE, ES, FR, GR, HU, IN, IT, MX, MY, PL, PT, RO, SA | 15 |
| **Payroll** | AU, BE, BR, CA, DE, ES, FR, GB, ID, IN, IT, JP, MT, NL, PT, SE | 16 |
| **Company formation** | AU, CA, DE, ES, FR, GB, IN, IT, JP, MT, NL, PT, SG | 13 |
| **Financial statements** | AU, BE, CA, DE, ES, FR, GB, IN, IT, JP, MT, NL, PT | 13 |
| **Transfer pricing** | AU, BR, CA, DE, ES, FR, GB, IN, IT, JP, MX, MT, NL, SG, ZA | 15 |
| **Tax optimization** | AU, CA, DE, ES, FR, GB, IN, IT, JP, MT, NL, PT, SG | 13 |
| **Crypto tax** | AU, BE, BR, CA, CH, DE, ES, FR, GB, IL, IN, IT, JP, KR, MT, MX, NL, NZ, PT, SE, SG, US | 22 |

### Domain-specific routing

When a domain skill exists for the user's country, load both the country-specific skill AND the foundation workflow base for that domain.

When a domain skill **doesn't exist** for the user's country:

> "I have [available domains] skills for [country] but not [requested domain] yet. Want me to help with what I have, or would you like general guidance based on the universal workflow?"

### 130+ countries with consumption tax skills only

> "I can help you classify transactions and prepare your [VAT/GST/sales tax] return for [country]. I don't cover [requested domain] for [country] yet. Want me to help with what I have?"

### Countries with nothing

> "I don't have skills for [country] yet. We're building them — visit openaccountants.com if you'd like to help. In the meantime, I'd recommend a local [practitioner type]."

## Step 4: Handoff

When routing to a jurisdiction skill, pass:

```json
{
  "jurisdiction": "[detected]",
  "domain": "[detected — tax, bookkeeping, payroll, formation, financial_statements, einvoicing, transfer_pricing, tax_optimization, cross_border, integration]",
  "business_type": "[detected — e.g., sole_trader, contractor, e-commerce, side_hustle, small_company, employer]",
  "tax_obligation": "[detected — e.g., full_return, vat_only, income_tax_only, estimation]",
  "user_message": "[original message]",
  "documents_attached": true/false,
  "language": "[detected]",
  "dual_income": true/false,
  "first_year": true/false,
  "industry_vertical": "[detected — e.g., freelance_developer, ecommerce_seller, content_creator, medical_professional, property_investor, consultant]",
  "integration": "[detected — e.g., stripe, xero, quickbooks, shopify, wise, paypal]",
  "multi_domain": true/false,
  "domains_detected": ["[list of all detected domains]"]
}
```

When routing directly to a content skill (no intake available), explain:

> "I'm loading the [skill name] skill. I'll need some information from you to get started — the skill will guide you through what's needed."

## Step 5: Special packages routing

**Special packages table**

| Package | When to load | Contents |
| --- | --- | --- |
| `_cross-border/` | User mentions 2+ countries, foreign clients, relocation, digital nomad, treaty, withholding on foreign income | 22 skills: treaty defaults, PE risk, withholding matrix, EU reverse charge, OSS, VAT place of supply, forex controls, payroll coordination, corridors (EU, US, UK, APAC, Americas, emerging markets) |
| `_verticals/` | User mentions a specific industry or profession | `freelance-developer`, `ecommerce-seller`, `content-creator`, `medical-professional`, `consultant-professional`, `property-investor` |
| `_integrations/` | User mentions specific software or platform | `stripe`, `xero`, `quickbooks`, `paypal`, `wise`, `revolut-business`, `shopify`, `amazon-seller`, `freeagent`, `sage` |

## Step 5: Special packages routing

Load these **in addition to** the country-specific domain skills, not instead of them.

## Step 6: Language handling

Respond in the user's language. If the user writes in:
- German → respond in German, use German tax terms (Steuererklärung, Einnahmenüberschussrechnung)
- Spanish → respond in Spanish (declaración de la renta, autónomo)
- French → respond in French (déclaration de revenus, travailleur indépendant)
- Italian → respond in Italian (dichiarazione dei redditi, partita IVA)
- Portuguese → respond in Portuguese (declaração de IRS, trabalhador independente)
- Dutch → respond in Dutch (belastingaangifte, zzp'er)
- Japanese → respond in Japanese (確定申告, 個人事業主)
- English → respond in English

Tax forms and legal terms should always use the local-language name (e.g., "Modelo 303" not "Form 303").

## PROHIBITIONS

- **Prohibitions list** — - NEVER guess a jurisdiction — ask if unclear - NEVER route to a skill that doesn't exist - NEVER claim you can do something you can't — be honest about availability - NEVER refuse a side hustler — employed + self-employed is in scope - NEVER refuse based on profession — doctors, lawyers, architects are in scope if self-employed - NEVER refuse e-commerce sellers — they use the same tax forms as any sole trader - NEVER respond in English if the user wrote in another language (unless they switch to English) - NEVER refuse a small company asking about formation, bookkeeping, or financial statements - NEVER load only tax skills when the user clearly needs a different domain - NEVER ignore industry context — if they say they're a developer, load the `freelance-developer` vertical - NEVER refuse payroll queries — payroll is a fully supported domain - NEVER refuse employer queries — route to payroll skills - NEVER refuse rental property / landlord queries — route to `property-investor` vertical

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
