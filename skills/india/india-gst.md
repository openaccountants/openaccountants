---
name: india-gst
description: >
  Use this skill whenever asked to prepare, review, classify or advise on India's Goods
  and Services Tax (GST) for FY 2026-27, for a self-employed individual, freelancer or
  small business with one GSTIN. Trigger on phrases like GST return, GSTR-1, GSTR-3B,
  GSTR-9, GSTR-2B, file GST, GST classification, HSN code, SAC code, input tax credit,
  ITC, reverse charge, IGST, CGST, SGST, GST registration threshold, QRMP, e-way bill,
  LUT export, GST late fee, GST rates after 22 September 2025, 5% 18% 40% GST, or any
  question about GST compliance in India. It covers the 56th GST Council rate structure
  in force from 22 September 2025, CGST and SGST or IGST, domestic and import reverse
  charge, e-invoicing scope, ITC conditions and blocked credits, return due dates and
  late fees, exports and SEZ, e-way bills, registration thresholds, QRMP, a supplier
  pattern library and bank statement reading guide. Tier 2, not reviewed by an
  accountant.
version: "3.1"
jurisdiction: IN
tax_year: 2026
tax_year_notes: "FY 2026-27 (1 April 2026 to 31 March 2027); law in force on 22 November 2026"
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# India GST: Monthly and Quarterly Returns, Annual Return and Input Tax Credit for a Single-GSTIN Business, FY 2026-27

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in India.

This skill covers GST for a regular registered business with one GSTIN in one State. It covers classification, GSTR-1, GSTR-3B, input tax credit (ITC) and GSTR-9 under the law in force on 22 November 2026. Returns run by month or quarter; the financial year runs from 1 April to 31 March. See Section 5.16 for the commencement of changes following the 57th GST Council meeting.

## Who this applies to

### Quick reference

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

#### GST rates from 22 September 2025

The 56th GST Council meeting (3 September 2025) replaced the old four-slab structure with two main rates and a special de-merit rate ("Rationalisation of the current 4-tiered tax rate structure"). The old middle and top general slabs no longer exist; items moved to the rates in the table below. The legal rate schedule is Notification 9/2025-Central Tax (Rate), which the official repository serves only in a form this skill could not read; the Council's release and FAQ below are the sources used. All rates in this table are the total GST on the supply (CGST plus SGST, or IGST), not the central share.

Further items the same press release names. The earlier Guide `in-gst-return` listed them as slab examples without quotes; they were re-read on the press release on 31 October 2026. Pan masala moves on 1 February 2026 (start-date rows above); the rest on 22 September 2025.

Electrical energy is exempt under Notification 10/2025-Central Tax (Rate), serial 111.

Rates for items not in these tables (telecom, software, professional services, rail travel, restaurants, hotels above the hotel value in the table above) are not printed on any page this skill could read. For a purchase, take the tax the supplier charged on its tax invoice. For a sale, find the item's rate in the rate notification before invoicing; do not guess (Section 10, PROHIBITIONS).

**Key GSTR-3B tables**

Use the prescribed forms. The GSTR-2B instructions and amendments to GSTR-1 and GSTR-3B are in Notification 12/2024-Central Tax.

| Table | Meaning |
| --- | --- |
| 3.1(a) | Outward taxable supplies (other than zero-rated, nil-rated, exempted) |
| 3.1(b) | Zero-rated outward supplies: exports and supplies to SEZ units or developers for authorised operations |
| 3.1(c) | Other outward supplies (nil-rated, exempted) |
| 3.1(d) | Inward supplies liable to reverse charge: the tax on them is declared here for payment |
| 3.1(e) | Non-GST outward supplies |
| 3.1.1(ii) | Taxable value of supplies made as a registered supplier through an e-commerce operator where the operator pays under section 9(5) |
| 3.2 | Inter-State supplies to unregistered persons, composition taxpayers, UIN holders |
| 4(A)(1) | ITC on import of goods |
| 4(A)(2) | ITC on import of services (reverse charge); this credit is not in GSTR-2B and is entered by the taxpayer |
| 4(A)(3) | ITC on inward supplies liable to reverse charge (other than imports), taken after the tax is paid |
| 4(A)(4) | ITC from an Input Service Distributor |
| 4(A)(5) | All other ITC (supplies from registered persons other than reverse charge) |
| 4(B)(2) | ITC reversed, including the rule 37A reversal (Section 5.6) |
| 4(D)(2) | Ineligible ITC under section 16(4) and ITC restricted due to place-of-supply rules |
| 5.1 | Interest and late fee payable |
| 6.1 | Payment of tax: cash and ITC, by tax head |

**Key GSTR-1 tables**

Table numbers follow the GSTR-1A instructions in Notification 12/2024-Central Tax (link above), which use the GSTR-1 table numbers.

| Table | Meaning |
| --- | --- |
| 4A / 4B | Supplies to registered persons (B2B): 4A other than reverse charge; 4B supplies attracting reverse charge |
| 5 | Inter-State supplies to unregistered persons with invoice value above the B2C large limit (Section 5.10) |
| 6 | Exports and supplies to SEZ units or developers, deemed exports |
| 7 | Intra-State supplies to unregistered persons at any value and inter-State supplies to unregistered persons up to and including the B2C large limit, consolidated as prescribed |
| 8 | Nil-rated, exempted and non-GST supplies |
| 9A / 9C | Amendments of earlier B2B, B2C large, export, and credit or debit note details |
| 9B | Credit and debit notes |
| 12 | HSN-wise summary of outward supplies |
| 14 | Supplies made through e-commerce operators by the supplier, including taxable value where the operator pays under section 9(5) |
| 14 / 14A / 15 | Supplies through e-commerce operators |

**Handling missing facts**

| Unresolved item | Treatment |
| --- | --- |
| GST rate on a sale | Confirm the HSN/SAC and current rate entry before computing tax |
| GST status of a purchase | Hold the credit until its eligibility is documented |
| Counterparty State or place of supply | Check the supplier's location and statutory place of supply before selecting the tax head |
| Buyer's GST registration | Confirm registration and GSTIN before reporting B2B or B2C |
| Unknown business-use share (vehicle, phone, home office) | No ITC |
| SaaS billing entity | Obtain the invoice and verify the conditions for import of services |
| Blocked-credit status | Hold the credit until the facts and any statutory exception are confirmed |
| Transaction scope | Establish what the transaction pays for before including it in the return |


**Red flags for the reviewer brief**

Flag any material unclassified transaction or credit, significant counterparty concentration or unusual net GST position in the reviewer brief.

## Rates, bands and thresholds

Every figure with its official source on the row. Subsection numbers (5.2, 5.5 and so on) match the rule sections under The base, Deadlines and filing and Cross-border points.

### GST rates from 22 September 2025

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Standard rate | 18% | 9% central tax on notified goods or services, plus the corresponding State or UT tax, or 18% IGST | https://egazette.gov.in/WriteReadData/2025/266209.pdf#page=76 |
| Merit rate | 5% | 2.5% central tax or 5% IGST under the applicable schedule | same |
| Special rate | 40% | 20% central tax or 40% IGST where the applicable schedule provides it | same |
| Goods and services rate changes | 22 September 2025 | Check the tariff entry, including the goods temporarily in the 28% schedule until 1 February 2026. Other goods rates include 3%, 0.25% and 1.5% | https://egazette.gov.in/WriteReadData/2025/266220.pdf#page=9 |

| Individual life insurance, health insurance and their reinsurance | Exempt from 22 September 2025 | Includes family floater and senior citizen policies given the insured meets the definition of individual. Group policies follow their own treatment | https://egazette.gov.in/WriteReadData/2025/266220.pdf#page=53 |

| Hotel accommodation at or below INR 7,500 per unit per day or equivalent | 5% | From 1 November 2026 the hotel may take credit on same-line hotel accommodation inputs, capped at 2.5% CGST on their value and subject to the other ITC conditions | https://egazette.gov.in/WriteReadData/2026/277456.pdf#page=6 |
| Hotel accommodation above INR 7,500 per unit per day or equivalent | 18% | Ordinary ITC conditions apply | https://gstcouncil.gov.in/sites/default/files/2024-02/gstservicerates.pdf |
| Gyms, salons, barbers, yoga centres and similar physical well-being services | 5% | Supplier ITC condition applies under the rate entry | https://egazette.gov.in/WriteReadData/2025/266220.pdf#page=9 |
| Cement | 18% | Heading 2523, check the current tariff description | https://egazette.gov.in/WriteReadData/2025/266209.pdf#page=76 |
| Air transport of passengers in other than economy class | 18% | See heading 9964 and its specific entries | https://egazette.gov.in/WriteReadData/2025/266220.pdf#page=9 |
| Passenger transport by motor vehicle with fuel included | 5% or 18% | The 5% entry restricts supplier credit to qualifying same-line input services. Check the current conditions in heading 9964 | https://egazette.gov.in/WriteReadData/2026/277456.pdf#page=6 |
| Goods transport agency (GTA) | 5% or 18% | Check the GTA's forward-charge election. The 5% rate restricts supplier credit | https://egazette.gov.in/WriteReadData/2025/266220.pdf#page=9 |
| Delivery services other than postal and courier | 5% from 1 November 2026 | The rate entry disallows ITC on the inputs used to supply delivery. For supply through an e-commerce operator, the operator pays under section 9(5) unless the supplier is liable to register under section 22(1) | https://egazette.gov.in/WriteReadData/2026/277456.pdf#page=8 |
| Restaurant services outside specified premises | 5% | From 1 November 2026, the supplier may take qualifying credit for restaurant services procured from another supplier outside specified premises. A stand-alone restaurant cannot declare itself as specified premises | https://egazette.gov.in/WriteReadData/2026/277456.pdf#page=6 |
| Optional simplified registration (rule 14A): output tax on supplies to registered persons per month not above | INR 2.5 lakh | "will not exceed Rs. 2.5 lakh per month (inclusive of CGST, SGST/UTGST and IGST)"; operational "from 1st November, 2025" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Specified aerated, sweetened, flavoured, caffeinated and carbonated fruit beverages under heading 2202 | 40% | Check the current tariff line and Schedule I exclusions before assigning the rate | https://egazette.gov.in/WriteReadData/2025/266209.pdf#page=124 |
| Other non-alcoholic beverages under heading 2202 | 40% where included in Schedule III | Check Schedule I exclusions and the amended tariff codes | https://taxinformation.cbic.gov.in/view-pdf/1010641/ENG/Notifications |
| Specified admission and race-club services | 40% | Check the classification and exemption schedule for the particular event | https://egazette.gov.in/WriteReadData/2025/266220.pdf#page=9 |
| Specified actionable claims, including betting, gambling, horse racing, lottery and online money gaming | 40% | Apply the valuation and reporting rules for the specific activity | https://egazette.gov.in/WriteReadData/2025/266209.pdf#page=124 |
| Leasing or renting goods without an operator where the rate follows the goods | 40% if the corresponding goods rate is 40% | Check the service entry for the contract | https://egazette.gov.in/WriteReadData/2025/266220.pdf#page=9 |
| Listed lifesaving drugs and medicines | Exempt | Check the named drugs and conditions in the exemption schedule | https://egazette.gov.in/WriteReadData/2025/266210.pdf#page=20 |
| Other drugs and medicines covered by the 5% schedule | 5% | Check the tariff entry and available exemptions | https://egazette.gov.in/WriteReadData/2025/266209.pdf#page=76 |
| Listed handicrafts, marble and travertine blocks, granite blocks and intermediate leather goods | 5% | Check the individual tariff entry | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Air travel, economy class | 5% | "if travel is by economy class then rate of GST is 5% otherwise the GST rate will be 18%" | https://gstcouncil.gov.in/sites/default/files/2025-09/faq_0.pdf |
| Air travel, any other class | 18% | "if travel is by economy class then rate of GST is 5% otherwise the GST rate will be 18%" | same |
| Small petrol/LPG/CNG cars up to 1,200 cc and 4,000 mm, and diesels up to 1,500 cc and 4,000 mm | 18% | Both the applicable engine and length conditions must be met | https://egazette.gov.in/WriteReadData/2025/266209.pdf#page=118 |
| Other cars under heading 8703 subject to Schedule III | 40% | Check the exclusions and other entries, including 5% for qualifying electric vehicles. A petrol car above 1,200 cc can fall in Schedule III even at up to 4,000 mm | https://egazette.gov.in/WriteReadData/2025/266209.pdf#page=124 |
| Compensation cess on most goods | Ended; merged into the GST rate | "Since it has been decided to end the Compensation Cess levy, the Compensation Cess rate is being merged with GST" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Start date for pan masala, tobacco, cigarettes and bidi | 1 February 2026 | "A revised rate structure has been notified with effect from February 1st, 2026, whereby bidi has been brought under the 18% GST rate" | https://gstcouncil.gov.in/sites/default/files/2026-01/monthly_newsletter_december_2025_1_0.pdf |
| Pan masala, tobacco (other than bidi), cigarettes, nicotine-based inhalation products | 40% | "cigarettes and nicotine-based inhalation products have been placed under the 40% GST rate" | same |
| Bidi | 18% | "bidi has been brought under the 18% GST rate" | same |
| Compensation cess on specified pan masala and tobacco products | Withdrawn | "the levy of compensation cess on specified pan masala and tobacco products has been withdrawn" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Electrical energy (2716 00 00) | Exempt | Serial 111 of Notification 10/2025-Central Tax (Rate) | https://egazette.gov.in/WriteReadData/2025/266210.pdf#page=20 |

