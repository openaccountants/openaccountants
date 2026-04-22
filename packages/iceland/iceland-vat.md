---
name: iceland-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Iceland VAT (VSK) return for any client. Trigger on phrases like "prepare VSK return", "Iceland VAT", "virðisaukaskattur", "Icelandic VAT filing", or any request involving Icelandic VAT. Iceland is NOT an EU member but IS in the EEA. This skill covers Iceland only. MUST be loaded alongside vat-workflow-base v0.1 or later. Does NOT require eu-vat-directive (Iceland is not EU). ALWAYS read this skill before touching any Iceland VSK work.
version: 2.0
---

# Iceland VAT Return Skill (VSK) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1. Note: Iceland is NOT an EU member. The eu-vat-directive companion skill does NOT apply. Iceland follows its own VSK legislation with EEA adaptations.**

| Field | Value |
|---|---|
| Country | Iceland (Island) |
| Standard rate | 24% |
| Reduced rate | 11% (food, accommodation, books, newspapers, geothermal hot water, radio/TV licence) |
| Zero rate | 0% (exports, international transport) |
| Return form | VSK return (Virðisaukaskattsskýrsla) |
| Filing portal | https://www.skattur.is (Skatturinn portal) |
| Authority | Rikisskattstjori (Directorate of Internal Revenue) |
| Currency | ISK (Icelandic Krona) |
| Filing frequencies | Bi-monthly (standard: Jan-Feb, Mar-Apr, etc.); Monthly (large taxpayers, optional) |
| Deadline | 5th of 2nd month after period end (e.g. 5 April for Jan-Feb) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (EU directive) | **NOT required — Iceland is not EU** |
| EEA status | EEA member via EFTA. No intra-community supplies. No VIES. Goods from EU treated as imports. Services from abroad subject to reverse charge. |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key VSK return fields:**

| Field | Meaning |
|---|---|
| A | Domestic sales at 24% — base |
| B | Domestic sales at 11% — base |
| C | Output VSK at 24% |
| D | Output VSK at 11% |
| E | Zero-rated sales (exports) |
| F | Exempt sales |
| G | Reverse charge on imported services — base |
| H | VSK on reverse charge (output) |
| I | Total output VSK (C + D + H) |
| J | Input VSK on domestic purchases |
| K | Input VSK on imports (customs) |
| L | Input VSK on reverse charge services (input side) |
| M | Total deductible input VSK (J + K + L) |
| N | Net VSK payable (I minus M) or refundable |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 24% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Iceland |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge (all foreign = import of service) |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | ISK 500,000 |
| HIGH tax-delta on single default | ISK 30,000 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net VSK position | ISK 800,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the bi-monthly period. Acceptable from: Islandsbanki, Landsbankinn, Arion banki, Revolut Business, Wise Business.

**Recommended** — sales/purchase invoices, kennitala (10-digit ID), VSK number (IS + 5-6 digits), prior VSK return.

**Ideal** — complete register, customs declarations for imports, prior period reconciliation.

### Iceland-specific refusal catalogue

**R-IS-1 — Non-registered.** *Trigger:* not registered, turnover below ISK 2,000,000. *Message:* "Non-registered entities do not file VSK returns."

**R-IS-2 — Partial exemption.** *Message:* "Mixed supplies require proportional attribution. Use a qualified tax adviser."

**R-IS-3 — Fishing vessel / special investment schemes.** *Message:* "Fishing vessel and special investment zone schemes out of scope."

**R-IS-4 — Faroe Islands trade.** *Trigger:* trade with Faroe Islands. *Message:* "Faroe Islands are a separate Danish territory, not part of Iceland for VSK. Specialist review needed."

---

## Section 3 — Supplier pattern library

### 3.1 Icelandic banks (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ISLANDSBANKI, ÍSLANDSBANKI | EXCLUDE | Financial service, exempt |
| LANDSBANKINN | EXCLUDE | Same |
| ARION BANKI, ARION | EXCLUDE | Same |
| REVOLUT, WISE (fee lines) | EXCLUDE | Check subscriptions |
| VEXTIR, INTEREST | EXCLUDE | Interest |
| LAN, LOAN | EXCLUDE | Loan principal |

### 3.2 Icelandic government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| RIKISSKATTSTJORI, RSK | EXCLUDE | Tax payment |
| TRYGGINGASTOFNUN | EXCLUDE | Social insurance |
| RIKISSKRÁ | EXCLUDE | National registry |

