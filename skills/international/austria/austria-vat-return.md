---
name: austria-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for an Austrian VAT return (Umsatzsteuervoranmeldung / UVA) or annual declaration (Umsatzsteuererklärung / U1) for a self-employed individual or small business in Austria. Trigger on phrases like "prepare UVA", "Austrian VAT return", "Umsatzsteuer", "classify transactions for Austrian VAT", or any request involving Austria VAT filing. This skill covers Austria only, standard regime (Regelbesteuerung). Kleinunternehmerregelung, partial exemption, margin scheme (Differenzbesteuerung), and VAT groups (Organschaft) are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Austrian VAT work.
version: 2.0
---

# Austria VAT Return Skill (UVA / Umsatzsteuervoranmeldung) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Austria (Republik Österreich) |
| Standard rate | 20% |
| Reduced rates | 13% (cultural events, live animals, plants, firewood, certain food, domestic flights), 10% (food and non-alcoholic drinks, books, passenger transport, hotels, medicines, agriculture) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods) |
| Return form | UVA (Umsatzsteuervoranmeldung, monthly/quarterly); U1 (Umsatzsteuererklärung, annual) |
| Filing portal | https://finanzonline.bmf.gv.at (FinanzOnline) |
| Authority | Bundesministerium für Finanzen (BMF) / Finanzamt |
| Currency | EUR only |
| Filing frequencies | Monthly (turnover > €100,000 in prior year); Quarterly (turnover ≤ €100,000); Annual (U1, always) |
| Deadline | UVA: 15th of 2nd month after period end (e.g. January due 15 March); U1: 30 April (paper) or 30 June (electronic) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants contributors |
| Validation date | April 2026 |

**Key UVA Kennzahlen (the field codes you will use most):**

| KZ | Meaning |
|---|---|
| 000 | Total revenue (Gesamtbetrag der Bemessungsgrundlagen) |
| 001 | Intra-EU supplies of goods (steuerfreie Lieferungen, Art. 6 Abs 1) |
| 017 | Other tax-free revenues (with credit) |
| 021 | Intra-EU services provided (Art. 3a Abs 2) |
| 022 | Sales at 20% (Bemessungsgrundlage) |
| 029 | Sales at 10% |
| 006 | Sales at 13% |
| 037 | Sales at 19% (for Jungholz/Mittelberg only) |
| 057 | Reverse charge — construction subcontracting received (Bauleistungen, § 19 Abs 1a) |
| 060 | Reverse charge — other domestic (§ 19 Abs 1) |
| 065 | Intra-EU acquisitions (Art. 3 Abs 8) — 20% |
| 066 | Intra-EU acquisitions — 10% |
| 070 | Intra-EU acquisitions — new vehicles |
| 072 | Intra-EU services received (Art. 3a Abs 2) |
| 073 | Imports (Einfuhren) — since 2022 deferred |
| 060/065/072 | All have corresponding output USt lines |
| 083 | Total output VAT (Gesamtbetrag der geschuldeten USt) |
| 060 | Input VAT deductible (Gesamtbetrag der Vorsteuer) — actually KZ 060 is dual-use; see form |
| KZ 060 (Vorsteuer) | Total deductible input VAT |
| KZ 070 (Vorsteuern aus ig Erwerben) | Input VAT on intra-EU acquisitions |
| KZ 065 (USt ig Erwerb) | Output VAT on intra-EU acquisitions |
| 095 | Net payable (Zahllast) |
| 090 | Excess credit (Gutschrift) |

**Note on Austrian UVA form:** The Austrian UVA uses Kennzahlen (KZ) rather than sequential box numbers. The mapping is less intuitive than Malta's VAT3. Key principle: every reverse charge transaction has a base KZ and a corresponding output USt KZ, plus an input Vorsteuer KZ. For a fully taxable business, the net effect of reverse charge is zero.

**Conservative defaults — Austria-specific:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 20% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Austria |
| Unknown B2B vs B2C for EU customer | B2C, charge 20% |
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

**Minimum viable** — bank statement for the period. Acceptable from: Erste Bank, Raiffeisen, BAWAG, Bank Austria (UniCredit), Oberbank, Hypo banks, easybank, Revolut Business, Wise Business, N26, or any other.

**Recommended** — sales invoices (especially intra-EU and reverse charge), purchase invoices above €400, the client's UID-Nummer (ATU + 8 digits).