### India-specific refusal catalogue

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Composition turnover limit (preceding financial year), normal States | INR 1.5 crore | "Composition threshold limit increased to be Rs. 1.5 Crore" | https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf |
| Composition limit in Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, Tripura, Uttarakhand | INR 75 lakh | "have the said limit as Rs. 75 lakh" | same |
| Rate, manufacturers (total) | 1% | "Manufacturers 1%" | same |
| Rate, traders (total, on taxable supplies) | 1% | "specified Traders 1%" | same |
| Rate, restaurants (total) | 5% | "Restaurants 5%" | same |
| Services composition option (section 10(2A)), total rate | 6% | "with a tax rate of 6% (3% CGST +3% SGST)" | same |
| Services composition option, preceding-year turnover up to | INR 50 lakh | "having an Annual Turnover in the preceding Financial Year up to Rs. 50 lakhs" | same |
| Composition annual return GSTR-4 | 30 June following the financial year | Applies from FY 2024-25 under rule 62(1)(ii). FY 2026-27 is due 30 June 2027 | https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf |
| Quarterly payment (CMP-08) | 18th of the month after the quarter | "quarterly basis till 18th of the month succeeding such quarter" | same |

### 5.2 CGST plus SGST, or IGST

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| IGST rate ceiling | not exceeding forty per cent | "at such rates, not exceeding forty per cent., as may be notified" | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_IGST_Act/active/chapteriii/section5_v1.00.html |
| Reverse charge power | categories notified by the Government | "specify categories of supply of goods or services or both, the tax on which shall be paid on reverse charge basis by the recipient" | same |

### 5.4 Domestic reverse charge

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Goods transport agency (GTA) services to factories, societies, co-operatives, registered persons, body corporates, partnership firms, casual taxable persons (serial 1) | Reverse charge, unless the GTA opted for forward charge | "Supply of Services by a goods Goods (a) Any factory registered under or transport agency (GTA)" | https://gstcouncil.gov.in/sites/default/files/2024-05/download_8_0.pdf |
| Taxable legal services by an individual advocate or a firm of advocates to a business entity (serial 2) | Reverse charge | Check the serial 45 exemptions, including a business recipient whose prior-year turnover did not exceed its registration exemption threshold | https://gstcouncil.gov.in/sites/default/files/2024-05/download_8_0.pdf |
| Sponsorship supplied by a person other than a body corporate to a body corporate or partnership firm (serial 4) | Reverse charge | The supplier limitation applies from 16 January 2025 | https://gstcouncil.gov.in/sites/default/files/2025-01/ctr07-2025.pdf |
| Services by the Central or State Government, Union territory or local authority to a business entity (serial 5, as amended) | Reverse charge, with exclusions added since 2017 | "d by the Central Central Any business entity located in the Government" | same |
| Services supplied in the capacity of a director to the company or body corporate (serial 6) | Reverse charge | Employee salary and supplies in a private or personal capacity fall outside this entry | https://gstcouncil.gov.in/sites/default/files/2024-05/download_8_0.pdf |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Renting of a residential dwelling to a registered person (serial 5AA) | Reverse charge on the registered tenant | "5AA Service by way of renting of Any Any registered person.”; residential dwelling to a person registered person." | https://gstcouncil.gov.in/sites/default/files/2024-05/05_2022-ctr-eng_1.pdf |
| Start date | 18 July 2022 | "This notification shall come into force with effect from the 18th July, 2022" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Residential dwelling rented to a registered proprietor as his own residence, in a personal capacity and on his own account | Exempt (Notification 12/2017-Central Tax (Rate), serial 12, Explanation) | "the registered person is proprietor of a proprietorship concern and rents the residential dwelling in his personal capacity for use as his own residence" | https://gstcouncil.gov.in/sites/default/files/2024-05/15_2022-ctr-eng.pdf |
| Start date | 1 January 2023 | "come into force with effect from the 01 st day of January, 2023" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Renting of any property other than a residential dwelling by an unregistered person to a registered person (serial 5AB) | Reverse charge on the registered tenant | "Service by way of renting of any Any unregistered Any registered property other than residential" | https://gstcouncil.gov.in/sites/default/files/2024-10/ctr-09-2024.pdf |
| Start date | 10 October 2024 | "This notification shall come into force with effect from the 10th day of October, 2024" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Supply of security personnel by a person other than a body corporate to a registered person (serial 14) | Reverse charge | Excludes composition taxpayers and the specified government and local authority recipients registered solely for TDS | https://gstcouncil.gov.in/sites/default/files/2024-05/download_2024-05-17t161051.835.pdf |
| Security-services entry commenced | 1 January 2019 | See the notification for the scope and exclusions | same |

### 5.5 E-invoicing, invoices and HSN codes

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| E-invoice aggregate turnover test | Exceeds five crore rupees | Test the notified class and exclusions using preceding financial years from 2017-18 | https://gstcouncil.gov.in/sites/default/files/2024-05/10ct_eng.pdf |
| Start date | 1 August 2023 | "with effect from the 1 st day of August, 2023" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Turnover test: aggregate turnover in | any preceding financial year from 2017-18 onwards | "for the words “a financial year”, the words and figures “any preceding financial year from 2017-18 onwards” shall be substituted" | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-70-central-tax-english-2020.pdf |
| E-invoicing covers supplies | to a registered person, or for exports | "after the words “goods or services or both to a registered person”, the words “or for exports” shall be inserted" | same |
| Notification date | 30 September 2020 | "New Delhi, the 30th September, 2020" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Aggregate turnover in the preceding financial year up to five crore rupees | 4 digits (may be omitted on invoices to unregistered persons) | "1. Up to rupees five crores 4"; "may not mention the number of digits of HSN Code ... in respect of supplies made to unregistered persons" | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-78-central-tax-english-2020.pdf |
| More than five crore rupees | 6 digits | "2. more than rupees five crores 6" | same |

### 5.6 ITC: conditions, GSTR-2B reconciliation and time limit

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Last date to take ITC for an invoice or debit note | 30 November following the end of the financial year, or the date the annual return is filed, whichever is earlier | "after the 6 [thirtieth day of November] following the end of financial year to which such invoice or" ... "or furnishing of the relevant annual return, whichever is earlier" | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html |
| Payment to supplier due within | one hundred and eighty days from the invoice date | "within a period of one hundred and eighty days from the date of issue of invoice by the supplier" | same |

