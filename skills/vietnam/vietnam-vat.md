---
name: vietnam-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Vietnam VAT (thuế giá trị gia tăng / GTGT) return, classify transactions for Vietnamese VAT purposes, or advise on VAT registration and filing in Vietnam. Trigger on phrases like "thuế GTGT", "Vietnam VAT", "tờ khai thuế GTGT", "hóa đơn điện tử", "phương pháp khấu trừ", "phương pháp trực tiếp", or any Vietnam VAT request. ALWAYS read this skill before touching any Vietnam VAT work.
version: 2.0
jurisdiction: VN
tax_year: 2026
last_updated: 2026-10-17
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Vietnam VAT (thuế giá trị gia tăng, GTGT): rates, methods, input credit, returns and refunds

This Guide covers Vietnam's value added tax for a business that sells goods or services in Vietnam: which rate applies, which calculation method the business must use, when input VAT can be credited, how foreign suppliers and digital platforms are taxed, and when returns and payments are due. Figures are for tax year 2026. VAT is not year-based: this Guide states the rules in force on 17 October 2026 under the VAT Law 48/2024/QH15 (in force from 1 July 2025, as amended) and its implementing Decree 181/2025/ND-CP, with the date each rule started. The temporary 8% rate ends on 31 December 2026. From 1 July 2026 filing and payment are governed by the Law on Tax Administration 108/2025/QH15 and Decree 252/2026/ND-CP. The old VAT Law 13/2008/QH12, Decree 209/2013/ND-CP, Circular 219/2013/TT-BTC, Law 38/2019/QH14 and Decree 126/2020/ND-CP are no longer the law and must not be cited as current.

## Section 1: Quick reference

**Quick reference fields**

| Field | Value |
| --- | --- |
| Country | Vietnam (Cộng hòa Xã hội chủ nghĩa Việt Nam) |
| Tax | Thuế giá trị gia tăng (GTGT), value added tax |
| Currency | Tax is declared in Vietnamese dong (Đồng Việt Nam), except cases the Government sets (Law 108/2025/QH15, table in Section 5.8) |
| VAT law | Law on Value Added Tax 48/2024/QH15 of 26 November 2024, in force 1 July 2025, amended by Resolution 204/2025/QH15, Law 90/2025/QH15, Law 149/2025/QH15 (from 1 January 2026) and Law 09/2026/QH16 (passed 24 April 2026) |
| Implementing decree | Decree 181/2025/ND-CP of 1 July 2025 (replaced Decree 209/2013/ND-CP), amended by Decree 359/2025/ND-CP and Decree 144/2026/ND-CP (from 20 June 2026) |
| Ministry of Finance guidance | Circular 69/2025/TT-BTC (replaced Circular 219/2013/TT-BTC) |
| Tax administration | Law 108/2025/QH15 and Decree 252/2026/ND-CP, both from 1 July 2026 (replacing Law 38/2019/QH14 and Decree 126/2020/ND-CP) |
| Tax authority | The tax authority (cơ quan Thuế): Cục Thuế (Tax Department), Chi cục Thuế doanh nghiệp lớn (large taxpayers), Chi cục Thuế thương mại điện tử (e-commerce), and provincial and city tax offices and grassroots tax offices (Decree 252/2026/ND-CP: "Cơ quan Thuế bao gồm Cục Thuế, Chi cục Thuế doanh nghiệp lớn, Chi cục Thuế thương mại điện tử, Thuế tỉnh, thành phố và Thuế cơ sở") |
| Rates | 0%, 5%, 10%, and the temporary 8% on most of the 10% group until 31 December 2026 (tables below) |
| Calculation methods | Credit (deduction) method, phương pháp khấu trừ; direct method on revenue or on value added, phương pháp tính trực tiếp (Section 5.5 and 5.6) |
| Revenue level below which there is no VAT | Only for household and individual businesses (table below). Companies have no such level: a company that sells taxable goods or services is a VAT payer |
| Invoices | Credit-method businesses issue VAT invoices (hóa đơn giá trị gia tăng); direct-method businesses issue sales invoices (hóa đơn bán hàng) (VAT Law Art. 16) |
| Filing | Monthly or quarterly return; deadlines in Section 5.8. Which businesses may file quarterly under the 2026 rules is not settled in this Guide (Section 5.8) |

### Rates, method threshold, direct-method percentages and refund thresholds in the VAT Law

All rows come from the consolidated VAT Law published by the National Assembly Office (12/VBHN-VPQH, February 2026). That text does not include Law 09/2026/QH16; the household threshold is therefore in the Decree 141/2026 table below, not here.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf |
| Zero rate: exported goods, exported services, international transport and the other exports listed in Art. 9(1), except the cases in Art. 9(1)(d) | 0% | "Điều 9. Thuế suất 1. Mức thuế suất 0% áp dụng đối với hàng hóa, dịch vụ sau đây" |
| Reduced rate: only the goods and services listed in Art. 9(2) (Section 5.2) | 5% | "2. Mức thuế suất 5% áp dụng đối với hàng hóa, dịch vụ sau đây: a) Nước sạch" |
| Standard rate: every taxable good or service not at 0% or 5% | 10% | "Mức thuế suất 10% áp dụng đối với hàng hóa, dịch vụ không quy định tại khoản 1 và khoản 2 Điều này" |
| The standard rate includes services sold by foreign suppliers without a permanent establishment to organisations and individuals in Vietnam through e-commerce and digital platforms (Art. 9(3)) | 10% | "10% áp dụng đối với hàng hóa, dịch vụ không quy định tại khoản 1 và khoản 2 Điều này, bao gồm cả dịch vụ được các nhà cung cấp nước ngoài" |
| Temporary rate for the 10% group, 1 July 2025 to 31 December 2026, except telecoms, finance, banking, securities, insurance, real estate business, metal products, mining products (except coal), and goods and services subject to special consumption tax (except petrol) (Resolution 204/2025/QH15) | 8% | "(còn 8%), trừ một số nhóm hàng hóa, dịch vụ sau: viễn thông, hoạt động tài chính, ngân hàng, chứng khoán, bảo hiểm, kinh doanh bất động sản, sản phẩm kim loại, sản phẩm khai khoáng (trừ than), sản phẩm hàng hóa và dịch vụ chịu thuế tiêu thụ đặc biệt (trừ xăng)" |
| Size of that temporary reduction on the 10% group | 2% cut | "Giảm 2% thuế suất thuế giá trị gia tăng, áp dụng đối với các nhóm hàng hóa, dịch vụ quy định tại khoản 3 Điều 9" |
| Credit method is compulsory for a business (not a household or individual business) whose annual revenue from goods and services is at or above, and which keeps full accounts, invoices and records | VND 1 billion | "Cơ sở kinh doanh có doanh thu hằng năm từ bán hàng hóa, cung cấp dịch vụ từ 01 tỷ đồng trở lên, trừ hộ, cá nhân sản xuất, kinh doanh" |
| Enterprises and cooperatives with annual revenue below this level use the direct method on revenue unless they register for the credit method | below VND 1 billion | "Doanh nghiệp, hợp tác xã, liên hiệp hợp tác xã có doanh thu hằng năm dưới mức ngưỡng doanh thu 01 tỷ đồng" |
| Direct method on revenue: distribution and supply of goods | 1% | "b1) Phân phối, cung cấp hàng hóa: 1%" |
| Direct method on revenue: services, and construction without supply of materials | 5% | "b2) Dịch vụ, xây dựng không bao thầu nguyên vật liệu: 5%" |
| Direct method on revenue: manufacturing, transport, services attached to goods, construction with supply of materials | 3% | "b3) Sản xuất, vận tải, dịch vụ có gắn với hàng hóa, xây dựng có bao thầu nguyên vật liệu: 3%" |
| Direct method on revenue: other business activities | 2% | "b4) Hoạt động kinh doanh khác: 2%" |
| Export refund: input VAT not yet credited, at or above, in a month or quarter with exports (not for goods imported and then re-exported) | VND 300 million | "nếu có số thuế giá trị gia tăng đầu vào chưa được khấu trừ hết từ 300 triệu đồng trở lên thì được hoàn thuế giá trị gia tăng theo tháng, quý" |
| Cap on the export refund, as a share of export revenue of the refund period (a cap, not a VAT rate) | 10% | "Số thuế giá trị gia tăng được hoàn của hàng hóa, dịch vụ xuất khẩu không vượt quá 10% doanh thu" |
| Investment-project refund: project input VAT not yet credited after offset, at or above | VND 300 million | "Sau khi bù trừ nếu số thuế giá trị gia tăng đầu vào của dự án đầu tư chưa được khấu trừ hết từ 300 triệu đồng trở lên" |
| Business that supplies only 5% goods or services: input VAT not yet credited, at or above, after 12 consecutive months or 4 consecutive quarters | VND 300 million | "nếu có số thuế giá trị gia tăng đầu vào chưa được khấu trừ hết từ 300 triệu đồng trở lên sau 12 tháng liên tục hoặc 04 quý liên tục" |

