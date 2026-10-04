---
name: cyprus-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Cyprus VAT return (VAT4 form) for any client. Trigger on phrases like "prepare Cyprus VAT return", "do the Cyprus VAT", "fill in VAT4", "create the return", "Cyprus VAT filing", or any request involving Cyprus VAT filing. This skill covers Cyprus only and standard VAT registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Cyprus VAT work.
version: 2.0
jurisdiction: CY
tax_year: 2026
last_updated: 2026-10-02
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cyprus VAT return: classifying a quarter and filling in the return

This Guide prepares and reviews the periodic Cyprus VAT return (Δήλωση Φ.Π.Α.) for a business on the normal VAT scheme: which rate applies, which box each transaction goes in, who must register, when the return is due, and how to correct it. Figures are for tax year 2026. Every figure comes from a Cyprus Tax Department page or document, linked in the table that holds it. Most of those pages are in Greek only, so the Note column quotes the Greek text. Use it with the `vat-workflow-base` Guide (workflow) and the `eu-vat-directive` Guide (EU rules).

## Section 1: Quick reference

Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1.

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Cyprus (Republic of Cyprus) |
| Authority | Tax Department (Τμήμα Φορολογίας), Ministry of Finance |
| Law | VAT Law N.95(I)/2000 as amended, and the VAT (General) Regulations Κ.Δ.Π. 314/2001 |
| Return | The VAT return (Δήλωση Φ.Π.Α.), 13 boxes numbered 1 to 11B. Earlier versions of this Guide called it "VAT4"; no Tax Department page read for this rewrite uses that name |
| Filing | Electronic only, through Tax For All (TFA) |
| Period | Usually quarterly, set at registration by the business's NACE code; the Commissioner may set monthly or annual periods (Section 2) |
| Deadline | Return and payment by the 10th day after the end of the month that follows the end of the period (Section 2) |
| Currency | EUR only |
| Companion Guides | `vat-workflow-base` and `eu-vat-directive`, both must be loaded |

**2026 VAT rates.** The Tax Department rates page lists the goods and services in each reduced band. Anything not listed on the rates page or in the Sixth Schedule table below takes the standard rate.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/mof-tax/documents/syntelestes-f-p-a/ |
| Standard rate: every taxable supply of goods or services and every import of goods, except those listed in the rows below | 19% | "Κανονικός συντελεστής (19%) Επιβάλλεται σε κάθε φορολογητέα παράδοση αγαθών ή παροχή υπηρεσιών ή εισαγωγή αγαθών πλην των πιο κάτω" |
| Reduced rate: passenger transport by urban, intercity and rural taxis, and by tourist and intercity buses; restaurant and catering services; accommodation in hotels, tourist lodgings and similar; supplies by old people's homes (other than exempt ones) | 9% | "Μειωμένος συντελεστής (9%) Μεταφορά επιβατών με αστικά, υπεραστικά και αγροτικά ταξί καθώς και τουριστικά και υπεραστικά λεωφορεία" |
| Reduced rate: among others, food and drinks (but NOT alcoholic drinks, beer, wine or soft drinks, and not the items in the 0% row), water, bottled gas, medicines and vaccines, contraceptives, medical equipment for people with disabilities, children's car seats, electricity on tariff 08, funeral services, authors' and composers' services, transport by urban and rural buses, camping pitches, admission to shows, cinemas, museums, zoos and sports events, hairdressing, renovation of private homes under conditions, school canteens, and the purchase or construction of a main and permanent residence after the Commissioner's approval | 5% | "Μειωμένος συντελεστής (5%) Φέρετρα"; "Τρόφιμα και ποτά (εκτός τον οινοπνευματωδη, μπύρα, καρασί και αναψυκτικά) εκτος αυτά που βρίσκονται στον 0%" |
| Super-reduced rate: books, newspapers and magazines (including electronic), talking books for people with disabilities, lifting devices and wheelchairs for people with disabilities, orthopaedic and hearing devices, street cleaning, refuse collection and waste treatment other than by local authorities, sewage disposal and tank emptying, admission to the first performance only of theatre, music and dance works | 3% | "Μειωμένος συντελεστής (3%) Βιβλία, εφημερίδες, περιοδικά και σε ηλεκτρονική μορφή" |
| Zero rate: export of goods; supply, repair and hire of sea-going ships and airline aircraft; services for the direct needs of sea-going ships | 0% | "Μηδενικός συντελεστής (0%) Εξαγωγή αγαθών" |
| Last day of the temporary zero rate on basic goods: baby milk, children's and adult nappies, meat, fish, cuttlefish, squid, octopus, and certain vegetables and fruit | 30/9/2026 | "συγκεκριμένα λαχανικά και φρούτα μέχρι και 30/9/2026" |

The temporary zero rate on basic goods applied "up to and including" 30 September 2026. The rates page, read on 2 October 2026, shows no extension. For supplies of those goods made from 1 October 2026, use the rate the page lists for the item (food and drinks are in the 5% row); an item the page does not list in any reduced row takes the standard rate. A quarter that straddles 30 September 2026 (for example August to October) needs the sales of these goods split by date.

The rates page does not list every zero-rated item. The Sixth Schedule of the VAT Law also zero-rates international passenger transport, to the extent the transport takes place in Cyprus.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/01/Consolidated-VAT-Law-%CE%9A%CE%94%CE%A0-221_2026.pdf |
| Passenger transport from Cyprus to abroad or the reverse, to the extent carried out inside Cyprus (Sixth Schedule paragraph 5(ε), wording in force from 20 August 2020) | 0% | "ΠΑΡΑΔΟΣΕΙΣ ΑΓΑΘΩΝ ΚΑΙ ΠΑΡΟΧΕΣ ΥΠΗΡΕΣΙΩΝ ΠΟΥ ΥΠΟΚΕΙΝΤΑΙ ΣΤΟ ΜΗΔΕΝΙΚΟ ΣΥΝΤΕΛΕΣΤΗ"; "(ε) Μεταφορά επιβατών ... εξωτερικό ή αντίστροφα, στην έκταση που η μεταφορά διενεργείται στο εσωτερικό της Δημοκρατίας" |

