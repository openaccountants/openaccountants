---
name: india-gst
description: Use this skill whenever asked to prepare, review, classify, or advise on India's Goods and Services Tax (GST) for a self-employed individual, freelancer, or small business. Trigger on phrases like "GST return", "GSTR-1", "GSTR-3B", "GSTR-9", "file GST", "GST classification", "HSN code", "SAC code", "input tax credit", "ITC", "reverse charge", "e-invoicing", "e-way bill", "CGST", "SGST", "IGST", "inter-state supply", "intra-state supply", "place of supply", or any request involving Indian indirect tax compliance. This skill covers regular (non-composition) GST-registered taxpayers with a single state GSTIN only. Composition scheme, multi-state, SEZ, e-commerce operator, and ISD registrations are in the refusal catalogue. ALWAYS read this skill before touching any India GST work.
version: 2.0
---

# India GST Return Skill (GSTR-3B / GSTR-1) v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | India (Republic of India) |
| Tax structure | Dual GST: CGST + SGST/UTGST (intra-state) or IGST (inter-state) |
| Standard rate | 18% (CGST 9% + SGST 9% / IGST 18%) |
| Lower rate | 5% (CGST 2.5% + SGST 2.5% / IGST 5%) |
| Demerit rate | 40% (CGST 20% + SGST 20% / IGST 40%) -- luxury/sin goods only |
| Nil/exempt | 0% -- fresh food, healthcare, education |
| Zero-rated | 0% -- exports, SEZ supplies (with ITC refund) |
| Key rule | IGST rate = CGST rate + SGST rate, always |
| Primary return forms | GSTR-3B (summary + tax payment); GSTR-1 (outward supply details) |
| Filing portal | https://gst.gov.in (GST Common Portal) |
| Authority | Central Board of Indirect Taxes and Customs (CBIC) |
| Currency | INR only |
| Filing frequencies | Monthly (turnover > INR 5 crore); Quarterly under QRMP (turnover <= INR 5 crore) |
| GSTR-3B deadline | 20th of following month (monthly); 22nd-24th of month after quarter (quarterly, by state) |
| GSTR-1 deadline | 11th of following month (monthly); 13th of month after quarter (quarterly) |
| Registration threshold (goods, general) | INR 40 lakh aggregate turnover |
| Registration threshold (goods, special states) | INR 20 lakh |
| Registration threshold (services, all) | INR 20 lakh (INR 10 lakh special states) |
| E-invoicing threshold | INR 5 crore aggregate turnover (any FY from 2017-18) |
| E-way bill threshold | INR 50,000 consignment value |
| GSTIN format | 15-digit: 2 state code + 10 PAN + entity code + Z + checksum |
| Contributor | Open Accounting Skills Project |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key GSTR-3B tables (the tables you will use most):**

| Table | Meaning |
|---|---|
| 3.1(a) | Outward taxable supplies (other than zero-rated, nil-rated, exempted) -- all taxable sales + tax collected |
| 3.1(b) | Outward taxable supplies (zero-rated) -- exports + SEZ supplies |
| 3.1(c) | Other outward supplies (nil-rated, exempted) |
| 3.1(d) | Inward supplies (liable to reverse charge) -- RCM purchases |
| 3.1(e) | Non-GST outward supplies -- petroleum, alcohol, etc. |
| 3.2 | Inter-state supplies to unregistered persons, composition taxpayers, UIN holders |
| 4(A) | ITC Available -- imports, RCM, ISD, other ITC |
| 4(B) | ITC Reversed -- Rule 42/43 reversals, others |
| 4(C) | Net ITC Available -- 4(A) minus 4(B) |
| 4(D) | Ineligible ITC -- as per Sec 17(5) |
| 5.1 | Interest and late fee payable |
| 6.1 | Tax payment -- IGST, CGST, SGST -- cash + ITC utilization |

**Key GSTR-1 tables:**

| Table | Meaning |
|---|---|
| 4A/4B/6B/6C | B2B supplies (invoices, debit notes, credit notes) |
| 5A/5B | B2C inter-state (invoice value > INR 2.5 lakh) |
| 7 | B2C other (intra-state and inter-state below INR 2.5 lakh, rate-wise) |
| 6A | Exports (with payment / without payment of tax) |
| 8A/8B/8C/8D | Nil-rated, exempted, and non-GST supplies |
| 9B | Credit notes / debit notes (unregistered) |
| 11A/11B | Amendments to prior period B2B / export invoices |
| 12 | HSN-wise summary of outward supplies |

**Conservative defaults -- India-specific:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 18% |
| Unknown VAT status of a purchase | Not deductible (no ITC) |
| Unknown counterparty state | Same state as client (intra-state, CGST+SGST) |
| Unknown B2B vs B2C status for buyer | B2C (no GSTIN, no ITC for buyer) |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-resident (IGST) |
| Unknown blocked-input status (entertainment, personal use) | Blocked under Sec 17(5) |
| Unknown whether transaction is in scope | In scope |
| Unknown inter-state vs intra-state | Intra-state (CGST+SGST) |

**Red flag thresholds -- country slot values for reviewer brief:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | INR 5,00,000 |
| HIGH tax-delta on a single conservative default | INR 25,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net GST position | INR 10,00,000 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the month/quarter in CSV, PDF, Excel, or pasted text. Must cover the full filing period. Acceptable from any Indian bank: SBI, HDFC, ICICI, Axis, Kotak, PNB, Bank of Baroda, IndusInd, Yes Bank, IDFC First, or any other scheduled bank. Also acceptable: Razorpay, Paytm, or other payment processor settlement reports.

**Recommended** -- purchase and sales invoices for the period (especially for inter-state B2B, exports, and reverse charge), prior period GSTR-3B and GSTR-1 filed copies, GSTR-2B (auto-drafted ITC statement) from the GST portal, Form 26AS / AIS (for cross-verification of TDS and high-value transactions).

**Ideal** -- Tally ERP / Zoho Books / ClearTax / Busy Accounting export (trial balance + GST-ready transaction register), complete invoice register with HSN/SAC codes, GSTR-9 from prior year, e-invoicing JSON exports if applicable.

**Refusal policy if minimum is missing -- SOFT WARN.** If no bank statement or transaction data is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This GSTR-3B was produced from bank statement alone. The reviewer must verify, before approval, that ITC claims are supported by tax invoices appearing in GSTR-2B, that all inter-state vs intra-state classifications are correct, and that reverse-charge self-assessments match the supplier's invoice."

### India-specific refusal catalogue

If any trigger fires, stop, output the refusal message verbatim, end the conversation. Refusal is a safety mechanism.