### 5.10 Return due dates and late fees: GSTR-1, GSTR-3B, GSTR-9

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| GSTR-1, monthly filers | eleventh day of the following month | "till the eleventh day of the month succeeding such tax period" | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-83-central-tax-english-2020.pdf |
| GSTR-1, quarterly (QRMP) filers | thirteenth day of the month after the quarter | "shall be extended till the thirteenth day of the month succeeding such tax period" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| GSTR-3B, monthly filers | twentieth day of the following month | "for each month, or part thereof, on or before the twentieth day of the month succeeding such month" | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html |
| GSTR-3B, QRMP, principal place of business in Chhattisgarh, Madhya Pradesh, Gujarat, Maharashtra, Karnataka, Goa, Kerala, Tamil Nadu, Telangana, Andhra Pradesh, Daman and Diu and Dadra and Nagar Haveli, Puducherry, Andaman and Nicobar Islands, Lakshadweep | twenty-second day of the month after the quarter | "Lakshadweep. twenty-second day of the month succeeding such quarter" | same |
| GSTR-3B, QRMP, principal place of business in Himachal Pradesh, Punjab, Uttarakhand, Haryana, Rajasthan, Uttar Pradesh, Bihar, Sikkim, Arunachal Pradesh, Nagaland, Manipur, Mizoram, Tripura, Meghalaya, Assam, West Bengal, Jharkhand, Odisha, Jammu and Kashmir, Ladakh, Chandigarh, Delhi | twenty-fourth day of the month after the quarter | "Ladakh, Chandigarh or Delhi. twenty-fourth day of the month succeeding such quarter" | same |
| QRMP monthly payment (PMT-06) for months 1 and 2 of the quarter | twenty fifth day of the following month | "by depositing the said amount in FORM GST PMT-06 , by the twenty fifth day of the month succeeding such month" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| GSTR-9 (annual return), due | 31 December after the end of the financial year | "electronically in FORM GSTR-9 on or before the thirty-first day of December following the end of such financial year" | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule80_v1.00.html |
| GSTR-9C (self-certified reconciliation statement), required when aggregate turnover in the financial year exceeds | five crore rupees | "whose aggregate turnover during a financial year exceeds five crore rupees, shall also furnish a self-certified reconciliation statement" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| GSTR-9 exemption from FY 2024-25 onwards | Aggregate turnover up to INR 2 crore in the relevant financial year | Notification 15/2025-Central Tax applies to the current year | https://egazette.gov.in/WriteReadData/2025/266213.pdf#page=3 |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| B2C large: inter-State invoice value to unregistered persons more than | one lakh rupees | "(ii) inter-State supplies with invoice value more than 10 [one lakh rupees] made to the unregistered persons" | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule59_v1.00.html |
| Invoice Furnishing Facility (IFF), months 1 and 2 of a quarter: upload window | 1st day to the 13th day of the following month | "from the 1st day of the month succeeding such month till the 13th day of the said month" | same |
| IFF cap per month | fifty lakh rupees | "up to a cumulative value of fifty lakh rupees in each of the months" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Statutory late fee, GSTR-1 and GSTR-3B (central tax) | one hundred rupees for every day | "shall pay a late fee of one hundred rupees for every day during which such failure continues subject to a maximum amount of five thousand rupees" | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section47_v1.00.html |
| Statutory maximum per return (central tax) | five thousand rupees | "subject to a maximum amount of five thousand rupees" | same |
| Statutory late fee, GSTR-9: maximum | a quarter per cent. of his turnover (in the State or UT) | "subject to a maximum of an amount calculated at a quarter per cent. of his turnover in the State or Union territory" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| GSTR-3B late fee per day after waiver (central tax) | twenty-five rupees for every day | "which is in excess of an amount of twenty-five rupees for every day during which such failure continues" | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-76-central-tax-english-2018.pdf |
| GSTR-3B, central tax payable nil | ten rupees for every day | "shall stand waived to the extent which is in excess of an amount of ten rupees for every day" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| GSTR-1 late fee per day after waiver (central tax) | twenty-five rupees for every day | "which is in excess of an amount of twenty-five rupees for every day during which such failure continues: Provided that where there are no outward supplies" | https://gstcouncil.gov.in/sites/default/files/2024-05/notification-4-2018-central_tax-english.pdf |
| GSTR-1, no outward supplies in the period | ten rupees for every day | "shall stand waived to the extent which is in excess of an amount of ten rupees for every day" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| GSTR-3B maximum, central tax payable nil | two hundred and fifty rupees | "Registered persons whose total amount of central tax Two hundred and payable in the said return is nil fifty rupees" | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-19-central-tax-english-2021.pdf |
| GSTR-3B maximum, aggregate turnover up to INR 1.5 crore | one thousand rupees | "2. Registered persons having an aggregate turnover of One thousand up to rupees 1.5 crores" | same |
| GSTR-3B maximum, aggregate turnover more than INR 1.5 crore and up to INR 5 crore | two thousand five hundred rupees | "Taxpayers having an aggregate turnover of more than Two thousand and rupees 1.5 crores and up to rupees 5 crores in the five hundred" | same |
| Turnover band boundary | INR 1.5 crore | "Registered persons having an aggregate turnover of One thousand up to rupees 1.5 crores" | same |
| Upper band boundary; above it the statutory maximum applies | INR 5 crore | "rupees 1.5 crores and up to rupees 5 crores" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| GSTR-1 maximum, nil outward supplies | two hundred and fifty rupees | "Registered persons who have nil outward supplies in Two hundred and the tax period fifty rupees" | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-20-central-tax-english-2021.pdf |
| GSTR-1 maximum, aggregate turnover up to INR 1.5 crore | one thousand rupees | "Registered persons having an aggregate turnover of One thousand up to rupees 1.5 crores" | same |
| GSTR-1 maximum, more than INR 1.5 crore and up to INR 5 crore | two thousand five hundred rupees | "Registered persons having an aggregate turnover of Two thousand and more than rupees 1.5 crores and up to rupees 5 crores five hundred rupees" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Turnover up to five crore rupees: per day | twenty-five rupees per day | "Twenty-five rupees per day, subject to a of up to five crore rupees in the relevant financial" | https://gstcouncil.gov.in/sites/default/files/2024-05/07_eng.pdf |
| Turnover up to five crore rupees: maximum | 0.02% of turnover in the State or UT | "maximum of an amount calculated at 0.02 per year. cent. of turnover in the State or Union territory" | same |
| Turnover above INR 5 crore and up to INR 20 crore | INR 50 per day, capped at 0.02% of turnover in the State or UT | Central tax component | same |
| Upper limit of the reduced fee | twenty crore rupees | "of more than five crores rupees and up to twenty amount calculated at 0.02 per cent. of turnover crore rupees" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Interest on late tax, section 50(1), per year | 18% | "Sub-section (1) of section 50 18" | https://gstcouncil.gov.in/sites/default/files/2024-04/notfctn-13-central-tax-english.pdf |
| Interest where ITC was wrongly availed and utilised, section 50(3), per year | 18% | Finance Act 2022 section 116 and the Sixth Schedule apply the rate retrospectively from 1 July 2017 | https://egazette.gov.in/WriteReadData/2022/234693.pdf#page=144 |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Statutory ceiling, section 50(1) | eighteen per cent. | "pay, on his own, interest at such rate, not exceeding eighteen per cent." | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter10/section50_v1.00.html |
| Statutory ceiling, section 50(3) | twenty-four per cent. | "at such rate not exceeding twenty-four per cent. as may be notified" | same |

### 5.12 E-way bill

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| E-way bill needed before moving goods of consignment value exceeding | fifty thousand rupees | "Every registered person who causes movement of goods of consignment value exceeding fifty thousand rupees" | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter16/rule138_v1.00.html |
| Validity, ordinary cargo | One day up to 200 km and one further day for each further 200 km or part | Oversize cargo and qualifying multimodal shipments with a ship leg use 20 km or part, under rule 138(10) | same |

### 5.13 Registration thresholds

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Register when aggregate turnover in a financial year exceeds (normal States) | twenty lakh rupees | "if his aggregate turnover in a financial year exceeds twenty lakh rupees" | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html |
| Special category States | ten lakh rupees | "he shall be liable to be registered if his aggregate turnover in a financial year exceeds ten lakh rupees" | same |
| Ceiling a State may set for suppliers of goods only | forty lakh rupees | "enhance the aggregate turnover from twenty lakh rupees to such amount not exceeding forty lakh rupees in case of supplier who is engaged exclusively in the supply of goods" | same |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Services (and mixed) suppliers | INR 20 lakh | "for suppliers of services would be Rs. 20 lakhs and Rs. 10 lakhs (for States of Manipur, Mizoram, Nagaland and Tripura)" | https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf |
| Services suppliers in Manipur, Mizoram, Nagaland, Tripura | INR 10 lakh | "Rs. 20 lakhs and Rs. 10 lakhs (for States of Manipur, Mizoram, Nagaland and Tripura)" | same |
| Goods-only suppliers, States that opted in | INR 40 lakh | "for the suppliers of goods would be Rs. 40 lakhs and Rs. 20 lakhs" | same |
| Goods-only suppliers excluded from the INR 40 lakh exemption | Apply the relevant ordinary threshold or compulsory registration rule | Notification 10/2019 excludes listed States and UTs, specified goods and persons needing registration under section 24 | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-10-central-tax-english-2019.pdf |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Time to apply for registration once liable (section 25(1)) | Thirty days | "within thirty days from the date on which he becomes liable to registration" | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section25_v1.00.html |

### 5.15 QRMP scheme (quarterly returns, monthly payment)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Turnover above which the person must move to monthly filing | INR 5 crore | "whose aggregate turnover exceeds 5 crore rupees during the current financial year, shall opt for furnishing of return on a monthly basis" | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61a_v1.00.html |

## The base

### Supplier pattern library (the lookup table)

Use the patterns to identify likely transactions. Match invoice, contract and relevant place-of-supply facts before assigning tax treatment.

Match the most specific bank description. 'ITC per invoice' means credit subject to the documentation, reconciliation and eligibility rules in Sections 5.6 and 5.7.

#### 3.1 Indian banks

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SBI, STATE BANK OF INDIA, HDFC BANK, ICICI BANK, AXIS BANK, KOTAK MAHINDRA, PNB, BANK OF BARODA, INDUSIND, YES BANK, IDFC FIRST | Bank charges: ITC per invoice | Check the bank's invoice or statement for the GST charged; claim only what it shows |
| INTEREST, BYAJ, INT PAID, INT RECD | EXCLUDE | Interest movement, no GST invoice |
| LOAN, EMI, PERSONAL LOAN, HOME LOAN | Split payment | Principal and exempt interest are excluded. Check whether the balance includes a taxable processing or other fee |
| FD, FIXED DEPOSIT, RD | EXCLUDE | Investment movement |

#### 3.2 Government payments

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GST PMT, GST PAYMENT, GST CHALLAN, GSTN | EXCLUDE | Tax payment to government |
| INCOME TAX, IT DEPT, TDS, ADVANCE TAX, CPC BANGALORE | EXCLUDE | Direct tax payment |
| MCA, ROC FEE, COMPANY AFFAIRS | Check the fee | Confirm the service and applicable government-service exemption |
| EPFO, PF, ESI, ESIC, PROVIDENT FUND | EXCLUDE | Statutory social security contribution |
| PROFESSIONAL TAX, PT PAYMENT | EXCLUDE | State professional tax |
| STAMP DUTY, REGISTRATION FEE (government) | Check the fee | Separate stamp duty from any registration service and verify the latter's exemption |
| MUNICIPAL, NAGAR NIGAM, PROPERTY TAX | Check the payment | Exclude property tax. Verify separately whether payment for a service is taxable |

#### 3.3 Telecom and utilities

| Pattern | Treatment | GSTR-3B table | Notes |
| --- | --- | --- | --- |
| JIO, RELIANCE JIO, AIRTEL, BHARTI AIRTEL, VI, VODAFONE IDEA, BSNL, MTNL | ITC per invoice | 4(A)(5) | Telecom service. Mixed personal use: apportion under section 17(1) |
| TATA POWER, ADANI ELECTRICITY, BSES, BESCOM, MSEDCL | Check the invoice | | Electrical energy is exempt. Classify ancillary supplies from their own entries and any applicable exemption |
| MAHANAGAR GAS, IGL, ADANI GAS | ITC per invoice | 4(A)(5) | Rate not proven on a readable page; use the invoice |
| WATER SUPPLY, JAL BOARD | EXCLUDE | | Municipal water |

#### 3.4 Insurance

| Pattern | Treatment | Notes |
| --- | --- | --- |
| LIC, LIFE INSURANCE CORP (individual policy) | EXCLUDE | Individual life insurance is exempt from 22 September 2025 (rate table above). Group policies are not covered by that exemption; ITC on life insurance is blocked anyway by section 17(5)(b)(i) unless the employer must provide it by law or it is used for an outward supply of the same category |
| STAR HEALTH, NIVA BUPA, CARE HEALTH (individual policy) | EXCLUDE | Individual health insurance is exempt from 22 September 2025. Health insurance ITC is blocked by section 17(5)(b)(i) with the same two exceptions |
| HDFC ERGO, ICICI LOMBARD, BAJAJ ALLIANZ, NEW INDIA ASSURANCE, UNITED INDIA (general insurance) | ITC per invoice, then check section 17(5)(ab) | General insurance of a car blocked under section 17(5)(a) is itself blocked by section 17(5)(ab) |

#### 3.5 SaaS and cloud billed by Indian entities

| Pattern | Billing entity | Treatment | Notes |
| --- | --- | --- | --- |
| AWS INDIA, AMAZON INTERNET SERVICES | Check the invoicing entity | ITC per invoice | Determine the supplier's location and the statutory place of supply before choosing the tax head |
| GOOGLE INDIA, GOOGLE CLOUD INDIA | Google India Pvt Ltd / Google Cloud India Pvt Ltd (IN) | ITC per invoice | Check the invoice carries an Indian GSTIN |
| ZOHO, ZOHO CORP | Zoho Corporation Pvt Ltd (IN) | ITC per invoice | Check State |
| FRESHWORKS | Freshworks Technologies Pvt Ltd (IN) | ITC per invoice | |
| MICROSOFT INDIA | Microsoft Corporation India Pvt Ltd (IN) | ITC per invoice | Check the invoice carries an Indian GSTIN |
| CLEARTAX, CLEAR | Clear (IN) | ITC per invoice | Accounting or compliance software |