The 5% rate on a main residence is a separate scheme with its own approval, limits and cliff (Section 5.3).

**Key return boxes.** From the Tax Department's guide to completing the VAT return, dated 31/08/2020 (file name 06082024). It predates the one-stop shop (OSS); where it says MOSS, read the OSS the rights page lists, unconfirmed on any page read.

| Box | Meaning |
| --- | --- |
| 1 | VAT due on outputs: sales, plus VAT you self-assess on services received from abroad and on domestic reverse charge purchases |
| 2 | VAT on acquisitions of GOODS (and linked services) from other EU member states |
| 3 | Total VAT due (Box 1 + Box 2) |
| 4 | Input VAT deductible this period on purchases and other inputs, including acquisitions from other EU member states |
| 5 | VAT payable or repayable (Box 3 minus Box 4) |
| 6 | Total value of outputs, without VAT, INCLUDING the amounts in Boxes 8A, 8B, 9, 10 and 11B |
| 7 | Total value of inputs, without VAT, INCLUDING the amounts in Boxes 11A and 11B |
| 8A | Value of supplies of goods (and linked services) to other EU member states |
| 8B | Value of services supplied to taxable persons in other EU member states where the customer accounts for the VAT |
| 9 | Value of zero-rated outputs other than those in 8A and 8B (exports included) |
| 10 | Value of out-of-scope sales with the right to deduct input VAT (other than 8B), including triangular sales and sales through the one-stop shop (the 2020 guide says "MOSS") |
| 11A | Value of acquisitions of goods (and linked services) from other EU member states |
| 11B | Value of services received from taxable persons in other EU member states |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 19% (standard rate) |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Cyprus |
| Unknown B2B vs B2C for an EU customer | B2C, charge Cyprus VAT at the standard rate |
| Unknown business-use proportion | No recovery |
| Unknown SaaS billing entity | Reverse charge as a service from outside the EU |
| Unknown blocked-input status | Blocked |
| Unknown whether in scope | In scope |

**Red flags for the reviewer.** Flag for review: a single transaction that is large for the business; any default whose effect on the VAT due is material; one counterparty dominating the quarter's sales or purchases; more than a handful of conservative defaults in one quarter; and a large net payable or repayable position. (The earlier numeric trigger levels were internal review settings, not law; set them with the reviewer.)

## Section 2: Registration, periods, deadlines and penalties

**Registration and filing obligations.** From the Tax Department page on the obligation and right to register.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/mof-tax/documents/eggrafi-akyrosi-f-p-a/eggrafes-mitrooy-f-p-a/ypochreosi-dikaioma-eggrafis-sto-mitroo-f-p-a/ |
| Registration threshold for a person established in Cyprus: taxable supplies (standard, reduced and zero rated) in the year ending at the end of any month have exceeded this, OR there are reasonable grounds to believe supplies in the next 30 days will exceed it. Capital assets of the business are not counted | EUR 15,600 | "η αξία των φορολογητέων συναλλαγών του κατά την περίοδο ενός έτους που τελειώνει σε αυτό το χρονικό σημείο έχει υπερβεί τις €15.600" |
| Penalty for late notification of the obligation to register, for every month the failure lasts | EUR 85 | "Καθυστέρηση γνωστοποίησης της υποχρέωσης για εγγραφή, συνεπάγεται χρηματική επιβάρυνση €85 για κάθε μήνα που διαρκεί η παράλειψη" |
| Registration threshold for acquisitions of goods from other EU member states, counted from 1 January of the calendar year (or expected within the next 30 days). Not the general threshold | EUR 10,251.61 | "έχουν υπερβεί το όριο των €10.251,61" |

- Past-12-months test: the business must notify within thirty days of the end of the month in which the threshold was exceeded. Registration takes effect from the end of the following month, or an earlier agreed date.
- Next-30-days test: the business must notify before the end of that thirty-day period, and registration takes effect from the start of it.
- The obligation exists whether or not the business applied. The Commissioner may register it back to the date it became liable, and it owes the VAT on its supplies from that date.
- No threshold: a person who supplies services to taxable persons in another EU member state, where the customer pays the VAT there, must register from the first such supply, whatever its value, and file the VIES recapitulative statement.
- No threshold: a business NOT established in Cyprus that makes taxable supplies in Cyprus (where the reverse charge does not apply) must register as soon as it intends to make them.
- Distance sales: the page sends distance sellers to Information Leaflet 3A. No allowed page read for this rewrite prints the EU distance-sales threshold, so this Guide does not state one. Refer.
- Voluntary registration is open to a business below the thresholds and to an intending trader.

**Return periods.** From the Tax Department page on submitting VAT returns. VAT returns "usually cover quarterly tax periods" ("Οι Δηλώσεις ΦΠΑ αφορούν συνήθως τριμηνιαίες φορολογικές περιόδους"), set at registration from the business's NACE activity code. Under conditions the Commissioner may set monthly or annual returns. The quarters are not always calendar quarters: the official calendar shows quarters such as June to August. Source: https://www.gov.cy/mof-tax/documents/ypovoli-tropopoiisi-diloseon-f-p-a/

**Deadlines.** The return is due, and the VAT must be paid, by the 10th day after the end of the month that follows the end of the tax period (regulation 17 of Κ.Δ.Π. 314/2001). For a quarter ending 31 March, that is 10 May. The VIES recapitulative statement is due by the 15th day after the end of each month in which the business supplied goods or services to a person registered in another member state, and also for months with no such supplies. A corrective VIES statement is due within one month of the end of the month it relates to. Source: https://www.gov.cy/mof-tax/documents/dikaiomata-kai-ypochreoseis/

