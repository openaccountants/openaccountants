---
name: greece-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Greek VAT return (Periodiki Dilosi FPA) for a self-employed individual or small business in Greece. Trigger on phrases like "prepare VAT return", "do the VAT", "Greek VAT", "FPA", "myAADE", "TAXISnet", or any request involving Greece VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Greece only and only standard normal-regime registrations. Small business exemption (Art. 39), farmers flat-rate (Art. 41), travel agent scheme (Art. 43), and VAT groups are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Greek VAT work.
version: 2.0
---

# Greece VAT Return Skill (Periodiki Dilosi FPA) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content and `eu-vat-directive` providing the EU directive content.**

| Field | Value |
|---|---|
| Country | Greece (Elliniki Dimokratia / Ελληνική Δημοκρατία) |
| Jurisdiction code | GR (EL for VIES purposes) |
| Standard rate | 24% |
| Reduced rates | 13% (food, energy, water supply, hotel accommodation, certain medical supplies), 6% (books, newspapers, theatre/cinema tickets, pharmaceuticals) |
| Aegean island rates | 30% discount on standard (17%) and reduced (9%, 4%) for certain Aegean islands — see Section 5.4 |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods, international transport, certain shipping supplies) |
| Return form | Periodiki Dilosi FPA (Περιοδική Δήλωση ΦΠΑ) — commonly "F2" |
| Annual summary | Ekkatharistiki Dilosi FPA (Εκκαθαριστική Δήλωση ΦΠΑ) |
| Filing portal | https://www.aade.gr (myTAXISnet / myAADE) |
| Authority | AADE (Ανεξάρτητη Αρχή Δημοσίων Εσόδων — Independent Authority for Public Revenue) |
| Currency | EUR only |
| Filing frequencies | Monthly (diplografika vivlia — double-entry bookkeeping); Quarterly (aplografika vivlia — single-entry bookkeeping) |
| Deadline | Monthly: last business day of month following period; Quarterly: last business day of month following quarter |
| myDATA | Mandatory electronic book/document reporting platform (myDATA / IAPR) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants |
| Validated by | Pending — requires logistis-forotechnikos validation |
| Validation date | Pending |

**Key F2 form fields (Periodiki Dilosi FPA):**

| Code | Meaning |
|---|---|
| 301 | Taxable sales at standard rate (24%) — net |
| 302 | Taxable sales at 13% — net |
| 303 | Taxable sales at 6% — net |
| 304 | Intra-EU supplies of goods — net |
| 305 | Intra-EU supplies of services — net |
| 306 | Exports — net |
| 307 | Exempt without credit — net |
| 308 | Island rate sales (17%) — net |
| 309 | Island rate sales (9%) — net |
| 310 | Island rate sales (4%) — net |
| 331 | Output VAT at 24% |
| 332 | Output VAT at 13% |
| 333 | Output VAT at 6% |
| 338 | Output VAT island rates |
| 341 | Total output VAT |
| 361 | Input VAT on domestic purchases |
| 362 | Input VAT on intra-EU acquisitions |
| 363 | Input VAT on imports |
| 364 | Input VAT on services from abroad (reverse charge) |
| 371 | Total input VAT |
| 381 | Intra-EU acquisitions of goods — net |
| 382 | Intra-EU acquisitions of services — net |
| 383 | Output VAT on intra-EU acquisitions |
| 384 | Purchases from non-EU (services — reverse charge) — net |
| 385 | Output VAT on non-EU reverse charge |
| 401 | VAT payable (341 − 371) if positive |
| 402 | Excess credit (371 − 341) if negative |
| 411 | Credit carried forward from prior period |
| 421 | Net VAT payable after carry-forward |
| 422 | Net credit to carry forward |

**Conservative defaults — Greece-specific:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 24% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Greece |
| Unknown B2B vs B2C status for EU customer | B2C, charge 24% |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU (384/385) |
| Unknown blocked-input status | Blocked |
| Unknown whether transaction is in scope | In scope |
| Unknown island vs mainland | Mainland rates |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | €3,000 |
| HIGH tax-delta on a single conservative default | €250 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | €5,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Acceptable from: National Bank of Greece (Εθνική Τράπεζα), Alpha Bank, Piraeus Bank (Τράπεζα Πειραιώς), Eurobank, Attica Bank, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices (τιμολόγια), purchase invoices, AFM (ΑΦΜ), myDATA export for the period.

