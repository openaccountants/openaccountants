---
name: india-gst
description: Use this skill whenever asked to prepare, review, classify, or advise on India's Goods and Services Tax (GST) for a self-employed individual, freelancer, or small business. Trigger on phrases like "GST return", "GSTR-1", "GSTR-3B", "GSTR-9", "file GST", "GST classification", "HSN code", "SAC code", "input tax credit", "ITC", "reverse charge", "e-invoicing", "e-way bill", "CGST", "SGST", "IGST", "inter-state supply", "intra-state supply", "place of supply", or any request involving Indian indirect tax compliance. This skill covers regular (non-composition) GST-registered taxpayers with a single state GSTIN only. Composition scheme, multi-state, SEZ, e-commerce operator, and ISD registrations are in the refusal catalogue. ALWAYS read this skill before touching any India GST work.
version: 2.1
jurisdiction: IN
tax_year: 2026
last_updated: 2026-10-31
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India GST: Monthly and Quarterly Returns, Annual Return and Input Tax Credit for a Single-GSTIN Business

This Guide covers India's Goods and Services Tax (GST) for a regular (non-composition) registered business with one GSTIN in one State: classifying purchases and sales, preparing GSTR-1 and GSTR-3B, reconciling input tax credit (ITC) with GSTR-2B, and filing the annual return GSTR-9. Figures are for tax year 2026. GST is not year-based: this Guide states the rules in force on 17 October 2026, with the date each rule started. Returns run by tax period (a month, or a quarter under QRMP); the annual return runs by financial year (1 April to 31 March). The recommendations of the 57th GST Council meeting of 8 October 2026 are not law yet; see Section 5.16.

## Section 1: Quick reference

Read this whole section before classifying anything.

**Quick reference fields**

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Tax structure | Intra-State supply: central tax (CGST) plus State tax (SGST) or Union territory tax (UTGST). Inter-State supply and imports: integrated tax (IGST) |
| Rate structure | Two main rates (standard and merit) plus a special de-merit rate, from 22 September 2025; figures in the rate table below |
| Primary returns | GSTR-1 (details of outward supplies); GSTR-3B (summary return and payment); GSTR-9 (annual return) |
| ITC statement | GSTR-2B, an auto-generated monthly statement of the ITC available to the recipient |
| Law | Central Goods and Services Tax Act 2017 (CGST Act), Integrated Goods and Services Tax Act 2017 (IGST Act), CGST Rules 2017, each State's SGST Act |
| Authority | Central Board of Indirect Taxes and Customs (CBIC) and the State tax departments; returns are filed on the GST common portal |
| Currency | INR only |
| Filing frequency | Monthly, or quarterly under the QRMP scheme (Section 5.15) |
| Due dates and late fees | Section 5.10 |

### GST rates from 22 September 2025

The 56th GST Council meeting (3 September 2025) replaced the old four-slab structure with two main rates and a special de-merit rate ("Rationalisation of the current 4-tiered tax rate structure"). The old middle and top general slabs no longer exist; items moved to the rates in the table below. The legal rate schedule is Notification 9/2025-Central Tax (Rate), which the official repository serves only in a form this Guide could not read; the Council's release and FAQ below are the sources used. All rates in this table are the total GST on the supply (CGST plus SGST, or IGST), not the central share.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau_0.pdf |
| Standard rate | 18% | "a 2 rate structure with a Standard Rate of 18% and a Merit Rate of 5%" |
| Merit (lower) rate | 5% | "a 2 rate structure with a Standard Rate of 18% and a Merit Rate of 5%" |
| Special de-merit rate (a select few goods and services) | 40% | "a special de-merit rate of 40% for a select few goods and services" |
| Start date, services | 22 September 2025 | "The changes in GST rates on services will be implemented with effect from 22nd September 2025" |
| Start date, goods | 22 September 2025, except pan masala, gutkha, cigarettes, chewing tobacco, unmanufactured tobacco and bidi | "The changes in GST rates of all goods except pan masala, gutkha, cigarettes, chewing tobacco products like zarda, unmanufactured tobacco and bidi" |
| Individual life insurance (term, ULIP, endowment) and its reinsurance | Exempt from 22 September 2025 | "Exemption of GST on all individual life insurance policies whether term life, ULIP or endowment policies and reinsurance thereof" |
| Individual health insurance (including family floater and senior citizen policies) and its reinsurance | Exempt from 22 September 2025 | "Exemption of GST on all individual health insurance policies (including family floater policies and policies for senior citizens)" |
| Hotel accommodation: value per unit per day at or below | INR 7,500 | "services having value less than or equal to Rs. 7,500 per unit per day or equivalent" |
| Hotel accommodation at or below that value | 5% | "Reduction of GST from 12% to 5% on “Hotel Accommodation” services having value less than or equal to Rs. 7,500"; the Annexure row reads "12% with ITC 5% without ITC" |
| Gyms, salons, barbers, yoga centres and similar well-being services | 5% | "Reduction of GST from 18% to 5% on beauty and physical well-being services used by common man including services of gyms, salons, barbers, yoga centres" |
| Cement | 18% | "Reduction of GST from 28% to 18% on Cement" |
| Air transport of passengers in other than economy class | 18% | Annexure IV: "Supply of Air transport of 12% with ITC 18% with ITC passengers in other than economy class" |
| Passenger transport by any motor vehicle where the fuel cost is included | 5% with ITC of input services in the same line of business, or 18% with ITC | Annexure IV row: "Supply of Passenger transport by 5% with ITC of 5% with ITC of any motor vehicle where fuel input services (in input services (in" ... "12% with ITC 18% with ITC" |
| Transport of goods by a goods transport agency (GTA) | 5% without ITC (reverse or forward charge), or 18% with ITC | Annexure row: "Supply of Transport of 5% without 5% without ITC goods by GTA ITC (RCM/FCM) (RCM/FCM) 12% with ITC 18% with ITC" |
| Local delivery services through an e-commerce operator (section 9(5)), supplier not liable to register | 18% | "The applicable rate on such services to be 18%" |
| Stand-alone restaurants | Cannot declare themselves "specified premises", so cannot opt for 18% with ITC | "a stand-alone restaurant cannot declare itself as a ‘specified premises’ and consequently cannot avail the option of paying GST at the rate of 18% with ITC" |
| Optional simplified registration (rule 14A): output tax on supplies to registered persons per month not above | INR 2.5 lakh | "will not exceed Rs. 2.5 lakh per month (inclusive of CGST, SGST/UTGST and IGST)"; operational "from 1st November, 2025" |

Further items the same press release names. The earlier Guide `in-gst-return` listed them as slab examples without quotes; they were re-read on the press release on 31 October 2026. Pan masala moves on 1 February 2026 (start-date rows above); the rest on 22 September 2025.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau_0.pdf |
| Pan masala; waters containing added sugar or other sweetening matter or flavoured, including aerated waters (2202 10); caffeinated beverages (2202 99 90); carbonated beverages of fruit drink or with fruit juice (2202) | 40% (from 28%) | Annexure heading "(28% to 40%)": "*Pan masala"; "All goods [including aerated waters], containin[g added sugar] or other sweetening matter or flavoured"; "Caffeinated Beverages"; "Carbonated Beverages of Fruit Drink or Carbona[ted Beverages] with Fruit Juice" |
| Other non-alcoholic beverages (2202 91 00, 2202 99) | 40% (from 18%) | Annexure heading "(18% to 40%)": "Other non-alcoholic beverages" |
| Admission to casinos, race clubs, any place having casinos or race clubs, or sporting events like the IPL; services by a race club for licensing of bookmakers | 40% with ITC (from 28% with ITC) | "Admission to casinos, race clubs, any place having casinos or race clubs, or sporting events like the IPL. 28% With ITC 40% with ITC" |
| Specified actionable claims: betting, casinos, gambling, horse racing, lottery, online money gaming | 40% with ITC (from 28% with ITC) | "Specified Actionable Claims (betting, casinos, gambling, horse racing, lottery, online money gaming) defined as goods 28% With ITC 40% with ITC" |
| Leasing or rental services, without operator, of goods that themselves attract 40% | 40% with ITC (from 28% with ITC) | "Leasing or rental services, without operator, of goods which will attract (28%) 40% GST" |
| 33 lifesaving drugs and medicines | Nil (from 12%) | "Reduction of GST from 12% to NIL on 33 lifesaving drugs and medicines" |
| All other drugs and medicines | 5% (from 12%) | "Reduction of GST on all other drugs and medicines from 12% to 5%" |
| Handicrafts, marble and travertine blocks, granite blocks, intermediate leather goods | 5% (from 12%) | "Reduction of GST from 12% to 5% on labour intensive goods such as Handicrafts, Marble and travertine blocks, granite blocks, and Intermediate leather goods" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2025-09/faq_0.pdf |
| Air travel, economy class | 5% | "if travel is by economy class then rate of GST is 5% otherwise the GST rate will be 18%" |
| Air travel, any other class | 18% | "if travel is by economy class then rate of GST is 5% otherwise the GST rate will be 18%" |
| Small cars (petrol/LPG/CNG up to 1200 cc and up to 4000 mm; diesel up to 1500 cc and up to 4000 mm) | 18% | "The GST rate on all small cars has been reduced from 28% to 18%" |
| Mid-size and large cars (over 1500 cc or over 4000 mm) | 40% | "The GST rate on all mid-size and large cars i.e vehicles exceeding 1500 cc or length exceeding 4000mm is 40%" |
| Compensation cess on most goods | Ended; merged into the GST rate | "Since it has been decided to end the Compensation Cess levy, the Compensation Cess rate is being merged with GST" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2026-01/monthly_newsletter_december_2025_1_0.pdf |
| Start date for pan masala, tobacco, cigarettes and bidi | 1 February 2026 | "A revised rate structure has been notified with effect from February 1st, 2026, whereby bidi has been brought under the 18% GST rate" |
| Pan masala, tobacco (other than bidi), cigarettes, nicotine-based inhalation products | 40% | "cigarettes and nicotine-based inhalation products have been placed under the 40% GST rate" |
| Bidi | 18% | "bidi has been brought under the 18% GST rate" |
| Compensation cess on specified pan masala and tobacco products | Withdrawn | "the levy of compensation cess on specified pan masala and tobacco products has been withdrawn" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/download_5.pdf |
| Electrical energy (tariff heading 2716 00 00) | Exempt in the 2017 text of Notification 2/2017-Central Tax (Rate), serial 104 | "104. 2716 00 00 Electrical energy" (2017 print; the current Nil-rate list for goods is Notification 10/2025-Central Tax (Rate), not read) |

The GST Council's 57th meeting FAQ refers to "notification No. 10/2025-Central Tax (Rate), dated 17.09.2025, which prescribes Nil rate of GST" (https://gstcouncil.gov.in/sites/default/files/2026-10/faqs_on_recommendations_made_in_57th_gst_council_meeting.pdf). Confirm the electrical energy entry there.

Rates for items not in these tables (telecom, software, professional services, rail travel, restaurants, hotels above the hotel value in the table above) are not printed on any page this Guide could read. For a purchase, take the tax the supplier charged on its tax invoice. For a sale, find the item's rate in the rate notification before invoicing; do not guess (Section 10, PROHIBITIONS).

**Key GSTR-3B tables**

