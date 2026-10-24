---
name: germany-vat-return
description: "Use this skill whenever asked to prepare, review, or classify transactions for a German VAT return (Umsatzsteuer-Voranmeldung / UStVA) for a self-employed individual or very small business operating under the Regelbesteuerung in Germany. Trigger on phrases like \"prepare VAT return\", \"do the German VAT\", \"fill in UStVA\", \"create the return\", \"Umsatzsteuer\", \"Vorsteuer\", or any request involving German VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Germany only and only Regelbesteuerung (standard taxation). Organschaft and Differenzbesteuerung are in the refusal catalogue; Kleinunternehmer, partial exemption and Ist-Versteuerung are handled in de-vat-annual-and-special-schemes. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any German VAT work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/germany-vat-return"
  jurisdiction: "DE"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# German VAT return: the Umsatzsteuer-Voranmeldung

How to read a German bank statement, classify each line for VAT and fill in the advance VAT
return (Umsatzsteuer-Voranmeldung, UStVA, form USt 1 A) for a self-employed person or very small
business on the normal scheme (Regelbesteuerung). Figures are for tax year 2026. Every box
number (Kennzahl, Kz) comes from the official 2026 form and its instructions, published by the
Federal Ministry of Finance on 29 December 2025: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=2

## Section 1: Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Germany (Federal Republic of Germany) |
| Return form | Umsatzsteuer-Voranmeldung, form USt 1 A, with form USt 1 H for the filing extension |
| Filing portal | Electronic transmission is the rule (§ 18(1) UStG). The tax office may allow paper only to avoid hardship. https://www.elster.de |
| Authority | The local Finanzamt. The Bundeszentralamt fuer Steuern handles the USt-IdNr and the recapitulative statement: https://www.bzst.de |
| Currency | EUR only. Tax bases in whole euros, no cents; tax amounts carry cents |
| Deadline | The tenth day after the end of the return period, and the payment is due the same day (§ 18(1) UStG) |
| Filing extension | One month longer, on application (§ 46 UStDV). A monthly filer must also declare and pay a Sondervorauszahlung of one eleventh of the previous year's advance payments (§ 47, § 48(2) UStDV); a quarterly filer pays none |
| Annual declaration | Umsatzsteuererklaerung, due seven months after the calendar year ends (§ 149(2) AO), or by the last day of February of the second following year when a Steuerberater files it (§ 149(3) AO) |
| Companion Guides | `vat-workflow-base` (workflow) and `eu-vat-directive` (EU directive content) |
| Scope | Regelbesteuerung, advance returns. Organschaft and Differenzbesteuerung are refused: Section 2. Kleinunternehmer, partial exemption and Ist-Versteuerung go to de-vat-annual-and-special-schemes |

**VAT rates on the 2026 return**

| What | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=2 |
| Standard rate, § 12(1) UStG. Sales go in Kz 81 | 19% | Form USt 1 A line 13: "zum Steuersatz von 19 %" |
| Reduced rate, § 12(2) UStG. Sales go in Kz 86 | 7% | Form USt 1 A line 14: "zum Steuersatz von 7 %". The statute itself prints this rate in words, "sieben Prozent" |
| Zero rate for solar supplies, § 12(3) UStG. Sales go in Kz 87 | 0% | Form USt 1 A line 15: "zum Steuersatz von 0 %" |

The rates are set by § 12 UStG: https://www.gesetze-im-internet.de/ustg_1980/__12.html
The zero rate is a rate, not an exemption, so the supplier keeps full input deduction: rule 5.12.

**Average rates for farming and forestry businesses (§ 24 UStG), outside the scope of this Guide**

| What | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__24.html |
| Forestry products other than sawmill products | 5.5% | § 24(1) sentence 1 no. 1 UStG: "auf 5,5 Prozent" |
| Remaining supplies under the scheme | 7.8% | § 24(1) sentence 1 no. 3 UStG: "auf 7,8 Prozent der Bemessungsgrundlage" |

These rates are reviewed yearly and may be changed by regulation (§ 24(5) UStG).

**Key UStVA Kennzahlen for 2026**

Kennzahlen move between years. These are read off the 2026 form and its instructions.

| Line | Kz | What goes in it |
| --- | --- | --- |
| Source | all figures below | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=2 |
| 13 | 81 | Taxable supplies at the standard rate, net base |
| 14 | 86 | Taxable supplies at the reduced rate, net base |
| 15 | 87 | Taxable supplies at the zero rate of § 12(3) UStG (solar), net base |
| 16 | 35 and 36 | Supplies at other tax rates: net base in Kz 35, the tax entered by hand in Kz 36 |
| 17, 18 | 77, then 76 and 80 | Supplies of a farming or forestry business under § 24 UStG. Out of scope here |
| 19 | 41 | Intra-Community supplies of goods to a customer with a USt-IdNr |
| 20, 21 | 44, 49 | New vehicles: to a customer without a USt-IdNr, and supplied outside a business |
| 22 | 43 | Other tax-free supplies WITH input deduction: exports, § 4 nos. 2 to 7 UStG |
| 23 | 48 | Tax-free WITHOUT input deduction: § 4 nos. 8 to 29 UStG, and a Kleinunternehmer's supplies |
| 24 | 91 | Tax-free intra-Community acquisitions (§§ 4b and 25c UStG) |
| 25 | 89 | Taxable intra-Community acquisitions at the standard rate, net base |
| 26 | 93 | Taxable intra-Community acquisitions at the reduced rate, net base |
| 27 | 90 | Taxable intra-Community acquisitions at the zero rate of § 12(3) UStG |
| 28, 29 | 95 and 98, 94 and 96 | Acquisitions at other rates; new vehicles from a supplier without a USt-IdNr |
| 30 | 46 and 47 | Reverse charge on § 3a(2) services from a business established in the REST OF THE EU (§ 13b(1) UStG): base in Kz 46, tax in Kz 47 |
| 31 | 73 and 74 | Reverse charge on supplies inside the real estate transfer tax act (§ 13b(2) no. 3 UStG) |
| 32 | 84 and 85 | Reverse charge on everything else (§ 13b(2) nos. 1, 2 and 4 to 12 UStG): works supplies and any other service of a business established ABROAD that does not belong in line 30, so this is the line for a supplier outside the EU, plus the domestic categories. Base in Kz 84, tax in Kz 85 |
| 33 | 42 | Your supplies as the first customer in an intra-Community triangular transaction (§ 25b UStG) |
| 34 | 60 | Your own supplies on which the customer owes the tax (§ 13b(5) UStG) |
| 35 | 21 | Your own § 3a(2) services to the rest of the EU on which the customer there owes the tax. Also go in the recapitulative statement |
| 36 | 45 | Your other non-taxable supplies whose place of supply is not Germany |
| 37 | none | Output VAT: the sum of lines 13 to 18 and 25 to 32 |
| 38 | 66 | Input VAT from other businesses' invoices |
| 39 | 61 | Input VAT on intra-Community acquisitions |
| 40 | 62 | Import VAT that has arisen: the box for Einfuhrumsatzsteuer |
| 41 | 67 | Input VAT on reverse-charge supplies under § 13b UStG |
| 42, 43 | 63, 59 | Input VAT by general average rates (§ 23a UStG), and the § 15(4a) UStG cases |
| 44, 45 | 64, none | Adjustment of input VAT (§ 15a UStG); then line 37 less lines 38 to 44 |
| 46 | 65 | Tax from a change of taxation method, and after-tax on advance payments at an older rate. NOT the payment line |
| 47 | 69 | Tax shown wrongly or without authority on an invoice (§ 14c UStG) |
| 48, 49 | none, 39 | The advance payment or surplus (lines 45 to 47); then the Sondervorauszahlung credit, normally only in the last return of the year |
| 50 | 83 | The amount to pay, or the surplus with a minus sign in front. The bottom line. Always fill it in |
| 51, 52 | 50, 37 | Extra information, only where an agreed fee has become UNCOLLECTIBLE (§ 17(2) Nr. 1 sentence 1 UStG): the reduction of the tax base already in lines 13 to 18, and the reduction of input VAT already in lines 38, 42 and 43. Not for ordinary credit notes or discounts |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | The standard rate |
| Unknown VAT status of a purchase | Not deductible (no Vorsteuerabzug) |
| Unknown counterparty country | Domestic Germany |
| Unknown business or consumer status of an EU customer | Consumer, charge German VAT at the standard rate |
| Unknown business-use proportion (vehicle, phone, home office) | No recovery |
| Unknown SaaS billing entity | Reverse charge from a supplier established abroad, Kz 84 and 85 |
| Unknown blocked-input status (gifts, private use) | Blocked |
| Unknown whether transaction is in scope | In scope |
| Unknown Bewirtung documentation status | Block (treat as undocumented, no recovery) |

**Red flag thresholds**

Review prompts for the preparer, not rules of law. Set the money figures with the client and
the reviewer, in proportion to the size of the business.

| Flag | Raise it when |
| --- | --- |
| HIGH single-transaction size | One line is large next to the period's turnover |
| HIGH tax-delta on a single conservative default | One default decides a material part of the return |
| MEDIUM counterparty concentration | One counterparty dominates the output or the input side |
| MEDIUM conservative-default count | Several defaults are carried in one return |
| LOW absolute net VAT position | The net position is large for this client |

