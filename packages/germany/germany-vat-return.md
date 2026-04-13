---
name: germany-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a German VAT return (Umsatzsteuer-Voranmeldung / UStVA) for a self-employed individual or very small business operating under the Regelbesteuerung in Germany. Trigger on phrases like "prepare VAT return", "do the German VAT", "fill in UStVA", "create the return", "Umsatzsteuer", "Vorsteuer", or any request involving German VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Germany only and only Regelbesteuerung (standard taxation). Kleinunternehmer, Organschaft, Differenzbesteuerung, partial exemption, and Ist-Versteuerung edge cases are all in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later (for workflow architecture) AND eu-vat-directive v0.1 or later (for EU directive content). ALWAYS read this skill before touching any German VAT work.
version: 2.0
---

# Germany VAT Return Skill (Umsatzsteuer-Voranmeldung / UStVA) v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 -- follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Germany (Federal Republic of Germany) |
| Standard rate | 19% |
| Reduced rate | 7% (food, books, accommodation, local transport under 50 km, water, cultural events) |
| Other rates | 0% photovoltaic installations under 30 kWp (ss12(3) UStG); 5.5% forestry (rare) |
| Zero rate (functional) | Exports (ss4 Nr.1a), intra-EU B2B goods (ss4 Nr.1b), B2B services to EU/non-EU (ss3a(2)) |
| Return form | Umsatzsteuer-Voranmeldung (UStVA) -- advance VAT return |
| Filing portal | https://www.elster.de (electronic only; paper not accepted) |
| Authority | Finanzamt (local tax office); Bundeszentralamt fuer Steuern (BZSt) for USt-IdNr |
| Currency | EUR only |
| Filing frequencies | Monthly (prior year VAT liability > EUR 9,000); Quarterly (EUR 2,000--9,000); Annual only (< EUR 2,000); First 2 years of new business: monthly (mandatory) |
| Deadline | 10th of the month following the return period (extended by 1 month with Dauerfristverlaengerung) |
| Annual declaration | Umsatzsteuererklaerung (USt-E), due 31 July following year (without Steuerberater) or end of February of 2nd following year (with Steuerberater) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later -- MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later -- MUST be loaded** |
| Contributor | DRAFT -- awaiting practitioner validation |
| Validated by | AWAITING VALIDATION -- must be validated by a Steuerberater (licensed tax advisor) in Germany |
| Validation date | Pending |

**Key UStVA Kennzahlen (the boxes you will use most):**

| Kz | Meaning |
|---|---|
| 81 | Taxable domestic supplies at 19% (net amount; tax auto-calculated) |
| 86 | Taxable domestic supplies at 7% (net amount; tax auto-calculated) |
| 35 | Supplies at other tax rates (net) |
| 36 | Tax on Kz 35 (tax amount entered manually) |
| 41 | Intra-Community supplies of goods, zero-rated B2B (net) |
| 43 | Export supplies to non-EU (net, zero-rated) |
| 45 | Other tax-free supplies with input deduction (B2B services to non-EU) |
| 21 | Non-taxable B2B services to EU customers (net, place of supply = recipient country) |
| 48 | Exempt supplies without input deduction (financial, insurance, medical, education, rent) |
| 46 | Reverse charge base -- supplies by foreign businesses, ss13b(1) (net) |
| 47 | Tax on Kz 46 (output VAT self-assessed, tax amount) |
| 84 | Reverse charge base -- domestic ss13b(2) (construction, cleaning, scrap, etc.) (net) |
| 85 | Tax on Kz 84 (output VAT self-assessed, tax amount) |
| 89 | Intra-Community acquisition of goods at 19% (net; tax auto-calculated) |
| 93 | Intra-Community acquisition of goods at 7% (net; tax auto-calculated) |
| 66 | Input VAT from domestic invoices (tax amount) |
| 61 | Input VAT from intra-Community acquisitions (tax amount) |
| 67 | Input VAT from ss13b reverse charge (tax amount) |
| 83 | Total output VAT (derived) |
| 65 | Net advance payment / refund (derived: output minus input) |

**Conservative defaults -- Germany-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 19% |
| Unknown VAT status of a purchase | Not deductible (no Vorsteuerabzug) |
| Unknown counterparty country | Domestic Germany |
| Unknown B2B vs B2C status for EU customer | B2C, charge 19% |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU (Kz 46/47) |
| Unknown blocked-input status (gifts, private use) | Blocked |
| Unknown whether transaction is in scope | In scope |
| Unknown Bewirtung documentation status | Block (treat as undocumented, no recovery) |

**Red flag thresholds -- country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | EUR 5,000 |
| HIGH tax-delta on a single conservative default | EUR 300 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | EUR 10,000 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement (Kontoauszug) for the period in CSV, PDF, or pasted text. Must cover the full filing period. Acceptable from any German or international business bank: Deutsche Bank, Sparkasse, Commerzbank, ING, N26, DKB, Volksbank/Raiffeisenbank, Postbank, Revolut Business, Wise Business, or any other.

**Recommended** -- sales invoices (Ausgangsrechnungen) for the period (especially for intra-EU B2B services and zero-rated supplies), purchase invoices (Eingangsrechnungen) for any input VAT claim above EUR 300, the client's USt-IdNr (DE + 9 digits) or Steuernummer in writing.

**Ideal** -- complete invoice register, EUeR (Einnahmen-Ueberschuss-Rechnung) or BWA, prior period UStVA, Dauerfristverlaengerung status, Sondervorauszahlung amount.

**Refusal policy if minimum is missing -- SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This UStVA was produced from Kontoauszug alone. The reviewer must verify, before approval, that input VAT claims above EUR 300 are supported by compliant Rechnungen (ss14 UStG) and that all reverse-charge classifications match the supplier's invoice."

### Germany-specific refusal catalogue

These refusals apply on top of the EU-wide refusals in `eu-vat-directive` Section 13 (R-EU-1 through R-EU-12). If any trigger fires, stop, output the refusal message verbatim, end the conversation. Refusal is a safety mechanism.

**R-DE-1 -- Kleinunternehmer ss19 UStG.** *Trigger:* client is Kleinunternehmer, or prior-year turnover was <= EUR 25,000 and current-year turnover will not exceed EUR 100,000, and client has not opted into Regelbesteuerung. *Message:* "Kleinunternehmer under ss19 UStG do not charge VAT and cannot recover Vorsteuer. They do not file UStVA advance returns. They must file an annual Umsatzsteuererklaerung only. This skill covers Regelbesteuerung clients only. Note: ss13b reverse charge obligations still apply to Kleinunternehmer receiving services from foreign businesses -- escalate to a Steuerberater for those situations."

**R-DE-2 -- Organschaft (VAT group).** *Trigger:* client is part of a VAT group (Organschaft) under ss2(2) Nr.2 UStG, or asks about group registration. *Message:* "Organschaft creates a single taxable entity for VAT purposes. Internal supplies between group members are non-taxable (Innenumsaetze). The Organtraeger files a single UStVA for the entire group. This requires Steuerberater guidance. Out of scope for this skill."

**R-DE-3 -- Differenzbesteuerung (margin scheme).** *Trigger:* client deals in second-hand goods, art, antiques, or collectables under the margin scheme (ss25a UStG). *Message:* "Margin scheme transactions require transaction-level margin computation under ss25a UStG. Out of scope for this skill."