**R-IN-1 -- Composition scheme taxpayer.** *Trigger:* client is registered under composition scheme (Sec 10), or mentions CMP-08, GSTR-4, or turnover below INR 1.5 crore with simplified filing. *Message:* "Composition scheme taxpayers file GSTR-4 (annual) and CMP-08 (quarterly challan), not GSTR-3B/GSTR-1. They cannot claim ITC, cannot make inter-state supplies, and pay tax at flat rates (1% for traders/manufacturers, 5% for restaurants, 6% for service providers). This skill covers regular taxpayers only. Please use a qualified GST practitioner for composition scheme returns."

**R-IN-2 -- Multi-state registration.** *Trigger:* client has GSTINs in more than one state and asks to consolidate or cross-credit. *Message:* "Each state GSTIN is a separate taxpayer under GST law. Cross-state ITC utilization is not permitted. This skill handles a single GSTIN filing only. If you need to file for multiple GSTINs, process each separately. For ISD (Input Service Distributor) cross-charge scenarios, please use a qualified CA/GST practitioner."

**R-IN-3 -- SEZ supplies (as supplier to SEZ).** *Trigger:* client makes supplies to SEZ units or developers and asks about zero-rating, LUT filing, or refund of accumulated ITC specific to SEZ. *Message:* "SEZ supply documentation (endorsed invoices, SEZ authority endorsement, LUT/bond filing) requires fact-specific verification beyond this skill. Please use a qualified GST practitioner for SEZ supply compliance."

**R-IN-4 -- E-commerce operator (TCS obligations).** *Trigger:* client operates an e-commerce platform and must collect TCS under Sec 52, or is a supplier through e-commerce with specific compliance obligations. *Message:* "E-commerce operators have TCS collection, GSTR-8 filing, and platform-level compliance obligations that are outside the scope of this skill. Please use a qualified GST practitioner."

**R-IN-5 -- Input Service Distributor (ISD).** *Trigger:* client is registered as an ISD or needs to distribute common input services across multiple GSTINs. *Message:* "ISD distribution requires proportional credit allocation across GSTINs under CGST Rules. This skill covers single-GSTIN regular taxpayers only. Please use a qualified CA/GST practitioner for ISD compliance."

---

## Section 3 -- Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. Do not consult Tier 1 rules -- the table is authoritative for patterns it covers.