**Ideal** — complete invoice register, prior period UVA, reconciliation of credit (KZ 090).

### Austria-specific refusal catalogue

**R-AT-1 — Kleinunternehmerregelung.** *Trigger:* client under the small business exemption (turnover ≤ €35,000 net, § 6 Abs 1 Z 27 UStG). *Message:* "Kleinunternehmer are exempt from charging USt and cannot recover Vorsteuer. They do not file a UVA. This skill covers the Regelbesteuerung only. If you have opted in (Option zur Steuerpflicht), confirm."

**R-AT-2 — Partial exemption (Vorsteueraufteilung).** *Trigger:* both taxable and exempt supplies, non-de-minimis. *Message:* "Mixed taxable and exempt supplies require Vorsteueraufteilung under § 12 Abs 4–6 UStG. Please use a Steuerberater."

**R-AT-3 — Differenzbesteuerung (margin scheme).** *Trigger:* second-hand goods, art, antiques. *Message:* "Differenzbesteuerung requires per-item margin computation. Out of scope."

**R-AT-4 — Organschaft (VAT group).** *Trigger:* client is part of an Organschaft. *Message:* "Organschaft requires consolidation. Out of scope."

**R-AT-5 — Fiscal representative.** *Trigger:* non-resident with fiscal representative. *Message:* "Non-resident with fiscal representative — out of scope."

**R-AT-6 — Real estate (Grundstücksumsätze).** *Trigger:* property transactions subject to USt option. *Message:* "Grundstücksumsätze are complex. Please use a Steuerberater."

**R-AT-7 — Jungholz/Mittelberg special rate.** *Trigger:* client operates in Jungholz or Mittelberg (19% special rate). *Message:* "The Jungholz/Mittelberg 19% rate (KZ 037) requires specific handling. Flag for Steuerberater."

**R-AT-8 — Income tax instead of USt.** *Trigger:* user asks about Einkommensteuer, Körperschaftsteuer instead of USt. *Message:* "This skill handles Austrian USt (Umsatzsteuer) only."

---

## Section 3 — Supplier pattern library (the lookup table)

Match by case-insensitive substring. If none match, fall through to Section 5.

### 3.1 Austrian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ERSTE BANK, SPARKASSE | EXCLUDE for bank charges | Financial service, exempt |
| RAIFFEISEN, RAIFFEISENBANK | EXCLUDE for bank charges | Same |
| BAWAG, BAWAG PSK | EXCLUDE for bank charges | Same |
| BANK AUSTRIA, UNICREDIT AT | EXCLUDE for bank charges | Same |
| OBERBANK, BKS BANK, BTV | EXCLUDE for bank charges | Same |
| HYPO, HYPO TIROL, HYPO NOE | EXCLUDE for bank charges | Same |
| EASYBANK | EXCLUDE for bank charges | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for taxable subscriptions |
| ZINSEN, HABENZINSEN, SOLLZINSEN | EXCLUDE | Interest, out of scope |
| KREDIT, DARLEHEN | EXCLUDE | Loan principal |

### 3.2 Austrian government and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| FINANZAMT, FA, BMF | EXCLUDE | Tax payment (USt, ESt, KöSt) |
| FINANZONLINE | EXCLUDE | Tax portal payment |
| SVS, SOZIALVERSICHERUNG DER SELBST | EXCLUDE | Self-employed social insurance (SVS) |
| OEGK, OGK | EXCLUDE | Health insurance |
| AMS | EXCLUDE | Employment service |
| WKO, WIRTSCHAFTSKAMMER | EXCLUDE | Chamber of Commerce membership |
| GERICHT, BEZIRKSGERICHT | EXCLUDE | Court fees |
| GEMEINDE, MAGISTRAT | EXCLUDE | Municipal fees |
| FIRMENBUCH, LANDESGERICHT | EXCLUDE | Company register |

### 3.3 Austrian utilities