## Section 2: Required inputs and refusal catalogue

### Required inputs

**Minimum viable.** The bank statement (Kontoauszug) for the period as CSV, PDF or pasted text, covering the whole filing period. Any German or international business bank is fine.

**Recommended.** Sales invoices for the period, especially for intra-EU services and tax-free supplies; purchase invoices for every input VAT claim, since the small-amount relief of § 33 UStDV stops at the invoice total in the thresholds tables and above it the full § 14 UStG details are needed; and the client's USt-IdNr or Steuernummer in writing.

**Ideal.** A complete invoice register, the EUeR or BWA, the previous period's UStVA, the Dauerfristverlaengerung status and the Sondervorauszahlung amount.

**Refusal policy if the minimum is missing: SOFT WARN.** With no bank statement at all, stop. With a statement but no invoices, proceed and record in the reviewer brief: "This UStVA was produced from the Kontoauszug alone. Before approval the reviewer must check that the input VAT claims are supported by invoices meeting § 14 UStG, that the small-amount relief of § 33 UStDV was used only within its limit, and that every reverse-charge classification matches the supplier's invoice."

### Germany-specific refusal catalogue

These sit on top of the EU-wide refusals in `eu-vat-directive` Section 13. R-DE-2 and R-DE-3 are refusals: if one fires, stop, give the message verbatim and end. R-DE-1, R-DE-4 and R-DE-5 are pointers to de-vat-annual-and-special-schemes.

- **R-DE-1: Kleinunternehmer § 19 UStG (pointer, not a refusal).** Trigger: the client is a Kleinunternehmer, or prior-year turnover was within EUR 25,000 and current-year turnover will stay within EUR 100,000 and the status has not been given up. Action: stop this skill and use [de-vat-annual-and-special-schemes](de-vat-annual-and-special-schemes.md), which covers the § 19 limits, the first year, losing the status mid-year, the waiver, the filing exemption and its exceptions (§ 149(1) sentence 2 AO, § 18(4a) UStG), and the EU scheme. Where a Kleinunternehmer owes reverse-charge tax on a service from abroad, the advance return for that period is due under § 18(4a) UStG, with the tax in lines 30 to 32 and no input deduction.
- **R-DE-2: Organschaft (VAT group).** Trigger: client is part of a VAT group (Organschaft) under § 2(2) Nr. 2 UStG, or asks about group registration. Message: "An Organschaft is one taxable person. Supplies inside the group are not taxable, and the Organtraeger files one UStVA for the whole group. This needs a Steuerberater. Out of scope."
- **R-DE-3: Differenzbesteuerung (margin scheme).** Trigger: client deals in second-hand goods, art, antiques, or collectables under the margin scheme (§ 25a UStG). Message: "The margin scheme needs a margin worked out transaction by transaction under § 25a UStG. Out of scope."
- **R-DE-4: Partial exemption (pointer, not a refusal).** Trigger: client makes both taxable supplies and exempt-without-credit supplies (§ 4 Nr. 8 to 29 UStG) and the exempt proportion is not de minimis. Action: apportion the input VAT under § 15(4) UStG with [de-vat-annual-and-special-schemes](de-vat-annual-and-special-schemes.md), which sets out direct allocation, the estimate, the turnover key, the floor-area rule for buildings, the final key in the annual return and § 15a corrections.
- **R-DE-5: Ist-Versteuerung (pointer, not a refusal).** Trigger: client uses cash-basis accounting (Ist-Versteuerung under § 20 UStG). Action: use [de-vat-annual-and-special-schemes](de-vat-annual-and-special-schemes.md) for the conditions, the timing of output tax on receipt, input tax on the invoice, and the change between methods; the box mapping in this skill still applies.

## Section 3: Supplier pattern library (the lookup table)

The deterministic pre-classifier. Where a counterparty matches a pattern, apply the treatment directly: the table is authoritative for the patterns it covers, with one exception. In Sections 3.8, 3.9 and 3.10 the billing entity named is only the usual one, and no official page prints it. The 2026 form sends a supplier in the rest of the EU and a supplier outside the EU to different boxes, so the entity on the INVOICE decides, not the table: rule 6.5 and Known gap 4.

**How to read it.** Match case-insensitively on the counterparty name in the Kontoauszug. Where several patterns match, take the most specific. Where none match, fall through to Section 5.

### 3.1 German banks (fees exempt: exclude)

**3.1 German banks table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DEUTSCHE BANK | EXCLUDE | Exempt financial service, § 4 Nr.  8 UStG |
| SPARKASSE, SPK, KREISSPARKASSE, STADTSPARKASSE | EXCLUDE | Same |
| COMMERZBANK, COBA | EXCLUDE | Same |
| ING, ING-DIBA | EXCLUDE | Same |
| N26, NUMBER26 | EXCLUDE | Same |
| DKB, DEUTSCHE KREDITBANK | EXCLUDE | Same |
| VOLKSBANK, RAIFFEISENBANK, VR BANK | EXCLUDE | Same |
| POSTBANK | EXCLUDE | Same |
| REVOLUT, WISE (fee lines) | EXCLUDE | Check for separate taxable subscription invoices |
| ZINSEN, ZINSERTRAG, HABENZINSEN | EXCLUDE | Interest, out of scope |
| DARLEHEN, KREDIT, TILGUNG | EXCLUDE | Loan principal, out of scope |
| KONTOGEBÜHR, KONTOFÜHRUNG, ENTGELT | EXCLUDE | Account fee, exempt |

### 3.2 German government, regulators, and statutory bodies (exclude entirely)

**3.2 German government table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| FINANZAMT, FA | EXCLUDE | Tax payment, not a supply |
| BUNDESKASSE, BUNDESZENTRALAMT | EXCLUDE | Federal treasury or BZSt, tax payment |
| IHK, INDUSTRIE- UND HANDELSKAMMER | EXCLUDE | Chamber fee, sovereign act |
| HWK, HANDWERKSKAMMER | EXCLUDE | Trades chamber fee, sovereign act |
| GEZ, RUNDFUNKBEITRAG, BEITRAGSSERVICE | EXCLUDE | Broadcasting levy, not a supply |
| GEWERBEAMT, ORDNUNGSAMT, STADTVERWALTUNG | EXCLUDE | Government fee, sovereign act |
| BERUFSGENOSSENSCHAFT, BG | EXCLUDE | Statutory accident insurance |
| ZOLLAMT, ZOLL | EXCLUDE for duties. Import VAT may be recoverable in Kz 62: flag for the reviewer | |

### 3.3 German utilities

**3.3 German utilities table**

| Pattern | Treatment | Kz | Notes |
| --- | --- | --- | --- |
| STADTWERKE | Domestic 19% | 66 | Electricity, gas, water |
| TELEKOM, DEUTSCHE TELEKOM, T-MOBILE | Domestic 19% | 66 | Telecoms and broadband |
| VODAFONE, VODAFONE DEUTSCHLAND | Domestic 19% | 66 | Telecoms |
| O2, TELEFONICA DEUTSCHLAND | Domestic 19% | 66 | Telecoms |
| 1&1, UNITED INTERNET | Domestic 19% | 66 | Internet/hosting |
| CONGSTAR, ALDI TALK, SIMYO | Domestic 19% | 66 | Mobile |
| STROM, GAS, ENERGIEVERSORGUNG, E.ON, RWE, VATTENFALL, ENBW | Domestic 19% | 66 | Energy supplier |

### 3.4 German insurance (exempt: exclude)

**3.4 German insurance table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ALLIANZ | EXCLUDE | Exempt insurance, § 4 Nr.  10 UStG |
| HUK-COBURG, HUK COBURG | EXCLUDE | Same |
| DEVK | EXCLUDE | Same |
| AXA VERSICHERUNG, ZURICH, ERGO, GENERALI | EXCLUDE | Same |
| VERSICHERUNG, VERSICHERUNGSBEITRAG | EXCLUDE | All premiums exempt |
| KRANKENVERSICHERUNG (private, e.g. DKV, DEBEKA) | EXCLUDE | Exempt |

### 3.5 German transport

**3.5 German transport table**

| Pattern | Treatment | Kz | Notes |
| --- | --- | --- | --- |
| DB, DEUTSCHE BAHN | Reduced rate for rail tickets | 66 | Rail: reduced-rated with no distance limit (§ 12(2) Nr. 10 a UStG) |
| BVG, MVG, MVV, RMV, VBB, KVB, SSB, VRS, HVV | Reduced rate | 66 | Local scheduled transport, within a municipality or not more than 50 kilometres |
| UBER, FREENOW, BOLT (DE) | Standard rate | 66 | A platform fee is standard-rated. A licensed taxi ride within a municipality or up to 50 kilometres is reduced-rated; hire car with driver is not |
| ADAC | Standard rate for membership and services | 66 | Not insurance: the membership is taxable |
| FLIXTRAIN | Reduced rate | 66 | Rail, so reduced-rated with no distance limit |
| FLIXBUS | Standard rate for a journey over 50 kilometres | 66 | Scheduled road transport is reduced-rated only within one municipality or up to 50 kilometres (§ 12(2) Nr. 10 b UStG) |
| SIXT, EUROPCAR, ENTERPRISE, AVIS (car rental DE) | Standard rate | 66 | Vehicle rental; business use portion only |

