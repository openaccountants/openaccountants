---
name: albania-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Albanian VAT (TVSH) return for any client. Trigger on phrases like "Albania VAT", "Albanian TVSH", "TVSH return", "DPT filing", "Albanian tax", or any request involving Albanian VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Albania only — standard TVSH payers filing monthly returns. Small business exemptions, free economic zones, agricultural compensation schemes, and margin schemes are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any Albanian VAT work.
version: 2.0
---

# Albania VAT (TVSH) Return Skill v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content.**

| Field | Value |
|---|---|
| Country | Albania (Republic of Albania) |
| Tax name | TVSH (Tatimi mbi Vleren e Shtuar) |
| Standard rate | 20% |
| Reduced rates | 6% (accommodation/tourism by certified structures), 10% (agricultural inputs — fertilisers, pesticides, seeds) |
| Zero rate | 0% (exports, international transport, diplomatic supplies) |
| Return form | Monthly TVSH declaration (electronic) |
| Filing portal | https://e-filing.tatime.gov.al |
| Authority | General Directorate of Taxation (DPT — Drejtoria e Pergjithshme e Tatimeve) |
| Currency | ALL (Albanian Lek) only |
| Filing frequency | Monthly (all TVSH payers) |
| Deadline | 14th of the month following the reporting month |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending — requires validation by licensed Albanian tax practitioner |
| Validation date | April 2026 (web-verified; practitioner sign-off pending) |

**Key TVSH return boxes:**

| Box | Meaning |
|---|---|
| 1 | Taxable supplies at 20% — tax base |
| 2 | Output TVSH at 20% |
| 3 | Taxable supplies at 6% — tax base |
| 4 | Output TVSH at 6% |
| 5 | Zero-rated supplies (exports) |
| 6 | Exempt supplies |
| 7 | Self-assessed TVSH on services from abroad (reverse charge) — base |
| 8 | Output TVSH on reverse charge |
| 9 | Total output TVSH (2 + 4 + 8) |
| 10 | Domestic purchases — tax base |
| 11 | Input TVSH on domestic purchases |
| 12 | Imports — customs value + duties |
| 13 | TVSH paid on imports |
| 14 | Fixed asset acquisitions — tax base |
| 15 | Input TVSH on fixed assets |
| 16 | Input TVSH on reverse charge (deductible) |
| 17 | Adjustments to input TVSH |
| 18 | Total input TVSH (11 + 13 + 15 + 16 + 17) |
| 19 | TVSH payable (if 9 > 18) |
| 20 | TVSH credit (if 18 > 9) |
| 21 | TVSH credit from prior period |
| 22 | TVSH credit for refund |
| 23 | Net TVSH payable |

