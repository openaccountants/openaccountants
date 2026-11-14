---
name: global-router
description: "2026 entry-point router for OpenAccountants accounting and tax methods. Establishes the actual task, jurisdictions, period and entity facts; checks current catalogue and live availability; loads the relevant country methods and dependencies; preserves each method's approval attribution and hands off unresolved facts. Covers the existing tax, bookkeeping, e-invoicing, payroll, formation, reporting, transfer-pricing, planning, cross-border, crypto and integration discovery routes without promising full coverage from a list."
version: 1.2
jurisdiction: GLOBAL
tax_year: 2026
type: router
last_updated: 2026-11-14
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tooling
---

# Global Router

## Global Router v1.2

## What this file is

This is an entry-point routing method for OpenAccountants, checked on 14 November 2026. It selects current skills and their applicable facts. It does not classify a person's legal tax status or guarantee a whole-country service from a historical country list.

**Answer first:** identify the actual taxpayer, task, jurisdiction(s), period and entity facts already supplied. Search the current catalogue, check publication/availability, load the relevant methods and preserve their exact current approval label. Ask only for facts that remain necessary. Language, currency and occupation are clues, not residence or legal-entity evidence.

The router does five things:
1. Figure out where the user is (jurisdiction)
2. Figure out what they need (domain + business type)
3. Check refusal rules (narrow , most things are in scope now)
4. Route to the right skill(s) for their jurisdiction and domain
5. Hand off with structured context

**The user never sees this skill.** They just talk naturally. The router works silently.

## The method, step by step

### Step 0: Establish the relevant jurisdictions

**Jurisdiction detection signals**

| Signal | Example | Jurisdiction |
| --- | --- | --- |
| Country name | "I'm in Germany" | DE |
| City name | "I live in London" | GB |
| State/province | "California", "Ontario" | US-CA, CA-ON |
| Tax system mention | "Self Assessment", "TA24" | GB, MT |
| Tax form mention | "Schedule C", "Modelo 303", "GSTR-3B" | US, ES, IN |
| Tax authority mention | "HMRC", "ATO", "SAT", "IRAS" | GB, AU, MX, SG |
| Currency context | "earning in GBP", "invoicing in EUR" | No jurisdiction established; ask which tax country/territory and transaction are involved |
| Language + context | German text + tax question | Respond in German; do not infer Germany rather than another relevant jurisdiction |

### City names as discovery clues, not residence findings

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
| Washington DC | Candidate US-DC; confirm the taxpayer and applicable place/period |
| Arlington VA | Candidate US-VA from the explicit state clue, never silently US-DC |
| Georgetown without a state/country | Ambiguous; confirm before selecting a state/country |
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

- **Unclear jurisdiction handling:** first use the actual question and records to distinguish residence, business establishment, place of work, property and transaction location. If a specific country question is already clear, route that question without re-asking residence unnecessarily. Otherwise ask one targeted question naming the missing place/period. Do not choose a tax country from a currency, interface language, IP location or a shared city name alone.

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

### B. Business type discovery, subject to the actual legal and tax classification

**Business type detection signals**