The ITC rows follow the GSTR-2B instructions in Notification 12/2024-Central Tax (https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf). Rows 3.1(a) to 3.1(c), 3.1(e), 3.2, 5.1 and 6.1 are legacy reference text kept from the earlier Guide; check them against the form on the portal.

| Table | Meaning |
| --- | --- |
| 3.1(a) | Outward taxable supplies (other than zero-rated, nil-rated, exempted) |
| 3.1(b) | Outward taxable supplies (zero-rated): exports and supplies to SEZ units or developers |
| 3.1(c) | Other outward supplies (nil-rated, exempted) |
| 3.1(d) | Inward supplies liable to reverse charge: the tax on them is declared here for payment |
| 3.1(e) | Non-GST outward supplies |
| 3.2 | Inter-State supplies to unregistered persons, composition taxpayers, UIN holders |
| 4(A)(1) | ITC on import of goods |
| 4(A)(2) | ITC on import of services (reverse charge); this credit is not in GSTR-2B and is entered by the taxpayer |
| 4(A)(3) | ITC on inward supplies liable to reverse charge (other than imports), taken after the tax is paid |
| 4(A)(4) | ITC from an Input Service Distributor |
| 4(A)(5) | All other ITC (supplies from registered persons other than reverse charge) |
| 4(B)(2) | ITC reversed, including the rule 37A reversal (Section 5.6) |
| 4(D)(2) | ITC not available under the GSTR-2B "ITC not available" part |
| 5.1 | Interest and late fee payable |
| 6.1 | Payment of tax: cash and ITC, by tax head |

**Key GSTR-1 tables**

Table numbers follow the GSTR-1A instructions in Notification 12/2024-Central Tax (link above), which use the GSTR-1 table numbers.

| Table | Meaning |
| --- | --- |
| 4A / 4B | Supplies to registered persons (B2B): 4A other than reverse charge; 4B supplies attracting reverse charge |
| 5 | Inter-State supplies to unregistered persons with invoice value above the B2C large limit (Section 5.10) |
| 6 | Exports and supplies to SEZ units or developers, deemed exports |
| 7 | Supplies to unregistered persons below that limit, rate-wise (B2C small) |
| 8 | Nil-rated, exempted and non-GST supplies (legacy reference) |
| 9A / 9C | Amendments of earlier B2B, B2C large, export, and credit or debit note details |
| 9B | Credit and debit notes |
| 12 | HSN-wise summary of outward supplies |
| 14 / 14A / 15 | Supplies through e-commerce operators |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Standard rate (18%) until the rate notification is checked |
| Unknown GST status of a purchase | No ITC |
| Unknown counterparty State | Same State as the client (intra-State, CGST plus SGST) |
| Unknown B2B vs B2C status for buyer | B2C (no GSTIN, no ITC for the buyer) |
| Unknown business-use share (vehicle, phone, home office) | No ITC |
| Unknown SaaS billing entity | Foreign supplier: reverse charge on import of services (IGST) |
| Unknown blocked-credit status (food, club, personal use) | Blocked under section 17(5) |
| Unknown whether transaction is in scope | In scope |
| Unknown inter-State vs intra-State | Intra-State (CGST plus SGST) |

**Red flags for the reviewer brief**

The earlier Guide gave fixed rupee and percentage trigger levels. They were internal settings, not law, and no official page prints them. The reviewing accountant sets the levels. Flag at least: any single transaction that is large for this client; any conservative default that moves a material amount of tax; one counterparty that dominates outputs or inputs; many conservative defaults in one return; a large net GST position.

## Section 2: Required inputs and refusal catalogue

### Required inputs

**Minimum viable**: bank statement for the month or quarter in CSV, PDF, Excel, or pasted text, covering the full filing period. Acceptable from any Indian bank (SBI, HDFC, ICICI, Axis, Kotak, PNB, Bank of Baroda, IndusInd, Yes Bank, IDFC First, or any other scheduled bank). Also acceptable: Razorpay, Paytm or other payment processor settlement reports.

**Recommended**: purchase and sales invoices for the period (especially for inter-State B2B, exports and reverse charge), prior period GSTR-3B and GSTR-1 filed copies, GSTR-2B for each month of the period, and Form 26AS / AIS for cross-checking.

**Ideal**: Tally / Zoho Books / Busy or similar export (trial balance and GST transaction register), complete invoice register with HSN/SAC codes, last year's GSTR-9, e-invoice JSON exports where e-invoicing applies.

**Refusal policy if minimum is missing: SOFT WARN.** If no bank statement or transaction data is available at all, hard stop. If bank statement only, without invoices, proceed but record in the reviewer brief: "This GSTR-3B was produced from the bank statement alone. Before approval the reviewer must check that every ITC claim is backed by a tax invoice that appears in GSTR-2B, that every inter-State and intra-State classification is right, and that each reverse-charge self-assessment matches the supplier's document."

### India-specific refusal catalogue

If any trigger fires, stop and give the refusal message. Refusal is a safety mechanism.

- **R-IN-1: Composition scheme taxpayer.** Trigger: the client pays tax under section 10 (composition), or mentions CMP-08 or GSTR-4. Message: "Composition taxpayers pay tax quarterly with statement CMP-08 and file one annual return, GSTR-4, not GSTR-1 and GSTR-3B. They pay tax at a flat rate on turnover and cannot claim input tax credit. This Guide covers regular taxpayers only. Please use a qualified GST practitioner." The composition limits, rates and dates are in the table below, for the referral note only.
- **R-IN-2: Multi-State registration.** Trigger: the client has GSTINs in more than one State and asks to consolidate or cross-use credit. Message: "Each State GSTIN is a separate registration, with its own returns and its own credit ledger. This Guide handles one GSTIN. File each GSTIN separately; for Input Service Distributor or cross-charge questions, use a qualified CA or GST practitioner."
- **R-IN-3: Supplies to SEZ units or developers.** Trigger: the client supplies to SEZ units or developers and asks about zero-rating, LUT or refund of accumulated ITC for those supplies. Message: "SEZ supply documentation needs fact-specific checks beyond this Guide. Please use a qualified GST practitioner."
- **R-IN-4: E-commerce operator.** Trigger: the client runs an e-commerce platform that must collect tax at source under section 52 or pay tax under section 9(5). Message: "E-commerce operators have TCS, GSTR-8 and platform-level duties outside this Guide. Please use a qualified GST practitioner."
- **R-IN-5: Input Service Distributor (ISD).** Trigger: the client is registered as an ISD or needs to distribute common input services across GSTINs. Message: "ISD distribution is outside this Guide, which covers single-GSTIN regular taxpayers. Please use a qualified CA or GST practitioner."
- **R-IN-6: Return outside the three-year window.** Trigger: GSTR-1, GSTR-3B or GSTR-9 for a period whose due date passed more than three years ago. Message: "The CGST Act bars filing these returns after three years from their due date unless the Government notifies otherwise (sections 37(5), 39(11), 44(2)). Please use a qualified GST practitioner."

Composition figures (for the R-IN-1 referral note):

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf |
| Composition turnover limit (preceding financial year), normal States | INR 1.5 crore | "Composition threshold limit increased to be Rs. 1.5 Crore" |
| Composition limit in Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, Tripura, Uttarakhand | INR 75 lakh | "have the said limit as Rs. 75 lakh" |
| Rate, manufacturers (total) | 1% | "Manufacturers 1%" |
| Rate, traders (total, on taxable supplies) | 1% | "specified Traders 1%" |
| Rate, restaurants (total) | 5% | "Restaurants 5%" |
| Services composition option (section 10(2A)), total rate | 6% | "with a tax rate of 6% (3% CGST +3% SGST)" |
| Services composition option, preceding-year turnover up to | INR 50 lakh | "having an Annual Turnover in the preceding Financial Year up to Rs. 50 lakhs" |
| Annual return (GSTR-4) for the previous financial year | 30th April | "furnish a return till 30th April for the previous financial year" |
| Quarterly payment (CMP-08) | 18th of the month after the quarter | "quarterly basis till 18th of the month succeeding such quarter" |

## Section 3: Supplier pattern library (the lookup table)

This is the pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table. If none match, fall through to the rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If several patterns match, use the most specific. "ITC per invoice" means: take the tax the supplier charged on its tax invoice, and claim it only if the invoice is in GSTR-2B and section 17(5) does not block it (Section 5.6 and 5.7). The bank line alone never proves the rate.

### 3.1 Indian banks

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SBI, STATE BANK OF INDIA, HDFC BANK, ICICI BANK, AXIS BANK, KOTAK MAHINDRA, PNB, BANK OF BARODA, INDUSIND, YES BANK, IDFC FIRST | Bank charges: ITC per invoice | Check the bank's invoice or statement for the GST charged; claim only what it shows |
| INTEREST, BYAJ, INT PAID, INT RECD | EXCLUDE | Interest movement, no GST invoice |
| LOAN, EMI, PERSONAL LOAN, HOME LOAN | EXCLUDE | Loan principal or EMI movement, not a purchase |
| FD, FIXED DEPOSIT, RD | EXCLUDE | Investment movement |

### 3.2 Government (exclude entirely)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GST PMT, GST PAYMENT, GST CHALLAN, GSTN | EXCLUDE | Tax payment to government |
| INCOME TAX, IT DEPT, TDS, ADVANCE TAX, CPC BANGALORE | EXCLUDE | Direct tax payment |
| MCA, ROC FEE, COMPANY AFFAIRS | EXCLUDE | Regulatory fee |
| EPFO, PF, ESI, ESIC, PROVIDENT FUND | EXCLUDE | Statutory social security contribution |
| PROFESSIONAL TAX, PT PAYMENT | EXCLUDE | State professional tax |
| STAMP DUTY, REGISTRATION FEE (government) | EXCLUDE | Government fee |
| MUNICIPAL, NAGAR NIGAM, PROPERTY TAX | EXCLUDE | Local body tax |

### 3.3 Telecom and utilities

| Pattern | Treatment | GSTR-3B table | Notes |
| --- | --- | --- | --- |
| JIO, RELIANCE JIO, AIRTEL, BHARTI AIRTEL, VI, VODAFONE IDEA, BSNL, MTNL | ITC per invoice | 4(A)(5) | Telecom service. Mixed personal use: apportion under section 17(1) |
| TATA POWER, ADANI ELECTRICITY, BSES, BESCOM, MSEDCL | EXCLUDE | | Electrical energy is exempt (rate table above). No GST to claim. The earlier Guide said electricity was taxed at the standard rate: wrong |
| MAHANAGAR GAS, IGL, ADANI GAS | ITC per invoice | 4(A)(5) | Rate not proven on a readable page; use the invoice |
| WATER SUPPLY, JAL BOARD | EXCLUDE | | Municipal water |

### 3.4 Insurance

| Pattern | Treatment | Notes |
| --- | --- | --- |
| LIC, LIFE INSURANCE CORP (individual policy) | EXCLUDE | Individual life insurance is exempt from 22 September 2025 (rate table above). Group policies are not covered by that exemption; ITC on life insurance is blocked anyway by section 17(5)(b)(i) unless the employer must provide it by law or it is used for an outward supply of the same category |
| STAR HEALTH, NIVA BUPA, CARE HEALTH (individual policy) | EXCLUDE | Individual health insurance is exempt from 22 September 2025. Health insurance ITC is blocked by section 17(5)(b)(i) with the same two exceptions |
| HDFC ERGO, ICICI LOMBARD, BAJAJ ALLIANZ, NEW INDIA ASSURANCE, UNITED INDIA (general insurance) | ITC per invoice, then check section 17(5)(ab) | General insurance of a car blocked under section 17(5)(a) is itself blocked by section 17(5)(ab) |