**Conservative defaults — Albania-specific values:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 20% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Albania |
| Unknown business-use proportion (vehicle, phone) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-resident (Box 7/8/16) |
| Unknown blocked-input status (entertainment, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |
| Unknown tourism certification status | 20% (not 6%) |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | ALL 500,000 |
| HIGH tax-delta on a single conservative default | ALL 30,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net TVSH position | ALL 800,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Albanian bank: Banka Kombetare Tregtare (BKT), Raiffeisen Bank Albania, Credins Bank, Intesa Sanpaolo Albania, OTP Bank Albania, Tirana Bank, Alpha Bank Albania, or any other.

**Recommended** — sales invoices (especially for exports and zero-rated supplies), purchase invoices for any input TVSH claim above ALL 30,000, the client's NUIS/NIPT in writing.

**Ideal** — complete fiscalized invoice register (from DPT e-Filing), prior period TVSH declaration, purchase and sales books.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This TVSH return was produced from bank statement alone. The reviewer must verify that input TVSH claims are supported by fiscalized invoices (NIVF code present) and that all reverse-charge classifications match the supplier's invoice."

### Albania-specific refusal catalogue

**R-AL-1 — Small business / non-registered entity attempting to file TVSH.** *Trigger:* client turnover below ALL 10,000,000 and not voluntarily VAT-registered, or client on the small business tax regime. *Message:* "Non-registered entities and those on the small business tax regime cannot file TVSH returns or claim input TVSH. This skill covers registered TVSH payers only."

**R-AL-2 — Free economic zone entity.** *Trigger:* client operates within a designated free economic zone (Spitalla, Koplik, Vlora). *Message:* "Free economic zone entities have special TVSH treatment that requires case-by-case analysis. Please escalate to a qualified Albanian tax practitioner."

**R-AL-3 — Agricultural compensation scheme.** *Trigger:* client is a small agricultural producer on the flat-rate compensation scheme. *Message:* "The agricultural compensation scheme under Article 92 has specific rules for deemed input TVSH. Out of scope for this skill."

**R-AL-4 — Partial exemption / proportional deduction.** *Trigger:* client makes both taxable and exempt supplies and the exempt proportion is not de minimis. *Message:* "Your input TVSH must be apportioned under Article 73. This requires an annual pro-rata calculation. Please use a qualified practitioner to determine the deductible proportion."

**R-AL-5 — Margin scheme.** *Trigger:* client deals in second-hand goods, art, antiques under the margin scheme. *Message:* "Margin scheme transactions require transaction-level margin computation. Out of scope."

**R-AL-6 — Income tax instead of TVSH.** *Trigger:* user asks about Albanian income tax, not the TVSH return. *Message:* "This skill only handles the monthly TVSH return. For Albanian income tax, use the appropriate income tax skill."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. Match by case-insensitive substring on the counterparty name as it appears in the bank statement.

### 3.1 Albanian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BKT, BANKA KOMBETARE TREGTARE | EXCLUDE for bank charges/fees | Financial service, exempt |
| RAIFFEISEN, RAIFFEISEN BANK AL | EXCLUDE for bank charges/fees | Same |
| CREDINS, CREDINS BANK | EXCLUDE for bank charges/fees | Same |
| INTESA SANPAOLO AL, ISP ALBANIA | EXCLUDE for bank charges/fees | Same |
| OTP BANK AL, TIRANA BANK, ALPHA BANK | EXCLUDE for bank charges/fees | Same |
| INTERESA, INTEREST, KAMATA | EXCLUDE | Interest income/expense, out of scope |
| KREDI, LOAN, HUADHENIE | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Albanian government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| DPT, DREJTORIA E TATIMEVE | EXCLUDE | Tax payment, not a supply |
| DOGANA, CUSTOMS | EXCLUDE | Customs duty (but see import TVSH for Box 12/13) |
| ISSH, SIGURIMET SHOQERORE | EXCLUDE | Social insurance contribution |
| QKR, QENDRA KOMBETARE E REGJISTRIMIT | EXCLUDE | Business registration fee |
| BASHKIA, MUNICIPALITY | EXCLUDE | Local government fee |
| TATIME, TAX OFFICE | EXCLUDE | Tax payment |

### 3.3 Albanian utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| OSHEE, OPERATORI SHPERNDARJES ENERGJISE | Domestic 20% | 10/11 | Electricity — overhead |
| UKT, UJESJELLESI | Domestic 20% | 10/11 | Water utility |
| ALBTELEKOM, ALBtelecom | Domestic 20% | 10/11 | Telecoms — overhead |
| ONE ALBANIA, VODAFONE AL | Domestic 20% | 10/11 | Mobile telecoms |
| ALBAGAS, ALBPETROL | Domestic 20% | 10/11 | Gas/fuel supply |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SIGAL, SIGMA, INSIG | EXCLUDE | Insurance, exempt |
| INTERSIG, ALBSIG, EUROSIG | EXCLUDE | Same |
| SIGURIM, INSURANCE, POLICA | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| POSTA SHQIPTARE | EXCLUDE for standard postage | | Universal postal service, exempt |
| POSTA SHQIPTARE (courier/parcel) | Domestic 20% | 10/11 | Non-universal services taxable |
| DHL ALBANIA, TNT, FedEx | Domestic 20% | 10/11 | Express courier, taxable |

### 3.6 Transport

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| ALBTRANSPORT, URBAN BUS | EXCLUDE | | Public transport, exempt |
| TAXI, TRANSFER | Domestic 20% | 10/11 | Local taxi |
| WIZZ AIR, TURKISH AIRLINES (international) | EXCLUDE / 0% | | International flights zero rated |

### 3.7 Food and entertainment (blocked)

| Pattern | Treatment | Notes |
|---|---|---|
| SUPERMARKET, CONAD, SPAR AL, NEPTUN | Default BLOCK input TVSH | Personal provisioning |
| RESTAURANT, RESTORANT, BAR, KAFE | Default BLOCK | Entertainment blocked under Article 71(3) |
| HOTEL (non-tourism business) | Default BLOCK | Entertainment/hospitality blocked |

### 3.8 SaaS — non-resident suppliers (reverse charge, Box 7/8/16)

Albania is not an EU member state. All foreign SaaS providers are non-resident suppliers triggering reverse charge.

| Pattern | Billing entity | Box | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) or Google LLC (US) | 7/8/16 | Reverse charge |
| MICROSOFT (365, Azure) | Microsoft Ireland or Microsoft Corp (US) | 7/8/16 | Reverse charge |
| ADOBE | Adobe Systems (IE or US) | 7/8/16 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland or Meta (US) | 7/8/16 | Reverse charge |
| SLACK, ZOOM, DROPBOX | Various non-resident entities | 7/8/16 | Reverse charge |
| AWS, AMAZON WEB SERVICES | AWS EMEA SARL (LU) or AWS Inc (US) | 7/8/16 | Reverse charge |
| NOTION, ANTHROPIC, OPENAI, GITHUB, FIGMA, CANVA | US entities | 7/8/16 | Reverse charge |