### The temporary 8% under Decree 174/2025/ND-CP

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45374/57334-1-2025895-896174-2025-nd-cp.pdf |
| Credit-method businesses: rate on goods and services that qualify for the reduction (Art. 1(1)); the VAT invoice shows "8%" | 8% | "thuế giá trị gia tăng 8% đối với hàng hóa, dịch vụ quy định tại khoản 1 Điều này" |
| Direct-method businesses, including household and individual businesses: reduction of the revenue percentage when invoicing qualifying goods and services. It is a reduction of the percentage itself, not a cut in percentage points | 20% reduction of the direct-method percentage | "được giảm 20% mức tỷ lệ % để tính thuế giá trị gia tăng khi thực hiện xuất hóa đơn" |
| Period | 1 July 2025 to 31 December 2026 | "Nghị định này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2025 đến hết ngày 31 tháng 12 năm 2026" |

Goods and services that are not subject to VAT or that sit at 5% under the VAT Law get no reduction, even if they appear in the Decree's annexes ("thì thực hiện theo quy định của Luật Thuế giá trị gia tăng và không được giảm thuế giá trị gia tăng"). Annex I lists the excluded telecoms, finance, banking, securities, insurance, real estate, metal and mining items by product code; Annex II lists the excluded special-consumption-tax items. The reduced items are declared on Form 01 in Annex III, filed with the VAT return. No extension past 31 December 2026 was found on 17 October 2026: from 1 January 2027 the 10% rate applies again unless a new resolution says otherwise.

### Household and individual businesses (Decree 141/2026/ND-CP)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/14/469455-1778231931_v1_1778720623_signed.pdf |
| Annual revenue at or below which a household or individual business is not subject to VAT, from 1 January 2026 (Decree 141 replaced the earlier figure in Decree 68/2026/ND-CP Art. 3) | VND 1 billion | "Sửa đổi cụm từ “500 triệu đồng” thành “01 tỷ đồng” tại Điều 3" |
| Household and individual businesses with annual revenue above this level must use e-invoices with a tax-authority code, or e-invoices generated from cash registers connected to the tax authority | VND 1 billion | "Hộ kinh doanh, cá nhân kinh doanh có doanh thu năm trên 01 tỷ đồng thì phải áp dụng hóa đơn điện tử có mã của cơ quan thuế" |
| A household whose cumulative revenue passes that level during the year registers for e-invoices within this period from the last day of the tax period in which it passed | 30 days | "đăng ký sử dụng hóa đơn điện tử trong thời gian 30 ngày kể từ ngày cuối cùng của kỳ tính thuế" |
| Start date | 1 January 2026 | "Nghị định này có hiệu lực thi hành từ ngày 01 tháng 01 năm 2026" |