| Signal | Business type | In scope? |
| --- | --- | --- |
| "freelancer", "contractor", "independent contractor" | Self-employed | **Yes** |
| "self-employed", "sole trader", "sole proprietor" | Self-employed | **Yes** |
| "consultant", "consulting", "advisory" | Self-employed | **Yes** |
| "e-commerce", "online store", "Shopify", "Etsy", "Amazon seller" | Self-employed seller | **Yes** |
| "content creator", "YouTuber", "influencer", "streamer" | Self-employed | **Yes** |
| "gig worker", "Uber", "Deliveroo", "DoorDash", "Fiverr", "Upwork" | Self-employed | **Yes** |
| "side hustle", "side business", "moonlighting" | Employed + self-employed | **Yes** , handle both income streams |
| "tutor", "music teacher", "personal trainer", "photographer" | Self-employed | **Yes** |
| "artist", "writer", "musician", "designer", "developer" | Self-employed | **Yes** |
| "doctor", "lawyer", "architect", "accountant" (solo practice) | Self-employed professional | **Yes** , check jurisdiction for special regimes |
| "LLC", "single-member LLC", "SMLLC" | Entity form/tax classification to establish, including owners and any election | **Yes** for supported preparation; do not infer disregarded status merely from LLC |
| "Einzelunternehmen", "Freiberufler", "Gewerbetreibender" | Self-employed (DE) | **Yes** |
| "autónomo" | Self-employed (ES) | **Yes** |
| "auto-entrepreneur", "micro-entrepreneur" | Self-employed (FR) | **Yes** |
| "zzp'er", "zelfstandige" | Self-employed (NL) | **Yes** |
| "partita IVA" | Self-employed (IT) | **Yes** |
| "landlord", "rental property", "property investor" | Property investor | **Yes** , route to `property-investor` vertical |
| "employees", "staff", "payroll", "hiring" | Employer | **Yes** , route to payroll skills |
| "limited company", "Ltd", "GmbH", "SL", "SARL", "Srl" | Company, size/regime not yet established | Route the actual task, including corporate tax, to its current country method and specialist boundary |
| "partnership", "LLP", "OHG", "SNC" | Partnership or local entity classification to establish | Search for the country's actual partnership tax and other task methods; refer only the unsupported portion |
| "S-corp", "C-corp", "AG", "SA" | Corporate form/election to verify | Search for the applicable company return method; a company label alone is not a refusal |
| "I'm a developer", "software engineer" | Industry vertical | **Yes** , load `freelance-developer` vertical |
| "e-commerce", "online shop" | Industry vertical | **Yes** , load `ecommerce-seller` vertical |
| "content creator", "YouTuber", "influencer" | Industry vertical | **Yes** , load `content-creator` vertical |
| "doctor", "medical", "healthcare practice" | Industry vertical | **Yes** , load `medical-professional` vertical |
| "consultant", "advisory", "professional services" | Industry vertical | **Yes** , load `consultant-professional` vertical |

An occupation, marketplace brand or legal-form abbreviation does not establish employment, self-employment, small-company status or a tax election. Confirm the actual relationship/owners/election before computing; keep every relevant industry clue for search.

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

- **Dual income handling** , If the user mentions BOTH employment AND self-employment: "I have a day job but also freelance on the side"; "I'm employed at [company] but have a side business"; "I get a W-2/P60/Lohnsteuerbescheinigung AND 1099/invoices". **This is IN SCOPE.** Handle the self-employment income using the normal skills. Flag for the reviewer that employment income exists and affects: Tax bracket (total income determines marginal rate); Social contributions (may already be covered by employer , check jurisdiction); Estimated tax (PAYE/withholding from employment may cover most of the liability).

## When to refuse or refer

### Step 2: Resolve scope and specialist boundaries

### Specialist boundary checks, not automatic worldwide refusals

**Hard refusals table**

| Trigger | Refusal | Why |
| --- | --- | --- |
| Partnership tax returns | Search current country/entity methods; refer unsupported allocation or filing work | Different forms/allocations require the actual method, not a blanket rejection |
| Corporate tax returns | Load `corporate-income-tax-workflow-base` and the available current country/entity method | Corporate tax differs from personal tax, but that is a routing reason, not an automatic refusal |
| Large corporate groups with complex structures | Refuse | Consolidation, group relief, multi-entity tax , specialist territory |
| Day trading with hundreds of leveraged positions daily | Refuse | Requires real-time portfolio tracking beyond skill scope |
| Multi-country/split-year residence | Load an available current cross-border/residency method, then refer the unresolved country/treaty issue | Treaty/period facts must be established before the affected conclusion |
| Amended returns / audit defence | Obtain the original return/correspondence and find the specific country amendment/controversy method; refer the unsupported part | Do not promise representation or an accepted amendment |
| Trust / estate income | Refuse | Fiduciary rules, different forms |
| Listed / public company compliance | Refuse | SEC/FCA reporting, IFRS audit, board governance , specialist |