**How to read this table.** Match by case-insensitive substring on the counterparty name/description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Indian banks (fees exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SBI, STATE BANK OF INDIA | EXCLUDE for bank charges/fees | Financial service, exempt under Notification 12/2017-CT(Rate) |
| HDFC BANK, HDFC BK | EXCLUDE for bank charges/fees | Same |
| ICICI BANK, ICICI BK | EXCLUDE for bank charges/fees | Same |
| AXIS BANK | EXCLUDE for bank charges/fees | Same |
| KOTAK MAHINDRA, KOTAK BK | EXCLUDE for bank charges/fees | Same |
| PNB, PUNJAB NATIONAL BANK | EXCLUDE for bank charges/fees | Same |
| BOB, BANK OF BARODA | EXCLUDE for bank charges/fees | Same |
| INDUSIND, YES BANK, IDFC FIRST | EXCLUDE for bank charges/fees | Same |
| INTEREST, BYAJ, INT PAID, INT RECD | EXCLUDE | Interest income/expense, exempt financial service |
| LOAN, EMI, PERSONAL LOAN, HOME LOAN | EXCLUDE | Loan principal/EMI movement, not a supply |
| FD, FIXED DEPOSIT, RD | EXCLUDE | Investment movement, not a supply |

### 3.2 Government (exclude entirely -- not a supply)

| Pattern | Treatment | Notes |
|---|---|---|
| GST PMT, GST PAYMENT, GST CHALLAN, GSTN | EXCLUDE | Tax payment to government |
| INCOME TAX, IT DEPT, TDS, ADVANCE TAX, CPC BANGALORE | EXCLUDE | Direct tax payment |
| MCA, ROC FEE, COMPANY AFFAIRS | EXCLUDE | Regulatory fee |
| EPFO, PF, ESI, ESIC, PROVIDENT FUND | EXCLUDE | Statutory social security contribution |
| PROFESSIONAL TAX, PT PAYMENT | EXCLUDE | State professional tax |
| STAMP DUTY, REGISTRATION FEE (govt) | EXCLUDE | Government fee, not a supply |
| MUNICIPAL, NAGAR NIGAM, PROPERTY TAX | EXCLUDE | Local body tax |

### 3.3 Telecom and utilities (18%)

| Pattern | Treatment | GSTR-3B Table | Notes |
|---|---|---|---|
| JIO, RELIANCE JIO | 18% input, CGST+SGST or IGST | 4(A) | Telecom service |
| AIRTEL, BHARTI AIRTEL | 18% input | 4(A) | Telecom service |
| VI, VODAFONE IDEA | 18% input | 4(A) | Telecom service |
| BSNL, MTNL | 18% input | 4(A) | Government telecom, still taxable |
| TATA POWER, ADANI ELECTRICITY, BSES, BESCOM, MSEDCL | 18% input | 4(A) | Electricity distribution (post-GST 2.0: electricity brought under GST at 18% for commercial/industrial consumers) |
| MAHANAGAR GAS, IGL, ADANI GAS | 5% input | 4(A) | Piped natural gas for domestic/CNG at 5% |
| WATER SUPPLY, JALABOARD | EXCLUDE | | Municipal water, exempt |

### 3.4 Insurance

| Pattern | Treatment | Notes |
|---|---|---|
| LIC, LIFE INSURANCE CORP | EXCLUDE | Life insurance premium -- exempt (pure life, term). Endowment/ULIP policies may have GST but ITC blocked under Sec 17(5)(d) |
| HDFC ERGO, ICICI LOMBARD, BAJAJ ALLIANZ | 18% -- but check Sec 17(5)(d) | General insurance at 18%. ITC blocked unless: (i) government-mandated employee coverage, or (ii) used for making taxable supply of same category |
| STAR HEALTH, NIVA BUPA, CARE HEALTH | 18% -- but check Sec 17(5)(d) | Health insurance at 18%. ITC blocked unless government-mandated employee coverage |
| NEW INDIA ASSURANCE, UNITED INDIA | 18% -- but check Sec 17(5)(d) | Same treatment as HDFC Ergo |

### 3.5 SaaS and cloud -- Indian entities (18%)

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| AWS INDIA, AMAZON INTERNET SERVICES | Amazon Internet Services Pvt Ltd (IN) | 18% IGST (if inter-state) or CGST+SGST (if same state) | Check supplier GSTIN state code vs client state |
| GOOGLE INDIA, GOOGLE CLOUD INDIA | Google India Pvt Ltd / Google Cloud India Pvt Ltd (IN) | 18% | Check invoice for GSTIN |
| ZOHO, ZOHO CORP | Zoho Corporation Pvt Ltd (IN, Chennai) | 18% IGST or CGST+SGST | Check state code |
| FRESHWORKS | Freshworks Technologies Pvt Ltd (IN, Chennai) | 18% | Same treatment |
| MICROSOFT INDIA | Microsoft Corporation India Pvt Ltd (IN) | 18% | Check invoice for Indian GSTIN |
| CLEARTAX, CLEAR | Clear (formerly ClearTax) (IN) | 18% | Accounting/compliance SaaS |

### 3.6 Non-resident SaaS (reverse charge under IGST Act Sec 5(3))

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| NOTION, NOTION LABS | Notion Labs Inc (US) | RCM -- self-assess IGST 18% via cash ledger | Report in GSTR-3B Table 3.1(d). ITC claimable in 4(A)(3) |
| OPENAI, CHATGPT | OpenAI Inc (US) | RCM -- IGST 18% | Same |
| GITHUB (US entity) | GitHub Inc (US) | RCM -- IGST 18% | Check if billed by Indian or US entity |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | RCM -- IGST 18% | Same |
| FIGMA | Figma Inc (US) | RCM -- IGST 18% | Same |
| CANVA | Canva Pty Ltd (AU) | RCM -- IGST 18% | Non-resident, reverse charge |
| SLACK (US) | Slack Technologies LLC (US) | RCM -- IGST 18% | If billed by US entity. Salesforce Ireland = check |
| HUBSPOT (US) | HubSpot Inc (US) | RCM -- IGST 18% | Check billing entity |
| TWILIO | Twilio Inc (US) | RCM -- IGST 18% | Same |

### 3.7 Payment processors (18%)

| Pattern | Treatment | Notes |
|---|---|---|
| RAZORPAY | 18% input (IGST or CGST+SGST) | Payment gateway fees -- check GSTIN state code |
| PAYTM, ONE97 COMMUNICATIONS | 18% input | Same |
| STRIPE INDIA, STRIPE PAYMENTS INDIA | 18% input | Indian entity -- check invoice |
| STRIPE (US/IE entity) | RCM -- IGST 18% | Non-resident -- reverse charge if no Indian GSTIN |
| CASHFREE, INSTAMOJO, PHONEPE BUSINESS | 18% input | Payment processing service |
| PAYPAL (transaction fees from foreign entity) | RCM -- IGST 18% | PayPal Pte Ltd (SG) -- non-resident reverse charge |
| CCAVENUE, BILLDESK | 18% input | Indian payment processors |

### 3.8 Travel (5% / 18%)

| Pattern | Treatment | Notes |
|---|---|---|
| INDIGO, INTERGLOBE AVIATION | 5% (economy class) | Domestic air travel economy = 5%. Business class = 18%. Check ticket class |
| AIR INDIA | 5% (economy) / 18% (business) | Same split. International flights = zero-rated |
| SPICEJET, AKASA AIR, AIR ASIA INDIA | 5% (economy) / 18% (business) | Same treatment |
| VISTARA, TATA SIA | 5% (economy) / 18% (business) | Same |
| OLA, ANI TECHNOLOGIES | 5% | Ride-hailing at 5% (non-AC auto/e-rickshaw may be exempt) |
| UBER INDIA | 5% | Same as Ola |
| IRCTC, INDIAN RAILWAYS | 5% | Rail transport of passengers. Sleeper/AC chair at 5%. Local suburban exempt |
| MAKEMYTRIP, GOIBIBO, YATRA | 18% on service fee; underlying transport at transport rate | Platform commission at 18%. Underlying ticket at 5%/18% per class |
| HOTELS, OYO, TAJ, ITC HOTELS, LEMON TREE | 18% (tariff > INR 7,500/night) or 5% (tariff <= INR 7,500, without ITC option) | Check declared tariff |

### 3.9 Restaurants (5% no ITC vs 18%)

| Pattern | Treatment | Notes |
|---|---|---|
| SWIGGY | 5% (collected by platform) | Restaurant service via e-commerce -- 5% with no ITC. Platform is liable to collect and remit GST |
| ZOMATO | 5% (collected by platform) | Same as Swiggy |
| Restaurant (direct, non-hotel, non-AC) | 5% output (no ITC) | Restaurant choosing 5% rate foregoes ITC |
| Restaurant (in hotel, tariff > INR 7,500) | 18% (with ITC) | Hotel restaurant where declared room tariff > INR 7,500 |
| DOMINOS, PIZZA HUT, MCDONALDS, KFC, BURGER KING | 5% (dine-in/takeaway) | QSR chains at 5% without ITC |
| CLOUD KITCHEN, REBEL FOODS | 5% via platform | Same treatment as Swiggy/Zomato delivery |

### 3.10 Professional services (18%)

| Pattern | Treatment | Notes |
|---|---|---|
| CA, CHARTERED ACCOUNTANT, [name] & ASSOCIATES | 18% input (CGST+SGST or IGST) | Professional services. ITC available if used for taxable outward supply |
| CS, COMPANY SECRETARY | 18% input | Same |
| ADVOCATE, ADV, LAWYER, LAW FIRM | 18% -- RCM applies | Legal services by individual advocate/firm = reverse charge. Recipient pays GST |
| CONSULTANT, CONSULTANCY | 18% input | Check if RCM applies (non-resident consultant = RCM) |
| ARCHITECT, INTERIOR DESIGNER | 18% input | Forward charge from registered supplier |

### 3.11 Rent

| Pattern | Treatment | Notes |
|---|---|---|
| RENT (commercial property) | 18% input (CGST+SGST or IGST) | Commercial property rent at 18%. ITC available |
| RENT (residential, to registered person for business) | 18% RCM | From 18 Jul 2022, residential property rented to registered person = RCM on tenant. Tenant self-assesses 18% |
| RENT (residential, to unregistered person) | EXCLUDE | Exempt. Not a taxable supply when tenant is unregistered |
| COWORKING, WEWORK, AWFIS, COWRKS, 91SPRINGBOARD | 18% input | Commercial workspace service at 18% |

### 3.12 Salaries and wages (exclude entirely -- not a supply)

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES, STIPEND, PAYROLL | EXCLUDE | Employer-employee relationship. Schedule III -- not a supply |
| BONUS, GRATUITY, LEAVE ENCASHMENT | EXCLUDE | Same |
| CONTRACTOR (individual, no GSTIN) | EXCLUDE from GST; flag for TDS | Not a GST supply if unregistered. May need 194C TDS |

---

## Section 4 -- Worked examples

These are six fully worked classifications drawn from a hypothetical HDFC Bank statement of a Mumbai-based self-employed software consultant (GSTIN: 27XXXXX1234X1Z5, Maharashtra). They illustrate the trickiest cases. Pattern-match against these when you encounter similar lines in any real statement.

### Example 1 -- Non-resident SaaS reverse charge (Notion)

**Input line:**
`05.01.2026 ; NOTION LABS INC DEBIT CARD ; DR ; USD 10.00 ; INR 840.00`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.6). No GST on the charge. This is an import of services -- the client must self-assess IGST at 18% under reverse charge (IGST Act Sec 5(3)). RCM liability paid via electronic cash ledger only. ITC claimable in the same period if conditions under Sec 16 are met. Net effect = zero (cash-neutral for fully taxable person).

