---
name: vietnam-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Vietnam VAT (thuế giá trị gia tăng / GTGT) return, classify transactions for Vietnamese VAT purposes, or advise on VAT registration and filing in Vietnam. Trigger on phrases like "thuế GTGT", "Vietnam VAT", "tờ khai thuế GTGT", "hóa đơn điện tử", "phương pháp khấu trừ", "phương pháp trực tiếp", or any Vietnam VAT request. ALWAYS read this skill before touching any Vietnam VAT work.
version: 2.0
jurisdiction: VN
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Vietnam VAT (Thuế Giá Trị Gia Tăng / GTGT) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Vietnam (Cộng hòa Xã hội chủ nghĩa Việt Nam) |
| Tax | Thuế Giá Trị Gia Tăng (GTGT — VAT) |
| Currency | VND (Vietnamese Dong / đồng) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Standard rate | 10% |
| Reduced rate | 5% (clean water, fertilizers, animal feed, medical equipment, teaching aids, books, scientific-technical services for agriculture, sugar, unprocessed agricultural products sold by non-farmers) |
| Zero rate | 0% (exports of goods and services; international transport) |
| Exempt | Financial services, insurance, health care, education and training, land use right transfers, housing sold by developers (first sale), postal services (universal), cultural/artistic activities |
| Registration threshold | VND 1,000,000,000 (1 billion VND) per year |
| Tax authority | Tổng cục Thuế (General Department of Taxation — GDT) |
| Return forms | Mẫu 01/GTGT (monthly/quarterly, deduction method); Mẫu 04/GTGT (direct method) |
| Filing frequency | Monthly (if prior year revenue > VND 50 billion); quarterly (if ≤ VND 50 billion) |
| Filing deadline | Monthly: 20th of following month; Quarterly: 30th of month following quarter end |
| e-Invoice | Hóa đơn điện tử — mandatory since 2022 under Decree 123/2020 |
| Tax invoice (VAT invoice) | Hóa đơn GTGT — required for deduction method input credits |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Vietnam-licensed tax agent (đại lý thuế) or CPA |
| Skill version | 2.0 |

### Key return form lines (Mẫu 01/GTGT — Deduction method)

| Line | Meaning |
|---|---|
| [26] | Taxable sales at 10% (doanh thu chịu thuế 10%) |
| [27] | Output VAT at 10% |
| [28] | Taxable sales at 5% |
| [29] | Output VAT at 5% |
| [30] | Zero-rated sales (xuất khẩu) |
| [31] | Exempt sales (không chịu thuế) |
| [32] | Total output VAT ([27]+[29]) |
| [33] | Total input VAT claimed (thuế GTGT đầu vào) |
| [34] | Non-deductible input VAT |
| [35] | Net input VAT ([33]−[34]) |
| [40] | VAT payable ([32]−[35]) |
| [41] | Excess credit carried forward |
| [42] | Net payable after prior credit |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 10% standard |
| Unknown whether 5% rate applies | 10% until confirmed |
| Unknown counterparty country | Domestic Vietnam |
| Unknown export qualification | Domestic 10% until evidence confirmed |
| Unknown business-use % | 0% input credit |
| Unknown whether e-invoice compliant | No input credit |
| Unknown B2B vs B2C for cross-border | Taxable at 10% (domestic consumption assumed) |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | VND 50,000,000 |
| HIGH tax delta on single default | VND 5,000,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net VAT position | VND 20,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Confirmation of VAT calculation method (deduction 方法khấu trừ or direct 方法trực tiếp) and MST (Mã số thuế — 10-digit tax code).

**Recommended** — hóa đơn GTGT (VAT invoices) for all purchases, electronic invoices (hóa đơn điện tử) for sales, prior period return and excess credit carried forward.

**Ideal** — complete ledger, export customs declarations (tờ khai hải quan), asset register, full invoice register.

**Refusal if minimum missing — SOFT WARN.** No bank statement = hard stop. "Input VAT credits in Vietnam require compliant hóa đơn GTGT (VAT invoices) or hóa đơn điện tử. All credits are provisional pending invoice verification."

### Refusal catalogue