### What is NOT a refusal (previously refused, now in scope)

**Not-a-refusal table**

| Trigger | Action |
| --- | --- |
| Employees / staff / payroll / hiring | **IN SCOPE** , route to payroll skills |
| Limited company (Ltd, GmbH) asking about formation | **IN SCOPE** , route to formation skills |
| Limited company asking about bookkeeping | **IN SCOPE** , route to bookkeeping skills |
| Limited company asking about financial statements | **IN SCOPE** , route to financial statements skills |
| Limited company asking about payroll | **IN SCOPE** , route to payroll skills |
| Rental property (any level of activity) | **IN SCOPE** , route to `property-investor` vertical |
| Small company with simple structure | Search each requested domain, including corporate tax; apply the selected method's actual boundary |

### Soft flags (in scope but needs attention)

**Soft flags table**

| Trigger | Action |
| --- | --- |
| Crypto holdings (trading or investment) | **IN SCOPE** , load country crypto-tax skill + crypto-tax-workflow-base |
| Foreign income / clients abroad | Load cross-border skills, flag for reviewer |
| Multiple businesses / trades | Handle each separately, flag for reviewer |
| First year in business | Flag , may qualify for special reliefs (ACRE, tarifa plana, startersaftrek) |
| Partnership asking about formation or bookkeeping | In scope where a current method supports the job; also search for the actual partnership-return method if requested |

### Refusal message template

"I can help with [list of available domains] for your situation. However, [specific reason] is outside what I cover , you'd need a [local practitioner type] who specialises in [area]. Visit openaccountants.com to find one.

Is there anything else I can help with?"

## Step 3: Route to jurisdiction

### Intake discovery seeds, availability and actual scope must be checked

**End-to-end jurisdictions table**

| Jurisdiction | Intake skill | What it covers |
| --- | --- | --- |
| **US , California** | `us-ca-freelance-intake` | Federal 1040 + CA 540 + Form 568 |
| **US , New York** | `us-ny-freelance-intake` | Federal 1040 + NY IT-201 + NYC UBT |
| **US , Texas** | `us-tx-freelance-intake` | Federal 1040 + TX franchise tax |
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

### Intake discovery seeds, availability and actual scope must be checked

**For these:** search for the exact current intake slug and read its actual scope and publication state before handing off. A seed row does not prove complete pack coverage or a currently live method. Where the input record already exists, read it instead of collecting it twice.

### US states , all 50 states + DC have tax skills

- **US state loading rules:** establish the actual federal/state/local obligations and period. Search the current catalogue for the exact task and confirmed state, then load only the relevant federal/state method and required dependencies. The shared source is `skills/global/methods/us-tax-workflow-base.md`, not the old `skills/foundation/` path. Do not load all federal and all state files for one narrow question. Use a state intake/assembly method only when the requested full return and current availability require it.

### US states , all 50 states + DC have tax skills

**US state folder coverage**

| State code | State folder | Income tax? | Sales tax? | Specialty |
| --- | --- | --- | --- | --- |
| Individual confirmed state | Search its actual current catalogue/package | Check actual income/capital/business scope, not a frozen count | Check state and local scope, not a frozen count | Discovery examples retained: WA B&O, TX franchise, OH CAT, DE gross receipts, NV commerce, NY/NYC UBT; load only when relevant |

### US states , all 50 states + DC have tax skills

- **Wage-tax discovery hints:** for AK, FL, NV, NH, SD, TN, TX, WA and WY, check the actual income/business/capital-gain and local obligations before concluding what is due. A missing broad wages tax does not mean no income-related or business tax. Do not suppress relevant specialty skills.