Law 09/2026/QH16 rewrote VAT Law Art. 5(25): the household threshold is now "the level set by the Government" ("doanh thu năm từ mức quy định của Chính phủ trở xuống"), with effect from 1 January 2026 ([Law 09/2026/QH16](https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/27/469536-1779329464_v1_1779843299_signed.pdf): "Quy định tại các điều 1, 2 và 3 của Luật này có hiệu lực thi hành từ ngày 01 tháng 01 năm 2026"). The consolidated VAT Law of February 2026 and Decree 68/2026/ND-CP as first published still print an older, lower figure. Do not use it. Revenue exactly at the threshold is still not subject ("trở xuống" means "or less"). A household or individual business above the threshold is subject to VAT and must use the direct method on revenue ([Decree 68/2026/ND-CP](https://congbaocdn.chinhphu.vn/180507251028987904/2026/3/18/469047-1773796836_v1_1773803477_signed.pdf), threshold as amended by Decree 141/2026/ND-CP: "thuộc đối tượng chịu thuế giá trị gia tăng và áp dụng phương pháp tính trực tiếp").

### Key return form lines

The live version of this Guide gave box numbers for the credit-method return (Mẫu 01/GTGT). No allowed page prints that form, and the forms that go with Decree 252/2026/ND-CP are set by a Ministry of Finance circular this Guide could not read. The box numbers are therefore not reproduced. Map amounts to the form by the meaning of each line:

**Return lines by meaning (credit method)**

| Meaning | What goes there |
| --- | --- |
| Sales not subject to VAT | Revenue from Art. 5 goods and services (no output VAT) |
| Sales at 0% | Exports meeting the 0% conditions (no output VAT) |
| Sales at 5% and the VAT on them | Net revenue and output VAT |
| Sales at 10% and the VAT on them | Net revenue and output VAT, for items outside the temporary cut |
| Sales at 8% and the VAT on them | Net revenue and output VAT for items under Decree 174/2025/ND-CP, also listed on Form 01 of Decree 174 Annex III |
| Input VAT on purchases | VAT on valid VAT invoices, import VAT receipts and receipts for VAT paid on behalf of foreign suppliers |
| Input VAT credited | Input VAT that meets the Art. 14 conditions, after apportionment |
| Input VAT carried forward | Credit left from the previous period |
| VAT payable, or credit to carry forward | Output VAT less credited input VAT less brought-forward credit |

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | The 10% standard rate until the item is confirmed as 0%, 5%, not subject, or within the temporary 8% |
| Unknown whether the 5% rate applies | Standard rate until the item is matched to the Art. 9(2) list |
| Unknown whether the temporary 8% applies (until 31 December 2026) | 10% on sales, and input VAT only as printed on the supplier's VAT invoice |
| Unknown counterparty country | Domestic Vietnam |
| Unknown export qualification | Domestic rate until the 0% conditions are evidenced |
| Unknown business use | No input credit |
| No VAT invoice, or no non-cash payment document where one is needed | No input credit |
| Unknown whether a foreign service supplier was paid through VAT withheld by the buyer | Flag; no input credit until the receipt for VAT paid on behalf exists |

### Red flag thresholds

**Red flag thresholds**

| Flag | Rule |
| --- | --- |
| HIGH | Any purchase at or above the non-cash payment level in Section 5.12 that was paid in cash: its input VAT is not creditable |
| HIGH | Any payment to a foreign service supplier without a Vietnamese VAT invoice or a receipt for VAT paid on behalf |
| MEDIUM | One counterparty accounts for most of the output or input of the period |
| MEDIUM | More than four conservative defaults used in one period |
| LOW | A brought-forward credit that has grown for several periods with exports or investment (check refund eligibility, Section 5.11) |

## Section 2: Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs.** Bank statement for the period in CSV, PDF, or pasted text. Confirmation of the VAT calculation method (credit method, phương pháp khấu trừ, or direct method, phương pháp tính trực tiếp) and the tax code (mã số thuế, MST).
- **Recommended inputs.** VAT invoices (hóa đơn giá trị gia tăng) for all purchases, e-invoices for sales, the prior period return and the credit carried forward.
- **Ideal inputs.** Complete ledger, export customs declarations (tờ khai hải quan), export contracts, asset register, full invoice register, and receipts for VAT paid on behalf of foreign suppliers.
- **Refusal if minimum missing.** SOFT WARN. No bank statement is a hard stop. "Input VAT in Vietnam is creditable only with a VAT invoice (or import VAT or VAT-paid-on-behalf receipt) and, where required, a non-cash payment document. All credits are provisional until the invoices are checked."

### Refusal catalogue

- **R-VN-1: Direct method taxpayers (phương pháp tính trực tiếp).** "A direct-method business pays VAT as a percentage of revenue (or, for gold, silver and gemstones, on value added). It has no input credit. Confirm the method before proceeding. This Guide mainly covers the credit method."
- **R-VN-2: Businesses below the credit-method revenue level, and household or individual businesses.** "An enterprise or cooperative below the revenue level in Section 1 uses the direct method unless it registered for the credit method. A household or individual business uses the direct method above its own threshold and is not subject to VAT at or below it. Confirm the method and status before proceeding."
- **R-VN-3: Apportionment (mixed taxable and not-subject supplies).** "If the business makes both taxable and not-subject supplies and cannot account for input VAT separately, the creditable share is the ratio of taxable revenue to total revenue in the tax period (Decree 181/2025/ND-CP Art. 23(2), revenue base as amended by Decree 144/2026/ND-CP from 20 June 2026). Out of scope without the period's revenue split: escalate."
- **R-VN-4: Real estate and construction.** "Real estate business has its own taxable-value rules (Decree 181/2025/ND-CP Art. 8) and is excluded from the temporary 8%. Out of scope: escalate to a licensed tax agent."
- **R-VN-5: Foreign contractor regime.** "A Vietnamese business that buys services from a foreign organisation without a permanent establishment, or from a non-resident individual, is the VAT payer for those services and pays on the foreign party's behalf (VAT Law Art. 4(3) and (4)). The corporate income tax side of the foreign contractor regime is outside this Guide. Out of scope beyond the VAT credit question in Section 5.10."

## Section 3: Supplier pattern library

Match by case-insensitive substring on counterparty name or reference. Most specific match wins. Fall through to Section 5 if no match. A supplier name never decides the rate: the rate printed on the supplier's VAT invoice does, checked against the rules in Section 5. Until 31 December 2026 many 10% items are invoiced at the temporary 8% (Section 1); telecoms, finance, banking, securities, insurance, real estate business, metal products, mining products (except coal), and goods and services subject to special consumption tax (except petrol) stay at 10%.

### 3.1 Vietnamese banks: interest, fees and charges

The not-subject list for banking (VAT Law Art. 5(9)) covers credit services, lending by non-credit institutions, securities business, capital transfers, debt sales, foreign currency trading, derivatives and the listed sale of collateral. Bank service fees that are not part of a credit service (for example account and transfer fees) are not on that list, so they are taxable. Fees that form part of a credit service follow the credit service; ask before treating credit-card fees as taxable. Banking is excluded from the temporary 8%, so taxable bank fees stay at 10%. Source: [VAT Law Art. 5(9)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf) ("a) Dịch vụ cấp tín dụng", "e) Kinh doanh ngoại tệ").

**Vietnamese banks**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VIETCOMBANK, NGÂN HÀNG NGOẠI THƯƠNG, VCB | Fee lines: input at the invoiced rate; interest: EXCLUDE | Take credit only with the bank's VAT invoice |
| BIDV, NGÂN HÀNG ĐẦU TƯ VÀ PHÁT TRIỂN | Same | Same |
| VIETINBANK, NGÂN HÀNG CÔNG THƯƠNG, CTG | Same | Same |
| AGRIBANK, NGÂN HÀNG NÔNG NGHIỆP | Same | Same |
| TECHCOMBANK, TCB | Same | Same |
| VPBANK, NGÂN HÀNG VIỆT NAM THỊNH VƯỢNG | Same | Same |
| MB BANK, NGÂN HÀNG QUÂN ĐỘI | Same | Same |
| ACB, NGÂN HÀNG Á CHÂU | Same | Same |
| SACOMBANK | Same | Same |
| TPBANK | Same | Same |
| LÃI SUẤT, LÃI TIỀN VAY, INTEREST | EXCLUDE | Interest on credit is a credit service, not subject to VAT (Art. 5(9)(a)) |
| PHÍ DỊCH VỤ, PHÍ CHUYỂN TIỀN, FEE | Input at the invoiced rate | Not on the Art. 5(9) list; banking stays at 10% |
| MUA BÁN NGOẠI TỆ, FX | EXCLUDE | Foreign currency trading is not subject (Art. 5(9)(e)) |

### 3.2 Vietnamese government and statutory (exclude)

**Government/statutory**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CỤC THUẾ, CHI CỤC THUẾ, THUẾ TỈNH, TAX AUTHORITY | EXCLUDE | Tax payment |
| THUẾ GTGT, THUẾ TNDN, THUẾ TNCN | EXCLUDE | Tax remittance |
| BẢO HIỂM XÃ HỘI, BHXH, SOCIAL INSURANCE | EXCLUDE | Social insurance |
| BẢO HIỂM Y TẾ, BHYT | EXCLUDE | Health insurance |
| HẢI QUAN, CUSTOMS | Import VAT: input, with the import VAT receipt; duty: EXCLUDE | Import VAT paid at customs is creditable with the receipt (Art. 14(2)(a)) |
| BHTN, BẢO HIỂM THẤT NGHIỆP | EXCLUDE | Unemployment insurance |

### 3.3 Vietnamese utilities

**Utilities**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EVN, TẬP ĐOÀN ĐIỆN LỰC, ĐIỆN LỰC, CÔNG TY ĐIỆN LỰC | Input at the invoiced rate | Electricity is in the 10% group and is not one of the excluded groups in Decree 174/2025/ND-CP Art. 1(1); expect 8% on invoices until 31 December 2026 |
| SAWACO, HAWACO, CẤP NƯỚC (water company) | Input 5% | Clean water for production and daily life is on the 5% list; bottled water and soft drinks are not (Art. 9(2)(a)). No temporary cut on 5% items |
| VIETTEL TELECOM, VNPT, VIỄN THÔNG VIỆT NAM, MOBIFONE, VIETNAMOBILE, GMOBILE | Input 10% | Telecoms are excluded from the temporary 8% |

### 3.4 Transport and logistics

**Transport and logistics**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VIETNAM AIRLINES, VNA, HÀNG KHÔNG VIỆT NAM, VIETJET AIR, VIETJET, BAMBOO AIRWAYS, VIETRAVEL AIRLINES | Check route | International transport is 0% (Art. 9(1)(c)); domestic flights are in the 10% group, so expect 8% until 31 December 2026 |
| ĐƯỜNG SẮT VIỆT NAM, VNR, RAILWAY | Input at the invoiced rate | Rail is not on the not-subject list for public transport (which names bus, tram and inland waterway, Art. 5(16)) |
| XE BUÝT, BUS, METRO, TÀU ĐIỆN | EXCLUDE (no VAT) | Public passenger transport by bus, tram and inland waterway is not subject (Art. 5(16)) |
| GRAB VIETNAM, BE, XANH SM | Input at the invoiced rate | Ride-hailing is taxable; 10% group |
| GIAO HÀNG TIẾT KIỆM, GHTK, GIAO HÀNG NHANH, GHN, VIETTEL POST, J&T EXPRESS, NINJA VAN | Input at the invoiced rate | Courier services are taxable; 10% group, not an excluded group under Decree 174 Art. 1(1) |
| VIETNAM POST, BƯU ĐIỆN | Input at the invoiced rate | Postal services are not on the Art. 5 not-subject list; exported postal services do not get 0% (Art. 9(1)(d)) |

### 3.5 Food and retail

**Food and retail**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| WINMART, WINCOMMERCE, GO!, AEON VIỆT NAM, CO.OPMART, SAIGON CO.OP, LOTTE MART | Input at the invoiced rate per line | A supermarket invoice can carry several rates: unprocessed farm produce sold at the commercial stage is 5% (Art. 9(2)(d)); processed food and most other goods are in the 10% group (8% until 31 December 2026) |
| NHÀ HÀNG (restaurant), BÁN LẺ (retail) | Input at the invoiced rate | 10% group; check business purpose |
| PHÂN BÓN, THUỐC TRỪ SÂU, THUỐC BẢO VỆ THỰC VẬT (fertiliser, pesticides) | Input 5% | Fertiliser and plant protection chemicals are on the 5% list (Art. 9(2)(b)) |
| THỨC ĂN CHĂN NUÔI (animal feed) | No VAT | Animal feed is not subject to VAT (Art. 5(3)) |

### 3.6 Software and cloud: local Vietnamese suppliers

**Software and cloud, local**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MISA, PHẦN MỀM MISA, FAST ACCOUNTING | No VAT if invoiced as software (check invoice) | Software products and software services are not subject to VAT (VAT Law Art. 5(21)) |
| VIETTEL CLOUD, VNPT CLOUD | Input at the invoiced rate | Check whether the invoice treats the service as software (not subject) or as a taxable service |
| VTC PAY | Input at the invoiced rate | Payment services are not on the Art. 5(9) list |

### 3.7 International suppliers of services and digital services

A Vietnamese business that buys services from a foreign organisation without a permanent establishment in Vietnam, or from a non-resident individual, is the VAT payer for those services (VAT Law Art. 4(3)). Where a credit-method business buys services from a foreign supplier through e-commerce or a digital platform, the Vietnamese business withholds and pays the foreign supplier's VAT (Art. 4(4)). The receipt for VAT paid on the foreign party's behalf is a valid basis for input credit (Art. 14(2)(a): "chứng từ nộp thuế giá trị gia tăng thay cho phía nước ngoài"). The rate for these digital services is in the VAT Law table (Section 1). Whether the temporary 8% reaches them is not settled in this Guide (Section 5.10). Source: [VAT Law](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf).

**International service suppliers**

| Pattern | Notes |
| --- | --- |
| GOOGLE (Workspace, Ads, Cloud) | Foreign supplier: check whether the business withheld and paid VAT on its behalf, and hold the receipt before taking credit |
| MICROSOFT (365, Azure) | Same; check whether a Vietnamese entity issued a Vietnamese VAT invoice instead |
| META, FACEBOOK ADS | Same |
| ZOOM, SLACK, NOTION, OPENAI | Same |
| AWS | Same |

### 3.8 Payment processors and e-wallets

Payment and e-wallet fees are not among the financial services on the not-subject list (Art. 5(9)), so they are taxable. Whether a given payment service falls inside "finance and banking" for the temporary 8% depends on Decree 174/2025/ND-CP Annex I. Take the rate printed on the VAT invoice. Decree 174 Annex I lists financial-support product group 6619, which includes transaction processing ("cấp phép cho các giao dịch, chuyển tiền đến/từ các tài khoản của người giao"); a fee in that group stays at 10%. Source: [VAT Law Art. 5(9)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf).

**Payment processors**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VNPAY (phí giao dịch) | Input at the invoiced rate | Taxable fee |
| MOMO (phí) | Input at the invoiced rate | Taxable fee |
| ZALOPAY (phí) | Input at the invoiced rate | Taxable fee |
| PAYOO (phí) | Input at the invoiced rate | Taxable fee |

### 3.9 Internal transfers and exclusions

**Internal transfers**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CHUYỂN KHOẢN NỘI BỘ, INTERNAL | EXCLUDE | Internal movement |
| VAY VỐN, TRẢ NỢ, LOAN | EXCLUDE | Loan principal |
| LƯƠNG, TIỀN LƯƠNG, SALARY | EXCLUDE | Wages are outside VAT |
| CỔ TỨC, DIVIDEND | EXCLUDE | Outside VAT |
| ĐẶT CỌC, DEPOSIT | EXCLUDE | Deposit: outside VAT until applied |
| RÚT TIỀN, ATM | Tier 2: ask | Default exclude. A cash withdrawal used to pay a supplier also breaks the non-cash payment condition (Section 5.12) |

## Section 4: Worked examples

Six classifications from a hypothetical Ho Chi Minh City IT consultancy company that uses the credit method. Format: Vietcombank transaction history. All amounts are hypothetical and in dong; the bank lines omit the currency column. Each example states the rate shown on the hypothetical invoice; on real data, take the rate from the invoice and check it against Section 5.

### Example 1: Domestic B2B revenue at the temporary 8%

**Input line:**
`15/09/2026  Nhận chuyển khoản  CÔNG TY TNHH ABC TECHNOLOGY  ND: THANH TOAN HD GTGT SO 0000123  +108,000,000`

**Reasoning:**
Incoming payment from a Vietnamese company for IT consulting. First confirm it is not a software service: software products and software services are not subject to VAT, so neither 8% nor 10% applies ([VAT Law Art. 5(21)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf): "sản phẩm phần mềm và dịch vụ phần mềm theo quy định của pháp luật"). Consulting is in the 10% group and is not one of the excluded groups in Decree 174/2025/ND-CP Art. 1(1), so the e-invoice the consultancy issued in September 2026 shows 8% (confirm against Annex I). Gross 108,000,000 = net 100,000,000 + output VAT of 8,000,000. Report on the 8% sales line and on Form 01 of Decree 174 Annex III. For a supply invoiced on or after 1 January 2027 the 10% rate applies unless the cut is extended.

**Classification:** Output VAT at 8%: 8,000,000. Net sales: 100,000,000.

### Example 2: Export of services (0%)

**Input line:**
`22/09/2026  Nhận ngoại tệ  ACME CORPORATION USA  Technical consulting Q3/2026  +125,000,000 (from 5,000.00 US dollars)`

**Reasoning:**
Payment from a US company for consulting supplied to it and used outside Vietnam. 0% applies to services "cung cấp trực tiếp cho tổ chức, cá nhân ở nước ngoài và được tiêu dùng ở ngoài Việt Nam" (VAT Law Art. 9(1)(b)), with a service contract with the foreign party and a non-cash payment document (Decree 181/2025/ND-CP Art. 18(2)). Payment in foreign currency is not itself a condition; a non-cash payment is. Evidence: signed contract and this bank credit. Report 125,000,000 on the 0% sales line. Output VAT: none. Conservative default: domestic rate if the contract or the place of consumption cannot be shown.

**Classification:** 0% export sales: 125,000,000. Output VAT: none.

### Example 3: Water utility (5%)

**Input line:**
`10/09/2026  Thanh toán tự động  SAWACO - CẤP NƯỚC SAIGON  Tiền nước tháng 8/2026  -2,100,000`

**Reasoning:**
Clean water for business use is on the 5% list. The temporary 8% does not touch 5% items. Gross 2,100,000 = net 2,000,000 + input VAT of 100,000. The purchase is below the non-cash payment level in Section 5.12, and it was paid by bank debit anyway. Credit needs SAWACO's VAT e-invoice.

**Classification:** Input VAT at 5%: 100,000. Net expense: 2,000,000.

### Example 4: Domestic courier (8%)

**Input line:**
`08/09/2026  Thanh toán  GIAO HÀNG NHANH GHN  Phí vận chuyển tháng 8/2026  -10,800,000`

**Reasoning:**
Courier services are in the 10% group and not an excluded group, so the hypothetical invoice shows 8%. Gross 10,800,000 = net 10,000,000 + input VAT of 800,000. The purchase is above the non-cash payment level in Section 5.12, so the bank transfer is the required non-cash payment document. Credit needs GHN's VAT e-invoice.

**Classification:** Input VAT at 8%: 800,000. Net expense: 10,000,000.

### Example 5: Bank deposit interest

**Input line:**
`01/09/2026  Lãi tiền gửi  Vietcombank  Lãi tháng 8/2026  +250,000`

**Reasoning:**
Deposit interest paid by the bank to the business. It is not a sale of goods or services by the consultancy. EXCLUDE from the VAT return. If the business itself makes not-subject supplies (for example lending as a non-credit institution, Art. 5(9)(b)), apportionment may apply (R-VN-3).

**Classification:** EXCLUDE.

### Example 6: Foreign software service (foreign supplier)

**Input line:**
`05/09/2026  Thanh toán quốc tế  GOOGLE ASIA PACIFIC PTE LTD  Google Workspace September 2026  -3,300,000`

**Reasoning:**
Payment to a foreign supplier for a digital service. The consultancy uses the credit method, so for services bought from a foreign supplier without a permanent establishment through e-commerce or a digital platform it withholds and pays the supplier's VAT (VAT Law Art. 4(4)). The receipt for VAT paid on behalf supports input credit (Art. 14(2)(a)). If no VAT was withheld and paid, there is no receipt and no credit, and the business may owe the VAT it should have withheld. Flag for review: confirm what was withheld, at what rate, and whether the service is software (Art. 5(21)).

**Classification:** Tier 2: FLAG. No input credit until the VAT-paid-on-behalf receipt exists.

## Section 5: Tier 1 rules

### 5.1 Standard rate and the temporary 8%

- **Standard rate.** The standard rate in the VAT Law table (Section 1) applies to every taxable good or service not on the 0% or 5% lists, including services sold by foreign suppliers without a permanent establishment through e-commerce and digital platforms (VAT Law 48/2024/QH15 Art. 9(3), from 1 July 2025).
- **Temporary 8%.** From 1 July 2025 to 31 December 2026, credit-method businesses charge 8% instead of 10% on goods and services in the 10% group, except telecoms, finance, banking, securities, insurance, real estate business, metal products, mining products (except coal), and goods and services subject to special consumption tax (except petrol) (Resolution 204/2025/QH15; Decree 174/2025/ND-CP Art. 1, tables in Section 1). The cut applies at every stage: import, production, processing and trade. It never applies to items that are not subject to VAT or that are at 5%. If a business sells items at different rates, each item's rate must be shown on the VAT invoice. A business that cannot separate its sales by rate pays at the highest rate of the goods and services it sells (VAT Law Art. 9(4): "phải tính và nộp thuế theo mức thuế suất cao nhất").

### 5.2 Reduced rate 5%

- **Reduced rate.** Only the items listed in VAT Law Art. 9(2) take 5% (rate in the Section 1 table): (a) clean water for production and daily life, not bottled water or soft drinks; (b) fertiliser, ores for making fertiliser, plant protection chemicals and livestock growth stimulants; (c) dredging of canals and ponds for farming, crop care and pest control, and preliminary processing and storage of farm products; (d) crop, planted-forest (except timber and bamboo shoots), livestock and aquaculture products that are unprocessed or only ordinarily pre-processed, except where Art. 5(1) makes them not subject; (đ) listed rubber latex forms, fishing nets and twine; (e) handicrafts from jute, sedge, bamboo, leaves, straw, coconut and similar farm materials, carded cotton fibre, newsprint; (g) fishing vessels and specialised farm machinery; (h) medical equipment, medicines and pharmaceutical ingredients; (i) teaching aids; (k) traditional performing arts; (l) children's toys and books, other than the books that are not subject under Art. 5(15); (m) science and technology services; (n) sale and lease of social housing. Source: [VAT Law Art. 9(2)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf).
- **Not on the 5% list.** Animal feed is not subject to VAT at all (Art. 5(3)). Sugar is not on the list. Medical services are not subject (Art. 5(10)); medical equipment and medicines are 5%.

### 5.3 Zero rate: exports

- **Scope.** 0% applies to exported goods (goods sold to organisations and individuals abroad and consumed outside Vietnam, goods sold into non-tariff zones for export production, duty-free and departure-area sales, on-the-spot exports), exported services (services supplied directly to organisations and individuals abroad and consumed outside Vietnam, or to organisations in non-tariff zones for export production), international transport and the other items in Art. 9(1)(c) (VAT Law Art. 9(1), as amended by Law 90/2025/QH15 from 1 July 2025).
- **Not 0% even when supplied abroad.** Technology transfer and IP transfers abroad, reinsurance abroad, credit services, capital transfers, derivatives, postal and telecom services, the exported resources in Art. 5(23), imported tobacco, alcohol and beer re-exported, domestic fuel sold into non-tariff zones, and the other cases in Art. 9(1)(d) ("Các trường hợp không áp dụng thuế suất 0% bao gồm"). Decree 181 Art. 17(4)(k) also excludes services supplied in Vietnam to foreign parties: sports, performing arts, culture, entertainment, conferences, hotels, training, advertising and tourism; services tied to selling or distributing goods in Vietnam; and non-cash payment services ("Các dịch vụ cung cấp tại Việt Nam cho tổ chức, cá nhân ở nước ngoài như sau: thi đấu thể thao, biểu diễn nghệ thuật, văn hóa, giải trí, hội nghị, khách sạn, đào tạo, quảng cáo, du lịch lữ hành"). Art. 17(4)(l) excludes listed services to organisations in non-tariff zones (premises rental, worker transport, catering).
- **Conditions (Decree 181/2025/ND-CP Art. 18).** Exported goods need all three: a sale, processing or export-entrustment contract; a non-cash payment document; and a customs declaration. Exported services (other than international transport, aviation and maritime services, which have their own lists) need both: a service contract with an organisation or individual abroad or in a non-tariff zone, and a non-cash payment document. Payment in foreign currency is not a listed condition. Table in Section 5.12. Where the customer is an individual abroad, the individual must be outside Vietnam while the service is supplied ([Decree 181/2025/ND-CP](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/7/45379/57344-1-2025899-900181-2025-nd-cp.pdf) Art. 17(2)(a): "cá nhân ở nước ngoài đáp ứng điều kiện ở ngoài Việt Nam trong thời gian diễn ra việc cung cấp dịch vụ").
- **Input credit on exports** additionally needs the documents in VAT Law Art. 14(2)(c): the contract with the foreign party, the sales invoice, the non-cash payment document, the customs declaration for goods, and the packing list, bill of lading and insurance documents if any.

### 5.4 Not subject to VAT (đối tượng không chịu thuế)

- **What it means.** A business supplying only not-subject goods or services charges no VAT and cannot credit or be refunded input VAT on them, except where the 0% rate applies (VAT Law Art. 5(27): "không được khấu trừ, không được hoàn thuế giá trị gia tăng đầu vào, trừ trường hợp được áp dụng mức thuế suất 0%"). This is different from 0%.
- **Main items (VAT Law Art. 5).** Unprocessed farm, forestry and fishery products sold by the producer and at import (1); breeding stock and seed (2); animal and aquaculture feed (3); salt (4); State-owned housing sold to tenants (5); irrigation, ploughing and harvesting services (6); transfer of land use rights (7); life, health, student and other person-related insurance and listed agricultural insurance and reinsurance (8); the financial services in (9); medical and veterinary services (10); funeral services (11); listed works funded at least half by public contributions or humanitarian aid (12); teaching and vocational training (13); State-funded broadcasting (14); newspapers, magazines and the listed categories of books (15); public passenger transport by bus, tram and inland waterway (16); technology transfer, IP transfers, and software products and software services (21); unworked gold bars at import (22); artificial body parts and mobility aids (24); goods and services of household and individual businesses at or below the Government's revenue level (25, Section 1); and the other items in Art. 5. Source: [VAT Law Art. 5](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf).
- **Business-to-business farm produce.** An enterprise or cooperative that buys unprocessed farm, forestry or fishery products and sells them to another enterprise or cooperative does not declare or pay VAT on that sale but may still credit its input VAT (Art. 5(1), as amended by Law 149/2025/QH15 from 1 January 2026: "thì không phải kê khai, tính nộp thuế giá trị gia tăng nhưng được khấu trừ thuế giá trị gia tăng đầu vào").
- **Insurance.** The insurance not subject to VAT is listed in VAT Law Art. 5(8) (life, health, student and other person-related insurance, agricultural insurance, fishing-vessel insurance, reinsurance, listed oil and gas insurance). Decree 144/2026/ND-CP repeated the list in Decree 181 Art. 4 from 20 June 2026. Other non-life insurance is taxable and excluded from the temporary 8%.
- **Postal services and bank fees** are not on the list and are taxable (Section 3).

### 5.5 Credit method (phương pháp khấu trừ)

- **Who must use it.** A business that keeps full accounts, invoices and records and whose annual revenue from goods and services is at or above the level in the VAT Law table (Section 1), except household and individual businesses (VAT Law Art. 11(2); Decree 181/2025/ND-CP Art. 21(1)).
- **How revenue is measured.** The business totals the taxable revenue line on its monthly VAT returns from November of the previous year to October of the current year (or its quarterly returns from the fourth quarter of the previous year to the third quarter of the current year), before the year the method applies. The method then stays fixed for 2 consecutive years (Decree 181 Art. 21(1)(a), table in Section 5.12).
- **New businesses.** A business started during the year annualises its revenue. At or above the level, it uses the credit method; below it, it uses the direct method on revenue for 2 years unless it registers voluntarily for the credit method (Decree 181 Art. 21(1)(b)).
- **Voluntary credit method.** Allowed for operating enterprises and cooperatives below the level that keep full accounts and invoices, and for listed new businesses, including a newly established enterprise that invests in or buys fixed assets, machinery or equipment, or has a lease for its business premises (Decree 181 Art. 21(2)). Not for household or individual businesses.
- **Computation.** VAT payable = output VAT less creditable input VAT (VAT Law Art. 11(1)(a)). Input VAT arising in a month or quarter is declared and credited in that period; any excess carries forward to the next period (Art. 14(1)(đ)). If input VAT was missed or declared wrongly, and the correction reduces tax payable or only changes the credit carried forward, declare it in the month or quarter the error is found, before a tax inspection or audit decision is announced. If the correction increases tax payable, declare it in the original period and pay late-payment interest (VAT Law Art. 14(1)(đ): "Người nộp thuế thực hiện khai vào tháng, quý phát hiện sai, sót nếu việc khai thuế vào tháng, quý phát sinh số thuế giá trị gia tăng đầu vào bị sai, sót làm giảm số tiền thuế phải nộp").

### 5.6 Direct method (phương pháp tính trực tiếp)

- **On revenue.** Applies to enterprises and cooperatives below the credit-method level that have not opted in, to household and individual businesses above their threshold, to foreign organisations and individuals without full accounting (other than the foreign e-commerce suppliers in Art. 4(4)), and to other organisations (VAT Law Art. 12). VAT = percentage x revenue, using the percentages in the VAT Law table (Section 1): distribution and supply of goods, services, manufacturing and transport, and other activities. Until 31 December 2026, the percentage on qualifying goods and services is reduced as shown in the Decree 174 table (Section 1); the invoice must state the amount of the reduction. No input credit.
- **On value added.** Applies only to buying, selling and working gold, silver and precious stones: VAT = value added x VAT rate ("trên giá trị gia tăng bằng giá trị gia tăng nhân với thuế suất"). Source: [VAT Law Art. 12](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf).
- **Return form.** The live version named Form 04/GTGT for the direct method. No allowed page confirms the form number for 2026 (Section 10, known gaps).

### 5.7 Invoices and e-invoices

- **Which invoice.** Credit-method businesses issue VAT invoices (hóa đơn giá trị gia tăng); direct-method businesses issue sales invoices (hóa đơn bán hàng). If a VAT invoice for a taxable sale does not show the VAT, output VAT is the payment amount on the invoice times the rate. Pre-printed stamps, tickets and cards include VAT in the printed price (VAT Law Art. 16).
- **E-invoices, companies.** Company e-invoice rules (content, timing, the tax-authority code, cash-register invoices) are in the Government's invoice decree and the Ministry of Finance circular under it. In March 2026, Decree 68/2026/ND-CP cited Decree 123/2020/ND-CP as amended by Decree 70/2025/ND-CP as the invoice decree ("Nghị định số 70/2025/NĐ-CP ngày 20 tháng 3 năm 2025 của Chính phủ sửa đổi, bổ sung một số điều của Nghị định số 123/2020/NĐ-CP"). This Guide could not read a later 2026 invoice decree or circular on an allowed page. Before relying on any field list or timing rule, check the current invoice decree and circular on vanban.chinhphu.vn and congbao.chinhphu.vn.
- **E-invoices, household and individual businesses.** See the Decree 141 table (Section 1).

### 5.8 Filing and payment deadlines

From 1 July 2026 the deadlines come from Decree 252/2026/ND-CP, which replaced Decree 126/2020/ND-CP, and the Law on Tax Administration 108/2025/QH15, which replaced Law 38/2019/QH14.

**Filing deadlines (Decree 252/2026/ND-CP)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all rules below | https://congbaocdn.chinhphu.vn/180507251028987904/2026/7/16/469958-1784169386_v1_1784170386_signed.pdf |
| Monthly return | No later than the 20th day of the month after the month in which the tax obligation arises | "thời hạn nộp hồ sơ khai thuế chậm nhất là ngày thứ 20 của tháng tiếp theo tháng phát sinh nghĩa vụ thuế" |
| Quarterly return | No later than the last day of the first month of the next quarter | "Đối với loại thuế khai theo quý, thời hạn nộp hồ sơ khai thuế chậm nhất là ngày cuối cùng của tháng đầu của quý tiếp theo" |
| Per-transaction return | No later than the 10th day counted from the day after the obligation arises | "thời hạn nộp hồ sơ khai thuế chậm nhất là ngày thứ 10 kể từ ngày tiếp theo ngày phát sinh nghĩa vụ thuế" |
| Decree 126/2020/ND-CP | Replaced from 1 July 2026 | "Nghị định này thay thế: a) Nghị định số 126/2020/NĐ-CP" |

**Payment, interest and amendments (Law 108/2025/QH15)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/108signed-17692413914281416017170.pdf |
| In force | 1 July 2026, except Art. 13 and the household and individual business e-invoice rules in Art. 26, which apply from 1 January 2026 (Art. 52) | "hiệu lực thi hành từ ngày 01 tháng 7 năm 2026, trừ quy định tại khoản 2 Điều này" |
| Payment deadline for self-assessed tax | The last day of the filing deadline for that return | "thời hạn nộp thuế, khoản thu khác chậm nhất là ngày cuối cùng của thời hạn nộp hồ sơ khai thuế" |
| Late-payment interest (tiền chậm nộp), a daily charge on the tax paid late | 0.03% per day | "Mức tính tiền chậm nộp bằng 0,03%/ngày tính trên số tiền thuế" |
| Supplementary return for an error, in the listed cases (including before a tax inspection or audit decision is announced) | Within 5 years from the filing deadline of the period with the error | "được khai bổ sung hồ sơ khai thuế, khoản thu khác trong thời hạn 05 năm" |
| Filing extension for force majeure, monthly, quarterly, annual and per-transaction returns (finalisation returns: not more than 60 days) | Not more than 30 days from the filing deadline | "thời gian gia hạn không quá 30 ngày kể từ ngày hết thời hạn nộp hồ sơ khai thuế" |
| Currency of declaration | Vietnamese dong | "Đồng tiền khai thuế, khoản thu khác là Đồng Việt Nam" |

- **Monthly or quarterly.** Decree 252/2026/ND-CP sets the deadline for each period but, as read for this Guide, does not state which VAT payers may file quarterly. The revenue test in the live version came from Decree 126/2020/ND-CP, which no longer applies from 1 July 2026. Check the Ministry of Finance circular guiding Decree 252 before choosing the period. Until confirmed, keep the period the business already uses and record the doubt.
- **No annual VAT return.** The live version listed an "annual settlement" for VAT. No allowed page shows an annual VAT finalisation; VAT input and output are declared by month or quarter (VAT Law Art. 14(1)(đ)). Annual finalisation belongs to income taxes, outside this Guide.

### 5.9 Penalties and interest

- **Late payment.** Interest as in the Law 108 table (Section 5.8), per day, on the tax paid late. It is a daily rate; do not annualise it.
- **Administrative penalties.** Decree 125/2020/ND-CP, as amended by Decree 102/2021/ND-CP and Decree 310/2025/ND-CP, continues in force from 1 July 2026 until replaced ([Decree 252/2026/ND-CP](https://congbaocdn.chinhphu.vn/180507251028987904/2026/7/16/469958-1784169386_v1_1784170386_signed.pdf): "tiếp tục có hiệu lực thi hành kể từ ngày 01 tháng 7 năm 2026 cho đến khi có văn bản thay thế"). The fine amounts are in that decree, which this Guide did not read. State no fine amount without reading it.
- **Invoice offences.** Buying, selling or advertising invoices, and creating sham transactions to claim credit or refund, are prohibited (VAT Law Art. 13). Input VAT on invoices created by prohibited acts is not creditable (Art. 14(3)).

### 5.10 Foreign suppliers, foreign contractors and digital platforms

- **Vietnamese buyer of foreign services.** A Vietnamese business that buys services (including services attached to goods) from a foreign organisation without a permanent establishment or from a non-resident individual is the VAT payer for those services (VAT Law Art. 4(3)). The receipt for VAT paid on the foreign party's behalf supports input credit (Art. 14(2)(a)).
- **Foreign digital suppliers, B2B.** Where a credit-method Vietnamese business buys services from a foreign supplier without a permanent establishment through e-commerce or digital platforms, the Vietnamese business withholds and pays the foreign supplier's VAT (Art. 4(4)). It also withholds the foreign supplier's corporate income tax (Decree 252/2026/ND-CP Art. 43(3)(b)), which is outside this Guide.
- **Foreign suppliers that register.** Foreign suppliers, including foreign e-commerce and digital platform operators, with revenue in Vietnam register for electronic tax transactions together with their first tax registration and receive a tax code. Those doing business regularly declare and pay monthly; those doing business irregularly declare and pay per transaction. A Vietnamese sale is identified from two non-contradictory pieces of information, one on payment and one on residence or access (Decree 252/2026/ND-CP, from 1 July 2026, source in Section 5.8).
- **Platforms withholding for household sellers.** Operators of e-commerce exchanges and digital platforms with a payment function withhold, declare and pay VAT for the household and individual businesses that sell on them (VAT Law Art. 4(5)). From 1 July 2026 the detailed rules are in Decree 252/2026/ND-CP, which replaced Decree 117/2025/ND-CP ("Chủ quản nền tảng thương mại điện tử có chức năng đặt hàng trực tuyến và chức năng thanh toán").
- **Not settled.** Whether the temporary 8% applies to services of foreign suppliers sold through digital platforms is not settled in this Guide. Decree 174/2025/ND-CP reduces "goods and services currently at 10%", and Art. 9(3) puts these services in the 10% group, but no allowed page read for this Guide applies the cut to them expressly. Ask an accountant before using 8% for them.

### 5.11 Refunds

- **Exports.** A business with exports in the month or quarter whose uncredited input VAT is at or above the level in the VAT Law table may claim a monthly or quarterly refund; not for goods imported and then re-exported. For a business with both exports and domestic sales, the export part left after offset against domestic VAT payable must reach that level. The refund may not exceed the cap in the same table; the excess carries forward (VAT Law Art. 15(1)).
- **Investment projects.** Uncredited input VAT of an investment project at or above the level in the table, after offset, is refundable, subject to the conditions and excluded projects in Art. 15(2).
- **Businesses that supply only 5% goods or services.** Refund if uncredited input VAT is at or above the level in the table after the waiting period in the table.
- **Departing foreigners.** Foreigners and overseas Vietnamese with a passport get a VAT refund on goods bought in Vietnam and taken out on departure.
- **Not settled.** The time limits for processing a refund were not read on an allowed page. Check Law 108/2025/QH15 and Decree 252/2026/ND-CP before promising a date.

### 5.12 Input credit conditions

- **Conditions in the law (VAT Law Art. 14(2)).** All of: (a) a VAT invoice, or the import VAT receipt, or the receipt for VAT paid on behalf of a foreign supplier; and (b) a non-cash payment document for the purchase, except special cases the Government sets; and, for exports, (c) the export documents in Section 5.3. Input VAT used for both taxable and not-subject supplies is creditable only for the taxable part; if it cannot be accounted for separately, use the ratio of taxable revenue to total revenue (Art. 14(1)(b); for the tax period under Decree 181 Art. 23(2)).
- **Cash deposits.** A record of the buyer paying cash into the seller's bank account is not a non-cash payment document ([Decree 181/2025/ND-CP](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/7/45379/57344-1-2025899-900181-2025-nd-cp.pdf) Art. 26(1): "trừ các chứng từ bên mua nộp tiền mặt vào tài khoản của bên bán").
- **Thresholds and caps in Decree 181/2025/ND-CP.**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/7/45379/57344-1-2025899-900181-2025-nd-cp.pdf |
| Purchases (including imports) at or above this value, VAT included, need a non-cash payment document for input credit | VND 5 million | "từ 05 triệu đồng trở lên đã bao gồm thuế giá trị gia tăng" |
| Purchases from one seller each below that value but bought several times on the same day with a total at or above it also need a non-cash payment document | VND 5 million | "Trường hợp mua hàng hóa, dịch vụ của một người nộp thuế có giá trị dưới 05 triệu đồng nhưng mua nhiều lần trong cùng một ngày" |
| Passenger cars of 9 seats or fewer as fixed assets (not cars used for goods or passenger transport, tourism or hotel business, or as demo cars): input VAT is creditable only on the part of the value, excluding VAT, up to | VND 1.6 billion | "có trị giá vượt trên 1,6 tỷ đồng (giá chưa có thuế giá trị gia tăng) thì số thuế giá trị gia tăng đầu vào được khấu trừ tương ứng với phần trị giá đến 1,6 tỷ đồng" |
| New business whose annualised revenue estimate is below the credit-method level: direct method on revenue for | 2 years | "chưa đến 01 tỷ đồng thì cơ sở kinh doanh áp dụng phương pháp tính trực tiếp theo doanh thu trong 02 năm" |
| Once determined, the calculation method stays fixed for | 2 consecutive years | "Thời gian áp dụng ổn định phương pháp tính thuế là 02 năm liên tục" |
| Exported goods: all three documents | Contract, non-cash payment, customs declaration | "b) Chứng từ thanh toán không dùng tiền mặt đối với hàng hóa xuất khẩu. c) Tờ khai hải quan theo quy định." |
| Exported services: both documents | Contract with a party abroad or in a non-tariff zone, and non-cash payment | "2. Đối với dịch vụ xuất khẩu, trừ quy định tại khoản 3, 4, 5 Điều này, phải có: a) Hợp đồng cung cấp dịch vụ" |

- **Deferred and instalment purchases.** From 20 June 2026, for purchases on deferred or instalment terms at or above the non-cash level, the buyer may credit the input VAT on the written contract and VAT invoice before payment is due. If no non-cash payment document exists when payment falls due under the contract, the buyer reduces the credited input VAT in that period; it may credit it again once the non-cash payment document exists ([Decree 144/2026/ND-CP](https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/18/469482-1778814209_v1_1779067294_signed.pdf) Art. 4: "Trường hợp chưa có chứng từ thanh toán không dùng tiền mặt do chưa đến thời điểm thanh toán theo hợp đồng").
- **Non-creditable VAT as a cost.** Input VAT that cannot be credited may be expensed for corporate income tax or added to the cost of a fixed asset, except VAT on purchases without the required non-cash payment document (VAT Law Art. 14(1)(e)).

## Section 6: Tier 2 catalogue

### 6.1 Foreign services and the foreign contractor regime

- **Foreign services.** **What it shows:** Payment to a foreign service provider. **What's missing:** Whether the supplier is registered in Vietnam and issued a Vietnamese invoice, or whether the business had to withhold and pay VAT on its behalf (VAT Law Art. 4(3) and (4)). **Conservative default:** Flag; no input credit until the receipt for VAT paid on behalf (or a Vietnamese VAT invoice) exists. **Question to ask:** "Did you withhold and pay VAT for this foreign supplier? Do you have the payment receipt? Or did the supplier issue a Vietnamese VAT invoice?"

### 6.2 Export qualification for services

- **Export of services.** **What it shows:** Revenue from a foreign client. **What's missing:** Whether the service was supplied directly to the party abroad and consumed outside Vietnam, whether there is a service contract with that party, and whether payment was non-cash (VAT Law Art. 9(1)(b); Decree 181/2025/ND-CP Art. 18(2)). Also whether the service is on the excluded list (Art. 9(1)(d); Decree 181 Art. 17(4)). **Conservative default:** Domestic rate. **Question to ask:** "Was this service used outside Vietnam by the foreign client? Is there a signed contract with them? Was it paid by bank transfer?"

### 6.3 Reduced rate confirmation (5% items)

- **5% items.** **What it shows:** A purchase that might be on the 5% list (water, fertiliser, farm produce, medical equipment, books, teaching aids). **What's missing:** The exact product. **Conservative default:** Standard rate on sales; input VAT only as printed on the invoice. **Question to ask:** "What exactly was bought or sold? Is it on the 5% list in VAT Law Art. 9(2)?"

### 6.4 Apportionment: businesses with mixed supplies

- **Mixed supplies.** **What it shows:** A business making both taxable and not-subject sales (for example IT consulting plus lending as a non-credit institution). **What's missing:** The split of taxable and total revenue for the tax period. **Conservative default:** No credit on shared overhead costs until the split is known. **Question to ask:** "What were your taxable sales and your not-subject sales in this period?"

### 6.5 Vehicle expenses

- **Vehicles.** **What it shows:** Vehicle purchase, lease, fuel or maintenance. **What's missing:** Whether the vehicle is used for the business, and for a passenger car of 9 seats or fewer bought as a fixed asset, its value excluding VAT (credit limited to the value up to the cap in Section 5.12, unless used for transport, tourism, hotel business or as a demo car). **Conservative default:** No input credit. **Question to ask:** "Is the vehicle in the company's name and used for the business? What did it cost before VAT, and what is it used for?"

### 6.6 The temporary 8% at the boundary

- **8% or 10%.** **What it shows:** A 10%-group sale or purchase in 2026. **What's missing:** Whether the item falls in an excluded group (Decree 174/2025/ND-CP Annexes I and II), and whether the invoice date is on or before 31 December 2026. **Conservative default:** Sales at 10% unless the item is confirmed outside the excluded groups; purchases at the rate printed on the invoice. **Question to ask:** "Which product or service code is this? On what date was the invoice issued?"

## Section 7: Excel working paper template

~~~
VIETNAM VAT WORKING PAPER (BẢNG TÍNH THUẾ GTGT)
Kỳ khai thuế (Period, month or quarter): ____________  MST: ____________

A. THUẾ ĐẦU RA (OUTPUT VAT)
  A1. Doanh thu chịu thuế 10% (net)           ___________
  A2. Thuế đầu ra 10% (A1 x 10%)              ___________
  A3. Doanh thu chịu thuế 8% (net, Decree 174, to 31 Dec 2026)  ___________
  A4. Thuế đầu ra 8% (A3 x 8%)                ___________
  A5. Doanh thu chịu thuế 5% (net)            ___________
  A6. Thuế đầu ra 5% (A5 x 5%)                ___________
  A7. Xuất khẩu 0% (net)                      ___________
  A8. Doanh thu không chịu thuế (net)         ___________
  A9. Tổng thuế đầu ra (A2 + A4 + A6)         ___________

B. THUẾ ĐẦU VÀO (INPUT VAT)
  B1. Thuế GTGT trên hóa đơn mua vào          ___________
  B2. Thuế GTGT hàng nhập khẩu đã nộp         ___________
  B3. Thuế GTGT nộp thay nhà cung cấp nước ngoài  ___________
  B4. Tổng thuế đầu vào (B1 + B2 + B3)        ___________
  B5. Không được khấu trừ (no invoice, no non-cash payment, car cap, private use)  ___________
  B6. Phân bổ cho doanh thu không chịu thuế (apportionment)  ___________
  B7. Thuế đầu vào được khấu trừ (B4 - B5 - B6)  ___________

C. THUẾ PHẢI NỘP
  C1. Chênh lệch thuế (A9 - B7)               ___________
  C2. Thuế còn được khấu trừ kỳ trước         ___________
  C3. Thuế GTGT phải nộp (C1 - C2, if positive)  ___________
  C4. Hoặc: Thuế còn được khấu trừ chuyển kỳ sau (if C1 - C2 is negative)  ___________

REVIEWER FLAGS:
  [ ] VAT e-invoice held for every input credit?
  [ ] Non-cash payment document for every purchase at or above the Decree 181 level?
  [ ] Export contract and non-cash payment for every 0% sale (customs declaration for goods)?
  [ ] VAT-paid-on-behalf receipts for foreign services?
  [ ] 8% only on items outside the Decree 174 excluded groups, invoices dated to 31 Dec 2026?
  [ ] Form 01 of Decree 174 Annex III filed with the return?
  [ ] 5% items matched to VAT Law Art. 9(2)?
  [ ] Apportionment calculated for the period if there are not-subject sales?
~~~

## Section 8: Bank statement reading guide

### Common Vietnamese bank statement formats

**Bank statement formats**

| Bank | Key columns | Date format | Amount |
| --- | --- | --- | --- |
| Vietcombank | Ngày GD, Nội dung, Phát sinh nợ (debit), Phát sinh có (credit), Số dư | DD/MM/YYYY | Dong, usually no decimals |
| BIDV | Ngày, Mô tả, Số tiền ghi nợ, Số tiền ghi có, Số dư | DD/MM/YYYY | Dong |
| Vietinbank | Ngày giao dịch, Nội dung, Số tiền, Số dư | DD/MM/YYYY | Dong |
| Techcombank | Thời gian, Mô tả giao dịch, Số tiền ghi nợ, Số tiền ghi có, Số dư | DD/MM/YYYY | Dong |
| MB Bank | Ngày, Nội dung giao dịch, Phát sinh, Số dư | DD/MM/YYYY | Dong |

Vietnamese documents write "." as the thousands separator and "," as the decimal mark ("1,6 tỷ đồng" is 1.6 billion dong). Check which convention an export uses before reading amounts.

### Key Vietnamese banking terms

**Banking terms**

| Vietnamese | Meaning | Classification hint |
| --- | --- | --- |
| Nhận chuyển khoản | Incoming transfer | Potential revenue |
| Thanh toán / Chuyển khoản | Outgoing payment | Potential expense; a transfer from the buyer's account is a non-cash payment document; a cash deposit into the seller's account is not |
| Nhận ngoại tệ | Foreign currency receipt | Potential export |
| Lãi tiền gửi | Deposit interest | Exclude |
| Phí dịch vụ | Service fee | Bank fee: taxable, credit only with the bank's VAT invoice |
| Số dư | Balance | Running balance: ignore |
| Nội dung | Transaction description | Key classification field |
| Thuế GTGT | VAT | Tax payment: exclude |
| Rút tiền ATM | ATM withdrawal | Tier 2: ask |
| Thanh toán tự động | Auto-payment | Subscription or utility |

## Section 9: Onboarding fallback

If the client provides a bank statement but cannot answer all questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Apply conservative defaults (Section 1)
3. Mark Tier 2 items as "PENDING: reviewer must confirm"
4. Generate the working paper with flags

~~~
VIETNAM GTGT ONBOARDING: CÂU HỎI TỐI THIỂU
1. Mã số thuế (MST, tax code)?
2. Phương pháp tính thuế: khấu trừ (credit) hay trực tiếp (direct)?
   If credit: compulsory (revenue at or above the level) or voluntary?
3. Kỳ khai thuế: theo tháng hay theo quý? (keep the period already used; the 2026 test is unconfirmed)
4. Doanh thu năm (November to October, or Q4 to Q3) for the method test?
5. Có doanh thu xuất khẩu (0%) không?
   Nếu có: hợp đồng với bên nước ngoài? thanh toán không dùng tiền mặt? tờ khai hải quan (goods)?
6. Có mua dịch vụ nước ngoài (Google, Microsoft, ...) không?
   Đã khấu trừ, nộp thay thuế GTGT chưa? Có chứng từ nộp thuế không?
7. Số thuế GTGT còn được khấu trừ kỳ trước (credit carried forward)?
8. Có doanh thu không chịu thuế không? (apportionment)
9. Hàng hóa, dịch vụ nào đang áp dụng 8% (Decree 174)?
~~~

## Section 10: Reference material

### Key legislation

**Key legislation**

| Topic | Reference |
| --- | --- |
| VAT Law | Law on Value Added Tax 48/2024/QH15, in force 1 July 2025, as amended by Resolution 204/2025/QH15, Law 90/2025/QH15, Law 149/2025/QH15 and Law 09/2026/QH16 (consolidated text 12/VBHN-VPQH of February 2026 does not include Law 09/2026) |
| Old VAT Law | Law 13/2008/QH12 and its amendments: no longer in effect from 1 July 2025 |
| Rates | VAT Law Art. 9; Decree 181/2025/ND-CP Arts. 17 to 19 |
| Temporary 8% | Resolution 204/2025/QH15; Decree 174/2025/ND-CP (1 July 2025 to 31 December 2026) |
| Not subject to VAT | VAT Law Art. 5; Decree 181/2025/ND-CP Art. 4 as amended by Decree 144/2026/ND-CP |
| Calculation methods | VAT Law Arts. 10 to 12; Decree 181/2025/ND-CP Arts. 20 to 22 |
| Input credit | VAT Law Art. 14; Decree 181/2025/ND-CP Arts. 23 to 28 (Arts. 23 and 26 amended by Decree 144/2026/ND-CP) |
| Refunds | VAT Law Art. 15; Decree 181/2025/ND-CP Arts. 29 to 37 |
| Household and individual businesses | VAT Law Art. 5(25) as amended by Law 09/2026/QH16; Decree 68/2026/ND-CP as amended by Decree 141/2026/ND-CP |
| Ministry of Finance guidance | Circular 69/2025/TT-BTC (replaced Circular 219/2013/TT-BTC) |
| Invoices | VAT Law Art. 16; invoice decree and circular: see Section 5.7 |
| Tax administration, filing, payment | Law 108/2025/QH15 and Decree 252/2026/ND-CP, from 1 July 2026 (replacing Law 38/2019/QH14, Decree 126/2020/ND-CP and Decree 117/2025/ND-CP) |
| Penalties | Decree 125/2020/ND-CP as amended by Decrees 102/2021/ND-CP and 310/2025/ND-CP |
| Foreign suppliers and platforms | VAT Law Art. 4(3) to (5); Decree 252/2026/ND-CP |

### Known gaps

- Which VAT payers may file quarterly under Decree 252/2026/ND-CP: the Ministry of Finance circular guiding it was not readable. Check it.
- Company e-invoice detail: the invoice decree and circular in force in 2026 were not read (Section 5.7).
- Whether the temporary 8% applies to services of foreign digital suppliers (Section 5.10).
- Refund processing time limits (Section 5.11).
- Return form numbers and box numbers for 2026 (Section 1).
- Administrative fine amounts (Section 5.9).
- Corporate income tax side of the foreign contractor regime: escalate.
- Real estate and construction VAT: escalate.
- Agricultural cooperative special rules: escalate.

### Self-check before filing

- [ ] All sales e-invoices issued and sent to the tax authority as required
- [ ] All input credits supported by VAT invoices (or import or VAT-paid-on-behalf receipts)
- [ ] Non-cash payment documents for purchases at or above the Decree 181 level
- [ ] 0% sales supported by contract and non-cash payment (and customs declaration for goods)
- [ ] VAT withheld and paid for foreign service suppliers where required
- [ ] 8% used only for qualifying items on invoices dated to 31 December 2026, with Form 01 of Decree 174 Annex III
- [ ] 5% and 10% correctly applied; not-subject items correctly excluded
- [ ] Prior period credit correctly carried forward

### Changelog

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2024 | Initial release |
| 2.0 | April 2026 | Full rewrite: pattern library, worked examples, foreign contractor note |
| 3.0 | October 2026 | Rewritten on VAT Law 48/2024/QH15, Decree 181/2025/ND-CP, Decree 174/2025/ND-CP, Law 108/2025/QH15 and Decree 252/2026/ND-CP; household threshold, input credit conditions, foreign supplier rules and deadlines brought up to date |

## The method, step by step

1. **Confirm the business is a VAT payer and which method it uses.** A company selling taxable goods or services is a VAT payer; only household and individual businesses at or below the Government's revenue level are outside VAT ([VAT Law Art. 4 and Art. 5(25)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf); [Decree 141/2026/ND-CP](https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/14/469455-1778231931_v1_1778720623_signed.pdf)). Then confirm credit or direct method from the revenue test and any voluntary registration ([Decree 181/2025/ND-CP Art. 21](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/7/45379/57344-1-2025899-900181-2025-nd-cp.pdf)).
2. **Classify each sale.** Not subject (Art. 5), 0% (Art. 9(1) with the Decree 181 Art. 18 documents), 5% (Art. 9(2)), or the 10% group ([VAT Law](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf)).
3. **Apply the temporary 8% where it fits.** For invoices dated 1 July 2025 to 31 December 2026, items in the 10% group outside the excluded groups take 8% (credit method) or the reduced percentage (direct method), shown on the invoice and listed on Form 01 of Annex III ([Decree 174/2025/ND-CP](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45374/57334-1-2025895-896174-2025-nd-cp.pdf)).
4. **Test each input credit.** VAT invoice (or import or VAT-paid-on-behalf receipt), non-cash payment where required, business use, car cap, apportionment for mixed supplies ([VAT Law Art. 14](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf); [Decree 181/2025/ND-CP Arts. 23 to 26](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/7/45379/57344-1-2025899-900181-2025-nd-cp.pdf); [Decree 144/2026/ND-CP](https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/18/469482-1778814209_v1_1779067294_signed.pdf)).
5. **Handle foreign suppliers.** For services bought from a foreign supplier without a permanent establishment, withhold and pay the VAT on its behalf where Art. 4(3) or (4) applies, and keep the receipt for the credit ([VAT Law Art. 4](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf); [Decree 252/2026/ND-CP](https://congbaocdn.chinhphu.vn/180507251028987904/2026/7/16/469958-1784169386_v1_1784170386_signed.pdf)).
6. **Compute the period's position.** Output VAT less credited input VAT less the credit brought forward; carry any excess forward, or test refund eligibility for exports, investment projects or 5%-only suppliers ([VAT Law Arts. 11, 14 and 15](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf)).
7. **File and pay on time.** Monthly by the 20th of the next month, quarterly by the last day of the first month of the next quarter; payment by the same day ([Decree 252/2026/ND-CP](https://congbaocdn.chinhphu.vn/180507251028987904/2026/7/16/469958-1784169386_v1_1784170386_signed.pdf); [Law 108/2025/QH15](https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/108signed-17692413914281416017170.pdf)). Correct errors with a supplementary return within the window in Section 5.8.

## Ask the client first

- Is the business a company or cooperative, or a household or individual business, and what was its revenue for the method test (November to October, or fourth quarter to third quarter)? This decides VAT status and method.
- Does it use the credit method, and if its revenue is below the level, did it register for it voluntarily?
- What does it sell, and is any of it on the 5% list, not subject to VAT, exported, or in a group excluded from the temporary 8%?
- Does it buy services from foreign suppliers (software, advertising, cloud), and did it withhold and pay VAT on their behalf?
- Were purchases at or above the Decree 181 non-cash level paid by bank transfer or another non-cash method?
- Does it file monthly or quarterly now, and has the tax authority told it of any change since 1 July 2026?

## When to refuse or refer

- Refer to a licensed tax agent (đại lý thuế) or accountant: real estate business, construction, oil and gas, gold and gemstones (direct method on value added), credit institutions, securities and insurance businesses.
- Refer: the corporate income tax side of foreign contractor payments, and any question on whether a foreign digital service takes 8%.
- Refer: refund claims (export, investment project, 5%-only, dissolution), because processing time limits and checks were not confirmed.
- Refer: penalties and fine amounts, and any notice from the tax authority.
- Refuse to state as current: the old VAT Law 13/2008/QH12, Decree 209/2013/ND-CP, Circular 219/2013/TT-BTC, Law 38/2019/QH14, Decree 126/2020/ND-CP or Decree 117/2025/ND-CP, and any household threshold other than the one in Section 1.
- Refuse to choose between monthly and quarterly filing on the old revenue test of Decree 126/2020/ND-CP.

## Prohibitions

- NEVER claim input VAT credit without a VAT invoice (or an import VAT or VAT-paid-on-behalf receipt)
- NEVER claim input VAT on a purchase at or above the Decree 181 level without a non-cash payment document
- NEVER zero-rate a service without the contract with the foreign party, non-cash payment and use outside Vietnam
- NEVER apply 8% to telecoms, finance, banking, securities, insurance, real estate business, metal products, mining products (except coal), or goods and services subject to special consumption tax (except petrol), or to any invoice dated after 31 December 2026 unless the cut is extended
- NEVER use the credit method for a direct-method taxpayer
- NEVER ignore VAT on services bought from foreign suppliers
- NEVER present calculations as definitive: direct to a licensed Vietnamese tax agent (đại lý thuế)

## Sources

- VAT Law 48/2024/QH15, consolidated text 12/VBHN-VPQH (February 2026): https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf
- Law 09/2026/QH16 (Official Gazette): https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/27/469536-1779329464_v1_1779843299_signed.pdf
- Decree 181/2025/ND-CP (Official Gazette): https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/7/45379/57344-1-2025899-900181-2025-nd-cp.pdf
- Decree 144/2026/ND-CP (Official Gazette): https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/18/469482-1778814209_v1_1779067294_signed.pdf
- Decree 174/2025/ND-CP (Official Gazette): https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45374/57334-1-2025895-896174-2025-nd-cp.pdf
- Decree 68/2026/ND-CP (Official Gazette): https://congbaocdn.chinhphu.vn/180507251028987904/2026/3/18/469047-1773796836_v1_1773803477_signed.pdf
- Decree 141/2026/ND-CP (Official Gazette): https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/14/469455-1778231931_v1_1778720623_signed.pdf
- Law on Tax Administration 108/2025/QH15 (Official Gazette): https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/24/108signed-17692413914281416017170.pdf
- Decree 252/2026/ND-CP (Official Gazette): https://congbaocdn.chinhphu.vn/180507251028987904/2026/7/16/469958-1784169386_v1_1784170386_signed.pdf
- Circular 69/2025/TT-BTC (Official Gazette): https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/7/45440/57458-1-2025923-92469-2025-tt-btc.pdf

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at openaccountants.com.

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