### 3.5 SaaS and cloud billed by Indian entities

| Pattern | Billing entity | Treatment | Notes |
| --- | --- | --- | --- |
| AWS INDIA, AMAZON INTERNET SERVICES | Amazon Internet Services Pvt Ltd (IN) | ITC per invoice: IGST if the supplier's State differs, CGST plus SGST if the same | Check the supplier GSTIN and the place of supply |
| GOOGLE INDIA, GOOGLE CLOUD INDIA | Google India Pvt Ltd / Google Cloud India Pvt Ltd (IN) | ITC per invoice | Check the invoice carries an Indian GSTIN |
| ZOHO, ZOHO CORP | Zoho Corporation Pvt Ltd (IN) | ITC per invoice | Check State |
| FRESHWORKS | Freshworks Technologies Pvt Ltd (IN) | ITC per invoice | |
| MICROSOFT INDIA | Microsoft Corporation India Pvt Ltd (IN) | ITC per invoice | Check the invoice carries an Indian GSTIN |
| CLEARTAX, CLEAR | Clear (IN) | ITC per invoice | Accounting or compliance software |

### 3.6 Foreign SaaS (reverse charge on import of services)

For a registered business, a service bought from a supplier outside India is an import of services. The business pays IGST itself under reverse charge (IGST Act section 5(3)), declares it in GSTR-3B table 3.1(d), and takes the credit in table 4(A)(2) after paying, because this credit is not in GSTR-2B (Notification 12/2024-Central Tax instructions). Rate: the rate notified for the service; the standard rate is the default until checked.

| Pattern | Billing entity | Treatment |
| --- | --- | --- |
| NOTION, NOTION LABS | Notion Labs Inc (US) | Reverse charge, IGST |
| OPENAI, CHATGPT | OpenAI (US) | Reverse charge, IGST |
| GITHUB | GitHub Inc (US) | Reverse charge if billed by the US entity; check the invoice |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Reverse charge, IGST |
| FIGMA | Figma Inc (US) | Reverse charge, IGST |
| CANVA | Canva Pty Ltd (AU) | Reverse charge, IGST |
| SLACK | Slack Technologies (US) or a Salesforce entity | Check the billing entity |
| HUBSPOT | HubSpot Inc (US) | Check the billing entity |
| TWILIO | Twilio Inc (US) | Reverse charge, IGST |

### 3.7 Payment processors

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RAZORPAY, PAYTM, ONE97 COMMUNICATIONS, CASHFREE, INSTAMOJO, PHONEPE BUSINESS, CCAVENUE, BILLDESK | ITC per invoice | Gateway fees; check the supplier GSTIN State |
| STRIPE INDIA, STRIPE PAYMENTS INDIA | ITC per invoice | Indian entity |
| STRIPE (US or Irish entity), PAYPAL (foreign entity fees) | Reverse charge, IGST | Foreign supplier with no Indian GSTIN on the document |

### 3.8 Travel

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INDIGO, INTERGLOBE AVIATION, AIR INDIA, SPICEJET, AKASA AIR, AIR INDIA EXPRESS | Economy 5%; any other class 18% | Rates from the GST Council FAQ in Section 1. ITC per invoice if business travel; travel benefits to employees on vacation are blocked (section 17(5)(b)(iii)) |
| OLA, ANI TECHNOLOGIES, UBER INDIA | ITC per invoice | Passenger transport by motor vehicle: 5% with limited ITC, or 18% with ITC, by the supplier's rate (Section 1). Renting or hiring a passenger car is blocked unless used for the purposes in section 17(5)(a) (section 17(5)(b)(i)) |
| IRCTC, INDIAN RAILWAYS | ITC per invoice | Rate not printed on a readable page |
| MAKEMYTRIP, GOIBIBO, YATRA | ITC per invoice | The platform fee and the underlying ticket or room are separate lines |
| HOTELS, OYO, TAJ, ITC HOTELS, LEMON TREE | ITC per invoice | Room value per unit per day at or below INR 7,500: 5% without ITC to the hotel. Above it: rate not printed on a readable page; use the invoice |

### 3.9 Restaurants and food delivery

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SWIGGY, BUNDL TECHNOLOGIES, ZOMATO | No ITC | Food and beverages: ITC blocked by section 17(5)(b)(i) unless used for an outward supply of the same category |
| Restaurant (direct), DOMINOS, PIZZA HUT, MCDONALDS, KFC, BURGER KING, REBEL FOODS | No ITC | Same block |

### 3.10 Professional services

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CA, CHARTERED ACCOUNTANT, [name] & ASSOCIATES, CS, COMPANY SECRETARY, ARCHITECT, INTERIOR DESIGNER | ITC per invoice | Forward charge from a registered supplier |
| ADVOCATE, ADV, LAWYER, LAW FIRM | Reverse charge | Legal services by an individual advocate or a firm of advocates to a business entity: the business pays the tax (Section 5.4) |
| CONSULTANT, CONSULTANCY | ITC per invoice | Foreign consultant: reverse charge on import of services |
| DIRECTOR FEE, SITTING FEE | Reverse charge | Services by a director to the company (Section 5.4); salary under an employment contract is excluded instead |
| SECURITY SERVICES, SECURITY AGENCY, SECURITY GUARDS (supplier not a body corporate) | Reverse charge | Supply of security personnel by a person other than a body corporate to a registered person (Section 5.4). A company supplier charges forward: ITC per invoice |

### 3.11 Rent

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RENT (commercial property, registered landlord) | ITC per invoice | Forward charge |
| RENT (commercial property, unregistered landlord, registered tenant) | Reverse charge | From 10 October 2024 (serial 5AB); a tenant paying tax under composition is excluded (Section 5.4) |
| RENT (residential dwelling, registered tenant) | Reverse charge | From 18 July 2022 (serial 5AA). Exempt from 1 January 2023 where a proprietor rents the home in a personal capacity as his own residence, on his own account (Section 5.4) |
| RENT (residential, unregistered tenant) | EXCLUDE | |
| COWORKING, WEWORK, AWFIS, COWRKS, 91SPRINGBOARD | ITC per invoice | Workspace service |

### 3.12 Salaries and wages (exclude entirely)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES, STIPEND, PAYROLL, BONUS, GRATUITY, LEAVE ENCASHMENT | EXCLUDE | Employee pay; no supplier invoice and no GST |
| CONTRACTOR (individual, no GSTIN) | EXCLUDE from ITC; flag for TDS | No tax invoice from an unregistered supplier. For TDS on contractor payments see `in-tds-freelance` |

## Section 4: Worked examples

Six classifications from a hypothetical HDFC Bank statement of a Mumbai-based self-employed software consultant registered in Maharashtra. Amounts in the bank lines are hypothetical. The tax columns are left for the working paper (Section 7), which computes them from the invoice; this Guide does not compute tax.

### Example 1: Foreign SaaS under reverse charge (Notion)

**Input line:** `05.01.2026 ; NOTION LABS INC DEBIT CARD ; DR ; 10.00 ; USD ; 840.00 ; INR`

**Reasoning:** Notion Labs Inc is a US entity (Section 3.6). No GST on the charge. This is an import of services: the client self-assesses IGST under reverse charge (IGST Act section 5(3)), pays it in cash (Section 5.8), declares it in table 3.1(d), and takes the credit in table 4(A)(2) once paid, if section 16 conditions are met.

| Date | Counterparty | Gross | GSTR-3B (output) | GSTR-3B (input) | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- |
| 05.01.2026 | NOTION LABS INC | -840 | 3.1(d) | 4(A)(2) | Y (rate) | "Confirm the rate notified for this service" |

### Example 2: Indian SaaS, inter-State (AWS India)

**Input line:** `10.01.2026 ; AMAZON INTERNET SERVICES PVT LTD NEFT ; DR ; 23,600.00 ; INR`

**Reasoning:** the supplier's invoice shows a GSTIN in another State, so the supply is inter-State and the invoice charges IGST. Take the IGST on the invoice as ITC in table 4(A)(5) if the invoice is in GSTR-2B.

| Date | Counterparty | Gross | GSTR-3B | Default? | Question? |
| --- | --- | --- | --- | --- | --- |
| 10.01.2026 | AMAZON INTERNET SERVICES | -23,600 | 4(A)(5) | N | "Invoice in GSTR-2B?" |

### Example 3: Food delivery, blocked ITC (Swiggy)

**Input line:** `15.01.2026 ; BUNDL TECHNOLOGIES SWIGGY ; DR ; 450.00 ; INR`

**Reasoning:** food and beverages are blocked by section 17(5)(b)(i) whatever the business purpose, unless used for an outward supply of the same category. No ITC. The expense may still count for income tax if business-related.

| Date | Counterparty | Gross | ITC? | Default? | Question? |
| --- | --- | --- | --- | --- | --- |
| 15.01.2026 | SWIGGY | -450 | BLOCKED, section 17(5)(b)(i) | N | "Business meal? (for income tax records only)" |

### Example 4: Legal services under reverse charge (advocate)

**Input line:** `20.01.2026 ; ADV RAJESH SHARMA NEFT ; DR ; 50,000.00 ; INR`

**Reasoning:** legal services by an individual advocate to a business entity are under reverse charge (Notification 13/2017-Central Tax (Rate), serial 2). The client pays the tax in cash, declares it in table 3.1(d), and takes credit in table 4(A)(3) after paying. Advocate and client are both in Maharashtra, so the tax is CGST plus SGST.

| Date | Counterparty | Gross | GSTR-3B (output) | GSTR-3B (input) | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- |
| 20.01.2026 | ADV RAJESH SHARMA | -50,000 | 3.1(d) | 4(A)(3) | Y | "Is the advocate in the same State? Is the service for the business?" |

### Example 5: Domestic air travel

**Input line:** `22.01.2026 ; INTERGLOBE AVIATION INDIGO PNR AB1CDE ; DR ; 5,250.00 ; INR`

**Reasoning:** domestic flight. Economy class is charged at 5%; any other class at 18% (Section 1). Take the tax on the airline's invoice as ITC in table 4(A)(5) if the trip was business travel and the invoice is in GSTR-2B. A proprietor's own business trip is not a travel benefit to an employee on vacation (section 17(5)(b)(iii)).

| Date | Counterparty | Gross | GSTR-3B | Default? | Question? |
| --- | --- | --- | --- | --- | --- |
| 22.01.2026 | INTERGLOBE AVIATION | -5,250 | 4(A)(5) | Y | "Economy or other class? Business purpose? Invoice in GSTR-2B?" |

### Example 6: Passenger car, blocked

**Input line:** `28.01.2026 ; MARUTI SUZUKI INDIA LTD NEFT ; DR ; 8,50,000.00 ; INR`

**Reasoning:** a car with seating for not more than thirteen persons including the driver is blocked by section 17(5)(a), except when used for further supply of such vehicles, transport of passengers, or driving training. A software consultant meets none of these. No ITC. The rate on the invoice depends on the car (small cars 18%, mid-size and large cars 40%; Section 1).