**Ideal** — complete invoice register, myDATA classification codes, prior period F2, carry-forward credit reconciliation.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement → hard stop. If bank statement only → reviewer brief warning.

### Greece-specific refusal catalogue

On top of EU-wide refusals in `eu-vat-directive` Section 13.

**R-GR-1 — Small business exemption (Art. 39).** *Trigger:* client is under the small business exemption threshold. *Message:* "Small business exemption entities do not file periodic FPA returns. This skill covers normal-regime entities only."

**R-GR-2 — Farmers flat-rate scheme (Art. 41).** *Trigger:* client is a farmer under the flat-rate scheme. *Message:* "The farmers flat-rate scheme has different filing obligations. Out of scope."

**R-GR-3 — Travel agent scheme (Art. 43).** *Trigger:* client uses the travel agent margin scheme. *Message:* "Travel agent margin scheme requires special computation. Out of scope."

**R-GR-4 — Partial exemption (pro-rata).** *Trigger:* client makes both taxable and exempt supplies, exempt proportion non-de-minimis. *Message:* "You make both taxable and exempt supplies. Input VAT must be apportioned. Please use a logistis-forotechnikos."

**R-GR-5 — VAT grouping.** *Trigger:* client is part of a VAT group. *Message:* "VAT groups require consolidated filing. Out of scope."

**R-GR-6 — Shipping/maritime.** *Trigger:* client is in the shipping sector with special VAT obligations. *Message:* "Maritime/shipping VAT has complex special rules. Out of scope."

**R-GR-7 — Used goods margin scheme (Art. 45).** *Trigger:* client deals in second-hand goods under margin scheme. *Message:* "Margin scheme requires transaction-level margin computation. Out of scope."

**R-GR-8 — Income tax instead of FPA.** *Trigger:* user asks about income tax. *Message:* "This skill handles FPA (VAT) only."

---

## Section 3 — Supplier pattern library (the lookup table)

Match by case-insensitive substring. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Greek banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ΕΘΝΙΚΗ ΤΡΑΠΕΖΑ, NATIONAL BANK OF GREECE, NBG | EXCLUDE | Financial service, exempt Art. 22 §1 |
| ALPHA BANK, ΑΛΦΑ ΤΡΑΠΕΖΑ | EXCLUDE | Same |
| ΤΡΑΠΕΖΑ ΠΕΙΡΑΙΩΣ, PIRAEUS BANK | EXCLUDE | Same |
| EUROBANK, EUROBANK ERGASIAS | EXCLUDE | Same |
| ATTICA BANK | EXCLUDE | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for taxable subscriptions |
| ΤΟΚΟΙ, INTEREST | EXCLUDE | Interest, out of scope |
| ΔΑΝΕΙΟ, LOAN | EXCLUDE | Loan principal, out of scope |

### 3.2 Greek government and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| ΑΑΔΕ, AADE, TAXISnet | EXCLUDE | Tax payment |
| ΔΟΥ, ΕΦΟΡΙΑ | EXCLUDE | Tax office |
| ΤΕΛΩΝΕΙΟ, CUSTOMS | EXCLUDE | Customs duty (see import VAT separately) |
| ΕΦΚΑ, EFKA, ΙΚΑ | EXCLUDE | Social security contributions |
| ΟΑΕΔ, DYPA | EXCLUDE | Employment agency/fund |
| ΚΕΠ | EXCLUDE | Citizen service centre fees |
| ΕΡΓΑΝΗ | EXCLUDE | Labour reporting system |

### 3.3 Greek utilities