### 3.9 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing, financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |

### 3.10 Professional services (Albania)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| NOTER, NOTAR, NOTARY | Domestic 20% | 10/11 | Deductible if business purpose |
| KONTABILIST, AUDITOR, EKSPERT KONTABEL | Domestic 20% | 10/11 | Always deductible |
| AVOKAT, LAWYER, JURIST | Domestic 20% | 10/11 | Deductible if business legal matter |
| QKR fees | EXCLUDE | | Government fee, not a supply |

### 3.11 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| ISSH, SOCIAL INSURANCE, SIGURIME | EXCLUDE | Social/health insurance payment |
| PAGA, SALARY, RROGA | EXCLUDE | Wages — outside TVSH scope |
| TAP, TATIM MBI TE ARDHURAT | EXCLUDE | Income tax withholding |

### 3.12 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| QIRA (commercial, with TVSH invoice) | Domestic 20% | Commercial lease, taxable |
| QIRA (residential, no TVSH) | EXCLUDE | Residential lease, exempt |

### 3.13 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFERTE, INTERNAL, BRENDSHME | EXCLUDE | Internal movement |
| DIVIDENT, DIVIDEND | EXCLUDE | Dividend, out of scope |
| TERHEQJE, ATM, CASH WITHDRAWAL | TIER 2 — ask | Default exclude; ask what cash was spent on |

---

## Section 4 — Worked examples

Six worked classifications from a hypothetical bank statement of an Albanian self-employed IT consultant based in Tirana.

### Example 1 — Non-resident SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; ALL 1,760`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.8). No Albanian registration. This is a service received from a non-resident. Reverse charge under Article 86: self-assess output TVSH at 20% in Box 7/8, claim input TVSH in Box 16. Net effect zero for a fully taxable business.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (input) | Box (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -1,760 | -1,760 | 352 | 20% | 16 | 7/8 | N | — | — |

### Example 2 — Non-resident SaaS reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -93,500 ; ALL`