### 3.3 Icelandic utilities

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| ORKUVEITA REYKJAVIKUR, OR | Domestic 24% or 11% | J | Electricity/hot water — hot water at 11% |
| RARIK | Domestic 24% | J | Electricity |
| HS VEITUR | Domestic 11% | J | Geothermal heating at 11% |
| SIMINN | Domestic 24% | J | Telecoms |
| VODAFONE IS, NOVA | Domestic 24% | J | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SJOVA | EXCLUDE | Exempt |
| VARDAR | EXCLUDE | Same |
| TM TRYGGINGAR | EXCLUDE | Same |
| VIS INSURANCE | EXCLUDE | Same |
| TRYGGING, INSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Notes |
|---|---|---|
| ISLANDSPÓSTUR, ICELAND POST | EXCLUDE for standard post; 24% for parcel | |
| DHL, UPS, FEDEX | Domestic 24% or import | Check if import |

### 3.6 Transport

| Pattern | Treatment | Notes |
|---|---|---|
| STRÆTO, STRÆTÓ | Domestic 24% | Public bus |
| ICELANDAIR (international) | 0% | International flight |
| ICELANDAIR (domestic) | Domestic 24% | Domestic flight |

### 3.7 Food retail

| Pattern | Treatment | Notes |
|---|---|---|
| BONUS, KRONAN, HAGKAUP, NETTO IS | Default BLOCK | Personal provisioning |
| VEITINGAHÚS, RESTAURANT | Default BLOCK | Entertainment |

### 3.8 SaaS — ALL foreign suppliers (reverse charge — Iceland treats all foreign as import of service)

Since Iceland is NOT EU, ALL foreign SaaS is treated identically: reverse charge under Act 50/1988 Art. 35.

| Pattern | Billing entity | Field | Notes |
|---|---|---|---|
| GOOGLE | Google Ireland Ltd (IE) | G/H + L | Reverse charge import of service |
| MICROSOFT | Microsoft Ireland (IE) | G/H + L | Same |
| ADOBE | Adobe Ireland (IE) | G/H + L | Same |
| META, FACEBOOK | Meta Ireland (IE) | G/H + L | Same |
| SPOTIFY | Spotify AB (SE) | G/H + L | Same (even though EFTA/EEA) |
| NOTION | Notion Labs Inc (US) | G/H + L | Same |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | G/H + L | Same |
| OPENAI, CHATGPT | OpenAI Inc (US) | G/H + L | Same |
| AWS EMEA SARL | LU entity | G/H + L | Same |
| GITHUB | GitHub Inc (US) | G/H + L | Same |
| FIGMA | Figma Inc (US) | G/H + L | Same |
| CANVA | Canva Pty Ltd (AU) | G/H + L | Same |

### 3.9 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| VALITOR, BORGUN | EXCLUDE for transaction fees | Icelandic card processors; fees exempt |

### 3.10 Professional services

| Pattern | Treatment | Notes |
|---|---|---|
| LÖGMAÐUR, LAWYER | Domestic 24% | Legal |
| ENDURSKOÐANDI, AUDITOR | Domestic 24% | Accounting |

### 3.11 Payroll (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| TRYGGINGAGJALD | EXCLUDE | Social insurance levy |
| LAUN, SALARY | EXCLUDE | Wages |
| TEKJUSKATTUR | EXCLUDE | Income tax |

### 3.12 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| MILLIFÆRSLA, OWN TRANSFER | EXCLUDE | Internal |
| ARÐUR, DIVIDEND | EXCLUDE | Out of scope |
| AFBORGUN, LOAN REPAYMENT | EXCLUDE | Loan principal |
| HRAÐBANKI, ATM | Ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Foreign SaaS reverse charge (Notion)
**Input:** `03.04.2026 ; NOTION LABS INC ; -2,200 ISK`
**Treatment:** All foreign services: reverse charge at 24%. Field G (base), Field H (output VSK). Input in Field L. Net zero.

### Example 2 — Foreign SaaS (Google — also reverse charge, no EU distinction)
**Input:** `10.04.2026 ; GOOGLE IRELAND LIMITED ; -127,500 ISK`
**Treatment:** Same as Example 1. Iceland does NOT have intra-EU treatment. All foreign = reverse charge.