**Output:**

| Date | Counterparty | Gross (INR) | Net | GST self-assessed | Rate | GSTR-3B Table (output) | GSTR-3B Table (input) | Default? | Question? |
|---|---|---|---|---|---|---|---|---|---|
| 05.01.2026 | NOTION LABS INC | -840 | -840 | IGST 151 | 18% | 3.1(d) | 4(A)(3) | N | -- |

### Example 2 -- Indian SaaS, inter-state (AWS India)

**Input line:**
`10.01.2026 ; AMAZON INTERNET SERVICES PVT LTD NEFT ; DR ; INR 23,600.00`

**Reasoning:**
Amazon Internet Services Pvt Ltd is registered in Telangana (GSTIN: 36XXXXXX). Client is in Maharashtra (27). Different states = inter-state = IGST at 18%. Invoice amount INR 23,600 is gross (INR 20,000 net + INR 3,600 IGST). ITC of INR 3,600 IGST claimable if reflected in GSTR-2B.

**Output:**

| Date | Counterparty | Gross (INR) | Net | GST paid | Rate | GSTR-3B Table | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 10.01.2026 | AMAZON INTERNET SERVICES | -23,600 | -20,000 | IGST 3,600 | 18% | 4(A)(5) | N | -- |

### Example 3 -- Domestic restaurant, blocked ITC (Swiggy)

**Input line:**
`15.01.2026 ; BUNDL TECHNOLOGIES SWIGGY ; DR ; INR 450.00`

**Reasoning:**
Swiggy (Bundl Technologies) is a restaurant aggregator platform. Restaurant food at 5% -- but ITC on food and beverages is blocked under Sec 17(5)(b). The 5% GST is collected and remitted by the e-commerce platform. For the recipient (our client), no ITC is available regardless of business purpose. Exclude from ITC claim. The expense may still be deductible for income tax purposes if business-related.

**Output:**

| Date | Counterparty | Gross (INR) | Net | GST | Rate | ITC? | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 15.01.2026 | SWIGGY | -450 | -429 | 21 (5%) | 5% | BLOCKED -- Sec 17(5)(b) | Y | "Was this a business meal or personal?" |

### Example 4 -- Legal services under reverse charge (Advocate)

**Input line:**
`20.01.2026 ; ADV RAJESH SHARMA NEFT ; DR ; INR 50,000.00`

**Reasoning:**
Payment to an advocate for legal services. Under Notification 13/2017-CT(Rate) Sl. No. 2, legal services by an individual advocate or firm of advocates to any business entity attract reverse charge. The client (business entity) must self-assess GST at 18%. Since both advocate and client are in Maharashtra, this is intra-state: CGST 9% + SGST 9% on INR 50,000 = INR 9,000 total. Paid via cash ledger. ITC of INR 9,000 claimable if the legal service was for business purposes.

**Output:**

| Date | Counterparty | Gross (INR) | Net | GST self-assessed | Rate | GSTR-3B Table (output) | GSTR-3B Table (input) | Default? | Question? |
|---|---|---|---|---|---|---|---|---|---|
| 20.01.2026 | ADV RAJESH SHARMA | -50,000 | -50,000 | CGST 4,500 + SGST 4,500 | 18% | 3.1(d) | 4(A)(3) | Y | "Confirm advocate is in same state (intra-state) and not an employee" |

### Example 5 -- Domestic air travel, economy class

**Input line:**
`22.01.2026 ; INTERGLOBE AVIATION INDIGO 6E-1234 ; DR ; INR 5,250.00`

**Reasoning:**
IndiGo domestic flight. Economy class domestic air travel attracts 5% GST (CGST 2.5% + SGST 2.5% or IGST 5%). Net = INR 5,000, GST = INR 250. ITC of INR 250 is available if the travel was for business purposes and not blocked under Sec 17(5)(e) (travel benefits to employees on vacation are blocked, but business travel by the proprietor is not LTC). Check: business class would be 18%.

**Output:**

| Date | Counterparty | Gross (INR) | Net | GST | Rate | GSTR-3B Table | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 22.01.2026 | INTERGLOBE AVIATION | -5,250 | -5,000 | 250 | 5% | 4(A)(5) | Y | "Economy or business class? Business purpose?" |

### Example 6 -- Motor vehicle (personal car), hard block

**Input line:**
`28.01.2026 ; MARUTI SUZUKI INDIA LTD NEFT ; DR ; INR 8,50,000.00`

**Reasoning:**
Car purchase payment. ITC on motor vehicles is hard-blocked under Sec 17(5)(a) unless the vehicle is used for: (i) further supply of vehicles, (ii) transportation of passengers, (iii) driving training, or (iv) transportation of goods. A software consultant does not qualify for any exception. Full ITC block regardless of business use. The GST paid (18% or 40% depending on vehicle type) is a cost to the business. Do not claim any ITC.

**Output:**

| Date | Counterparty | Gross (INR) | Net | GST | Rate | ITC? | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 28.01.2026 | MARUTI SUZUKI | -8,50,000 | -- | -- | 18%/40% | BLOCKED -- Sec 17(5)(a) | Y | "Motor vehicle: blocked. Is this for transport of goods/passengers as primary business?" |

---

## Section 5 -- Tier 1 classification rules (compressed)

Each rule states the legal source and the GSTR-3B table mapping. Apply silently if the data is unambiguous.

### 5.1 GST rate slabs (post-GST 2.0, effective 22 Sep 2025)

**Legislation:** CGST Act Sec 9; 56th GST Council; Notification 01/2017-CT(Rate) as amended.

Three active slabs plus nil/zero:
- **5%** (CGST 2.5% + SGST 2.5% / IGST 5%): packaged food, medicines, economy transport, insurance, EVs, restaurants (without ITC option), small hotels
- **18%** (CGST 9% + SGST 9% / IGST 18%): most goods and services -- IT, telecom, financial services, professional services, branded garments, consumer durables, cement, non-luxury automobiles, commercial rent
- **40%** (CGST 20% + SGST 20% / IGST 40%): demerit/luxury only -- aerated drinks, energy drinks, premium motor vehicles (SUVs >4m, >1500cc), online gaming/casinos/betting
- **0% (nil/exempt)**: fresh food (milk, cereals, vegetables, fruits), healthcare, education
- **0% (zero-rated)**: exports, SEZ supplies

Former 12% and 28% slabs abolished 22 Sep 2025. Items moved to 5% or 18% respectively.