| Pattern | Treatment | Code | Notes |
|---|---|---|---|
| ΔΕΗ, ΔΕΔΔΗΕ, DEDDIE, PPC | Domestic 24% | 361 (input) | Electricity — overhead |
| ΔΕΠΑ, ΦΥΣΙΚΟ ΑΕΡΙΟ | Domestic 24% | 361 (input) | Natural gas |
| ΕΥΔΑΠ, EYDAP | Domestic 13% | 361 (input) | Water supply at 13% |
| COSMOTE, ΟΤΕ, ΓΕΡΜΑΝΟΣ | Domestic 24% | 361 (input) | Telecoms — overhead |
| VODAFONE GR, WIND HELLAS, NOVA | Domestic 24% | 361 (input) | Mobile telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ΕΘΝΙΚΗ ΑΣΦΑΛΙΣΤΙΚΗ, ΕΥΡΩΠΑΙΚΗ ΠΙΣΤΗ | EXCLUDE | Insurance, exempt Art. 22 §1(κα) |
| INTERAMERICAN, GENERALI GR, ALLIANZ GR | EXCLUDE | Same |
| ΑΣΦΑΛΕΙΑ, ΑΣΦΑΛΙΣΤΗΡΙΟ | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Code | Notes |
|---|---|---|---|
| ΕΛΤΑ, ELTA, HELLENIC POST | EXCLUDE for standard postage | | Universal service, exempt |
| ΕΛΤΑ COURIER | Domestic 24% | 361 | Non-universal, taxable |
| ACS COURIER, SPEEDEX, ΓΕΝΙΚΗ ΤΑΧΥΔΡΟΜΙΚΗ | Domestic 24% | 361 | Courier, taxable |

### 3.6 Transport (Greece domestic)

| Pattern | Treatment | Code | Notes |
|---|---|---|---|
| ΚΤΕΛ, KTEL | Domestic 13% | 361 | Intercity bus at 13% |
| ΟΑΣΑ, OASA, METRO, ΤΡΑΜ | Domestic 13% | 361 | Athens public transport at 13% |
| ΤΡΕΝΟΣΕ, TRAINOSE, HELLENIC TRAIN | Domestic 13% | 361 | Rail at 13% |
| ΤΑΞΙ, TAXI, BEAT, UBER GR | Domestic 24% | 361 | Taxi at 24% |
| AEGEAN AIRLINES, OLYMPIC AIR (domestic) | Domestic 13% | 361 | Domestic flights at 13% |
| AEGEAN, RYANAIR (international) | EXCLUDE / 0% | | International flights zero rated |
| BLUE STAR, ANEK LINES, MINOAN | Domestic 13% or 0% | 361 | Domestic ferry at 13%; international 0% |

### 3.7 Food retail and entertainment (blocked unless hospitality)

| Pattern | Treatment | Notes |
|---|---|---|
| ΣΚΛΑΒΕΝΙΤΗΣ, SKLAVENITIS | Default BLOCK | Supermarket — personal provisioning |
| ΑΒ ΒΑΣΙΛΟΠΟΥΛΟΣ, AB VASSILOPOULOS | Default BLOCK | Same |
| LIDL GR, ΜΑΣΟΥΤΗΣ, MASOUTIS, METRO CASH & CARRY | Default BLOCK | Same (Metro C&C may be deductible if wholesale for resale) |
| RESTAURANTS, ΕΣΤΙΑΤΟΡΙΟ, ΤΑΒΕΡΝΑ | Default BLOCK | Entertainment — check deductibility |

**Note on Greek entertainment:** Greece allows input VAT recovery on business meals/entertainment if properly documented with business purpose and the expense is genuinely business-related (no hard block like Malta). However, the burden of proof is on the taxpayer. Default: block. [T2] flag if client claims business purpose with documentation.

### 3.8 SaaS — EU suppliers (reverse charge, 382/383/362)

| Pattern | Billing entity | Code | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 382/383/362 | EU service reverse charge |
| MICROSOFT (365, Azure) | Microsoft Ireland (IE) | 382/383/362 | Reverse charge |
| ADOBE | Adobe Ireland (IE) | 382/383/362 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland (IE) | 382/383/362 | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland (IE) | 382/383/362 | Reverse charge |
| SPOTIFY | Spotify AB (SE) | 382/383/362 | EU reverse charge |
| DROPBOX | Dropbox Ireland (IE) | 382/383/362 | Reverse charge |
| SLACK | Slack Ireland (IE) | 382/383/362 | Reverse charge |
| ATLASSIAN | Atlassian BV (NL) | 382/383/362 | EU reverse charge |
| ZOOM | Zoom Ireland (IE) | 382/383/362 | Reverse charge |
| STRIPE (subscription) | Stripe IE | 382/383/362 | Transaction fees may be exempt |

### 3.9 SaaS — non-EU suppliers (reverse charge, 384/385/364)