| Date | Counterparty | Gross | ITC? | Default? | Question? |
| --- | --- | --- | --- | --- | --- |
| 28.01.2026 | MARUTI SUZUKI | -8,50,000 | BLOCKED, section 17(5)(a) | Y | "Is the vehicle used to carry passengers for a fare, resold, or used for driving training?" |

## Section 5: Rules

Each rule names its legal source. Apply silently when the data is unambiguous.

### 5.1 Rates

Use the rate tables in Section 1. The 56th GST Council rates apply from 22 September 2025 for services and for goods other than pan masala, tobacco, cigarettes and bidi, which moved on 1 February 2026. An invoice dated before the start date keeps the old rate; for supplies that straddle a start date, refer (Section 10, Known gaps).

### 5.2 CGST plus SGST, or IGST

Central tax (CGST Act section 9(1)) and State tax are levied on intra-State supplies; integrated tax is levied on inter-State supplies (IGST Act section 5(1), at a rate "not exceeding forty per cent"). The place of supply decides which, under Chapter V of the IGST Act (sections 10 to 14).

| Scenario | Tax type |
| --- | --- |
| Supplier's location and place of supply in the same State | CGST plus SGST |
| Same Union territory (without legislature) | CGST plus UTGST |
| Different States | IGST |
| Import of goods | IGST through customs |
| Import of services by a business | IGST under reverse charge |
| Export, or supply to an SEZ unit or developer for authorised operations | Zero-rated (Section 5.11) |