### 5.2 CGST+SGST vs IGST determination

**Legislation:** CGST Act Sec 9; IGST Act Sec 5; IGST Act Chapter V (Place of Supply).

| Scenario | Tax type |
|---|---|
| Supplier state = Buyer state (intra-state) | CGST + SGST (half rate each) |
| Supplier state = Buyer UT (intra-UT) | CGST + UTGST |
| Supplier state != Buyer state (inter-state) | IGST (full rate) |
| Import of goods | IGST (via Customs) + BCD (no ITC on BCD) |
| Import of services | IGST under reverse charge |
| Export | Zero-rated (IGST or under LUT) |

**Key determination:** Compare first two digits of supplier GSTIN vs buyer GSTIN. If same state code = intra-state. If different = inter-state. If buyer has no GSTIN (B2C), use buyer's billing address to determine state.

### 5.3 Reverse charge on import of services

**Legislation:** IGST Act Sec 5(3); Sec 5(4).

ANY import of services where supplier is outside India and recipient is in India -- IGST must be self-assessed and paid by recipient under reverse charge. No threshold. Paid via electronic cash ledger only (ITC cannot be used to discharge RCM liability). ITC on the RCM payment is available in the same period if Sec 16 conditions are met. Net effect = zero for a fully taxable recipient.

Report: GSTR-3B Table 3.1(d) for output; Table 4(A)(3) for ITC.

### 5.4 Domestic reverse charge (specified services)

**Legislation:** CGST Act Sec 9(3); Notification 13/2017-CT(Rate).

Key RCM categories for freelancers/small businesses:
- Legal services by individual advocate/firm of advocates
- Services by director (not as employee) to company
- Services by Goods Transport Agency (GTA) -- if GTA has not opted for forward charge
- Sponsorship services to body corporate/partnership
- Services by government/local authority to business entity
- Security services from unincorporated supplier to registered person

Mechanics: self-assess at applicable rate, pay via cash ledger, report in 3.1(d), claim ITC in 4(A)(3).

### 5.5 E-invoicing (INR 5 crore threshold)

**Legislation:** CGST Rule 48(4); Notification 13/2020-CT and amendments.

If aggregate turnover in any FY from 2017-18 onwards exceeds INR 5 crore:
- Mandatory e-invoice for all B2B supplies
- Upload JSON to Invoice Registration Portal (IRP) at einvoice1.gst.gov.in
- Receive IRN (Invoice Reference Number) + QR code
- IRN + QR must appear on invoice
- E-invoice auto-populates GSTR-1 and e-way bill Part A
- 30-day reporting rule: taxpayers with AATO >= INR 10 crore must report within 30 days of invoice date (from 1 Apr 2025)
- MFA mandatory for all GST portal access from 1 Apr 2025

### 5.6 ITC conditions (all four must be met)

**Legislation:** CGST Act Sec 16(2).

1. Possession of tax invoice or debit note
2. Receipt of goods or services
3. Tax actually paid to government by supplier (reflected in GSTR-2B)
4. Recipient has filed GSTR-3B

**ITC cannot exceed amount in GSTR-2B.** If supplier has not uploaded invoice, recipient CANNOT claim ITC.

**Time limit:** Earlier of 30 Nov of year following the FY, or date of filing GSTR-9 for that FY.

**Non-payment reversal:** If recipient does not pay supplier within 180 days of invoice date, ITC must be reversed. Re-claim upon payment.

### 5.7 Blocked credits -- Sec 17(5) (absolute blocks)

| Category | Blocked? | Exception |
|---|---|---|
| Motor vehicles and conveyances | YES | Only if used for: further supply of vehicles, transport of passengers, driving training, transport of goods |
| Food, beverages, outdoor catering, beauty, health, cosmetic surgery | YES | Only if used for making outward taxable supply of same category, or as element of taxable composite/mixed supply |
| Club membership, health and fitness centre | YES | None |
| Rent-a-cab, life insurance, health insurance | YES | Government-mandated employee provision; or used for making taxable supply of same category |
| Travel benefits to employees on vacation (LTC/LTA) | YES | None |
| Works contract for immovable property (not plant & machinery) | YES | Input service for further supply of works contract |
| Construction of immovable property on own account (not plant & machinery) | YES | None |
| Personal consumption | YES | None |
| Goods lost, stolen, destroyed, written off, gifts, free samples | YES | None -- ITC must be reversed |

### 5.8 ITC utilization order

**Legislation:** CGST Act Sec 49(5); Circular 98/17/2019-GST.

```
IGST Credit --> First against IGST liability
            --> Then against CGST liability
            --> Then against SGST/UTGST liability

CGST Credit --> First against CGST liability
            --> Then against IGST liability
            --> CANNOT be used against SGST/UTGST

SGST Credit --> First against SGST liability
            --> Then against IGST liability
            --> CANNOT be used against CGST
```

IGST credit must be fully exhausted before CGST or SGST credit is used against IGST liability.

### 5.9 ITC reversal -- Rule 42/43

**Legislation:** CGST Rules, Rule 42 (inputs/input services), Rule 43 (capital goods).

When inputs are used partly for taxable and partly for exempt supplies:

```
ITC to reverse = (Exempt turnover / Total turnover) x Common Credit
```

Capital goods: 5-year useful life. Monthly reversal = Total ITC / 60 x (exempt / total turnover).

### 5.10 Filing deadlines and late fees

| Return | Deadline | Late fee (with tax liability) | Late fee (nil) |
|---|---|---|---|
| GSTR-3B (monthly) | 20th of following month | INR 50/day (max INR 10,000) | INR 20/day (max INR 500) |
| GSTR-1 (monthly) | 11th of following month | INR 50/day (max INR 10,000) | INR 50/day (max INR 10,000) |
| GSTR-9 | 31st December following FY | INR 200/day (max 0.5% of turnover) | Same |

Interest on late payment: 18% per annum on net cash liability. Excess ITC claimed and utilized: 24% per annum.

### 5.11 Exports -- two options

**Legislation:** IGST Act Sec 16(3); CGST Rules, Rule 96/96A.

| Option | Mechanism | Refund |
|---|---|---|
| Export with payment of IGST | Charge IGST on invoice | Automatic refund via shipping bill (Rule 96) |
| Export under LUT (without tax) | File Letter of Undertaking annually (RFD-11), invoice at 0% | Claim refund of accumulated ITC (Rule 89, RFD-01) |

Report in GSTR-3B Table 3.1(b). GSTR-1 Table 6A.

### 5.12 E-way bill

**Legislation:** CGST Rules, Rule 138.

Required for movement of goods where consignment value > INR 50,000. Validity: 1 day per 200 km. Generated on ewaybillgst.gov.in. Not applicable to services.

### 5.13 HSN/SAC on invoices