**R-DE-4 -- Partial exemption.** *Trigger:* client makes both taxable supplies and exempt-without-credit supplies (ss4 Nr.8-29 UStG) and the exempt proportion is not de minimis. *Message:* "You make both taxable and exempt supplies. Your input VAT must be apportioned under ss15(4) UStG, which requires an annual pro-rata calculation. Please use a Steuerberater to determine and confirm the pro-rata rate before input VAT is claimed."

**R-DE-5 -- Ist-Versteuerung edge cases.** *Trigger:* client uses cash-basis accounting (Ist-Versteuerung under ss20 UStG) and the period contains timing differences between invoicing and payment that materially affect the return. *Message:* "Ist-Versteuerung timing issues require transaction-by-transaction analysis of payment dates versus invoice dates. This skill assumes Soll-Versteuerung (accrual basis). For Ist-Versteuerung with material timing differences, please use a Steuerberater."

---

## Section 3 -- Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. Do not consult Tier 1 rules -- the table is authoritative for patterns it covers.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement (Kontoauszug). If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 German banks (fees exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| DEUTSCHE BANK | EXCLUDE for bank charges/fees | Financial service, exempt under ss4 Nr.8 UStG |
| SPARKASSE, SPK, KREISSPARKASSE, STADTSPARKASSE | EXCLUDE for bank charges/fees | Same |
| COMMERZBANK, COBA | EXCLUDE for bank charges/fees | Same |
| ING, ING-DIBA | EXCLUDE for bank charges/fees | Same |
| N26, NUMBER26 | EXCLUDE for bank charges/fees | Same |
| DKB, DEUTSCHE KREDITBANK | EXCLUDE for bank charges/fees | Same |
| VOLKSBANK, RAIFFEISENBANK, VR BANK | EXCLUDE for bank charges/fees | Same |
| POSTBANK | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| ZINSEN, ZINSERTRAG, HABENZINSEN | EXCLUDE | Interest income/expense, out of scope |
| DARLEHEN, KREDIT, TILGUNG | EXCLUDE | Loan principal movement, out of scope |
| KONTOGEBÜHR, KONTOFÜHRUNG, ENTGELT | EXCLUDE | Account maintenance fee, exempt financial service |

### 3.2 German government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| FINANZAMT, FA | EXCLUDE | Tax payment (Umsatzsteuer, Einkommensteuer, Gewerbesteuer), not a supply |
| BUNDESKASSE, BUNDESZENTRALAMT | EXCLUDE | Federal treasury / BZSt, tax payments |
| IHK, INDUSTRIE- UND HANDELSKAMMER | EXCLUDE | Chamber of commerce membership fees, sovereign act |
| HWK, HANDWERKSKAMMER | EXCLUDE | Trades chamber fees, sovereign act |
| GEZ, RUNDFUNKBEITRAG, BEITRAGSSERVICE | EXCLUDE | Broadcasting levy, not a VATable supply |
| GEWERBEAMT, ORDNUNGSAMT, STADTVERWALTUNG | EXCLUDE | Government fee, sovereign act |
| BERUFSGENOSSENSCHAFT, BG | EXCLUDE | Statutory accident insurance, social security |
| ZOLLAMT, ZOLL | EXCLUDE for duties; EUSt (import VAT) may be recoverable -- flag for reviewer |

### 3.3 German utilities

| Pattern | Treatment | Kz | Notes |
|---|---|---|---|
| STADTWERKE | Domestic 19% | 66 | Electricity, gas, water -- standard rated overhead |
| TELEKOM, DEUTSCHE TELEKOM, T-MOBILE | Domestic 19% | 66 | Telecoms/broadband -- overhead |
| VODAFONE, VODAFONE DEUTSCHLAND | Domestic 19% | 66 | Telecoms -- overhead |
| O2, TELEFONICA DEUTSCHLAND | Domestic 19% | 66 | Telecoms -- overhead |
| 1&1, UNITED INTERNET | Domestic 19% | 66 | Internet/hosting -- overhead |
| CONGSTAR, ALDI TALK, SIMYO | Domestic 19% | 66 | Mobile -- overhead |
| STROM, GAS, ENERGIEVERSORGUNG, E.ON, RWE, VATTENFALL, ENBW | Domestic 19% | 66 | Energy supplier -- overhead |

### 3.4 German insurance (exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ALLIANZ | EXCLUDE | Insurance, exempt under ss4 Nr.10 UStG |
| HUK-COBURG, HUK COBURG | EXCLUDE | Same |
| DEVK | EXCLUDE | Same |
| AXA VERSICHERUNG, ZURICH, ERGO, GENERALI | EXCLUDE | Same |
| VERSICHERUNG, VERSICHERUNGSBEITRAG | EXCLUDE | All insurance premiums exempt |
| KRANKENVERSICHERUNG (private, e.g. DKV, DEBEKA) | EXCLUDE | Private health insurance, exempt |

### 3.5 German transport

| Pattern | Treatment | Kz | Notes |
|---|---|---|---|
| DB, DEUTSCHE BAHN | Domestic 7% for tickets (Fernverkehr and Nahverkehr) | 66 | Passenger transport at 7% (ss12(2) Nr.10 for Nahverkehr <= 50 km; Fernverkehr also 7% since 2020 permanent) |
| BVG, MVG, MVV, RMV, VBB, KVB, SSB, VRS, HVV | Domestic 7% | 66 | Local public transport at 7% |
| UBER, FREENOW, BOLT (DE) | Domestic 19% | 66 | Ride-hailing platform fee at 19% |
| ADAC | Domestic 19% for membership/services | 66 | Not insurance -- ADAC membership is taxable |
| FLIXBUS, FLIXTRAIN | Domestic 7% | 66 | Long-distance transport at 7% |
| SIXT, EUROPCAR, ENTERPRISE, AVIS (car rental DE) | Domestic 19% | 66 | Vehicle rental at 19%; business use portion only |

### 3.6 German food/supermarkets (blocked unless hospitality)

| Pattern | Treatment | Notes |
|---|---|---|
| ALDI, ALDI SUED, ALDI NORD | Default BLOCK input VAT | Personal provisioning. Deductible only if hospitality/catering business where food is stock in trade. |
| LIDL | Default BLOCK | Same |
| REWE | Default BLOCK | Same |
| EDEKA | Default BLOCK | Same |
| DM, ROSSMANN, MUELLER DROGERIE | Default BLOCK | Personal care, default not business |
| PENNY, NETTO, KAUFLAND, REAL | Default BLOCK | Same |
| RESTAURANT, GASTSTÄTTE, IMBISS (any named) | Domestic 19%, RECOVERABLE only if Bewirtungsbeleg complete | See Section 5 rule 5.3 for Bewirtung documentation requirements |

### 3.7 German rent

| Pattern | Treatment | Kz | Notes |
|---|---|---|---|
| MIETE (commercial, landlord opted to charge VAT under ss9 UStG) | Domestic 19% | 66 | Commercial lease where landlord exercised option to tax |
| MIETE, WOHNUNGSMIETE (residential) | EXCLUDE | Residential lease exempt under ss4 Nr.12 UStG, no input deduction |
| BÜROMIETE, GEWERBEMIETE | Domestic 19% if VAT shown on invoice | 66 | Commercial office rent -- confirm VAT is charged |
| NEBENKOSTEN, BETRIEBSKOSTEN | Check invoice | 66 | Service charges may include VAT; confirm with invoice |