**Reasoning:**
Google Ireland Ltd is non-resident (Albania is not EU). Reverse charge at 20%. Box 7 for the base, Box 8 for output TVSH, Box 16 for input TVSH credit. Both sides must appear on the return.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (input) | Box (output) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -93,500 | -93,500 | 18,700 | 20% | 16 | 7/8 | N | — | — |

### Example 3 — Entertainment, fully blocked

**Input line:**
`15.04.2026 ; RESTORANT MULLIRI I VJETER ; DEBIT ; Business dinner ; -24,000 ; ALL`

**Reasoning:**
Restaurant transaction. Entertainment and hospitality expenses are blocked under Article 71(3). Input TVSH is irrecoverable regardless of business purpose. Default: full block.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTORANT MULLIRI I VJETER | -24,000 | -24,000 | 0 | — | — | Y | Q1 | "Entertainment: blocked" |

### Example 4 — Fixed asset purchase

**Input line:**
`18.04.2026 ; NEPTUN SHPK ; DEBIT ; Laptop HP ProBook ; -175,000 ; ALL`

**Reasoning:**
The item is a laptop with useful life over 12 months — qualifies as a fixed asset under Albanian accounting standards. Goes to Box 14 (net base) and Box 15 (input TVSH). Must have a fiscalized invoice with NIVF code.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | NEPTUN SHPK | -175,000 | -145,833 | -29,167 | 20% | 14/15 | N | — | — |

### Example 5 — Export of services (zero-rated)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; IT consultancy March ; +385,000 ; ALL`

**Reasoning:**
Incoming payment from a German company for IT consulting services. Export of services — zero-rated under Article 54. Report net in Box 5. No output TVSH. Related input TVSH is fully deductible. Requires: customs/export documentation or service export evidence.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +385,000 | +385,000 | 0 | 0% | 5 | Y | Q2 (HIGH) | "Verify export documentation" |

### Example 6 — Motor vehicle, blocked

**Input line:**
`28.04.2026 ; AUTOSTAR SHPK ; DEBIT ; Car lease payment Hyundai ; -71,500 ; ALL`

**Reasoning:**
Car lease payment. Input TVSH on passenger vehicles is blocked under Article 71(2). Exceptions only for taxis, rental fleet, driving school, delivery vehicles. An IT consultant does not qualify. Default: full block.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | AUTOSTAR SHPK | -71,500 | -71,500 | 0 | — | — | Y | Q3 | "Motor vehicle: blocked" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 20% (Article 56)

Default rate for any taxable supply unless a reduced rate, zero rate, or exemption applies. Sales at 20% go to Box 1/2. Purchases at 20% go to Box 10/11.

### 5.2 Reduced rate 6% — accommodation/tourism (Article 56(1.1))

Applies only to accommodation services by certified tourism structures (hotels, resorts, guesthouses, agritourism). The service provider must hold a valid tourism licence. Restaurant, bar, spa services within hotels are at 20%. Sales at 6% go to Box 3/4.

### 5.3 Reduced rate 10% — agricultural inputs (Article 56)

Applies to chemical fertilisers, pesticides, seeds, seedlings. Narrow category.

### 5.4 Zero rate (Articles 51-55)

Exports of goods outside Albania (requires customs export declaration). International transport services. Supplies to diplomatic missions. Report in Box 5.

### 5.5 Exempt supplies (Article 51)

Financial and banking services, insurance, medical/dental (licensed), educational (accredited), residential rental, postal universal service, cultural events (public interest), gambling (separately taxed), burial services, social welfare, agricultural land, gold to Bank of Albania. No output TVSH, no input TVSH deduction on related costs.

### 5.6 Domestic purchases — input TVSH

Input TVSH deductible if: (a) goods/services for taxable operations, (b) valid fiscalized invoice (NIVF present), (c) recorded in accounting, (d) supplier is TVSH registered. Box 10 (base) / Box 11 (input TVSH). Fixed assets go to Box 14/15.

### 5.7 Reverse charge — services from non-residents (Article 86)