| Turnover | HSN digits required |
|---|---|
| Up to INR 5 crore | 4-digit HSN on B2B invoices |
| Above INR 5 crore | 6-digit HSN on all invoices |

HSN = goods (based on WCO classification). SAC = services (starts with 99xxxx).

### 5.14 Compensation cess -- abolished

Abolished for non-tobacco items from 22 Sep 2025. Abolished for tobacco/pan masala from 1 Feb 2026 (replaced by Health Security and National Security Cess on production capacity). Do NOT apply compensation cess to any invoice dated on or after these dates.

### 5.15 QRMP scheme

**Legislation:** CGST Rule 61A; Notification 84/2020-CT.

Eligible if aggregate turnover <= INR 5 crore in preceding FY. GSTR-1 and GSTR-3B filed quarterly. Tax paid monthly via PMT-06 by 25th of following month. Invoice Furnishing Facility (IFF) available for optional B2B invoice upload in months 1 and 2 of quarter (max INR 50 lakh/month).

---

## Section 6 -- Tier 2 catalogue (compressed)

For each ambiguity type: pattern, why the bank statement is insufficient, conservative default, question for the structured form.

### 6.1 Vehicle costs (petrol/diesel)

*Pattern:* HPCL, BPCL, IOCL, SHELL, petrol pump, fuel station, toll charges (FASTag/NHAI). *Why insufficient:* vehicle type and business-use proportion unknown. If vehicle is a car -> ITC on the car itself is blocked under Sec 17(5)(a), and fuel for a blocked vehicle is also typically blocked. If commercial vehicle (delivery van, truck) -> ITC available. *Default:* 0% recovery. *Question:* "Is this fuel for a car (ITC blocked) or a commercial vehicle used for business? What percentage is business use?"

### 6.2 Restaurants via platforms (Swiggy/Zomato)

*Pattern:* SWIGGY, ZOMATO, BUNDL TECHNOLOGIES, ZOMATO LTD, food delivery charges. *Why insufficient:* personal vs business meal unknown. GST at 5% is collected by the platform (e-commerce operator liable from 1 Jan 2022). ITC on food is blocked under Sec 17(5)(b) regardless. *Default:* no ITC claim. Expense may still be income tax deductible if business purpose established. *Question:* "Was this a business meal (e.g., client meeting) or personal? (Note: ITC is blocked either way -- this is for income tax records.)"

### 6.3 Home office (rent/utilities)

*Pattern:* rent payment, electricity bill, internet bill from residential address. *Why insufficient:* proportion of business use unknown. Residential rent to registered person triggers RCM at 18% from 18 Jul 2022 -- but the ITC on residential rent for personal use is blocked under Sec 17(5)(g). Mixed use requires apportionment but lacks clear methodology. *Default:* 0% ITC recovery on residential expenses. *Question:* "Do you work from home? What percentage of the property is used exclusively for business? Is the rent in your personal name or business name?"

### 6.4 Cash withdrawals

*Pattern:* ATM, CASH WDL, CASH WITHDRAWAL. *Why insufficient:* unknown what cash was spent on. Cash expenses need invoices for ITC. *Default:* exclude as owner drawing. *Question:* "What was the cash used for? Do you have invoices for any cash purchases?"

### 6.5 Mixed B2B/B2C sales (GSTIN determination)

*Pattern:* incoming payments from individuals or entities where GSTIN is unknown. *Why insufficient:* B2B (with GSTIN) requires per-invoice reporting in GSTR-1 Table 4A. B2C inter-state above INR 2.5 lakh requires Table 5A. B2C below threshold goes to Table 7 (rate-wise summary). Without knowing if buyer has GSTIN, cannot determine correct GSTR-1 table. *Default:* B2C (no GSTIN). *Question:* "For each sale: does the buyer have a GSTIN? If yes, what is it?"

### 6.6 Inter-state vs intra-state (counterparty location)

*Pattern:* payments to/from entities where state is unclear from bank statement description. *Why insufficient:* CGST+SGST vs IGST determination depends on comparing supplier and buyer state codes. Wrong determination = wrong tax heads = demand notice risk. *Default:* intra-state (same state as client) = CGST+SGST. *Question:* "Where is [counterparty] located? Same state as you, or a different state? If B2B, what is their GSTIN?"

### 6.7 Digital services from abroad (reverse charge -- is it really B2B?)

*Pattern:* foreign SaaS, cloud services, streaming subscriptions where business vs personal use is ambiguous. *Why insufficient:* RCM on import of services applies only when the service is received "in relation to business or commerce." Personal subscriptions (Netflix, Spotify personal) are not subject to RCM -- the foreign OIDAR supplier registers and pays under Simplified Registration (IGST Sec 14). *Default:* if the subscription appears on a business bank statement, treat as business use -> RCM applies. *Question:* "Is [service] used for business or personal purposes? If personal, it should not be on the business bank statement."

---

## Section 7 -- Excel working paper template (India-specific)

### Sheet "Transactions"

Columns:
- A: Date
- B: Counterparty / Description
- C: Debit/Credit indicator
- D: Gross amount (INR)
- E: Net amount (INR)
- F: GST amount (INR)
- G: GST rate (0%, 5%, 18%, 40%, RCM, Exempt, Excluded)
- H: Tax type (CGST+SGST / IGST / RCM-IGST / RCM-CGST+SGST / Nil / Excluded)
- I: GSTR-3B table reference (3.1(a), 3.1(b), 3.1(c), 3.1(d), 4(A), 4(D), Excluded)
- J: GSTR-1 table reference (4A, 5A, 7, 6A, 8A, Excluded)
- K: Default? (Y/N)
- L: Question / Notes

Use blank for excluded transactions in columns G-J.

### Sheet "GSTR-3B Summary"

One row per table. Column A = table number, Column B = description, Column C = taxable value, Column D = IGST, Column E = CGST, Column F = SGST.

```
| 3.1(a) | Outward taxable (other) | =SUMIFS(...) | ... |
| 3.1(b) | Outward taxable (zero-rated) | =SUMIFS(...) | ... |
| 3.1(c) | Other outward (nil/exempt) | =SUMIFS(...) | ... |
| 3.1(d) | Inward (reverse charge) | =SUMIFS(...) | ... |
| 4(A)   | ITC Available | =SUMIFS(...) | ... |
| 4(B)   | ITC Reversed | =SUMIFS(...) | ... |
| 4(C)   | Net ITC | =4(A)-4(B) | ... |
| 4(D)   | Ineligible ITC (Sec 17(5)) | =SUMIFS(...) | ... |
```

### Sheet "Tax Computation"

```
Output tax liability:
  IGST payable on outward supplies = [from 3.1(a) IGST column]
  CGST payable = [from 3.1(a) CGST column]
  SGST payable = [from 3.1(a) SGST column]
  Add: RCM liability (IGST/CGST/SGST) = [from 3.1(d)]

Less: ITC utilized (per utilization order in Section 5.8):
  IGST credit applied -> IGST -> CGST -> SGST
  CGST credit applied -> CGST -> IGST
  SGST credit applied -> SGST -> IGST

Net payable via cash = Output - ITC utilized
```