### 3.6 German food/supermarkets (blocked unless hospitality)

**3.6 German food/supermarkets table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ALDI, ALDI SUED, ALDI NORD | Default BLOCK input VAT | Personal provisioning. Deductible only where food is stock in trade |
| LIDL | Default BLOCK | Same |
| REWE | Default BLOCK | Same |
| EDEKA | Default BLOCK | Same |
| DM, ROSSMANN, MUELLER DROGERIE | Default BLOCK | Personal care, not business by default |
| PENNY, NETTO, KAUFLAND, REAL | Default BLOCK | Same |
| RESTAURANT, GASTSTÄTTE, IMBISS (any named) | From 2026: food at the reduced rate, drinks at the standard rate. Recoverable only if the Bewirtungsbeleg is complete | § 12(2) Nr. 15 UStG covers restaurant and catering services but not drinks, so one receipt can carry both rates. Rule 5.3 has the documentation |

### 3.7 German rent

**3.7 German rent table**

| Pattern | Treatment | Kz | Notes |
| --- | --- | --- | --- |
| MIETE (commercial, landlord opted to charge VAT under § 9 UStG) | Domestic 19% | 66 | Landlord opted to tax |
| MIETE, WOHNUNGSMIETE (residential) | EXCLUDE | Exempt, § 4 Nr.  12 UStG, no input deduction | |
| BÜROMIETE, GEWERBEMIETE | Domestic 19% if VAT shown on invoice | 66 | Confirm VAT is charged |
| NEBENKOSTEN, BETRIEBSKOSTEN | Check invoice | 66 | May include VAT: confirm on the invoice |

### 3.8 SaaS EU suppliers (reverse charge, Kz 46/47)

Billed from entities in the rest of the EU, usually Ireland or Luxembourg, so § 13b(1) UStG applies to a § 3a(2) service. Self-assess the tax in Kz 46 and 47 and claim it back in Kz 67. Net effect zero for a fully taxable client.

**3.8 SaaS EU suppliers table**

| Pattern | Billing entity | Kz (base/output/input) | Notes |
| --- | --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 46/47/67 | Reverse charge |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 46/47/67 | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 46/47/67 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 46/47/67 | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 46/47/67 | Reverse charge |
| SPOTIFY | Spotify AB (SE) | 46/47/67 | Reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | 46/47/67 | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | 46/47/67 | Reverse charge |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 46/47/67 | Reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 46/47/67 | Reverse charge |
| CANVA | Canva Pty Ltd (AU) billed via IE entity in some cases | 46/47/67 | Check invoice: if IE entity, EU reverse charge |

### 3.9 SaaS non-EU suppliers (reverse charge, Kz 84 and 85)

**3.9 SaaS non-EU suppliers table**

| Pattern | Billing entity | Kz (base/output/input) | Notes |
| --- | --- | --- | --- |
| AWS | AWS EMEA SARL (LU), an EU entity | 46/47/67 | Established in the rest of the EU, so a § 3a(2) service goes in the EU boxes |
| NOTION | Notion Labs Inc (US) | 84/85/67 | Supplier established abroad, outside the EU |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 84/85/67 | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 84/85/67 | Non-EU reverse charge |
| GITHUB (standard plans) | GitHub Inc (US) | 84/85/67 | If the invoice shows an Irish entity, use Kz 46 and 47 instead |
| FIGMA | Figma Inc (US) | 84/85/67 | Non-EU reverse charge |
| HUBSPOT | HubSpot Inc (US) or HubSpot Ireland Ltd (IE): check the invoice | 84/85/67 or 46/47/67 | The country of the billing entity decides the boxes |
| TWILIO | Twilio Inc (US) | 84/85/67 | Non-EU reverse charge |
| VERCEL, NETLIFY, HEROKU | US entities | 84/85/67 | Non-EU reverse charge |

- **EU and non-EU foreign suppliers use DIFFERENT boxes.** A § 3a(2) service from a business established in the rest of the EU is § 13b(1) UStG, line 30: Kz 46 and Kz 47. Works supplies, and other services taxable in Germany that do not belong in line 30, from a business established abroad are § 13b(2) Nr. 1 UStG, line 32: Kz 84 and Kz 85. That covers a service from a supplier outside the EU whose place of supply is Germany. It does not cover goods: goods from the rest of the EU are an intra-Community acquisition (rule 5.8) and goods from outside the EU carry import VAT (rule 5.9). Nor does it cover a service supplied outside Germany, or the cases § 13b(6) UStG takes out, such as a cross-border passenger flight or admission to a trade fair in Germany. Input VAT is Kz 67 either way. Neither case goes in your recapitulative statement, which lists only your own outgoing supplies.

### 3.10 Payment processors

**3.10 Payment processors table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE (transaction fees) | EXCLUDE (exempt) | Exempt financial service, § 4 Nr.  8 UStG |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | PayPal Europe S.a r.l. (LU), exempt |
| STRIPE (monthly subscription) | EU reverse charge, Kz 46/47/67 | Stripe Technology Europe Ltd (IE): separate from transaction fees |
| SUMUP, ZETTLE, SQUARE | Check the invoice | German entity: Kz 66. Rest of the EU: Kz 46/47/67. Outside the EU: Kz 84/85/67 |
| KLARNA (merchant fees) | EXCLUDE (exempt) | Exempt |

### 3.11 Professional services (Germany)

**3.11 Professional services table**

| Pattern | Treatment | Kz | Notes |
| --- | --- | --- | --- |
| STEUERBERATER, STEUERKANZLEI, TAX ADVISOR | Domestic 19% | 66 | Deductible overhead |
| RECHTSANWALT, KANZLEI, ANWALT, ANWALTSKANZLEI | Domestic 19% | 66 | Deductible if a business matter |
| NOTAR, NOTARIAT | Domestic 19% | 66 | For business purposes |
| WIRTSCHAFTSPRÜFER, WP | Domestic 19% | 66 | Audit and accounting |
| UNTERNEHMENSBERATER, BERATUNG | Domestic 19% | 66 | Consulting fees |
| HANDELSREGISTER, AMTSGERICHT | EXCLUDE | Court or registry fee, sovereign act | |

### 3.12 Payroll and social security contributions (exclude entirely)

**3.12 Payroll and social security table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KRANKENVERSICHERUNG (statutory: AOK, TK, BARMER, DAK, IKK) | EXCLUDE | Statutory health insurance |
| RENTENVERSICHERUNG, DRV | EXCLUDE | Statutory pension |
| PFLEGEVERSICHERUNG | EXCLUDE | Long-term care insurance |
| FINANZAMT LOHNSTEUER, LOHNSTEUER | EXCLUDE | PAYE tax remittance |
| GEHALT, LOHN, LOHNZAHLUNG | EXCLUDE | Wages, outside the scope |
| AGENTUR FUER ARBEIT, ARBEITSLOSENVERSICHERUNG | EXCLUDE | Unemployment insurance |
| KNAPPSCHAFT, MINIJOBZENTRALE | EXCLUDE | Minijob social contributions |

### 3.13 Internal transfers and exclusions

**3.13 Internal transfers table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UMBUCHUNG, EIGENE UEBERWEISUNG, KONTOÜBERTRAG | EXCLUDE | Between own accounts |
| DAUERAUFTRAG (to own account) | EXCLUDE | To own account |
| PRIVATEINLAGE, EINLAGE | EXCLUDE | Owner injection |
| PRIVATENTNAHME, ENTNAHME | EXCLUDE | Owner drawing |
| DIVIDENDE | EXCLUDE | Out of scope |
| DARLEHEN, TILGUNG, KREDIT | EXCLUDE | Loan principal, out of scope |
| BARGELDABHEBUNG, GELDAUTOMAT, ATM | TIER 2: ask | Exclude by default: ask what it was spent on |
| GUTSCHRIFT STORNO, STORNIERUNG, RÜCKLASTSCHRIFT | Reverse of original | Negative in the same Kennzahl as the original |

## Section 4: Worked examples

Six worked classifications from a hypothetical Kontoauszug of a German self-employed IT consultant. The amounts are invented and carry no authority; only the treatment does. They are written as a German statement prints them: dot for thousands, comma for decimals.

### Example 1: Non-EU SaaS reverse charge (OpenAI)

**Input line (Sparkasse Kontoauszug format):**
```
Buchungstag: 05.04.2026
Buchungstext: SEPA-Basislastschrift
Verwendungszweck: OPENAI *CHATGPT PLUS 4973857 SAN FRANCISCO US
Betrag: -23,78
```

**Reasoning.** OpenAI Inc is a US entity (Section 3.9), no VAT on the invoice. The place of supply is Germany under § 3a(2) UStG. The supplier is established abroad but NOT in the rest of the EU, so this is § 13b(2) Nr. 1 UStG, not § 13b(1), and it goes in line 32: Kz 84 (base), Kz 85 (tax), Kz 67 (input VAT). Net effect zero for a fully taxable client, and it does NOT go in the recapitulative statement.

**Example 1 output table**

| Date | Counterparty | Gross | Net | VAT | Rate | Kz (base) | Kz (output) | Kz (input) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | OPENAI INC | -23.78 | -23.78 | 4.52 | 19% | 84 | 85 | 67 | N | none | none |