**R-VN-1 — Direct method taxpayers (phương pháp trực tiếp).** "Direct method taxpayers pay VAT on the value-added margin, not on gross output minus gross input. They cannot claim input credits in the same way. Confirm the calculation method before proceeding. This skill primarily covers the deduction method."

**R-VN-2 — Businesses below VND 1 billion threshold.** "Businesses below the registration threshold use a simplified approach. Confirm registration status before proceeding."

**R-VN-3 — Partial exemption proration.** "If the business makes both taxable and exempt supplies, input VAT must be apportioned. Apportionment requires the taxable/total revenue ratio for the year. Out of scope without full-year data — escalate."

**R-VN-4 — Real estate and construction.** "Real estate development and construction have special VAT treatment for housing and land. Out of scope — escalate to a licensed tax agent."

**R-VN-5 — Foreign contractor withholding tax (FCT).** "Foreign contractors providing services in Vietnam are subject to Foreign Contractor Tax (FCT = CIT + VAT withholding). FCT is different from the regular GTGT return. Out of scope."

---

## Section 3 — Supplier pattern library

Match by case-insensitive substring on counterparty name or reference. Most specific match wins. Fall through to Section 5 if no match.

### 3.1 Vietnamese banks — fees and charges (exempt / exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| VIETCOMBANK, NGÂN HÀNG NGOẠI THƯƠNG, VCB | EXCLUDE (fee lines) | Financial service — exempt from GTGT |
| BIDV, NGÂN HÀNG ĐẦU TƯ VÀ PHÁT TRIỂN | EXCLUDE (fee lines) | Same |
| VIETINBANK, NGÂN HÀNG CÔNG THƯƠNG, CTG | EXCLUDE (fee lines) | Same |
| AGRIBANK, NGÂN HÀNG NÔNG NGHIỆP | EXCLUDE (fee lines) | Same |
| TECHCOMBANK, TCB | EXCLUDE (fee lines) | Same |
| VPBANK, NGÂN HÀNG VIỆT NAM THỊNH VƯỢNG | EXCLUDE (fee lines) | Same |
| MB BANK, NGÂN HÀNG QUÂN ĐỘI | EXCLUDE (fee lines) | Same |
| ACB, NGÂN HÀNG Á CHÂU | EXCLUDE (fee lines) | Same |
| SACOMBANK | EXCLUDE (fee lines) | Same |
| TPBANK | EXCLUDE (fee lines) | Same |
| PHÍ DỊCH VỤ, LÃI SUẤT, INTEREST, FEE | EXCLUDE | Bank fee/interest — exempt |

### 3.2 Vietnamese government and statutory (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| TỔNG CỤC THUẾ, CỤC THUẾ, TAX AUTHORITY | EXCLUDE | Tax payment |
| THUẾ GTGT, THUẾ TNDN, THUẾ TNCN | EXCLUDE | Tax remittance |
| BẢO HIỂM XÃ HỘI, BHXH, SOCIAL INSURANCE | EXCLUDE | Social insurance |
| BẢO HIỂM Y TẾ, BHYT | EXCLUDE | Health insurance |
| HẢI QUAN, CUSTOMS | EXCLUDE | Customs duty |
| BHTN, BẢO HIỂM THẤT NGHIỆP | EXCLUDE | Unemployment insurance |

### 3.3 Vietnamese utilities (taxable at 10%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| EVN, TẬP ĐOÀN ĐIỆN LỰC, ĐIỆN LỰC | Input 10% | 10% | Electricity — standard rate |
| CÔNG TY ĐIỆN LỰC (regional utilities) | Input 10% | 10% | Regional electricity distribution |
| SAWACO, HAWACO, CẤP NƯỚC (water company) | Input 5% | 5% | Clean water — reduced rate 5% |
| VIETTEL TELECOM | Input 10% | 10% | Telecom — standard rate |
| VNPT, VIỄN THÔNG VIỆT NAM | Input 10% | 10% | Telecom — standard rate |
| MOBIFONE | Input 10% | 10% | Mobile — standard rate |
| VIETNAMOBILE | Input 10% | 10% | Mobile — standard rate |
| GMOBILE | Input 10% | 10% | Mobile — standard rate |

