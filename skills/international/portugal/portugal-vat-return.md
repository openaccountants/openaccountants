---
name: portugal-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Portuguese VAT return (Declaração Periódica de IVA) for a self-employed individual or small business in Portugal. Trigger on phrases like "prepare Declaração Periódica", "Portuguese VAT return", "IVA Portugal", "classify transactions for Portuguese VAT", or any request involving Portugal VAT filing. This skill covers Continental Portugal only (standard regime). Madeira/Azores reduced rates, regime de isenção, partial exemption, margin scheme (regime da margem), and VAT groups are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Portuguese VAT work.
version: 2.0
---

# Portugal VAT Return Skill (Declaração Periódica de IVA) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Portugal (República Portuguesa) |
| Standard rate | 23% (Continental); 22% (Madeira); 16% (Azores) |
| Reduced rates | 13% Continental / 12% Madeira / 9% Azores (intermediate: restaurants, food products, diesel, some agricultural inputs); 6% Continental / 5% Madeira / 4% Azores (reduced: basic foodstuffs, water, books, medicines, passenger transport, hotels) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods) |
| Return form | Declaração Periódica de IVA (campos/fields 1–41+) |
| Filing portal | https://www.portaldasfinancas.gov.pt (Portal das Finanças) |
| Authority | Autoridade Tributária e Aduaneira (AT) |
| Currency | EUR only |
| Filing frequencies | Monthly (turnover > €650,000 or Vol. B); Quarterly (turnover ≤ €650,000, Vol. A) |
| Deadline | Monthly: 10th of 2nd month after period end; Quarterly: 15th of 2nd month after quarter end |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants contributors |
| Validation date | April 2026 |

**Key Declaração Periódica campos (the fields you will use most):**

| Campo | Meaning |
|---|---|
| 1 | Sales at standard rate — base (23%) |
| 2 | Sales at standard rate — IVA |
| 3 | Sales at intermediate rate — base (13%) |
| 4 | Sales at intermediate rate — IVA |
| 5 | Sales at reduced rate — base (6%) |
| 6 | Sales at reduced rate — IVA |
| 7 | Exempt sales with deduction right (exports, intra-EU) |
| 8 | Exempt sales without deduction right |
| 9 | Intra-EU acquisitions — base |
| 10 | Intra-EU acquisitions — IVA (output, self-assessed) |
| 16 | Other operations with IVA due by purchaser (reverse charge received) |
| 17 | IVA due on campo 16 |
| 20 | Total IVA due (sum of output fields) |
| 21 | Deductible IVA — immobilizado (capital goods) |
| 22 | Deductible IVA — existências (stock for resale) |
| 23 | Deductible IVA — other goods and services |
| 24 | Total deductible IVA |
| 40 | IVA to pay (if 20 > 24) |
| 41 | IVA credit (if 24 > 20) |

**Conservative defaults — Portugal-specific:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 23% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Portugal (Continental) |
| Unknown B2B vs B2C for EU customer | B2C, charge 23% |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU |
| Unknown blocked-input status | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction | €5,000 |
| HIGH tax-delta conservative default | €400 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net VAT position | €10,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period. Acceptable from: CGD (Caixa Geral de Depósitos), Millennium BCP, Santander Portugal, Novo Banco, BPI, ActivoBank, Banco CTT, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices (especially intra-EU and reverse charge), purchase invoices above €400, the client's NIF (9 digits, PT prefix for EU context).

**Ideal** — SAF-T (PT) extract from billing software, prior period Declaração Periódica, reconciliation of campo 41 credit.

**Refusal policy if minimum is missing — SOFT WARN.** Same pattern as Malta v2.0.

### Portugal-specific refusal catalogue

**R-PT-1 — Regime de isenção (Art. 53 CIVA).** *Trigger:* client under the small business exemption (turnover ≤ €14,500 or ≤ €15,000 depending on current threshold). *Message:* "Regime de isenção clients do not charge IVA and cannot recover input IVA. They do not file the Declaração Periódica. This skill covers the normal regime only."

**R-PT-2 — Partial exemption (pro rata / Art. 23 CIVA).** *Trigger:* both taxable and exempt supplies, non-de-minimis. *Message:* "Mixed taxable and exempt supplies require pro rata under Art. 23 CIVA. Please use a contabilista certificado."