### Example 3 — Entertainment
**Input:** `15.04.2026 ; GRILLIÐ RESTAURANT ; -33,000 ISK`
**Treatment:** Restaurant. Entertainment input VSK not deductible. Block.

### Example 4 — EU B2B service sale (no zero-rate — just non-domestic)
**Input:** `22.04.2026 ; STUDIO KREBS GMBH ; +525,000 ISK`
**Treatment:** Service sold to German company. Export of service. Field E (zero-rated export). No output VSK.

### Example 5 — Accommodation (reduced rate)
**Input:** `Sales: Hotel room in Reykjavik ; +45,000 ISK`
**Treatment:** Accommodation at 11%. Field B (base), Field D (output VSK at 11%).

### Example 6 — Import of goods
**Input:** `Customs declaration: Computer from US ; ISK 240,000 + ISK 57,600 import VSK`
**Treatment:** Import VSK paid to customs. Input in Field K.

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard 24% (Act 50/1988, Art. 14(1))
Default. Sales: Field A/C. Input: Field J.

### 5.2 Reduced 11% (Art. 14(2))
Food, accommodation, books, newspapers, geothermal hot water, radio/TV licence.

### 5.3 Zero rate (Art. 12, 42)
Exports: Field E. International transport: Field E.

### 5.4 Exempt
Financial, insurance, healthcare, education, postal, gambling, residential rental.

### 5.5 Reverse charge — ALL foreign services (Art. 35)
No EU/non-EU distinction. All services received from abroad: self-assess at 24%. Field G (base), Field H (output). Input in Field L.

### 5.6 Imports of goods
Import VSK assessed by customs. Input: Field K.

### 5.7 No intra-community rules
Iceland has NO intra-EU acquisition/supply mechanism. Goods from EU countries are imports. Services from anywhere are reverse charge.

### 5.8 Blocked input
- Entertainment: blocked
- Personal use: blocked
- Motor vehicles: restricted (deductible only if exclusively for business)

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs — *Default:* 0%. *Question:* "Exclusive business use?"
### 6.2 Entertainment — *Default:* block.
### 6.3 Foreign SaaS — *Default:* reverse charge at 24%.
### 6.4 Owner transfers — *Default:* exclude.
### 6.5 Tourism/hospitality — *Default:* 11%. *Question:* "Confirm accommodation vs food service."
### 6.6 Import goods — *Default:* check customs declaration.
### 6.7 Cash withdrawals — *Default:* exclude.

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3. Column H accepts Iceland VSK field codes (A-N). Bottom-line: Field N (net payable/refundable = Field I minus Field M).

---

## Section 8 — Iceland bank statement reading guide

**CSV conventions.** Islandsbanki and Landsbankinn use semicolons, DD.MM.YYYY. ISK amounts.

**Icelandic language.** leiga (rent), laun (salary), vextir (interest), millifærsla (transfer), reiðufe (cash).

**Currency.** ISK only. Convert foreign at Central Bank of Iceland rate.

**No IBAN.** Iceland uses IBAN with IS prefix but is NOT in the EU SEPA zone for all purposes.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Inference:* ehf. = company; einstaklingsrekstur = sole trader.
### 9.2 VSK registration — *Fallback:* "VSK-registered?"
### 9.3 Kennitala — *Fallback:* "Kennitala? (10 digits)"
### 9.4 VSK number — *Fallback:* "VSK number? (IS + 5-6 digits)"
### 9.5 Filing period — Bi-monthly default.
### 9.6 Tourism/hospitality — *Fallback:* "Tourism or accommodation business?"
### 9.7 Exports — *Fallback:* "Do you export goods or services?"

---

## Section 10 — Reference material

### Sources
1. Log um virðisaukaskatt (Act No. 50/1988, as amended)
2. Regulation No. 630/2008
3. EEA Agreement (cross-border service rules)
4. Central Bank of Iceland exchange rates

### Known gaps
1. Fishing vessel schemes not covered.
2. Svalbard-equivalent special zones not detailed.
3. Tourism sector-specific rules could be expanded.

### Change log
- **v2.0 (April 2026):** Full rewrite. Icelandic banks (Islandsbanki, Landsbankinn, Arion). EEA-not-EU distinction clarified throughout.
- **v1.0 (April 2026):** Initial skill.

## End of Iceland VAT Return Skill v2.0

This skill is incomplete without `vat-workflow-base` v0.1+. Note: `eu-vat-directive` is NOT required for Iceland.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