### 3.8 SaaS EU suppliers (reverse charge, Kz 46/47)

These are billed from EU entities (typically Ireland or Luxembourg) and trigger ss13b(1) reverse charge. The recipient self-assesses output VAT (Kz 46/47) and claims input VAT (Kz 67). Net effect zero for fully taxable clients.

| Pattern | Billing entity | Kz (base/output/input) | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 46/47/67 | Reverse charge services |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 46/47/67 | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 46/47/67 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 46/47/67 | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 46/47/67 | Reverse charge |
| SPOTIFY | Spotify AB (SE) | 46/47/67 | EU, reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | 46/47/67 | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | 46/47/67 | Reverse charge |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | 46/47/67 | EU, reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | 46/47/67 | Reverse charge |
| CANVA | Canva Pty Ltd (AU) billed via IE entity in some cases | 46/47/67 | Check invoice -- if IE entity, EU reverse charge |

### 3.9 SaaS non-EU suppliers (reverse charge, Kz 46/47)

| Pattern | Billing entity | Kz (base/output/input) | Notes |
|---|---|---|---|
| AWS | AWS EMEA SARL (LU) -- EU entity | 46/47/67 | LU entity = EU reverse charge. Same Kz 46/47 as other foreign suppliers under ss13b(1) |
| NOTION | Notion Labs Inc (US) | 46/47/67 | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 46/47/67 | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 46/47/67 | Non-EU reverse charge |
| GITHUB (standard plans) | GitHub Inc (US) | 46/47/67 | Check if billed by IE entity |
| FIGMA | Figma Inc (US) | 46/47/67 | Non-EU reverse charge |
| HUBSPOT | HubSpot Inc (US) or HubSpot Ireland Ltd (IE) -- check invoice | 46/47/67 | Depends on billing entity; same Kz regardless |
| TWILIO | Twilio Inc (US) | 46/47/67 | Non-EU reverse charge |
| VERCEL, NETLIFY, HEROKU | US entities | 46/47/67 | Non-EU reverse charge |

**Note:** Under German law, ss13b(1) uses the same Kennzahlen (Kz 46/47/67) for both EU and non-EU foreign suppliers. Unlike Malta, there is no separate box for EU vs non-EU reverse charge. The distinction matters only for the Zusammenfassende Meldung (ZM / EC Sales List), which reports EU transactions only.

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services under ss4 Nr.8 UStG |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same -- PayPal Europe S.a r.l. (LU), exempt financial service |
| STRIPE (monthly subscription) | EU reverse charge Kz 46/47/67 | Stripe Technology Europe Ltd (IE) -- separate from transaction fees |
| SUMUP, ZETTLE, SQUARE | Check invoice | If German entity: domestic 19% Kz 66; if IE/EU entity: reverse charge Kz 46/47/67 |
| KLARNA (merchant fees) | EXCLUDE (exempt) | Financial service, exempt |

### 3.11 Professional services (Germany)

| Pattern | Treatment | Kz | Notes |
|---|---|---|---|
| STEUERBERATER, STEUERKANZLEI, TAX ADVISOR | Domestic 19% | 66 | Always deductible business overhead |
| RECHTSANWALT, KANZLEI, ANWALT, ANWALTSKANZLEI | Domestic 19% | 66 | Deductible if business legal matter |
| NOTAR, NOTARIAT | Domestic 19% | 66 | Notarial fees for business purposes |
| WIRTSCHAFTSPRÜFER, WP | Domestic 19% | 66 | Audit/accounting fees |
| UNTERNEHMENSBERATER, BERATUNG | Domestic 19% | 66 | Consulting fees |
| HANDELSREGISTER, AMTSGERICHT | EXCLUDE | Court/registry fees, sovereign act |

### 3.12 Payroll and social security contributions (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| KRANKENVERSICHERUNG (statutory: AOK, TK, BARMER, DAK, IKK) | EXCLUDE | Statutory health insurance contribution |
| RENTENVERSICHERUNG, DRV | EXCLUDE | Statutory pension contribution |
| PFLEGEVERSICHERUNG | EXCLUDE | Long-term care insurance contribution |
| FINANZAMT LOHNSTEUER, LOHNSTEUER | EXCLUDE | PAYE tax remittance |
| GEHALT, LOHN, LOHNZAHLUNG | EXCLUDE | Wages paid to employees, outside VAT scope |
| AGENTUR FUER ARBEIT, ARBEITSLOSENVERSICHERUNG | EXCLUDE | Unemployment insurance contribution |
| KNAPPSCHAFT, MINIJOBZENTRALE | EXCLUDE | Minijob social contributions |

### 3.13 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| UMBUCHUNG, EIGENE UEBERWEISUNG, KONTOÜBERTRAG | EXCLUDE | Internal movement between own accounts |
| DAUERAUFTRAG (to own account) | EXCLUDE | Standing order to own account |
| PRIVATEINLAGE, EINLAGE | EXCLUDE | Owner injection of capital |
| PRIVATENTNAHME, ENTNAHME | EXCLUDE | Owner drawing |
| DIVIDENDE | EXCLUDE | Dividend payment, out of scope |
| DARLEHEN, TILGUNG, KREDIT | EXCLUDE | Loan principal, out of scope |
| BARGELDABHEBUNG, GELDAUTOMAT, ATM | TIER 2 -- ask | Default exclude; ask what cash was spent on |
| GUTSCHRIFT STORNO, STORNIERUNG, RÜCKLASTSCHRIFT | Reverse of original | Book as negative in same Kz as original transaction |

---

## Section 4 -- Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement (Kontoauszug) of a Germany-based self-employed IT consultant (Einzelunternehmer, Regelbesteuerung). They illustrate the trickiest cases. Pattern-match against these when you encounter similar lines in any real statement.

### Example 1 -- Non-EU SaaS reverse charge (OpenAI)

**Input line (Sparkasse Kontoauszug format):**
```
Buchungstag: 05.04.2026
Wertstellung: 05.04.2026
Buchungstext: SEPA-Basislastschrift
Verwendungszweck: OPENAI *CHATGPT PLUS 4973857 SAN FRANCISCO US
Betrag: -23,78 EUR
```