### Example 2: EU service, reverse charge (Google Ads)

**Input line:**
```
Buchungstag: 10.04.2026
Buchungstext: SEPA-Basislastschrift
Verwendungszweck: GOOGLE IRELAND LTD GOOGLE ADS CID:123-456-7890
IBAN: IE29AIBK93115212345678
Betrag: -1.200,00
```

**Reasoning.** Google Ireland Limited is an IE entity (the IBAN confirms it). A § 3a(2) service from a business established in the rest of the EU, so § 13b(1) UStG applies and it goes in line 30: Kz 46 for the net base, Kz 47 for the self-assessed tax, Kz 67 for the input VAT. The amount charged is already net, because the supplier invoices without VAT to a customer with a USt-IdNr. A service RECEIVED is not reported in the recapitulative statement; only your own outgoing § 3a(2) services are.

**Example 2 output table**

| Date | Counterparty | Gross | Net | VAT | Rate | Kz (base) | Kz (output) | Kz (input) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | GOOGLE IRELAND LTD | -1,200.00 | -1,200.00 | 228.00 | 19% | 46 | 47 | 67 | N | none | none |

### Example 3: Bewirtung (business entertainment), fully recoverable

**Input line:**
```
Buchungstag: 15.04.2026
Buchungstext: Kartenzahlung
Verwendungszweck: RESTAURANT ZUM GOLDENEN HIRSCH MUENCHEN
Betrag: -285,60
```

**Reasoning.** A restaurant bill. The input VAT on business entertainment is fully recoverable under § 15(1) Nr. 1 UStG if documented: see rule 5.3. From 2026 the food and the drinks on the bill carry different rates, so split it before working out the tax. Default: BLOCK, because the Bewirtungsbeleg status is unknown. Flag for the reviewer.

**Example 3 output table**  _("Bewirtung: do you have a properly completed Bewirtungsbeleg? If yes, the Vorsteuer in this row is recoverable via Kz 66.")_

| Date | Counterparty | Gross | Net | VAT | Rate | Kz (input) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | RESTAURANT ZUM GOLDENEN HIRSCH | -285.60 | not known until the bill is split | 0 | food reduced, drinks standard | none | Y | Q1 | "Bewirtung: do you have a properly completed Bewirtungsbeleg, and how much of the bill was drinks? If documented, the Vorsteuer is recoverable via Kz 66." |

### Example 4: Domestic purchase, standard 19%

**Input line:**
```
Buchungstag: 18.04.2026
Buchungstext: SEPA-Basislastschrift
Verwendungszweck: DEUTSCHE TELEKOM AG RECHNUNG APRIL 2026 KD-NR 12345
Betrag: -59,95
```

**Reasoning.** Deutsche Telekom is a domestic supplier (Section 3.3), telecoms at the standard rate. The statement shows the gross; the net and the tax below are taken out of it. Full deduction via Kz 66 if the line is used wholly for the business; otherwise the business share only.

**Example 4 output table**

| Date | Counterparty | Gross | Net | VAT | Rate | Kz (input) | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18.04.2026 | DEUTSCHE TELEKOM AG | -59.95 | -50.38 | -9.57 | 19% | 66 | N | none | none |

### Example 5: EU B2B service sale (IT consulting to Austrian client)

**Input line:**
```
Buchungstag: 22.04.2026
Buchungstext: SEPA-Gutschrift
Verwendungszweck: KREATIV DIGITAL GMBH WIEN RE-2026-042 IT BERATUNG MAERZ
IBAN: AT611904300234573201
Betrag: +4.500,00
```

**Reasoning.** An incoming payment from an Austrian company (AT IBAN) for consulting supplied to a business. The place of supply under § 3a(2) UStG is Austria. Invoice without German VAT and with a reverse-charge note; the customer accounts for the tax there. Report the net amount in Kz 21, line 35, and in the recapitulative statement. The reference shows the consulting was done in March, so it belongs in the return and the recapitulative statement for the period that contains March, not the period of the payment. Kz 21 is not a tax-free supply: it is a supply not taxable here. Confirm the USt-IdNr with the Bundeszentralamt fuer Steuern; without a valid number, treat the customer as a consumer and charge German VAT.

**Example 5 output table**  _("Verify Austrian USt-IdNr (ATU format)")_

| Date | Counterparty | Gross | Net | VAT | Rate | Kz | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22.04.2026 | KREATIV DIGITAL GMBH WIEN | +4,500.00 | +4,500.00 | 0 | none | 21 | Y | Q2 (HIGH) | "Verify Austrian USt-IdNr (ATU format)" |

### Example 6: Bank fee and insurance (excluded)

**Input line:**
```
Buchungstag: 30.04.2026
Buchungstext: Abschluss
Verwendungszweck: KONTOFÜHRUNGSGEBÜHR Q2/2026
Betrag: -12,90

Buchungstag: 30.04.2026
Buchungstext: SEPA-Basislastschrift
Verwendungszweck: ALLIANZ VERSICHERUNG BETRIEBSHAFTPFLICHT POLICE 12345
Betrag: -89,50
```

**Reasoning.** The bank fee is an exempt financial service (§ 4 Nr.  8 UStG, Section 3.1) and the premium is exempt insurance (§ 4 Nr.  10 UStG, Section 3.4). Neither carries input VAT and neither appears on the UStVA.

**Example 6 output table**

| Date | Counterparty | Gross | Net | VAT | Rate | Kz | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30.04.2026 | SPARKASSE KONTOFÜHRUNG | -12.90 | none | none | none | none | N | none | EXCLUDE: exempt bank fee |
| 30.04.2026 | ALLIANZ VERSICHERUNG | -89.50 | none | none | none | none | N | none | EXCLUDE: exempt insurance |

## Section 5: Tier 1 classification rules (compressed)

Each rule gives its source and its Kennzahl. Apply it silently where the data is clear.

### 5.1 Standard rate 19% (ss12(1) UStG)

- **Standard rate default.** The rate for any taxable supply unless a reduced rate, the zero rate or an exemption applies. Sales: Kz 81, net base. Purchases: Kz 66, the tax amount.

### 5.2 Reduced rate 7% (ss12(2) UStG)

- **Reduced rate scope.** The list is § 12(2) UStG with its Annex 2: food and the other Annex 2 goods, books, newspapers and their electronic editions, water, cut flowers and plants, dental technicians' work, admission to theatres, concerts, museums and zoos, short-term letting of rooms and camping pitches, and from 1 January 2026 restaurant and catering services with the express exception of DRINKS (§ 12(2) Nr. 15 UStG). Passenger transport is reduced-rated by rail with no distance limit, and by trolleybus, scheduled bus, taxi, cable car and scheduled ferry only within one municipality or where the journey is not more than 50 kilometres. Breakfast, parking and internet sold with a room are not covered. Sales: Kz 86. Purchases: Kz 66.

### 5.3 Bewirtung (business entertainment): VAT fully recoverable

- **Bewirtung VAT recovery rules.** Unlike Malta and Ireland, where entertainment VAT is blocked, in Germany the input VAT on REASONABLE and EVIDENCED entertainment is recoverable in full under § 15(1) Nr. 1 UStG: § 15(1a) UStG blocks the costs of § 4(5) sentence 1 Nr. 1 to 4 and 7 EStG, and then lifts the block for entertainment to the extent that the income tax rule cuts reasonable, evidenced costs. Entertainment that is not reasonable gives no input VAT. Conditions: a machine-produced invoice from the restaurant; the date, the guests, the business reason and the host's signature on the receipt; a concrete business reason. The income tax cut of § 4(5) Nr. 2 EStG, whose share is in the thresholds tables, does NOT reduce the VAT claim. From 2026 split the bill between food and drinks. **Default when documentation is unknown: BLOCK.**

### 5.4 Tax-free with input deduction, and supplies not taxable in Germany

- **Tax-free with input deduction, and not taxable at all: two different things.** Exports outside the EU: Kz 43, tax-free with input deduction, needs the customs export evidence. Intra-Community supplies of goods to a business: Kz 41, tax-free with input deduction, needs the customer's USt-IdNr, transport evidence and a Gelangensbestaetigung or equivalent (§§ 17a to 17c UStDV). Your § 3a(2) services to a business in the rest of the EU: Kz 21, line 35, NOT tax-free but not taxable here, needs the customer's USt-IdNr and goes in the recapitulative statement. Services to a business outside the EU, and any other supply whose place of supply is not Germany: Kz 45, line 36, also not taxable rather than tax-free.

### 5.5 Exempt without input deduction (ss4 Nr.8-29 UStG)

- **Exempt supplies list.** Financial services, insurance, residential rent, healthcare, education, social welfare, the universal postal service. They go in Kz 48, line 23. No output VAT, and no input VAT on the related costs (§ 15(2) UStG). If they are not trivial, the input tax must be apportioned under § 15(4) UStG: R-DE-4 points to de-vat-annual-and-special-schemes.

### 5.6 Reverse charge: foreign suppliers (§ 13b(1) and § 13b(2) Nr. 1 UStG)