**Calendar example.** The official deadline calendar prints "2026-10-10 Προθεσμία Υποβολής Δήλωσης και Πληρωμής Φ.Π.Α. για την τριμηνία Ιουνίου" for the June to August 2026 quarter (return and payment due 10 October 2026), and states that when the deadline falls on a weekend or public holiday it moves to the next working day ("Όταν η ημερομηνία λήξης συμπίπτει με Σαββατοκύριακο ή αργία, η προθεσμία είναι η επόμενη εργάσιμη ημέρα"). Source: https://www.gov.cy/mof-tax/prothesmies/

**Penalties and corrections.** From the VAT return FAQ and the FAQ on correcting errors.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/mof-tax/documents/ypovoli-tropopoiisi-diloseon-f-p-a/sychnes-erotiseis-dilosis-f-p-a/ |
| Fixed charge for failing to submit a required VAT return | EUR 100 | "χρηματική επιβάρυνση ύψους 100€, επιπρόσθετος φόρος ίσο προς το 10% του οφειλόμενου φόρου καθώς και τόκοι υπερημερίας" |
| Additional tax on the tax due, on top of the fixed charge and default interest | 10% | "επιπρόσθετος φόρος ίσο προς το 10% του οφειλόμενου φόρου" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/mof-tax/documents/ypovoli-tropopoiisi-diloseon-f-p-a/sychnes-erotiseis-se-schesi-me-tis-diorthoseis-lathon/ |
| Errors in earlier returns may be corrected in the current period's VAT account ONLY if the net total of all errors found does not exceed this AND the error relates to a period less than three years old. Otherwise the business must send a written request to the Tax Department through TFA | EUR 1,708.60 | "δεν υπερβαίνει τα €1708,60, μπορείτε να προβείτε σε καταχώριση του εν λόγω ποσού στο ανάλογο μερίδιο του Λογαριασμού Φ.Π.Α. της τρέχουσας φορολογικής περιόδου" |

- Before the deadline, the business can amend its own return (boxes 1 to 11B) in TFA.
- Value boxes 6 to 11B of a return whose deadline is after 27/3/2023 can be amended in TFA by the business itself. Earlier returns need a written request.
- The correction in the current return follows regulation 24 of Κ.Δ.Π. 314/2001. The net total is worked out by setting the under-declared output VAT and over-claimed input VAT against the over-declared output VAT and under-claimed input VAT.

**Deregistration and invoicing.** From the Tax Department page on business rights and obligations.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/mof-tax/documents/dikaiomata-kai-ypochreoseis/ |
| A registered person may be deregistered if it satisfies the Commissioner that its taxable supplies in the coming year will not exceed this | EUR 13,668.81 | "δεν θα υπερβεί τις €13.668,81 μπορεί να διαγραφεί από το Μητρώο Φ.Π.Α." |
| A retailer must issue a VAT invoice if the customer is a taxable person, asks for one, and the consideration exceeds this | EUR 85 | "αν ο πελάτης είναι υποκείμενο στο φόρο πρόσωπο και το ζητήσει και αν η αντιπαροχή υπερβαίνει τις €85" |
| Administrative charge for failing to issue a legal receipt to consumers: up to this share of the transaction value | 20% | "διοικητικής χρηματικής επιβάρυνσης ίσης με ποσοστό έως και 20% της αξίας της συναλλαγής" |

- A business must notify the end of its taxable activity within 60 days.
- The same page lists the special schemes a business may join where conditions are met, including the special scheme for small businesses (SME-SS) under Law 104(I)/2025, the one-stop shop (OSS / IOSS), the cash accounting scheme (article 42Ε), the margin schemes, the farmers' scheme and the urban taxi scheme. All are outside this Guide (refusal catalogue).

## Section 3: Required inputs and refusal catalogue

### Required inputs

**Minimum viable**: bank statement for the period. Acceptable from: Bank of Cyprus, Hellenic Bank, RCB Bank, Eurobank Cyprus, Astrobank, Revolut Business, Wise Business.

**Recommended**: sales invoices (intra-EU B2B, exports), purchase invoices for input VAT claims, the CY VAT number. To claim input VAT in Box 4 the business must hold a tax invoice dated in the period (Section 5.11).

**Ideal**: complete invoice register, prior VAT return, VIES statements, credit brought forward reconciliation.

### Cyprus-specific refusal catalogue

- **R-CY-1: Non-registered entity.** Trigger: not registered and not required to register (Section 2). Message: "A person that is not registered and not required to register does not file a VAT return."
- **R-CY-2: Partial exemption.** Trigger: mixed taxable and exempt supplies. Message: "Input VAT must be apportioned under regulations 64-65Γ of Κ.Δ.Π. 314/2001. Use a licensed accountant."
- **R-CY-3: Domestic reverse charge.** Trigger: purchases or sales under articles 11A, 11B, 11Γ or 11Δ (for example construction). Message: "Domestic reverse charge needs specialist classification."
- **R-CY-4: Ship management and maritime services.** Trigger: shipping or maritime services. Message: "Ship management and tonnage tax structures need specialist advice."
- **R-CY-5: Special schemes.** Trigger: tour operator margin scheme, second-hand goods or car margin schemes, investment gold, farmers' scheme, urban taxi scheme, cash accounting, the small business scheme (SME-SS), OSS / IOSS. Message: "Special schemes need specialist computation."
- **R-CY-6: Immovable property.** Trigger: sale, lease or construction of property, including the 5% main-residence scheme. Message: "Immovable property needs specialist review."
- **R-CY-7: Distance sales.** Trigger: B2C sales of goods to other member states, or distance sales into Cyprus by a foreign seller. Message: "The distance-sales threshold and OSS position must be checked by an accountant."