#### 3.6 Foreign SaaS (reverse charge on import of services)

Use Section 5.3 to confirm a taxable import and the service rate. Pay reverse-charge IGST in cash and report it in GSTR-3B table 3.1(d). Eligible credit is entered in 4(A)(2). Vendor labels are prompts to check the invoice.

| Pattern | Billing entity | Treatment |
| --- | --- | --- |
| NOTION, NOTION LABS | See invoice | Test for taxable import |
| OPENAI, CHATGPT | See invoice | Test for taxable import |
| GITHUB | See invoice | Test for taxable import |
| ANTHROPIC, CLAUDE | See invoice | Test for taxable import |
| FIGMA | See invoice | Test for taxable import |
| CANVA | See invoice | Test for taxable import |
| SLACK | Slack Technologies (US) or a Salesforce entity | Check the billing entity |
| HUBSPOT | HubSpot Inc (US) | Check the billing entity |
| TWILIO | See invoice | Test for taxable import |

#### 3.7 Payment processors

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RAZORPAY, PAYTM, ONE97 COMMUNICATIONS, CASHFREE, INSTAMOJO, PHONEPE BUSINESS, CCAVENUE, BILLDESK | ITC per invoice | Gateway fees; check the supplier GSTIN State |
| STRIPE INDIA, STRIPE PAYMENTS INDIA | ITC per invoice | Indian entity |
| Foreign payment gateway fees | Check for taxable import under Section 5.3 | Determine the service classification and place of supply as well as the actual supplier |

#### 3.8 Travel

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INDIGO, INTERGLOBE AVIATION, AIR INDIA, SPICEJET, AKASA AIR, AIR INDIA EXPRESS | Economy 5%; any other class 18% | Rates from the GST Council FAQ in Section 1. ITC per invoice if business travel; travel benefits to employees on vacation are blocked (section 17(5)(b)(iii)) |
| Ride-hailing and vehicle hire | Check the invoice and eligibility | Passenger transport and vehicle hire have distinct entries. For hire, apply section 17(5)(b)(i) and its exceptions |
| IRCTC, INDIAN RAILWAYS | ITC per invoice | Rate not printed on a readable page |
| MAKEMYTRIP, GOIBIBO, YATRA | ITC per invoice | The platform fee and the underlying ticket or room are separate lines |
| HOTELS, OYO, TAJ, ITC HOTELS, LEMON TREE | ITC per invoice | Room value up to INR 7,500 per unit per day or equivalent is taxed at 5%, with restricted same-line supplier ITC from 1 November 2026. The higher band is 18% |

#### 3.9 Restaurants and food delivery

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SWIGGY, BUNDL TECHNOLOGIES, ZOMATO | Separate the charges | Apply the food and beverage block to the meal, subject to section 17(5)(b) exceptions. Classify any separate delivery service under its own entry |
| Restaurant (direct) | Hold ITC unless an exception applies | Apply section 17(5)(b) |

#### 3.10 Professional services

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CA, CHARTERED ACCOUNTANT, [name] & ASSOCIATES, CS, COMPANY SECRETARY, ARCHITECT, INTERIOR DESIGNER | ITC per invoice | Forward charge from a registered supplier |
| ADVOCATE, ADV, LAWYER, LAW FIRM | Check reverse charge | Check the legal-service classification and exemptions in Section 5.4 |
| CONSULTANT, CONSULTANCY | Verify the invoice | For a foreign supplier, test the conditions for a taxable import |
| DIRECTOR FEE, SITTING FEE | Reverse charge | Services by a director to the company (Section 5.4); salary under an employment contract is excluded instead |
| SECURITY SERVICES, SECURITY AGENCY, SECURITY GUARDS | Check reverse charge | Identify supply of personnel, whether the supplier is a body corporate and whether the registered recipient is excluded |

#### 3.11 Rent

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RENT (commercial property, registered landlord) | ITC per invoice | Forward charge |
| RENT (commercial property, unregistered landlord, registered tenant) | Reverse charge | From 10 October 2024 (serial 5AB); a tenant paying tax under composition is excluded (Section 5.4) |
| RENT (residential dwelling, registered tenant) | Reverse charge | From 18 July 2022 (serial 5AA). Exempt from 1 January 2023 where a proprietor rents the home in a personal capacity as his own residence, on his own account (Section 5.4) |
| RENT (residential dwelling, unregistered tenant) | Check exemption | Exemption ordinarily requires use as a residence |
| COWORKING, WEWORK, AWFIS, COWRKS, 91SPRINGBOARD | ITC per invoice | Workspace service |

#### 3.12 Salaries and wages (exclude entirely)

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES, STIPEND, PAYROLL, BONUS, GRATUITY, LEAVE ENCASHMENT | EXCLUDE | Employee pay; no supplier invoice and no GST |
| CONTRACTOR (individual, no GSTIN) | EXCLUDE from ITC; flag for TDS | No tax invoice from an unregistered supplier. For TDS on contractor payments see `in-tds-freelance` |

### Rules

Each rule names its legal source. Apply silently when the data is unambiguous.

#### 5.1 Rates

Use the notified HSN or SAC entry and effective date. For a change of rate, apply CGST Act section 14 to the dates of supply, invoice and payment.

#### 5.2 CGST plus SGST, or IGST

Central and State or UT tax generally apply to intra-State supplies and integrated tax to inter-State supplies. Determine the supplier's location and place of supply under IGST Act sections 7, 8 and 10 to 14, including exceptions for SEZ supplies.

| Scenario | Tax type |
| --- | --- |
| Supplier's location and place of supply in the same State | CGST plus SGST |
| Same Union territory (without legislature) | CGST plus UTGST |
| Different States | IGST |
| Import of goods | IGST through customs |
| Import of services by a business | IGST under reverse charge |
| Export, or supply to an SEZ unit or developer for authorised operations | Zero-rated (Section 5.11) |

An intra-State supply splits the rate equally between central tax and State or Union territory tax; IGST carries the whole rate.

| Total rate | CGST | SGST or UTGST | IGST | Source |
| --- | --- | --- | --- | --- |
| 18% | 9% | 9% | 18% | Notification 9/2025-Central Tax (Rate) and the integrated tax schedules, with corresponding State notifications |
| 5% | 2.5% | 2.5% | 5% | Same schedules |

Check the matching State notification for the specific supply.