- **Foreign supplier reverse charge: two boxes, not one.** § 13b(1) UStG covers ONLY a § 3a(2) service from a business established in the rest of the EU: base Kz 46, tax Kz 47, input VAT Kz 67, line 30. Works supplies and the other services taxable in Germany that do not belong in line 30, from a business established abroad, are § 13b(2) Nr. 1 UStG: base Kz 84, tax Kz 85, input VAT Kz 67, line 32. A service from a supplier outside the EU goes here only if its place of supply is Germany. Goods are never in this rule: rules 5.8 and 5.9. Net cash effect zero for a fully taxable client. If a supplier in another member state wrongly charged its own VAT, that is not a reverse charge: book an overhead with foreign VAT you cannot recover here and ask for a corrected invoice.

### 5.7 Reverse charge: the domestic categories of § 13b(2) UStG

- **Domestic reverse charge categories.** Construction services, building cleaning, scrap metal (Annex 3), gold, gas and electricity from a supplier abroad, and, only where the fees in one economic transaction reach the amount in the thresholds tables, the Annex 4 metals and mobile phones, tablets, games consoles and integrated circuits, and emission certificates. All share line 32 with the foreign-supplier cases: Kz 84, Kz 85, input VAT Kz 67. Supplies inside the real estate transfer tax act are the exception, on line 31: Kz 73 and Kz 74. Construction applies only where BOTH parties supply such services, and cleaning only where the customer supplies cleaning too.

### 5.8 Intra-Community acquisition of goods (ss1a UStG)

- **Intra-Community acquisition of goods.** A business purchase of goods dispatched from another member state to Germany. Net base in Kz 89 at the standard rate, Kz 93 at the reduced rate, Kz 90 at the zero rate of § 12(3) UStG; the tax is worked out from the base. Input VAT in Kz 61, line 39, which is a different box from Kz 66. Net effect zero for a fully taxable client. Intrastat statistical reporting may also be due; its thresholds are set by the statistical authority and are outside this Guide.

### 5.9 Import VAT (Einfuhrumsatzsteuer / EUSt)

- **Import VAT treatment.** Physical goods imported from outside the EU. The Einfuhrumsatzsteuer is assessed by Zoll at the border and is not self-assessed on the UStVA. On the 2026 form it is recovered in Kz 62, line 40, headed "Entstandene Einfuhrumsatzsteuer" and citing § 15(1) sentence 1 Nr. 2 UStG: not Kz 66. The claim is for the import VAT that has ARISEN, and needs the customs assessment notice (Einfuhrabgabenbescheid).

### 5.10 Blocked input VAT

- **Blocked input VAT categories.** § 15(1a) UStG blocks the input VAT on the costs caught by § 4(5) sentence 1 Nr. 1 to 4 and Nr. 7 EStG and by § 12 Nr. 1 EStG: gifts to a person once the cost of everything given to that recipient in the calendar year passes the amount in the thresholds tables, and then on ALL of it, not only the excess; hunting, fishing, yachts and similar hospitality; and private living costs. Also excluded: the private share of a mixed asset, an item used below the minimum business share in the thresholds tables, purchases relating to exempt supplies (§ 15(2) UStG), and anything without an invoice meeting § 14 UStG. **Reasonable, evidenced entertainment is NOT blocked**, because § 15(1a) sentence 2 UStG lifts the block to that extent: rule 5.3. Motor vehicles are not blocked either: Section 6.1.

### 5.11 Private use deemed supply (unentgeltliche Wertabgabe)

- **Private use deemed supply.** If the client uses a business asset privately, output VAT arises on the private share as a deemed supply under § 3(1b) UStG for goods or § 3(9a) UStG for use and services. The base is the cost that carried input VAT, not the income tax list-price figure (the 1-Prozent-Regelung). It is reported with the ordinary taxable supplies at the rate that applies, so normally Kz 81. Tier 2: a Steuerberater should confirm the method and the amount.  _(§ 3(1b) UStG; § 3(9a) UStG)_

### 5.12 Photovoltaic installations at 0% (ss12(3) UStG)

- **Photovoltaic installations at the zero rate.** Supply, intra-Community acquisition, import and installation of solar modules, their essential components and storage, for the operator of a system on or near homes and buildings used for public-benefit activities. The conditions count as met where the registered gross output is not more than 30 kilowatts peak. A RATE, not an exemption, so the supplier keeps full input deduction. Sales go in Kz 87, line 15; such an acquisition goes in Kz 90, line 27.

### 5.13 Credit notes and corrections

- **Credit notes and corrections.** A Gutschrift under § 14 UStG is self-billing by the buyer and creates output tax for the supplier. A Stornorechnung or Rechnungskorrektur cancels or amends an earlier invoice. Both change the original Kennzahl. A correction is entered in the period in which the change happened, as a change to the tax base in the same Kennzahl, with a minus sign where it is a reduction (§ 17(1) UStG). Only where the agreed fee has become uncollectible (§ 17(2) Nr. 1 sentence 1 UStG) is the reduction ALSO shown in Kz 50, line 51, or for input VAT in Kz 37, line 52. An ordinary credit note, discount or cancellation is not entered there.

### 5.14 Sales: cross-border B2C

- **Cross-border sales to consumers.** § 3c(4) UStG keeps the place of supply in Germany while cross-border distance sales of goods AND telecom, broadcasting and electronic services to consumers in other member states stay together, EU-wide, within the amount in the thresholds tables, in the previous and the current year. Below it, charge German VAT and report in Kz 81 or Kz 86. Above it, or after a waiver, the place of supply moves: R-EU-5 in `eu-vat-directive` fires and the one-stop shop is used. Supplies taxable IN GERMANY that are declared under §§ 18i, 18j or 18k UStG are not entered in lines 13 to 16. Your own distance sales and telecom, broadcasting and electronic services to consumers whose place of supply is another member state are not taxable here and go in Kz 45, line 36, even when the tax itself is declared through the one-stop shop.

### 5.15 Dauerfristverlaengerung and Sondervorauszahlung

- **Dauerfristverlaengerung mechanics.** On application the tax office must extend the filing AND the payment deadline by one month, unless the tax claim appears to be at risk (§ 46 UStDV). Only a MONTHLY filer must also declare and pay a Sondervorauszahlung; a quarterly filer pays none. It is one eleventh of the sum of the previous year's advance payments (§ 47 UStDV), taken before that year's Sondervorauszahlung credit, so add the Kz 39 amount back to the total of Kz 83, computed, declared and paid by the statutory date of the first advance return of the year, on form USt 1 H (§ 48(1) and (2) UStDV). It is credited in the last return of the year in Kz 39, line 49, reducing Kz 83 (§ 48(4) UStDV).

## Section 6: Tier 2 catalogue (compressed)

For each ambiguity: the pattern, why the statement is not enough, the conservative default and the question to ask.

### 6.1 Vehicle costs

- **Vehicle costs ambiguity.** Pattern: ARAL, SHELL, TOTAL, ESSO, JET, AGIP, STAR, Tankstelle, ADAC Pannenhilfe, TÜV. Why insufficient: the vehicle and the business share are unknown. German VAT does not block motor vehicles; the split decides the deduction, and below the minimum business share in the thresholds tables there is none at all. The private share is a deemed supply under § 3(9a) UStG. Default: no recovery. Question: "Used only for the business? If mixed, what share? Fahrtenbuch or the list-price method (1-Prozent-Regelung)?"

### 6.2 Bewirtungskosten

- **Bewirtungskosten ambiguity.** Pattern: any named restaurant, Gaststätte, Imbiss or hotel. Why insufficient: the Bewirtungsbeleg status is unknown, and from 2026 the food and the drinks on one bill carry different rates. Fully recoverable if documented; denied if not. Default: block. Question: "Do you have a completed Bewirtungsbeleg: guests, business reason and your signature on the machine-produced invoice? How much of the bill was drinks?"

### 6.3 Home office (Arbeitszimmer)

- **Home office ambiguity.** Pattern: Miete, Strom, Internet that could relate to a home office. Why insufficient: the day flat rate for working at home is an INCOME TAX concept with no VAT equivalent. For VAT, a share of rent and running costs is deductible only where a separate room is used for the business and VAT was charged at all; residential rent is exempt, so usually there is none. Default: no recovery. Question: "A separate room used only for business, and what share of the floor area?"

### 6.4 Cash withdrawals (Bargeldabhebung)

- **Cash withdrawals ambiguity.** Pattern: ATM, Geldautomat, Bargeldabhebung. Why insufficient: what the cash bought is unknown. Default: exclude as an owner drawing. Question: "What did the cash buy, and do you have receipts?"

### 6.5 Mixed SaaS billing entity

- **Mixed SaaS billing ambiguity.** Pattern: Google, Microsoft, Adobe, Meta, Slack, Zoom, LinkedIn, Apple, Amazon, Dropbox, Atlassian, Stripe, PayPal where the legal entity is not in the Kontoauszug. Why insufficient: the same brand can bill from Ireland (Kz 46 and 47), the United States (Kz 84 and 85) or Germany (Kz 66). Default: Kz 84 and 85. Question: "Could you send the latest invoice from each provider, showing the legal entity, its country, and whether it charges German VAT or notes a reverse charge?"

### 6.6 Round-number transfers (Gesellschaftereinlage or Umsatz?)