### 3.4 Transport and logistics

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| VIETNAM AIRLINES, VNA, HÀNG KHÔNG VIỆT NAM | Check route | 0%/10% | International 0%; domestic 10% |
| VIETJET AIR, VIETJET | Check route | 0%/10% | International 0%; domestic 10% |
| BAMBOO AIRWAYS | Check route | 0%/10% | International 0%; domestic 10% |
| VIETRAVEL AIRLINES | Check route | 0%/10% | Domestic 10%; international 0% |
| ĐƯỜNG SẮT VIỆT NAM, VNR, RAILWAY | Input 10% | 10% | Rail — taxable |
| GRAB VIETNAM | Input 10% | 10% | Ride-hailing — taxable |
| BE (taxi app), BEE TAXI | Input 10% | 10% | Ride-hailing — taxable |
| GIAO HÀNG TIẾT KIỆM, GHTK | Input 10% | 10% | Courier — taxable |
| GIAO HÀNG NHANH, GHN | Input 10% | 10% | Courier — taxable |
| VIETTEL POST | Input 10% | 10% | Courier — taxable |
| VIETNAM POST, BƯU ĐIỆN (parcel) | Input 10% | 10% | Parcel services — taxable |
| VIETNAM POST, BƯU ĐIỆN (stamps) | EXEMPT | 0% | Universal postal stamps — exempt |
| J&T EXPRESS VIETNAM | Input 10% | 10% | Courier — taxable |
| NINJA VAN VIETNAM | Input 10% | 10% | Courier — taxable |

### 3.5 Food and retail

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| WINMART, VINMART, WINCOMMERCE | Input 10% | 10% | Supermarket — 10% (no food reduced rate in Vietnam at retail level) |
| BIG C VIỆT NAM (now GO!) | Input 10% | 10% | Hypermarket — 10% |
| AEON VIỆT NAM | Input 10% | 10% | Department store — 10% |
| BÁN LẺ (retail), NHÀ HÀNG (restaurant) | Input 10% | 10% | Standard rate — taxable |
| CO.OPMART, SAIGON CO.OP | Input 10% | 10% | Supermarket — 10% |
| LOTTE MART VIỆT NAM | Input 10% | 10% | Hypermarket — 10% |
| PHÂN BÓN, THUỐC TRỪ SÂU (fertilizers/pesticides) | Input 5% | 5% | Agricultural inputs — reduced 5% |

### 3.6 SaaS — local Vietnamese suppliers (10%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| MISA, PHẦN MỀM MISA | Input 10% | 10% | Vietnamese accounting SaaS |
| FAST ACCOUNTING | Input 10% | 10% | Vietnamese accounting software |
| VIETTEL CLOUD | Input 10% | 10% | Cloud services — 10% |
| VNPT CLOUD | Input 10% | 10% | Cloud services — 10% |
| VTC PAY | Input 10% | 10% | Vietnamese payment — taxable |

### 3.7 SaaS — international suppliers (foreign contractor tax / FCT note)

Foreign digital service providers in Vietnam: for B2B, the Vietnamese buyer may be required to withhold Foreign Contractor Tax (FCT = VAT component + CIT component). The VAT portion of FCT is generally not creditable as input VAT. This is complex — flag for specialist review.

| Pattern | Notes |
|---|---|
| GOOGLE (Workspace, Ads, Cloud) | FCT applies — flag; may be registered via Google's Vietnam registration |
| MICROSOFT (365, Azure) | FCT may apply — check if Vietnam entity invoices |
| META, FACEBOOK ADS | FCT applies — flag |
| ZOOM, SLACK, NOTION, OPENAI | FCT applies — flag for specialist |
| AWS | FCT applies — flag |

### 3.8 Payment processors (exempt fees)

| Pattern | Treatment | Notes |
|---|---|---|
| VNPAY (phí giao dịch) | EXCLUDE | Payment processing fee — exempt |
| MOMO (phí) | EXCLUDE | E-wallet fee — exempt |
| ZALOPAY (phí) | EXCLUDE | Payment fee — exempt |
| PAYOO (phí) | EXCLUDE | Payment fee — exempt |