**R-PT-3 — Margin scheme (regime da margem / Art. 50-A to 50-D).** *Trigger:* second-hand goods, art, antiques. *Message:* "Regime da margem requires per-item computation. Out of scope."

**R-PT-4 — VAT group (grupo de IVA).** *Trigger:* VAT group. *Message:* "Grupo de IVA requires consolidation. Out of scope."

**R-PT-5 — Fiscal representative.** *Trigger:* non-resident with fiscal representative. *Message:* "Non-resident with representante fiscal — out of scope."

**R-PT-6 — Madeira / Azores rates.** *Trigger:* client operates in Madeira or Azores. *Message:* "Madeira (22%/12%/5%) and Azores (16%/9%/4%) have different rate tables. This skill covers Continental Portugal rates only. Please use a contabilista certificado familiar with regional rates."

**R-PT-7 — Real estate (IVA imobiliário).** *Trigger:* property transactions. *Message:* "IVA on real estate is complex. Please use a contabilista certificado."

**R-PT-8 — Income tax instead of IVA.** *Trigger:* user asks about IRS/IRC instead of IVA. *Message:* "This skill handles Portuguese IVA only."

---

## Section 3 — Supplier pattern library (the lookup table)

Match by case-insensitive substring. If none match, fall through to Section 5.

### 3.1 Portuguese banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| CGD, CAIXA GERAL, CAIXA GERAL DE DEPOSITOS | EXCLUDE for bank charges | Financial service, exempt |
| MILLENNIUM BCP, BCP | EXCLUDE for bank charges | Same |
| SANTANDER PORTUGAL, SANTANDER PT | EXCLUDE for bank charges | Same |
| NOVO BANCO | EXCLUDE for bank charges | Same |
| BPI, BANCO BPI | EXCLUDE for bank charges | Same |
| ACTIVOBANK | EXCLUDE for bank charges | Same |
| BANCO CTT | EXCLUDE for bank charges | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for taxable subscriptions |
| JUROS, JURO | EXCLUDE | Interest, out of scope |
| EMPRESTIMO, CREDITO HABITACAO | EXCLUDE | Loan principal |

### 3.2 Portuguese government and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| PORTAL DAS FINANCAS, AT, AUTORIDADE TRIBUTARIA | EXCLUDE | Tax payment (IVA, IRS, IRC) |
| SEGURANCA SOCIAL | EXCLUDE | Social security contributions |
| FINANÇAS, DIRECAO GERAL | EXCLUDE | Tax authority |
| CONSERVATORIA, REGISTO COMERCIAL | EXCLUDE | Commercial registry |
| CAMARA MUNICIPAL | EXCLUDE | Municipal fees |
| IRN, INSTITUTO REGISTOS E NOTARIADO | EXCLUDE | Government registry |
| IAPMEI | EXCLUDE | Government agency |
| ALFANDEGA, DIREÇÃO-GERAL DAS ALFÂNDEGAS | EXCLUDE | Customs (check for import IVA) |

### 3.3 Portuguese utilities

| Pattern | Treatment | Campo | Notes |
|---|---|---|---|
| EDP, EDP ENERGIA, EDP COMERCIAL | Domestic 23% | 23 (input) | Electricity — standard rate |
| GALP, GALP ENERGIA | Domestic 23% | 23 | Energy/fuel |
| ENDESA PORTUGAL, IBERDROLA | Domestic 23% | 23 | Energy |
| EPAL, AGUAS DE PORTUGAL | Domestic 6% | 23 | Water at reduced rate |
| NOS, NOS COMUNICACOES | Domestic 23% | 23 | Telecoms — overhead |
| MEO, ALTICE PORTUGAL | Domestic 23% | 23 | Telecoms/broadband |
| VODAFONE PT, VODAFONE PORTUGAL | Domestic 23% | 23 | Telecoms |
| NOWO | Domestic 23% | 23 | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| FIDELIDADE | EXCLUDE | Insurance, exempt |
| AGEAS PORTUGAL, ALLIANZ PORTUGAL | EXCLUDE | Same |
| TRANQUILIDADE, GENERALI PT | EXCLUDE | Same |
| SEGURO, APOLICE | EXCLUDE | All insurance exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Campo | Notes |
|---|---|---|---|
| CTT (standard mail) | EXCLUDE for standard postage | | Universal service exempt |
| CTT (parcels, CTT Expresso) | Domestic 23% | 23 | Non-universal taxable |
| DHL EXPRESS PORTUGAL | Domestic 23% | 23 | Express courier |
| CHRONOPOST PORTUGAL | Domestic 23% | 23 | Express |
| FEDEX, UPS PORTUGAL | Domestic 23% | 23 | Courier |