- **Round-number transfers ambiguity.** Pattern: a large round credit from the client's own name or a family member. Why insufficient: it could be a sale, an owner injection or a loan. Default: exclude as an Einlage. Question: "The transfer from that name: is it a customer payment, your own money going in (Einlage), or a loan?"

### 6.7 Amazon purchases

- **Amazon purchases ambiguity.** Pattern: AMAZON, AMAZON PAYMENTS, AMAZON EU SARL, AMZN MKTP. Why insufficient: an Amazon purchase may be a business supply, deductible at whichever rate the item carries, or personal, which is blocked. Amazon may also bill from Luxembourg (Amazon EU S.a r.l.), Germany (Amazon.de GmbH) or a US entity, which changes the boxes as in item 6.5. Default: block (personal). Question: "Business or personal? If business, what was the item?"

## Section 7: Excel working paper template (Germany-specific)

Base specification: `vat-workflow-base` Section 3. This is the Germany overlay.

### Sheet "Transactions"

Columns A to L per the base. Column H ("Kz code") takes only Kennzahl codes from the table in
Section 1, and is blank for an excluded transaction. For a reverse charge, enter base, output
and input separated by slashes: 46/47/67 for a § 3a(2) service from the rest of the EU,
84/85/67 for works supplies and other services taxable in Germany from a business established
abroad that do not belong in line 30, and for the domestic § 13b(2) categories, 73/74/67 for
a supply inside the real estate transfer tax act.

### Sheet "Kz Summary"

**Kz Summary mandatory rows**

Output side:

~~~
81   Taxable supplies, standard rate (net)   =SUMIFS(Transactions!E:E, Transactions!H:H, "81")
T81  Tax on Kz 81                            =C[81_row]*0.19
86   Taxable supplies, reduced rate (net)    =SUMIFS(Transactions!E:E, Transactions!H:H, "86")
T86  Tax on Kz 86                            =C[86_row]*0.07
87   Taxable supplies, zero rate (net)       =SUMIFS(Transactions!E:E, Transactions!H:H, "87")
35   Supplies at other rates (net)           =SUMIFS(Transactions!E:E, Transactions!H:H, "35")
36   Tax on Kz 35                            entered by hand
41, 43, 48, 21, 45  one SUMIFS row each, net amounts, no tax computed on them
89   IC acquisitions, standard rate (net)    =SUMIFS(Transactions!E:E, Transactions!H:H, "89")
T89  Tax on Kz 89                            =C[89_row]*0.19
93   IC acquisitions, reduced rate (net)     =SUMIFS(Transactions!E:E, Transactions!H:H, "93")
T93  Tax on Kz 93                            =C[93_row]*0.07
46   EU service reverse charge, base         =SUMIFS(Transactions!E:E, Transactions!H:H, "46")
47   Tax on Kz 46                            =C[46_row]*0.19
84   Other reverse charge, base              =SUMIFS(Transactions!E:E, Transactions!H:H, "84")
85   Tax on Kz 84                            =C[84_row]*0.19
73   GrEStG reverse charge, base             =SUMIFS(Transactions!E:E, Transactions!H:H, "73")
74   Tax on Kz 73                            =C[73_row]*0.19
L37  Output VAT (form line 37, no Kennzahl)  =C[T81]+C[T86]+C[36]+C[T89]+C[T93]+C[47]+C[74]+C[85]
~~~

Input side and the bottom line:

~~~
66   Input VAT from invoices                 =SUMIFS(Transactions!F:F, Transactions!H:H, "66")
61   Input VAT on IC acquisitions            =C[T89_row]+C[T93_row]
62   Import VAT assessed by customs          entered from the Einfuhrabgabenbescheid
67   Input VAT on § 13b supplies             =C[47_row]+C[74_row]+C[85_row]
64   Input VAT adjustment (§ 15a UStG)       by hand, Tier 2
L45  Remaining amount (form line 45)         =C[L37]-C[66]-C[61]-C[62]-C[67]-C[64]
65, 69  Change of method, § 14c UStG tax     normally empty
83   BOTTOM LINE: pay, or surplus with minus =C[L45]+C[65]+C[69]-C[39]
~~~

Kz 83 is the amount to pay or reclaim, not a subtotal of output tax, and Kz 65 is the
change-of-method box, not the net result. Swapping those two is the most common structural
error in a German working paper.

### Sheet "Return Form"

- **Return Form final figures logic.** Line 37 is output VAT, lines 38 to 44 the deductible
  input tax, line 45 the difference. Lines 46 and 47 add the other tax amounts, giving line 48.
  Kz 39 on line 49 takes off the Sondervorauszahlung, and Kz 83 on line 50 is what is left. A
  positive Kz 83 is payable; a surplus is written with a minus sign. Always fill Kz 83 in.

### Color and formatting conventions