Working check, not the legal test (the test is the supplier's location and the place of supply, IGST Act Chapter V): compare the State code at the start of the supplier's GSTIN with the client's. For a buyer with no GSTIN, use the place of supply rules, not the billing address alone. Online information and database access services from abroad to a person who is not registered (a "non-taxable online recipient") are taxed on the foreign supplier, not the customer (IGST Act section 14).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_IGST_Act/active/chapteriii/section5_v1.00.html |
| IGST rate ceiling | not exceeding forty per cent | "at such rates, not exceeding forty per cent., as may be notified" |
| Reverse charge power | categories notified by the Government | "specify categories of supply of goods or services or both, the tax on which shall be paid on reverse charge basis by the recipient" |

### 5.3 Reverse charge on import of services

A registered business that buys a service from a supplier outside India pays IGST on it under reverse charge (IGST Act section 5(3)). Pay it through the electronic cash ledger (Section 5.8). Declare it in GSTR-3B table 3.1(d). Take the credit in table 4(A)(2), once paid, if the service is for the business and section 17(5) does not block it. GSTR-2B does not show this credit: "reverse charge credit on import of services is not part of this statement and will be continued to be entered by taxpayers in Table 4(A)(2) of FORM GSTR-3B" (Notification 12/2024-Central Tax, https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf). The notification that lists import of services under reverse charge (10/2017-Integrated Tax (Rate)) could not be read on an allowed host.

### 5.4 Domestic reverse charge

The recipient pays the tax on these supplies (CGST Act section 9(3) and Notification 13/2017-Central Tax (Rate), as amended). Self-assess at the rate for the service, pay in cash, declare in table 3.1(d), and take credit in table 4(A)(3) after paying.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/download_8_0.pdf |
| Goods transport agency (GTA) services to factories, societies, co-operatives, registered persons, body corporates, partnership firms, casual taxable persons (serial 1) | Reverse charge, unless the GTA opted for forward charge | "Supply of Services by a goods Goods (a) Any factory registered under or transport agency (GTA)" |
| Legal services by an individual advocate or a firm of advocates to a business entity (serial 2) | Reverse charge | "Services supplied by an individual An Any business entity located in the advocate including a senior" |
| Sponsorship services to a body corporate or partnership firm (serial 4) | Reverse charge | "Services provided by way of Any Any body corporate or partnership sponsorship" |
| Services by the Central or State Government, Union territory or local authority to a business entity (serial 5, as amended) | Reverse charge, with exclusions added since 2017 | "d by the Central Central Any business entity located in the Government" |
| Services by a director to the company or body corporate (serial 6) | Reverse charge | "Services supplied by a director of a A director The company or a body corporate" |

The GTA forward-charge option is in Notification 05/2022-Central Tax (Rate): the entry does not apply where the GTA has registered, opted to pay tax under forward charge, and declared so on its invoice.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/05_2022-ctr-eng_1.pdf |
| Renting of a residential dwelling to a registered person (serial 5AA) | Reverse charge on the registered tenant | "5AA Service by way of renting of Any Any registered person.”; residential dwelling to a person registered person." |
| Start date | 18 July 2022 | "This notification shall come into force with effect from the 18th July, 2022" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/15_2022-ctr-eng.pdf |
| Residential dwelling rented to a registered proprietor as his own residence, in a personal capacity and on his own account | Exempt (Notification 12/2017-Central Tax (Rate), serial 12, Explanation) | "the registered person is proprietor of a proprietorship concern and rents the residential dwelling in his personal capacity for use as his own residence" |
| Start date | 1 January 2023 | "come into force with effect from the 01 st day of January, 2023" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-10/ctr-09-2024.pdf |
| Renting of any property other than a residential dwelling by an unregistered person to a registered person (serial 5AB) | Reverse charge on the registered tenant | "Service by way of renting of any Any unregistered Any registered property other than residential" |
| Start date | 10 October 2024 | "This notification shall come into force with effect from the 10th day of October, 2024" |

Notification 07/2025-Central Tax (Rate) takes a tenant who pays tax under composition out of serial 5AB: "the words “other than a person who has opted to pay tax under composition levy” shall be inserted" (https://gstcouncil.gov.in/sites/default/files/2025-01/ctr07-2025.pdf).

Security services were added to the reverse charge list by Notification 29/2018-Central Tax (Rate):

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/download_2024-05-17t161051.835.pdf |
| Security services (supply of security personnel) by a person other than a body corporate to a registered person (serial 14) | Reverse charge on the registered recipient | "Security services (services provided by way of supply of security personnel) provided to a registered person"; supplier "Any person other than a body corporate"; recipient "A registered person, located in the taxable territory" |
| Start date | 1 January 2019 | "This notification shall come into force on the 1st day of January, 2019" |

Serial 14 carries a proviso ("Provided that nothing ...") that takes some recipients out of the entry; read it on the notification before applying reverse charge to a particular client. Other entries added after 2017 are not covered here: the amending notifications were not read. Check the current consolidated Notification 13/2017-Central Tax (Rate) for any service not in the tables above.

### 5.5 E-invoicing, invoices and HSN codes

A registered person in the class notified under rule 48(4) of the CGST Rules must report each B2B invoice to the Invoice Registration Portal, get an Invoice Reference Number (IRN), and print the QR code carrying the IRN on the invoice (rule 46(r)). The class is set by Notification 13/2020-Central Tax as amended; its turnover test is in the table below. The years that count are in the second table below (Notification 70/2020-Central Tax). The exempt categories and any time limit for reporting are in that notification and in GSTN advisories, which could not be read on an allowed host. For e-invoicing detail use `india-einvoice`.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/10ct_eng.pdf |
| E-invoice aggregate turnover threshold (amending Notification 13/2020-Central Tax) | five crore rupees | "for the words “ten crore rupees”, the words “five crore rupees” shall be substituted" |
| Start date | 1 August 2023 | "with effect from the 1 st day of August, 2023" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-70-central-tax-english-2020.pdf |
| Turnover test: aggregate turnover in | any preceding financial year from 2017-18 onwards | "for the words “a financial year”, the words and figures “any preceding financial year from 2017-18 onwards” shall be substituted" |
| E-invoicing covers supplies | to a registered person, or for exports | "after the words “goods or services or both to a registered person”, the words “or for exports” shall be inserted" |
| Notification date | 30 September 2020 | "New Delhi, the 30th September, 2020" |

So a business whose aggregate turnover crossed five crore rupees in any financial year from 2017-18 onwards, even if it is below that now, is in the e-invoicing class.

HSN code digits on tax invoices, from 1 April 2021 (Notification 78/2020-Central Tax under rule 46):

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-78-central-tax-english-2020.pdf |
| Aggregate turnover in the preceding financial year up to five crore rupees | 4 digits (may be omitted on invoices to unregistered persons) | "1. Up to rupees five crores 4"; "may not mention the number of digits of HSN Code ... in respect of supplies made to unregistered persons" |
| More than five crore rupees | 6 digits | "2. more than rupees five crores 6" |

HSN covers goods; services use the SAC codes of the services classification (chapter 99).

### 5.6 ITC: conditions, GSTR-2B reconciliation and time limit

**Conditions (CGST Act section 16(2)), all of them:**
1. The business holds a tax invoice or debit note from a registered supplier (or another prescribed document, rule 36(1)).
2. The supplier has reported the invoice in GSTR-1 (or IFF, or GSTR-1A) and it has been communicated to the business (section 16(2)(aa)); rule 36(4) adds that the ITC must be communicated in GSTR-2B.
3. The goods or services have been received.
4. The ITC communicated in GSTR-2B has not been restricted (section 16(2)(ba)).
5. The tax has been actually paid to the Government by the supplier, in cash or through its own ITC.
6. The business has filed its own GSTR-3B (section 39 return).

**Reconciliation, every period:**
1. Download GSTR-2B for the month. It is auto-generated, monthly (rule 60(7)); the form instructions show a January statement "made available on 14 th Feb 2023". Match every purchase invoice in the books to GSTR-2B.
2. Claim in GSTR-3B only ITC that is in GSTR-2B (rule 36(4)), except the import-of-services credit in table 4(A)(2), which GSTR-2B never shows.
3. Invoice in the books but not in GSTR-2B: do not claim. Ask the supplier to report it; claim it in the month it appears, within the time limit below.
4. Invoice in GSTR-2B but not in the books: check whether it is a real purchase before claiming.
5. Credit shown in GSTR-2B under "ITC not available": do not claim (table 4(D)(2)).
6. If ITC claimed in GSTR-3B exceeds GSTR-2B beyond the limit the Council sets, the portal sends Form DRC-01C; within seven days pay the excess with interest through DRC-03 or explain the difference (rule 88D).
7. If tax payable per GSTR-1 exceeds tax paid per GSTR-3B beyond the set limit, the portal sends Form DRC-01B; pay or explain within seven days (rule 88C).

**Reversals:**
- **Supplier not paid within one hundred and eighty days of the invoice date** (section 16(2), second proviso; rule 37): reverse the ITC, in proportion to the amount not paid, with interest, in the GSTR-3B for the period after the one hundred and eighty days end. Re-claim when you pay; the time limit below does not apply to the re-claim (rule 37(4)). Supplies under reverse charge are outside this rule.
- **Supplier filed GSTR-1 but not its GSTR-3B by 30 September following the end of the financial year** in which the business took the credit (rule 37A): reverse the credit in a GSTR-3B filed on or before 30 November of that year, reported in table 4(B)(2). If not reversed by then, pay it with interest. Re-claim once the supplier files.
- **Common credit for taxable and exempt supplies**: reverse the exempt share under section 17(2) and rule 42 (inputs and input services) or rule 43 (capital goods). Rule 43 treats the useful life of capital goods as five years from the invoice date and spreads the credit monthly as "T m = T c / 60".
- **Depreciation on the tax**: if income tax depreciation is claimed on the tax component, no ITC on that tax (section 16(3)).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html |
| Last date to take ITC for an invoice or debit note | 30 November following the end of the financial year, or the date the annual return is filed, whichever is earlier | "after the 6 [thirtieth day of November] following the end of financial year to which such invoice or" ... "or furnishing of the relevant annual return, whichever is earlier" |
| Payment to supplier due within | one hundred and eighty days from the invoice date | "within a period of one hundred and eighty days from the date of issue of invoice by the supplier" |

For invoices of financial year 2025-26, the last date is 30 November 2026, or the earlier date GSTR-9 for 2025-26 is filed.

### 5.7 Blocked credits: section 17(5)

No ITC on the items below, even if used for business (CGST Act section 17(5), text in force on 17 October 2026: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section17_v1.00.html). Separately, section 17(1) limits ITC to the business share of a mixed-use purchase, and section 17(2) to the share used for taxable (including zero-rated) supplies.

| Clause | Blocked | Exception (ITC allowed only then) |
| --- | --- | --- |
| (a) | Motor vehicles for transporting persons with approved seating of not more than thirteen persons (including the driver) | Used for further supply of such vehicles, transport of passengers, or training on driving them. Goods vehicles are not in this clause |
| (aa) | Vessels and aircraft | Further supply, passenger transport, navigation or flying training, or transport of goods |
| (ab) | General insurance, servicing, repair and maintenance of the vehicles, vessels and aircraft in (a) and (aa) | Where the vehicle, vessel or aircraft is used for the excepted purposes, or the buyer manufactures them or insures them |
| (b)(i) | Food and beverages, outdoor catering, beauty treatment, health services, cosmetic and plastic surgery, leasing, renting or hiring of the vehicles, vessels or aircraft in (a) or (aa) (except for the excepted purposes), life insurance and health insurance | Used for an outward taxable supply of the same category, or as an element of a taxable composite or mixed supply; or the employer must provide it to employees by law |
| (b)(ii) | Membership of a club, health and fitness centre | Employer must provide it by law |
| (b)(iii) | Travel benefits to employees on vacation, such as leave or home travel concession | Employer must provide it by law |
| (c) | Works contract services for construction of immovable property (other than plant and machinery) | Input service for a further supply of works contract service |
| (d) | Goods or services for construction of immovable property (other than plant and machinery) on own account, even if used in business | None. "Construction" includes renovation and repairs to the extent capitalised |
| (e) | Goods or services on which tax was paid under composition (section 10) | None |
| (f) | Goods or services received by a non-resident taxable person | Goods he imports |
| (fa) | Goods or services used for corporate social responsibility obligations under section 135 of the Companies Act 2013 | None (from 1 October 2023) |
| (g) | Goods or services for personal consumption | None |
| (h) | Goods lost, stolen, destroyed, written off, or disposed of as gifts or free samples | None |
| (i) | Tax paid under section 74 for periods up to financial year 2023-24 | None |

The earlier Guide listed "transport of goods" as an exception for motor vehicles. Since 1 February 2019, clause (a) covers only passenger vehicles of up to thirteen seats; the goods exception is in clause (aa) for vessels and aircraft.

### 5.8 Paying the liability: cash and credit order

- Reverse-charge tax is paid in cash (electronic cash ledger). Credit in the electronic credit ledger may be used only "towards output tax" (section 49(4)), and "output tax" "excludes tax payable by him on reverse charge basis" (section 2(82)). The GSTR-3B instructions allow the matching credit only "on payment of tax".
- Order of use of credit (section 49(5) and rule 88A, https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter9/rule88a_v1.00.html):
  1. IGST credit is used first against IGST. Any balance may then be used against CGST and SGST/UTGST "in any order" (rule 88A).
  2. CGST and SGST credit may be used only after the IGST credit "has first been utilised fully".
  3. CGST credit: against CGST, then IGST. Never against SGST/UTGST (section 49(5)(e)).
  4. SGST/UTGST credit: against SGST/UTGST, then IGST, but against IGST only where no CGST credit is left for it (section 49(5)(c) proviso). Never against CGST (section 49(5)(f)).

The earlier Guide said IGST credit must go to CGST before SGST. Rule 88A, in force since 29 March 2019, lets the balance go to either "in any order".

### 5.9 ITC reversal for exempt supplies (rules 42 and 43)

Common credit (inputs and input services used for both taxable and exempt supplies) is split under rule 42; capital goods under rule 43. In outline: credit used only for exempt supplies or non-business use is not taken; credit used only for taxable supplies is taken in full; the exempt share of common credit is reversed in proportion to exempt turnover over total turnover in the State. The value of exempt supply includes reverse-charge supplies, securities, land and some building sales (section 17(3)). The monthly working is recalculated for the whole financial year before the due date of the return for September following the year end, and any excess reversal is paid with interest (rule 42(2)); refer the annual true-up to the accountant.

### 5.10 Return due dates and late fees: GSTR-1, GSTR-3B, GSTR-9

**Due dates.** The statute prints GSTR-1 "on or before the tenth day of the month succeeding the said tax period" (section 37(1)); Notification 83/2020-Central Tax extends it. GSTR-3B due dates are in rule 61; GSTR-9 in rule 80. A return is due even for a period with no supplies (section 39(8)). GSTR-1 cannot be filed while an earlier GSTR-1 is missing, and GSTR-3B cannot be filed while an earlier GSTR-3B or the same period's GSTR-1 is missing (sections 37(4), 39(10)). GSTR-1 (and IFF) also cannot be filed while the GSTR-3B for the preceding month, or for QRMP filers the preceding tax period, is unfiled (rule 59(6): "shall not be allowed to furnish ... FORM GSTR-1, if he has not furnished the return in FORM GSTR-3B for the preceding month"). After filing GSTR-1 and before filing GSTR-3B for the same period, the business may amend or add outward supplies in GSTR-1A (rule 59(1), proviso).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-83-central-tax-english-2020.pdf |
| GSTR-1, monthly filers | eleventh day of the following month | "till the eleventh day of the month succeeding such tax period" |
| GSTR-1, quarterly (QRMP) filers | thirteenth day of the month after the quarter | "shall be extended till the thirteenth day of the month succeeding such tax period" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html |
| GSTR-3B, monthly filers | twentieth day of the following month | "for each month, or part thereof, on or before the twentieth day of the month succeeding such month" |
| GSTR-3B, QRMP, principal place of business in Chhattisgarh, Madhya Pradesh, Gujarat, Maharashtra, Karnataka, Goa, Kerala, Tamil Nadu, Telangana, Andhra Pradesh, Daman and Diu and Dadra and Nagar Haveli, Puducherry, Andaman and Nicobar Islands, Lakshadweep | twenty-second day of the month after the quarter | "Lakshadweep. twenty-second day of the month succeeding such quarter" |
| GSTR-3B, QRMP, principal place of business in Himachal Pradesh, Punjab, Uttarakhand, Haryana, Rajasthan, Uttar Pradesh, Bihar, Sikkim, Arunachal Pradesh, Nagaland, Manipur, Mizoram, Tripura, Meghalaya, Assam, West Bengal, Jharkhand, Odisha, Jammu and Kashmir, Ladakh, Chandigarh, Delhi | twenty-fourth day of the month after the quarter | "Ladakh, Chandigarh or Delhi. twenty-fourth day of the month succeeding such quarter" |
| QRMP monthly payment (PMT-06) for months 1 and 2 of the quarter | twenty fifth day of the following month | "by depositing the said amount in FORM GST PMT-06 , by the twenty fifth day of the month succeeding such month" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule80_v1.00.html |
| GSTR-9 (annual return), due | 31 December after the end of the financial year | "electronically in FORM GSTR-9 on or before the thirty-first day of December following the end of such financial year" |
| GSTR-9C (self-certified reconciliation statement), required when aggregate turnover in the financial year exceeds | five crore rupees | "whose aggregate turnover during a financial year exceeds five crore rupees, shall also furnish a self-certified reconciliation statement" |

GSTR-9 for financial year 2025-26 is due on 31 December 2026. Composition taxpayers are outside this Guide (R-IN-1): rule 80(1) still prints "FORM GSTR-9A" for them, while the CBIC 2019 update describes an annual GSTR-4; refer. The Commissioner may exempt a class of persons from the annual return (section 44(1), proviso); this has been notified year by year. The only year proven on a readable page is financial year 2022-23:

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/gst-ct-32-2023.pdf |
| GSTR-9 optional for financial year 2022-23 where aggregate turnover is up to | two crore rupees | "whose aggregate turnover in the financial year 2022-23 is up to two crore rupees, from filing annual return" |

For later years, check whether a new exemption notification was issued before treating GSTR-9 as optional.

**GSTR-1 table limit (B2C large).** Inter-State supplies to unregistered persons are reported invoice by invoice above the limit below, and State-wise in consolidated form up to it (rule 59). The earlier Guide said two and a half lakh: Notification 12/2024-Central Tax substituted "one lakh rupees" (from 1 August 2024).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule59_v1.00.html |
| B2C large: inter-State invoice value to unregistered persons more than | one lakh rupees | "(ii) inter-State supplies with invoice value more than 10 [one lakh rupees] made to the unregistered persons" |
| Invoice Furnishing Facility (IFF), months 1 and 2 of a quarter: upload window | 1st day to the 13th day of the following month | "from the 1st day of the month succeeding such month till the 13th day of the said month" |
| IFF cap per month | fifty lakh rupees | "up to a cumulative value of fifty lakh rupees in each of the months" |

**Late fees.** Section 47 sets the late fee under the CGST Act; the State or UT Act charges the same again. Waiver notifications cut it. Every amount in the tables below is central tax only. Do not add the State share to a figure yourself; say "the same amount again under the SGST Act".

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section47_v1.00.html |
| Statutory late fee, GSTR-1 and GSTR-3B (central tax) | one hundred rupees for every day | "shall pay a late fee of one hundred rupees for every day during which such failure continues subject to a maximum amount of five thousand rupees" |
| Statutory maximum per return (central tax) | five thousand rupees | "subject to a maximum amount of five thousand rupees" |
| Statutory late fee, GSTR-9: maximum | a quarter per cent. of his turnover (in the State or UT) | "subject to a maximum of an amount calculated at a quarter per cent. of his turnover in the State or Union territory" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-76-central-tax-english-2018.pdf |
| GSTR-3B late fee per day after waiver (central tax) | twenty-five rupees for every day | "which is in excess of an amount of twenty-five rupees for every day during which such failure continues" |
| GSTR-3B, central tax payable nil | ten rupees for every day | "shall stand waived to the extent which is in excess of an amount of ten rupees for every day" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/notification-4-2018-central_tax-english.pdf |
| GSTR-1 late fee per day after waiver (central tax) | twenty-five rupees for every day | "which is in excess of an amount of twenty-five rupees for every day during which such failure continues: Provided that where there are no outward supplies" |
| GSTR-1, no outward supplies in the period | ten rupees for every day | "shall stand waived to the extent which is in excess of an amount of ten rupees for every day" |

Maximum late fee per return, by aggregate turnover in the preceding financial year, for tax periods from June 2021 (central tax). The PDFs print the table in two interleaved columns; the quotes are literal.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-19-central-tax-english-2021.pdf |
| GSTR-3B maximum, central tax payable nil | two hundred and fifty rupees | "Registered persons whose total amount of central tax Two hundred and payable in the said return is nil fifty rupees" |
| GSTR-3B maximum, aggregate turnover up to INR 1.5 crore | one thousand rupees | "2. Registered persons having an aggregate turnover of One thousand up to rupees 1.5 crores" |
| GSTR-3B maximum, aggregate turnover more than INR 1.5 crore and up to INR 5 crore | two thousand five hundred rupees | "Taxpayers having an aggregate turnover of more than Two thousand and rupees 1.5 crores and up to rupees 5 crores in the five hundred" |
| Turnover band boundary | INR 1.5 crore | "Registered persons having an aggregate turnover of One thousand up to rupees 1.5 crores" |
| Upper band boundary; above it the statutory maximum applies | INR 5 crore | "rupees 1.5 crores and up to rupees 5 crores" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-20-central-tax-english-2021.pdf |
| GSTR-1 maximum, nil outward supplies | two hundred and fifty rupees | "Registered persons who have nil outward supplies in Two hundred and the tax period fifty rupees" |
| GSTR-1 maximum, aggregate turnover up to INR 1.5 crore | one thousand rupees | "Registered persons having an aggregate turnover of One thousand up to rupees 1.5 crores" |
| GSTR-1 maximum, more than INR 1.5 crore and up to INR 5 crore | two thousand five hundred rupees | "Registered persons having an aggregate turnover of Two thousand and more than rupees 1.5 crores and up to rupees 5 crores five hundred rupees" |

GSTR-9 late fee, financial year 2022-23 onwards (Notification 07/2023-Central Tax), by aggregate turnover in the relevant financial year (central tax):

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-05/07_eng.pdf |
| Turnover up to five crore rupees: per day | twenty-five rupees per day | "Twenty-five rupees per day, subject to a of up to five crore rupees in the relevant financial" |
| Turnover up to five crore rupees: maximum | 0.02% of turnover in the State or UT | "maximum of an amount calculated at 0.02 per year. cent. of turnover in the State or Union territory" |
| Turnover more than five crore and up to twenty crore rupees: per day | fifty rupees per day | "Fifty rupees per day, subject to a maximum of an of more than five crores rupees and up to twenty amount calculated at 0.02 per cent." |
| Upper limit of the reduced fee | twenty crore rupees | "of more than five crores rupees and up to twenty amount calculated at 0.02 per cent. of turnover crore rupees" |

The maximum for the five-to-twenty-crore band is not settled: this print shows the same "0.02 per cent." as the band below, and other sources report a higher cap. Check the gazette copy before stating it. Above twenty crore rupees the statute applies (one hundred rupees per day, maximum a quarter per cent. of State turnover).

**Interest.** Interest runs from the day after tax was due (section 50(2)). On a GSTR-3B filed late, interest falls only on the tax paid through the cash ledger, unless proceedings under section 73, 74 or 74A have started (section 50(1), proviso). Wrongly availed ITC that was also utilised carries interest under section 50(3).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2024-04/notfctn-13-central-tax-english.pdf |
| Interest on late tax, section 50(1), per year | 18% | "Sub-section (1) of section 50 18" |
| Rate fixed in 2017 for section 50(3) | 24% | "sub-section (3) of section 50 24" (original 2017 text; section 50(3) was substituted in 2022 and later amendments to this rate were not checked: confirm the current rate) |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter10/section50_v1.00.html |
| Statutory ceiling, section 50(1) | eighteen per cent. | "pay, on his own, interest at such rate, not exceeding eighteen per cent." |
| Statutory ceiling, section 50(3) | twenty-four per cent. | "at such rate not exceeding twenty-four per cent. as may be notified" |

**Three-year bar.** GSTR-1, GSTR-3B and GSTR-9 cannot be filed after three years from their due date, unless the Government notifies otherwise (sections 37(5), 39(11) and 44(2), in force from 1 October 2023). Refer (R-IN-6).

**Corrections.** An error in GSTR-1 or GSTR-3B is corrected in a later period's return, with interest on any short payment, but not after 30 November following the end of the financial year or the date the annual return is filed, whichever is earlier (sections 37(3) and 39(9)).

### 5.11 Exports and supplies to SEZ

Export of goods or services, and supply to an SEZ unit or developer for authorised operations, are zero-rated supplies (IGST Act section 16(1)). ITC may be taken for them even if the supply is exempt (section 16(2)).

| Option | Mechanism | Refund |
| --- | --- | --- |
| Under bond or Letter of Undertaking, without paying IGST (section 16(3)) | File the LUT in Form GST RFD-11 before export (rule 96A) | Refund of unutilised ITC (section 54) |
| On payment of IGST (section 16(4)) | Only for a class of persons, or of goods or services, notified by the Government (substituted section, in force from 1 October 2023) | Refund of IGST paid |

Under an LUT, the exporter binds itself to pay the tax with interest within fifteen days after three months from the export invoice if the goods are not exported (or a longer period the Commissioner allows), and, for services, within fifteen days after one year or the FEMA period, whichever is later, if payment is not received in convertible foreign exchange, or in Indian rupees where the Reserve Bank of India permits (rule 96A(1)). Report exports in GSTR-3B table 3.1(b) and GSTR-1 table 6. Before using the IGST-payment route, confirm the client falls in a notified class; the earlier Guide presented it as open to every exporter.

### 5.12 E-way bill

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter16/rule138_v1.00.html |
| E-way bill needed before moving goods of consignment value exceeding | fifty thousand rupees | "Every registered person who causes movement of goods of consignment value exceeding fifty thousand rupees" |
| Validity | One day up to 200 km, and one more day for every further 200 km (other than over-dimensional cargo) | "Validity period (1) (2) (3) 1. Up to 3 [200 km.] One day in cases other than Over Dimensional Cargo" |

E-way bills cover goods only. Rule 138 lists exceptions (for example some short movements within a State to a transporter or weighbridge).

### 5.13 Registration thresholds

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html |
| Register when aggregate turnover in a financial year exceeds (normal States) | twenty lakh rupees | "if his aggregate turnover in a financial year exceeds twenty lakh rupees" |
| Special category States | ten lakh rupees | "he shall be liable to be registered if his aggregate turnover in a financial year exceeds ten lakh rupees" |
| Ceiling a State may set for suppliers of goods only | forty lakh rupees | "enhance the aggregate turnover from twenty lakh rupees to such amount not exceeding forty lakh rupees in case of supplier who is engaged exclusively in the supply of goods" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf |
| Services (and mixed) suppliers | INR 20 lakh | "for suppliers of services would be Rs. 20 lakhs and Rs. 10 lakhs (for States of Manipur, Mizoram, Nagaland and Tripura)" |
| Services suppliers in Manipur, Mizoram, Nagaland, Tripura | INR 10 lakh | "Rs. 20 lakhs and Rs. 10 lakhs (for States of Manipur, Mizoram, Nagaland and Tripura)" |
| Goods-only suppliers, States that opted in | INR 40 lakh | "for the suppliers of goods would be Rs. 40 lakhs and Rs. 20 lakhs" |
| Goods-only suppliers in Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Puducherry, Sikkim, Telangana, Tripura, Uttarakhand | INR 20 lakh | "Rs. 40 lakhs and Rs. 20 lakhs (in the States of Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Puducherry, Sikkim, Telangana, Tripura and U" |

The 2019 update lists the States as they stood in June 2019. Check the client's State has not changed its option since.

### 5.14 Compensation cess

Ended for most goods from 22 September 2025, with the cess folded into the GST rate (GST Council FAQ, Section 1). Withdrawn for specified pan masala and tobacco products from 1 February 2026 (December 2025 newsletter, Section 1). Do not add compensation cess to an invoice dated on or after the date that applies to the goods. The earlier Guide named a replacement cess on production capacity; no allowed page was found for it, so it is not stated here.

### 5.15 QRMP scheme (quarterly returns, monthly payment)

A registered person may opt to file GSTR-1 and GSTR-3B quarterly (section 39(1), proviso). The option is exercised on the portal from the first day of the second month of the preceding quarter to the last day of the first month of the quarter (rule 61A(1)); it cannot be exercised while the last due return is unfiled. Once aggregate turnover in the current financial year exceeds the limit below, the person must move to monthly returns from the next quarter (rule 61A(2)). QRMP filers pay tax for months 1 and 2 by the PMT-06 date in Section 5.10 and may upload B2B invoices through IFF (Section 5.10).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61a_v1.00.html |
| Turnover above which the person must move to monthly filing | INR 5 crore | "whose aggregate turnover exceeds 5 crore rupees during the current financial year, shall opt for furnishing of return on a monthly basis" |

The entry test for QRMP (aggregate turnover in the preceding financial year) is in Notification 84/2020-Central Tax, which was not read on an allowed host.

### 5.16 Pending: 57th GST Council recommendations (8 October 2026)

The 57th GST Council meeting recommended, among other things, a late fee waiver for small taxpayers who file within the due month, changes to penalties and prosecution limits, and extending e-invoicing to reverse-charge purchases from unregistered persons and to imports of services ("Extending relief for small taxpayers on late fees: The GST Council recommended waiver of late fee on delayed filing of return under section 39(1)", https://gstcouncil.gov.in/sites/default/files/2026-10/press_release_0.pdf). These are recommendations. None is law until the CGST Act or Rules are amended and the change is notified. Apply the rules in Sections 5.1 to 5.15 until then.

## Section 6: Tier 2 catalogue

For each ambiguity: the pattern, why the bank statement is not enough, the conservative default, and the question for the client.

### 6.1 Vehicle costs (fuel, tolls)

Pattern: HPCL, BPCL, IOCL, SHELL, petrol pump, FASTag, NHAI. Why not enough: the vehicle type and business use are unknown. A passenger car of up to thirteen seats is blocked by section 17(5)(a) unless used for the excepted purposes; its insurance, servicing and repair are blocked by section 17(5)(ab). A goods vehicle is not blocked by clause (a). GST on petrol and high speed diesel applies only from a date the Government notifies (IGST Act section 5(2)); if the fuel bill shows no GST, there is no credit to claim. Default: no ITC. Question: "Is this for a passenger car or a goods vehicle used in the business?"

### 6.2 Food delivery and restaurants

Pattern: SWIGGY, ZOMATO, BUNDL TECHNOLOGIES, restaurant names. Why not enough: business or personal is unknown, but it does not change the GST answer: food and beverages are blocked by section 17(5)(b)(i). Default: no ITC. Question (income tax records only): "Was this a client meeting?"

### 6.3 Home office (rent and utilities)

Pattern: rent to a landlord, electricity, internet at a home address. Why not enough: the business share and the tenant's capacity are unknown. A registered tenant of a residential dwelling pays tax under reverse charge (serial 5AA, from 18 July 2022), except a proprietor renting in a personal capacity as his own residence (exempt from 1 January 2023). Credit for personal consumption is blocked (section 17(5)(g)); mixed use is limited to the business share (section 17(1)). Electricity is exempt, so there is nothing to claim on it. Default: no ITC. Question: "Is the lease in your personal name or the business name? Do you live there? What share of the property is used only for business?"

### 6.4 Cash withdrawals

Pattern: ATM, CASH WDL, CASH WITHDRAWAL. Why not enough: what the cash bought is unknown, and ITC needs a tax invoice. Default: exclude as owner drawing. Question: "What was the cash used for? Do you have tax invoices for any cash purchases?"

### 6.5 Mixed B2B and B2C sales

Pattern: receipts from individuals or entities with no GSTIN visible. Why not enough: B2B sales go invoice by invoice in GSTR-1 table 4A; inter-State B2C sales above the B2C large limit go in table 5; other B2C sales go rate-wise in table 7. Default: B2C. Question: "For each sale, does the buyer have a GSTIN? If yes, what is it?"

### 6.6 Inter-State or intra-State

Pattern: counterparty State unclear. Why not enough: CGST plus SGST or IGST depends on the supplier's location and the place of supply; the wrong tax head means paying again under the right head and claiming a refund. Default: intra-State. Question: "Where is the counterparty? If registered, what is its GSTIN?"

### 6.7 Digital services from abroad: business or personal?

Pattern: foreign SaaS, streaming, cloud. Why not enough: if the client takes the service as a registered business, it pays IGST under reverse charge (Section 5.3). Online information and database access services to a person who is not registered are taxed on the foreign supplier (IGST Act section 14). Default: if it is on the business account, treat as business: reverse charge. Question: "Is this used for the business? If personal, it should not be on the business account."

## Section 7: Excel working paper template

### Sheet "Transactions"

Columns:
- A: Date
- B: Counterparty / description
- C: Debit / credit
- D: Gross amount (INR)
- E: Taxable value (INR), from the invoice
- F: GST amount (INR), from the invoice, or computed for reverse charge
- G: GST rate (merit, standard, de-merit, exempt, nil, reverse charge, excluded)
- H: Tax type (CGST plus SGST / IGST / RCM-IGST / RCM-CGST plus SGST / nil / excluded)
- I: GSTR-3B table (3.1(a), 3.1(b), 3.1(c), 3.1(d), 4(A)(1) to 4(A)(5), 4(B)(2), 4(D)(2), excluded)
- J: GSTR-1 table (4A, 4B, 5, 6, 7, 8, 9B, excluded)
- K: In GSTR-2B? (Y / N / not applicable)
- L: Default? (Y / N)
- M: Question / notes

Leave G to K blank for excluded rows.

### Sheet "GSTR-2B reconciliation"

One row per purchase invoice: supplier GSTIN, invoice number, date, taxable value, IGST, CGST, SGST per books; the same per GSTR-2B; status (matched, books only, GSTR-2B only, ITC not available); action (claim, hold, ask supplier, reverse). Totals of "matched" plus import-of-services credit feed table 4(A).

### Sheet "GSTR-3B summary"

One row per table. Column A = table number, B = description, C = taxable value, D = IGST, E = CGST, F = SGST.

~~~
| 3.1(a) | Outward taxable (other)       | =SUMIFS(...) | ... |
| 3.1(b) | Outward taxable (zero-rated)  | =SUMIFS(...) | ... |
| 3.1(c) | Other outward (nil/exempt)    | =SUMIFS(...) | ... |
| 3.1(d) | Inward (reverse charge)       | =SUMIFS(...) | ... |
| 4(A)   | ITC available, rows (1)-(5)   | =SUMIFS(...) | ... |
| 4(B)   | ITC reversed                  | =SUMIFS(...) | ... |
| 4(C)   | Net ITC                       | =4(A)-4(B)   | ... |
| 4(D)   | ITC not available             | =SUMIFS(...) | ... |
~~~

### Sheet "Tax computation"

~~~
Output tax on outward supplies, by head = from 3.1(a) and 3.1(b) (if IGST paid)
Reverse-charge tax, by head             = from 3.1(d), paid in CASH only

Use of credit (Section 5.8):
  IGST credit -> IGST first; balance -> CGST and SGST in any order
  CGST credit -> CGST, then IGST (only after IGST credit is used up); never SGST
  SGST credit -> SGST, then IGST (only if no CGST credit is left for it); never CGST

Cash payable by head = output tax not covered by credit + reverse-charge tax
~~~

### Colour and formatting conventions

Blue for values typed from the bank statement or invoice. Black for formulas. Green for cross-sheet references. Yellow background for any row where Default? = "Y". Red text for any blocked-ITC row (section 17(5)).

### Mandatory recalc step

After building the workbook, run:

~~~bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/india-gst-PERIOD-working-paper.xlsx
~~~

Check the JSON output. If `status` is `errors_found`, fix the formulas and run it again.

## Section 8: Indian bank statement reading guide

Follow the universal exclusion rules, plus these India-specific patterns.

### HDFC Bank statement format

Typical CSV columns: Date, Narration, Chq/Ref No, Value Dt, Withdrawal Amt, Deposit Amt, Closing Balance. Date format DD/MM/YY or DD/MM/YYYY. The narration carries the counterparty, often in short form: "NEFT/RTGS/IMPS-[IFSC]-[Sender name]", "UPI-[UPI ID]-[Name]", "POS [Merchant]-[Terminal ID]", "ATM-SELF", "BIL/ONL/[Biller name]".

**HDFC narration parsing rules:**
- `NEFT-UTIB0000XXX-JOHN DOE`: payment to or from John Doe via Axis Bank
- `UPI-rajesh@okhdfcbank-RAJESH KUMAR`: UPI payment to or from Rajesh Kumar
- `POS [terminal ID] AMAZON`: card purchase at Amazon
- `BIL/ONL/AIRTEL`: online bill payment to Airtel
- `INT.PD`: interest paid (exclude)
- `CHG-GST` or `SERVICE CHARGES`: bank charges; ITC only per the bank's GST invoice

### SBI statement format

Typical columns: Txn Date, Value Date, Description, Ref No/Cheque No, Debit, Credit, Balance. Description format: "INB/NEFT/[Ref]-[Name]", "ATM/SELF/[Branch]", "UPI/[ID]/[Name]", "SI-[Standing Instruction]".

### ICICI Bank statement format

Typical columns: S No, Value Date, Transaction Date, Cheque Number, Transaction Remarks, Withdrawal Amount (INR), Deposit Amount (INR), Balance (INR). Remarks format: "NEFT-[IFSC]-[Name]", "UPI/[Ref]/[Name]", "MMT/IMPS/[Ref]/[Name]", "POS/[Merchant]/[Location]".

### Common patterns across Indian bank statements

**UPI payments:** the most common. Always contains "UPI" and a UPI ID or reference; the name is usually extractable. UPI to an individual without a GSTIN: likely personal or an unregistered supplier; Tier 2 question needed.

**NEFT/RTGS/IMPS:** business payments. The IFSC code identifies the counterparty's bank branch. Large RTGS payments are likely business transactions.

**Card transactions (POS/online):** merchant name embedded but often cut short. "POS" plus a card or terminal number with no name: ask the client.

**Standing instructions (SI/ECS/NACH):** recurring debits for EMI, insurance, subscriptions. Pattern: "ECS/NACH-[Mandate]-[Payee]".

**Internal transfers and exclusions:**
- Own-account transfers: "TRF-OWN", "SELF TRANSFER", "FD CREATION"
- Mutual fund SIPs: "BSE-MF-[Fund name]": investment, exclude
- FD maturity or creation: "FD-[number]": exclude
- ATM self-withdrawal: "ATM-SELF", "ATM WDL": exclude as drawing

**Refunds and reversals:** "REVERSAL", "REFUND", "RETURN-NEFT". For GST, a refund from a supplier needs the supplier's credit note; reduce ITC in the period the credit note is reported, not by changing the original period.

**Salary payments:** "PAYROLL", "SALARY-[month]", many outgoing payments to individuals on one date. Exclude.

**Loan disbursement or repayment:** "LOAN DISB", "EMI-[Account]". Exclude.

**Foreign currency:** some banks show "FCY-USD-[amount]" in the narration. The taxable value of an import of services for reverse charge is the value of the supply; record the rupee amount and rate shown on the statement in column M and let the reviewer confirm the conversion rule.

## Section 9: Onboarding fallback (only when inference fails)

Infer the client profile from the data first. Ask only when inference fails.

### 9.1 Legal name and GSTIN

Inference: the GSTIN sometimes appears in NEFT narrations or on invoices. Check the shape: 15 characters, being the two-digit State code, the ten-character PAN, an entity code, the letter Z and a check character (format of the registration certificate, GST REG-06; carried from the earlier Guide `in-gst-return`, not re-read for this version). Fallback question: "What is your GSTIN?"

### 9.2 Registration type

Inference: a request for GSTR-3B or GSTR-1 means a regular taxpayer. CMP-08 or GSTR-4 means composition: R-IN-1 refuses. Fallback question: "Are you a regular GST taxpayer or under the composition scheme?"

### 9.3 State of registration

Inference: the State code at the start of the GSTIN; the IFSC branch location. Fallback question: "Which State is your GST registration in?" (This also sets the QRMP GSTR-3B date group in Section 5.10.)

### 9.4 Filing period and frequency

Inference: first and last transaction dates. Monthly filers: one month. QRMP filers: a full quarter. Fallback question: "Which period does this cover? Monthly or quarterly (QRMP)?"

### 9.5 Business activity

Inference: counterparty mix, sales descriptions, HSN/SAC on invoices. Fallback question: "In one sentence, what does the business do?"

### 9.6 Inter-State supplies

Inference: buyers' or suppliers' GSTINs from other States, IGST on invoices. Fallback question: "Do you sell to buyers in other States? Which ones?"

### 9.7 Exports

Inference: foreign currency receipts, "FIRC" or "EXPORT" in narrations. Fallback question: "Do you export goods or services? Is a Letter of Undertaking (RFD-11) filed for this financial year?"

### 9.8 Reverse charge purchases

Inference: payments to advocates, transporters, security agencies, foreign suppliers, directors, unregistered landlords. Fallback question: "Do you buy from advocates, goods transport agencies, non-corporate security agencies, foreign suppliers or unregistered landlords? Do you pay sitting fees to directors?"

### 9.9 E-invoicing

Inference: prior-year GSTR-9 or stated turnover. Fallback question: "Has your aggregate turnover crossed the e-invoicing threshold (Section 5.5) in any financial year from 2017-18 onwards?"

### 9.10 ITC brought forward

Not inferable from one period. Always ask: "What are your electronic credit ledger balances (IGST, CGST, SGST separately) at the start of the period?"

## The method, step by step

1. **Confirm scope.** Regular taxpayer, one GSTIN, no composition, ISD, e-commerce operator or SEZ supplies (Section 2, refusals). Check the period is within three years of its due date (CGST Act sections 37(5), 39(11), 44(2): https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section39_v1.00.html).
2. **Fix the frequency and the due dates.** Monthly or QRMP (rule 61A: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61a_v1.00.html); GSTR-1 date from Notification 83/2020-Central Tax and GSTR-3B date from rule 61 (Section 5.10).
3. **Classify every bank line.** Use the pattern library (Section 3), then the rules (Section 5), then Tier 2 (Section 6). Record rate, tax head, GSTR-3B and GSTR-1 table per line (Section 7).
4. **Build outward supplies for GSTR-1.** B2B invoice by invoice (table 4A/4B); inter-State B2C above the B2C large limit invoice by invoice (table 5); other B2C rate-wise (table 7); exports (table 6); credit and debit notes (table 9B); HSN summary (table 12) with the digits required by turnover (rule 59: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule59_v1.00.html , Notification 78/2020-Central Tax). File by the GSTR-1 date. Correct any omission in GSTR-1A before filing GSTR-3B.
5. **Reconcile ITC with GSTR-2B.** Follow Section 5.6: claim only what GSTR-2B shows (rule 36(4): https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter5/rule36_v1.00.html), plus import-of-services credit in 4(A)(2); drop blocked credits (section 17(5)); reverse for unpaid suppliers (rule 37) and for suppliers who never filed GSTR-3B (rule 37A, https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter5/rule37a_v1.00.html); reverse the exempt share (rules 42 and 43).
6. **Self-assess reverse charge.** Import of services and domestic reverse-charge services (Sections 5.3 and 5.4; Notification 13/2017-Central Tax (Rate): https://gstcouncil.gov.in/sites/default/files/2024-05/download_8_0.pdf). Declare in 3.1(d); pay in cash; take credit in 4(A)(2) or 4(A)(3).
7. **Compute the liability and the use of credit.** Apply section 49(5) and rule 88A (Section 5.8: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter10/section49_v1.00.html). Check GSTR-3B output tax against GSTR-1 so that no DRC-01B difference arises (rule 88C).
8. **File GSTR-3B and pay** by the GSTR-3B date (rule 61: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html). QRMP filers pay months 1 and 2 by PMT-06. If late: add the late fee (Section 5.10, central tax plus the same under the SGST Act) and interest on the cash part of the tax (section 50: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter10/section50_v1.00.html).
9. **Year end.** By 30 November after the year end: take any missed ITC for that year, correct GSTR-1 and GSTR-3B errors, complete rule 37A reversals (section 16(4): https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html). Before the September return: the rule 42 and 43 annual true-up. By 31 December: GSTR-9, and GSTR-9C if aggregate turnover exceeds the limit (rule 80: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule80_v1.00.html). Check whether an optional-filing notification exists for the year before skipping GSTR-9.
10. **Write the reviewer brief.** List every default, every Tier 2 question, every blocked credit, every GSTR-2B mismatch held back, and any 57th Council change the client asks about (pending, Section 5.16).

## Ask the client first

- Are you registered as a regular taxpayer or under composition, and do you hold more than one GSTIN? (Composition or several GSTINs changes the returns entirely.)
- In which State is your principal place of business, and do you file monthly or quarterly (QRMP)? (Sets the GSTR-3B due date group and the PMT-06 payments.)
- What was your aggregate turnover last financial year, and so far this year? (Sets QRMP eligibility, late fee caps, HSN digits, e-invoicing and GSTR-9C.)
- Do you buy anything from abroad, from advocates, transporters, non-corporate security agencies or unregistered landlords, or pay directors? (Reverse charge.)
- Do you export, and is an LUT filed for this financial year? (Zero-rating without tax, or not.)
- Have all suppliers been paid within one hundred and eighty days of their invoices, and do you have GSTR-2B for each month? (ITC reversals and what may be claimed.)

## When to refuse or refer

- Any refusal trigger R-IN-1 to R-IN-6 in Section 2.
- A sale whose rate cannot be found in the rate notification, or a supply that straddles 22 September 2025 or 1 February 2026.
- A notice in DRC-01B, DRC-01C or any section 73, 74 or 74A notice: refer; the seven-day reply window in rules 88C and 88D is short.
- Export on payment of IGST, or any refund claim (RFD-01).
- Place of supply disputes for services (IGST Act sections 12 and 13), especially cross-border.
- The annual rule 42/43 true-up, GSTR-9 and GSTR-9C: prepare the working, but the accountant signs off.
- A client asking to apply a 57th Council recommendation now: refuse until it is notified (Section 5.16).

## Section 10: Reference material

### Validation status

Team rewrite of October 2026. Every figure was re-proven on a CBIC or GST Council page saved on 16 and 17 October 2026, and every rule sentence names its section or rule. Rates follow the 56th GST Council structure (in force 22 September 2025; tobacco 1 February 2026). Notifications served only as unreadable files by CBIC (including the rate schedules 9/2025, 19/2025 and 01/2026-Central Tax (Rate)) were not read; where a rule depends on one, the Guide says so.

### Known gaps

1. The pattern library covers common Indian and foreign vendors only. Add patterns as they emerge.
2. The worked examples use one hypothetical Mumbai IT consultant. Manufacturing, trading and hospitality are not covered.
3. HSN/SAC classification needs the rate notifications; this Guide does not hold the HSN/SAC master. Flag unknown classifications as Tier 2.
4. Place of supply for services (IGST Act sections 12 and 13) is often disputed. Flag cross-border or multi-State cases as Tier 2.
5. Supplies that straddle the 22 September 2025 or 1 February 2026 start dates need the time-of-supply rules; refer.
6. The current rate notifications (9/2025, 19/2025, 01/2026 and 10/2025-Central Tax (Rate)) could not be read; 01/2026 of 30 April 2026 amends 9/2025 and may have moved individual rate entries.
7. E-invoicing detail (exemptions, reporting time limits) is left to `india-einvoice`; the years that count are in Section 5.5.
8. The GSTR-9 optional-filing limit is notified year by year; only financial year 2022-23 is proven here.

### PROHIBITIONS

- NEVER allow ITC on blocked credits under section 17(5), whatever the business use, unless the clause's own exception applies.
- NEVER apply CGST plus SGST to an inter-State supply, or IGST to an intra-State supply.
- NEVER guess an HSN/SAC code or a rate. Classification is checked against the rate notification.
- NEVER claim ITC that is not in GSTR-2B, except import-of-services credit in table 4(A)(2).
- NEVER pay reverse-charge tax with ITC. It is paid in cash.
- NEVER claim ITC after 30 November following the end of the financial year (or after GSTR-9 is filed, if earlier). A re-claim of credit reversed earlier (rule 37) is outside this limit (rule 37(4)).
- NEVER classify a mixed supply as composite to reach a lower rate.
- NEVER ignore the order of credit use (IGST credit first, in full).
- NEVER issue a B2B invoice without IRN and QR code where e-invoicing applies.
- NEVER treat an export as zero-rated without an LUT or bond, or proof of IGST paid under a notified class.
- NEVER present a 57th GST Council recommendation as law.
- NEVER compute a figure from two others: no combined central-plus-State late fee, no effective rate. Arithmetic in the working paper is done by the spreadsheet engine.

### Change log

- **October 2026 (team rewrite):** rates moved to the 56th Council structure with start dates; electricity and individual life and health insurance corrected to exempt; GSTR-1 B2C large limit corrected; late fees rewritten as central tax with the turnover-band caps and the GSTR-9 bands; ITC conditions expanded (GSTR-2B, rules 36(4), 37, 37A, 88C, 88D); section 17(5) rewritten from the current text; credit use order corrected under rule 88A; import-of-services credit moved to table 4(A)(2); export on payment of IGST limited to notified classes; QRMP, IFF, GSTR-1A and the three-year bar added; residential and commercial rent reverse charge added; 57th Council recommendations marked pending.
- **31 October 2026 (v2.1, merge):** the duplicate Guide `in-gst-return` (the April 2026 v2.0 text this Guide was rewritten from) was merged in and retired. Added from it, each re-proven on an official page on 31 October 2026: security services under reverse charge (Notification 29/2018-Central Tax (Rate)), the e-invoicing years test (Notification 70/2020-Central Tax), named 40%, 5% and nil items from the 56th Council press release, the GSTIN format check, and the portal addresses. Not carried over: its 12% and 28% slabs, electricity at 18%, combined central-plus-State late fees with the old INR 10,000 cap, the INR 2.5 lakh B2C large limit, the IGST-then-CGST-then-SGST credit order, the "transport of goods" motor vehicle exception, and the computed tax figures in its worked examples; each is superseded or wrong, as this Guide's sections note.
- **v2.0 (April 2026):** Rewrite to the three-tier structure (quick reference, supplier pattern library, worked examples, Tier 1 and Tier 2 rules, working paper, bank statement guide, onboarding fallback, five refusals).
- **v1.0 (April 2026):** Initial version.

## Sources

Items 1 to 6 were read on 16 or 17 October 2026; items 7 and 8 on 31 October 2026, when `in-gst-return` was merged into this Guide; item 9 was not read.

1. CGST Act 2017, consolidated sections (CBIC tax repository): section 9 https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter3/section9_v1.00.html ; section 16 (link in Section 5.6); section 17 (link in Section 5.7); section 22 (link in Section 5.13); section 37 https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section37_v1.00.html ; section 39 (link in the method); section 44 https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section44_v1.00.html ; section 47 (link in Section 5.10); section 49 and section 50 (links in the method); section 2 https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter1/section2_v1.00.html
2. IGST Act 2017: section 5 (link in Section 5.2); section 14 https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_IGST_Act/active/chapterv/section14_v1.00.html ; section 16 https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_IGST_Act/active/chaptervii/section16_v1.00.html
3. CGST Rules 2017: rules 36, 37A, 59, 61, 61A, 80, 88A, 138 (links above); rule 37 https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter5/rule37_v1.00.html ; rule 42 https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter5/rule42_v1.00.html ; rule 43 https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter5/rule43_v1.00.html ; rule 46 https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule46_v1.00.html ; rule 60 https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule60_v1.00.html ; rule 88C https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter9/rule88c_v1.00.html ; rule 88D https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter9/rule88d_v1.00.html ; rule 96A https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter10/rule96a_v1.00.html
4. GST Council: 56th meeting press release and FAQ; December 2025 newsletter; 57th meeting press release (links in Sections 1 and 5.16).
5. Notifications (GST Council copies): 2/2017, 13/2017, 05/2022, 15/2022, 09/2024 and 07/2025-Central Tax (Rate); 13/2017, 4/2018, 76/2018, 78/2020, 83/2020, 19/2021, 20/2021, 07/2023, 10/2023, 32/2023 and 12/2024-Central Tax (links in the tables above).
6. CBIC, "GST: An Update" (1 June 2019): https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf
7. Notifications added at the merge: 29/2018-Central Tax (Rate), security services under reverse charge (link in Section 5.4); 70/2020-Central Tax, e-invoicing years test (link in Section 5.5).
8. Portals: GST common portal https://www.gst.gov.in ; Invoice Registration Portal (e-invoice) https://einvoice1.gst.gov.in ; e-way bill https://ewaybillgst.gov.in
9. Named by the earlier Guide `in-gst-return` and not read for this version: Circular 98/17/2019-GST (order of credit use; rule 88A is used above instead), Circular 140/10/2020-GST (director services under reverse charge), Circular 164/20/2021-GST (restaurant services), Notification 10/2017-Integrated Tax (Rate) (import of services under reverse charge), Notification 84/2020-Central Tax (QRMP entry test).

Related Guides: `india-einvoice` (e-invoicing), `in-tds-freelance` (TDS on contractor and professional payments), `in-income-tax` (income tax), `in-return-assembly` (full filing package).

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained on the OpenAccountants site. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