| Pattern | Billing entity | Code | Notes |
|---|---|---|---|
| AWS (standard) | AWS EMEA SARL (LU) — check | 382/383/362 | LU → EU reverse charge |
| NOTION | Notion Labs Inc (US) | 384/385/364 | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 384/385/364 | Non-EU |
| OPENAI, CHATGPT | OpenAI Inc (US) | 384/385/364 | Non-EU |
| GITHUB | GitHub Inc (US) | 384/385/364 | Check if billed by IE |
| FIGMA | Figma Inc (US) | 384/385/364 | Non-EU |
| CANVA | Canva Pty Ltd (AU) | 384/385/364 | Non-EU |
| HUBSPOT | US or IE — check | 384/385 or 382/383 | Depends on billing entity |
| TWILIO | Twilio Inc (US) | 384/385/364 | Non-EU |

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing exempt |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| VIVA WALLET, VIVA PAYMENTS | Check invoice | Greek acquirer — fees may be exempt financial services |

### 3.11 Professional services (Greece)

| Pattern | Treatment | Code | Notes |
|---|---|---|---|
| ΔΙΚΗΓΟΡΟΣ, ΔΙΚΗΓΟΡΙΚΟ ΓΡΑΦΕΙΟ | Domestic 24% | 361 | Legal — deductible if business |
| ΛΟΓΙΣΤΗΣ, ΛΟΓΙΣΤΙΚΟ ΓΡΑΦΕΙΟ | Domestic 24% | 361 | Accountant — always deductible |
| ΣΥΜΒΟΛΑΙΟΓΡΑΦΟΣ, NOTARY | Domestic 24% | 361 | Notary |
| ΓΕΜΗ, GEMI | EXCLUDE | Business registry fee, not a supply |

### 3.12 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| ΕΦΚΑ, EFKA, ΙΚΑ, ΑΣΦΑΛΙΣΤΙΚΕΣ ΕΙΣΦΟΡΕΣ | EXCLUDE | Social security |
| ΜΙΣΘΟΔΟΣΙΑ, ΜΙΣΘΟΣ (outgoing) | EXCLUDE | Wages |
| ΦΟΡΟΣ ΜΙΣΘΩΤΩΝ, ΦΜΥ | EXCLUDE | Payroll tax withholding |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| ΕΝΟΙΚΙΟ, ΜΙΣΘΩΜΑ (commercial, with FPA) | Domestic 24% | Commercial lease with VAT |
| ΕΝΟΙΚΙΟ (residential, no FPA) | EXCLUDE | Residential lease, exempt Art. 22 §1(κστ) |
| ΚΤΗΜΑΤΟΛΟΓΙΟ | EXCLUDE | Land registry fee |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| ΜΕΤΑΦΟΡΑ, ΕΣΩΤΕΡΙΚΗ ΜΕΤΑΦΟΡΑ | EXCLUDE | Internal movement |
| ΜΕΡΙΣΜΑ, DIVIDEND | EXCLUDE | Dividend, out of scope |
| ΔΟΣΗ ΔΑΝΕΙΟΥ | EXCLUDE | Loan repayment |
| ΑΝΑΛΗΨΗ, ATM | TIER 2 — ask | Default exclude; ask about cash use |

---

## Section 4 — Worked examples