### 3.6 Transport (Portugal domestic)

| Pattern | Treatment | Campo | Notes |
|---|---|---|---|
| CP, COMBOIOS DE PORTUGAL | Domestic 6% | 23 (input) | Rail at reduced rate |
| METRO LISBOA, METRO PORTO | Domestic 6% | 23 | Urban rail |
| CARRIS, CARRIS METROPOLITANA | Domestic 6% | 23 | Lisbon bus |
| STCP | Domestic 6% | 23 | Porto bus |
| UBER PT, UBER PORTUGAL | Domestic 6% (transport) | 23 | Ride-hailing |
| BOLT PT | Domestic 6% | 23 | Ride-hailing |
| TAXI | Domestic 6% | 23 | Local taxi |
| TAP AIR PORTUGAL (domestic) | Domestic 6% | 23 | Domestic flights reduced |
| TAP, RYANAIR, EASYJET (international) | EXCLUDE / 0% | | International flights exempt |
| BRISA, VIA VERDE | Domestic 23% | 23 | Motorway tolls |

### 3.7 Food retail (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| CONTINENTE, MODELO | Default BLOCK input VAT | Personal provisioning |
| PINGO DOCE, JERÓNIMO MARTINS | Default BLOCK | Same |
| LIDL, ALDI, INTERMARCHE | Default BLOCK | Same |
| MINIPREÇO, MERCADONA | Default BLOCK | Same |
| RESTAURANTE, PASTELARIA, CAFÉ | Default BLOCK | Entertainment — see 5.12 |

### 3.8 SaaS — EU suppliers (reverse charge / autoliquidação)

| Pattern | Billing entity | Campo | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 16/17 + 23 | Autoliquidação: output on 17, input on 23 |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 16/17 + 23 | Autoliquidação |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 16/17 + 23 | Autoliquidação |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 16/17 + 23 | Autoliquidação |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 16/17 + 23 | Autoliquidação |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | 16/17 + 23 | EU, autoliquidação |
| DROPBOX | Dropbox International Unlimited (IE) | 16/17 + 23 | Autoliquidação |
| SLACK | Slack Technologies Ireland Ltd (IE) | 16/17 + 23 | Autoliquidação |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 16/17 + 23 | EU, autoliquidação |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 16/17 + 23 | Autoliquidação |
| STRIPE (subscription) | Stripe Technology Europe Ltd (IE) | 16/17 + 23 | Transaction fees exempt — see 3.11 |

### 3.9 SaaS — non-EU suppliers (reverse charge / autoliquidação)

| Pattern | Billing entity | Campo | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — check | 16/17 + 23 | LU → EU autoliquidação |
| NOTION | Notion Labs Inc (US) | 16/17 + 23 | Non-EU autoliquidação |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 16/17 + 23 | Non-EU autoliquidação |
| OPENAI, CHATGPT | OpenAI Inc (US) | 16/17 + 23 | Non-EU autoliquidação |
| GITHUB | GitHub Inc (US) | 16/17 + 23 | Check IE entity |
| FIGMA | Figma Inc (US) | 16/17 + 23 | Non-EU |
| CANVA | Canva Pty Ltd (AU) | 16/17 + 23 | Non-EU |
| HUBSPOT | HubSpot Inc (US) or IE — check | 16/17 + 23 | Depends on billing entity |
| TWILIO | Twilio Inc (US) | 16/17 + 23 | Non-EU |

### 3.10 SaaS — the exception

| Pattern | Treatment | Why |
|---|---|---|
| AWS EMEA SARL | EU autoliquidação campo 16/17 + 23 (LU entity) | Standard EU treatment. If invoice shows Portuguese IVA, treat as domestic 23%. |