| Pattern | Treatment | KZ | Notes |
|---|---|---|---|
| WIEN ENERGIE | Domestic 20% | Vorsteuer (input) | Electricity/gas — standard rate |
| WIENER STADTWERKE | Domestic 20% | Vorsteuer | Utilities |
| EVN | Domestic 20% | Vorsteuer | Energy |
| ENERGIE AG, LINZ AG | Domestic 20% | Vorsteuer | Energy |
| SALZBURG AG, KELAG, TIWAG, ILLWERKE | Domestic 20% | Vorsteuer | Regional energy |
| A1 TELEKOM, A1, TELEKOM AUSTRIA | Domestic 20% | Vorsteuer | Telecoms — overhead |
| MAGENTA, T-MOBILE AUSTRIA | Domestic 20% | Vorsteuer | Telecoms |
| DREI, HUTCHISON DREI | Domestic 20% | Vorsteuer | Telecoms |
| WIENER WASSER, WASSERWERK | Domestic 10% | Vorsteuer | Water supply at reduced rate |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| WIENER STADTISCHE, VIENNA INSURANCE | EXCLUDE | Insurance, exempt |
| UNIQA, GENERALI AUSTRIA | EXCLUDE | Same |
| ALLIANZ AUSTRIA, ZURICH | EXCLUDE | Same |
| VERSICHERUNG, PRAEMIE | EXCLUDE | All insurance exempt |
| WUSTENROT | EXCLUDE | Building society/insurance |

### 3.5 Post and logistics

| Pattern | Treatment | KZ | Notes |
|---|---|---|---|
| OSTERREICHISCHE POST, POST AG (standard) | EXCLUDE for standard postage | | Universal service exempt |
| POST AG (parcels) | Domestic 20% | Vorsteuer | Non-universal taxable |
| DHL EXPRESS AUSTRIA | Domestic 20% | Vorsteuer | Express courier |
| DPD AUSTRIA, GLS AUSTRIA | Domestic 20% | Vorsteuer | Courier |

### 3.6 Transport (Austria domestic)

| Pattern | Treatment | KZ | Notes |
|---|---|---|---|
| OBB, OSTERREICHISCHE BUNDESBAHNEN | Domestic 10% | Vorsteuer | Rail at reduced rate |
| WESTBAHN | Domestic 10% | Vorsteuer | Rail |
| WIENER LINIEN | Domestic 10% | Vorsteuer | Vienna public transport |
| LINZ AG LINIEN, GRAZER LINIEN, IVB | Domestic 10% | Vorsteuer | Regional public transport |
| UBER AT, UBER AUSTRIA | Domestic 10% | Vorsteuer | Ride-hailing, transport rate |
| TAXI | Domestic 10% | Vorsteuer | Local taxi |
| AUSTRIAN AIRLINES (domestic) | Domestic 13% | Vorsteuer | Domestic flights at 13% |
| AUSTRIAN AIRLINES, RYANAIR (international) | EXCLUDE / 0% | | International flights exempt |
| ASFINAG | Domestic 20% | Vorsteuer | Motorway tolls (Vignette/GO-Box) |

### 3.7 Food retail (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| SPAR, INTERSPAR, EUROSPAR | Default BLOCK input VAT | Personal provisioning |
| BILLA, BILLA PLUS, MERKUR | Default BLOCK | Same |
| HOFER, LIDL, PENNY | Default BLOCK | Same |
| MPreis, UNIMARKT | Default BLOCK | Same |
| RESTAURANT, GASTHAUS, WIRTSHAUS, CAFE | Default BLOCK | Entertainment — see 5.12 |

### 3.8 SaaS — EU suppliers (reverse charge, Art. 3a Abs 2 / KZ 072)

| Pattern | Billing entity | KZ | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 072 + Vorsteuer | EU service reverse charge |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 072 + Vorsteuer | Same |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 072 + Vorsteuer | Same |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 072 + Vorsteuer | Same |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 072 + Vorsteuer | Same |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | 072 + Vorsteuer | EU reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | 072 + Vorsteuer | Same |
| SLACK | Slack Technologies Ireland Ltd (IE) | 072 + Vorsteuer | Same |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 072 + Vorsteuer | EU reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 072 + Vorsteuer | Same |
| STRIPE (subscription) | Stripe Technology Europe Ltd (IE) | 072 + Vorsteuer | Transaction fees exempt — see 3.11 |

### 3.9 SaaS — non-EU suppliers (reverse charge, § 19 Abs 1 / KZ 060)