### 3.9 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| CHUYỂN KHOẢN NỘI BỘ, INTERNAL | EXCLUDE | Internal movement |
| VAY VỐN, TRẢ NỢ, LOAN | EXCLUDE | Loan principal |
| LƯƠNG, TIỀN LƯƠNG, SALARY | EXCLUDE | Wages — outside VAT scope |
| CỔ TỨC, DIVIDEND | EXCLUDE | Out of scope |
| ĐẶT CỌC, DEPOSIT | EXCLUDE | Deposit — out of scope until applied |
| RÚT TIỀN, ATM | Tier 2 — ask | Default exclude |

---

## Section 4 — Worked examples

Six classifications from a hypothetical Ho Chi Minh City-based IT consultant. Format: Vietcombank (VCB) transaction history.

### Example 1 — Domestic B2B revenue (10%)

**Input line:**
`15/04/2025  Nhận chuyển khoản  CÔNG TY TNHH ABC TECHNOLOGY  ND: HD GTGT SO 001/2025  +110,000,000  VND`

**Reasoning:**
Incoming VND 110,000,000 from a Vietnamese company for IT consulting. Standard 10% VAT. Gross VND 110,000,000 includes VAT. Net = VND 100,000,000 (doanh thu chịu thuế) + VND 10,000,000 output GTGT. An electronic VAT invoice (hóa đơn GTGT điện tử) must be issued and transmitted to GDT. Report net on line [26].

**Classification:** Output VAT 10% — VND 10,000,000. Net sales: VND 100,000,000.

### Example 2 — Export service (zero-rated)

**Input line:**
`22/04/2025  Nhận ngoại tệ  ACME CORPORATION USA  Technical consulting Q1/2025  +USD 5,000 (VND 125,000,000)`

**Reasoning:**
USD receipt from a US company for services. Zero-rated if the service is provided to a foreign entity and consumed outside Vietnam. Evidence: signed contract, bank transfer showing USD payment. Report VND 125,000,000 on line [30] (zero-rated). Output VAT: VND 0. Conservative default: 10% if export status cannot be confirmed.

**Classification:** Zero-rated exports — VND 125,000,000. Output VAT: VND 0.

### Example 3 — Water utility (5% reduced rate)

**Input line:**
`10/04/2025  Thanh toán tự động  SAWACO - CẤP NƯỚC SAIGON  Tiền nước tháng 3/2025  -2,100,000  VND`

**Reasoning:**
Water bill from SAWACO (Saigon Water Corporation). Clean water is subject to 5% reduced rate VAT. Gross VND 2,100,000. Net = VND 2,000,000 + VND 100,000 input VAT at 5%. SAWACO issues a compliant electronic invoice — input credit of VND 100,000 claimable. Report on line [33] (input VAT).

**Classification:** Input VAT 5% — VND 100,000. Net expense: VND 2,000,000.

### Example 4 — Domestic courier (10%)

**Input line:**
`08/04/2025  Thanh toán  GIAO HÀNG NHANH GHN  Phí vận chuyển tháng 3/2025  -11,000,000  VND`

**Reasoning:**
Courier services from GHN (Giao Hàng Nhanh). Taxable at 10%. Gross VND 11,000,000. Net = VND 10,000,000 + VND 1,000,000 input VAT. GHN is a major registered provider — electronic invoice should be available. Input credit of VND 1,000,000 claimable pending invoice verification.

**Classification:** Input VAT 10% — VND 1,000,000. Net expense: VND 10,000,000.

### Example 5 — Exempt financial service

**Input line:**
`01/04/2025  Lãi tiền gửi  Vietcombank  Lãi tháng 3/2025  +250,000  VND`

**Reasoning:**
Bank deposit interest. Interest income is exempt from VAT in Vietnam. EXCLUDE from the VAT return entirely. This is passive income — not a supply of goods or services for VAT purposes. No output VAT. Note: if the business has significant exempt income, a proration of input VAT may be required.

**Classification:** EXEMPT — exclude from GTGT return. Note any proration implications.

### Example 6 — International software (FCT flag)