Working check, not the legal test (the test is the supplier's location and the place of supply, IGST Act Chapter V): compare the State code at the start of the supplier's GSTIN with the client's. For a buyer with no GSTIN, use the place of supply rules, not the billing address alone. Online information and database access services from abroad to a person who is not registered (a "non-taxable online recipient") are taxed on the foreign supplier, not the customer (IGST Act section 14).

#### 5.4 Domestic reverse charge

For taxable notified supplies, self-assess at the applicable rate, pay in cash and report in table 3.1(d). Take eligible credit in 4(A)(3) after paying.

The GTA forward-charge option is in Notification 05/2022-Central Tax (Rate): the entry does not apply where the GTA has registered, opted to pay tax under forward charge, and declared so on its invoice.

Notification 07/2025-Central Tax (Rate) takes a tenant who pays tax under composition out of serial 5AB: "the words “other than a person who has opted to pay tax under composition levy” shall be inserted" (https://gstcouncil.gov.in/sites/default/files/2025-01/ctr07-2025.pdf).

Check the supplier and recipient exclusions for each entry in amended Notification 13/2017-Central Tax (Rate).

For qualifying fuel-included renting of passenger motor vehicles to a body corporate, Notification 08/2026-Central Tax (Rate) changes the supplier forward-charge exception from 6% to 9% CGST from 1 November 2026.

#### 5.5 E-invoicing, invoices and HSN codes

A supplier in the notified class must report covered invoices to the Invoice Registration Portal and include the required IRN and QR code. This covers supplies to registered persons and exports. Check the exempt supplier classes, reporting window and prescribed documents in `india-einvoice`.

Use only preceding financial years from 2017-18 for the turnover test.

HSN code digits on tax invoices, from 1 April 2021 (Notification 78/2020-Central Tax under rule 46):

HSN covers goods; services use the SAC codes of the services classification (chapter 99).

#### 5.6 ITC: conditions, GSTR-2B reconciliation and time limit

**Conditions (CGST Act section 16(2)), all of them:**
1. The business holds a tax invoice or debit note from a registered supplier (or another prescribed document, rule 36(1)).
2. For documents required to be furnished under section 37, the supplier has furnished them in GSTR-1, IFF or GSTR-1A, and the credit has been communicated in the recipient's GSTR-2B (section 16(2)(aa), rule 36(4)).
3. The goods or services have been received.
4. Any ITC communicated under section 38 is unrestricted (section 16(2)(ba)).
5. The tax has been paid to the Government. For reverse charge, verify the recipient's own payment.
6. The business has filed its own GSTR-3B (section 39 return).

**Reconciliation, every period:**
1. Reconcile the portal's GSTR-2B with books and prescribed documents. Check the generation date and the effect of any Invoice Management System actions for the period.
2. Apply the GSTR-2B condition to documents required under section 37. For imports of goods, verify the bill of entry under rule 36(1)(d). For imported services and eligible domestic reverse charge documented by self-invoice, verify the applicable document and tax payment before claiming. ISD credit is reported separately.
3. For an invoice required under section 37 that is absent from GSTR-2B, ask the supplier to report it and wait for it to be communicated within the credit time limit.
4. Invoice in GSTR-2B but not in the books: check whether it is a real purchase before claiming.
5. Hold unavailable or restricted ITC. Table 4(D)(2) identifies section 16(4) and place-of-supply ineligibility.
6. If ITC claimed in GSTR-3B exceeds GSTR-2B beyond the limit the Council sets, the portal sends Form DRC-01C; within seven days pay the excess with interest through DRC-03 or explain the difference (rule 88D).
7. If tax payable per GSTR-1 exceeds tax paid per GSTR-3B beyond the set limit, the portal sends Form DRC-01B; pay or explain within seven days (rule 88C).

**Reversals:**
- **Supplier not paid within 180 days of invoice** (section 16(2), rule 37): report a proportionate reversal or payment, with any applicable interest, in the following period's GSTR-3B. Reclaim upon paying the supplier. Reverse-charge supplies and prescribed deemed payments have separate treatment. Rule 37(4) excludes reclaims from the section 16(4) time limit.
- **Supplier furnished an invoice in GSTR-1, as amended by GSTR-1A if applicable, or IFF and missed its GSTR-3B** (rule 37A): test whether the return was filed by 30 September after the credit year. If missing then, reverse by 30 November. If the reversal is late, apply interest. Reclaim once the supplier files.
- **Common credit for taxable and exempt supplies**: reverse the exempt share under section 17(2) and rule 42 (inputs and input services) or rule 43 (capital goods). Rule 43 treats the useful life of capital goods as five years from the invoice date and spreads the credit monthly as "T m = T c / 60".
- **Depreciation on the tax**: if income tax depreciation is claimed on the tax component, no ITC on that tax (section 16(3)).

For FY 2026-27 invoices, claim by 30 November 2027 or the earlier date of filing the annual return. For FY 2025-26 use 30 November 2026 or its earlier annual filing date.

#### 5.7 Blocked credits: section 17(5)

Section 17(5) blocks the listed credits unless an exception applies. Section 17(1) limits mixed-use credit to business use and section 17(2) to taxable supplies, including zero-rated supplies.

| Clause | Blocked | Exception (ITC allowed only then) |
| --- | --- | --- |
| (a) | Motor vehicles for transporting persons with approved seating of not more than thirteen persons (including the driver) | Used for further supply of such vehicles, transport of passengers, or training on driving them. Goods vehicles are not in this clause |
| (aa) | Vessels and aircraft | Further supply, passenger transport, navigation or flying training, or transport of goods |
| (ab) | General insurance, servicing, repair and maintenance of the vehicles, vessels and aircraft in (a) and (aa) | An excepted use, manufacture of the specified vehicles, vessels or aircraft, or general insurance supplied by an insurer in respect of what it insured |
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

#### 5.8 Paying the liability: cash and credit order

- Reverse-charge tax is paid in cash (electronic cash ledger). Credit in the electronic credit ledger may be used only "towards output tax" (section 49(4)), and "output tax" "excludes tax payable by him on reverse charge basis" (section 2(82)). The GSTR-3B instructions allow the matching credit only "on payment of tax".
- Order of use of credit (section 49(5) and rule 88A, https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter9/rule88a_v1.00.html):
  1. IGST credit is used first against IGST. Any balance may then be used against CGST and SGST/UTGST "in any order" (rule 88A).
  2. CGST and SGST credit may be used only after the IGST credit "has first been utilised fully".
  3. CGST credit: against CGST, then IGST. Never against SGST/UTGST (section 49(5)(e)).
  4. SGST/UTGST credit: against SGST/UTGST, then IGST, but against IGST only where no CGST credit is left for it (section 49(5)(c) proviso). Never against CGST (section 49(5)(f)).

The earlier Guide said IGST credit must go to CGST before SGST. Rule 88A, in force since 29 March 2019, lets the balance go to either "in any order".

#### 5.9 ITC reversal for exempt supplies (rules 42 and 43)

Allocate common input and service credit under rule 42 and capital goods credit under rule 43. Apply the statutory exempt-turnover calculation and applicable exclusions. Under rule 42(2), calculate the year-end amount before the due date of the following September return, adjust within the rule's September cut-off and pay interest from 1 April on any under-reversal. Rule 43 generally works monthly over 60 months; check the separate reconciliation for qualifying real-estate projects under rule 43(2).

### Tier 2 catalogue

For each ambiguity: the pattern, why the bank statement is not enough, the conservative default, and the question for the client.

#### 6.1 Vehicle costs (fuel, tolls)

Pattern: HPCL, BPCL, IOCL, SHELL, petrol pump, FASTag, NHAI. Why not enough: the vehicle type and business use are unknown. A passenger car of up to thirteen seats is blocked by section 17(5)(a) unless used for the excepted purposes; its insurance, servicing and repair are blocked by section 17(5)(ab). A goods vehicle is not blocked by clause (a). GST on petrol and high speed diesel applies only from a date the Government notifies (IGST Act section 5(2)); if the fuel bill shows no GST, there is no credit to claim. Default: no ITC. Question: "Is this for a passenger car or a goods vehicle used in the business?"

#### 6.2 Food delivery and restaurants

Pattern: food delivery or restaurant. Hold ITC unless the client confirms a section 17(5)(b) exception such as taxable onward supply or a legally required employee benefit.

#### 6.3 Home office (rent and utilities)

Pattern: rent to a landlord, electricity, internet at a home address. Why not enough: the business share and the tenant's capacity are unknown. A registered tenant of a residential dwelling pays tax under reverse charge (serial 5AA, from 18 July 2022), except a proprietor renting in a personal capacity as his own residence (exempt from 1 January 2023). Credit for personal consumption is blocked (section 17(5)(g)); mixed use is limited to the business share (section 17(1)). Electricity is exempt, so there is nothing to claim on it. Default: no ITC. Question: "Is the lease in your personal name or the business name? Do you live there? What share of the property is used only for business?"

#### 6.4 Cash withdrawals

Pattern: ATM or cash withdrawal. Use the cash records to match business payments and prescribed documents. Hold ITC pending evidence and identify any owner drawing separately.

#### 6.5 Mixed B2B and B2C sales

For unidentified buyers, confirm registration before allocating GSTR-1. Use 4A or 4B for registered buyers as applicable, table 5 for inter-State B2C above the threshold and table 7 for remaining domestic B2C.

#### 6.6 Inter-State or intra-State

If the tax head is unclear, obtain the supplier location and place-of-supply facts. Hold the classification until they are confirmed. Wrong-head tax has a statutory correction and refund process.

#### 6.7 Digital services from abroad: business or personal?

Check the service and place of supply under IGST Act section 13 and the recipient's status under section 14. Section 5.3 covers taxable imports by a registered recipient. Claim ITC only for eligible business use.

### Excel working paper template

#### Sheet "Transactions"

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

#### Sheet "GSTR-2B reconciliation"

Use one row per supporting document. Record its identifying details, taxable value, tax heads, GSTR-2B match where applicable, eligibility and action. Total each GSTR-3B input credit category separately, following Section 5.6.

#### Sheet "GSTR-3B summary"

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

#### Sheet "Tax computation"

~~~
Output tax on outward supplies, by head = from 3.1(a) and 3.1(b) (if IGST paid)
Reverse-charge tax, by head             = from 3.1(d), paid in CASH only

Use of credit (Section 5.8):
  IGST credit -> IGST first; balance -> CGST and SGST in any order
  CGST credit -> CGST, then IGST (only after IGST credit is used up); never SGST
  SGST credit -> SGST, then IGST (only if no CGST credit is left for it); never CGST

Cash payable by head = output tax not covered by credit + reverse-charge tax
~~~

#### Colour and formatting conventions

Blue for values typed from the bank statement or invoice. Black for formulas. Green for cross-sheet references. Yellow background for any row where Default? = "Y". Red text for any blocked-ITC row (section 17(5)).

#### Mandatory recalc step

After building the workbook, recalculate every formula and cache the results so the
values can be read back. On a normal machine, recalc with LibreOffice headless:

~~~bash
soffice --headless --convert-to xlsx --outdir /tmp /mnt/user-data/outputs/india-gst-PERIOD-working-paper.xlsx
~~~

Then re-open the converted file and check for formula errors. If any cell shows an
error, fix the formulas and recalc again.

### Indian bank statement reading guide

Follow the universal exclusion rules, plus these India-specific patterns.

#### HDFC Bank statement format

Typical CSV columns: Date, Narration, Chq/Ref No, Value Dt, Withdrawal Amt, Deposit Amt, Closing Balance. Date format DD/MM/YY or DD/MM/YYYY. The narration carries the counterparty, often in short form: "NEFT/RTGS/IMPS-[IFSC]-[Sender name]", "UPI-[UPI ID]-[Name]", "POS [Merchant]-[Terminal ID]", "ATM-SELF", "BIL/ONL/[Biller name]".

**HDFC narration parsing rules:**
- `NEFT-UTIB0000XXX-[PAYER]`: transfer through the bank branch identified by the IFSC
- `UPI-[ID]-[PAYEE]`: UPI payment with a payee identifier
- `POS [terminal ID] AMAZON`: card purchase at Amazon
- `BIL/ONL/AIRTEL`: online bill payment to Airtel
- `INT.PD`: interest paid (exclude)
- `CHG-GST` or `SERVICE CHARGES`: bank charges; ITC only per the bank's GST invoice

#### SBI statement format

Typical columns: Txn Date, Value Date, Description, Ref No/Cheque No, Debit, Credit, Balance. Description format: "INB/NEFT/[Ref]-[Name]", "ATM/SELF/[Branch]", "UPI/[ID]/[Name]", "SI-[Standing Instruction]".

#### ICICI Bank statement format

Typical columns: S No, Value Date, Transaction Date, Cheque Number, Transaction Remarks, Withdrawal Amount (INR), Deposit Amount (INR), Balance (INR). Remarks format: "NEFT-[IFSC]-[Name]", "UPI/[Ref]/[Name]", "MMT/IMPS/[Ref]/[Name]", "POS/[Merchant]/[Location]".

#### Common patterns across Indian bank statements

**UPI payments:** use the identifiers shown to match the underlying invoice or receipt.

**NEFT/RTGS/IMPS:** an IFSC identifies the bank branch. Verify the underlying payment and the place of supply from the transaction documents.

**Card transactions (POS/online):** merchant name embedded but often cut short. "POS" plus a card or terminal number with no name: ask the client.

**Standing instructions (SI/ECS/NACH):** recurring debits for EMI, insurance, subscriptions. Pattern: "ECS/NACH-[Mandate]-[Payee]".

**Internal transfers and exclusions:**
- Own-account transfers: "TRF-OWN", "SELF TRANSFER", "FD CREATION"
- Mutual fund SIPs: "BSE-MF-[Fund name]": investment, exclude
- FD maturity or creation: "FD-[number]": exclude
- ATM self-withdrawal: match to the cash records before assigning the transaction

**Refunds and reversals:** "REVERSAL", "REFUND", "RETURN-NEFT". For GST, a refund from a supplier needs the supplier's credit note; reduce ITC in the period the credit note is reported, not by changing the original period.

**Salary payments:** "PAYROLL", "SALARY-[month]", many outgoing payments to individuals on one date. Exclude.

**Loan disbursement or repayment:** separate principal and exempt interest from any fees.

**Foreign currency:** for services use the exchange rate determined under generally accepted accounting principles at the time of supply (rule 34(2)). Reconcile it to the bank debit.

## Deadlines and filing

### 5.10 Return due dates and late fees: GSTR-1, GSTR-3B, GSTR-9

**Due dates.** Section 37(1) gives the underlying tenth-day date; Notification 83/2020 extends it as shown above. A GSTR-3B is due even without supplies. Verify filing prerequisites under sections 37(4), 39(10) and rule 59(6), including prior returns and the period's GSTR-1. GSTR-1A opens at the later of the GSTR-1 due date and actual filing, and closes when the same period's GSTR-3B is filed.

Where required, GSTR-9 is due on 31 December 2026 for FY 2025-26 and 31 December 2027 for FY 2026-27. Apply the INR 2 crore exemption above. Composition taxpayers file GSTR-4 and are covered only in the referral table.



**GSTR-1 table limit (B2C large).** Inter-State supplies to unregistered persons are reported invoice by invoice above the limit below, and State-wise in consolidated form up to it (rule 59). The earlier Guide said two and a half lakh: Notification 12/2024-Central Tax substituted "one lakh rupees" (from 1 August 2024).

**Late fees.** Tables give the central tax component. Check the relevant State or UT law and waiver before calculating that component.

The GSTR-1 and GSTR-3B reduced caps in Notifications 19/2021 and 20/2021 use preceding-year turnover. Apply the nil test for the particular form first.

The GSTR-9 reductions in Notification 07/2023 apply from FY 2022-23 and use relevant-year aggregate turnover.

Both reduced GSTR-9 bands are capped at 0.02% of turnover in the State or UT under the central notification. Above INR 20 crore, use section 47(2), INR 100 a day and a 0.25% cap.

**Interest.** Interest runs from the day after tax was due (section 50(2)). For an ordinary late GSTR-3B, calculate it on the cash-paid portion subject to the proceedings exception in section 50(1) and the qualifying cash-ledger balance exclusion in rule 88B(1). Wrongly availed ITC that was also utilised carries interest under section 50(3).

**Three-year bar.** GSTR-1, GSTR-3B and GSTR-9 cannot be filed after three years from their due date, unless the Government notifies otherwise (sections 37(5), 39(11) and 44(2), in force from 1 October 2023). Refer (R-IN-6).

**Corrections.** An error in GSTR-1 or GSTR-3B is corrected in a later period's return, with interest on any short payment, but not after 30 November following the end of the financial year or the date the annual return is filed, whichever is earlier (sections 37(3) and 39(9)).

### 5.12 E-way bill

Rule 138 has exemptions and cases where a bill is needed regardless of value, including specified inter-State job work and handicraft movements. Distinguish the short local movements exempt only from Part B vehicle details.

### 5.13 Registration thresholds

Apply sections 22 to 25 and the goods-only exemption conditions, including mandatory registration, location and excluded products.

### 5.14 Compensation cess

Check the product-specific cessation date for GST compensation cess. The Health Security se National Security Cess is a separate manufacturing levy on scheduled products, including pan masala, from 1 February 2026.

### 5.15 QRMP scheme (quarterly returns, monthly payment)

A registered person may opt to file GSTR-1 and GSTR-3B quarterly (section 39(1), proviso). The option is exercised on the portal from the first day of the second month of the preceding quarter to the last day of the first month of the quarter (rule 61A(1)); it cannot be exercised while the last due return is unfiled. Once aggregate turnover in the current financial year exceeds the limit below, the person must move to monthly returns from the next quarter (rule 61A(2)). QRMP filers pay tax for months 1 and 2 by the PMT-06 date in Section 5.10 and may upload B2B invoices through IFF (Section 5.10).

Under Notification 84/2020-Central Tax, entry requires aggregate turnover up to INR 5 crore in the preceding financial year and excludes persons subject to section 14 of the IGST Act. Check current-year turnover for exit.

### 5.16 Changes following the 57th GST Council recommendations (8 October 2026)

The October Gazette notifications gave certain changes effect from 1 November 2026, including revised delivery and hotel rules. Specified recipient e-invoicing for purchases from unregistered suppliers and imports of services starts on 1 January 2027. See `india-einvoice` for the scope. Check a gazetted commencement before applying any other recommendation, including the proposed late-fee relief for small filers.

## Penalties and interest

Late fees, interest under section 50 and the GSTR-9 late fee bands are in the rates table (subsection 5.10) and described in 5.10 under Deadlines and filing. For a contravention with no penalty set elsewhere, section 125 of the CGST Act allows a general penalty of up to twenty-five thousand rupees ([section 125](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter19/section125_v1.00.html)). E-invoicing penalties (sections 122 and 125) are in `india-einvoice`. Never derive a combined central-plus-State late fee or an effective rate.

## Cross-border points

### 5.3 Reverse charge on import of services

Under IGST Act sections 2(11) and 5(3) and Notification 10/2017-Integrated Tax (Rate), serial 1, check that the supplier is outside India, the recipient is in India and the place of supply is in India. Confirm any applicable exemption or special collection rule, including section 14 for online services to unregistered recipients. For a taxable import under reverse charge, pay IGST in cash, enter it in table 3.1(d) and claim eligible credit in 4(A)(2). This credit is entered by the taxpayer, outside GSTR-2B.

Finance Act 2026 section 157 omitted the special supplier-location rule in IGST Act section 13(8)(b) for intermediary services from 30 March 2026. Determine the place of supply under the applicable remaining provisions and separately test any export conditions.

### 5.11 Exports and supplies to SEZ

Exports and supplies to SEZ units or developers for authorised operations qualify as zero-rated under IGST Act section 16(1). Eligibility for ITC is subject to section 17(5) of the CGST Act. Verify the refund route separately.

| Option | Mechanism | Refund |
| --- | --- | --- |
| Under bond or Letter of Undertaking, without paying IGST (section 16(3)) | File the LUT in Form GST RFD-11 before export (rule 96A) | Refund of unutilised ITC (section 54), claimed under rule 89 in Form GST RFD-01 |
| On payment of IGST (section 16(4)) | Only for a class of persons, or of goods or services, notified by the Government (substituted section, in force from 1 October 2023) | Refund of IGST paid |

An LUT generally requires payment of tax and interest within 15 days after the 3-month goods export deadline or the services receipt deadline under rule 96A(1). The services deadline is one year or the longer FEMA period, measured from the invoice. Check any Commissioner extension and the currency rules. Report exports in GSTR-3B table 3.1(b) and GSTR-1 table 6. Verify the notified class before electing the IGST-payment route.

## Worked examples

Examples 1 to 6 apply the rules to fictional July 2026 bank transactions for a Mumbai software consultant. The calculations use the stated invoice and supply facts. Examples 7 to 9 cover tax heads and registration.

### Example 1: Foreign SaaS under reverse charge (Notion)

**Input line:** `05.07.2026 ; NOTION LABS INC DEBIT CARD ; DR ; 10.00 ; USD ; 840.00 ; INR`

Assume a taxable digital service supplied from outside India with its place of supply in India, a notified 18% IGST rate and the rule 34(2) exchange rate of INR 84 per US dollar. The taxable amount is USD 10 × 84 = INR 840. Pay INR 151.20 IGST in cash, report it in 3.1(d) and claim INR 151.20 in 4(A)(2) when eligible.

| Date | Counterparty | Gross | GSTR-3B (output) | GSTR-3B (input) | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- |
| 05.07.2026 | NOTION LABS INC | -840 | 3.1(d) | 4(A)(2) | Y (rate) | "Confirm the rate notified for this service" |

### Example 2: Indian SaaS, inter-State (AWS India)

**Input line:** `10.07.2026 ; AMAZON INTERNET SERVICES PVT LTD NEFT ; DR ; 23,600.00 ; INR`

Assume the supplier is located outside Maharashtra, the place of supply for the registered recipient is Maharashtra and 18% IGST applies. INR 23,600 ÷ 1.18 = INR 20,000 taxable value and INR 3,600 IGST. Claim the eligible INR 3,600 in 4(A)(5) after section 16 checks.

| Date | Counterparty | Gross | GSTR-3B | Default? | Question? |
| --- | --- | --- | --- | --- | --- |
| 10.07.2026 | AMAZON INTERNET SERVICES | -23,600 | 4(A)(5) | N | "Invoice in GSTR-2B?" |

### Example 3: Food delivery, blocked ITC (Swiggy)

**Input line:** `15.07.2026 ; BUNDL TECHNOLOGIES SWIGGY ; DR ; 450.00 ; INR`

This is an ordinary delivered meal with no applicable section 17(5)(b) exception. ITC on the INR 450 payment is INR 0.

| Date | Counterparty | Gross | ITC? | Default? | Question? |
| --- | --- | --- | --- | --- | --- |
| 15.07.2026 | SWIGGY | -450 | BLOCKED, section 17(5)(b)(i) | N | "Business meal? (for income tax records only)" |

### Example 4: Legal services under reverse charge (advocate)

**Input line:** `20.07.2026 ; ADVOCATE FEES NEFT ; DR ; 50,000.00 ; INR`

Assume the advocate and the place of supply are in Maharashtra. The business exceeded its applicable registration exemption threshold in the prior year, so no small-recipient exemption applies. On INR 50,000 at 18%, pay INR 4,500 CGST plus INR 4,500 SGST in cash, report INR 9,000 in 3.1(d) and claim it in 4(A)(3) if eligible.

| Date | Counterparty | Gross | GSTR-3B (output) | GSTR-3B (input) | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- |
| 20.07.2026 | ADVOCATE FEES | -50,000 | 3.1(d) | 4(A)(3) | Y | "Is the advocate in the same State? Is the service for the business?" |

### Example 5: Domestic air travel

**Input line:** `22.07.2026 ; INTERGLOBE AVIATION INDIGO PNR AB1CDE ; DR ; 5,250.00 ; INR`

Assume the invoice is for eligible economy-class business travel with GST included at 5%. INR 5,250 ÷ 1.05 = INR 5,000 taxable fare and INR 250 GST, claimable in 4(A)(5) after section 16 checks. Confirm the class from the invoice.

| Date | Counterparty | Gross | GSTR-3B | Default? | Question? |
| --- | --- | --- | --- | --- | --- |
| 22.07.2026 | INTERGLOBE AVIATION | -5,250 | 4(A)(5) | Y | "Economy or other class? Business purpose? Invoice in GSTR-2B?" |

### Example 6: Passenger car, blocked

**Input line:** `28.07.2026 ; MARUTI SUZUKI INDIA LTD NEFT ; DR ; 8,50,000.00 ; INR`

Assume approved seating of at most 13 including the driver and own use in the consulting business, with no section 17(5)(a) exception. The INR 850,000 gross price yields INR 0 ITC. The seller's tax rate depends on the vehicle's tariff entry.

| Date | Counterparty | Gross | ITC? | Default? | Question? |
| --- | --- | --- | --- | --- | --- |
| 28.07.2026 | MARUTI SUZUKI | -8,50,000 | BLOCKED, section 17(5)(a) | Y | "Is the vehicle used to carry passengers for a fare, resold, or used for driving training?" |

### Example 7: Intra-State invoice at the standard rate

A supplier in Maharashtra invoices a client in Maharashtra INR 10,000 before tax for a supply at the standard rate of 18% (Section 1). Supplier and place of supply are in the same State, so the tax is split into central and State tax at 9% each (Section 5.2).

```oa-check
name: Intra-State invoice, INR 10,000 at 18%
inputs:
  taxable_value: 10000
steps:
  - cgst: pct(taxable_value, 9)
  - sgst: pct(taxable_value, 9)
  - total_tax: cgst + sgst
  - invoice_total: taxable_value + total_tax
expected:
  cgst: 900.00
  sgst: 900.00
  total_tax: 1800.00
  invoice_total: 11800.00
```

### Example 8: Inter-State invoice at the merit rate

A supplier in Karnataka invoices a client in Maharashtra INR 10,000 before tax for a supply at the merit rate of 5% (Section 1). The States differ, so the whole tax is IGST (Section 5.2).

```oa-check
name: Inter-State invoice, INR 10,000 at 5%
inputs:
  taxable_value: 10000
steps:
  - igst: pct(taxable_value, 5)
  - invoice_total: taxable_value + igst
expected:
  igst: 500.00
  invoice_total: 10500.00
```

### Example 9: A Pune web designer with 22 lakh rupees of turnover, register or not

A Pune designer's taxable Maharashtra-only services reach INR 22 lakh turnover in January 2027. Assume no earlier compulsory registration and no exemption. Section 22(1) makes the designer liable upon crossing INR 20 lakh; apply within 30 days of crossing under section 25(1). For a subsequent Maharashtra invoice of INR 100,000 classified at 18%, use 9% CGST and 9% Maharashtra SGST.

```oa-check
name: Registration test, 22 lakh services turnover in a general State, then tax on a 1,00,000 invoice
inputs:
  turnover: 2200000
  threshold: 2000000
  invoice: 100000
steps:
  - over_threshold: turnover - threshold
  - cgst: invoice * 0.09
  - sgst: invoice * 0.09
  - total: invoice + cgst + sgst
expected:
  over_threshold: 200000
  cgst: 9000
  sgst: 9000
  total: 118000
```

A positive amount over the threshold means registration is required.

## Ask the client first

- Are you registered as a regular taxpayer or under composition, and do you hold more than one GSTIN? (Composition or several GSTINs changes the returns entirely.)
- In which State is your principal place of business, and do you file monthly or quarterly (QRMP)? (Sets the GSTR-3B due date group and the PMT-06 payments.)
- What was your aggregate turnover last financial year, and so far this year? (Sets QRMP eligibility, late fee caps, HSN digits, e-invoicing and GSTR-9C.)
- Do you buy anything from abroad, from advocates, transporters, non-corporate security agencies or unregistered landlords, or pay directors? (Reverse charge.)
- Do you export, and is an LUT filed for this financial year? (Zero-rating without tax, or not.)
- Have all suppliers been paid within one hundred and eighty days of their invoices, and do you have GSTR-2B for each month? (ITC reversals and what may be claimed.)

### Required inputs and refusal catalogue

#### Required inputs

**Minimum viable**: bank statement for the month or quarter in CSV, PDF, Excel, or pasted text, covering the full filing period. Acceptable from any Indian bank (SBI, HDFC, ICICI, Axis, Kotak, PNB, Bank of Baroda, IndusInd, Yes Bank, IDFC First, or any other scheduled bank). Also acceptable: Razorpay, Paytm or other payment processor settlement reports.

**Evidence**: sales and purchase invoices, prior GSTR-1 and GSTR-3B, GSTR-2B, and other prescribed documents for imports and self-invoiced reverse charge.

**Ideal**: Tally / Zoho Books / Busy or similar export (trial balance and GST transaction register), complete invoice register with HSN/SAC codes, last year's GSTR-9, e-invoice JSON exports where e-invoicing applies.

With bank data alone, prepare a draft reconciliation and list unresolved transactions. Get the underlying documents and verify the rate, tax head, recipient status and credit conditions before finalising the returns.

#### India-specific refusal catalogue

If any trigger fires, stop and give the refusal message. Refusal is a safety mechanism.

- **R-IN-1: Composition scheme taxpayer.** Trigger: the client pays tax under section 10 (composition), or mentions CMP-08 or GSTR-4. Message: "Composition taxpayers pay tax quarterly with statement CMP-08 and file one annual return, GSTR-4, not GSTR-1 and GSTR-3B. They pay tax at a flat rate on turnover and cannot claim input tax credit. This skill covers regular taxpayers only. Please use a qualified GST practitioner." The composition limits, rates and dates are in the table below, for the referral note only.
- **R-IN-2: Multi-State registration.** Trigger: the client has GSTINs in more than one State and asks to consolidate or cross-use credit. Message: "Each State GSTIN is a separate registration, with its own returns and its own credit ledger. This skill handles one GSTIN. File each GSTIN separately; for Input Service Distributor or cross-charge questions, use a qualified CA or GST practitioner."
- **R-IN-3: Supplies to SEZ units or developers.** Trigger: the client supplies to SEZ units or developers and asks about zero-rating, LUT or refund of accumulated ITC for those supplies. Message: "SEZ supply documentation needs fact-specific checks beyond this skill. Please use a qualified GST practitioner."
- **R-IN-4: E-commerce operator.** Trigger: the client runs an e-commerce platform that must collect tax at source under section 52 or pay tax under section 9(5). Message: "E-commerce operators have TCS, GSTR-8 and platform-level duties outside this skill. Please use a qualified GST practitioner."
- **R-IN-5: Input Service Distributor (ISD).** Trigger: the client is registered as an ISD or needs to distribute common input services across GSTINs. Message: "ISD distribution is outside this skill, which covers single-GSTIN regular taxpayers. Please use a qualified CA or GST practitioner."
- **R-IN-6: Return outside the three-year window.** Trigger: GSTR-1, GSTR-3B or GSTR-9 for a period whose due date passed more than three years ago. Message: "The CGST Act bars filing these returns after three years from their due date unless the Government notifies otherwise (sections 37(5), 39(11), 44(2)). Please use a qualified GST practitioner."

Composition figures (for the R-IN-1 referral note):

### Onboarding fallback (only when inference fails)

Infer the client profile from the data first. Ask only when inference fails.

#### 9.1 Legal name and GSTIN

Take the GSTIN from the registration certificate or a verified invoice. If unavailable, ask for it.

#### 9.2 Registration type

Inference: a request for GSTR-3B or GSTR-1 means a regular taxpayer. CMP-08 or GSTR-4 means composition: R-IN-1 refuses. Fallback question: "Are you a regular GST taxpayer or under the composition scheme?"

#### 9.3 State of registration

Use the registration certificate and principal place of business for the QRMP date group. Verify place of supply separately for each transaction.

#### 9.4 Filing period and frequency

Inference: first and last transaction dates. Monthly filers: one month. QRMP filers: a full quarter. Fallback question: "Which period does this cover? Monthly or quarterly (QRMP)?"

#### 9.5 Business activity

Inference: counterparty mix, sales descriptions, HSN/SAC on invoices. Fallback question: "In one sentence, what does the business do?"

#### 9.6 Inter-State supplies

Inference: buyers' or suppliers' GSTINs from other States, IGST on invoices. Fallback question: "Do you sell to buyers in other States? Which ones?"

#### 9.7 Exports

Inference: foreign currency receipts, "FIRC" or "EXPORT" in narrations. Fallback question: "Do you export goods or services? Is a Letter of Undertaking (RFD-11) filed for this financial year?"

#### 9.8 Reverse charge purchases

Inference: payments to advocates, transporters, security agencies, foreign suppliers, directors, unregistered landlords. Fallback question: "Do you buy from advocates, goods transport agencies, non-corporate security agencies, foreign suppliers or unregistered landlords? Do you pay sitting fees to directors?"

#### 9.9 E-invoicing

Inference: prior-year GSTR-9 or stated turnover. Fallback question: "Has your aggregate turnover crossed the e-invoicing threshold (Section 5.5) in any financial year from 2017-18 onwards?"

#### 9.10 ITC brought forward

Not inferable from one period. Always ask: "What are your electronic credit ledger balances (IGST, CGST, SGST separately) at the start of the period?"

### The method, step by step

1. **Confirm scope.** Regular taxpayer, one GSTIN, no composition, ISD, e-commerce operator or SEZ supplies (Section 2, refusals). Check the period is within three years of its due date (CGST Act sections 37(5), 39(11), 44(2): https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section39_v1.00.html).
2. **Fix the frequency and the due dates.** Monthly or QRMP (rule 61A: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61a_v1.00.html); GSTR-1 date from Notification 83/2020-Central Tax and GSTR-3B date from rule 61 (Section 5.10).
3. **Classify every bank line.** Use the pattern library (Section 3), then the rules (Section 5), then Tier 2 (Section 6). Record rate, tax head, GSTR-3B and GSTR-1 table per line (Section 7).
4. **Build outward supplies for GSTR-1.** B2B invoice by invoice (table 4A/4B); inter-State B2C above the B2C large limit invoice by invoice (table 5); other B2C rate-wise (table 7); exports (table 6); credit and debit notes (table 9B); HSN summary (table 12) with the digits required by turnover (rule 59: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule59_v1.00.html , Notification 78/2020-Central Tax). File by the GSTR-1 date. Correct any omission in GSTR-1A before filing GSTR-3B.
5. **Reconcile ITC.** Apply the GSTR-2B condition to section 37 documents and verify other prescribed documents. Adjust blocked credits, unpaid suppliers and exempt-supply shares as described in Sections 5.6 to 5.9.
6. **Self-assess reverse charge.** Import of services and domestic reverse-charge services (Sections 5.3 and 5.4; Notification 13/2017-Central Tax (Rate): https://gstcouncil.gov.in/sites/default/files/2024-05/download_8_0.pdf). Declare in 3.1(d); pay in cash; take credit in 4(A)(2) or 4(A)(3).
7. **Compute the liability and the use of credit.** Apply section 49(5) and rule 88A (Section 5.8: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter10/section49_v1.00.html). Check GSTR-3B output tax against GSTR-1 so that no DRC-01B difference arises (rule 88C).
8. **File and pay.** File GSTR-3B by the applicable rule 61 date. QRMP filers pay months 1 and 2 by PMT-06. Apply the relevant late fee and section 50 interest where due.
9. **Year end.** Calculate the rule 42 annual adjustment before the September return's due date. Track the 30 November cut-off for corrections, missed ITC and rule 37A reversals, and any earlier annual-return cut-off. File GSTR-9 and GSTR-9C by 31 December where required after applying the threshold rules.
10. **Write the reviewer brief.** List unresolved classifications, blocked and held credits and changes with a later commencement date.

### When to refuse or refer

- Any refusal trigger R-IN-1 to R-IN-6 in Section 2.
- A supply whose rate, classification or section 14 transition cannot be established.
- A notice in DRC-01B, DRC-01C or any section 73, 74 or 74A notice: refer; the seven-day reply window in rules 88C and 88D is short.
- Export on payment of IGST, or any refund claim (RFD-01).
- Place of supply disputes for services (IGST Act sections 12 and 13), especially cross-border.
- Rule 42 annual reconciliation, any project-specific rule 43 reconciliation, GSTR-9 and GSTR-9C, for accountant sign-off.
- A recommendation for which the applicable legislation or commencement cannot be confirmed.

### Reference material

#### Known gaps

1. The pattern library covers common Indian and foreign vendors only. Add patterns as they emerge.
2. The worked examples use one hypothetical Mumbai IT consultant. Manufacturing, trading and hospitality are not covered.
3. HSN/SAC classification needs the rate notifications; this skill does not hold the HSN/SAC master. Flag unknown classifications as Tier 2.
4. Place of supply for services (IGST Act sections 12 and 13) is often disputed. Flag cross-border or multi-State cases as Tier 2.
5. Supplies that straddle the 22 September 2025 or 1 February 2026 start dates need the time-of-supply rules; refer.

7. E-invoicing detail (exemptions, reporting time limits) is left to `india-einvoice`; the years that count are in Section 5.5.


##### PROHIBITIONS

- NEVER allow ITC on blocked credits under section 17(5), whatever the business use, unless the clause's own exception applies.
- NEVER apply CGST plus SGST to an inter-State supply, or IGST to an intra-State supply.
- NEVER guess an HSN/SAC code or a rate. Classification is checked against the rate notification.
- NEVER claim ITC on a section 37 document before it is communicated in GSTR-2B. Verify separately prescribed evidence for other credit.
- NEVER pay reverse-charge tax with ITC. It is paid in cash.
- NEVER claim ITC after 30 November following the end of the financial year (or after GSTR-9 is filed, if earlier). A re-claim of credit reversed earlier (rule 37) is outside this limit (rule 37(4)).
- NEVER classify a mixed supply as composite to reach a lower rate.
- NEVER ignore the order of credit use (IGST credit first, in full).
- NEVER issue a B2B invoice without IRN and QR code where e-invoicing applies.
- Verify that an export or supply for authorised SEZ operations is zero-rated under section 16. Verify the LUT, bond or notified IGST-payment route for any refund claim.
- Check whether a Council recommendation has been enacted and commenced before applying it.
- NEVER guess or derive a rate or fee: no combined central-plus-State late fee, no effective rate. Tax on a value at a rate this skill prints is plain arithmetic and is allowed (Section 4, Examples 7 and 8).

#### Change log

The version history (October 2026 team rewrite, v2.1 and v2.2 merges of the retired `in-gst-return`) is in the repository history.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for faqs_on_recommendations_made_in_57th_gst_council_meeting.pdf (GST rates from 22 September 2025) | https://gstcouncil.gov.in/sites/default/files/2026-10/faqs_on_recommendations_made_in_57th_gst_council_meeting.pdf | 2026-11-14 |
| Read for central-tax-12-2024-11072024.pdf (GST rates from 22 September 2025) | https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf | 2026-11-14 |
| Read for press_release_press_information_bureau_0.pdf (GST rates from 22 September 2025) | https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau_0.pdf | 2026-11-14 |
| Read for faq_0.pdf (GST rates from 22 September 2025) | https://gstcouncil.gov.in/sites/default/files/2025-09/faq_0.pdf | 2026-11-14 |
| Read for monthly_newsletter_december_2025_1_0.pdf (GST rates from 22 September 2025) | https://gstcouncil.gov.in/sites/default/files/2026-01/monthly_newsletter_december_2025_1_0.pdf | 2026-11-14 |
| Read for download_5.pdf (GST rates from 22 September 2025) | https://gstcouncil.gov.in/sites/default/files/2024-05/download_5.pdf | 2026-11-14 |
| Read for 01062019-GST-An-Update.pdf (India-specific refusal catalogue) | https://cbic-gst.gov.in/pdf/01062019-GST-An-Update.pdf | 2026-11-14 |
| Read for IGST Act section 5 (CGST plus SGST, or IGST) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_IGST_Act/active/chapteriii/section5_v1.00.html | 2026-11-14 |
| Read for download_8_0.pdf (Domestic reverse charge) | https://gstcouncil.gov.in/sites/default/files/2024-05/download_8_0.pdf | 2026-11-14 |
| Read for 05_2022-ctr-eng_1.pdf (Domestic reverse charge) | https://gstcouncil.gov.in/sites/default/files/2024-05/05_2022-ctr-eng_1.pdf | 2026-11-14 |
| Read for 15_2022-ctr-eng.pdf (Domestic reverse charge) | https://gstcouncil.gov.in/sites/default/files/2024-05/15_2022-ctr-eng.pdf | 2026-11-14 |
| Read for ctr-09-2024.pdf (Domestic reverse charge) | https://gstcouncil.gov.in/sites/default/files/2024-10/ctr-09-2024.pdf | 2026-11-14 |
| Read for download_2024-05-17t161051.835.pdf (Domestic reverse charge) | https://gstcouncil.gov.in/sites/default/files/2024-05/download_2024-05-17t161051.835.pdf | 2026-11-14 |
| Read for 10ct_eng.pdf (E-invoicing, invoices and HSN codes) | https://gstcouncil.gov.in/sites/default/files/2024-05/10ct_eng.pdf | 2026-11-14 |
| Read for notfctn-70-central-tax-english-2020.pdf (E-invoicing, invoices and HSN codes) | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-70-central-tax-english-2020.pdf | 2026-11-14 |
| Read for notfctn-78-central-tax-english-2020.pdf (E-invoicing, invoices and HSN codes) | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-78-central-tax-english-2020.pdf | 2026-11-14 |
| Read for CGST Act section 16 (ITC: conditions, GSTR-2B reconciliation ) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html | 2026-11-14 |
| Read for notfctn-83-central-tax-english-2020.pdf (Return due dates and late fees: GSTR-1, ) | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-83-central-tax-english-2020.pdf | 2026-11-14 |
| Read for CGST Rules rule 61 (Return due dates and late fees: GSTR-1, ) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 80 (Return due dates and late fees: GSTR-1, ) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule80_v1.00.html | 2026-11-14 |
| Read for gst-ct-32-2023.pdf (Return due dates and late fees: GSTR-1, ) | https://gstcouncil.gov.in/sites/default/files/2024-05/gst-ct-32-2023.pdf | 2026-11-14 |
| Read for CGST Rules rule 59 (Return due dates and late fees: GSTR-1, ) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule59_v1.00.html | 2026-11-14 |
| Read for CGST Act section 47 (Return due dates and late fees: GSTR-1, ) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section47_v1.00.html | 2026-11-14 |
| Read for notfctn-76-central-tax-english-2018.pdf (Return due dates and late fees: GSTR-1, ) | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-76-central-tax-english-2018.pdf | 2026-11-14 |
| Read for notification-4-2018-central_tax-english.pdf (Return due dates and late fees: GSTR-1, ) | https://gstcouncil.gov.in/sites/default/files/2024-05/notification-4-2018-central_tax-english.pdf | 2026-11-14 |
| Read for notfctn-19-central-tax-english-2021.pdf (Return due dates and late fees: GSTR-1, ) | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-19-central-tax-english-2021.pdf | 2026-11-14 |
| Read for notfctn-20-central-tax-english-2021.pdf (Return due dates and late fees: GSTR-1, ) | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-20-central-tax-english-2021.pdf | 2026-11-14 |
| Read for 07_eng.pdf (Return due dates and late fees: GSTR-1, ) | https://gstcouncil.gov.in/sites/default/files/2024-05/07_eng.pdf | 2026-11-14 |
| Read for notfctn-13-central-tax-english.pdf (Return due dates and late fees: GSTR-1, ) | https://gstcouncil.gov.in/sites/default/files/2024-04/notfctn-13-central-tax-english.pdf | 2026-11-14 |
| Read for CGST Act section 50 (Return due dates and late fees: GSTR-1, ) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter10/section50_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 138 (E-way bill) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter16/rule138_v1.00.html | 2026-11-14 |
| Read for CGST Act section 22 (Registration thresholds) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section22_v1.00.html | 2026-11-14 |
| Read for CGST Act section 25 (Registration thresholds) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter6/section25_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 61a (QRMP scheme (quarterly returns, monthly ) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule61a_v1.00.html | 2026-11-14 |
| Read for ctr01-2025.pdf (CGST plus SGST, or IGST) | https://gstcouncil.gov.in/sites/default/files/2025-01/ctr01-2025.pdf | 2026-11-14 |
| Read for ctr07-2025.pdf (Domestic reverse charge) | https://gstcouncil.gov.in/sites/default/files/2025-01/ctr07-2025.pdf | 2026-11-14 |
| Read for CGST Act section 17 (Blocked credits: section 17(5)) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section17_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 88a (Paying the liability: cash and credit or) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter9/rule88a_v1.00.html | 2026-11-14 |
| Read for press_release_0.pdf (Pending: 57th GST Council recommendation) | https://gstcouncil.gov.in/sites/default/files/2026-10/press_release_0.pdf | 2026-11-14 |
| Read for CGST Act section 125 (Pending: 57th GST Council recommendation) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter19/section125_v1.00.html | 2026-11-14 |
| Read for CGST Act section 39 (The method, step by step) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section39_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 36 (The method, step by step) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter5/rule36_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 37a (The method, step by step) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter5/rule37a_v1.00.html | 2026-11-14 |
| Read for CGST Act section 49 (The method, step by step) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter10/section49_v1.00.html | 2026-11-14 |
| Read for CGST Act section 9 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter3/section9_v1.00.html | 2026-11-14 |
| Read for CGST Act section 37 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section37_v1.00.html | 2026-11-14 |
| Read for CGST Act section 44 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter9/section44_v1.00.html | 2026-11-14 |
| Read for CGST Act section 2 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter1/section2_v1.00.html | 2026-11-14 |
| Read for IGST Act section 14 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_IGST_Act/active/chapterv/section14_v1.00.html | 2026-11-14 |
| Read for IGST Act section 16 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_IGST_Act/active/chaptervii/section16_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 37 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter5/rule37_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 42 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter5/rule42_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 43 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter5/rule43_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 46 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule46_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 60 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter8/rule60_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 88c (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter9/rule88c_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 88d (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter9/rule88d_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 96a (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter10/rule96a_v1.00.html | 2026-11-14 |
| Read for CGST Rules rule 89 (the source list of the earlier version) | https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter10/rule89_v1.00.html | 2026-11-14 |
| Read for the portal address only (GST common portal home), named in the source list of the earlier version | https://www.gst.gov.in | 2026-11-14 |
| einvoice1.gst.gov.in, portal named in the source list of the earlier version | https://einvoice1.gst.gov.in | Timed out on 2026-11-14, not read |
| ewaybillgst.gov.in, portal named in the source list of the earlier version | https://ewaybillgst.gov.in | Timed out on 2026-11-14, not read |
| Current central rate schedules and amendments | https://egazette.gov.in/WriteReadData/2025/266209.pdf#page=76 and https://egazette.gov.in/WriteReadData/2026/277454.pdf#page=2 | 2026-11-24 |
| Current goods exemption schedule | https://egazette.gov.in/WriteReadData/2025/266210.pdf#page=20 | 2026-11-24 |
| September 2025 services rate and exemption changes | https://egazette.gov.in/WriteReadData/2025/266220.pdf#page=9 | 2026-11-24 |
| February 2026 pan masala and tobacco rate changes | https://egazette.gov.in/WriteReadData/2025/268978.pdf#page=3 | 2026-11-24 |
| November 2026 services rates, reverse charge and operator liability | https://egazette.gov.in/WriteReadData/2026/277456.pdf#page=6 | 2026-11-24 |
| November 2026 Rules and January 2027 recipient e-invoicing commencement | https://egazette.gov.in/WriteReadData/2026/277451.pdf#page=113 | 2026-11-24 |
| Maharashtra goods rate schedules | https://mahagst.gov.in/public/uploads/mvatservices/1760688140Notification%20No.%209_2025-State%20Tax%20%28Rate%29.pdf | 2026-11-24 |
| Maharashtra legal and professional services rates, heading 9982 and heading 9983 | https://mahagst.gov.in/public/uploads/mvatservices/1760596631State%20Tax%20%28Rate%29_Notification_11%20of%202017%20updated%20upto_31032025_compressed_0.pdf | 2026-11-24 |
| Annual return exemption from FY 2024-25 onward | https://egazette.gov.in/WriteReadData/2025/266213.pdf#page=3 | 2026-11-24 |
| Current section 50(3) interest rate, Finance Act 2022 section 116 and Sixth Schedule | https://egazette.gov.in/WriteReadData/2022/234693.pdf#page=144 | 2026-11-24 |
| Finance Act 2026 section 157, intermediary place of supply | https://egazette.gov.in/WriteReadData/2026/271439.pdf#page=78 | 2026-11-24 |
| GSTR-3B tables and e-commerce supplies | https://tutorial.gst.gov.in/userguide/returns/Create_and_Submit_GSTR3B.htm | 2026-11-24 |
| GSTR-1 tables | https://tutorial.gst.gov.in/userguide/returns/Creation_of_Outward_Supplies_Return_in_GSTR-1.htm | 2026-11-24 |
| QRMP entry, Notification 84/2020-Central Tax | https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-84-central-tax-english-2020.pdf | 2026-11-24 |
| Legal services prior-year threshold exemption | https://gstcouncil.gov.in/sites/default/files/2024-05/download_2024-05-17t162437.456.pdf | 2026-11-24 |
| Reverse charge on imports of services | https://gstcouncil.gov.in/sites/default/files/2024-02/10-reverse_charge-igst-01.04.2019.pdf | 2026-11-24 |
| Health Security se National Security Cess | https://dor.gov.in/files/acts_files/Act.pdf and https://www.dor.gov.in/files/rules_files/Rule.pdf | 2026-11-24 |


The two transaction portals could not be opened directly on 24 November 2026. Verify portal-specific workflows with GSTN guidance. Use the relevant State or UT instruments for local late fees and any rate variation.