| Pattern | Billing entity | KZ | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — check | 072 + Vorsteuer | LU → EU reverse charge |
| NOTION | Notion Labs Inc (US) | 060 + Vorsteuer | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 060 + Vorsteuer | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 060 + Vorsteuer | Non-EU reverse charge |
| GITHUB | GitHub Inc (US) | 060 + Vorsteuer | Check IE entity |
| FIGMA | Figma Inc (US) | 060 + Vorsteuer | Non-EU |
| CANVA | Canva Pty Ltd (AU) | 060 + Vorsteuer | Non-EU |
| HUBSPOT | HubSpot Inc (US) or IE — check | 060 or 072 | Depends on billing entity |
| TWILIO | Twilio Inc (US) | 060 + Vorsteuer | Non-EU |

### 3.10 SaaS — the exception

| Pattern | Treatment | Why |
|---|---|---|
| AWS EMEA SARL | EU reverse charge KZ 072 + Vorsteuer (LU entity) | Standard EU reverse charge. If invoice shows Austrian USt, treat as domestic 20%. |

### 3.11 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (subscription) | EU reverse charge KZ 072 | IE entity |
| SUMUP, SQUARE, ZETTLE | Check invoice | If Austrian: domestic 20%; if EU: reverse charge |

### 3.12 Professional services (Austria)

| Pattern | Treatment | KZ | Notes |
|---|---|---|---|
| STEUERBERATER, WIRTSCHAFTSPRUFER | Domestic 20% | Vorsteuer | Always deductible |
| RECHTSANWALT, ANWALTSKANZLEI | Domestic 20% | Vorsteuer | Business legal matters |
| NOTAR, NOTARIAT | Domestic 20% | Vorsteuer | Business notarial fees |
| UNTERNEHMENSBERATER, CONSULTANT | Domestic 20% | Vorsteuer | Consulting |
| BILANZBUCHHALTER | Domestic 20% | Vorsteuer | Bookkeeper |

### 3.13 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| SVS, SOZIALVERSICHERUNG | EXCLUDE | Self-employed social insurance |
| OEGK, GESUNDHEITSKASSE | EXCLUDE | Health insurance |
| GEHALT, LOHN, ENTGELT | EXCLUDE | Wages |
| MITARBEITERVORSORGEKASSE, MVK | EXCLUDE | Employee provident fund |
| BETRIEBLICHE VORSORGE | EXCLUDE | Pension |

### 3.14 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| BÜROMIETE, GESCHÄFTSLOKAL | Domestic 20% | Commercial lease with USt option |
| MIETE, WOHNUNGSMIETE (residential) | Domestic 10% or EXCLUDE | Residential rent at 10% if landlord is USt-pflichtig; otherwise exempt |
| GRUNDSTEUER | EXCLUDE | Property tax |
| GRUNDBUCH | EXCLUDE | Land register fee |

### 3.15 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| UMBUCHUNG, INTERN, EIGENUEBERWEISUNG | EXCLUDE | Internal movement |
| DIVIDENDE | EXCLUDE | Out of scope |
| KREDITRÜCKZAHLUNG, TILGUNG | EXCLUDE | Loan repayment |
| BEHEBUNG, BARABHEBUNG | TIER 2 — ask | Default exclude |
| PRIVATEINLAGE | EXCLUDE | Owner injection |

---

## Section 4 — Worked examples