When the client receives services from a non-resident with no Albanian registration and place of supply is Albania: self-assess at 20%. Box 7 (base), Box 8 (output TVSH), Box 16 (input TVSH credit if entitled). Net effect zero for fully taxable business.

### 5.8 Import of goods

Goods imported into Albania: TVSH collected by customs at the border. Base = customs value + duties + excise. Rate 20% (or reduced if applicable). Box 12 (base) / Box 13 (input TVSH). Recoverable with customs declaration as evidence.

### 5.9 Blocked input TVSH (Article 71)

Zero TVSH recovery with no exceptions unless specifically noted:
- Passenger vehicles: purchase, lease, fuel (unless taxi/rental/driving school/delivery fleet) — Article 71(2)
- Entertainment, hospitality, representation — Article 71(3)
- Personal consumption of employees/directors — Article 71(4)
- Without valid fiscalized invoice — Article 69
- Goods/services for exempt operations — Article 71
- Goods lost/destroyed (except force majeure) — Article 71
- Accommodation/catering for staff (unless remote work site) — Article 71

Blocked categories override all other rules. Check blocked status first.

### 5.10 Fiscalization requirement (Law No. 87/2019)

All invoices must be electronically registered through the fiscalization system (since 2021). Each invoice receives a NIVF code. Non-fiscalized invoices may result in denial of input TVSH deduction.

### 5.11 Credit notes and returns (Article 82)

Seller reduces output TVSH in current period. Buyer reduces input TVSH in current period. Credit note must be fiscalized.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* Kastrati, Kurum, Shell, fuel receipts. *Why insufficient:* vehicle type and use unknown. Cars are blocked regardless. *Default:* 0% recovery. *Question:* "Is this a car (blocked) or a commercial vehicle used exclusively for business?"

### 6.2 Restaurants and entertainment

*Pattern:* any restaurant, cafe, bar. *Why insufficient:* entertainment is hard blocked under Article 71(3). *Default:* block. *Question:* "Was this entertainment? (Note: blocked regardless — for income tax records only.)"

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, Adobe, Meta, etc. *Why insufficient:* billing entity not visible on bank statement. *Default:* reverse charge Box 7/8/16 (all non-resident for Albania). *Question:* "Could you check the invoice for the legal entity name?"

### 6.4 Round-number incoming transfers from owner-named counterparties

*Pattern:* large round credit matching client's name. *Default:* exclude as owner injection. *Question:* "Is this a customer payment, your own money, or a loan?"

### 6.5 Incoming transfers from individual names

*Pattern:* incoming from private-looking counterparties. *Default:* domestic sale at 20%, Box 1/2. *Question:* "Was this a sale? Business or consumer?"

### 6.6 Incoming transfers from foreign counterparties

*Pattern:* foreign IBAN or currency. *Default:* zero-rated export Box 5. *Question:* "What was this — export sale, service, refund? Do you have export documentation?"

### 6.7 Large one-off purchases (potential fixed assets)

*Pattern:* single invoice for equipment, laptop, machinery. *Default:* if asset with useful life >12 months, Box 14/15; otherwise Box 10/11. *Question:* "Is this equipment with useful life over 12 months?"

### 6.8 Mixed-use phone, internet

*Pattern:* ONE Albania, Vodafone personal lines, home electricity. *Default:* 0% if mixed without declared proportion. *Question:* "Is this a dedicated business line or mixed-use?"

### 6.9 Outgoing transfers to individuals

*Pattern:* outgoing to private names. *Default:* exclude as drawings. *Question:* "Was this a contractor payment with invoice, wages, or personal transfer?"

### 6.10 Cash withdrawals

*Pattern:* ATM, terheqje, cash withdrawal. *Default:* exclude. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* monthly qira, rent to landlord-sounding name. *Default:* no TVSH, no deduction (residential default). *Question:* "Is this commercial property? Does the landlord charge TVSH?"

### 6.12 Foreign hotel and accommodation