### 3.11 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (subscription) | EU autoliquidação 16/17 + 23 | IE entity |
| SUMUP, SQUARE, ZETTLE | Check invoice | If Portuguese: domestic 23%; if EU: autoliquidação |
| IFTHENPAY, EUPAGO | Check invoice | Portuguese payment processors — fees may be exempt |

### 3.12 Professional services (Portugal)

| Pattern | Treatment | Campo | Notes |
|---|---|---|---|
| CONTABILISTA, GABINETE CONTABILIDADE | Domestic 23% | 23 | Always deductible |
| ADVOGADO, ESCRITORIO ADVOCACIA | Domestic 23% | 23 | Business legal matters |
| NOTARIO, CARTORIO | Domestic 23% | 23 | Business notarial fees |
| SOLICITADOR | Domestic 23% | 23 | Legal practitioner |
| REVISOR OFICIAL DE CONTAS, ROC | Domestic 23% | 23 | Auditor |

### 3.13 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| SEGURANCA SOCIAL | EXCLUDE | Social security contributions |
| SALARIO, VENCIMENTO, REMUNERACAO | EXCLUDE | Wages |
| SUBSIDIO, SUBSIDIO FERIAS | EXCLUDE | Holiday/vacation pay |
| FUNDO COMPENSACAO, FCT | EXCLUDE | Compensation fund |

### 3.14 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| RENDA COMERCIAL, ARRENDAMENTO COMERCIAL | Domestic 23% | Commercial lease with IVA option (Art. 12 n.1 al. e CIVA) |
| RENDA, ARRENDAMENTO (residential) | EXCLUDE | Residential lease exempt |
| IMI, IMPOSTO MUNICIPAL | EXCLUDE | Property tax |
| AIMI | EXCLUDE | Additional property tax |

### 3.15 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFERENCIA INTERNA, MOVIMENTO INTERNO | EXCLUDE | Internal movement |
| DIVIDENDO | EXCLUDE | Out of scope |
| AMORTIZACAO EMPRESTIMO | EXCLUDE | Loan repayment |
| LEVANTAMENTO, LEVANTAMENTO ATM | TIER 2 — ask | Default exclude |
| REFORÇO DE CAPITAL, SUPRIMENTO | EXCLUDE | Owner injection / shareholder loan |

---

## Section 4 — Worked examples