**Reasoning:**
OpenAI Inc is a US entity (Section 3.9). No VAT on the invoice. This is a service received from a non-EU supplier. ss13b(1) reverse charge applies. Place of supply is Germany under ss3a(2) UStG (B2B general rule). Both sides of the reverse charge must be reported: Kz 46 (base), Kz 47 (output VAT at 19%), Kz 67 (input VAT). Net effect zero for a fully taxable client.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Kz (base) | Kz (output) | Kz (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | OPENAI INC | -23.78 | -23.78 | 4.52 | 19% | 46 | 47 | 67 | N | -- | -- |

### Example 2 -- EU service, reverse charge (Google Ads)

**Input line:**
```
Buchungstag: 10.04.2026
Wertstellung: 10.04.2026
Buchungstext: SEPA-Basislastschrift
Verwendungszweck: GOOGLE IRELAND LTD GOOGLE ADS CID:123-456-7890
IBAN: IE29AIBK93115212345678
Betrag: -1.200,00 EUR
```

**Reasoning:**
Google Ireland Limited is an IE entity (IBAN confirms IE). Standard EU reverse charge under ss13b(1). Google Ads is a service. Kz 46 for the net base, Kz 47 for output VAT self-assessed at 19%, Kz 67 for input VAT. The gross amount is treated as the net (Google invoices net of VAT to VAT-registered EU clients). Both sides must appear on the return. Also report in ZM (Zusammenfassende Meldung) as an EU service received.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Kz (base) | Kz (output) | Kz (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LTD | -1,200.00 | -1,200.00 | 228.00 | 19% | 46 | 47 | 67 | N | -- | -- |

### Example 3 -- Bewirtung (business entertainment), fully recoverable

**Input line:**
```
Buchungstag: 15.04.2026
Wertstellung: 15.04.2026
Buchungstext: Kartenzahlung
Verwendungszweck: RESTAURANT ZUM GOLDENEN HIRSCH MUENCHEN
Betrag: -285,60 EUR
```

**Reasoning:**
Restaurant transaction. Unlike Malta where entertainment VAT is hard-blocked, in Germany business entertainment (Bewirtung) VAT is 100% recoverable under ss15(1) Nr.1 UStG -- provided proper documentation exists: maschinell erstellte Rechnung, attendees listed on back of receipt, business purpose noted, host's signature. The 30% disallowance is an income tax rule only (ss4(5) Nr.2 EStG), NOT a VAT rule. Gross EUR 285.60 includes 19% VAT. Net = EUR 240.00, VAT = EUR 45.60. Default: BLOCK (conservative -- Bewirtungsbeleg documentation unknown). Flag for reviewer.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Kz (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTAURANT ZUM GOLDENEN HIRSCH | -285.60 | -240.00 | 0 | 19% | -- | Y | Q1 | "Bewirtung: do you have a properly completed Bewirtungsbeleg? If yes, EUR 45.60 Vorsteuer is recoverable via Kz 66." |

### Example 4 -- Domestic purchase, standard 19%

**Input line:**
```
Buchungstag: 18.04.2026
Wertstellung: 18.04.2026
Buchungstext: SEPA-Basislastschrift
Verwendungszweck: DEUTSCHE TELEKOM AG RECHNUNG APR 2026 KD-NR 12345
Betrag: -59,95 EUR
```

**Reasoning:**
Deutsche Telekom is a domestic German supplier (Section 3.3). Telecoms at 19%. Gross EUR 59.95 includes 19% VAT. Net = EUR 50.38, VAT = EUR 9.57. Full input VAT deduction as business overhead via Kz 66, assuming 100% business use. If mixed-use phone line, business proportion applies.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Kz (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | DEUTSCHE TELEKOM AG | -59.95 | -50.38 | -9.57 | 19% | 66 | N | -- | -- |

### Example 5 -- EU B2B service sale (IT consulting to Austrian client)

**Input line:**
```
Buchungstag: 22.04.2026
Wertstellung: 22.04.2026
Buchungstext: SEPA-Gutschrift
Verwendungszweck: KREATIV DIGITAL GMBH WIEN RE-2026-042 IT BERATUNG MAERZ
IBAN: AT611904300234573201
Betrag: +4.500,00 EUR
```

**Reasoning:**
Incoming EUR 4,500 from an Austrian company (AT IBAN). The client is providing IT consulting services (B2B). Place of supply for services under ss3a(2) UStG is the customer's country (Austria). The client invoices at 0% with a reverse-charge note, the Austrian customer accounts for reverse charge in Austria. Report net amount in Kz 21 (non-taxable B2B services to EU). No output VAT. Also report in ZM. Confirm: (a) customer is VAT-registered -- ask for ATU number; (b) the invoice shows no German VAT with a reverse-charge note citing ss3a(2) UStG. If the customer cannot provide a valid ATU number, reclassify as B2C and charge German 19%.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Kz | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | KREATIV DIGITAL GMBH WIEN | +4,500.00 | +4,500.00 | 0 | 0% | 21 | Y | Q2 (HIGH) | "Verify Austrian USt-IdNr (ATU format)" |

### Example 6 -- Bank fee and insurance (excluded)

**Input line:**
```
Buchungstag: 30.04.2026
Wertstellung: 30.04.2026
Buchungstext: Abschluss
Verwendungszweck: KONTOFÜHRUNGSGEBÜHR Q2/2026
Betrag: -12,90 EUR

Buchungstag: 30.04.2026
Buchungstext: SEPA-Basislastschrift
Verwendungszweck: ALLIANZ VERSICHERUNG BETRIEBSHAFTPFLICHT POLICE 12345
Betrag: -89,50 EUR
```

**Reasoning:**
Bank fee: exempt financial service under ss4 Nr.8 UStG (Section 3.1). Exclude entirely. Insurance: exempt under ss4 Nr.10 UStG (Section 3.4). Exclude entirely. Neither generates input VAT nor appears on the UStVA.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Kz | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | SPARKASSE KONTOFÜHRUNG | -12.90 | -- | -- | -- | -- | N | -- | EXCLUDE: exempt bank fee |
| 30.04.2026 | ALLIANZ VERSICHERUNG | -89.50 | -- | -- | -- | -- | N | -- | EXCLUDE: exempt insurance |

---

## Section 5 -- Tier 1 classification rules (compressed)

Each rule states the legal source and the Kennzahl mapping. Apply silently if the data is unambiguous. For full doctrinal context, see the source citations in Section 10.

### 5.1 Standard rate 19% (ss12(1) UStG)

Default rate for any taxable supply unless a reduced rate, zero rate, or exemption applies. Sales: Kz 81 (net; tax auto-calculated). Purchases: Kz 66 (enter tax amount).

### 5.2 Reduced rate 7% (ss12(2) UStG)

Applies to: food (excluding restaurant service, alcohol, luxury food), books (including e-books since 2020), newspapers, water supply, cut flowers and plants, accommodation (short-term, excluding breakfast/parking/Wi-Fi which are 19%), local public transport (Nahverkehr <= 50 km), cultural admissions (theatre, concert, museum, zoo), passenger transport (Fernverkehr, permanent 7%). Sales: Kz 86 (net; tax auto-calculated). Purchases: Kz 66 (enter tax amount at 7%).

### 5.3 Bewirtung (business entertainment) -- VAT fully recoverable

This is a commonly misunderstood rule. Unlike Malta and Ireland where entertainment VAT is blocked, in Germany:

- VAT on business entertainment IS 100% recoverable under ss15(1) Nr.1 UStG, provided:
  - A proper VAT invoice exists (maschinell erstellte Rechnung from the restaurant)
  - The back of the receipt documents: date, names of attendees, business purpose, and the host's signature
  - The entertainment has a concrete business reason (Bewirtung aus geschaeftlichem Anlass)

- The 30% disallowance is ONLY an income tax rule under ss4(5) Nr.2 EStG. It does NOT affect VAT recovery.

- Example: Business dinner EUR 200 net + EUR 38 VAT (19%). Kz 66 = EUR 38 (full VAT recovery). For income tax: only EUR 140 (70% of EUR 200) is deductible.

- **Conservative default when documentation status is unknown: BLOCK.** Only recover if the client confirms the Bewirtungsbeleg is properly completed.

### 5.4 Zero-rated and tax-free with input deduction

Exports outside EU: Kz 43 (zero-rated, requires customs export documentation). Intra-EU B2B supplies of goods: Kz 41 (zero-rated, requires customer USt-IdNr verified on VIES, transport proof, Gelangensbestaetigung or equivalent under ss17a-17c UStDV). B2B services to EU customers: Kz 21 (place of supply is customer's country under ss3a(2), no German VAT, requires customer USt-IdNr, report in ZM). B2B services to non-EU customers: Kz 45 (zero-rated, no German VAT).

### 5.5 Exempt without input deduction (ss4 Nr.8-29 UStG)

Financial services, insurance, residential rent, healthcare, education, social welfare, universal postal service. These supplies go to Kz 48. No output VAT, no input VAT deduction on related costs. If these are significant, partial exemption rules apply -- **R-DE-4 refuses** if non-de-minimis.

### 5.6 Reverse charge -- foreign suppliers (ss13b(1) UStG)

When the client receives a supply (goods or services) from a business not established in Germany and the supply is taxable in Germany: net base goes to Kz 46, output VAT self-assessed in Kz 47, input VAT in Kz 67. This applies to both EU and non-EU suppliers. Net cash effect zero for a fully taxable client. If the EU supplier incorrectly charged their local VAT (e.g. Irish 23%), that is NOT reverse charge -- treat as an overhead expense with irrecoverable foreign VAT.

### 5.7 Reverse charge -- domestic ss13b(2) UStG

Construction services (Bauleistungen), building cleaning, scrap metal, gold, gas/electricity from foreign suppliers, mobile phones/tablets > EUR 5,000 net, emission certificates. Kz 84 (base), Kz 85 (output VAT), Kz 67 (input VAT). Construction reverse charge applies ONLY when both supplier and recipient are in the construction trade (Bauleistender).

### 5.8 Intra-Community acquisition of goods (ss1a UStG)

B2B purchase of goods shipped from another EU state to Germany. Kz 89 (19%) or Kz 93 (7%) for the net base; tax auto-calculated. Input VAT via Kz 61. Net effect zero. Also report in Intrastat if above threshold (arrivals > EUR 800,000/year).

### 5.9 Import VAT (Einfuhrumsatzsteuer / EUSt)

Physical goods imported from non-EU countries. EUSt is paid to Zoll (customs) at the border, NOT self-assessed on the UStVA. Recoverable as input tax -- the Kz for recovery should be confirmed by Steuerberater (historically Kz 62 or Kz 66 with customs document). Requires Einfuhrabgabenbescheid (customs assessment notice).

### 5.10 Blocked input VAT

The following categories have restricted or zero VAT recovery:
- Business gifts > EUR 50 net per person per year (ss15(1a) Nr.1 UStG) -- hard block on ALL gifts to that recipient (not just excess)
- Hunting, fishing, yachts, guest houses, similar luxury (ss15(1a) Nr.1 UStG; ss4(5) Nr.1-4 EStG)
- Private use portion of mixed-use assets (vehicle, phone, home office) -- only business proportion deductible
- Purchases related to exempt supplies (ss15(2) UStG)
- Purchases without a proper invoice (ss15(1) Nr.1 UStG -- invoice requirement under ss14)

**Entertainment (Bewirtung) is NOT blocked** -- see rule 5.3 above. Motor vehicles are NOT fully blocked -- see Section 6.1 for the Tier 2 treatment of business/private split.

### 5.11 Private use deemed supply (unentgeltliche Wertabgabe)

If the client uses a business asset for private purposes, output VAT must be charged on the private-use portion as a deemed supply under ss3(1b) UStG (goods) or ss3(9a) UStG (services/ongoing use). The VAT base is the actual cost, not the income tax 1%-Regelung figure. Report in Kz 81 or dedicated Kz. Tier 2 -- Steuerberater must confirm the calculation method and correct Kz.

### 5.12 Photovoltaic installations at 0% (ss12(3) UStG)

Supply and installation of PV systems under 30 kWp on or near dwellings: 0% VAT since 1 January 2023. The supply is taxable at 0%, NOT exempt -- the supplier retains full input deduction rights. Purchaser pays no VAT.

### 5.13 Credit notes and corrections

Gutschrift (ss14 UStG): self-billing by the buyer, creates output tax for the supplier. Stornorechnung / Rechnungskorrektur: correction by the supplier to cancel or amend a previous invoice. Both reduce the original Kz entries. A correction in period 2 for a period 1 invoice: adjust the relevant Kz in period 2 by the negative amounts.

### 5.14 Sales -- cross-border B2C

Goods to EU consumers above EUR 10,000 EU-wide threshold: **R-EU-5 (OSS refusal) from eu-vat-directive fires**. Digital services to EU consumers above EUR 10,000: same. Below threshold: German VAT at applicable rate, Kz 81/86.

### 5.15 Dauerfristverlaengerung and Sondervorauszahlung

If granted, filing deadline extends by 1 month. Client must pay Sondervorauszahlung (1/11 of prior year's VAT liability) by 10 February. The Sondervorauszahlung is credited back in the last Voranmeldung of the year via Kz 39, deducted from the final Kz 65 result.

---

## Section 6 -- Tier 2 catalogue (compressed)

For each ambiguity type: pattern, why the Kontoauszug is insufficient, conservative default, question for the structured form.

### 6.1 Vehicle costs

*Pattern:* ARAL, SHELL, TOTAL, ESSO, JET, AGIP, STAR, Tankstelle charge; ADAC Pannenhilfe; TÜV. *Why insufficient:* vehicle type and business-use proportion unknown. Unlike Malta, German VAT does not hard-block motor vehicles -- but the business/private split determines deductibility. If 100% business: full recovery. If mixed: only business proportion recoverable, and private portion triggers deemed supply output VAT under ss3(9a). *Default:* 0% recovery. *Question:* "Is this vehicle used exclusively for business? If mixed-use, what is the business percentage? Do you keep a Fahrtenbuch or use the 1%-Regelung?"

### 6.2 Bewirtungskosten

*Pattern:* any named restaurant, Gaststätte, Imbiss, Hotel restaurant. *Why insufficient:* Bewirtungsbeleg documentation status unknown. VAT is fully recoverable IF properly documented (attendees, business purpose, signature on back of receipt). Without documentation, Finanzamt will deny the deduction. *Default:* block (no recovery). *Question:* "Do you have a properly completed Bewirtungsbeleg for this meal? (Attendees listed, business purpose noted, your signature on the back of the maschinell erstellte Rechnung?)"

### 6.3 Home office (Arbeitszimmer)

*Pattern:* Miete, Strom, Internet charges that could relate to a home office. *Why insufficient:* home office deductibility in Germany requires either a dedicated room (abgetrenntes Arbeitszimmer) with no private use, or the Tagespauschale (EUR 6/day, max EUR 1,260/year for income tax -- but this is an income tax concept, not VAT). For VAT, only a proportional share of utilities/rent is deductible if the home office qualifies. *Default:* 0% recovery for home-related costs. *Question:* "Do you have a dedicated home office room (separate room used exclusively for business)? What percentage of total living space does it represent?"

### 6.4 Cash withdrawals (Bargeldabhebung)

*Pattern:* ATM, Geldautomat, Bargeldabhebung, Kassenbeleg. *Why insufficient:* unknown what cash was spent on. *Default:* exclude as owner drawing (Privatentnahme). *Question:* "What was the cash withdrawal used for? If business purchases, do you have receipts?"

### 6.5 Mixed SaaS billing entity

*Pattern:* Google, Microsoft, Adobe, Meta, Slack, Zoom, LinkedIn, Apple, Amazon, Dropbox, Atlassian, Stripe, PayPal where the legal entity is not visible in the Kontoauszug. *Why insufficient:* same brand can bill from Ireland (EU reverse charge Kz 46/47), US (non-EU reverse charge Kz 46/47), or Germany (domestic 19% Kz 66). While the Kz is the same for EU and non-EU foreign suppliers, the treatment differs if the supplier has a German establishment. *Default:* reverse charge from non-EU (Kz 46/47 -- most conservative). *Question:* "Could you check the most recent invoice from each SaaS provider? I need the legal entity name, country, and whether it shows German VAT (Umsatzsteuer) or a reverse-charge note."

### 6.6 Round-number transfers (Gesellschaftereinlage or Umsatz?)

*Pattern:* large round incoming credit from a name matching the client's name or a family member. *Why insufficient:* could be a customer sale (Umsatz), owner injection (Privateinlage), or family loan. *Default:* exclude as Privateinlage. *Question:* "The EUR X transfer from [name] -- is this a customer payment, your own money going in (Einlage), or a loan?"

### 6.7 Amazon purchases

*Pattern:* AMAZON, AMAZON PAYMENTS, AMAZON EU SARL, AMZN MKTP. *Why insufficient:* Amazon purchases could be business supplies (deductible at 19% or 7% depending on item) or personal (blocked). Additionally, Amazon may bill from Luxembourg (Amazon EU S.a r.l.), Germany (Amazon.de GmbH), or US entities. *Default:* block (personal). *Question:* "Was this Amazon purchase for business or personal use? If business, what was the item?"

---

## Section 7 -- Excel working paper template (Germany-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Germany-specific overlay.

### Sheet "Transactions"

Columns A-L per the base. Column H ("Kz code") accepts only valid German UStVA Kennzahl codes from Section 1 of this skill. Use blank for excluded transactions. For reverse-charge transactions, enter the base Kz (e.g. 46), the output Kz (e.g. 47), and the input Kz (e.g. 67) separated by slashes in column H.

### Sheet "Kz Summary"

One row per Kennzahl. Column A is the Kz number, column B is the description, column C is the value computed via formula. Mandatory rows:

```
Output tax (domestic sales):
| 81  | Taxable supplies 19% (net)         | =SUMIFS(Transactions!E:E, Transactions!H:H, "81")  |
| T81 | Tax on Kz 81                        | =Kz_Summary!C[81_row]*0.19                          |
| 86  | Taxable supplies 7% (net)          | =SUMIFS(Transactions!E:E, Transactions!H:H, "86")  |
| T86 | Tax on Kz 86                        | =Kz_Summary!C[86_row]*0.07                          |
| 35  | Supplies at other rates (net)      | =SUMIFS(Transactions!E:E, Transactions!H:H, "35")  |
| 36  | Tax on Kz 35                        | entered manually                                     |

Zero-rated / exempt:
| 41  | IC supplies of goods (net)         | =SUMIFS(Transactions!E:E, Transactions!H:H, "41")  |
| 43  | Export supplies (net)              | =SUMIFS(Transactions!E:E, Transactions!H:H, "43")  |
| 21  | B2B services to EU (net)          | =SUMIFS(Transactions!E:E, Transactions!H:H, "21")  |
| 45  | Other tax-free with deduction     | =SUMIFS(Transactions!E:E, Transactions!H:H, "45")  |
| 48  | Exempt without deduction (net)    | =SUMIFS(Transactions!E:E, Transactions!H:H, "48")  |

Intra-Community acquisitions:
| 89  | IC acquisitions 19% (net)         | =SUMIFS(Transactions!E:E, Transactions!H:H, "89")  |
| T89 | Tax on Kz 89                       | =Kz_Summary!C[89_row]*0.19                          |
| 93  | IC acquisitions 7% (net)          | =SUMIFS(Transactions!E:E, Transactions!H:H, "93")  |
| T93 | Tax on Kz 93                       | =Kz_Summary!C[93_row]*0.07                          |

Reverse charge (ss13b):
| 46  | Foreign supplier base (net)       | =SUMIFS(Transactions!E:E, Transactions!H:H, "46")  |
| 47  | Tax on Kz 46                       | =Kz_Summary!C[46_row]*0.19                          |
| 84  | Domestic ss13b(2) base (net)      | =SUMIFS(Transactions!E:E, Transactions!H:H, "84")  |
| 85  | Tax on Kz 84                       | =Kz_Summary!C[84_row]*0.19                          |

Input tax:
| 66  | Input VAT domestic invoices        | =SUMIFS(Transactions!F:F, Transactions!H:H, "66")  |
| 61  | Input VAT IC acquisitions          | =C[T89_row]+C[T93_row]                              |
| 67  | Input VAT ss13b reverse charge     | =C[47_row]+C[85_row]                                |

Totals:
| 83  | Total output VAT                   | =C[T81]+C[T86]+C[36]+C[T89]+C[T93]+C[47]+C[85]    |
| TIN | Total input VAT                    | =C[66]+C[61]+C[67]                                  |
| 65  | Net advance payment / refund       | =C[83]-C[TIN]                                       |
```

### Sheet "Return Form"

Final UStVA-ready figures. The bottom-line cell is Kz 65:

```
Kz 83 = Total output VAT
TIN   = Total input VAT

IF TIN > Kz 83:
  Kz 65 = negative (Erstattungsanspruch / refund claim)
ELSE:
  Kz 65 = positive (Zahllast / tax payable)

If Dauerfristverlaengerung applies (last period of year):
  Kz 65 = (Kz 83 - TIN) - Kz 39 (Sondervorauszahlung credit)
```

Positive Kz 65 = payable to Finanzamt. Negative = refund claim.

### Color and formatting conventions

Per the xlsx skill: blue for hardcoded values from the bank statement (column D of Transactions), black for formulas (everything in Kz Summary and Return Form), green for cross-sheet references (Return Form referencing Kz Summary), yellow background for any row in Sheet "Transactions" where Default? = "Y".

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/germany-vat-<period>-working-paper.xlsx
```

Check the JSON output. If `status` is `errors_found`, fix the formulas and re-run. If `status` is `success`, present via `present_files`.

---

## Section 8 -- German bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Germany-specific patterns.

### Kontoauszug format conventions

German bank statements (Kontoauszuege) follow a standard structure across all banks, though CSV column names vary:

| Field | Meaning | Notes |
|---|---|---|
| Buchungstag | Booking date | The date the transaction was posted to the account. Use this as the transaction date for UStVA purposes. DD.MM.YYYY format. |
| Wertstellung / Valuta | Value date | The date used for interest calculation. May differ from Buchungstag by 1-2 days. Not relevant for VAT classification. |
| Buchungstext | Transaction type | Standardised codes: SEPA-Ueberweisung, SEPA-Basislastschrift, SEPA-Gutschrift, Kartenzahlung, Dauerauftrag, Abschluss, Gehalt/Lohn. Use this to identify the transaction mechanism. |
| Verwendungszweck | Purpose / reference | Free-text field containing the payment reference, invoice number, customer/supplier name, and other details. This is the primary field for counterparty identification. |
| Begünstigter / Auftraggeber | Payee / payer | The counterparty name. In SEPA transactions, this is the registered account holder name. |
| IBAN | Counterparty IBAN | DE = Germany. Country prefix identifies the counterparty location for EU reverse charge determination. |
| BIC / SWIFT | Bank code | Identifies the counterparty's bank. Useful for confirming country when IBAN prefix is ambiguous. |
| Betrag | Amount | Negative = outgoing (debit). Positive = incoming (credit). German number format: dot for thousands separator, comma for decimal (e.g. -1.200,50 = minus one thousand two hundred euros and fifty cents). |
| Saldo | Balance | Running account balance after the transaction. |

### IBAN country prefixes

| Prefix | Country | VAT treatment |
|---|---|---|
| DE | Germany | Domestic |
| AT, BE, BG, CY, CZ, DK, EE, ES, FI, FR, GR, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK | EU member states | EU reverse charge (ss13b(1)) for B2B services; IC acquisition for goods |
| GB, US, CH, AU, NO, CA, JP | Non-EU | Non-EU reverse charge (ss13b(1)) |

### Common Buchungstext codes

| Code | Meaning | Typical treatment |
|---|---|---|
| SEPA-Ueberweisung | Outgoing bank transfer | Supplier payment -- classify by counterparty |
| SEPA-Gutschrift | Incoming bank transfer | Customer payment / income -- classify as sales |
| SEPA-Basislastschrift | Direct debit | Recurring supplier charges (telecoms, SaaS, insurance) |
| Kartenzahlung / EC-Zahlung | Card payment | Point-of-sale purchase (office supplies, restaurant, petrol) |
| Dauerauftrag | Standing order | Recurring fixed payment (rent, subscriptions) |
| Abschluss | Account settlement | Bank fees, interest -- typically EXCLUDE |
| Gehalt/Lohn | Salary payment | Employee wages -- EXCLUDE |
| Lastschrift Finanzamt | Tax authority direct debit | Tax payment -- EXCLUDE |

### German-language transaction descriptions

Common German words in Verwendungszweck and their meaning for classification:

| German | English | Classification hint |
|---|---|---|
| Rechnung, Rg., RE | Invoice | Purchase or sale with invoice reference |
| Miete | Rent | See Section 3.7 |
| Gehalt, Lohn | Salary, wages | EXCLUDE |
| Zinsen | Interest | EXCLUDE |
| Versicherung | Insurance | EXCLUDE (exempt) |
| Steuern, USt, MwSt | Tax, VAT | Tax payment = EXCLUDE |
| Beitrag | Contribution/fee | Could be chamber fee (EXCLUDE) or subscription (classify) |
| Gutschrift | Credit note | Reverse of original transaction |
| Rücklastschrift | Returned direct debit | Reversal -- book negative in original Kz |
| Erstattung | Refund | Reverse of original transaction |
| Einlage | Capital injection | EXCLUDE (owner injection) |
| Entnahme | Drawing/withdrawal | EXCLUDE (owner drawing) |

### Internal transfers and exclusions

Own-account transfers between the client's Deutsche Bank, Sparkasse, N26, Revolut accounts. Labelled "Umbuchung", "eigene Ueberweisung", "Kontoübertrag". Always exclude.

### Foreign currency transactions

Convert to EUR at the transaction date rate. Use the ECB reference rate or the rate shown on the bank statement. Note the rate used in the Transactions sheet column L (Notes). German Kontoauszuege from domestic banks typically show amounts already converted to EUR.

### Cryptic descriptions

Card purchases with only a terminal ID; SEPA direct debits with only a Mandatsreferenz (mandate reference). If the counterparty cannot be identified from the Verwendungszweck, ask the client. Do not classify unidentified transactions.

---

## Section 9 -- Onboarding fallback (only when inference fails)

The workflow in `vat-workflow-base` Section 1 mandates inferring the client profile from the data first (Step 3) and only confirming with the client in Step 4. The questionnaire below is a fallback -- ask only the questions the data could not answer.

For each question, the inference rule comes first. Only ask if inference fails.

### 9.1 Entity type and trading name
*Inference rule:* sole trader (Einzelunternehmer) names often match the account holder; company names end in "GmbH", "UG", "GbR", "OHG", "KG", "AG", "e.K.". *Fallback question:* "Are you a self-employed sole trader (Einzelunternehmer/Freiberufler), a GmbH, a UG, or another entity type?"

### 9.2 VAT registration status
*Inference rule:* if the client is asking for a UStVA, they are Regelbesteuerung. If they mention no VAT on sales, they may be Kleinunternehmer -- trigger R-DE-1. *Fallback question:* "Are you under Regelbesteuerung (standard VAT, charging 19%) or Kleinunternehmer (ss19 UStG, no VAT on invoices)?"

### 9.3 USt-IdNr and Steuernummer
*Inference rule:* USt-IdNr (DE + 9 digits) sometimes appears in payment descriptions from EU customers. Steuernummer appears on Finanzamt correspondence. Search statement descriptions first. *Fallback question:* "What is your USt-IdNr (DE + 9 digits) and/or your Steuernummer?"

### 9.4 Filing period and frequency
*Inference rule:* first and last transaction dates on the bank statement determine the period. Filing frequency depends on prior year VAT liability (> EUR 9,000 = monthly; EUR 2,000-9,000 = quarterly; < EUR 2,000 = annual). *Fallback question:* "Which period does this cover? Monthly (which month) or quarterly (Q1 Jan-Mar, Q2 Apr-Jun, Q3 Jul-Sep, Q4 Oct-Dec)?"

### 9.5 Industry and sector
*Inference rule:* counterparty mix, sales description patterns, invoice descriptions. IT, consulting, trades, hospitality, retail, medical are recognisable. *Fallback question:* "In one sentence, what does the business do?"

### 9.6 Employees
*Inference rule:* Gehalt, Lohn, Sozialversicherung outgoing transfers to non-owner names. *Fallback question:* "Do you have employees? If so, how many?"

### 9.7 Exempt supplies
*Inference rule:* presence of medical/financial/educational/residential rental income. *Fallback question:* "Do you make any VAT-exempt sales (medical, education, insurance, financial services, residential lettings)?" *If yes and non-de-minimis: R-DE-4 refuses.*

### 9.8 Soll- or Ist-Versteuerung
*Inference rule:* most small businesses use Soll (accrual). Ist-Versteuerung (cash basis) requires prior approval and turnover <= EUR 600,000. *Fallback question:* "Are you on Soll-Versteuerung (accrual, default) or Ist-Versteuerung (cash basis, approved by Finanzamt)?" *If Ist with material timing differences: R-DE-5 may fire.*

### 9.9 Dauerfristverlaengerung
*Inference rule:* not inferable from a single period statement. *Fallback question:* "Do you have a Dauerfristverlaengerung (permanent 1-month filing extension)? If so, what is the Sondervorauszahlung amount?"

### 9.10 Cross-border customers
*Inference rule:* foreign IBANs on incoming transfers, foreign currency, foreign-name customers. *Fallback question:* "Do you have customers outside Germany? In EU countries or outside the EU? Are they businesses (B2B with USt-IdNr) or consumers?"

---

## Section 10 -- Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the three-tier Accora architecture (vat-workflow-base + eu-vat-directive + country skill). It supersedes v1.0-draft (April 2026, standalone monolithic skill). The Germany-specific content (Kennzahl mappings, rates, thresholds, blocked categories, reverse charge catalogue) is AWAITING VALIDATION by a Steuerberater (licensed tax advisor) in Germany.

### Sources

**Primary legislation:**
1. Umsatzsteuergesetz (UStG) -- German Value Added Tax Act, especially ss1-3a, ss4, ss9, ss12, ss13b, ss14, ss15, ss15a, ss18, ss19, ss20, ss25a
2. Umsatzsteuer-Durchfuehrungsverordnung (UStDV) -- implementing regulation, especially ss17a-17c (IC supply proof), ss46-48 (Dauerfristverlaengerung)
3. Abgabenordnung (AO) -- General Tax Code, especially ss149, ss152, ss233a, ss238, ss240, ss328, ss370
4. Einkommensteuergesetz (EStG) -- ss4(5) (entertainment/gifts income tax disallowance, cross-referenced for VAT blocked input)

**Authority guidance:**
5. BMF (Bundesministerium der Finanzen) official form guidance for UStVA
6. ELSTER filing system -- https://www.elster.de
7. BZSt USt-IdNr verification -- https://evatr.bff-online.de

**EU directive (loaded via companion skill):**
8. Council Directive 2006/112/EC (Principal VAT Directive) -- implemented via eu-vat-directive companion skill
9. Council Implementing Regulation 282/2011

**Other:**
10. VIES validation -- https://ec.europa.eu/taxation_customs/vies/
11. ECB euro reference rates -- https://www.ecb.europa.eu/stats/eurofxref/
12. PWC Tax Summaries Germany -- https://taxsummaries.pwc.com/germany/corporate/other-taxes (used for threshold verification)

### Key thresholds summary

| Threshold | Value | Source |
|---|---|---|
| Kleinunternehmer prior-year turnover | EUR 25,000 | ss19(1) UStG (as amended 1 Jan 2025) |
| Kleinunternehmer current-year turnover | EUR 100,000 | ss19(1) UStG (as amended 1 Jan 2025; breach = immediate loss of status) |
| Monthly filing trigger | Prior year VAT liability > EUR 9,000 | ss18(2) UStG |
| Quarterly filing trigger | Prior year VAT liability EUR 2,000-9,000 | ss18(2) UStG |
| Annual only trigger | Prior year VAT liability < EUR 2,000 | ss18(2) UStG |
| Ist-Versteuerung turnover ceiling | EUR 600,000 | ss20 UStG |
| Business gifts block threshold | EUR 50 net per person per year | ss15(1a) Nr.1 UStG; ss4(5) Nr.1 EStG |
| Mobile phones/tablets domestic reverse charge | Invoice > EUR 5,000 net | ss13b(2) Nr.9-10 UStG |
| EU Kleinunternehmer cross-border ceiling | EUR 100,000 EU-wide (from 2025) | EU Directive, transposed into ss19 UStG |
| Intrastat arrivals threshold | EUR 800,000/year | EU Regulation 2019/2152 |
| Intrastat dispatches threshold | EUR 500,000/year | EU Regulation 2019/2152 |
| OSS distance selling threshold | EUR 10,000 EU-wide | ss3c UStG |

### Known gaps

1. The supplier pattern library in Section 3 covers the most common German and international counterparties but does not cover every regional Sparkasse name variant, local SME, or regional brand. Add patterns as they emerge.
2. The worked examples are drawn from a hypothetical IT consultant (Einzelunternehmer). They do not cover hospitality, retail, e-commerce, construction, or medical sectors specifically. A v2.1 should add sector-specific worked examples.
3. The ss13b(2) domestic reverse charge catalogue (construction, cleaning, scrap, etc.) is complex and context-dependent. Construction reverse charge in particular requires confirming both parties are Bauleistende. This is flagged as Tier 2 in all cases.
4. Import VAT (EUSt) Kennzahl has changed over time. The correct Kz for the current filing period should be confirmed by a Steuerberater.
5. The Kleinunternehmer thresholds (EUR 25,000 / EUR 100,000) reflect the 2025 amendment. The EU-wide cross-border Kleinunternehmer scheme details are still emerging and should be confirmed annually.
6. Red flag thresholds (EUR 5,000 single transaction, EUR 300 tax-delta, EUR 10,000 absolute position) are conservative starting values for Germany's typical self-employed client profile -- not empirically calibrated.
7. Photovoltaic 0% rate (ss12(3) UStG) is relatively new (2023). The exact Kennzahl for reporting 0%-rate supplies should be confirmed by a Steuerberater.

### Change log

- **v2.0 (April 2026):** Full rewrite to align with three-tier Accora architecture (Malta v2.0 structure). Quick reference moved to top (Section 1). Supplier pattern library restructured as literal lookup tables (Section 3, 13 sub-tables). Six worked examples added (Section 4). Tier 1 rules compressed with no inline [T1]/[T2]/[T3] tags (Section 5). Tier 2 catalogue restructured to compressed format (Section 6, 7 items). Excel working paper specification added (Section 7). German bank statement reading guide added (Section 8). Onboarding moved to fallback role with inference rules (Section 9). Reference material moved to bottom (Section 10). Companion skill references added (vat-workflow-base v0.1 and eu-vat-directive v0.1). Refusal catalogue added (R-DE-1 through R-DE-5). Malta comparison section removed (now handled by cross-skill reference). Test suite removed (moved to eval harness).
- **v1.0-draft (April 2026):** Initial skill. Standalone monolithic document covering UStG, Kennzahl mappings, reverse charge mechanics, blocked categories, edge cases, test suite, and Malta comparison. Awaiting Steuerberater validation.

### Self-check (v2.0 of this document)

1. Quick reference at top with Kz table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 13 sub-tables).
3. Worked examples drawn from hypothetical IT consultant: yes (Section 4, 6 examples).
4. Tier 1 rules compressed, no inline [T1]/[T2]/[T3] tags: yes (Section 5, 15 rules).
5. Tier 2 catalogue compressed with conservative defaults: yes (Section 6, 7 items).
6. Excel template specification with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only, inference rules first: yes (Section 9, 10 items).
8. All 5 Germany-specific refusals present: yes (Section 2, R-DE-1 through R-DE-5).
9. Reference material at bottom: yes (Section 10).
10. Bewirtung 100% VAT recovery (not blocked) explicit: yes (Section 5.3 + Example 3).
11. Motor vehicle NOT hard-blocked (business proportion deductible) explicit: yes (Section 5.10 + Section 6.1).
12. ss13b reverse charge catalogue (foreign and domestic) explicit: yes (Section 5.6 + 5.7).
13. EU B2B service sale (Kz 21) and USt-IdNr verification explicit: yes (Example 5).
14. Non-EU SaaS reverse charge (Kz 46/47) explicit: yes (Example 1 + Section 3.9).
15. Kleinunternehmer refusal (R-DE-1) with 2025 thresholds explicit: yes (Section 2).

## End of Germany VAT Return Skill v2.0

This skill is incomplete without BOTH companion files loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture) AND `eu-vat-directive` v0.1 or later (Tier 2, EU directive content). Do not attempt to produce a UStVA without all three files loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