*Pattern:* hotel abroad. *Default:* exclude from input TVSH (non-Albanian VAT). *Question:* "Was this a business trip?"

### 6.13 Tourism income at 6%

*Pattern:* booking.com payouts, hotel/accommodation income. *Default:* flag for reviewer — verify tourism certification. *Question:* "Do you hold a valid tourism licence? Is this accommodation under 3 months?"

---

## Section 7 — Excel working paper template

The base specification is in `vat-workflow-base` Section 3. This section provides the Albania-specific overlay.

### Sheet "Transactions"

Columns A-L per the base. Column H ("Box code") accepts only valid Albanian TVSH box codes from Section 1 of this skill. Use blank for excluded transactions.

### Sheet "Box Summary"

```
Output:
| 1  | Taxable supplies 20% base | =SUMIFS(Transactions!E:E, Transactions!H:H, "1") |
| 2  | Output TVSH 20% | =Box_Summary!C[1_row]*0.20 |
| 3  | Taxable supplies 6% base | =SUMIFS(Transactions!E:E, Transactions!H:H, "3") |
| 4  | Output TVSH 6% | =Box_Summary!C[3_row]*0.06 |
| 5  | Zero-rated supplies | =SUMIFS(Transactions!E:E, Transactions!H:H, "5") |
| 6  | Exempt supplies | =SUMIFS(Transactions!E:E, Transactions!H:H, "6") |
| 7  | Reverse charge base | =SUMIFS(Transactions!E:E, Transactions!H:H, "7") |
| 8  | Output TVSH reverse charge | =Box_Summary!C[7_row]*0.20 |
| 9  | Total output TVSH | =C[2_row]+C[4_row]+C[8_row] |

Input:
| 10 | Domestic purchases base | =SUMIFS(Transactions!E:E, Transactions!H:H, "10") |
| 11 | Input TVSH domestic | =Box_Summary!C[10_row]*0.20 |
| 12 | Imports base | =SUMIFS(Transactions!E:E, Transactions!H:H, "12") |
| 13 | TVSH on imports | =SUMIFS(Transactions!F:F, Transactions!H:H, "12") |
| 14 | Fixed assets base | =SUMIFS(Transactions!E:E, Transactions!H:H, "14") |
| 15 | Input TVSH fixed assets | =Box_Summary!C[14_row]*0.20 |
| 16 | Input TVSH reverse charge | =Box_Summary!C[7_row]*0.20 |
| 17 | Adjustments | 0 |
| 18 | Total input TVSH | =SUM(C[11_row]:C[17_row]) |

Settlement:
| 19 | TVSH payable | =IF(C[9_row]>C[18_row], C[9_row]-C[18_row], 0) |
| 20 | TVSH credit | =IF(C[18_row]>C[9_row], C[18_row]-C[9_row], 0) |
| 21 | Credit from prior period | [manual entry] |
| 23 | Net payable | =MAX(C[19_row]-C[21_row], 0) |
```

### Sheet "Return Form"

Final TVSH-ready figures. Bottom-line cell is Box 23 (net payable) or Box 20 (credit).

---

## Section 8 — Albanian bank statement reading guide

**CSV format conventions.** BKT and Raiffeisen Albania exports typically use semicolon delimiters with DD.MM.YYYY dates. Common columns: Date, Description, Debit, Credit, Balance. Always confirm which account currency applies.

**Albanian language variants.** Some descriptions appear in Albanian: qira (rent), paga/rroga (salary), interesa/kamata (interest), terheqje (withdrawal), transferte (transfer), blerje (purchase), shitje (sale). Treat as the English equivalent.

**Internal transfers and exclusions.** Own-account transfers between the client's BKT, Raiffeisen, Credins accounts. Labelled "transferte brendshme", "own transfer", "internal". Always exclude.

**Refunds and reversals.** Identify by "rimbursim", "kthim", "reversal", "storno". Book as negative in the same box as the original transaction.