**Input line:**
`05/04/2025  Thanh toán quốc tế  GOOGLE IRELAND LIMITED  Google Workspace April 2025  -3,300,000  VND`

**Reasoning:**
Payment to Google Ireland for cloud services. This triggers the Foreign Contractor Tax (FCT) rules in Vietnam. FCT = CIT component (typically 5%) + VAT component (10% of grossed-up amount). The VAT component of FCT is withheld by the Vietnamese buyer and remitted to the GDT — but this withheld VAT is generally NOT creditable as input GTGT. This is a complex area. Flag for specialist: confirm whether Google has registered directly in Vietnam (in which case standard input credit rules apply) or whether FCT withholding is required.

**Classification:** Tier 2 — FLAG for specialist. FCT rules may apply. Do not claim input credit until registration status confirmed.

---

## Section 5 — Tier 1 rules (compressed)

### 5.1 Standard rate 10%

Default rate for all taxable goods and services. Legislation: VAT Law No. 13/2008/QH12 as amended; Circular 219/2013/TT-BTC Article 11.

### 5.2 Reduced rate 5%

Applies to: clean water; fertilizers, animal feed, plant protection chemicals; medical equipment and health services (some — check specifics); teaching aids; books (not newspapers); sugar; unprocessed agricultural products sold by non-farmers to businesses. Legislation: VAT Law Article 9; Circular 219/2013 Article 10.

### 5.3 Zero rate — exports

Exports of goods and services. Services are zero-rated if (1) provided for consumption outside Vietnam, (2) the counterparty is a foreign entity, (3) payment is made in foreign currency, and (4) the service is not performed in Vietnam (for some categories). Legislation: VAT Law Article 8; Circular 219/2013 Article 9.

### 5.4 Exempt supplies

Financial services (interest, currency exchange, insurance), healthcare and medical, education and vocational training, certain cultural/artistic activities, land use right transfers, housing sold by developer (first sale below certain threshold), universal postal services (stamps, basic postal). Legislation: VAT Law Article 5.

### 5.5 Deduction method (phương pháp khấu trừ)

General taxpayers with annual revenue ≥ VND 1 billion use the deduction method: Output VAT − Input VAT = Net VAT payable. Input credits require compliant hóa đơn GTGT (VAT invoices) or hóa đơn điện tử.

### 5.6 Direct method (phương pháp trực tiếp)

Available to small taxpayers (revenue < VND 1 billion) or businesses in specific sectors (gold, silver, precious metals). Tax = VAT rate × value added (selling price − purchase price). No input credit mechanism. File using Form 04/GTGT.

### 5.7 e-Invoice requirements

From 1 July 2022, all registered businesses must issue electronic invoices (hóa đơn điện tử) registered with the GDT portal. Required fields: seller's MST (tax code), buyer's MST, invoice date, goods/service description, quantity, unit price, net amount, VAT rate, VAT amount, total. Paper invoices no longer accepted for new issuances.

### 5.8 Filing deadlines

| Filer | Period | Due date |
|---|---|---|
| Monthly filer (revenue > VND 50B) | Monthly | 20th of following month |
| Quarterly filer (revenue ≤ VND 50B) | Quarterly | 30th of month following quarter |
| Annual settlement | Calendar year | 31 March following year |

### 5.9 Penalties

| Offence | Penalty |
|---|---|
| Late filing | VND 2,000,000–25,000,000 |
| Late payment | 0.03% per day of unpaid tax |
| Tax evasion | 1×–3× evaded tax + criminal liability |
| False invoice | Administrative + potential criminal |

---

## Section 6 — Tier 2 catalogue

### 6.1 Foreign contractor tax (FCT) on international services

**What it shows:** Payment to a foreign service provider.
**What's missing:** Whether the foreign supplier has registered in Vietnam directly or whether FCT withholding applies.
**Conservative default:** Flag — do not claim input credit until status confirmed.
**Question to ask:** "Has this foreign supplier registered for VAT in Vietnam? Do they issue Vietnamese electronic invoices? If not, FCT withholding may be required."

### 6.2 Export qualification for services

