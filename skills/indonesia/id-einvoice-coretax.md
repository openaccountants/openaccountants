---
name: id-einvoice-coretax
description: Use this skill whenever asked about filing, invoicing, or submitting any Indonesian tax obligation through the Coretax DJP system that went live 1 January 2025. Trigger on phrases like "Coretax DJP", "Coretax pajak", "Coretax login", "e-Faktur Indonesia", "e-Bupot Unifikasi", "NSFP", "Nomor Seri Faktur Pajak", "SPT Masa Unifikasi", "Indonesia tax filing system", "DJP Online vs Coretax", "Coretax Form", "Coretax Mobile", "NIK as NPWP", "16-digit NPWP", "pajak.go.id new system", "Coretax onboarding", or any operational query about how to file, issue invoices, or pay tax to the Indonesian DJP from 2025 onward. This skill covers the Coretax platform mechanics, account activation, NIK/NPWP integration, e-Faktur issuance and NSFP management within Coretax, e-Bupot Unifikasi withholding slip workflow, SPT filing channels, and the DJP Online to Coretax cutover. It does NOT compute the underlying tax - VAT (PPN) sits in indonesia-vat, withholding PPh 21 sits in id-payroll-pph21, and corporate / individual income tax sits in their respective skills. ALWAYS read this skill when filing or invoicing through Coretax DJP.
jurisdiction: ID
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: e-invoicing
version: "2.0"
category: international
type: filing-howto
---

# Indonesia Coretax, e-Faktur and e-Bupot v2.0

## Scope

Prepare an Indonesian 2026 invoice, withholding, payment and return workflow from an already supported tax computation. This is a platform and evidence method, not a substitute for classifying the tax. Read `indonesia-vat` for PPN, `id-payroll-pph21` for employment withholding, `id-pph-final-umkm` for qualifying turnover tax and `id-corporate-tax` for ordinary company tax. `id-income-tax` is the US Idaho skill, not an Indonesian individual-income method. Do not load it for Indonesia.