Per the spreadsheet conventions: blue for hardcoded statement values (column D of Transactions),
black for formulas, green for cross-sheet references, yellow background on any Transactions row
where Default? = "Y".

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/germany-vat-working-paper.xlsx
```

Check the JSON output. If `status` is `errors_found`, fix the formulas and run it again.

## Section 8: German bank statement reading guide

Follow the exclusion rules in `vat-workflow-base` Step 6, plus these German patterns.

### Kontoauszug format conventions

**Kontoauszug field table**

| Field | Meaning | Notes |
| --- | --- | --- |
| Buchungstag | Booking date | The transaction date for the return. DD.MM.YYYY |
| Wertstellung / Valuta | Value date | For interest only, not for VAT |
| Buchungstext | Transaction type | SEPA-Ueberweisung, SEPA-Basislastschrift, SEPA-Gutschrift, Kartenzahlung, Dauerauftrag, Abschluss, Gehalt |
| Verwendungszweck | Purpose or reference | Free text with the reference, invoice number and counterparty. The main identifying field |
| Begünstigter / Auftraggeber | Payee or payer | The registered account holder in a SEPA transaction |
| IBAN | Counterparty IBAN | The country prefix places the counterparty and points to the reverse-charge box |
| BIC / SWIFT | Bank code | Confirms the country when the IBAN is ambiguous |
| Betrag | Amount | Negative is outgoing. German format: dot for thousands, comma for decimals |
| Saldo | Balance | Running balance after the transaction |

A statement is not an invoice: it fixes the cash date, not the tax point. Under
Soll-Versteuerung the tax point is the supply, not the payment.

### IBAN country prefixes

**IBAN prefixes table**

| Prefix | Country | VAT treatment |
| --- | --- | --- |
| DE | Germany | Domestic |
| AT, BE, BG, CY, CZ, DK, EE, ES, FI, FR, GR, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK | Rest of the EU | A service under § 3a(2) UStG: reverse charge in Kz 46 and 47. Goods: intra-Community acquisition in Kz 89 or Kz 93 |
| GB, US, CH, AU, NO, CA, JP | Outside the EU | Reverse charge under § 13b(2) Nr. 1 UStG in Kz 84 and 85. Goods arriving physically: import VAT in Kz 62 |

The IBAN is a clue, not proof. What counts is where the SUPPLIER is established, which the
invoice states and a payment account does not.

### Common Buchungstext codes

**Buchungstext codes table**

| Code | Meaning | Typical treatment |
| --- | --- | --- |
| SEPA-Ueberweisung | Outgoing transfer | Supplier payment: classify by counterparty |
| SEPA-Gutschrift | Incoming transfer | Customer payment: classify as a sale |
| SEPA-Basislastschrift | Direct debit | Recurring supplier charges: telecoms, SaaS, insurance |
| Kartenzahlung / EC-Zahlung | Card payment | Point-of-sale purchase |
| Dauerauftrag | Standing order | Recurring fixed payment such as rent |
| Abschluss | Account settlement | Bank fees and interest: usually EXCLUDE |
| Gehalt/Lohn | Salary payment | Employee wages: EXCLUDE |
| Lastschrift Finanzamt | Tax authority direct debit | Tax payment: EXCLUDE |

### German-language transaction descriptions

**German terms table**

| German | English | Classification hint |
| --- | --- | --- |
| Rechnung, Rg., RE | Invoice | Purchase or sale with an invoice reference |
| Miete | Rent | See Section 3.7 |
| Gehalt, Lohn | Salary, wages | EXCLUDE |
| Zinsen | Interest | EXCLUDE |
| Versicherung | Insurance | EXCLUDE, exempt |
| Steuern, USt, MwSt | Tax, VAT | Tax payment: EXCLUDE |
| Beitrag | Contribution or fee | Chamber fee (EXCLUDE) or a subscription (classify) |
| Gutschrift | Credit note | Reverse of the original transaction |
| Rücklastschrift | Returned direct debit | Reversal: book negative in the original Kennzahl |
| Erstattung | Refund | Reverse of the original transaction |
| Einlage | Capital injection | EXCLUDE, owner injection |
| Entnahme | Drawing | EXCLUDE, owner drawing |

### Internal transfers and exclusions

- **Internal transfers exclusion.** Transfers between the client's own accounts, labelled
  "Umbuchung", "eigene Ueberweisung" or "Kontoübertrag". Always exclude.

### Foreign currency transactions

- **Foreign currency conversion.** Convert to euro at the average rate the Federal Ministry of
  Finance publishes for the month of the supply under § 16(6) UStG. The day rate on a bank
  advice may be used only if the tax office has allowed it. Record
  it in column L. German bank statements usually show the euro amount already.

### Cryptic descriptions

Card purchases with only a terminal ID, direct debits with only a Mandatsreferenz. Ask the
client. Do not classify an unidentified transaction.

## Section 9: Onboarding fallback (only when inference fails)

`vat-workflow-base` Section 1 infers the client profile from the data first. Ask only what the
data could not answer.

### 9.1 Entity type and trading name

- Inference: a sole trader's name usually matches the account holder; a company name ends in
  GmbH, UG, GbR, OHG, KG, AG or e.K. Ask: "Sole trader, GmbH, UG, or something else?"

### 9.2 VAT registration status

- Inference: a client asking for a UStVA is on Regelbesteuerung. No VAT on sales suggests a
  Kleinunternehmer, which triggers the R-DE-1 pointer. Ask: "Are you on Regelbesteuerung, or a
  Kleinunternehmer under § 19 UStG with no VAT on your invoices?"

### 9.3 USt-IdNr and Steuernummer

- Inference: the USt-IdNr (DE and nine digits) sometimes appears in EU payment references; the
  Steuernummer is on Finanzamt letters. Ask: "Your USt-IdNr and Steuernummer?"

### 9.4 Filing period and frequency

- Inference: the first and last transaction dates give the period; the rhythm follows the
  previous year's VAT against the thresholds tables. Ask: "Which period, monthly or quarterly?"

### 9.5 Industry and sector

- Inference: the counterparty mix and the sales descriptions. Ask: "What does the business do?"

### 9.6 Employees

- Inference: Gehalt, Lohn and Sozialversicherung payments to non-owners. Ask: "Any employees?"

### 9.7 Exempt supplies

- Inference: medical, financial, educational or residential letting income. Ask: "Any VAT-exempt
  sales?" If yes and not trivial, follow the R-DE-4 pointer.

### 9.8 Soll- or Ist-Versteuerung

- Inference: most small businesses are on Soll. Ist-Versteuerung needs the tax office's
  permission and, on the turnover ground, turnover within the limit in the Key thresholds
  summary. Ask: "Are you taxed on invoices issued or on payments received, and do you have the
  permission in writing?" If it is Ist, follow the R-DE-5 pointer.

### 9.9 Dauerfristverlaengerung

- Inference: not visible in one period's statement. Ask: "Do you have a Dauerfristverlaengerung,
  and was a Sondervorauszahlung declared and paid this year?"

### 9.10 Cross-border customers

- Inference: foreign IBANs, foreign currency, foreign customer names. Ask: "Customers outside
  Germany? In the EU or outside it? Businesses with a USt-IdNr, or consumers?"

### Validation status

No accountant stands behind this Guide yet. Every rate, amount and box number was checked
against the pages listed under Sources on 19 September 2026, and anything those pages do not
print was taken out. Read the Known gaps before relying on it.

## The method, step by step

1. Fix the period and the rhythm. Quarterly is the default. Monthly is compulsory when the VAT
   for the previous calendar year was above the limit in the return rhythm table, and may be
   chosen when the previous year ended with a surplus above the same figure. For 2021 to 2026
   the start-up rule differs: instead of two automatic monthly years, a part-year business has
   its tax annualised, and a business starting in the current year is judged on its expected tax
   for that year. § 18(2) and (2a) UStG:
   https://www.gesetze-im-internet.de/ustg_1980/__18.html
2. Check scope before classifying anything: run the refusal catalogue in Section 2. A
   Kleinunternehmer inside both limits of § 19(1) UStG files no advance return and no annual
   VAT return, because § 18(1) to (4) UStG does not apply to them: https://www.gesetze-im-internet.de/ustg_1980/__19.html
3. Classify every line of the statement: Section 3 first, then the Tier 1 rules in Section 5.
   Decide for each line whether it is taxable and at which rate, tax-free with or without input
   deduction, a reverse charge, or outside the scope.
4. Decide the place of supply before the rate. For services between businesses the general rule
   is the customer's country (§ 3a(2) UStG): https://www.gesetze-im-internet.de/ustg_1980/__3a.html
   For a reverse charge received, the box depends on where the supplier is established: a
   § 3a(2) service from the rest of the EU goes in Kz 46 and 47; works supplies and other
   services taxable in Germany from a business established abroad go in Kz 84 and 85; goods are
   not a reverse charge at all (§ 13b(1) and (2) UStG): https://www.gesetze-im-internet.de/ustg_1980/__13b.html
5. Test every input VAT claim against § 15 UStG: an invoice meeting § 14 UStG, no block under
   § 15(1a) UStG, and business use at or above the minimum share in the input tax table:
   https://www.gesetze-im-internet.de/ustg_1980/__15.html
6. Map each line to its Kennzahl from the table in Section 1, build the working paper in
   Section 7 and recalculate it. Tax bases go in whole euros.
7. File through ELSTER by the tenth day after the end of the period and pay the same day, or by
   the extended date under a Dauerfristverlaengerung. Send the recapitulative statement
   separately to the Bundeszentralamt fuer Steuern by the twenty-fifth day (§ 18a UStG): https://www.gesetze-im-internet.de/ustg_1980/__18a.html

## Ask the client first

- Are you on the normal scheme, or a Kleinunternehmer under § 19 UStG? If the latter, have you
  given that status up, and from which year?
- Monthly or quarterly, and is there a Dauerfristverlaengerung? If so, was a Sondervorauszahlung
  declared and paid this year, and is this the last period of the year?
- VAT on invoices issued (Soll-Versteuerung) or on payments received (Ist-Versteuerung under
  § 20 UStG)? If on payments, was that permitted in writing?
- Any sales that are tax-free without input deduction: medical, educational, insurance,
  financial or residential letting income?
- For each foreign supplier: which legal entity issued the invoice, where is it established,
  and does the invoice show German VAT or a reverse-charge note? This decides Kz 46 and 47
  against Kz 84 and 85.
- For each cross-border customer: do you hold a valid USt-IdNr, confirmed with the
  Bundeszentralamt fuer Steuern?
- For restaurant receipts: do you hold a machine-produced invoice with the guests, the business
  reason and your signature recorded, and how much of the bill was drinks?

## When to refuse or refer

- A refusal in Section 2 fires: Organschaft or Differenzbesteuerung. Kleinunternehmer, partial
  exemption and Ist-Versteuerung go to de-vat-annual-and-special-schemes.
- A special scheme this Guide does not cover is in use: the one-stop shop (§§ 18i, 18j, 18k
  UStG), travel services (§ 25 UStG), or the average-rate scheme of § 24 UStG.
- Construction or building-cleaning reverse charge is in play: it turns on whether BOTH parties
  supply such services, which a statement cannot show.
- The return needs a private-use deemed supply valued, an input tax adjustment under § 15a UStG,
  or a correction of an earlier period that changes an assessment.
- An invoice shows German VAT wrongly or shows too much: § 14c UStG makes the issuer owe it
  until the invoice is corrected.
- A material line's counterparty cannot be identified and the client cannot produce the invoice.

### Key thresholds summary

**Small business (Kleinunternehmer), § 19 UStG**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__19.html |
| Total turnover of the PREVIOUS calendar year, not exceeded | EUR 25,000 | "im vorangegangenen Kalenderjahr 25 000 Euro" |
| Total turnover of the CURRENT calendar year, not exceeded | EUR 100,000 | "im laufenden Kalenderjahr 100 000 Euro" |
| Business established elsewhere in the EU: its EU-wide turnover, previous and current year | EUR 100,000 | § 19(4) UStG. It also needs a small-business identification number from its home state |

The two German limits are joined by AND. Total turnover is the receipts-based figure of
§ 19(2) UStG, without sales of fixed assets. The status is lost during the year, not at year end.

**Small business: the start-up year and the receipt that crosses the limit**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2 |
| Business starting during the year: total turnover of the current calendar year | EUR 25,000 | "darf der Gesamtumsatz im laufenden Kj. 25.000 € nicht überschreiten" |

The same instructions say the very receipt that crosses the limit is already taxed under the
normal rules, and that receipts taken in before that point stay exempt.

**Return rhythm and release, § 18 UStG**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__18.html |
| Monthly is compulsory if the previous year's VAT was MORE THAN | EUR 9,000 | "mehr als 9 000 Euro, ist der Kalendermonat Voranmeldungszeitraum" |
| The tax office MAY release from advance returns if it was NOT MORE THAN | EUR 2,000 | "nicht mehr als 2 000 Euro, kann das Finanzamt den Unternehmer ... befreien" |
| Monthly may be CHOSEN if the previous year ended with a surplus in your favour of more than | EUR 9,000 | § 18(2a) UStG. Choose it by filing the January return by 10 February; it binds for the year |

The test is the VAT, not the turnover. The release is discretionary and the annual return stays.

**Cash accounting (Ist-Versteuerung), § 20 UStG**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__20.html |
| Total turnover of the previous calendar year, on application | EUR 800,000 | "im vorangegangenen Kalenderjahr nicht mehr als 800 000 Euro betragen hat" |

Alternative grounds, joined by OR: release from the duty to keep books, or income from a liberal
profession, where there is no turnover limit. It always needs the tax office's permission.

**Small-amount invoices, § 33 UStDV**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustdv_1980/__33.html |
| Invoice total (gross) up to which the short set of details is enough | EUR 250 | "Eine Rechnung, deren Gesamtbetrag 250 Euro nicht übersteigt" |

Not available for distance sales (§ 3c UStG), intra-Community supplies (§ 6a UStG) or
reverse-charge supplies (§ 13b UStG). Above it the full § 14 UStG details are needed before
input VAT may be claimed.

**Domestic reverse charge on mobile phones, tablets, games consoles and integrated circuits, and Annex 4 metals**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__13b.html |
| Fees invoiced in one economic transaction, at or above which the customer owes the tax | EUR 5,000 | § 13b(2) nos. 10 and 11 UStG: "mindestens 5 000 Euro beträgt". A later reduction of the fee is ignored |

**Distance selling to consumers in other member states, § 3c UStG**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__3c.html |
| Distance sales of goods PLUS telecom, broadcasting and electronic services to consumers, EU-wide, previous and current year | EUR 10,000 | "insgesamt 10 000 Euro im vorangegangenen Kalenderjahr nicht überschritten hat" |

One EU-wide total, not one per country, and not a limit on German domestic sales. A waiver binds for two calendar years.

**Recapitulative statement (Zusammenfassende Meldung), § 18a UStG**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__18a.html |
| Quarterly filing allowed while intra-Community supplies of goods stay at or below this in the current and each of the four previous quarters | EUR 50,000 | "der vier vorangegangenen Kalendervierteljahre jeweils mehr als 50 000 Euro beträgt" |
| Yearly filing, condition 1 of 3: all supplies, not above this in the previous year and not expected to exceed it in the current year | EUR 200,000 | § 18a(9) UStG: "nicht überstiegen hat und im laufenden Kalenderjahr voraussichtlich nicht übersteigen wird"; only for a business released from advance returns |
| Yearly filing, condition 2 of 3: those supplies and § 3a(2) services taxed in the other state, not above this in the previous year and not expected to exceed it in the current year | EUR 15,000 | § 18a(9) UStG: "nicht überstiegen hat und im laufenden Kalenderjahr voraussichtlich nicht übersteigen wird". Condition 3: no new vehicles supplied |

Monthly is the default for intra-Community supplies of goods, by the twenty-fifth day after the
month. Services under § 3a(2) UStG are reported quarterly in any case (§ 18a(2)).

**Input tax: minimum business use, § 15(1) UStG**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__15.html |
| Below this share of business use an item does not count as bought for the business, so no input VAT at all | 10% | "zu weniger als 10 Prozent für sein Unternehmen nutzt" |

**Business gifts and entertainment, § 4(5) EStG read with § 15(1a) UStG**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/estg/__4.html |
| Gifts to a person who is not your employee: input VAT is blocked once the cost of everything given to one recipient in the year exceeds this. The income tax text counts by financial year; for VAT the ministry's application decree, section 15.6(4), counts by CALENDAR year | EUR 50 | § 4(5) sentence 1 no. 1 EStG: "insgesamt 50 Euro nicht übersteigen" |
| Business entertainment: the share of a reasonable, evidenced cost deductible for INCOME TAX | 70% | § 4(5) sentence 1 no. 2 EStG: "soweit sie 70 Prozent der Aufwendungen übersteigen". This is an income tax rule and does not cut the VAT claim |

**E-invoicing: the turnover limit for the 2027 relief, § 27(38) UStG**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ustg_1980/__27.html |
| Issuer's total turnover of the previous calendar year, for the relief running to 31 December 2027 | EUR 800,000 | § 27(38) no. 2 UStG: "im vorangegangenen Kalenderjahr nicht mehr als 800 000 Euro betragen hat" |

Since 1 January 2025 every business in Germany must be able to RECEIVE an e-invoice, a
Kleinunternehmer included. For supplies made in 2025 and 2026 an issuer may still send paper or,
with the customer's consent, another electronic format, until 31 December 2026, with no turnover
test; for supplies made in 2027, until 31 December 2027, only within the limit above or by EDI.
The formats, the ministry letter and the detail are in
`germany-einvoice`.

**Late filing and late payment**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gesetze-im-internet.de/ao_1977/__240.html |
| Late payment surcharge per started month of delay, on the rounded-down overdue tax | 1% | "ein Säumniszuschlag von 1 Prozent des abgerundeten rückständigen Steuerbetrags" |
| The overdue tax is rounded down to the next amount divisible by | EUR 50 | "abzurunden ist auf den nächsten durch 50 Euro teilbaren Betrag" |

The late FILING surcharge formula of § 152(5) AO does NOT apply to a monthly or quarterly VAT
advance return or to the Sondervorauszahlung declaration. § 152(8) AO leaves the amount to the
tax office's discretion there. https://www.gesetze-im-internet.de/ao_1977/__152.html

### Known gaps

1. The supplier library covers the common counterparties, not every regional name.
2. The worked examples come from one hypothetical IT consultant, not from every sector.
3. The § 13b(2) domestic categories are context-dependent and stay Tier 2. Construction needs
   both parties confirmed as Bauleistende.
4. The billing entity and its country decide between Kz 46 and 47 and Kz 84 and 85. The
   statement rarely proves it; the invoice does.
5. No official page prints a money figure for a preparer's red flag, so those were removed.
6. Section 3.5 gives the common passenger-transport cases only.
7. From 2026 a restaurant bill splits between food and drinks. Only the invoice shows the split.

### Change log

- **2026 refresh.** Every figure re-checked against the statute and the 2026 form. Kennzahlen
  rebuilt from that form: Kz 83 is the bottom line, Kz 65 the change-of-method box, Kz 87
  zero-rated sales, Kz 62 import VAT, and reverse charge splits between Kz 46 and 47 and
  Kz 84 and 85. Cash accounting limit and Kleinunternehmer filing duty corrected. Red flag
  money figures, Intrastat figures and non-official sources removed.
- **v2.0 (April 2026):** quick reference to the top, supplier library as lookup tables, worked
  examples, Tier 1 and Tier 2, Excel specification, bank statement guide, refusal catalogue.
- **v1.0-draft (April 2026):** initial standalone document.

### Self-check (v2.0 of this document)

1. Quick reference, Kennzahl table and conservative defaults at the top: yes, Section 1.
2. Supplier library, worked examples, Tier 1 and Tier 2: yes, Sections 3 to 6.
3. Excel template with a mandatory recalculation step, and the bank statement guide: Sections 7
   and 8. Onboarding as a fallback: Section 9. Refusals and pointers: Section 2.
4. Entertainment VAT recoverable and motor vehicles not blocked, both stated: rules 5.3, 5.10.
5. Reverse charge split between the EU box and the other-foreign box: Section 1, rules 5.6 and
   5.7, Examples 1 and 2.

## End of the Germany VAT return Guide

Use this Guide with `vat-workflow-base` (workflow) and `eu-vat-directive` (EU directive
content). Load all three before producing a UStVA.

## Sources

- UStG: § 3a https://www.gesetze-im-internet.de/ustg_1980/__3a.html · § 3c https://www.gesetze-im-internet.de/ustg_1980/__3c.html · § 4 https://www.gesetze-im-internet.de/ustg_1980/__4.html · § 12 https://www.gesetze-im-internet.de/ustg_1980/__12.html · § 13b https://www.gesetze-im-internet.de/ustg_1980/__13b.html · § 14 https://www.gesetze-im-internet.de/ustg_1980/__14.html · § 15 https://www.gesetze-im-internet.de/ustg_1980/__15.html
- UStG: § 18 https://www.gesetze-im-internet.de/ustg_1980/__18.html · § 18a https://www.gesetze-im-internet.de/ustg_1980/__18a.html · § 19 https://www.gesetze-im-internet.de/ustg_1980/__19.html · § 20 https://www.gesetze-im-internet.de/ustg_1980/__20.html · § 24 https://www.gesetze-im-internet.de/ustg_1980/__24.html · § 27 https://www.gesetze-im-internet.de/ustg_1980/__27.html
- UStDV: § 33 https://www.gesetze-im-internet.de/ustdv_1980/__33.html · § 46 https://www.gesetze-im-internet.de/ustdv_1980/__46.html · § 47 https://www.gesetze-im-internet.de/ustdv_1980/__47.html · § 48 https://www.gesetze-im-internet.de/ustdv_1980/__48.html
- § 4 EStG https://www.gesetze-im-internet.de/estg/__4.html · AO: § 149 https://www.gesetze-im-internet.de/ao_1977/__149.html · § 152 https://www.gesetze-im-internet.de/ao_1977/__152.html · § 240 https://www.gesetze-im-internet.de/ao_1977/__240.html
- Ministry letter of 29 December 2025, the 2026 UStVA form patterns and instructions: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=2
- Ministry instructions for the 2026 EUeR form: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2026-09-01-anlage-EUER-2026.pdf?__blob=publicationFile&v=2
- Ministry tax booklet, 2025 edition: https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9
- ELSTER, the filing portal: https://www.elster.de
- Bundeszentralamt fuer Steuern: https://www.bzst.de
- EU VIES check of a customer's VAT number: https://ec.europa.eu/taxation_customs/vies/

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do
not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no
liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs
must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or
equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.

> Contributed by Ryan Duguid.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `germany-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/germany-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