**What it shows:** Revenue from a foreign client.
**What's missing:** Whether the service was consumed outside Vietnam, paid in foreign currency, and the counterparty is a foreign entity.
**Conservative default:** 10% domestic rate.
**Question to ask:** "Was this service entirely consumed outside Vietnam? Is the client a foreign entity? Was payment received in USD/EUR or other foreign currency?"

### 6.3 Reduced rate confirmation (5% items)

**What it shows:** Purchase that might qualify for 5% (e.g., water, agricultural inputs, books).
**What's missing:** Confirmation of specific product category.
**Conservative default:** 10%.
**Question to ask:** "What exactly was purchased? Is it on the 5% reduced rate list (clean water, fertilizer, animal feed, medical equipment, books, etc.)?"

### 6.4 Partial exemption — businesses with mixed supplies

**What it shows:** Business making both taxable and exempt sales (e.g., IT consulting + financial advisory).
**What's missing:** The taxable/total revenue ratio for the period.
**Conservative default:** 0% credit on shared overhead costs.
**Question to ask:** "What proportion of your sales are taxable vs. exempt? Provide a monthly revenue breakdown."

### 6.5 VAT on vehicle expenses

**What it shows:** Vehicle purchase, lease, fuel, or maintenance.
**What's missing:** Whether the vehicle is used exclusively for business and whether input VAT is claimable.
**Conservative default:** 0% input credit.
**Question to ask:** "Is this vehicle registered in the company's name and used exclusively for business? VAT on personal-use or mixed vehicles is limited."

---

## Section 7 — Excel working paper template

```
VIETNAM VAT WORKING PAPER — BẢNG TÍNH THUẾ GTGT
Kỳ khai thuế (Period): ____________  MST: ____________

A. THUẾ ĐẦU RA (OUTPUT VAT)
  A1. Doanh thu chịu thuế 10% (net)           ___________
  A2. Thuế đầu ra 10% (A1 × 10%)              ___________
  A3. Doanh thu chịu thuế 5% (net)            ___________
  A4. Thuế đầu ra 5% (A3 × 5%)                ___________
  A5. Xuất khẩu 0% (net)                      ___________
  A6. Doanh thu không chịu thuế (net)         ___________
  A7. Tổng thuế đầu ra (A2 + A4)              ___________

B. THUẾ ĐẦU VÀO (INPUT VAT)
  B1. Mua hàng chịu thuế 10% (net)            ___________
  B2. Thuế đầu vào 10% (B1 × 10%)             ___________
  B3. Mua hàng chịu thuế 5% (net)             ___________
  B4. Thuế đầu vào 5% (B3 × 5%)               ___________
  B5. Thuế nhập khẩu đã nộp                   ___________
  B6. Tổng thuế đầu vào (B2+B4+B5)           ___________
  B7. Thuế đầu vào không được khấu trừ        ___________
  B8. Thuế đầu vào được khấu trừ (B6−B7)      ___________

C. THUẾ PHẢI NỘP
  C1. Chênh lệch thuế (A7 − B8)               ___________
  C2. Thuế còn được khấu trừ kỳ trước         ___________
  C3. Thuế GTGT phải nộp (C1 − C2)            ___________
  C4. Hoặc: Thuế còn được khấu trừ (nếu C1<C2) ___________

REVIEWER FLAGS:
  [ ] Hóa đơn điện tử confirmed for all input credits?
  [ ] Export evidence available for zero-rated sales?
  [ ] FCT status confirmed for all international service payments?
  [ ] 5% rate items correctly identified?
  [ ] Proration calculated for any exempt supplies?
```

---

## Section 8 — Bank statement reading guide

### Common Vietnamese bank statement formats

| Bank | Key columns | Date format | Amount |
|---|---|---|---|
| Vietcombank VCB | Ngày GD, Nội dung, Phát sinh nợ (debit), Phát sinh có (credit), Số dư | DD/MM/YYYY | VND (no decimals typically) |
| BIDV | Ngày, Mô tả, Số tiền ghi nợ, Số tiền ghi có, Số dư | DD/MM/YYYY | VND |
| Vietinbank | Ngày giao dịch, Nội dung, Số tiền, Số dư | DD/MM/YYYY | VND |
| Techcombank | Thời gian, Mô tả giao dịch, Số tiền ghi nợ, Số tiền ghi có, Số dư | DD/MM/YYYY | VND |
| MB Bank | Ngày, Nội dung giao dịch, Phát sinh, Số dư | DD/MM/YYYY | VND |