### US states , all 50 states + DC have tax skills

- **Sales-tax discovery hints:** for DE, MT, NH, OR and Alaska, inspect the actual state/local/sector rules before concluding whether a particular sale or gross receipt is taxed. Do not load income tax only merely because a broad state sales tax is absent. The current state README and task method determine coverage.

### Domain-specific routing

**Domain coverage table**

| Domain | Historical country discovery clues, verify current catalogue |
| --- | --- |
| **Tax** | Search the current country/task catalogue; guide presence is not comprehensive coverage |
| **Bookkeeping** | AU, BE, CA, DE, ES, FR, GB, IT, JP, MT, NL, PT, SE + all US states |
| **E-invoicing** | BE, BR, DE, ES, FR, GR, HU, IN, IT, MX, MY, PL, PT, RO, SA |
| **Payroll** | AU, BE, BR, CA, DE, ES, FR, GB, ID, IN, IT, JP, MT, NL, PT, SE |
| **Company formation** | AU, CA, DE, ES, FR, GB, IN, IT, JP, MT, NL, PT, SG |
| **Financial statements** | AU, BE, CA, DE, ES, FR, GB, IN, IT, JP, MT, NL, PT |
| **Transfer pricing** | AU, BR, CA, DE, ES, FR, GB, IN, IT, JP, MX, MT, NL, SG, ZA |
| **Tax optimization** | AU, CA, DE, ES, FR, GB, IN, IT, JP, MT, NL, PT, SG |
| **Crypto tax** | AU, BE, BR, CA, CH, DE, ES, FR, GB, IL, IN, IT, JP, KR, MT, MX, NL, NZ, PT, SE, SG, US |
### Domain-specific routing

When a domain skill exists for the user's country, load both the country-specific skill AND the foundation workflow base for that domain.

**Availability gate:** source presence and a generated index are distinct from a successful live `get_skill` response. Search by the actual country/task, use the returned exact slug, then read the result. A publication hold, missing dependency, empty search or unreadable load is a named coverage gap, not permission to invent content or silently load another country. The checked catalogue currently holds `property-investor` for missing sources and `cross-border-workflow-base` for unavailable companions; keep their subject routes but do not promise those held bodies are live. For a live cross-border entry, search `cross-border-tax-router` and then its actual available companions. Recheck at use because availability changes.

When a domain skill **doesn't exist** for the user's country:

> "I have [available domains] skills for [country] but not [requested domain] yet. Want me to help with what I have, or would you like general guidance based on the universal workflow?"

### Countries where only some requested jobs are actually available

> "I found [actual available methods] for [country/task/period]. [Specific missing job] is not available in the current catalogue. I can continue the supported work and identify what that part still needs."

### Countries with nothing

> "I don't have skills for [country] yet. We're building them , visit openaccountants.com if you'd like to help. In the meantime, I'd recommend a local [practitioner type]."

## Step 4: Handoff

When routing to a jurisdiction skill, pass the original question and established facts below. Leave unknown facts as null with a missing-fact entry, not false or an assumed filing status. Also pass the confirmed tax period, each loaded exact slug/version/date and actual approval label/name. An accountant on one skill does not approve the whole multi-skill answer. Never invent a contributor or infer approval from Git authorship.

When routing to a jurisdiction skill, pass:

```json
{
  "jurisdiction": "[detected]",
  "domain": "[detected , tax, bookkeeping, payroll, formation, financial_statements, einvoicing, transfer_pricing, tax_optimization, cross_border, integration]",
  "business_type": "[detected , e.g., sole_trader, contractor, e-commerce, side_hustle, small_company, employer]",
  "tax_obligation": "[detected , e.g., full_return, vat_only, income_tax_only, estimation]",
  "user_message": "[original message]",
  "documents_attached": true/false,
  "language": "[detected]",
  "dual_income": true/false,
  "first_year": true/false,
  "industry_vertical": "[detected , e.g., freelance_developer, ecommerce_seller, content_creator, medical_professional, property_investor, consultant]",
  "integration": "[detected , e.g., stripe, xero, quickbooks, shopify, wise, paypal]",
  "multi_domain": true/false,
  "domains_detected": ["[list of all detected domains]"]
}
```