Coretax DJP is the taxpayer portal and administration platform associated with the Pembaruan Sistem Inti Administrasi Perpajakan (PSIAP), also called SIAP. PMK 81/2024 is the operative administration framework from the start of 2025, with amendments. The portal is [coretaxdjp.pajak.go.id](https://coretaxdjp.pajak.go.id). The operator is Direktorat Jenderal Pajak, Kementerian Keuangan. Indonesian rupiah is the ordinary currency; an authorised foreign-currency bookkeeping/return case needs its own verified route. [PMK 81](https://pajak.go.id/en/node/113110); [PER-3 art. 2](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0).

The old claim that all legacy tools vanished and the desktop e-Faktur client was retired is false. DJP expressly allowed a desktop channel with conditions. Coretax, designated integrated PJAP applications and eligible desktop use are distinct routes. PER-11/PJ/2025 regulates reporting and invoices; PER-3/PJ/2026 regulates return submission/receipt; PER-12/PJ/2026 changes specified reporting/correction rules from its commencement. This method does not certify a live menu, mobile build or bulk-upload schema that has not been inspected for this taxpayer and form. [PER-11](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0); [PER-3](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0); [PER-12 art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan); [DJP desktop announcement](https://www.pajak.go.id/index.php/id/pengumuman/pembuatan-faktur-pajak-melalui-aplikasi-e-faktur-client-desktop).

Contributor: Open Accountants Community.

## Ask the client first

Read the existing intake, books, tax computations, prior invoices/slips/returns, payment evidence and error tickets before asking anything. Obtain only missing facts:

- Actual taxpayer legal identity, resident/non-resident status, NPWP/NIK and NITKU/location where applicable; legal form and PKP confirmation/date.
- Tax period, original or correction status, exact obligation and relevant pre-2025 history; accounting currency/year and actual source method/version.
- Taxpayer or authorised representative who will activate, prepare and sign; current role/authority and whether an authorised electronic signature is available. Never ask them to send a password, passphrase, private key, OTP or credential file to the assistant.
- Supported transaction ledger and source invoices/contracts: supply, advance/progress payment, recipient identity, article/object code, price/base/rate/tax, exemption/treaty/certificate and dates. A portal's arithmetic does not establish legal classification.
- Existing accepted-return receipt, original/replacement/cancellation links, previous tax payments and credits/refunds/compensation. Confirm none of the transactions has already been uploaded, signed, paid or submitted through another channel.
- Volume, current channel eligibility, current official import template and validation report. A PJAP connection may help a high-volume taxpayer, but integration implementation is engineering scope.

A draft can be assembled with labelled missing fields. No activated/authorised access means no filing-ready signing claim; no underlying computation means no tax-total claim. Do not use a guessed KLU, identifier, recipient, PKP date, withholding article or tax code as a conservative default. A valid legal paper-filing exception is not disproved solely by an unactivated portal profile. [PER-3 arts. 7-8](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0).

## The method, step by step

## Rates, dates and limits

| Item | Rule and boundary | Official source |
|---|---|---|
| Current invoice format | Seventeen digits: two transaction-code digits, two status-code digits and thirteen serial digits | [PER-11 art. 37](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0) |
| Coretax electronic serial | Automatically assigned when uploaded AND approved; no Coretax request for a serial-number stock | [PER-11 art. 43](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0) |
| Invoice approval deadline | Upload and DJP approval no later than twentieth of following month; no approval means no qualifying electronic tax invoice | [PER-11 art. 44](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0) |
| Invoice tax point | Supply, payment before supply, progress payment or other prescribed point; not whenever the operator has a spare serial | [PER-11 art. 31](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0) |
| Consolidated invoice | Same buyer and calendar month, made by month end; separate transaction codes and statutory exceptions apply | [PER-11 art. 32](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0) |
| Ordinary PPh deposit | Fifteenth of following month for the listed categories, subject to the actual category exception and holiday rule | [PMK 81 arts. 94 and 100](https://pajak.go.id/en/node/113110) |
| Ordinary monthly income-tax return | Twenty days after period end unless specifically varied | [KUP art. 3(3)(a)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| VAT own monthly balance | End of following month and before the return; distinguish collectors and import payments | [PMK 81 art. 94(3)](https://pajak.go.id/en/node/113110) |
| VAT monthly return | End of following month under its specific statutory rule | [VAT Law art. 15A(2)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Annual individual return | Three months after the actual tax-year/part-year end; ordinarily 31 March 2027 for calendar 2026 | [PER-3 art. 4](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Annual entity return | Four months after actual year/part-year end; ordinarily 30 April 2027 for calendar 2026 | [PER-3 art. 4](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Annual balance payment | Before submission, no later than the applicable annual deadline; extension is not automatically payment deferral | [PMK 81 art. 95](https://pajak.go.id/en/node/113110); [PER-3 arts. 5-6](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Billing validity | 336 hours, or fourteen times twenty-four hours from issue, under amended billing art. 5 | [PER-8/PJ/2026 art. I](https://pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-10pj2024-tentang-ketentuan) |
| Salary certificates | BPA1/BPA2 issued for the final tax period; provided within one month after that period ends | [PER-12 amended arts. 6-7](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan) |
| Record retention | Ten years in Indonesia for books, supporting records and electronic data | [KUP art. 28(11)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

### 1. Identify the applicable system and period

Keep the original legacy-service inventory, but distinguish a migrated function from a universally closed service. The legacy search names DJP Online e-Filing, desktop e-Faktur, e-Bupot 23/26, e-Bupot 4(2), PPh 15 tools, e-Bupot 21/26, e-Registration, e-Objection/e-Appeal, e-Billing, e-SKD and KSWP help locate old evidence. Their names do not prove a current route or the availability of a new Coretax module. A tax dispute or appeal still needs the correct authority/procedure, not an assumed portal button.

For tax periods beginning in 2025, use the current reporting framework and the taxpayer's permitted electronic channel. For December 2024 and earlier, preserve original legacy invoices, returns, slips, payment IDs and receipts, and establish the actual supported correction channel before lodgement. Do not copy an old form to the new system simply because the current calendar year is 2026. The old annual search names 1770/1770S/1770SS and 1771 are not a certified current field map. For 2025 annual returns filed in 2026 and 2026 returns filed in 2027, use the correct tax year's form, current instructions and available channel. [PER-3 arts. 2-8](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0); [PER-12 art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan).

Payment settlement remains distinct from return filing. A payment through an authorised receiving bank, Pos Indonesia or designated collection partner is not a filed return. Customs PIB/PEB and customs-system evidence (INSW/CEISA search names) remain distinct from a domestic tax invoice. BPJS is a separate contribution authority. Historical audit case files, residence certificates, refunds and taxpayer-status requests retain their own records and legal procedures.

The old billing cutover claim that no channel other than Coretax can issue any code is too broad. Amended billing art. 5 allows taxpayer creation or assistance through the taxpayer portal or integrated services. Confirm the actual current authorised channel; never enter credentials at an unverified third-party URL. [PER-8 art. I](https://pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-10pj2024-tentang-ketentuan).

### 2. Verify identity, activation and signing authority

DJP's identifier implementation distinguishes **resident individuals** using NIK, and non-resident individuals, entities and government institutions using sixteen-digit NPWP; NITKU identifies places of business. Citizenship alone is not the resident/non-resident test. Do not universally construct an identifier by prefixing a zero, or append a legacy three-digit branch suffix to make an assumed new identifier. Reconcile the actual DJP master record, current taxpayer identity and branch/NITKU. [DJP NIK, NPWP and NITKU implementation release](https://www.pajak.go.id/index.php/id/siaran-pers/peluncuran-layanan-perpajakan-berbasis-nik-sebagai-npwp-npwp-16-digit-dan-nitku).

The July 2024 release describes staged legacy support, so it does not prove that every DJP service stopped accepting every legacy format on that date. Treat an old fifteen-digit value as a legacy reference until the actual current mapping is established. The unsupported claim of an imminent dedicated foreign-national ID is not an operative rule.

The taxpayer or authorised representative opens the official portal, establishes whether account activation or a password reset is appropriate, and follows the current official process for registered email/phone and identity. A stale contact record requires an authorised update; preserve the official helpdesk/KPP route rather than inventing a compulsory in-person remedy for every error. Confirm legal name, tax status, address, activity and authorised responsible person. Do not promise that a KLU mismatch always prevents a serial request, because Coretax automatic serial assignment is a different process.

Invoice access requires an electronic certificate **or** authorisation code and invoice access under the relevant rule. Register the actual authorised signer's identity; multiple designated signers are permitted. Do not claim a certificate renewed within a fixed historical interval is necessarily valid today, that a passphrase must be entered for every action, or that every taxpayer needs the same certificate type. The actual validity and access state must be checked without sharing secrets. [PER-11 arts. 38,42](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

Keep preparation and signing roles separate. The old working labels Penanggung Jawab/PIC, Karyawan, Konsultan Pajak and Wakil Wajib Pajak indicate roles to reconcile with actual legal authority, not universal menu names. An operator's access alone is not permission to sign on an entity's behalf. Retain appointment/representation evidence; revoke departed-user access promptly and replace compromised credentials through the authorised process. The assistant never impersonates the taxpayer or signs, submits, pays or renews a certificate merely because it has read this method.

### 3. Choose the actual invoice channel

PER-11 art. 40 allows the taxpayer portal or a designated integrated application; PJAP providers have their own designation. For an eligible Coretax/integrated invoice, the serial is assigned on upload **and approval**. Remove the old Coretax steps requesting a quantity, waiting for a serial range, consuming a balance and returning unused numbers by a copied date. Those are not the current automatic-serial procedure. Do not back-date an invoice to disguise an access or approval problem. [PER-11 arts. 40-44](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

Desktop e-Faktur is a separate route, not a universally retired one. DJP's February 2025 announcement permits desktop from 12 February 2025 but excludes the listed transaction codes, PKPs centralising VAT at a branch and PKPs confirmed after 1 January 2025. It describes e-Nofa serial requests, desktop replacement, transmission into Coretax within at most H+2 and Coretax returns/cancellations/reporting. That historical announcement disproves the old absolute prohibition. **It does not certify that this particular taxpayer is eligible in November 2026 or that no subsequent change exists.** Verify a current channel entitlement before choosing desktop; keep its serial/request procedure separate from automatic Coretax serials. [DJP desktop announcement](https://www.pajak.go.id/index.php/id/pengumuman/pembuatan-faktur-pajak-melalui-aplikasi-e-faktur-client-desktop).

In that announcement code **06** covers specified other supplies including goods to individual foreign-passport holders, and code **07** is VAT not collected or government-borne. **07 is not a general zero-rated export-services code.** Do not select 01,04,06,07 or08 solely from a short legacy label. Establish actual domestic supply, special base, facility, retail/tourist or export treatment from the substantive VAT rule and current invoice annex. No current full code/annex mapping is certified here. [PER-11 arts. 33,36-37](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0); [DJP desktop announcement](https://www.pajak.go.id/index.php/id/pengumuman/pembuatan-faktur-pajak-melalui-aplikasi-e-faktur-client-desktop).

### 4. Prepare, validate, upload and preserve the invoice

Obtain the actual supply/advance/progress-payment date and create the invoice when required. A late invoice/approval issue is not cured by changing its true date. Confirm seller identity and actual customer type: domestic entity NPWP; resident individual NPWP/NIK; foreign individual passport; foreign entity name/address as prescribed. A foreign buyer is not automatically an export and a recipient-validation error does not justify entering a fictitious ID. [PER-11 arts. 31,33](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

Capture the goods/services, consideration, discounts, applicable legal VAT base, rate/regime, VAT and PPnBM if any. The ordinary PMK 131 mechanism is nominal twelve percent applied to eleven-twelfths of price for its specified non-luxury transactions, not a universal statutory eleven-percent rate. Separate luxury, separately regulated other-base/specific-amount supplies, export, exempt and not-collected transactions. A calculated portal total is a check, not a legal override. [PMK 131 arts. 2-5](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf).

The authorised signer reviews and signs the draft, uploads via the permitted channel, then confirms DJP approval and automatic numbering. Saving, exporting a PDF or receiving an upload acknowledgement is not the same as invoice approval. Check the legal upload/approval deadline separately from the tax point and VAT return deadline. A commercial invoice qualifies as an electronic tax invoice only when the prescribed content and timely upload/approval conditions are satisfied. [PER-11 arts. 33,38,43-45](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

For bulk work, download the current official template for the exact form/channel; map fields, test a small batch, reconcile count/base/tax before and after import, and preserve validation/rejection reports and IDs. Do not guarantee CSV or XML support or a minutes-long processing time without the current schema and actual result. Avoid duplicate upload through both portal and PJAP. The original CSV/Excel ledger recommendation survives as a workpaper format, not a guarantee that any spreadsheet is a valid import file.

### 5. Replace, cancel or return without creating duplicate tax

A QR/verification failure requires investigation of the official verification/approval record, data, network and issuer. Do not automatically reissue an invoice on a transient QR error or call it permanently uncreditable without establishing the legal defect. Obtain the approved original and correction history; never create two live invoices for one supply merely to bypass a scanner.

Replacement corrects wrong details **except buyer identity**, uses its actual new creation date and is reported in the original invoice's VAT period under the applicable rule. Wrong buyer identity requires cancellation and a new invoice with correct buyer information. Cancellation also covers genuinely cancelled transactions or invoices that should not have been made, with the actual supporting cancellation evidence. The old three-digit example `011` replacing `010` and an invented status position are not the seventeen-digit format. [PER-11 arts. 37,48-49](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

Keep a cancellation audit trail and source contract/cancellation documents. If an original has already been included by seller or buyer, each amends its affected return as required; an unreported cancelled invoice is not included as a live supply/input invoice. Do not keep a cancelled invoice as active output merely because its original number remains in the register. Replacement/cancellation is conditional on the ability to submit/amend the affected return. Retail invoices linked to a foreign-tourist VAT refund have their special restriction. [PER-11 arts. 49-50](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

For goods returned or services cancelled, obtain the actual return/cancellation note, supplier/customer identities, original invoice, quantities/value/tax and dates. A Nota Retur commonly originates with the buyer; its legal validity, tax-period effect and any applicable invoice replacement require the relevant rules, not an unexplained ledger credit. Where a replacement follows a return, preserve the linkage and recompute only the correct remaining supply; do not subtract both the original return and a replacement adjustment twice. Detailed current note format/timing remains unconfirmed here. [PER-11 art. 48](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

### 6. Prepare the correct withholding slips and monthly return

Keep employment PPh21/26 separate from the unified non-employment obligations. Current unified reporting covers the categories in PER-11, including relevant PPh4(2),15,22,23 and26; special government/industry collection procedures still need their exact rule. A withholding article is not chosen by which form is easiest. Services, non-land rent, royalties and non-bank interest require actual recipient and payer classification; distributions are not universally taxable dividends merely because paid to an individual. Construction, land/building rent, deposit interest, lottery prizes and qualifying UMKM may have separate final treatment. Shipping/aviation and other specific PPh15 regimes need their own supported computation. [PER-11 arts. 14-23](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

PER-11 provides standard **BPPU** domestic/permanent-establishment slips and **BPNR** non-resident slips. Preserve taxpayer/recipient identity, period, final/non-final nature, actual tax-object code, facility, base/rate/tax, supporting document, agent identity/NITKU, signer and signing date. Multiple same-recipient/same-object-code transactions in a period may be consolidated when the rule allows. Certain bank, securities, government-system or other prescribed transactions use an equivalent document instead; a statement may be evidence where the law permits, not an automatically invalid missing standard slip. [PER-11 arts. 17-19](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

No transaction and a transaction with nil withholding are different. The prescribed exemption, certificate, individual UMKM declaration, facility or treaty-zero cases can still require a slip. Obtain actual treaty entitlement, foreign tax identity and current residence-certificate/receipt requirements before applying treaty relief; a foreign payment does not mechanically mean twenty percent and a certificate alone does not establish all beneficial-owner/treaty conditions. Do not invent a document or override a missing material residence fact. [PER-11 arts. 20-21](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

Create and validate the draft slips, have the authorised person sign, preserve the issued versions and give the recipient the actual document. Do not assume automatic access in their account replaces the agent's delivery obligation. Reconcile original/replaced/cancelled slips and equivalent documents into the return, payment register and ledger. Under PER-11 arts.24-26, correction/additional/cancelled slips and a return amendment have conditions tied to examinations and the actual dispute/refund position; overpaid tax has the prescribed recovery route, not an invented universal next-month credit. [PER-11 arts. 24-26](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0).

For employment, the current certificate names are **BPA1** for the specified permanent/periodic-pension category, **BPA2** for the specified public-service category, **BP21** for other resident personnel payments and **BP26** for non-resident personnel payments. BPA1/2 cover the final tax period, including earlier actual cessation, and must be provided within one month after its end. BP21/26 are delivered whenever made under the permitted transaction/period process. The old 1721-A1/A2 names remain legacy search labels, not a separate annual employer return or certified current form. [PER-12 amended arts. 6-7](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan).

### 7. Generate a supported bill and reconcile state receipt

Reconcile the tax actually due by article, taxpayer, period and legal deposit category against prior valid deposits, collections, overpayments and corrections before generating any billing instruction. Confirm the current tax-account/deposit-code pair from the applicable official annex and actual obligation. Do not copy an old MAP/KJS pair, guessed receipt length or bank-reference string and call it a current payment instruction.

Under amended billing art.5 a code is valid for **336 hours from issue**. It ends unused at expiry; an unused/unexpired code can be cancelled under the rule, and a new code may be created after expiry/cancellation. Expiry of a code does not extend the legal payment deadline or erase the liability. No automatic payment is authorised here. Taxpayer/authorised payer settles through the actual permitted receiving channel and preserves the state receipt and NTPN/other applicable state-collection validation. A bank transfer reference or screenshot alone is not assumed to be a valid state receipt. [PER-8 art. I](https://pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-10pj2024-tentang-ketentuan).

The old tenth-day PPh payment rule is not the ordinary current deposit date. PMK 81 lists fifteenth-day deposits for the relevant PPh categories, with import/collector exceptions; VAT has its own end-of-month/before-filing rule. Check the actual holiday adjustment rather than adding an invented grace period. A billing-code validity window never overrides these legal dates. [PMK 81 arts.94-100](https://pajak.go.id/en/node/113110).

### 8. File through an eligible channel and keep the accepted receipt

PER-3 allows electronic submission through the taxpayer portal or an integrated designated service, with specified paper routes where permitted. A person obliged to file electronically who instead uses paper does not obtain a qualifying filing receipt by that substitution. Prefilled figures do not shift responsibility for a correct, complete, clear return. [PER-3 arts.2,7-8](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0).

The original Mobile/M-Pajak and offline Coretax Form topics remain useful channel checks, but their exact current supported taxpayer types, nil/non-nil status, forms, attachments and upload procedure are **Not yet confirmed** in this reading. Do not promise all individual taxpayers can file all 1770/1770S/1770SS forms on mobile, a particular February rollout date, Play/App Store availability or a universal offline/self-employed route. Use a current official module-specific instruction before recommending that path, and check the publisher before any app installation. PJAP host-to-host availability depends on designation and implemented taxpayer service, not merely a branded connector.

Reconcile every imported slip/invoice, VAT carried balance, deposit and annual attachment; sign through the authorised person's actual electronic process; submit only when instructed and qualified to do so. Preserve the accepted return, attachments, exact status/time and **Bukti Penerimaan Elektronik (BPE)** or applicable legal receipt. An upload acknowledgement, draft, payment NTPN and accepted-return receipt are different documents. Do not claim a reminder banner/email was delivered unless actually observed; a missing reminder does not change the deadline.

For annual extensions, a valid timely notification needs the prescribed provisional computation, statements and payment, with the correct authority evidence. PER-3 permits up to two months and has response/resubmission rules; do not treat an unanswered draft or an unfinished audit as an automatic extension. [PER-3 arts.5-6](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0).

### 9. Apply the current correction and compensation regime

PER-12 commences on **1 October 2026**, with transitional applicability to specified pending filings and corrections. Its signature/metadata date is not the commencement date. Determine which version governs the actual transaction and return. [PER-12 art.II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan).

For applicable VAT filings, normal returns are sequential subject to the express exception. Corrections account for actual earlier payments, refunds and decisions. Compensation adjustments use the prescribed next-not-yet-filed normal period and termination exceptions; do not automatically amend every intervening return or treat every negative correction as cash refunded. Legacy 2024 overpayments passed into January 2025 have their specific transition adjustment. [PER-12 amended arts.29A-29E](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan).

For applicable annual corrections, reconcile prior annual-balance payments and specified refunds/decisions. A corrected return can invalidate an earlier annual-balance instalment/deferral approval; use the current legal result, not the obsolete payment schedule. The latest correction governs within the actual rules, but filing a correction does **not** automatically stop an audit or refund examination already started. If an examination/open preliminary investigation or prior relief is involved, refer before submitting. [PER-12 amended arts.80A,129A-129B](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan).

### 10. Handle access failures and preserve evidence

Keep the original six implementation categories as diagnostic checks, not current universal platform facts: login/reset or stale contacts; desktop serial/e-Nofa versus Coretax upload/approval trouble; certificate/authorisation mismatch; PJAP latency or rejected imports; genuine identity-validation errors; slow rendering/high-volume returns. Historical January-March 2025 incidents do not prove an ongoing failure or a legal extension in November 2026.

Record URL, timestamp/timezone, taxpayer/period, action, exact status/error, rejected-record list, counts/base/tax, screenshot with secrets redacted, helpdesk/KPP ticket and the permitted recovery path. Retry safely after establishing whether the first upload, payment or submission succeeded. Never assume no response means nothing was filed, and never pay the same liability twice merely because a receipt is delayed.

Document-and-retry does not itself excuse lateness. Check an actual DJP announcement/decision for period, taxpayer group, covered obligation and relief conditions. Continue supported work, use a lawful alternative where available and preserve an explanation, but do not self-declare force majeure or a blanket waiver. A 2025-return relief decision expiring in April 2026 is not a 2026 tax-year extension.

## Worked cases

### Case 1. Commercial price is not ordinary VAT base

Assume a PKP makes a qualifying ordinary non-luxury domestic taxable supply with commercial price IDR 12,000,000 excluding VAT. PMK 131's specified eleven-twelfths base gives DPP11,000,000; nominal twelve percent produces VAT1,320,000; the invoice total is13,320,000. A worksheet treating the price as full DPP and applying twelve percent would overstate tax by120,000. Confirm actual classification; this mechanism does not apply to every special-base, luxury, export or exempt supply. Approval/numbering and the tax point remain separate checks. [PMK 131 art.3](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf).

```oa-check
name: Ordinary invoice price to legal base
inputs:
  commercial_price: 12000000
  base_numerator: 11
  base_denominator: 12
  nominal_rate: 0.12
steps:
  - vat_base: commercial_price * base_numerator / base_denominator
  - vat: vat_base * nominal_rate
  - invoice_total: commercial_price + vat
  - wrong_vat: commercial_price * nominal_rate
  - overstatement: wrong_vat - vat
expected:
  vat_base: 11000000
  vat: 1320000
  invoice_total: 13320000
  wrong_vat: 1440000
  overstatement: 120000
```

### Case 2. A correction is not a second full payment

Assume a permitted ordinary return correction has supported final tax due IDR 3,000,000, an earlier valid deposit IDR 2,000,000 and no refund/other adjustment. Reconcile the prior deposit, leaving1,000,000 additional tax. Paying3,000,000 again would create total deposits5,000,000 and an excess2,000,000, not discharge a second liability. The exact return/category recovery procedure still governs; this is not automatic permission to net an unrelated tax or refund. A newly created code's fourteen-day validity is336hours, not a new payment deadline. [PER-11 arts.22,25-26](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0); [PER-8 art.I](https://pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-10pj2024-tentang-ketentuan).

```oa-check
name: Correction payment and billing duration
inputs:
  corrected_due: 3000000
  prior_valid_payment: 2000000
  hours_per_day: 24
  billing_days: 14
steps:
  - remaining_due: corrected_due - prior_valid_payment
  - duplicate_total: prior_valid_payment + corrected_due
  - duplicate_excess: duplicate_total - corrected_due
  - validity_hours: billing_days * hours_per_day
expected:
  remaining_due: 1000000
  duplicate_total: 5000000
  duplicate_excess: 2000000
  validity_hours: 336
```

## When to refuse or refer

- **R-CT-1, substantive tax missing:** keep PPN, PPh21, ordinary income and planning in the relevant supported method; no guessed rate, code or tax total to satisfy a form.
- **R-CT-2, foreign/identity onboarding:** resolve actual residence and official identifier mapping; do not fabricate a padded legacy number, NIK or passport.
- **R-CT-3, historical amendments:** determine the supported pre-2025 route before a correction; no universal Coretax migration claim.
- **R-CT-4, PJAP integration:** implementation/debugging, private credentials and API registration are engineering/authorised-operator work; preserve the tax requirements and refer.
- **R-CT-5, outage relief:** no self-declared waiver; actual official period-specific relief and evidence are required.
- **R-CT-6, certificate/credential operations:** the authorised user handles activation, renewal and signing secrets. Never request or reuse a taxpayer passphrase across unrelated users.
- Wrong buyer, duplicate invoice/payment, closed correction window, pending audit/dispute/refund, unclear treaty/certificate or unknown current template: stop the affected final action, preserve the draft/evidence and refer the precise issue.

### Final self-check and output

Retain a workflow register with taxpayer/period, current legal/channel basis, source computation, identity/authority, original and corrected document IDs, invoice approval, relevant code/template version, validation reports, deposits/state receipt, return/attachments, accepted receipt, unresolved facts and outage history. Deliver a ready-to-review draft and specific taxpayer/authorised-filer action list, never an invented successful filing. Check identity/period; PKP/current channel; actual access/signature; correct transaction/article; treaty/facility evidence; duplicates and correction links; ledger-to-form counts/base/tax; prior deposits; legal payment/filing dates; BPE; and record retention. Coretax automatic serials do not require a fictitious NSFP balance check.

## Sources

All following official bodies were read on **2026-11-14**, for the stated portions only. No portal credentials, taxpayer activation, filing or payment were used.

- Read 2026-11-14: [DJP consolidated KUP, Income Tax and VAT laws](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf): KUP art.3 deadlines, art.28 retention and VAT art.15A distinct VAT deadline; not a certification of every administrative/criminal sanction.
- Read 2026-11-14: [PMK 81/2024 actual operative text](https://pajak.go.id/en/node/113110): arts.94-100 payments/holiday and annual balance; other platform modules are not certified by their names alone. Read alongside the cached actual PMK1/2026 amendment inventory for the affected provisions.
- Read 2026-11-14: [PER-11/PJ/2025 operative reporting text](https://www.pajak.go.id/id/peraturan/ketentuan-pelaporan-pajak-penghasilan-pajak-pertambahan-nilai-pajak-penjualan-atas-0): arts.14-26 unified slips/returns/corrections, arts.30-45 invoice content/point/numbering/signature/approval and arts.48-50 replacement/cancellation. The full annex/code catalogue was not certified.
- Read 2026-11-14: [PER-12/PJ/2026 actual operative amendment](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan): amended arts.6-7 employment certificates,29A-29E VAT sequence/compensation,80A and129A-129B corrections and art.II commencement/transition. A JDIH metadata attachment with a different PER-11/2026 printer-designation heading was rejected; this linked operative text is the relevant law.
- Read 2026-11-14: [PER-3/PJ/2026](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0): arts.2-8 return content, deadlines, extensions and permitted electronic/paper channels; no invented current mobile/offline eligibility.
- Read 2026-11-14: [PER-8/PJ/2026](https://pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-10pj2024-tentang-ketentuan): amended billing art.5, creation,336-hour validity and cancellation/replacement; not a general payment extension.
- Read 2026-11-14: [DJP desktop e-Faktur announcement](https://www.pajak.go.id/index.php/id/pengumuman/pembuatan-faktur-pajak-melalui-aplikasi-e-faktur-client-desktop): February2025 eligibility exclusions, three channels, e-Nofa and desktop correction/transfer process; historical evidence, not certification of every taxpayer's current channel.
- Read 2026-11-14: [DJP NIK/NPWP/NITKU implementation release](https://www.pajak.go.id/index.php/id/siaran-pers/peluncuran-layanan-perpajakan-berbasis-nik-sebagai-npwp-npwp-16-digit-dan-nitku): resident-individual identity, non-resident/entity/government sixteen-digit NPWP and business-place identifier; not the false citizenship-only mapping.
- Read 2026-11-14: [PMK 131/2024](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf): arts.2-5 ordinary eleven-twelfths base, luxury distinction and separately regulated exceptions for the worked invoice.

Not yet confirmed: current taxpayer-specific desktop eligibility and any later channel decision; exact live menu names, app publisher/build and Mobile/M-Pajak/Coretax Form eligibility; current bulk-import schema and complete object/transaction/deposit-code annex; detailed return/cancellation-note format/timing; actual taxpayer identity/activation/signature state; supported pre-2025 correction route for each form; period-specific deadline relief and actual payment-interest rate. Obtain the named official module/annex/decision or actual taxpayer record before issuing the affected filing instruction. No unknown is replaced by a guessed historical button, expiry or tax code.

### Change and preservation record

Version2.0 replaces the conflicting generated-facts block and obsolete portal walkthrough with current operative rules and a document-first workflow. The original quick reference, entity/identity intake, six refusals, legacy-service inventory, activation/roles, invoice serial/issuance/QR/replacement/cancellation/return/bulk topics, Unifikasi scope/slips, employment separation, four filing-channel topics, deadline/receipt checks, six historical implementation categories, cutover, outage handling, retained documents and final checklist are retained above. Removed instructions were wrong or unverified: desktop retired; Coretax serial requests/pool/annual return;07 as export; citizenship-only/fifteen-digit identity; ten-day deposit; automatic QR reissue; obsolete three-digit replacement example; blanket app/form availability; guaranteed template types/latency/reminders; fixed certificate-renewal interval; guessed module names. Legacy statutes and form names are history, not the applicable current procedural authority.

## Prohibitions

Never back-date, duplicate an invoice/payment, invent an identifier/tax code, claim a saved draft is approved/filed, use a desktop route without establishing eligibility, select a withholding article for convenience, self-declare relief, share signing secrets, or present this platform method as a substitute for the substantive tax calculation.

## Disclaimer

Provided for informational purposes only; not tax, legal, or financial advice. Open Accountants and its contributors accept no liability. Coretax behaviour, URLs, and procedures may change without notice; cross-check against the latest DJP Pengumuman on pajak.go.id. All outputs must be reviewed by a qualified Konsultan Pajak before lodgement.

The most up-to-date version is maintained at openaccountants.com.