### Key Vietnamese banking terms

| Vietnamese | Meaning | Classification hint |
|---|---|---|
| Nhận chuyển khoản | Incoming wire transfer | Potential revenue |
| Thanh toán / Chuyển khoản | Outgoing payment | Potential expense |
| Nhận ngoại tệ | Foreign currency receipt | Potential export |
| Lãi tiền gửi | Deposit interest | Exempt |
| Phí dịch vụ | Service fee | Bank charge — exempt |
| Số dư | Balance | Running balance — ignore |
| Nội dung | Transaction description / narrative | Key classification field |
| Thuế GTGT | VAT | Tax payment — exclude |
| Rút tiền ATM | ATM withdrawal | Tier 2 — ask |
| Thanh toán tự động | Auto-payment | Subscription/utility |

---

## Section 9 — Onboarding fallback

If the client provides a bank statement but cannot answer all questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Apply conservative defaults (Section 1)
3. Mark Tier 2 items as "PENDING — reviewer must confirm"
4. Generate working paper with flags

```
VIETNAM GTGT ONBOARDING — CÂU HỎI TỐI THIỂU
1. Mã số thuế (MST — 10-digit tax code)?
2. Phương pháp tính thuế: khấu trừ (deduction) hay trực tiếp (direct)?
3. Kỳ khai thuế: theo tháng hay theo quý?
4. Doanh thu năm trước (for determining monthly vs. quarterly)?
5. Có doanh thu xuất khẩu (zero-rated) không?
   Nếu có: paid in foreign currency? Hợp đồng với đối tác nước ngoài?
6. Có dịch vụ quốc tế (Google, Microsoft, etc.) không?
   Có hóa đơn GTGT từ nhà cung cấp nước ngoài không?
7. Số thuế GTGT còn được khấu trừ kỳ trước (excess credit carried forward)?
8. Có doanh thu không chịu thuế (exempt supplies) không?
```

---

## Section 10 — Reference material

### Key legislation

| Topic | Reference |
|---|---|
| VAT Law | Luật Thuế GTGT No. 13/2008/QH12 (amended 2013, 2014, 2016) |
| VAT rates | VAT Law Articles 8–10 |
| Exempt supplies | VAT Law Article 5 |
| Calculation methods | Circular 219/2013/TT-BTC |
| e-Invoice | Decree 123/2020/ND-CP; Circular 78/2021/TT-BTC |
| Export zero-rating | VAT Law Article 8; Circular 219/2013 Article 9 |
| Foreign contractor tax | Circular 103/2014/TT-BTC |
| Registration threshold | VAT Law Article 13 |
| Penalties | Law on Tax Administration No. 38/2019/QH14 |

### Known gaps

- Foreign Contractor Tax (FCT) computation — complex; escalate to specialist
- Partial exemption proration — requires full-year data; escalate
- Real estate and construction VAT — escalate
- Non-commercial import VAT — escalate
- Agricultural cooperative special rules — escalate

### Self-check before filing

- [ ] All hóa đơn điện tử (e-invoices) transmitted to GDT for sales
- [ ] All input credits supported by compliant electronic invoices
- [ ] Export zero-rating supported by contracts + FX transfer evidence
- [ ] FCT implications flagged for all international service payments
- [ ] 5% vs. 10% rate correctly applied where applicable
- [ ] Prior period excess credit correctly carried forward

### Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2024 | Initial release |
| 2.0 | April 2026 | Full v2.0 rewrite: pattern library, worked examples, FCT note, no inline tier tags |

---

## Prohibitions

- NEVER claim input VAT credit without a compliant hóa đơn điện tử (e-invoice)
- NEVER zero-rate a service without confirming foreign consumption + FX payment
- NEVER use the deduction method for a direct-method taxpayer
- NEVER ignore FCT implications for international service payments
- NEVER present calculations as definitive — direct to a licensed Vietnamese tax agent (đại lý thuế)

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at openaccountants.com.