## Section 4: Supplier pattern library

Match by case-insensitive substring. Most specific match wins. "No input VAT" means nothing goes in Box 4; the Box 7 column says whether the net value still belongs in Box 7.

### 4.1 Cypriot banks

| Pattern | Treatment | Box 7 | Notes |
| --- | --- | --- | --- |
| BANK OF CYPRUS, BOC | Exempt: no input VAT for bank charges and fees | Yes (exempt purchase) | Exempt financial service |
| HELLENIC BANK | Same | Yes | Same |
| RCB BANK | Same | Yes | Same |
| EUROBANK CYPRUS | Same | Yes | Same |
| ASTROBANK | Same | Yes | Same |
| REVOLUT, WISE, N26 (fee lines) | Exempt fee lines | Yes | Check for taxable subscription invoices |
| TOKOI, INTEREST | EXCLUDE | No | Interest is not a supply to the business |
| DANEIO, LOAN | EXCLUDE | No | Loan principal |

### 4.2 Cypriot government and statutory bodies

| Pattern | Treatment | Box 7 | Notes |
| --- | --- | --- | --- |
| TAX DEPARTMENT, TMHMA FOROLOGIAS | EXCLUDE | No | Tax payment |
| SOCIAL INSURANCE, KOINONIKON ASFALISION | EXCLUDE | No | Contribution to a fund |
| REGISTRAR OF COMPANIES | EXCLUDE | No | Fees and duties |
| CYPRUS STOCK EXCHANGE | Ask | Ask | Regulatory fee or taxable service: check invoice |

### 4.3 Cypriot utilities

| Pattern | Treatment | Box | Notes |
| --- | --- | --- | --- |
| EAC, ELECTRICITY AUTHORITY CYPRUS | Domestic 19% | 4 (input) | Electricity. Only tariff 08 is in the 5% row |
| WATER BOARD, SYMVOULIO YDATOPROMITHEIAS | Domestic 5% | 4 (input) | Water is in the 5% row |
| CYTA, CYTANET | Domestic 19% | 4 (input) | Telecoms |
| EPIC, PRIMETEL | Domestic 19% | 4 (input) | Telecoms |

### 4.4 Insurance

| Pattern | Treatment | Box 7 | Notes |
| --- | --- | --- | --- |
| GENERAL INSURANCE CYPRUS | Exempt: no input VAT | Yes | Insurance is exempt (Seventh Schedule, Table B) |
| CNP CYPRIALIFE | Same | Yes | Same |
| ALLIANZ CYPRUS | Same | Yes | Same |
| ATLANTIC INSURANCE | Same | Yes | Same |
| ASFALEIA, INSURANCE | Same | Yes | Same |

### 4.5 Post and logistics

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CYPRUS POST, KYPRIAKO TACHYDROMEIO | Exempt: no input VAT | The exemption covers services by Cyprus Post as a public body |
| AKIS EXPRESS, ACS COURIER CY | Domestic 19% | Private couriers are not covered by the Cyprus Post exemption |
| DHL INTERNATIONAL | Check invoice entity | Reverse charge if billed from abroad |

### 4.6 Transport

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TAXI | Domestic 9% | Urban, intercity and rural taxis are in the 9% row |
| INTERCITY BUSES, TRAVEL EXPRESS | Domestic 9% | Intercity and tourist buses are in the 9% row |
| URBAN BUS, RURAL BUS | Domestic 5% | Urban and rural buses are in the 5% row |
| RYANAIR, WIZZ AIR (international) | No Cyprus input VAT unless the ticket shows it | Check the ticket |

### 4.7 Food retail and restaurants

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ALPHAMEGA, PAPANTONIOU, LIDL CY, CARREFOUR CY | Default BLOCK | Personal provisioning |
| RESTAURANT, ESTIATORIO, TAVERNA | Default BLOCK | Entertainment (Section 5.11) |

### 4.8 SaaS: EU suppliers (reverse charge: Boxes 1, 4, 6, 7 and 11B)

| Pattern | Billing entity | Notes |
| --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | EU reverse charge |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | Reverse charge |
| LINKEDIN | LinkedIn Ireland Unlimited (IE) | Reverse charge |
| SPOTIFY | Spotify AB (SE) | EU reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | Reverse charge |
| ATLASSIAN | Atlassian Network Services BV (NL) | EU reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | Reverse charge |
| AWS EMEA SARL | AWS EMEA SARL (LU) | LU = EU reverse charge |

### 4.9 SaaS: non-EU suppliers (reverse charge: Boxes 1, 4, 6 and 7; not 11B)

| Pattern | Billing entity | Notes |
| --- | --- | --- |
| NOTION | Notion Labs Inc (US) | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | Non-EU reverse charge |
| GITHUB | GitHub Inc (US) | Check if billed by an EU entity |
| FIGMA | Figma Inc (US) | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | Non-EU reverse charge |

### 4.10 Payment processors

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE (transaction fees) | Default taxable, reverse charge: output VAT in Box 1, input VAT in Box 4, value in Boxes 6 and 7, plus 11B when billed by an EU entity | The exemptions page puts processing, clearing and authorisation services for card payments at the standard rate. Treat a fee as exempt only where the invoice shows an exempt payment service. |
| PAYPAL (transaction fees) | Same | Same |

### 4.11 Professional services (Cyprus)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DIKIGOROS, LAWYER, ADVOCATE | Domestic 19% | Legal |
| LOGISTIS, ACCOUNTANT, AUDITOR | Domestic 19% | Accounting |
| SYMVOLAIOGRAFOS, NOTARY | Domestic 19% | Notary |

### 4.12 Payroll and contributions

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KOINONIKES ASFALISIS, SOCIAL INSURANCE | EXCLUDE (not in Box 7) | Contributions to funds |
| SALARY, MISTHOS | EXCLUDE (not in Box 7) | Wages |