**Foreign currency transactions.** Convert to ALL at the Bank of Albania middle rate on the transaction date.

**IBAN prefix.** AL = Albania. Non-AL IBANs indicate foreign counterparty — check if reverse charge or export applies.

**Fiscalization codes.** If the bank description includes a NIVF reference, the transaction has a fiscalized invoice. If absent, flag for verification.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type and trading name
*Inference rule:* sole trader names match account holder; company names end in "SHPK", "SHA". *Fallback:* "Are you a sole trader or a company (SHPK/SHA)?"

### 9.2 TVSH registration status
*Inference rule:* if asking for a TVSH return, they are registered. *Fallback:* "Are you a registered TVSH payer?"

### 9.3 NUIS/NIPT
*Inference rule:* may appear in payment descriptions. *Fallback:* "What is your NUIS/NIPT?"

### 9.4 Filing period
*Inference rule:* transaction date range on statement (monthly). *Fallback:* "Which month does this cover?"

### 9.5 Industry and sector
*Inference rule:* counterparty mix, invoice descriptions. *Fallback:* "What does the business do?"

### 9.6 Employees
*Inference rule:* ISSH, salary outgoing transfers. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Inference rule:* medical/financial/educational income patterns. *Fallback:* "Do you make any TVSH-exempt sales?" *If yes and non-de-minimis, R-AL-4 fires.*

### 9.8 Credit brought forward
*Inference rule:* not inferable from single period. Always ask. *Question:* "Do you have TVSH credit from the previous month? (Box 21)"

### 9.9 Cross-border customers
*Inference rule:* foreign IBANs on incoming. *Fallback:* "Do you have customers outside Albania?"

### 9.10 Tourism certification
*Inference rule:* Airbnb/booking.com payouts, hotel income. *Fallback:* "Do you hold a tourism licence for 6% rate?"

---

## Section 10 — Reference material

### Sources

**Primary legislation:**
1. Law No. 92/2014 "On Value Added Tax in the Republic of Albania" (as amended) — Articles 3-6, 11, 25-30, 51-56, 68-73, 76, 82, 86, 105-107
2. Law No. 87/2019 on E-Invoicing and Fiscalization

**DPT guidance:**
3. DPT TVSH declaration form and completion notes — https://e-filing.tatime.gov.al
4. DPT guidance on reverse charge
5. DPT fiscalization instructions

**Other:**
6. Bank of Albania exchange rates — https://www.bankofalbania.org

### Known gaps

1. Supplier pattern library covers common Albanian and international counterparties but not every local SME.
2. Tourism reduced rate (6%) categories are subject to frequent legislative changes — verify current applicability.
3. Agricultural inputs reduced rate (10%) scope requires ongoing verification.
4. Free economic zone rules require case-by-case analysis.
5. Red flag thresholds are conservative starting values, not empirically calibrated.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 10-section structure. Supplier pattern library added. Worked examples added. Tier 1 rules compressed. Tier 2 catalogue restructured. Excel template specification added. Bank statement reading guide added. Onboarding moved to fallback.
- **v1.1 (April 2026):** Initial skill with step-based structure.

### Self-check (v2.0)

1. Quick reference at top with box table and conservative defaults: yes.
2. Supplier library as literal lookup tables: yes (13 sub-tables).
3. Worked examples: yes (6 examples).
4. Tier 1 rules compressed: yes (11 rules).
5. Tier 2 catalogue compressed: yes (13 items).
6. Excel template specification: yes.
7. Onboarding as fallback: yes (10 items).
8. All 6 Albania-specific refusals present: yes.
9. Reference material at bottom: yes.
10. Entertainment hard-block explicit: yes.
11. Motor vehicle hard-block explicit: yes.
12. Fiscalization requirement explicit: yes.
13. Reverse charge (non-resident services) explicit: yes.
14. No inline tags: yes.

## End of Albania VAT (TVSH) Skill v2.0

This skill is incomplete without the companion file loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture).


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