Six fully worked classifications from a hypothetical Portugal-based self-employed IT consultant (trabalhador independente, normal IVA regime).

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
US entity. Non-EU autoliquidação under Art. 6 n.6 CIVA. Client self-assesses: output IVA on campo 17, input IVA deductible on campo 23. Net zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Campo (input) | Campo (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 3.38 | 23% | 23 | 16/17 | N | — | — |

### Example 2 — EU service, autoliquidação (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -850.00 ; EUR`

**Reasoning:**
IE entity — EU autoliquidação. Output IVA on campo 17, input IVA on campo 23. Net zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Campo (input) | Campo (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 195.50 | 23% | 23 | 16/17 | N | — | — |

### Example 3 — Entertainment, treatment in Portugal

**Input line:**
`15.04.2026 ; RESTAURANTE BELCANTO LISBOA ; DEBIT ; Business dinner ; -220.00 ; EUR`

**Reasoning:**
Restaurant. In Portugal, IVA on business meals (refeições de negócios) is generally deductible under Art. 21 n.1 al. d) CIVA, but only 50% deductible if they are considered despesas de representação (entertainment/representation expenses). The 50% limit applies to the IVA deduction (not just the income tax base). Default: block, flag for reviewer. If confirmed business with documentation → 50% IVA deductible.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Campo | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTAURANTE BELCANTO LISBOA | -220.00 | -220.00 | 0 | — | — | Y | Q1 | "Restaurant: IVA 50% deductible if despesas de representação. Confirm business purpose." |

### Example 4 — Capital goods (imobilizado)

**Input line:**
`18.04.2026 ; WORTEN (SONAE) ; DEBIT ; Laptop HP ; -1,595.00 ; EUR`

**Reasoning:**
€1,595 gross. In Portugal, assets used for >1 year and above a de minimis threshold are imobilizado (bens de investimento). Input IVA goes to campo 21 (IVA dedutível — imobilizado) rather than campo 23. Subject to regularisation over 5 years movable / 20 years immovable (Art. 24–26 CIVA).

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Campo | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | WORTEN | -1,595.00 | -1,296.75 | -298.25 | 23% | 21 | N | — | — |

### Example 5 — EU B2B service sale

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice PT-2026-018 IT consultancy ; +3,500.00 ; EUR`

**Reasoning:**
B2B services to Germany — place of supply is customer's country (Art. 6 n.6 al. a) CIVA / Art. 44 Directive). Report on campo 7 (operações isentas com direito a dedução). No output IVA. Verify German USt-IdNr on VIES.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Campo | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | 0% | 7 | Y | Q2 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6 — Motor vehicle, deduction rules

**Input line:**
`28.04.2026 ; ALD AUTOMOTIVE PORTUGAL ; DEBIT ; Lease payment VW Golf ; -450.00 ; EUR`

**Reasoning:**
Car lease. In Portugal, IVA on light passenger vehicles (viaturas ligeiras de passageiros) is generally NOT deductible (Art. 21 n.1 al. a) CIVA). Exceptions: taxis, driving schools, rental vehicles used in rental business, electric vehicles (50% deductible since 2020), hybrid plug-in vehicles (50% deductible). A VW Golf (non-electric) → blocked. If electric/hybrid → 50% deductible.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Campo | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | ALD AUTOMOTIVE PORTUGAL | -450.00 | -450.00 | 0 | — | — | Y | Q3 | "Viatura ligeira de passageiros: IVA blocked. Electric/hybrid (50% deductible)?" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 23% (Art. 18 n.1 al. c) CIVA)

Default rate for Continental Portugal. Sales → campo 1/2. Purchases → campo 23 (or 21/22).

### 5.2 Intermediate rate 13% (Art. 18 n.1 al. b), Lista II)

Restaurants (food + non-alcoholic drinks), diesel, certain food products (conserves, oils), wine, agricultural inputs. Sales → campo 3/4.

### 5.3 Reduced rate 6% (Art. 18 n.1 al. a), Lista I)

Basic foodstuffs (bread, milk, fruit, vegetables, fish, meat), water, books, medicines, passenger transport, hotels, cultural events. Sales → campo 5/6.

### 5.4 Zero rate and exempt with credit

Exports → campo 7. Intra-EU goods → campo 7. Intra-EU B2B services → campo 7.

### 5.5 Exempt without credit (Art. 9 CIVA)

Medical, education, insurance, financial services, residential rent, postal universal service. If significant → **R-PT-2 refuses**.

### 5.6 Local purchases

Input IVA on compliant fatura. Capital goods → campo 21. Stock → campo 22. Other → campo 23.

### 5.7 Autoliquidação — EU services (Art. 6 n.6)

EU service: base → campo 16, output IVA → campo 17, input → campo 23. Net zero.

### 5.8 Autoliquidação — EU goods (aquisições intracomunitárias)

EU goods: base → campo 9, output IVA → campo 10, input → campo 23/21.

### 5.9 Autoliquidação — non-EU

Non-EU: base → campo 16, output IVA → campo 17, input → campo 23.

### 5.10 Domestic reverse charge (Art. 2 n.1 al. i-j CIVA)

Portugal has domestic reverse charge for construction services (empreitadas de obras), scrap metal, and CO2 emission allowances. The acquirer self-assesses IVA.

### 5.11 Capital goods (bens de investimento)

Assets used >1 year → campo 21 for input IVA. Subject to regularização over 5 years (movable) or 20 years (immovable), Art. 24–26 CIVA.

### 5.12 Blocked/restricted input IVA (Art. 21 CIVA)

- Light passenger vehicles (viaturas ligeiras de passageiros): IVA blocked (Art. 21 n.1 al. a)). Exceptions: taxi, driving school, rental. Electric vehicles: 50% deductible. Hybrid plug-in: 50% deductible.
- Fuel: diesel for VP 50% deductible; GPL/electric 100% deductible. Petrol: NOT deductible for VP.
- Entertainment (despesas de representação): IVA 50% deductible (Art. 21 n.1 al. d)). This includes business meals — 50% of IVA, not full deduction.
- Travel and accommodation: IVA deductible if business-related and documented.
- Tobacco: not deductible.
- Personal use: not deductible.
- Gifts: IVA deductible only if ≤ 5 per mille of turnover and unit cost ≤ €50.

### 5.13 SAF-T (PT)

Portugal requires SAF-T (Standard Audit File for Tax) from all businesses using billing software. The SAF-T file must be submitted monthly to AT. It provides the most reliable data source for IVA classification. If available, prefer SAF-T data over bank statement.

### 5.14 Sales — local domestic

Charge 23%, 13%, or 6%. Map to campo 1/3/5 as appropriate.

### 5.15 Sales — cross-border B2C

Above €10,000 → **R-EU-5 OSS refusal fires**.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* GALP, REPSOL, BP, CEPSA. *Default:* blocked (VP default). *Question:* "Viatura ligeira or comercial? Electric/hybrid (50% IVA deductible)? Diesel for VP is 50% IVA deductible."

### 6.2 Restaurants and entertainment

*Pattern:* restaurante, pastelaria, café. *Default:* block. *Question:* "Business meal (despesas de representação)? IVA 50% deductible with documentation."

### 6.3 Ambiguous SaaS

*Default:* non-EU autoliquidação campo 16/17 + 23. *Question:* "Check invoice for legal entity."

### 6.4 Owner transfers

*Default:* exclude as suprimento/reforço. *Question:* "Customer payment, own money, or loan?"

### 6.5 Incoming from individuals

*Default:* domestic B2C 23%. *Question:* "Sale? Business or consumer?"

### 6.6 Foreign incoming

*Default:* domestic 23%. *Question:* "B2B with NIF, B2C, goods/services, country?"

### 6.7 Large purchases

*Default:* campo 21 if capital good. *Question:* "Confirm invoice total."

### 6.8 Mixed-use phone, internet

*Default:* 0%. *Question:* "Dedicated business or mixed?"

### 6.9 Outgoing to individuals

*Default:* exclude. *Question:* "Contractor, wages, refund, personal?"

### 6.10 Cash withdrawals

*Default:* exclude. *Question:* "What for?"

### 6.11 Rent

*Default:* no IVA (residential). *Question:* "Commercial with IVA option (Art. 12 n.1 al. e)?"

### 6.12 Foreign hotel

*Default:* exclude from input IVA. *Question:* "Business trip?"

### 6.13 Airbnb income

*Default:* [T2] flag. *Question:* "Alojamento Local registration? Duration? 6% reduced rate for accommodation?"

### 6.14 Construction reverse charge

*Pattern:* empreiteiro, construção civil. *Default:* [T2] flag. *Question:* "Construction subcontractor subject to domestic reverse charge?"

### 6.15 Platform sales

*Default:* if EU cross-border above €10,000 → R-EU-5. Otherwise domestic 23%. *Question:* "Sell outside Portugal?"

---

## Section 7 — Excel working paper template (Portugal-specific)

### Sheet "Transactions"

Column H accepts campo codes from Section 1.

### Sheet "Campo Summary"

```
| 1  | Sales 23% base | =SUMIFS(...) |
| 2  | IVA on sales 23% | =1*0.23 |
| 3  | Sales 13% base | =SUMIFS(...) |
| 4  | IVA on sales 13% | =3*0.13 |
| 5  | Sales 6% base | =SUMIFS(...) |
| 6  | IVA on sales 6% | =5*0.06 |
| 7  | Exempt with deduction right | =SUMIFS(...) |
| 9  | Intra-EU acquisitions base | =SUMIFS(...) |
| 10 | IVA on intra-EU | =9*0.23 |
| 16 | Other reverse charge base | =SUMIFS(...) |
| 17 | IVA on reverse charge | =16*0.23 |
| 20 | Total IVA due | =2+4+6+10+17 |
| 21 | Deductible IVA — imobilizado | =SUMIFS(input VAT, ..., "21") |
| 22 | Deductible IVA — existências | =SUMIFS(..., "22") |
| 23 | Deductible IVA — other | =SUMIFS(..., "23") |
| 24 | Total deductible IVA | =21+22+23 |
| 40 | IVA to pay | =MAX(0, 20-24) |
| 41 | IVA credit | =MAX(0, 24-20) |
```

### Mandatory recalc step

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/portugal-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Portuguese bank statement reading guide

**CSV format conventions.** Portuguese banks export CSV with semicolons and DD-MM-YYYY or DD/MM/YYYY dates. Common columns: Data, Descrição/Movimento, Débito, Crédito, Saldo. CGD and Millennium BCP use their own export formats.

**Portuguese language variants.** Renda (rent), salário/vencimento (salary), juros (interest), transferência (transfer), contribuições (contributions), fatura (invoice), reembolso (refund), depósito (deposit), levantamento (withdrawal).

**Internal transfers.** "Transferência interna", "movimento entre contas". Exclude.

**Portal das Finanças payments.** Tax payments appear as "AT", "FINANÇAS", "PAGAMENTO ESTADO". Always exclude.

**Segurança Social.** Social security contributions appear as monthly direct debits. Always exclude.

**SAF-T integration.** If SAF-T file is available, it provides structured invoice data including NIF of counterparties, IVA rates, and amounts. Prefer SAF-T data.

**Foreign currency.** Convert to EUR at ECB rate.

**IBAN prefix.** PT = Portugal. ES, IE, FR, DE = EU. US, GB, BR = non-EU.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type
*Inference:* LDA = company; Unipessoal/Sociedade = company; trabalhador independente = freelancer/sole trader. *Fallback:* "Trabalhador independente, LDA, or SA?"

### 9.2 IVA regime
*Fallback:* "Normal regime or regime de isenção (Art. 53)?"

### 9.3 NIF
*Fallback:* "Your NIF? (9 digits, PT prefix for EU)"

### 9.4 Filing period and frequency
*Fallback:* "Monthly (Vol. B) or quarterly (Vol. A)?"

### 9.5 Industry
*Fallback:* "What does the business do?"

### 9.6 Employees
*Inference:* Segurança Social outgoing. *Fallback:* "Employees?"

### 9.7 Exempt supplies
*Fallback:* "Any exempt sales?" *If yes → R-PT-2.*

### 9.8 Credit carried forward
*Always ask.* "IVA credit from prior period? (Campo 41)"

### 9.9 Cross-border customers
*Fallback:* "Customers outside Portugal? EU/non-EU? B2B/B2C?"

### 9.10 Madeira/Azores operations
*Conditional:* "Do you have operations in Madeira or Azores?" *If yes → R-PT-6 refuses.*

---

## Section 10 — Reference material

### Sources

1. Código do IVA (CIVA) — https://info.portaldasfinancas.gov.pt
2. RITI (Regime do IVA nas Transações Intracomunitárias) — D.L. 290/92
3. Declaração Periódica form and instructions — Portal das Finanças
4. SAF-T (PT) technical specifications — Portaria 302/2016
5. Council Directive 2006/112/EC — via eu-vat-directive companion
6. VIES — https://ec.europa.eu/taxation_customs/vies/

### Known gaps

1. Madeira/Azores rate tables not included (R-PT-6 refuses).
2. Construction domestic reverse charge flagged T2 only.
3. Electric/hybrid vehicle 50% IVA rule requires current vehicle classification.
4. Regime de isenção threshold (€14,500/€15,000) — verify current.
5. SAF-T integration is flagged but not automated.
6. Restaurant 50% IVA deduction for despesas de representação requires documentation.
7. Diesel 50% IVA deduction for VP is current — verify annually.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure.
- **v1.0/1.1:** Initial skill.

### Self-check (v2.0)

1. Quick reference: yes. 2. Supplier library (15): yes. 3. Worked examples (6): yes. 4. Tier 1 (15): yes. 5. Tier 2 (15): yes. 6. Excel template: yes. 7. Onboarding (10): yes. 8. 8 refusals: yes. 9. Reference: yes. 10. Vehicle block with EV/hybrid 50% exception: yes. 11. Restaurant 50% IVA deduction: yes. 12. SAF-T requirement mentioned: yes. 13. Continental vs Madeira/Azores rates: yes. 14. Three-rate structure (23/13/6): yes. 15. Non-EU autoliquidação campo 16/17: yes.

## End of Portugal VAT Return Skill v2.0

This skill is incomplete without BOTH companion files: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contabilista certificado, revisor oficial de contas, or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