### 4.13 Property and rent

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ENOIKIO, RENT (commercial, invoice shows VAT) | Domestic 19% | Commercial lease with VAT charged |
| ENOIKIO, RENT (residential or no VAT) | No input VAT; Box 7 if a business expense | Refer property questions (R-CY-6) |

### 4.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| MERISMA, DIVIDEND | EXCLUDE | Not a supply |
| LOAN REPAYMENT | EXCLUDE | Loan principal |
| ATM, CASH WITHDRAWAL | Ask | Default exclude |

## Section 5: Classification rules

### 5.1 Standard rate

Default rate for any supply not in a reduced row of the rates table in Section 1. Output VAT in Box 1, value in Box 6. Input VAT in Box 4, value in Box 7.

### 5.2 Reduced rates

Use only the items the rates table lists for each band. Common traps from the live page:
- Taxis and intercity or tourist buses are in the 9% row; urban and rural buses are in the 5% row.
- Books, newspapers and magazines are in the 3% row, not the 5% row.
- Alcoholic drinks, beer, wine and soft drinks are excluded from the 5% food row (the rates page prints the word as 'καρασί').
- Electricity is standard rated except tariff 08.
- The 3% row is not a social housing rate.

### 5.3 The 5% rate on a main residence

From Tax Department circular 11/2023 (a scanned document; only clean fragments are quoted). The rules apply under the amending law in force from 16 June 2023. The rates page lists this purchase or construction in the 5% row only "μετά από έγκριση του Εφόρου" (after the Commissioner's approval).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/01/%CE%95%CE%95-11_2023.pdf |
| The 5% rate covers the first 130 square metres of buildable area, and only up to this value | EUR 350,000 | "η αξία είναιμέχρι €350.000" |
| If the total value of the purchase or construction exceeds this, the standard rate applies to the WHOLE amount (a cliff) | EUR 475,000 | "πέντε χιλιάδες ευρώ (€475.000), επιβάλλεται Φ.Π.Α. με τον εκάστοτε ισχύοντα κανονικό συντελεστή" |

- Area cliff: the 5% rate does not apply at all where the total buildable area "υπερβαίνει τα 190 τετραγωνικά μέτρα" (exceeds 190 square metres). The circular joins the area and value tests with "ή/και" (and/or): failing either one loses the whole relief.
- Between the two levels the 5% rate is applied pro rata to the square metres, as the circular sets out. The circular also has special rules for large families and for people with disabilities.
- If the owner stops using the home as a residence within ten years, they must tell the Commissioner within thirty days and pay the difference from the standard rate for the unused period; the Tax Department raises the debt by issuing a VAT Return for Special Cases (Δήλωση Φ.Π.Α. για Ειδικές Περιπτώσεις). Sources: https://www.gov.cy/mof-tax/documents/dikaiomata-kai-ypochreoseis/ and https://www.gov.cy/mof-tax/documents/ypovoli-tropopoiisi-diloseon-f-p-a/sychnes-erotiseis-dilosis-f-p-a-gia-eidikes-periptoseis/
- For a VAT return, this matters to a developer or contractor deciding which rate to charge. Refer every case (R-CY-6).

### 5.4 Zero rate and EU supplies

- Exports of goods and the ship and aircraft supplies in the 0% row: value in Box 9 and Box 6.
- Supplies of goods to other EU member states: value in Box 8A and Box 6, and file VIES.
- Services to taxable persons in other EU member states where the customer accounts for the VAT: value in Box 8B and Box 6, and file VIES. Verify the customer's VAT number.
- International passenger transport sold by a Cyprus business: 0% (table in Section 1), value in Box 9 and Box 6.

### 5.5 Exempt supplies

The exempt supplies are in the Seventh Schedule, Tables A and B, of the VAT Law. The Tax Department exemptions page lists, among others: services by Cyprus Post as a public body; hospital and medical care by recognised health professionals; education by public schools and registered private schools and institutes; insurance and reinsurance; credit, bank account, card and other financial services; lotteries, betting and gambling. Property exemptions are on a separate page (R-CY-6). The same page puts card processing, clearing and authorisation services and the collection of third-party receivables at the standard rate. Source: https://www.gov.cy/mof-tax/documents/exairoymenes-synallages/

Exempt sales go in Box 6 (no VAT in Box 1). Exempt purchases go in Box 7 (no VAT in Box 4).

### 5.6 Reverse charge: services received from another EU member state

For services whose place of supply is Cyprus (article 11), received from a taxable person in another member state: self-assess output VAT in **Box 1** (not Box 2), claim input VAT in Box 4 under the conditions of article 21, enter the value in **Boxes 6 and 7**, and also in **Box 11B**.

### 5.7 Reverse charge: services received from outside the EU

Output VAT in **Box 1**, input VAT in Box 4 under article 21, value in **Boxes 6 and 7**. Nothing in Box 11B.

### 5.8 Acquisitions of goods from another EU member state

Output VAT in **Box 2**, input VAT in Box 4 under article 21, value in **Boxes 7 and 11A**. The tax point is the earlier of the supplier's invoice date and the 15th day of the month after the goods were sent.

### 5.9 Imports of goods from outside the EU

VAT paid on import goes in Box 4. The value of goods cleared through customs in the period goes in Box 7.

### 5.10 Domestic reverse charge (articles 11A to 11Δ)

Output VAT in Box 1, input VAT in Box 4 under article 21, value in Boxes 6 and 7. Refer (R-CY-3).

### 5.11 Input VAT that must not go in Box 4

The return guide says do not include VAT on:
- purchases for private use;
- business entertainment of employees or of persons engaged in managing a company ("για επιχειρηματική ψυχαγωγία σε εργοδοτούμενους, ή σε πρόσωπα που ασχολούνται με τη διεύθυνση εταιρείας");
- second-hand goods bought under the second-hand goods scheme;
- payments to the Tax Department under an assessment.

To claim any input VAT, the business must hold a tax invoice dated in the period. Credit notes received reduce Box 4.

Client entertainment and motor vehicles. The Tax Department's General VAT Guide (Information Leaflet 10, dated November 2001, still published on gov.cy) lists among the VAT that may not be deducted: the purchase, hire or import of a motor car, other than taxis, hire cars and driving-school cars, where "car" means an ordinary passenger car and excludes single-seaters, vehicles with more than ten seats, commercial and van-type vehicles, caravans, ambulances and vehicles over three tonnes; and business entertainment expenses, without limiting them to employees or managers. The guide predates the current law, so this Guide keeps the conservative default (block, ask, refer) and does not restate the rule as current law. Source: https://www.gov.cy/media/sites/167/2026/01/%CE%93%CE%B5%CE%BD%CE%B9%CE%BA%CF%8C%CF%82-%CE%9F%CE%B4%CE%B7%CE%B3%CF%8C%CF%82-%CE%A6.%CE%A0.%CE%91.-%CE%95%CE%BD%CE%B7%CE%BC%CE%B5%CF%81%CF%89%CF%84%CE%B9%CE%BA%CF%8C-%CE%88%CE%BD%CF%84%CF%85%CF%80%CE%BF-10.pdf

### 5.12 Output VAT that is easy to miss

The return guide lists output VAT due in Box 1 beyond normal sales, including: services received from abroad and reverse charge purchases; commission on sales made for third parties; sales of fixed assets; goods taken for private use; VAT on self-billed invoices; VAT refunded for bad debts that are later recovered; and gifts of goods above a cost limit (table below). Credit notes issued reduce Box 1.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.gov.cy/media/sites/167/2026/01/%CE%9F%CE%B4%CE%B7%CE%B3%CF%8C%CF%82-%CE%B3%CE%B9%CE%B1-%CE%A3%CF%85%CE%BC%CF%80%CE%BB%CE%AE%CF%81%CF%89%CF%83%CE%B7-%CE%94%CE%AE%CE%BB%CF%89%CF%83%CE%B7%CF%82-%CE%A6%CE%A0%CE%91-06082024.pdf |
| Goods given as gifts: output VAT is due when the cost exceeds this (see circular 195) | EUR 17 | "δώρα όταν το κόστος υπερβαίνει το ποσό των €17" |

### 5.13 Return format rules

From the same return guide:
- Boxes 1 to 5 are VAT amounts: two decimals, with a comma as the decimal sign, not a point, no thousands separators, a minus sign for a negative amount, "0" when empty. Box 3 must equal Box 1 plus Box 2, and Box 5 must equal Box 3 minus Box 4.
- Boxes 6 to 11B are values without VAT, rounded to the nearest euro, "0" when empty.
- Box 6 must be at least the sum of Boxes 8A, 8B, 9, 10 and 11B. Box 7 must be at least the sum of Boxes 11A and 11B.
- Leave out of Box 6: capital you put into the business, loans, dividends, insurance compensation, and stock exchange transactions (unless you are a financial institution).
- Leave out of Box 7: wages, contributions to funds, money donations, interest, dividends, taxes and fees.
- Triangular transactions as the intermediate supplier: purchase value in Box 7, sale value in Boxes 6 and 10.
- A negative Box 5 is a credit. It can be carried forward, set off against other tax owed, or claimed back on form 4B with the return if the conditions for a refund are met.

## Section 6: Tier 2 catalogue

### 6.1 Fuel and vehicle costs

Default: no recovery. Question: "Vehicle type and business-use percentage?" Refer (Section 5.11).

### 6.2 Entertainment

Default: block. Question: "Who was entertained, and for what business purpose?"

### 6.3 Ambiguous SaaS

Default: non-EU reverse charge. Question: "Check invoice entity."

### 6.4 Owner transfers

Default: exclude. Question: "Customer payment, own money, or loan?"

### 6.5 Individual incoming

Default: domestic B2C at the standard rate. Question: "Sale? Country?"

### 6.6 Foreign incoming

Default: standard rate. Question: "B2B? Country? VAT number?"

### 6.7 Large purchases

Default: deductible if business use is confirmed; flag if a capital item. Question: "Useful life more than one year?"

### 6.8 Mixed-use telecom or home office

Default: no recovery. Question: "Business line or mixed?"

### 6.9 Outgoing to individuals

Default: exclude. Question: "Contractor, wages, or personal?"

### 6.10 Cash withdrawals

Default: exclude. Question: "Cash purpose?"

### 6.11 Rent

Default: no input VAT unless the invoice shows VAT. Question: "Commercial or residential? Does the landlord charge VAT?"

### 6.12 Basic goods around 30 September 2026

Default: 0% only for supplies made up to and including 30 September 2026; the normal rate after. Question: "Which sales of baby milk, nappies, meat, fish or fruit and vegetables fall before and after 1 October 2026?"

## Section 7: Worked examples

All amounts in these examples are hypothetical bank lines in euro. The arithmetic is checked in `quality-cases.json`.

### Example 1: Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; -14.68 ; EUR`

**Reasoning:**
US supplier, service received from outside the EU. Self-assess output VAT at the standard rate in Box 1. Claim the same amount in Box 4 if the service is used for taxable supplies. Value in Boxes 6 and 7. Nothing in Box 11B. Net VAT effect zero.

| Date | Counterparty | Net | VAT | Rate | Box (input) | Box (output) | Value boxes | Default? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 03.04.2026 | NOTION LABS INC | 14.68 | 2.79 | 19% | 4 | 1 | 6, 7 | N |

### Example 2: EU service reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads ; -850.00 ; EUR`

**Reasoning:**
Irish supplier, service received from another member state. Output VAT in Box 1, input in Box 4, value in Boxes 6, 7 and 11B.

| Date | Counterparty | Net | VAT | Rate | Box (input) | Box (output) | Value boxes | Default? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | GOOGLE IRELAND LIMITED | 850.00 | 161.50 | 19% | 4 | 1 | 6, 7, 11B | N |

### Example 3: Entertainment

**Input line:**
`15.04.2026 ; COLUMBIA STEAK HOUSE LIMASSOL ; DEBIT ; Business dinner ; -220.00 ; EUR`

**Reasoning:**
Restaurant bill. The return guide bars input VAT on business entertainment of employees or company managers; the 2001 General VAT Guide blocks business entertainment generally. Default: block and ask who attended.

| Date | Counterparty | Gross | VAT claimed | Box | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | COLUMBIA STEAK HOUSE | 220.00 | 0 | none | Y | "Who was entertained?" |

### Example 4: Equipment purchase

**Input line:**
`18.04.2026 ; LOGITECH CYPRUS ; DEBIT ; Laptop ; -1,595.00 ; EUR`

**Reasoning:**
Business equipment bought in Cyprus with a tax invoice. Input VAT at the standard rate in Box 4, net value in Box 7.

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 18.04.2026 | LOGITECH CYPRUS | 1,595.00 | 1,340.34 | 254.66 | 19% | 4 (VAT), 7 (net) | N |

### Example 5: EU B2B service sale

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; IT consultancy ; +3,500.00 ; EUR`

**Reasoning:**
Service to a German business. The customer accounts for the VAT in Germany. No Cyprus VAT; value in Boxes 8B and 6; include on the VIES statement. Verify the customer's VAT number.

| Date | Counterparty | Net | VAT | Box | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- |
| 22.04.2026 | STUDIO KREBS GMBH | 3,500.00 | 0 | 8B, 6 | Y | "Verify the German VAT number" |

### Example 6: Fuel

**Input line:**
`28.04.2026 ; PETROLINA STATIONS ; DEBIT ; Fuel ; -60.00 ; EUR`

**Reasoning:**
Fuel. Business use unknown and the 2001 General VAT Guide blocks VAT on passenger cars; fuel is not addressed. Default: no recovery, ask, refer.

| Date | Counterparty | Gross | VAT claimed | Box | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- |
| 28.04.2026 | PETROLINA STATIONS | 60.00 | 0 | none | Y | "Vehicle and business-use percentage?" |

## Section 8: Excel working paper template (Cyprus-specific)

Per `vat-workflow-base` Section 3. Column H accepts the Cyprus return box codes (1 to 11B). Sheet "Box Summary" maps directly to the return. Check the format rules in Section 5.13 before filing. Bottom line: Box 5 (Box 3 minus Box 4).

## Section 9: Cyprus bank statement reading guide

**CSV conventions.** Bank of Cyprus and Hellenic Bank typically use comma delimiters and DD/MM/YYYY dates.

**Greek language variants.** Enoikio (rent), misthos (salary), tokoi (interest), metafora (transfer). Treat as the English equivalent.

**Internal transfers.** "Own transfer", "esoteriki metafora". Exclude.

**IBAN prefix.** CY = Cyprus. IE, DE, NL = EU. US, GB = non-EU.

## Section 10: Onboarding fallback

### 10.1 Entity type

Inference: Ltd = company; otherwise sole trader. Fallback: "Company or self-employed?"

### 10.2 VAT registration

Fallback: "Are you VAT-registered? If not, have your taxable sales in the last twelve months passed the registration threshold?"

### 10.3 VAT number

Fallback: "CY VAT number? (CY + 8 digits + letter)"

### 10.4 Filing period

Inference: quarterly. Fallback: "Which tax period does your registration certificate show?"

### 10.5 Industry

Fallback: "What does the business do?"

### 10.6 Exempt supplies

Fallback: "Any exempt supplies?" If yes: R-CY-2.

### 10.7 Credit brought forward

Fallback: "Excess VAT credit from the prior period?"

### 10.8 Cross-border customers

Fallback: "Customers outside Cyprus? Businesses or consumers?"

## The method, step by step

1. Confirm the business must file: registered, or required to register under the tests in the VAT registration page (https://www.gov.cy/mof-tax/documents/eggrafi-akyrosi-f-p-a/eggrafes-mitrooy-f-p-a/ypochreosi-dikaioma-eggrafis-sto-mitroo-f-p-a/). If not, R-CY-1.
2. Confirm the tax period on the registration certificate and the deadline: the 10th day after the end of the month following the period, moved to the next working day if it falls on a weekend or holiday (https://www.gov.cy/mof-tax/prothesmies/).
3. Classify each sale by the rates page (https://www.gov.cy/mof-tax/documents/syntelestes-f-p-a/): standard, 9%, 5%, 3%, 0%, exempt (https://www.gov.cy/mof-tax/documents/exairoymenes-synallages/), or EU or out-of-scope. Split basic goods at 30 September 2026.
4. Classify each purchase with the supplier library and the reverse charge rules in Sections 5.6 to 5.10, which follow the Tax Department return guide (https://www.gov.cy/media/sites/167/2026/01/%CE%9F%CE%B4%CE%B7%CE%B3%CF%8C%CF%82-%CE%B3%CE%B9%CE%B1-%CE%A3%CF%85%CE%BC%CF%80%CE%BB%CE%AE%CF%81%CF%89%CF%83%CE%B7-%CE%94%CE%AE%CE%BB%CF%89%CF%83%CE%B7%CF%82-%CE%A6%CE%A0%CE%91-06082024.pdf). Services from abroad: output VAT in Box 1. Goods from the EU: output VAT in Box 2.
5. Remove blocked input VAT (Section 5.11) and add easy-to-miss output VAT (Section 5.12).
6. Fill Boxes 1 to 11B and run the format checks in Section 5.13.
7. Check for errors in earlier returns. Correct them in this return only within the limit and the three-year window in the corrections FAQ (https://www.gov.cy/mof-tax/documents/ypovoli-tropopoiisi-diloseon-f-p-a/sychnes-erotiseis-se-schesi-me-tis-diorthoseis-lathon/); otherwise write to the Tax Department through TFA.
8. File in TFA and pay by the deadline, or claim the credit or a refund on form 4B (https://www.gov.cy/media/sites/167/2026/01/%CE%9F%CE%B4%CE%B7%CE%B3%CF%8C%CF%82-%CE%B3%CE%B9%CE%B1-%CE%A3%CF%85%CE%BC%CF%80%CE%BB%CE%AE%CF%81%CF%89%CF%83%CE%B7-%CE%94%CE%AE%CE%BB%CF%89%CF%83%CE%B7%CF%82-%CE%A6%CE%A0%CE%91-06082024.pdf). File VIES by the 15th day after each month with EU supplies (https://www.gov.cy/mof-tax/documents/dikaiomata-kai-ypochreoseis/).

## Ask the client first

- Which tax period does your VAT registration certificate show (quarter ending which month, or monthly)?
- Do you make any exempt supplies, such as financial services, insurance, medical care, education, or property letting? (Partial exemption, R-CY-2.)
- Do you sell to customers in other EU countries, and are they businesses with VAT numbers or consumers? (Boxes 8A and 8B, VIES, distance sales.)
- Do you buy services or goods from suppliers outside Cyprus? Which entity bills you? (Box 1 or Box 2, and 11A or 11B.)
- Did you sell baby milk, nappies, meat, fish or fruit and vegetables in a period that includes 30 September 2026?
- Did you find errors in earlier returns, and how large are they in total? (The correction limit in Section 2.)

## When to refuse or refer

- Partial exemption, domestic reverse charge, ship management, any special scheme, property (including the 5% main-residence scheme), and distance sales: R-CY-2 to R-CY-7.
- The business is not established in Cyprus, or is in the small business scheme (Law 104(I)/2025) or OSS / IOSS.
- Errors in earlier returns above the correction limit or older than three years: the business must write to the Tax Department.
- Client entertainment, cars and fuel, where the amount matters: the only source is the Tax Department's 2001 General VAT Guide, which predates the current law.
- Late registration or unfiled returns: penalties, interest and possible estimated assessments.

## Sources

1. Tax Department, VAT rates: https://www.gov.cy/mof-tax/documents/syntelestes-f-p-a/
2. Tax Department, obligation and right to register for VAT: https://www.gov.cy/mof-tax/documents/eggrafi-akyrosi-f-p-a/eggrafes-mitrooy-f-p-a/ypochreosi-dikaioma-eggrafis-sto-mitroo-f-p-a/
3. Tax Department, submitting and amending VAT returns: https://www.gov.cy/mof-tax/documents/ypovoli-tropopoiisi-diloseon-f-p-a/
4. Tax Department, guide to completing the VAT return: https://www.gov.cy/media/sites/167/2026/01/%CE%9F%CE%B4%CE%B7%CE%B3%CF%8C%CF%82-%CE%B3%CE%B9%CE%B1-%CE%A3%CF%85%CE%BC%CF%80%CE%BB%CE%AE%CF%81%CF%89%CF%83%CE%B7-%CE%94%CE%AE%CE%BB%CF%89%CF%83%CE%B7%CF%82-%CE%A6%CE%A0%CE%91-06082024.pdf
5. Tax Department, VAT return FAQ: https://www.gov.cy/mof-tax/documents/ypovoli-tropopoiisi-diloseon-f-p-a/sychnes-erotiseis-dilosis-f-p-a/
6. Tax Department, FAQ on correcting errors: https://www.gov.cy/mof-tax/documents/ypovoli-tropopoiisi-diloseon-f-p-a/sychnes-erotiseis-se-schesi-me-tis-diorthoseis-lathon/
7. Tax Department, rights and obligations: https://www.gov.cy/mof-tax/documents/dikaiomata-kai-ypochreoseis/
8. Tax Department, exempt transactions: https://www.gov.cy/mof-tax/documents/exairoymenes-synallages/
9. Tax Department, circular 11/2023 on the 5% residence rate: https://www.gov.cy/media/sites/167/2026/01/%CE%95%CE%95-11_2023.pdf
10. Tax Department, deadline calendar: https://www.gov.cy/mof-tax/prothesmies/
11. VAT Law N.95(I)/2000 as amended, and Κ.Δ.Π. 314/2001 (cited by section in words).
12. EU VAT Directive 2006/112/EC: via the `eu-vat-directive` Guide.
13. Consolidated VAT Law (Κ.Δ.Π. 221/2026): https://www.gov.cy/media/sites/167/2026/01/Consolidated-VAT-Law-%CE%9A%CE%94%CE%A0-221_2026.pdf
14. Tax Department, General VAT Guide (Information Leaflet 10, November 2001): https://www.gov.cy/media/sites/167/2026/01/%CE%93%CE%B5%CE%BD%CE%B9%CE%BA%CF%8C%CF%82-%CE%9F%CE%B4%CE%B7%CE%B3%CF%8C%CF%82-%CE%A6.%CE%A0.%CE%91.-%CE%95%CE%BD%CE%B7%CE%BC%CE%B5%CF%81%CF%89%CF%84%CE%B9%CE%BA%CF%8C-%CE%88%CE%BD%CF%84%CF%85%CF%80%CE%BF-10.pdf

### Known gaps

1. Ship management and maritime sector not covered.
2. Domestic reverse charge, special schemes and immovable property are refusals.
3. The EU distance-sales threshold and the VAT number format are not proved on an allowed page. The rules on client entertainment and on cars and fuel rest only on a 2001 document (Source 14), which predates the current law.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date version of this Guide is maintained at openaccountants.com.

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