Six fully worked classifications from a hypothetical Greek self-employed IT consultant.

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
US entity. Non-EU service reverse charge. Net EUR 14.68 in code 384, output VAT (24% = EUR 3.52) in 385, input VAT EUR 3.52 in 364. Net effect zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Code (output) | Code (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 3.52 | 24% | 384/385 | 364 | N | — | — |

### Example 2 — EU service, reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April ; -850.00 ; EUR`

**Reasoning:**
IE entity. EU service reverse charge. Net EUR 850 in 382, output VAT (24% = EUR 204) in 383, input VAT EUR 204 in 362.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Code (output) | Code (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 204.00 | 24% | 382/383 | 362 | N | — | — |

### Example 3 — Entertainment, default block

**Input line:**
`15.04.2026 ; ΤΑΒΕΡΝΑ Ο ΚΩΣΤΑΣ ; DEBIT ; Client dinner ; -180.00 ; EUR`

**Reasoning:**
Restaurant/taverna transaction. Greek law does not have a hard block on entertainment like Malta, but documentation requirements are strict. Default: block. [T2] flag.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Code | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | ΤΑΒΕΡΝΑ Ο ΚΩΣΤΑΣ | -180.00 | -180.00 | 0 | — | — | Y | Q1 | "Entertainment: blocked by default — recovery possible if business purpose documented" |

### Example 4 — Domestic purchase at 24%

**Input line:**
`18.04.2026 ; ΠΛΑΙΣΙΟ COMPUTERS ; DEBIT ; Laptop Dell XPS ; -1,300.00 ; EUR`

**Reasoning:**
Greek electronics retailer. EUR 1,300 incl. 24% VAT. Net = EUR 1,048.39. VAT = EUR 251.61. Input VAT deductible in code 361.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Code | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | ΠΛΑΙΣΙΟ COMPUTERS | -1,300.00 | -1,048.39 | -251.61 | 24% | 361 | N | — | — |

### Example 5 — EU B2B service sale (inbound receipt)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice GR-2026-018 IT consultancy ; +3,500.00 ; EUR`

**Reasoning:**
Incoming from German company. B2B IT consulting — place of supply is Germany. Invoice at 0%, customer accounts for reverse charge. Report net in code 305 (EU services supplied). Verify German USt-IdNr on VIES.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Code | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | 0% | 305 | Y | Q2 (HIGH) | "Verify German USt-IdNr on VIES" |

### Example 6 — Motor vehicle, restricted

**Input line:**
`28.04.2026 ; AUTOHELLAS HERTZ ; DEBIT ; Car lease May ; -500.00 ; EUR`

**Reasoning:**
Car lease. In Greece, passenger vehicles used for business purposes: input VAT is generally deductible if the vehicle is used for taxable business activity (no hard block like Malta). However, personal use portion must be excluded. Default: block. [T2] — reviewer must determine business use proportion.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Code | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | AUTOHELLAS HERTZ | -500.00 | -500.00 | 0 | — | — | Y | Q3 | "Vehicle: blocked by default — deductible for business portion if documented" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 24% (Art. 21 §1)

Default rate. Sales → 301 (net), 331 (output VAT). Purchases → 361 (input VAT).

### 5.2 Reduced rate 13% (Art. 21 §2, Annex III)

Food and non-alcoholic beverages, energy (electricity, gas), water supply, hotel accommodation, certain medical supplies, domestic transport. Sales → 302/332.

### 5.3 Reduced rate 6% (Art. 21 §4)

Books, newspapers, periodicals, theatre/cinema tickets, pharmaceuticals, vaccines. Sales → 303/333.

### 5.4 Aegean island reduced rates

Certain Aegean islands receive a 30% discount: standard 24% → 17%, 13% → 9%, 6% → 4%. Sales → 308/309/310 and 338. Applies to supplies made on and delivered to qualifying islands. **If client is island-based, [T2] flag — reviewer must confirm island qualification.**

### 5.5 Zero rate / exempt with credit

Exports → 306. Intra-EU B2B goods → 304 (requires VIES verification). Intra-EU B2B services → 305. International transport, ship supplies (Art. 27).

### 5.6 Exempt without credit (Art. 22)

Medical/dental, hospital services, education, insurance, financial services, postal universal service, residential rent. Excluded from FPA return. If significant → **R-GR-4 refuses**.

### 5.7 Reverse charge — EU services (Art. 14 §2)

EU supplier at 0%: net → 382, output VAT → 383, input VAT → 362. Net effect zero.

### 5.8 Reverse charge — EU goods acquisitions (Art. 11)

Physical goods from EU: net → 381, output VAT → 383, input VAT → 362.

### 5.9 Reverse charge — non-EU services (Art. 14)

Services from outside EU: net → 384, output VAT → 385, input VAT → 364.

### 5.10 Import of goods

Goods from non-EU: import VAT on customs declaration. Input VAT → 363.

### 5.11 Blocked / restricted input VAT

- Entertainment: not hard-blocked in Greece, but documentation required. Default: block. [T2] for documented business entertainment.
- Motor vehicles: deductible for business use (no hard block); private portion must be excluded. Default: block for IT consultants.
- Tobacco: blocked.
- Personal use: blocked.
- Gifts above EUR 10: blocked (promotional gifts up to EUR 10 per item deductible).

### 5.12 myDATA reporting

All income and expenses must be reported through myDATA (IAPR platform). The FPA return must reconcile with myDATA classifications. Classification codes (παραστατικά) must match. If discrepancies exist between bank statement and myDATA, flag for reviewer.

### 5.13 Sales — local domestic

Charge 24%, 13%, or 6%. Map to 301/302/303 and 331/332/333.

### 5.14 Sales — cross-border B2C

EU consumers above €10,000 threshold → **R-EU-5 (OSS refusal)**. Below threshold → Greek VAT.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* BP GR, Shell GR, EKO, Aegean Oil. *Default:* 0% recovery. *Question:* "Business vehicle or personal? What proportion of business use?"

### 6.2 Entertainment

*Pattern:* restaurant, taverna, cafe. *Default:* block. *Question:* "Documented business purpose with attendees?"

### 6.3 Ambiguous SaaS billing entities

*Default:* non-EU reverse charge 384/385/364. *Question:* "Check invoice for legal entity."

### 6.4 Round-number owner transfers

*Default:* exclude as owner injection. *Question:* "Customer payment, capital, or loan?"

### 6.5 Incoming from individuals

*Default:* domestic B2C at 24%, 301/331. *Question:* "Sale? Country?"

### 6.6 Foreign counterparty incoming

*Default:* domestic 24%. *Question:* "B2B with VAT number or B2C? Country?"

### 6.7 Large one-off purchases

*Default:* normal overhead in 361. *Question:* "Confirm invoice amount."

### 6.8 Mixed-use phone/internet

*Pattern:* Cosmote, Vodafone personal lines. *Default:* 0% if mixed. *Question:* "Dedicated business line? Business percentage?"

### 6.9 Outgoing to individuals

*Default:* exclude as drawings. *Question:* "Contractor, wages, refund, or personal?"

### 6.10 Cash withdrawals

*Pattern:* ΑΝΑΛΗΨΗ, ATM. *Default:* exclude. *Question:* "What was cash used for?"

### 6.11 Rent payments

*Default:* no VAT (residential). *Question:* "Commercial? Does landlord charge FPA?"

### 6.12 Foreign hotel

*Default:* exclude from input VAT. *Question:* "Business trip?"

### 6.13 Aegean island classification

*Pattern:* supplier address on qualifying island. *Default:* mainland rates. *Question:* "Is this business/supplier located on a qualifying Aegean island?"

### 6.14 myDATA reconciliation

*Pattern:* any transaction without matching myDATA entry. *Default:* accept but flag. *Question:* "Has this been reported in myDATA? Classification code?"

---

## Section 7 — Excel working paper template (Greece-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Greece-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("F2 code") accepts valid F2 codes from Section 1. Additional column M for myDATA classification code.

### Sheet "Box Summary"

```
Output:
| 301 | Sales 24% net | =SUMIFS(...) |
| 302 | Sales 13% net | =SUMIFS(...) |
| 303 | Sales 6% net | =SUMIFS(...) |
| 304 | EU goods supplies net | =SUMIFS(...) |
| 305 | EU services supplies net | =SUMIFS(...) |
| 306 | Exports net | =SUMIFS(...) |
| 331 | Output VAT 24% | =C[301]*0.24 |
| 332 | Output VAT 13% | =C[302]*0.13 |
| 333 | Output VAT 6% | =C[303]*0.06 |

Acquisitions:
| 381 | EU goods acquisitions net | =SUMIFS(...) |
| 382 | EU services acquisitions net | =SUMIFS(...) |
| 383 | Output VAT EU acquisitions | =(C[381]+C[382])*0.24 |
| 384 | Non-EU services net | =SUMIFS(...) |
| 385 | Output VAT non-EU | =C[384]*0.24 |

| 341 | Total output VAT | =C[331]+C[332]+C[333]+C[383]+C[385] |

Input:
| 361 | Input VAT domestic | =SUMIFS(...) |
| 362 | Input VAT EU acquisitions | =C[383] (mirror for fully taxable) |
| 363 | Input VAT imports | =SUMIFS(...) |
| 364 | Input VAT non-EU services | =C[385] (mirror for fully taxable) |
| 371 | Total input VAT | =C[361]+C[362]+C[363]+C[364] |

Bottom line:
| 401 | VAT payable | =IF(C[341]>C[371], C[341]-C[371], 0) |
| 402 | Excess credit | =IF(C[371]>C[341], C[371]-C[341], 0) |
| 421 | Net payable after carry-forward | =C[401]-C[411] |
```

### Mandatory recalc step

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/greece-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Greece bank statement reading guide

**CSV format conventions.** National Bank of Greece and Alpha Bank exports use semicolons with DD/MM/YYYY dates. Piraeus Bank uses comma-separated. Common columns: Ημερομηνία (Date), Περιγραφή (Description), Ποσό (Amount), Υπόλοιπο (Balance).

**Greek language variants.** Ενοίκιο (rent), μισθός (salary), τόκοι (interest), μεταφορά (transfer), ανάληψη (withdrawal), κατάθεση (deposit), τιμολόγιο (invoice). Treat as English equivalents.

**Internal transfers.** Labelled "μεταφορά", "εσωτερική μεταφορά". Always exclude.

**Owner draws.** Ατομική επιχείρηση (sole trader) transfers to personal account are drawings — exclude.

**Refunds.** Identify by "επιστροφή", "ακύρωση", "πιστωτικό". Book as negative.

**Foreign currency.** Convert to EUR at ECB rate or bank statement rate.

**IBAN prefix.** GR = Greece. IE, DE, FR = EU. US, GB, CH = non-EU.

**myDATA cross-check.** For each classified transaction, note whether a corresponding myDATA entry exists. Discrepancies between bank data and myDATA should be flagged for reviewer.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
*Inference rule:* ατομική επιχείρηση (sole trader) vs ΙΚΕ vs ΕΠΕ vs ΑΕ. *Fallback:* "Are you sole trader (ατομική), ΙΚΕ, ΕΠΕ, ΑΕ, or other?"

### 9.2 VAT registration status
*Inference rule:* if asking for FPA return, they are normal regime. *Fallback:* "Normal VAT regime or small business exemption (Art. 39)?"

### 9.3 AFM
*Fallback:* "What is your ΑΦΜ? (9 digits, EL prefix for VIES)"

### 9.4 Filing period and frequency
*Inference rule:* transaction dates + bookkeeping type. *Fallback:* "Monthly or quarterly filer? Which period?"

### 9.5 Industry
*Fallback:* "What does the business do?"

### 9.6 Employees
*Inference rule:* ΕΦΚΑ, μισθοδοσία outgoing. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Fallback:* "Do you make FPA-exempt sales?" *If yes → R-GR-4 may fire.*

### 9.8 Credit brought forward
*Always ask:* "Excess credit from previous period? (Code 411)"

### 9.9 Cross-border customers
*Fallback:* "Customers outside Greece? EU or non-EU? B2B or B2C?"

### 9.10 Island location
*Fallback:* "Is your business located on an Aegean island with reduced rates?"

---

## Section 10 — Reference material

### Validation status

v2.0, rewritten April 2026. Awaiting validation by logistis-forotechnikos in Greece.

### Sources

1. N.2859/2000 (Kodikos FPA) — as amended
2. N.4174/2013 (Tax Procedure Code)
3. myDATA legislation (A.1138/2020, A.1052/2023)
4. AADE guidance — https://www.aade.gr
5. Council Directive 2006/112/EC — via eu-vat-directive companion skill
6. VIES — https://ec.europa.eu/taxation_customs/vies/
7. ECB exchange rates

### Known gaps

1. Aegean island reduced rates apply to specific islands — the full list is not enumerated here. Verify per AADE guidance.
2. myDATA classification codes are not fully mapped — a future version should add the code table.
3. Entertainment deductibility is more permissive than Malta but documentation standards are high — the skill defaults to block.
4. The shipping/maritime sector is entirely excluded (R-GR-6).
5. Capital goods scheme thresholds for Greece are not specified — verify per N.2859/2000.

### Change log

- **v2.0 (April 2026):** Full rewrite to three-tier Accora architecture.
- **v1.0 (April 2026):** Initial draft. Standalone monolithic document.

### Self-check (v2.0)

1. Quick reference with F2 code table and conservative defaults: yes (Section 1).
2. Supplier library with Greek-language patterns: yes (Section 3, 14 sub-tables).
3. Worked examples: yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 14 rules).
5. Tier 2 catalogue: yes (Section 6, 14 items).
6. Excel template with recalc: yes (Section 7).
7. Onboarding as fallback: yes (Section 9, 10 items).
8. All 8 Greece-specific refusals: yes (R-GR-1 through R-GR-8).
9. Reference material at bottom: yes (Section 10).
10. Three rates (24%/13%/6%) mapped: yes.
11. Aegean island rates documented: yes (Section 1, Section 5.4).
12. myDATA requirements documented: yes (Section 5.12).