### Color and formatting conventions

Blue for hardcoded values from bank statement (columns A-D). Black for formulas. Green for cross-sheet references. Yellow background for any row where Default? = "Y". Red text for any blocked ITC row (Sec 17(5)).

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/india-gst-<period>-working-paper.xlsx
```

Check the JSON output. If `status` is `errors_found`, fix the formulas and re-run.

---

## Section 8 -- Indian bank statement reading guide

Follow the universal exclusion rules, plus these India-specific patterns.

### HDFC Bank statement format

Typical CSV columns: Date, Narration, Chq/Ref No, Value Dt, Withdrawal Amt, Deposit Amt, Closing Balance. Date format: DD/MM/YY or DD/MM/YYYY. Narration field contains the counterparty info -- often cryptic: "NEFT/RTGS/IMPS-[IFSC]-[Sender name]", "UPI-[UPI ID]-[Name]", "POS [Merchant]-[Terminal ID]", "ATM-SELF", "BIL/ONL/[Biller name]".

**HDFC narration parsing rules:**
- `NEFT-UTIB0000XXX-JOHN DOE` -> payment to/from John Doe via Axis Bank
- `UPI-rajesh@okhdfcbank-RAJESH KUMAR` -> UPI payment to/from Rajesh Kumar
- `POS 123456789012 AMAZON` -> card purchase at Amazon
- `BIL/ONL/AIRTEL` -> online bill payment to Airtel
- `INT.PD` -> interest paid (exclude)
- `CHG-GST` or `SERVICE CHARGES` -> bank charges (exclude, exempt)

### SBI statement format

Typical columns: Txn Date, Value Date, Description, Ref No/Cheque No, Debit, Credit, Balance. Description format: "INB/NEFT/[Ref]-[Name]", "ATM/SELF/[Branch]", "UPI/[ID]/[Name]", "SI-[Standing Instruction]".

### ICICI Bank statement format

Typical columns: S No, Value Date, Transaction Date, Cheque Number, Transaction Remarks, Withdrawal Amount (INR), Deposit Amount (INR), Balance (INR). Remarks format: "NEFT-[IFSC]-[Name]", "UPI/[Ref]/[Name]", "MMT/IMPS/[Ref]/[Name]", "POS/[Merchant]/[Location]".

### Common patterns across all Indian bank statements

**UPI payments:** Most common. Format varies but always contains "UPI" and a UPI ID or reference. The counterparty name is usually extractable. UPI to individuals without GSTIN -> likely personal or unregistered supplier -> Tier 2 question needed.

**NEFT/RTGS/IMPS:** Business payments. IFSC code in the narration can identify the counterparty bank branch. Large RTGS payments (> INR 2 lakh) are likely business transactions.

**Card transactions (POS/online):** Merchant name is embedded but often truncated. "AMAZON", "FLIPKART", "SWIGGY" are recognizable. "POS 4XXXXX" with no name -> ask client.

**Standing instructions (SI/ECS/NACH):** Recurring debits for EMI, insurance, subscriptions. Pattern: "ECS/NACH-[Mandate]-[Payee]". Common: LIC (insurance), HDFC HOME LOAN (EMI), SIP (mutual fund).

**Internal transfers and exclusions:**
- Own-account transfers between savings/current accounts: "TRF-OWN", "SELF TRANSFER", "FD CREATION"
- Mutual fund SIPs: "BSE-MF-[Fund name]" -> investment, exclude
- FD maturity/creation: "FD-[number]" -> exclude
- ATM self-withdrawal: "ATM-SELF", "ATM WDL" -> exclude as drawing

**Refunds and reversals:** "REVERSAL", "REFUND", "RETURN-NEFT". Book as negative in the same classification as the original transaction. Correct in the period booked, not by amending the original period.

**Salary credits (if client has employees):** "PAYROLL", "SALARY-[month]", outgoing to multiple individuals on same date. Exclude -- not a supply (Schedule III).

**Loan disbursement/repayment:** "LOAN DISB", "EMI-[Account]". Exclude -- not a supply.

**Foreign currency transactions:** Some banks show forex in narration: "FCY-USD-[amount]". Convert to INR at the transaction date rate shown on the statement. Note the rate in column L.

---

## Section 9 -- Onboarding fallback (only when inference fails)

The workflow mandates inferring the client profile from the data first and only confirming with the client when inference fails. The questionnaire below is a fallback.

### 9.1 Legal name and GSTIN

*Inference rule:* GSTIN sometimes appears in payment descriptions, especially in NEFT narrations. Extract and validate the 15-digit format (2 state code + 10 PAN + entity code + Z + checksum). *Fallback question:* "What is your GSTIN? (15-digit alphanumeric, e.g. 27AAPFU0939F1Z5)"

### 9.2 Registration type

*Inference rule:* if client is asking for GSTR-3B/GSTR-1, they are regular (non-composition). If they mention CMP-08 or GSTR-4 -> R-IN-1 refuses. *Fallback question:* "Are you a regular GST taxpayer or under the composition scheme?"

### 9.3 State of registration

*Inference rule:* first two digits of GSTIN. Also inferable from the bank branch location in IFSC codes. *Fallback question:* "Which state is your GST registration in?"

### 9.4 Filing period and frequency

*Inference rule:* first and last transaction dates on the bank statement. Monthly filers: single month. QRMP filers: full quarter. *Fallback question:* "Which period does this cover? Are you a monthly filer or quarterly (QRMP)?"

### 9.5 Business activity

*Inference rule:* counterparty mix, sales descriptions, HSN/SAC on invoices. IT/software, consulting, trading, manufacturing are recognizable from transaction patterns. *Fallback question:* "In one sentence, what does the business do?"

### 9.6 Inter-state supplies

*Inference rule:* if outward payments or receipts involve GSTINs from different states or IGST appears on invoices. *Fallback question:* "Do you make sales to buyers in other states? If so, which states?"

### 9.7 Exports

*Inference rule:* foreign currency receipts, forex conversion entries, "FIRC" or "EXPORT" in narration. *Fallback question:* "Do you export goods or services? If so, do you have a Letter of Undertaking (LUT) filed for this financial year?"

### 9.8 Reverse charge purchases

*Inference rule:* payments to advocates, GTA, foreign services, directors. *Fallback question:* "Do you receive any services from advocates, goods transport agencies, or foreign suppliers? Do you have non-employee directors?"

### 9.9 E-invoicing applicability

*Inference rule:* aggregate turnover from prior year GSTR-9 or from client's stated turnover. *Fallback question:* "Has your aggregate turnover exceeded INR 5 crore in any financial year since 2017-18?"

### 9.10 ITC brought forward

*Inference rule:* not inferable from a single period statement. Always ask. *Question:* "Do you have any ITC balance carried forward from the previous period? (IGST, CGST, SGST amounts separately)"

---

## Section 10 -- Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the Malta v2.0 three-tier architecture (Quick reference, Supplier pattern library, Worked examples, Tier 1/Tier 2 split). It supersedes v1.0 (standalone monolithic skill). The India-specific content (rate structure, GSTR-3B/GSTR-1 table mappings, blocked credits, reverse charge, e-invoicing, e-way bill) has been compiled from the CGST Act 2017, IGST Act 2017, CGST Rules 2017, and CBIC notifications/circulars. Post-GST 2.0 rate rationalization (56th GST Council, 22 Sep 2025) is reflected.

### Sources

**Primary legislation:**
1. Central Goods and Services Tax Act, 2017 (CGST Act) -- https://cbic-gst.gov.in
2. Integrated Goods and Services Tax Act, 2017 (IGST Act) -- https://cbic-gst.gov.in
3. CGST Rules, 2017 -- https://cbic-gst.gov.in
4. State Goods and Services Tax Acts (each state)
5. Goods and Services Tax (Compensation to States) Act, 2017 (abolished 2025/2026)

**Key notifications:**
6. Notification 01/2017-CT(Rate) -- GST rate schedule for goods (as amended by GST 2.0)
7. Notification 11/2017-CT(Rate) -- GST rate schedule for services (as amended)
8. Notification 12/2017-CT(Rate) -- Exempt services list
9. Notification 13/2017-CT(Rate) -- Reverse charge on specified services
10. Notification 13/2020-CT -- E-invoicing applicability
11. Notification 84/2020-CT -- QRMP scheme
12. Notification 02/2025 -- Compensation cess abolition (non-tobacco)

**Key circulars:**
13. Circular 98/17/2019-GST -- ITC utilization order
14. Circular 140/10/2020-GST -- Director services RCM clarification
15. Circular 164/20/2021-GST -- Restaurant composite/mixed supply

**Portals:**
16. GST Common Portal -- https://gst.gov.in
17. E-Invoice Portal -- https://einvoice1.gst.gov.in
18. E-Way Bill Portal -- https://ewaybillgst.gov.in

### Known gaps

1. The supplier pattern library covers common Indian vendors but does not cover every regional vendor or local supplier. Add patterns as they emerge.
2. Worked examples are drawn from a hypothetical Mumbai-based IT consultant. They do not cover manufacturing, trading, or hospitality specifically. A v2.1 should add sector-specific examples.
3. HSN/SAC classification requires looking up the master schedule -- this skill does not contain the full HSN/SAC master. Flag unknown classifications as [T2].
4. Place of supply for services is frequently disputed (IGST Act Sec 12/13). Complex scenarios involving multiple states or cross-border elements should be flagged [T2].
5. The GST 2.0 rate rationalization (56th GST Council, 22 Sep 2025) abolished the 12% and 28% slabs. Some transitional edge cases may exist for invoices straddling the effective date.
6. Health Security and National Security Cess (replacing compensation cess on tobacco/pan masala from 1 Feb 2026) is not detailed in this skill. Flag as [T3] if encountered.
7. The e-invoicing threshold (INR 5 crore) and 30-day reporting rule (INR 10 crore AATO) are as of April 2026. Verify for future periods.
8. ITC reversal calculations under Rule 42/43 require annual reconciliation in GSTR-9. This skill covers the monthly computation but not the annual true-up.

### PROHIBITIONS [T1]

- NEVER allow ITC on blocked credits under Sec 17(5) -- absolute blocks regardless of business use.
- NEVER apply intra-state rates (CGST+SGST) to inter-state supplies, or vice versa.
- NEVER let AI guess HSN/SAC codes -- classification must be verified against the HSN/SAC master.
- NEVER allow ITC claims that do not appear in GSTR-2B.
- NEVER discharge RCM liability using ITC -- must be paid via electronic cash ledger only.
- NEVER allow ITC beyond the time limit (30 Nov of following FY).
- NEVER classify a mixed supply as composite to achieve a lower rate.
- NEVER ignore the ITC utilization order (IGST must be exhausted first).
- NEVER allow e-invoicing-applicable businesses to issue invoices without IRN/QR code.
- NEVER assume export status without LUT filing or IGST payment proof.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 architecture. Quick reference with GSTR-3B/GSTR-1 table structure moved to top (Section 1). Supplier pattern library added with 12 sub-tables covering Indian banks, government, telecom, insurance, SaaS, non-resident SaaS, payment processors, travel, restaurants, professional services, rent, salaries (Section 3). Six worked examples from hypothetical HDFC Bank statement (Section 4). Tier 1 rules compressed with post-GST 2.0 rates (Section 5). Tier 2 catalogue with 7 ambiguity types (Section 6). Excel working paper template (Section 7). Indian bank statement reading guide covering HDFC, SBI, ICICI formats (Section 8). Onboarding moved to fallback with inference rules (Section 9). Five India-specific refusals: R-IN-1 (composition), R-IN-2 (multi-state), R-IN-3 (SEZ), R-IN-4 (e-commerce operator), R-IN-5 (ISD).
- **v1.0 (April 2026):** Initial skill. Standalone monolithic document covering CGST/IGST Acts, rate classification, return forms, ITC rules, blocked credits, reverse charge, e-invoicing, e-way bill, composition scheme, edge cases, and test suite. Compiled from deep research verification.

### Self-check (v2.0 of this document)

1. Quick reference at top with GSTR-3B table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 12 sub-tables).
3. Worked examples drawn from hypothetical HDFC Bank statement: yes (Section 4, 6 examples).
4. Tier 1 rules compressed with post-GST 2.0 rates (5%/18%/40%): yes (Section 5, 15 rules).
5. Tier 2 catalogue compressed with inference rules: yes (Section 6, 7 items).
6. Excel template specification with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only, inference rules first: yes (Section 9, 10 items).
8. All 5 India-specific refusals present: yes (Section 2, R-IN-1 through R-IN-5).
9. Reference material at bottom: yes (Section 10).
10. Blocked credits (Sec 17(5)) hard-block explicit: yes (Section 5.7 + Examples 3, 6).
11. Motor vehicle hard-block explicit: yes (Section 5.7 + Example 6).
12. RCM on import of services explicit: yes (Section 5.3 + Example 1).
13. RCM on domestic specified services (advocate) explicit: yes (Section 5.4 + Example 4).
14. CGST+SGST vs IGST determination explicit: yes (Section 5.2 + Example 2).
15. Restaurant/food ITC block explicit: yes (Section 5.7 + Example 3).

## End of India GST Return Skill v2.0


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