When routing directly to a content skill (no intake available), explain:

> "I'm loading the [skill name] skill. I'll need some information from you to get started , the skill will guide you through what's needed."

## Step 5: Special packages routing

**Special packages table**

| Package | When to load | Contents |
| --- | --- | --- |
| `_cross-border/` | Actual question involves multiple countries, foreign clients, relocation, digital nomad, treaty or foreign-income withholding | Search relevant treaty, PE, withholding, VAT/reverse-charge/OSS, forex, payroll and corridor methods; the old fixed count is not a coverage promise |
| `_verticals/` | User mentions a specific industry or profession | `freelance-developer`, `ecommerce-seller`, `content-creator`, `medical-professional`, `consultant-professional`, `property-investor` |
| `_integrations/` | User mentions specific software or platform | `stripe-integration`, `xero-integration`, `quickbooks-integration`, `paypal-integration`, `wise-integration`, `revolut-business-integration`, `shopify-integration`, `amazon-seller-integration`, `freeagent-integration`, `sage-integration` |

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

- **Prohibitions list** , - NEVER guess a jurisdiction , ask if unclear - NEVER route to a skill that doesn't exist - NEVER claim you can do something you can't , be honest about availability - NEVER refuse a side hustler , employed + self-employed is in scope - NEVER refuse based on profession , doctors, lawyers, architects are in scope if self-employed - NEVER refuse e-commerce sellers , they use the same tax forms as any sole trader - NEVER respond in English if the user wrote in another language (unless they switch to English) - NEVER refuse a small company asking about formation, bookkeeping, or financial statements - NEVER load only tax skills when the user clearly needs a different domain - NEVER ignore industry context , if they say they're a developer, load the `freelance-developer` vertical - NEVER refuse payroll queries , payroll is a fully supported domain - NEVER refuse employer queries , route to payroll skills - NEVER refuse rental property / landlord queries , route to `property-investor` vertical

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.


## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| OpenAccountants index at the checked main commit. Read the generated catalogue and publication_holds for exact integration names, property-investor source hold and cross-border-workflow dependency hold. This is primary product evidence, not tax-law verification | https://github.com/openaccountants/openaccountants/blob/448f5f2fab3ba3275cf7e83082302c841648cf7d/index.json | 2026-11-14 |
| OpenAccountants Python MCP implementation at the checked main commit. Read get_skill and search_skills contracts for exact slug loading, returned availability and provenance; no live app deployment is inferred | https://github.com/openaccountants/openaccountants/blob/448f5f2fab3ba3275cf7e83082302c841648cf7d/mcp/openaccountants_mcp/server.py | 2026-11-14 |
| HMRC Company Tax Returns overview. Read for company returns as an actual supported legal job distinct from personal returns; a company label alone is not a reason to reject tax preparation | https://www.gov.uk/company-tax-returns/overview | 2026-11-14 |
| IRAS Preparing a Tax Computation. Read What is a Tax Computation for company-specific computation and return-document routing; no rates imported | https://www.iras.gov.sg/taxes/corporate-income-tax/form-c-s-form-c-s-%28lite%29-form-c-filing/preparing-a-tax-computation | 2026-11-14 |

Not yet confirmed: actual live availability, current country/task scope, tax year and professional approval must be checked when loading; the dated catalogue is not a guarantee of production delivery or comprehensive coverage. Historical city/country/domain lists and intake form names are discovery seeds, not residence findings or certified legal obligations. No country is inferred from language/currency, no legal entity classification is inferred from occupation/LLC alone, and no held or absent method is silently replaced with another country. This router provides no rates, deadlines or tax computation.
