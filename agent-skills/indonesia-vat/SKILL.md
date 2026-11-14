---
name: indonesia-vat
description: "Use this skill whenever asked to prepare, review, or classify transactions for an Indonesia VAT (PPN - Pajak Pertambahan Nilai) return (SPT Masa PPN), handle e-Faktur compliance, or advise on PPN registration and filing in Indonesia. Trigger on phrases like \"PPN Indonesia\", \"Pajak Pertambahan Nilai\", \"SPT Masa PPN\", \"e-Faktur\", \"Faktur Pajak\", \"PKP registration\", \"Pengusaha Kena Pajak\", or any Indonesia PPN request. ALWAYS read this skill before touching any Indonesia PPN work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/indonesia-vat"
  jurisdiction: "ID"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Indonesia VAT, PPN Return Preparation v2.2

## Scope

Prepare and review an Indonesian 2026 **SPT Masa PPN** working paper for a PKP from complete supply, purchase, invoice, import, foreign-service, payment and prior-return records. PPN is Pajak Pertambahan Nilai; output is Pajak Keluaran and input is Pajak Masukan. DJP administers it; the ordinary currency is IDR/rupiah. A VAT period is monthly, not a single annual tax return. Contributor: Open Accountants Community.

Read `vat-workflow-base` for the general reconciliation workflow and `id-einvoice-coretax` for current permitted channels, automatic invoice numbering, signatures, replacement/cancellation, payments and accepted receipts. This method computes a reviewable return package; it does not submit, pay, claim a refund, activate an account or invent a qualified accountant's sign-off.

Ordinary non-luxury supplies, separately regulated bases/specific amounts, luxury VAT, exports, exempt supplies, not-collected facilities and transactions outside VAT are different classes. Do not turn every bank row into eleven-percent income or input. PPnBM is a separate luxury-goods sales tax, and its list/rate calculation is outside this ordinary method. Retain the old scope flags for mixed activity/apportionment, exporter refunds, designated collectors, real estate/construction and special facilities; obtain their actual law and records or refer the affected computation.

## Ask the client first

Read the existing client record, registration, books, invoices and prior returns first. Ask only what is absent or unreconciled:

- Actual identity, tax residence/legal type, NPWP/NIK and NITKU/location as relevant; PKP confirmation and effective date, current period and original/amended status. NIK mapping follows resident-individual status, not a universal citizenship rule. Non-resident individuals/entities/government also use sixteen-digit NPWP. Do not fabricate a padded legacy ID. [DJP implementation release](https://www.pajak.go.id/index.php/id/siaran-pers/peluncuran-layanan-perpajakan-berbasis-nik-sebagai-npwp-npwp-16-digit-dan-nitku).
- Supply and purchase ledgers, invoice dates and approvals, consideration excluding/including VAT, discount/return/advance/progress-payment terms, actual supplier/customer, activity and place of utilisation, and taxable business purpose.
- Approved Faktur Pajak or a legally equivalent document, not simply a retail receipt or merchant brand; imports require customs declarations, supporting documents and actual state-receipt/collection data. Export goods require the actual customs/export packet; services require the specified service category, written agreement and payment/utilisation evidence.
- Prior accepted VAT returns, original/amended carried excess, refunds/decisions, actual own payments, designated-collector evidence, and which input has already been claimed, expensed or capitalised.
- Bank/card/marketplace settlements and cash records, accounts receivable/payable, advances, fixed assets, foreign subscriptions and current supplier status. Reconcile gross invoices to fees, income-tax deductions, VAT collections and net cash rather than equating them.

A bank statement alone is not a filing-ready VAT ledger, and absence of a bank statement need not block useful work where complete ledgers/invoices and payment evidence exist. Keep genuine missing information as pending. Unknown country, rate, business-use percentage, PKP status or export eligibility is not automatically domestic, non-PKP, nil credit or eleven percent. Show provisional alternatives where useful and hold the affected final total; do not silently overcharge output or permanently discard a potential lawful input credit.

## The method, step by step

## Rates, bands and thresholds

| Item | Applicable rule and limit | Official source |
|---|---|---|
| Nominal domestic VAT | Twelve percent under the current law; use the prescribed base or specific-amount mechanism | [VAT Law art.7](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 131 arts.2-4](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf) |
| Ordinary PMK 131 non-luxury mechanism | Twelve percent times eleven-twelfths of selling price/replacement/import value: effective eleven percent of that commercial amount | [PMK 131 art.3](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf) |
| Luxury goods within PPnBM list | Twelve percent of full prescribed price/import base; January2025 transitional eleven-twelfths treatment was confined to the specified supplies to FINAL consumers, not all luxury/imports | [PMK 131 arts.2,5](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf) |
| Other bases/specific amounts | Not universally subject to the ordinary PMK 131 multiplier; apply their own rule | [PMK 131 art.4](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf); [PMK 11](https://www.pajak.go.id/index.php/id/peraturan/ketentuan-nilai-lain-sebagai-dasar-pengenaan-pajak-dan-besaran-tertentu-pajak-pertambahan) |
| Qualifying export VAT | Zero percent for the statutory goods/intangible/service export classes, with actual evidence and service restrictions | [VAT Law art.7(2)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 81 arts.278-284](https://pajak.go.id/en/node/113110) |
| PKP turnover | IDR 4,800,000,000 applicable small-business boundary; mandatory crossing procedure and voluntary route separate from income-tax final eligibility | [PMK 164 arts.17-19](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau); [VAT Law art.3A](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Ordinary PKP deposit and return | End of following month, balance paid before submission; specific collector/import/holiday rules separate | [VAT Law art.15A](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 81 arts.94 and 100](https://pajak.go.id/en/node/113110) |
| Later-period input claim | At most three FOLLOWING tax periods after invoice period, with no prior expense/capitalisation and all other conditions; not an unconditional ninety-day expiry | [VAT Law art.9(9)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Invoice approval | Coretax format seventeen digits; upload AND approval no later than twentieth of following month; tax-point issuance is separate | [PER-11 arts.37,43-44](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0) |
| Late monthly VAT return | IDR 500,000 per affected late return subject to statutory exceptions/relief, not an additional monthly recurring charge for one return | [KUP art.7](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Missing/late/incomplete invoice fine | One percent of DPP for the applicable KUP art.14 category, in addition to underlying tax; not two percent | [KUP art.14(1)(d)-(e),(4)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Late payment | Actual ministerial monthly rate under the applicable provision; part-month counted in full and relevant cap, not fixed two percent or daily proration | [KUP art.9](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Assessment | Actual legal assessment category decides interest/uplift; specified art.13(3) VAT cases use seventy-five percent, not every audit or every underpayment | [KUP art.13(1)-(3a)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| PMSE designation criteria | Transactions over IDR 600m/year OR IDR 50m/month; and/or traffic over12,000/year OR1,000/month; actual DJP designation/effective date required | [PER-12/PJ/2025 arts.3-6](https://pajak.go.id/id/peraturan/batasan-kriteria-tertentu-pihak-lain-serta-penunjukan-pihak-lain-pemungutan-penyetoran) |
| Qualifying package courier | Ten percent times eleven-twelfths times twelve percent of replacement, effective1.1%, under its specific-amount rule | [PMK 71 art.2(2)(a)](https://www.pajak.go.id/index.php/id/peraturan/pajak-pertambahan-nilai-atas-penyerahan-jasa-kena-pajak-tertentu); [PMK 11 art.17 amending art.3(a)](https://www.pajak.go.id/index.php/id/peraturan/ketentuan-nilai-lain-sebagai-dasar-pengenaan-pajak-dan-besaran-tertentu-pajak-pertambahan) |
| Records | Ten years in Indonesia for supporting books/records/electronic data | [KUP art.28(11)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

### 1. Establish PKP status, period and completeness

A business below the general boundary can be voluntarily registered; a business above it may have an unmet mandatory obligation. **Non-PKP does not mean below threshold**, and below threshold does not prove non-PKP. For a non-PKP ordinary supplier, do not fabricate output invoices or standard input credits, but consider separate obligations on imports/utilisation of foreign services and overdue registration under their own rules. Refer retrospective registration and special pre-registration credits rather than issuing a blanket permanent denial. [VAT Law arts.3A,9(9a)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 164 arts.17-19](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

For the applicable turnover crossing, PMK 164 requires reporting for PKP confirmation no later than book-year end, with its prescribed next-year start and early option. Establish actual turnover/category, book year, notice and effective confirmation. Income-tax UMKM's amended eligibility/aggregation is not automatically the same test and a PKP can still have a separate lawful income-tax regime.

Build the full sales/purchase ledger from invoices, contracts, delivery records, accruals, cash and settlements. Include unpaid supplies, advances and imports; remove true duplicates, internal transfers and non-supply financing with evidence. Record the commercial price before VAT, legal DPP, nominal rate, special mechanism/facility, VAT, PPnBM if flagged, gross, settlement, tax point, invoice approval and period. Preserve exemptions and zero-rated income as separate reportable classes, not invisible cash exclusions.

### 2. Classify the actual supply and its legal base

For an ordinary PMK 131 supply, DPP=eleven-twelfths of commercial selling price/replacement/import value and VAT=twelve percent of DPP. If a gross invoice includes effective eleven-percent VAT, commercial price=gross divided by1.11; **that commercial price is not DPP**. Do not multiply a reduced DPP by eleven percent again. A true tax-exclusive amount is not divided as if gross. [PMK 131 art.3](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf).

PMK 131 excludes supplies governed by another prescribed other-base/specific-amount regime. Courier/freight, vouchers/telecom distribution, used vehicles, fuel/LPG, financial/payment services, self-construction and special facilities cannot all be resolved by a merchant name or the ordinary gross divisor. The relevant actual period's rule decides. PMK 11 and its amendments are not a licence to use obsolete crypto provisions from an earlier PMK 81 text; PMK 53 changes selected PMK 81 provisions and deletes specified crypto articles, with later amendments checked where relevant. Special crypto/financial instruments remain outside this ordinary method. [PMK 131 art.4](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf); [PMK 11](https://www.pajak.go.id/index.php/id/peraturan/ketentuan-nilai-lain-sebagai-dasar-pengenaan-pajak-dan-besaran-tertentu-pajak-pertambahan); [PMK 53](https://pajak.go.id/id/peraturan/perubahan-atas-peraturan-menteri-keuangan-nomor-11-tahun-2025-tentang-ketentuan-nilai).

Tax is ordinarily due on the supply; an actual payment before supply and progress payment have their own earlier invoice tax points. A refundable security/loan/internal transfer labelled DP/UANG MUKA is not automatically consideration for a taxable supply. Establish the contract and actual payment, make the appropriate advance invoice and avoid taxing it again on final settlement. Combined same-buyer/calendar-month invoices have a specific permitted month-end rule, not a general permission to delay every invoice until month end. [VAT Law art.13](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PER-11 arts.31-32](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

### 3. Distinguish exemption, outside VAT, zero rate and not-collected

Basic staples are no longer simply the old art.4A list: specified goods are exempt through art.16B/PP 49 and their detailed criteria. Rice, paddy, corn, sago, soybeans, salt, meat, eggs, milk, fruits and vegetables require the prescribed item description; specified white cane consumption sugar has its own PP 49 entry. Packaging alone does not revoke an exemption, and a supermarket name does not exempt every grocery line. Do not call an exempt purchase “zero-rated” or infer its income-tax deductibility. [VAT Law arts.4A,16B](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PP 49 arts.6-7](https://www.pajak.go.id/id/peraturan/pajak-pertambahan-nilai-dibebaskan-dan-pajak-pertambahan-nilai-atau-pajak-pertambahan).

Specified medical, education, finance, insurance, employment, public transport and other strategic services are exempt under PP 49's actual definitions. They are not all blanket art.4A non-objects. Underlying insurance differs from supporting brokerage/agent services. A financing transaction differs from an electronic payment/gateway fee. Clean water and electricity have their own goods exemption and exceptions. A brand, bank licence, electricity contract or a bare “admin” line is not sufficient legal classification. [PP 49 arts.6-8,10-19](https://www.pajak.go.id/id/peraturan/pajak-pertambahan-nilai-dibebaskan-dan-pajak-pertambahan-nilai-atau-pajak-pertambahan).

Restaurant/warung/catering meals that are objects of local tax under the statutory definition are outside national VAT, with the applicable local levy analysed separately. Do not claim national input VAT by dividing the restaurant bill by1.11, and do not describe a local PBJT amount as input PPN. Hotels, parking and entertainment have related statutory exclusions/conditions; mixed businesses can still make other taxable supplies. [VAT Law art.4A](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

Input related to exempt supplies is generally not creditable under the applicable rules; zero-rated exports can preserve lawful input credits; a not-collected facility has its own legal credit consequences. For mixed business identify direct allocations first, then the actual prescribed apportionment/recalculation for common input. A simple arbitrary taxable-turnover fraction without the required method/year information is not a filing-ready apportionment. Retain the missing full-year data flag and refer the specialist calculation. [VAT Law arts.9(5)-(6),16B](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

### 4. Use the pattern library as a search aid, not a tax engine

The original counterparty strings are retained below for matching case-insensitive descriptions and locating evidence. A more specific pattern can identify the invoice to inspect; it does **not** override legal facts or justify a taxable/exempt decision. The old automatic eleven-percent/exempt labels were wrong for multiple categories. Ask for the invoice/contract only when the evidence is missing from the record.

#### Banks, wallets and fees

Separate principal, interest/financing, taxable ancillary services and electronic payments; no blanket exemption of every fee. [Applicable primary framework](https://www.pajak.go.id/id/peraturan/pajak-pertambahan-nilai-dibebaskan-dan-pajak-pertambahan-nilai-atau-pajak-pertambahan).

`BANK CENTRAL ASIA, BCA`; `BANK RAKYAT INDONESIA, BRI`; `BANK NEGARA INDONESIA, BNI`; `BANK MANDIRI`; `CIMB NIAGA`; `BANK DANAMON`; `BANK PERMATA`; `OVO (fintech)`; `GOPAY, GOJEK (payment fee)`; `DANA E-WALLET`; `BIAYA ADMIN, BUNGA, FEE`.

#### Government/statutory payments

Reconcile true tax/contribution/principal settlements separately from underlying goods/services/import VAT. No second input merely for paying a tax balance. [Applicable primary framework](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

`DIREKTORAT JENDERAL PAJAK, DJP`; `PAJAK PERTAMBAHAN NILAI, PPN`; `PAJAK PENGHASILAN, PPH`; `BPJS KESEHATAN`; `BPJS KETENAGAKERJAAN`; `BEA CUKAI, CUSTOMS`; `IURAN BPJS`.

#### Utilities

Electricity/clean-water exemptions and exceptions, fuel/gas products and telecom services require the actual bill and regime. Do not default every PLN or gas bill to ordinary taxable VAT. [Applicable primary framework](https://www.pajak.go.id/id/peraturan/pajak-pertambahan-nilai-dibebaskan-dan-pajak-pertambahan-nilai-atau-pajak-pertambahan).

`PLN, PERUSAHAAN LISTRIK NEGARA`; `PDAM, AIR MINUM`; `PERTAMINA`; `PERTAGAS, PGN (gas network)`; `TELKOM INDONESIA`; `TELKOMSEL`; `INDOSAT OOREDOO HUTCHISON`; `XL AXIATA`; `SMARTFREN`; `FIRST MEDIA, MNC PLAY`.

#### Transport/logistics

Separate qualifying public transport/exempt routes, domestic air, charter, courier-specific amounts, platform service fees and underlying fare. A foreign destination is not a universal export zero rate. [Applicable primary framework](https://www.pajak.go.id/id/peraturan/pajak-pertambahan-nilai-dibebaskan-dan-pajak-pertambahan-nilai-atau-pajak-pertambahan).

`GARUDA INDONESIA`; `LION AIR, WINGS AIR`; `CITILINK`; `BATIK AIR`; `GOJEK (ride)`; `GRAB INDONESIA (ride)`; `BLUEBIRD TAXI`; `DAMRI`; `KAI, KERETA API INDONESIA`; `JNE, JALUR NUGRAHA EKAKURIR`; `TIKI TITIPAN KILAT`; `J&T EXPRESS INDONESIA`; `SICEPAT EKSPRES`; `ANTERAJA`; `NINJA VAN INDONESIA`.

#### Food/retail/marketplaces

Inspect line items and actual seller, staple criteria, restaurant local-tax status, marketplace fees and taxable merchandise separately. Packaging alone is not an exemption test. [Applicable primary framework](https://www.pajak.go.id/id/peraturan/pajak-pertambahan-nilai-dibebaskan-dan-pajak-pertambahan-nilai-atau-pajak-pertambahan).

`INDOMARET`; `ALFAMART`; `HYPERMART`; `CARREFOUR INDONESIA, TRANS MART`; `GIANT (HERO GROUP)`; `TOKOPEDIA (marketplace)`; `SHOPEE INDONESIA (marketplace)`; `LAZADA INDONESIA (marketplace)`; `BUKALAPAK (marketplace)`; `RESTORAN, RUMAH MAKAN (restaurant)`.

#### Domestic software

Verify actual selling entity, supply, PKP and approved invoice. No vendor is permanently certified by this pattern table. [Applicable primary framework](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

`JURNAL.ID (Mekari)`; `ACCURATE ONLINE`; `ZAHIR ACCOUNTING`; `KLIKPAJAK (Mekari)`; `TALENTA (Mekari)`.

#### Foreign subscriptions/PMSE

Verify actual provider legal entity and period-specific designation, payment, buyer identity and compliant receipt. Business versus consumer labels do not remove the PMSE liability. [Applicable primary framework](https://pajak.go.id/id/peraturan/batasan-kriteria-tertentu-pihak-lain-serta-penunjukan-pihak-lain-pemungutan-penyetoran).

`GOOGLE (Workspace, Ads, Cloud)`; `MICROSOFT (365, Azure)`; `META, FACEBOOK ADS`; `NETFLIX`; `SPOTIFY`; `ZOOM`; `SLACK`; `NOTION, OPENAI, ANTHROPIC`; `AWS (Amazon)`.

#### Payment processors

Identify actual taxable payment/gateway/technology fee versus exempt financing; no automatic exemption. Establish the applicable current special/ordinary rule before a rate. [Applicable primary framework](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

`MIDTRANS (biaya)`; `DOKU (biaya)`; `XENDIT (biaya)`; `STRIPE (biaya)`.

#### Internal movements, finance, wages and advances

Evidence true own-account transfer, loan principal, dividend/payroll or cash withdrawal separately. An advance for a taxable supply can trigger tax; an unexplained bank narrative cannot decide it. [Applicable primary framework](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

`TRANSFER ANTAR REKENING, INTERNAL`; `PINJAMAN, CICILAN PINJAMAN`; `GAJI, UPAH, SALARY`; `DIVIDEN`; `UANG MUKA, DP (deposit advance)`; `TARIK TUNAI, ATM`.

No current PMSE designation is certified merely from GOOGLE, MICROSOFT, META, AWS or another brand. A taxable invoice issued by a different group entity must be checked as that actual entity. A salary, principal, dividend, tax deposit or internal transfer is not a purchase of a taxable service merely because a bank line exists; split any fee or underlying transaction rather than losing it with the excluded principal.

### 5. Determine lawful input VAT, including equivalent documents

Use the actual approved invoice or a legally equivalent document, correct taxpayer/period, taxable-business connection and credit conditions. Under art.9(9), an otherwise creditable input not claimed in its own period can be claimed in at most three following periods if not already expensed/capitalised and other conditions hold. This does not establish a universal “within three months or lost forever” rule; amendments, pre-registration, audit-disclosed input and paid-assessment credits have separate statutory routes. Refer cases needing those rules rather than silently denying them. [VAT Law art.9(2)-(9c)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

The ordinary exclusions include no direct business connection and defective invoice/content; the law does not impose a universal ban labelled “entertainment/golf” in this current general list. Personal use, exempt activity or unsupported evidence can still prevent a credit on the actual facts. A non-PKP retail receipt does not create VAT, but “only a standard Faktur Pajak ever qualifies” is also wrong: law permits prescribed equivalent documents. [VAT Law arts.9,13(6)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PER-11 arts.62-69](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

For imports retain the actual customs declaration, supporting packet, taxpayer identity, state collection validation and electronic interchange conditions. Never multiply the entire bank customs transfer by a VAT rate: duty, excise, VAT and income-tax import collections are different. For a taxable utility/airline/bank service, the prescribed bill/ticket may be equivalent subject to formal/material and buyer-identity rules; a generic unauthorised receipt is not. [PER-11 arts.62-69](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

**PMSE input is not a general grey area.** Current PER-12/PJ/2025 art.11 and PER-11 art.69(5) permit the specified PMSE collection document as input subject to buyer identity/account evidence and ordinary credit rules. Obtain the paid commercial invoice/billing/order receipt noting VAT, the actual designated collector and the buyer's required name/NPWP/NIK or DJP-registered email, or qualifying attached account evidence. A provider brand or card charge alone is insufficient; a document need not fail merely because it is called a commercial invoice rather than domestic Faktur Pajak. [PER-12/PJ/2025 art.11](https://pajak.go.id/id/peraturan/batasan-kriteria-tertentu-pihak-lain-serta-penunjukan-pihak-lain-pemungutan-penyetoran); [PER-11 arts.62(p),67(5)-(6),69(5)](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

Keep pending input amounts in a separate evidence register, not as final claimed tax and not as permanently disallowed expenses. Missing business use or taxable/exempt allocation blocks the dependent final claim; it is not resolved with a fictitious zero-percent business assumption. Check duplicate claim, credit period, correction/refund history and current return status before using any credit.

### 6. Review foreign-service purchases and exports separately

PMSE applies to the specified imported intangible/digital/service utilisation in Indonesia, including business users; it is not only a B2C regime. Appointment by DJP and its effective/revocation dates matter. The current designation thresholds include annual **or monthly** transaction/traffic alternatives. Passing a threshold is not automatic appointment or proof a particular invoice was collected by that appointed entity. [PMK 81 arts.332-337](https://pajak.go.id/en/node/113110); [PER-12/PJ/2025 arts.2-6](https://pajak.go.id/id/peraturan/batasan-kriteria-tertentu-pihak-lain-serta-penunjukan-pihak-lain-pemungutan-penyetoran).

If the taxable foreign utilisation was not collected by the designated party, the recipient's self-accounting obligation can remain under VAT Law art.3A/PMK 81 art.332(5), even if the recipient is not a PKP. Confirm the current procedure/base/payment and obtain evidence before calculating a final amount. Do not duplicate self-payment where valid PMSE collection has already settled the same VAT, or treat a foreign currency card statement as proof no Indonesian VAT applies.

For export goods obtain the actual PEB/customs exit and sales/settlement evidence and applicable special-zone rules. For services, identify the prescribed type, work produced in Indonesia for utilisation outside customs territory and actual recipient. PMK 81 lists qualifying mobile/immovable/result-delivered service classes; technology/IT and the listed business/technical consultancies require their actual definition. Obtain the written agreement stating service type, activity and value and lawful payment evidence. A foreign customer, USD payment or an email stating “export” alone does not establish zero-rating. The rule does not universally require payment in foreign currency; do not deny a genuine export solely because paid in rupiah. [PMK 81 arts.278-282](https://pajak.go.id/en/node/113110).

Qualifying service export tax point is when replacement is recorded/recognised as a receivable or income; its prescribed export notification plus invoice is an equivalent tax document. If the actual required contract/payment conditions are not met, art.282(2) treats the specified activity as domestic taxable supply. Distinguish that legal failure from evidence not yet obtained: keep the latter pending, and show any provisional domestic comparison without asserting a false location. Services both produced and utilised abroad have a separate rule. [PMK 81 arts.282-284](https://pajak.go.id/en/node/113110).

### 7. Reconcile designated collectors, input and compensation

Identify the actual designated government/BUMN/other collector and payment exception before classifying a short receipt. Split output VAT collected by supplier, output handled by the designated collector, income-tax withholding, fees and commercial adjustments. The supplier still reports supplies/tax under art.16A, but does not pay again tax validly remitted by the collector. Obtain actual collector/invoice/state-collection evidence; a cash difference alone is not an input credit or proof a customer is designated. The old instruction both to “credit” government VAT and to never offset it was too vague: follow the current collector reporting mechanism, not an ordinary purchase-input line. [VAT Law art.16A](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

Compute ordinary own output less lawful input; bring forward only the actual supported excess after accepted prior corrections/refunds/decisions, and account for earlier valid deposits. An excess is not automatically a cash refund. Ordinary year-end and specified period refund rights, preliminary-refund categories and examination requirements differ. The old categorical statement that every exporter refund requires the same audit was too broad; preserve specialist review and exact current procedure without promising either a refund or universal audit. [VAT Law art.9(3)-(4f)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

From the applicable PER-12/PJ/2026 commencement/transition, normal VAT returns are sequential with the stated exception; corrections account for earlier payments and prescribed decisions/refunds. Compensation differences use the specified next-unfiled normal period/termination rules, with legacy2024-to-January2025 rules where relevant. Do not blindly amend every intervening return, carry a refunded credit or double-pay an earlier deposit. Pending examination/open preliminary investigation may restrict correction. [PER-12/PJ/2026 amended arts.29A-29E,129A and art.II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan).

### 8. Complete invoice, return and deadline checks

Read `id-einvoice-coretax`. Coretax electronic invoices have seventeen digits and receive a serial on upload **and approval**; the tax invoice must be made at its actual legal tax point, while upload/approval is due no later than twentieth of next month. Do not request a fictional Coretax serial stock, issue every invoice only at month end or assume a QR/PDF proves approval. Eligibility-limited desktop use and designated integrated PJAP are separate channels, so the old desktop-retired claim is removed. No universal Mobile/Coretax Form VAT filing entitlement is certified here. [PER-11 arts.31-44](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

Wrong buyer identity requires cancellation/new correct invoice; other errors can require replacement, with actual reporting/correction periods and conditions. Retain original/replacement/cancelled/return notes and prevent duplicate output/input. A transient QR failure requires checking official approval and issuer; it is not a reason to create two live invoices or automatically deny every credit. [PER-11 arts.48-50](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

Pay the supported ordinary own VAT balance before submitting the return and no later than the applicable end of following month, with actual holiday/import/collector exceptions. A reminder email/dashboard, valid billing code or documented outage does not extend a deadline. No force-majeure relief is invented. Preserve the full filed return/attachments and accepted BPE separately from payment NTPN and draft/upload status. [VAT Law art.15A](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 81 arts.94 and 100](https://pajak.go.id/en/node/113110).

The old I.A/I.B/I.C,II,III.A-III.D,IV-VI labels remain a conceptual worksheet inventory: taxable domestic, export, exempt/non-taxable, output, domestic/import/non-creditable/net input, pre-compensation balance, prior excess and final balance. They are not a certified current Coretax statutory line map. Download the actual tax-period form/annex and map those concepts to its fields before filing. Keep exempt and outside-tax supplies distinct even if an older worksheet grouped them together.

### 9. Calculate sanctions only from the applicable provision

A late VAT return generally attracts the statutory IDR 500,000 for that affected return, subject to exceptions/relief; it is not multiplied by every month of delay for the same return. Missing/late/incomplete invoices in the specified KUP art.14 categories can trigger one percent of DPP plus tax. The source is **KUP art.14**, not VAT Law art.14, and not the old two-percent instruction. Do not label every portal warning as that fine. [KUP arts.7,14](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

Late-payment interest needs actual provision, period, principal, start/end and ministerial rate. Assessment interest/uplifts depend on the statutory category. The art.13(3) VAT increase is seventy-five percent for its specified cases; the law also contains distinct hundred-percent additional-assessment rules, so neither “every audit is100%” nor “no100%sanction exists anywhere” is correct. Do not reuse a March2025 reference rate for2026, confuse different benchmark uplifts or apply fixed two percent/daily proration. Criminal/fraudulent invoice cases require specialist legal review; preserve evidence and do not offer a definitive criminal sentence calculation. [KUP arts.9,13-15](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

### 10. Produce a complete working paper and unresolved-evidence list

The workbook retains the original output/input/compensation sections, now with one record per legal supply/document and no universal eleven-percent formula:

```text
INDONESIA PPN WORKING PAPER / KERTAS KERJA SPT MASA PPN
Taxpayer, actual identity/PKP, period, normal/correction, source versions
A. OUTPUT: commercial price, legal DPP, nominal rate/specific mechanism,
   output tax, own versus designated-collector settlement,
   exports, exempt supplies, outside VAT and not-collected facilities
B. INPUT: domestic invoices, imports, foreign utilisation/PMSE,
   approved/equivalent evidence, business use/direct allocation,
   eligible credit period, non-creditable/pending and eligible input
C. BALANCE: own output less supported eligible input,
   verified carried excess and correction/compensation/refund history,
   actual earlier payment, remaining own payable OR supported excess
D. EVIDENCE: invoice/return-note/approval IDs, contracts/export/customs,
   receipts/slips, linked bank entries and unresolved differences
E. REVIEW: source, legal regime, assumptions, missing facts, owner action
```

Formulas must recalculate each regime independently and agree to the commercial ledger, invoices, accepted previous returns and state receipts. Avoid double-counting a settlement or carryforward. A negative net balance stays negative in the working paper; it is not concealed by capping input or automatically refunded.

Retain all five bank-format checks from the original: **BCA** Tanggal/Keterangan/Debit/Kredit/Saldo; **BRI** Tgl Transaksi/Uraian/Debit/Kredit/Saldo; **BNI** Tanggal/Mutasi/Debet/Kredit/Saldo; **Mandiri** Tgl/Ket-Keterangan/Debet/Kredit/Saldo; **CIMB Niaga** Date/Description/Debit/Credit/Balance. These are parsing clues; inspect the actual export and verify sign, date and running balance. Indonesian `Rp111.000.000` means IDR 111,000,000; periods commonly separate thousands and comma decimals. Do not treat the running Saldo as a second transaction.

Retain narrative clues: Transfer Masuk=incoming, Transfer Keluar=outgoing, Bayar Tagihan=bill payment, Penerimaan Valas=foreign-currency receipt, Bunga=interest, Biaya Admin=fee, Saldo=balance, Keterangan/Uraian=description, Tarik Tunai/ATM=cash withdrawal, Gaji=wages. These identify evidence to locate, not a proven revenue/export/exemption/input classification.

The old arbitrary IDR 100m transaction, IDR 11m default-tax difference, forty-percent concentration, more-than-four-defaults and IDR 50m balance flags were internal triage values, not law. Remove them as mandatory thresholds. Flag any material/unsupported classification, unexplained reconciliation, missing valid evidence, duplicate, unusual related-party/collector/foreign flow or deadline risk without pretending a smaller error is acceptable.

Onboarding can proceed with supported rows and visibly pending rows. Preserve the original eight minimum questions in updated form: actual identifier; PKP confirmation/effective date; period; export evidence; designated-collector evidence; foreign software/provider and collection document; prior compensated excess; advance invoices. Do not ask again if those facts are already in the record. Never apply the old blanket defaults to manufacture a filed-ready total.

## Worked cases

The original six BCA-statement examples are retained as hypothetical calendar2026 transactions for a Jakarta IT consulting PKP. The names are transaction labels, not proof of registration or tax treatment. Source invoices/contracts are expressly supplied or missing; actual tax-point and FX rates must be verified for a real filing.

### Example 1. PT TEKNOLOGI NUSANTARA, domestic receipt

`15/04/2026 Transfer Masuk PT TEKNOLOGI NUSANTARA REF:FP-2026-041 Rp111.000.000 SaldoRp500.000.000`

Assume the actual invoice confirms an ordinary non-luxury taxable supply, priceIDR100m excluding VAT, no withholding/fee/advance adjustment and valid PKP invoice. OutputVAT11m; gross111m. **Legal DPP is91,666,666.6667**, not the100m commercial price. Preserve exact arithmetic before actual prescribed invoice rounding. A different net bank receipt needs a reconciliation, not a new tax-inclusive split. [PMK 131 art.3](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf).

```oa-check
name: Ordinary domestic receipt price versus VAT base
inputs:
  price: 100000000
  nominal_rate: 0.12
steps:
  - dpp: price * 11 / 12
  - output_vat: dpp * nominal_rate
  - gross: price + output_vat
expected:
  dpp: 91666666.66666667
  output_vat: 11000000
  gross: 111000000
```

### Example 2. ACME CORPORATION USA, possible service export

`22/04/2026 Penerimaan Valas ACME CORPORATION USA Technical consulting Q1/2026 USD5000 (Rp80.000.000)`

The supplied IDR 80m valuation is a case input, not a verified ministerial exchange rate. If the actual technical/IT service falls within the prescribed class, is produced/delivered for utilisation abroad and has the required written agreement and valid payment evidence, exportVAT is nil. Required export notification/invoice and correct tax point remain. Foreign customer plus USD alone is insufficient. A supported domestic ordinary alternative at the same tax-exclusive price would be8.8m, but do not apply that alternative as a fact just because a document is pending. [PMK 81 arts.278-284](https://pajak.go.id/en/node/113110); [PMK 131 art.3](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf).

```oa-check
name: Export and explicitly conditional domestic alternative
inputs:
  supplied_rupiah_value: 80000000
  export_rate: 0
  ordinary_effective_rate: 0.11
steps:
  - qualifying_export_vat: supplied_rupiah_value * export_rate
  - conditional_domestic_vat: supplied_rupiah_value * ordinary_effective_rate
expected:
  qualifying_export_vat: 0
  conditional_domestic_vat: 8800000
```

### Example 3. PLN electricity, no automatic credit

`10/04/2026 Bayar Tagihan PLN UNIT PELAYANAN ListrikApril2026 Rp5.500.000 SaldoRp44.500.000`

PP 49 generally exempts electricity including connection/load charges, except the specified household power category. For an actual qualifying exempt business electricity bill with **no VAT charged**, input isnil, not the oldIDR545,045 implied credit. If the actual bill contains a separately taxable product/service or an exception, classify that actual line and use its prescribed equivalent document; do not infer it from PLN. The old gross divisor is shown only to quantify the false claim. [PP 49 art.6(2)(l)](https://www.pajak.go.id/id/peraturan/pajak-pertambahan-nilai-dibebaskan-dan-pajak-pertambahan-nilai-atau-pajak-pertambahan); [PER-11 arts.62(d),67-69](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

```oa-check
name: Exempt electricity does not create deemed input
inputs:
  exempt_bill: 5500000
  actual_vat: 0
  wrong_effective_rate: 0.11
steps:
  - lawful_input_from_this_exempt_bill: actual_vat
  - erroneous_implied_vat: exempt_bill * wrong_effective_rate / (1 + wrong_effective_rate)
expected:
  lawful_input_from_this_exempt_bill: 0
  erroneous_implied_vat: 545045.045045045
```

### Example 4. JNE package delivery, specific amount

`08/04/2026 Transfer Keluar JNE JALUR NUGRAHA EKAKURIR OngkosKirimMaret2026 Rp11.000.000 SaldoRp33.500.000`

Assume the actual invoice establishes **package-delivery service within PMK 71 art.2(2)(a)** and priceIDR11m excluding VAT, with valid buyer evidence and taxable-business use. The specific amount is10%times11/12times12%=1.1%ofreplacement:VAT121,000,gross11,121,000. Therefore the bank debit11m cannot also be that gross invoice without an explained settlement/partial-payment difference. If instead the documented11m is fully VAT-inclusive for this exact mechanism, replacement=10,880,316.5183 and VAT119,683.4817, subject to actual required invoice rounding. Neither option supports the old ordinary-eleven-percent input1,090,090. Don't choose between exclusive/inclusive from a brand. PMK 71's input restriction concerns the supplier's inputs for those services, not an automatic denial of a properly evidenced customer's otherwise lawful credit. [PMK 71 arts.2,5](https://www.pajak.go.id/index.php/id/peraturan/pajak-pertambahan-nilai-atas-penyerahan-jasa-kena-pajak-tertentu); [PMK 11 art.17](https://www.pajak.go.id/index.php/id/peraturan/ketentuan-nilai-lain-sebagai-dasar-pengenaan-pajak-dan-besaran-tertentu-pajak-pertambahan).

```oa-check
name: Package-delivery specific amount and inclusive alternative
inputs:
  quoted_exclusive_replacement: 11000000
  bank_debit_if_inclusive: 11000000
  statutory_fraction: 0.10
  nominal_rate: 0.12
steps:
  - effective_amount_fraction: statutory_fraction * 11 / 12 * nominal_rate
  - vat_if_exclusive: quoted_exclusive_replacement * effective_amount_fraction
  - gross_if_exclusive: quoted_exclusive_replacement + vat_if_exclusive
  - replacement_if_inclusive: bank_debit_if_inclusive / (1 + effective_amount_fraction)
  - vat_if_inclusive: bank_debit_if_inclusive - replacement_if_inclusive
expected:
  effective_amount_fraction: 0.011
  vat_if_exclusive: 121000
  gross_if_exclusive: 11121000
  replacement_if_inclusive: 10880316.518298714
  vat_if_inclusive: 119683.48170128651
```

### Example 5. GOOGLE IRELAND LIMITED, PMSE invoice reconciliation

`05/04/2026 DebitKartu GOOGLE IRELAND LIMITED GoogleWorkspaceApril2026 Rp3.300.000 SaldoRp30.200.000`

Assume a real paid invoice from the actually designated collector states tax-exclusive price3m and ordinary PMK 131VAT330,000 with qualifying buyer identity/account evidence. Total is **3,330,000**, not3,300,000; reconcile the30,000 difference in the statement before finalising. If the documented3.3m is instead the inclusive full invoice for that ordinary mechanism, commercial price=2,972,972.973 andVAT327,027.027, subject to actual invoice rounding. Do not fabricate a330k credit from an unexplained3.3m debit. PMSE input can be lawful under the named document rule; no general “ask whether DJP permits it” gap remains. [PER-12/PJ/2025 art.11](https://pajak.go.id/id/peraturan/batasan-kriteria-tertentu-pihak-lain-serta-penunjukan-pihak-lain-pemungutan-penyetoran); [PER-11 art.69(5)](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0); [PMK 131 art.3](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf).

```oa-check
name: PMSE invoice and card amount do not reconcile
inputs:
  stated_price: 3000000
  effective_fraction: 0.11
  card_amount: 3300000
steps:
  - stated_vat: stated_price * effective_fraction
  - correct_gross: stated_price + stated_vat
  - unreconciled_difference: correct_gross - card_amount
  - price_if_card_is_inclusive: card_amount / (1 + effective_fraction)
  - vat_if_card_is_inclusive: card_amount - price_if_card_is_inclusive
expected:
  stated_vat: 330000
  correct_gross: 3330000
  unreconciled_difference: 30000
  price_if_card_is_inclusive: 2972972.972972973
  vat_if_card_is_inclusive: 327027.0270270272
```

### Example 6. TOKO SEMBAKO MAKMUR, staple evidence

`12/04/2026 Pembelian TOKO SEMBAKO MAKMUR BerasdanGula Rp5.000.000 SaldoRp25.200.000`

If the actual itemised receipt establishes qualifying rice and the specified white cane consumption sugar within PP 49's criteria, with noVAT charged, inputVATnil. Preserve the purchase in books; it is exempt, not an assumed zero-rated supply. If the sugar/product details or mixed receipt do not meet the rule, obtain them and classify the actual items. No packaged-food prohibition or universal income-tax business deduction is inferred. [PP 49 arts.6-7](https://www.pajak.go.id/id/peraturan/pajak-pertambahan-nilai-dibebaskan-dan-pajak-pertambahan-nilai-atau-pajak-pertambahan).

```oa-check
name: Confirmed exempt staple purchase has no deemed input
inputs:
  qualifying_staple_cost: 5000000
  vat_shown: 0
steps:
  - payable_to_supplier: qualifying_staple_cost + vat_shown
  - input_from_this_purchase: vat_shown
expected:
  payable_to_supplier: 5000000
  input_from_this_purchase: 0
```

## When to refuse or refer

- **R-ID-1:** absent/uncertain PKP effective status or overdue registration: no invented ordinary VAT invoice/credit, but retain separate foreign-utilisation/import duties and obtain the actual registration analysis.
- **R-ID-2:** PPnBM/luxury-list tax, special real estate, construction or separately regulated regimes beyond the verified computation: preserve the transaction and refer; a generic merchant rate is insufficient.
- **R-ID-3:** mixed taxable/exempt/non-business input requiring allocation/recalculation: obtain the prescribed method/year facts, not a guessed percentage.
- **R-ID-4:** exporter refund or special preliminary-refund process: retain supporting records and refer the actual procedure, without promising a universal audit or immediate refund.
- **R-ID-5:** designated-collector/government contract: establish the actual designation, invoice, collection/remittance and return treatment, with no duplicate payment or misclassified input.
- Missing export classification/payment/contract, PMSE collector/identity document, receipt line split, advance contract, input validity, foreign exchange, correction/examination status or unexplained commercial-bank difference blocks only the dependent final claim. Continue supported working-paper sections and state the precise gap.

### Final checks

Confirm taxpayer/PKP/period; complete invoice ledger; commercial price versus DPP/regime; tax point/approval; export evidence; exempt versus outside-tax/not-collected distinction; valid domestic/import/PMSE input; business use and timing; collector settlement; originals/replacements/cancellations/return notes; prior excess/refunds/corrections; actual own payment/state receipt; current form mapping and acceptedBPE; no duplicate; retained records. Output a working paper, evidence register and authorised-filer action list. Never claim a live filing or professional approval that did not happen.

## Sources

- Read 2026-11-14: [DJP consolidated KUP and VAT laws](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf), VAT arts.3A,4A,7-9,13,15A,16A-16B and KUP arts.7,9,13-15,28. Read the operative provisions for registration, rate/base, credit/exclusions, invoice point, collector/deadline/facility and sanctions; original-law examples are not substituted for later PMK mechanisms.
- Read 2026-11-14: [PMK 131/2024 actual official PDF](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf), operative arts.1-6, ordinary base, luxury and narrowly scoped January2025 consumer transition, separately regulated exceptions.
- Read 2026-11-14: [PP 49/2022 actual operative text](https://www.pajak.go.id/id/peraturan/pajak-pertambahan-nilai-dibebaskan-dan-pajak-pertambahan-nilai-atau-pajak-pertambahan), arts.6-8 electricity/water/staples and arts.10-19 strategic-service scope, including actual finance/insurance/education/transport distinctions. The complete goods/sector annex and every exception were not certified.
- Read 2026-11-14: [PMK 71/2022](https://www.pajak.go.id/index.php/id/peraturan/pajak-pertambahan-nilai-atas-penyerahan-jasa-kena-pajak-tertentu), arts.2-5 actual package/freight scope and supplier-input restriction; [PMK 11/2025](https://www.pajak.go.id/index.php/id/peraturan/ketentuan-nilai-lain-sebagai-dasar-pengenaan-pajak-dan-besaran-tertentu-pajak-pertambahan), art.17 amended specific-amount formula and transition; [PMK 53/2025](https://pajak.go.id/id/peraturan/perubahan-atas-peraturan-menteri-keuangan-nomor-11-tahun-2025-tentang-ketentuan-nilai), actual limited amendment/deletions and commencement. No current crypto computation is supplied.
- Read 2026-11-14: [PMK 81/2024 actual text](https://pajak.go.id/en/node/113110), arts.94-100 payment,278-284 export definition/type/document/tax point,332-339 PMSE framework; later special-regime amendments must be applied where relevant. The ordinary administration portions were checked against the cached actual PMK1/2026 amendment inventory.
- Read 2026-11-14: [PER-12/PJ/2025 current PMSE rule](https://pajak.go.id/id/peraturan/batasan-kriteria-tertentu-pihak-lain-serta-penunjukan-pihak-lain-pemungutan-penyetoran), arts.2-6 designation/criteria,art.11 paid-document/identity and input entitlement. Do not confuse this with the different PER-12/PJ/2026 reporting amendment.
- Read 2026-11-14: [PER-11/PJ/2025](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0), arts.31-44 invoices,48-50 replacement/cancellation,62-69 equivalent documents and input requirements. Full current form/code annex not certified.
- Read 2026-11-14: [PER-12/PJ/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan), amended29A-29E and129A plus art.II for current compensation,correction,transition and commencement, not an automatic audit-stopping right.
- Read 2026-11-14: [PMK 164/2023](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau), arts.17-19 PKP crossing and early confirmation process.
- Read 2026-11-14: [DJP identifier implementation release](https://www.pajak.go.id/index.php/id/siaran-pers/peluncuran-layanan-perpajakan-berbasis-nik-sebagai-npwp-npwp-16-digit-dan-nitku), actual NIK/residence versus non-resident/entity NPWP and NITKU distinction; not a fifteen-digit foreigner exception.

Not yet confirmed: actual taxpayer-specific current PKP/collector/PMSE designation and valid document status; complete staple/product/transport/payment-service special regime for each unmatched line; exact current Coretax form/annex field and permitted channel; applicable import/FX rate and prescribed invoice/payment rounding; full mixed-input annual allocation; specific refund/preliminary-refund/real-estate/construction/PPnBM facilities; actual sanction provision and ministerial interest rate for a late payment. No unknown is filled with a guessed country, eleven-percent rate, bank status or blanket nil business-use assumption.

### Preservation and corrections

All original nine supplier-pattern families and every named pattern, six worked transaction examples, input/export/PMSE/collector/advance/mixed-grocery gaps, five refusal categories, output/input/compensation worksheet, five bank formats and narrative clues, eight onboarding questions, retained-record/final checks and special-regime referrals remain above. Corrected: nominal/base confusion; universal merchant exemptions/rates; electricity/public-transport/restaurant treatment; packaged-staple prohibition; PMSE document grey-area claim and incomplete designation thresholds; courier-specific amount; PMSE arithmetic; old sanction rates; universal three-month denial; month-end invoice permission; manual Coretax numbering/desktop retired; foreign fifteen-digit ID; obsolete fixed form map and arbitrary triage/defaults. No person's contribution credit or approval changed; no country file was deleted.

## Prohibitions

Never invent inputVAT from a non-tax retail receipt, merchant name or tax remittance; confuse commercial price with legal DPP; substitute a blanket ordinary multiplier for a special/exempt/export regime; treat packaging as disqualifying all staples; omit designated-collector evidence; double-claim/pay/carry a refunded amount; fabricate export identity/documents; back-date an invoice; or present an unresolved/unsigned working paper as a filed return.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at openaccountants.com.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `indonesia-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/indonesia-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