Six fully worked classifications from a hypothetical Austria-based self-employed IT consultant (Einzelunternehmer, Regelbesteuerung).

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
US entity (Section 3.9). Non-EU reverse charge under § 19 Abs 1 UStG. Client self-assesses: output USt on KZ 060 area, input Vorsteuer deductible. Net zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ (input) | KZ (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 2.94 | 20% | Vorsteuer | 060 | N | — | — |

### Example 2 — EU service, reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -850.00 ; EUR`

**Reasoning:**
IE entity — EU service reverse charge (Art. 3a Abs 2 UStG). Output USt on KZ 072-related line, input Vorsteuer deductible. Net zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ (input) | KZ (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 170.00 | 20% | Vorsteuer | 072 | N | — | — |

### Example 3 — Entertainment, Bewirtung in Austria

**Input line:**
`15.04.2026 ; GASTHAUS PURSTNER WIEN ; DEBIT ; Business dinner ; -220.00 ; EUR`

**Reasoning:**
Restaurant. In Austria, Bewirtungsspesen (business entertainment) are partially deductible. The USt (Vorsteuer) on business meals is deductible if the meal is for a clearly documented business purpose. For income tax: 50% of the net amount is deductible. For USt (Vorsteuer): 100% of the USt is deductible on the portion that relates to business (which is typically 50% or 100% of the invoice depending on the nature). Practice: Vorsteuer is fully deductible on the entire invoice if the event is for business entertainment. Default: block, flag for reviewer.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | GASTHAUS PURSTNER WIEN | -220.00 | -220.00 | 0 | — | — | Y | Q1 | "Bewirtung: Vorsteuer deductible if business purpose documented. Confirm." |

### Example 4 — Capital goods (Anlagevermögen)

**Input line:**
`18.04.2026 ; DELL AUSTRIA GMBH ; DEBIT ; Laptop XPS 15 ; -1,595.00 ; EUR`

**Reasoning:**
€1,595 gross. In Austria, assets with acquisition cost > €1,000 net (since 2023 GWG threshold increase) are not GWG (geringwertige Wirtschaftsgüter) and must be capitalised. €1,595 / 1.20 = €1,329.17 > €1,000. This is Anlagevermögen. Vorsteuer fully deductible. Subject to Vorsteuerberichtigung over 5 years (movable) or 20 years (immovable) if use changes.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | DELL AUSTRIA GMBH | -1,595.00 | -1,329.17 | -265.83 | 20% | Vorsteuer | N | — | — |

### Example 5 — EU B2B service sale

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice AT-2026-018 IT consultancy ; +3,500.00 ; EUR`

**Reasoning:**
B2B services to Germany — place of supply is customer's country. Report on KZ 021 (innergemeinschaftliche Dienstleistungen erbracht). No output USt. Verify German USt-IdNr on VIES.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | 0% | 021 | Y | Q2 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6 — Motor vehicle, Vorsteuerabzug

**Input line:**
`28.04.2026 ; PORSCHE BANK LEASING ; DEBIT ; Lease payment VW Golf ; -550.00 ; EUR`

**Reasoning:**
Car lease. In Austria, Vorsteuer on passenger cars (PKW) is generally NOT deductible (§ 12 Abs 2 Z 2 lit b UStG). Exception: Fiskal-LKW (light commercial vehicles with specific characteristics — certain van models are published on the BMF list), taxis, driving school vehicles, rental vehicles. A VW Golf is a PKW, not a Fiskal-LKW. Default: blocked.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | KZ | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | PORSCHE BANK LEASING | -550.00 | -550.00 | 0 | — | — | Y | Q3 | "PKW: Vorsteuer blocked. Is this a Fiskal-LKW (BMF list)?" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 20% (§ 10 Abs 1 UStG)

Default rate. Sales → KZ 022. Purchases → Vorsteuer.

### 5.2 Reduced rate 10% (§ 10 Abs 2 UStG, Anlage 1)

Food and non-alcoholic drinks (dine-in and takeaway), books (print and digital), medicines, passenger transport, hotels (Beherbergung), agriculture. Sales → KZ 029. Purchases → Vorsteuer.

### 5.3 Reduced rate 13% (§ 10 Abs 3 UStG, Anlage 2)

Cultural events (museums, concerts, theatre, cinema), live animals, plants, firewood, certain foodstuffs (wine from producer), domestic flights. Sales → KZ 006.

### 5.4 Zero rate and exempt with credit

Exports → KZ 017. Intra-EU goods → KZ 001. Intra-EU B2B services → KZ 021.

### 5.5 Exempt without credit (§ 6 Abs 1 UStG)

Medical, education, insurance, financial services, residential rent (old buildings), postal universal service. If significant → **R-AT-2 refuses**.

### 5.6 Local purchases

Input Vorsteuer on compliant Rechnung. → Vorsteuer KZ.

### 5.7 Reverse charge — EU services (Art. 3a Abs 2 / § 19)

EU supplier → KZ 072 (base + output USt), Vorsteuer (input). Net zero.

### 5.8 Reverse charge — EU goods (innergemeinschaftlicher Erwerb)

EU goods → KZ 065 (base + output USt at 20%), Vorsteuer (input). Also KZ 066 for 10% goods.

### 5.9 Reverse charge — non-EU

Non-EU → KZ 060 (base + output USt), Vorsteuer (input).

### 5.10 Reverse charge — Bauleistungen (§ 19 Abs 1a)

Austria has a domestic reverse charge for construction services (Bauleistungen). The recipient self-assesses via KZ 057. Subcontractor invoices without USt. This is important for the Austrian construction sector.

### 5.11 Capital goods

GWG threshold: €1,000 net (since 2023). Above → Anlagevermögen. Vorsteuerberichtigung: 5 years movable, 20 years immovable.

### 5.12 Blocked Vorsteuer (§ 12 Abs 2 UStG)

- PKW (passenger cars): Vorsteuer fully blocked unless Fiskal-LKW (on BMF list), taxi, driving school, car rental. No partial deduction (unlike Italy's 40%).
- Fuel for PKW: blocked (follows vehicle).
- Fuel for Fiskal-LKW: deductible.
- Entertainment (Bewirtung): Vorsteuer IS deductible for business entertainment in Austria (unlike Malta's hard block). Income tax: 50% deductible. USt: full Vorsteuer if business purpose.
- Gifts: Vorsteuer blocked if > €40 per recipient per year.
- Personal use: not deductible.
- Tobacco: not deductible.

### 5.13 Residential rent at 10%

Residential rent in Austria can be subject to 10% USt (older buildings) or 20% (newer buildings post-2012, if landlord opts). Some residential rent is exempt. The treatment depends on building age and landlord election. Default: [T2] flag if uncertain.

### 5.14 Sales — local domestic

Charge 20%, 10%, or 13%. Map to KZ 022/029/006.

### 5.15 Sales — cross-border B2C

Above €10,000 → **R-EU-5 OSS refusal**.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* OMV, BP, SHELL, AVIA, ENI, JET. *Default:* blocked (PKW default). *Question:* "PKW or Fiskal-LKW (BMF list)?"

### 6.2 Restaurants and entertainment

*Pattern:* Gasthaus, Restaurant, Wirtshaus. *Default:* block (conservative). *Question:* "Bewirtung with business purpose? Vorsteuer deductible if documented."

### 6.3 Ambiguous SaaS

*Default:* non-EU reverse charge KZ 060. *Question:* "Check invoice for legal entity."

### 6.4 Owner transfers

*Default:* exclude as Privateinlage. *Question:* "Customer payment, own money, or loan?"

### 6.5 Incoming from individuals

*Default:* domestic B2C 20%. *Question:* "Sale?"

### 6.6 Foreign incoming

*Default:* domestic 20%. *Question:* "B2B with UID, B2C, goods/services, country?"

### 6.7 Large purchases

*Default:* if net > €1,000 → Anlagevermögen. *Question:* "Confirm invoice total."

### 6.8 Mixed-use phone, internet

*Default:* 0%. *Question:* "Dedicated business or mixed?"

### 6.9 Outgoing to individuals

*Default:* exclude. *Question:* "Contractor, wages, refund, personal?"

### 6.10 Cash withdrawals

*Default:* exclude. *Question:* "What for?"

### 6.11 Rent

*Default:* [T2] flag (10% or 20% or exempt uncertain). *Question:* "Commercial or residential? Building age? USt charged?"

### 6.12 Foreign hotel

*Default:* exclude from Vorsteuer. *Question:* "Business trip?"

### 6.13 Airbnb income

*Default:* [T2] flag. *Question:* "Duration? Beherbergung at 10%?"

### 6.14 Bauleistungen reverse charge

*Pattern:* Bauunternehmen, construction. *Default:* [T2] flag. *Question:* "Construction subcontractor subject to § 19 Abs 1a Bauleistungen reverse charge?"

### 6.15 Platform sales

*Default:* if EU cross-border above €10,000 → R-EU-5. Otherwise domestic 20%. *Question:* "Sell outside Austria?"

---

## Section 7 — Excel working paper template (Austria-specific)

### Sheet "Transactions"

Column H accepts Kennzahl codes from Section 1.

### Sheet "KZ Summary"

```
| 022 | Sales 20% base | =SUMIFS(...) |
| 029 | Sales 10% base | =SUMIFS(...) |
| 006 | Sales 13% base | =SUMIFS(...) |
| 001 | Intra-EU goods | =SUMIFS(...) |
| 021 | Intra-EU services provided | =SUMIFS(...) |
| 065 | Intra-EU acquisitions base | =SUMIFS(...) |
| 072 | EU services received base | =SUMIFS(...) |
| 060 | Non-EU reverse charge base | =SUMIFS(...) |
| 083 | Total output USt | =022*0.20 + 029*0.10 + 006*0.13 + USt on RC |
| Vorsteuer | Total deductible Vorsteuer | =SUM(input lines) |
| 095 | Zahllast (payable) | =MAX(0, 083-Vorsteuer) |
| 090 | Gutschrift (credit) | =MAX(0, Vorsteuer-083) |
```

### Mandatory recalc step

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/austria-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Austrian bank statement reading guide

**CSV format conventions.** Austrian banks export CSV with semicolons and DD.MM.YYYY dates. Common columns: Buchungsdatum, Umsatztext/Verwendungszweck, Betrag, Saldo. Erste Bank uses CAMT format; Raiffeisen varies by regional bank.

**German language variants.** Miete (rent), Gehalt/Lohn (salary), Zinsen (interest), Überweisung (transfer), Beiträge (contributions), Rechnung (invoice), Rückzahlung/Gutschrift (refund), Einzahlung (deposit), Behebung/Abhebung (withdrawal).

**Internal transfers.** "Umbuchung", "Eigenüberweisung". Exclude.

**Finanzamt payments.** Tax payments appear as "FINANZAMT" with an Abgabenkontonummer. Always exclude.

**SVS payments.** Self-employed social insurance (SVS) appears as quarterly direct debits. Always exclude — not a VATable supply.

**Foreign currency.** Convert to EUR at ECB rate.

**IBAN prefix.** AT = Austria. DE, NL, IE = EU. US, GB, CH = non-EU. Note: CH (Switzerland) is non-EU — important for Austrian businesses near the Swiss border.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type
*Inference:* GmbH = company; Einzelunternehmer/e.U. = sole trader; KG/OG = partnership. *Fallback:* "Einzelunternehmer, GmbH, or KG?"

### 9.2 USt regime
*Fallback:* "Regelbesteuerung or Kleinunternehmerregelung?"

### 9.3 UID-Nummer
*Fallback:* "Your UID-Nummer? (ATU + 8 digits)"

### 9.4 Filing period
*Fallback:* "Which month or quarter?"

### 9.5 Industry
*Fallback:* "What does the business do?"

### 9.6 Employees
*Inference:* Gehalt outgoing. *Fallback:* "Employees?"

### 9.7 Exempt supplies
*Fallback:* "Any exempt sales?" *If yes → R-AT-2.*

### 9.8 Credit carried forward
*Always ask.* "USt credit from prior period? (KZ 090)"

### 9.9 Cross-border customers
*Fallback:* "Customers outside Austria? EU/non-EU? B2B/B2C?"

### 9.10 Construction
*Conditional:* "In construction? (Bauleistungen reverse charge may apply.)"

---

## Section 10 — Reference material

### Sources

1. Umsatzsteuergesetz 1994 (UStG) — https://www.ris.bka.gv.at
2. Umsatzsteuerrichtlinien (UStR) 2000 — BMF guidance
3. BMF Fiskal-LKW list — updated periodically
4. FinanzOnline UVA form and instructions — https://finanzonline.bmf.gv.at
5. Council Directive 2006/112/EC — via eu-vat-directive companion
6. VIES — https://ec.europa.eu/taxation_customs/vies/

### Known gaps

1. Fiskal-LKW list not reproduced — reference BMF publication.
2. Bauleistungen reverse charge flagged T2 only.
3. Residential rent rate (10%/20%/exempt) depends on building age — simplified.
4. GWG threshold (€1,000 net since 2023) — verify annually.
5. Jungholz/Mittelberg 19% rate refused entirely.
6. Bewirtung Vorsteuer deductibility requires documentation — flagged.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure.
- **v1.0/1.1:** Initial skill.

### Self-check (v2.0)

1. Quick reference: yes. 2. Supplier library (15): yes. 3. Worked examples (6): yes. 4. Tier 1 (15): yes. 5. Tier 2 (15): yes. 6. Excel template: yes. 7. Onboarding (10): yes. 8. 8 refusals: yes. 9. Reference: yes. 10. PKW block vs Fiskal-LKW: yes. 11. Bewirtung deductible (Austria vs Malta): yes. 12. Bauleistungen § 19 Abs 1a: yes. 13. KZ system: yes. 14. GWG threshold: yes. 15. Non-EU reverse charge KZ 060: yes.

## End of Austria VAT Return Skill v2.0

This skill is incomplete without BOTH companion files: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater, Wirtschaftsprüfer, or equivalent licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
