---
name: id-return-assembly
description: >
  Assemble an Indonesian calendar-2026 annual-return working paper from
  documented bookkeeping, ordinary/final income-tax, payroll, VAT and withholding
  outputs. Reconcile credits, payments and reporting before producing a workbook,
  reviewer brief and taxpayer action list. Trigger on SPT Tahunan, annual return,
  Coretax filing package, prepare SPT 1770 or 1771 and Indonesian return assembly.
  Never submit a return or load the US Idaho id-income-tax skill for Indonesia.
jurisdiction: ID
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: "2.0"
category: international
type: filing-howto
---

# Indonesia Annual Return Assembly v2.0

## Scope

Prepare a calendar-2026 Indonesian resident individual's or ordinary resident entity's annual-return package. Consume intake and calculation outputs, reconcile them and produce a master workbook, reviewer brief and taxpayer action list. This method is a capstone, not a substitute for missing tax computations and not a permission to file, pay, activate an account or post a ledger. The original required review and taxpayer/authorised-filer submission remain in place.

The old individual forms 1770/1770S/1770SS and corporate 1771 remain useful historical search names. Their copied line numbers and attachment labels are not a certified 2026 Coretax field map. Use the actual current annual form and its attachments under the applicable reporting rules before making a filing-ready mapping. For tax year 2025 onward, distinguish the original PER-11/2025 forms, current submission/receipt rules in PER-3/2026 and the applicable PER-12/2026 correction regime. [PER-3/PJ/2026 arts. 2-8](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0); [PER-12/PJ/2026 art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan).

This ordinary route excludes non-residents, mixed-residence/treaty years, permanent-establishment branch-profits tax, banking/insurance, oil/gas/mining contracts, controlled foreign companies, specialist expatriate facilities, consolidated/group computations, tax holidays, KEK/free-zone facilities and VAT margin/refund special regimes. Keep those income/credit rows in the data inventory, label the missing specialist computation and refer; never drop the underlying receipt from the return package merely because its tax is out of scope.

## Ask the client first

Read all existing intake and upstream evidence first. Do not repeat questions already answered or ask whether to assemble the package when the user requested a return. Collect only a missing fact, document or reconciliation explanation. Required identity/period data are taxpayer legal type/name, residence/subjection period, NPWP/NIK mapping, actual NITKU/location where relevant, KLU and activity, KPP, accounting year, family/PTKP status and signer/authority. Never substitute a default consulting or holding-company code for a missing activity code. A missing identifier produces a labelled placeholder in the draft and blocks a filing-ready claim, not all useful reconciliation work.

### Upstream packages and their destinations

| Package | Consume | Working-paper destination |
|---|---|---|
| `id-bookkeeping` | Trial balance, income/cost records, financial statements, fixed assets, NPPN notice/classification and supporting gross/net evidence | Commercial accounts, business/professional income, fiscal reconciliation and asset/liability evidence |
| Indonesian ordinary individual computation | Separately documented ordinary net-income, permitted loss, PTKP, PKP, progressive tax and foreign-credit calculation | Ordinary individual tax calculation and credit schedule; a missing computation is an explicit gap |
| `id-corporate-tax` | Commercial-to-fiscal bridge, losses by year, Article 31E/other lawful rate and instalment basis | Ordinary company tax, fiscal adjustment, losses and next-year instalment schedules |
| `id-pph-final-umkm` | Eligibility, actual activity, connected-taxpayer ceiling, election/transition history, monthly turnover, individual relief and final deposits/collections | Final-income schedule, monthly reconciliation and following-year regime decision |
| `id-payroll-pph21` | Employment gross/net and final-period withholding evidence as recipient; payroll costs and obligations as employer | Individual employment income/credit schedule OR employer expense/agent compliance, never the same tax credit twice |
| `indonesia-vat` | Monthly output/input, exempt/non-taxable/export supplies, actual invoice bases, payment/collection and compensation history | Separate VAT reconciliation and revenue bridge; only supported non-recoverable costs affect income-tax profit |
| `id-withholding` | Recipient slips and separately agent returns, payee evidence and payment register | Eligible own non-final credit register, final-income settlement and separate agent-compliance schedule |
| `id-einvoice-coretax` | Applicable return/certificate/invoice process, billing and accepted-return evidence | Ready-to-file checklist, unresolved portal fields and payment/filing evidence |

**Routing safeguard:** `id-income-tax` is a US Idaho skill in this repository. Never load it for Indonesia. There is no verified Indonesian companion with that slug. If an ordinary individual computation is absent, name that gap and obtain a computation under Indonesian law, rather than substituting another jurisdiction. The protected accountant-approved `id-withholding` is not rewritten here; its old deposit-day, VAT and UMKM statements must not override the current primary rules below.

### Document packet

For individuals collect business/professional income by method, employment slips, domestic non-final withholding, permitted foreign credits, final/exempt income, assets at year end, liabilities, family members, loss/instalment evidence and any separate-spouse computation. For entities collect management/statutory accounts and audit report only where required, fiscal reconciliation, costs, depreciation/amortisation, losses, shareholdings, owners/directors/commissioners, connected-party investments/loans/transactions and TP disclosures. An absent prior return may be legitimate for a new entity; obtain registration evidence and use its correct instalment category instead of fabricating a prior-year basis.

## The method, step by step

## Rates, bands and thresholds

| Item | Supported rule and limits | Official source |
|---|---|---|
| Individual annual deadline | Three months after tax-year/part-year end; calendar 2026 ordinarily 31 March 2027 | [KUP art. 3(3)(b); PER-3 art. 4](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PER-3](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Entity annual deadline | Four months after tax-year/part-year end; calendar 2026 ordinarily 30 April 2027 | [KUP art. 3(3)(c); PER-3 art. 4](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PER-3](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Annual extension | Up to two months by timely valid notification with the required provisional computation, statements and payment evidence, not an automatic payment deferral | [KUP art. 3(4)-(5)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PER-3 arts. 5-6](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Ordinary monthly income-tax deposit | Fifteenth of following month for the listed PPh categories, with stated exceptions and actual holiday adjustment | [PMK 81 arts. 94 and 100](https://pajak.go.id/en/node/113110) |
| Ordinary monthly withholding return | Twenty days after period end, with applicable specific/exception rules | [KUP art. 3(3)(a)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Monthly VAT balance | End of following month and before return submission, with its own applicable holiday/period rule | [PMK 81 art. 94(3)(e)-(f)](https://pajak.go.id/en/node/113110) |
| Final turnover tax | 0.5% qualifying monthly gross; individual annual untaxed portion IDR 500,000,000, no company allowance | [PP 55 art. 60](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PMK 164 art. 6](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau) |
| Final-tax ceiling | IDR 4,800,000,000 under the actual eligibility and connected-taxpayer test; current-year crossing and permanent-exit rules differ | [PP 20 amended arts. 57-58](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [PP 55 art. 61](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan) |
| Ordinary company rate | 22%; Article 31E fifty-percent rate reduction relates to income PROPORTIONAL to qualifying turnover, not an untaxed or low-rate first slice of profit | [Income Tax Law arts. 17,31E](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Article 31E boundaries | Turnover at most IDR 50,000,000,000; first IDR 4,800,000,000 of turnover determines the proportional eligible income | [Income Tax Law art. 31E](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Ordinary loss carryforward | Five consecutive following tax years, with separate granted extensions if applicable | [Income Tax Law art. 6(2)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Late annual return fine | Individual IDR 100,000; entity IDR 1,000,000, subject to statutory exceptions and period-specific relief | [KUP art. 7](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Late-payment interest | Actual ministerial monthly rate, at most twenty-four months where art. 9 applies, part-month in full; no fixed percentage or daily proration | [KUP art. 9(2a)-(2c)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Records | Ten years in Indonesia for books, records and supporting electronic data | [KUP art. 28(11)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

### 1. Build the status and evidence register

Each upstream output receives taxpayer, period, currency, preparation date, source/method version, confirmed facts, assumptions, missing facts and reviewer status. Identify whether an output is original, replacement or amended. A prefill is a starting point, not proof of completeness. Keep blank values distinct from nil, unavailable documents distinct from no transaction, and an unverified credit distinct from an invalid credit. Maintain copies and document IDs for every return, slip, state receipt, assessment, compensation/refund and extension used.

Do not silently absorb a failed upstream check or invent its missing calculation. Continue assembling supported sections and produce a gap list. A balance or filing-ready statement dependent on an unresolved material fact stays blocked until resolved, even if the workbook can be built. This preserves the original run-through workflow while correcting its instruction to treat every failed check as merely advisory.

### 2. Reconcile revenue across books, VAT and each income-tax base

Start from total commercial income and bridge by actual income category, entity, cash/accrual timing, advances, foreign exchange, returns/discounts, exemptions, final/non-final separation, branches and related-party flows. VAT annual DPP is not automatically annual bookkeeping turnover. Under the ordinary PMK 131 method the VAT base can be eleven-twelfths of actual price; special bases/rates and exports create further differences. Reconcile to commercial selling price before comparing the totals. [PMK 131 arts. 2-4](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf).

Final-tax monthly gross is received or accrued qualifying business turnover before discounts, with its own statutory exclusions and individual untaxed portion. The eligibility ceiling uses the wider business/professional and connected-taxpayer test. Do not equate the ceiling, the final-tax base, general-rate gross income and VAT DPP. Construction/final rental and other separately taxed items stay in their own schedules, with supporting classification. Intra-group movements are not automatically eliminable in a resident company's separate return. [PP 55 arts. 60-61](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PP 20 amended arts. 56-58](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

Record every variance and its documentary reason. The old IDR 1,000/100,000 bands were internal workflow thresholds, not a legal rounding allowance. A reviewer may set operational triage levels, but no unexplained difference is silently written off and a material unresolved variance blocks a filing-ready total. Preserve actual required form rounding separately from reconciliation errors.

### 3. Reconcile the taxpayer's own credits and annual balance

Create separate columns for tax due, eligible own non-final PPh 21/22/23, permitted art. 24 foreign credit, own PPh 25 instalments, final income/settlement, and tax deducted by the taxpayer as an agent from someone else's income. A resident company does not claim employee PPh 21 as its own corporate credit. Withholding/remittance on a supplier payment is an agent liability, not the company's own credit. PPh 26 credits have limited statutory exceptions and need separate legal analysis; do not add them universally to resident-company credits. [Income Tax Law arts. 21-26](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

Reconcile each own credit to a valid slip, taxpayer, income, year/period and prefill/confirmation. A recipient should not automatically lose a valid credit merely because the withholding agent's own NTPN was not supplied to them. Investigate the actual evidence rule and missing slip; leave a provisional credit visibly pending rather than permanently disallow it or invent a receipt. Self-paid instalments and annual balances require the payer's own state-receipt evidence. Foreign credits need actual income/category/country, tax evidence and the permitted cap; absence of a certificate of residence alone does not establish universal denial. The detailed foreign-credit computation is upstream specialist work.

Annual ordinary balance = ordinary tax liability minus lawful own non-final credits and own instalments. Final turnover tax is not another ordinary credit. If credits exceed liability, show the supported negative balance and apply the lawful overpayment/refund process; do not cap credits at tax liability to conceal the excess. Do not promise a refund or automatically carry it forward without the proper return and procedure. Preserve final and exempt income disclosure separately.

### 4. Reconcile final turnover tax and its transitions

Use the monthly tracker, cumulative individual allowance, certificate/turnover statements, final-tax slips and actual self-deposits. Do not demand a self-deposit for tax already validly collected by a customer, and do not require 0.5% of ALL individual annual turnover when the untaxed portion applies. A company does not borrow the individual's allowance. Reconcile a tax-not-due refund request separately from ordinary credits. [PP 55 arts. 60,62-63](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PMK 164 arts. 6-9](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

A taxpayer whose current-year turnover exceeds the ordinary ceiling can continue the statutory final treatment through the crossing year under art. 61, then apply the following-year rule. It does not switch to progressive/corporate tax in the next month merely because the ceiling was crossed. Apply the new owner/company aggregation, permanent election/exit and exact art. II transitions separately. [PP 55 art. 61](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PP 20 amended arts. 57-59 and art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

The old annual package's universal PT-three/CV-four/individual-seven-year grid is not a 2026 eligibility rule. Article 59 is deleted; qualifying individuals and single-founder companies have the amended general rule, cooperatives have the stated period and historical transition, and ordinary PT/CV/firma/BUMDes retain only the exact earlier entitlement allowed by art. II. Preserve registration, initial clock, earlier notices and certificate history. Do not treat unknown history as the final eligible year, manufacture a new election or prescribe automatic bookkeeping without checking possible NPPN eligibility. The complete calculation/transition analysis belongs to `id-pph-final-umkm`.

### 5. Reconcile employment and employer obligations

As an employee, reconcile employment gross, permitted deductions, final-period liability, earlier TER withholding, any employee refund and the actual employer-issued annual/final-period certificate. As employer, reconcile payroll expense, taxable benefits, contribution liabilities, employee withholding, monthly returns, tax receipts and certificates issued. Include the last employment period's true-up, which may be earlier than December; do not insist that every employee stayed to year end. [PMK 168 arts. 5-10,15,20-22](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1).

An annual salary-withholding certificate, historically called 1721-A1/A2, is not a separate annual employer tax return due on the individual's annual deadline. Do not instruct the employer to file a new March annual return based solely on that slip name. Current PER-12 amended arts. 6-7 name BPA1 for the specified permanent/periodic-pension employees and BPA2 for the specified public-service category; these final-period certificates are provided within one month after the final period ends. BP21 and BP26 cover other resident and non-resident personnel payments and are delivered whenever made under the prescribed transaction/period process. [PER-12 arts. 6-7](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan). Withholding from consultants/non-employees and non-residents is classified separately, not slipped into employee wages or a resident company's own credit.

### 6. Reconcile the business as a withholding agent

For wages, professional fees, service/royalty/interest payments, rentals, construction and non-resident payments, obtain actual contract, payer status, recipient/category/residence, gross/base/VAT components, tax point, treaty or certificate where relevant, tax withheld, slip issued, deposit and monthly return. Keep PPh 21/26 personnel returns distinct from PPh Unifikasi and any special collection rule. Do not assume every individual payer is a withholding agent or every consultant is subject to supplier-company PPh 23.

Missing withholding is a compliance issue, but the remedy, payment and sanction depend on its actual legal provision and period. The old fixed two-percent monthly interest instruction is not current art. 9 guidance. Use the current deposit and applicable correction rule and compute interest from the official ministerial rate if required. Do not file or pay automatically. [PMK 168 arts. 2,19-22](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1); [PMK 81 arts. 94 and 100](https://pajak.go.id/en/node/113110); [KUP art. 9](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

### 7. Reconcile VAT and fiscal costs without double claims

Reconcile each period's output tax, creditable input, non-creditable input, imports, foreign services/PMSE evidence, government/other collector evidence, advances, exports, exempt/non-taxable supplies and prior compensation. A credited input tax is not also an expense or asset cost. Non-recoverable input is considered for cost/capitalisation under the underlying income-tax/business-purpose rules; it is not universally deductible merely because VAT credit was unavailable. Capital goods follow their actual credit/cost treatment and depreciation. Final-tax or exempt-income expenses must not automatically shelter ordinary taxable income. Keep the original P&L-to-VAT and asset checks; obtain the correct source and explanation where a difference exists.

For corrections submitted from 1 October 2026, apply PER-12's amended rules to the tax periods/years it covers. VAT corrections account for prior deposits/refunds and adjust compensation balances; the next unfiled normal period may receive a positive or negative adjustment. Do not force every intervening month to be amended or pay a second time merely because a replacement return shows the full liability. Distinguish earlier pending filings covered by the transition and legacy periods. [PER-12 amended arts. 29A-29E and art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan).

### 8. Assemble the individual ordinary and final schedules

The workbook preserves the old working-paper components without pretending they are current form line numbers:

| Working schedule | Components retained and checks |
|---|---|
| Identity/period | Taxpayer, actual residence/subjection year, legal type, NPWP/NIK, relevant location/NITKU, actual KLU, address, family/PTKP and signer [Filing framework; current field mapping not yet confirmed](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Ordinary net-income bridge | Business net profit OR permitted NPPN result; professional net income; employment net income; other ordinary domestic income; foreign net income and underlying documents [Filing framework; current field mapping not yet confirmed](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Taxable-income bridge | Supported income aggregation, permissible loss/adjustment, applicable PTKP, zero floor and statutory rounding, then the documented progressive computation [Filing framework; current field mapping not yet confirmed](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Own credit register | PPh 21/22/23 and allowed foreign credit, taxpayer/year/slip, actual own instalments and annual balance; final withholding separate [Filing framework; current field mapping not yet confirmed](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Final and exempt income | Qualifying final-business receipts, specific rental/construction/interest/dividend/gain treatment and actual exemption evidence, not universal copied passive-income rates [Filing framework; current field mapping not yet confirmed](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Assets and liabilities | Year-end assets/debts and their documentary/cash-flow bridge, including changes and ownership/location, not only balances visible in the bank [Filing framework; current field mapping not yet confirmed](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Family/spouse | Family members, actual dependant support and joint/separate spouse treatment with necessary supporting computation [Filing framework; current field mapping not yet confirmed](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |
| Following-year instalments | Actual ordinary/special taxpayer basis and effective period; do not subtract own instalments again [Filing framework; current field mapping not yet confirmed](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) |


Old labels such as Lampiran I-IV/V and 1770 Induk Parts A-G are preserved only in the source-to-destination record. The old precise ordering/line numbers and 60-million salaried-form shortcut are retired as current instructions because the actual 2026 form map was not read. Pick the applicable current return from its official instructions and map each verified component before sign-off. Do not drop an asset, final receipt or family disclosure because the old form label changed. [PER-3 arts. 2-8](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0).

### 9. Assemble the entity ordinary and final schedules

The company workbook preserves commercial turnover, COGS, gross profit, operating/other costs, commercial profit, positive/negative fiscal adjustments, net fiscal income, year-by-year losses, PKP, applicable ordinary/facility tax, lawful credits, instalments and annual balance. Article 31E is a turnover-proportional reduction, not eleven percent on the first IDR 4.8 billion of profit. A listed-company reduction or incentive needs its separately supported interaction/grant; do not stack an old recipe by default. [Income Tax Law arts. 6,9,17,25,31E](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

Keep schedules for COGS/cost details, domestic-credit evidence, final/exempt income, shareholders/owners and directors/commissioners, investments in affiliates, related-party loans/transactions, assets/depreciation/amortisation, losses and applicable TP summaries. An audit report attaches only where legally required; management statements are not automatically unacceptable. The old 1771-I through VI and special 1A/1B/2A/3A references are historical component names, not a certified 2026 Coretax map. Keep the actual effective form and source beside the final mapping.

Final-tax company income goes to the final schedule, not ordinary PKP and not an ordinary credit. Use the company's actual PP 20 transition and no individual's untaxed-turnover allowance. Employment tax paid as employer is its own liability/expense issue, not its own PPh 21 tax credit. Do not claim PPh 26 paid to a supplier as a resident-company credit without a specific applicable exception.

### 10. Prepare billing/payment instructions from confirmed current codes

Prepare a draft payment schedule, not a live billing code. Record taxpayer, actual tax article, payment type, period/year, original/correction/assessment reference, amount and source. The original MAP catalogue retained these historical mappings: 411125 individual PPh 25/29, 411126 entity PPh 25/29, 411128 final income tax, 411121 PPh 21, 411124 PPh 23, 411127 PPh 26, 411122 PPh 22, 411211 domestic VAT and 411221 import VAT. The earlier KJS 100/monthly and 200/annual examples and fifteen-digit code description are historical, not validated current pairings. **Not yet confirmed:** the exact applicable 2026 KAP/MAP-KJS combinations, current billing-code length and each portal field for this transaction. Do not generate a code or prescribe a thirty-day expiry from that old catalogue. Amended billing art. 5 provides 336 hours, or fourteen times twenty-four hours from issue; this does not extend the legal payment deadline. [PER-8/PJ/2026](https://pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-10pj2024-tentang-ketentuan).

The authorised filer selects the correct obligation/current combination, generates or uses the valid bill through the supported channel, checks payee/state destination and amount, pays once and retains the BPN/NTPN/equivalent state receipt plus ledger allocation. A bank debit or marketplace receipt alone is not the state-payment identifier. Prevent duplication when a customer/collector already settled tax. Confirm the actual receipt and the correct liability/year/period rather than assume every payment automatically becomes a credit in the next return. Current payment-code detail belongs to `id-einvoice-coretax` and the official operative annex used for the actual transaction.

For an annual underpayment, settlement is before submission and not beyond the applicable deadline, subject to any lawful extension/payment arrangement. For monthly obligations use their own payment/filing rules. VAT and import collections can differ from ordinary PPh deposits. A recipient withholding credit does not universally require that recipient to possess the agent's NTPN. Keep those distinct. [PMK 81 arts. 94-100](https://pajak.go.id/en/node/113110).

### 11. Prepare submission and receipt evidence

The taxpayer or authorised filer checks current account/signer authority, correct period and original/corrected status, current form, supported portal/integrated application, and actual required attachments. Assemble employment/other slips, financial statements where required, any required audit report, losses/fixed-asset/TP disclosures and statutory statements. Do not advertise every old form on a generic mobile/XML/offline channel or promise an unconfirmed current upload schema. PER-3 permits current electronic/integrated channels and has distinct paper rules; a taxpayer required to file electronically does not meet the obligation by an unauthorised paper substitute. [PER-3 arts. 7-8](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0).

Run the return's schema and arithmetic validation, resolve substantive blockers, have the original professional review completed, then the authorised person submits. Retain the actual accepted receipt, timestamp, return version and all attachments. A saved draft, invoice, tax bill, payment receipt or generic upload-success message is not an accepted annual return. Do not hard-code the old nineteen-digit BPE number claim as a validation rule. Save the actual evidence required by the current channel and check acceptance/status rather than inventing success.

Extensions require the actual timely notification, provisional computation/statements, relevant payment and authority evidence. A PDF named extension is not proof that the requested period was accepted. Track original due date, valid extended due date, provisional/full liability and any interest separately. [PER-3 arts. 5-6](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0).

For an annual correction in PER-12's scope, account for prior PPh 29 payments and specified refunds/decisions before determining a further balance. The latest accepted correction governs under art. 129A; art. 129B has a specific consequence for an earlier annual payment-instalment/deferral decision. Preserve every earlier return, receipt, refund and decision, and refer where an audit/investigation limits correction. Do not prepare an extra annual payment simply by comparing the corrected return's full tax to zero. [PER-12 amended arts. 80A,129A-129B and art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan).

### 12. Prepare following-year planning without changing the return

Ordinary PPh 25 uses prior liability less the eligible withholding/foreign credits, not less prior PPh 25 again. The number of applicable year/part-year months and actual filing/extension/correction date matter; it does not universally start in January or May on a newly invented basis. Carry forward the final preceding-year instalment where art. 25(2) applies. Ordinary new taxpayers, periodic-statement entities, OPPT and mergers/splits/conversions have separate PMK 81 arts. 226-237 rules; first ordinary-rate years after final tax also need PMK 164 art. 16. [Income Tax Law art. 25](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 81](https://pajak.go.id/en/node/113110); [PMK 164](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

Re-evaluate final-tax eligibility/elections, connected turnover, cooperative/legacy transition and permanent exclusion from the actual amended law. Consider NPPN notice and bookkeeping duties separately. Reconcile VAT status and registration/effective period under PMK 164 independently of the income-tax choice; it is not always registration before crossing or an immediate VAT-start rule. Keep a dated action list and identify any rule not yet published for the future period.

For related-party work, PMK 172 art. 16 master/local thresholds use preceding-year gross turnover and related-party categories, plus the lower-tax-jurisdiction trigger; being below the thresholds does not remove arm's-length duties. Domestic-parent CbCR uses an inclusive consolidated threshold. Files' availability, summaries, notification and submission are distinct. Use `id-corporate-tax` and the actual source, not PMK 213/2016 copied deadlines. Master/local files are available within four months, CbCR within twelve; art. 19 treats annual-return summaries/reporting separately. A cash transfer to an affiliate is not exempt just because no documentation threshold is met. [PMK 172 arts. 16-19](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan).

## Boundary and exception table

| Retained refusal/check | Action and completion condition |
|---|---|
| R-ID-ASM-1: upstream method missing | Name the missing method/computation, continue supported sections, do not invent a result or load Idaho |
| R-ID-ASM-2: upstream self-check failed | Preserve the exact failure and dependent schedules; block a filing-ready claim if the tax result is unresolved |
| R-ID-ASM-3: reconciliation discrepancy | Document every difference and evidence; internal triage thresholds never authorise an unexplained write-off |
| R-ID-ASM-4: special VAT, extractive contracts, BUT, CFC, tax holiday or KEK | Preserve the data and named specialist gap; no unsupported special computation |
| R-ID-ASM-5: non-resident, part-year or expatriate-special/treaty facts | Refer the actual residence/source/period computation; no full-year assumptions silently imposed |
| R-ID-ASM-6: identifier or intake fact missing | Label draft fields; no invented KLU/NITKU/NPWP, family status or filing-ready completion |
| R-ID-ASM-7: asked to submit | Produce instructions and workpapers only; submission belongs to the taxpayer/authorised filer after required review |
| Missing slip, receipt or credit cap evidence | Keep provisional claim and document request separate from a legally invalid claim; no automatic confiscation of supported excess credits |
| Unclear audit requirement | Obtain actual legal category/threshold and financials; do not make every company audit or invent a current threshold |
| Missing current form/code | Continue conceptual schedule assembly, but hold field mapping/payment instructions until official period-specific confirmation |

## Worked cases

### Case 1. Final individual turnover is not an ordinary-income tax credit

Assume the upstream final-tax method has established full eligibility, no opt-out, individual turnover IDR 1,200,000,000 evenly over the year and the annual untaxed portion IDR 500,000,000. Its computed final tax is 3,500,000. Actual final amounts are 1,000,000 collected by customers and 2,500,000 self-deposited, so final settlement reconciles with no extra payment. Separately the supplied ordinary employment/professional computation has tax 29,550,000 and lawful ordinary credits 20,000,000, leaving 9,550,000; subtracting final tax again would wrongly show 6,050,000. These are upstream supported case inputs, not proof that any unclassified worker qualifies for final business tax. [PP 55 art. 60](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PMK 164 arts. 6-9](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

```oa-check
name: Separate final settlement from ordinary annual credits
inputs:
  final_turnover: 1200000000
  individual_untaxed: 500000000
  final_rate: 0.005
  final_collected: 1000000
  final_self_paid: 2500000
  ordinary_tax: 29550000
  ordinary_credits: 20000000
steps:
  - final_due: max(final_turnover - individual_untaxed, 0) * final_rate
  - final_settled: final_collected + final_self_paid
  - final_remaining: final_due - final_settled
  - ordinary_balance: ordinary_tax - ordinary_credits
  - incorrect_ordinary_balance: ordinary_balance - final_due
expected:
  final_due: 3500000
  final_settled: 3500000
  final_remaining: 0
  ordinary_balance: 9550000
  incorrect_ordinary_balance: 6050000
```

### Case 2. Company annual settlement and next-year instalment bases differ

The supplied ordinary PT computation establishes turnover 6,000,000,000, PKP 1,500,000,000, Article 31E proportional slice 1,200,000,000 at eleven percent and remaining 300,000,000 at twenty-two percent, tax 198,000,000. PPh 22/23 total 40,000,000 and own instalments total 80,000,000. Annual balance is 78,000,000. The ordinary following-year instalment numerator is 158,000,000, not 78,000,000: the earlier instalments are not deducted again. The exact monthly rounding/effective period needs the actual return/filing history and current rule. [Income Tax Law arts. 25,31E](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

```oa-check
name: Company final settlement versus ordinary instalment numerator
inputs:
  turnover: 6000000000
  eligible_turnover: 4800000000
  taxable: 1500000000
  ordinary_rate: 0.22
  reduced_rate: 0.11
  own_withholding: 40000000
  own_instalments: 80000000
steps:
  - reduced_slice: taxable * eligible_turnover / turnover
  - remaining_slice: taxable - reduced_slice
  - tax: reduced_slice * reduced_rate + remaining_slice * ordinary_rate
  - annual_balance: tax - own_withholding - own_instalments
  - following_numerator: tax - own_withholding
  - incorrect_numerator: following_numerator - own_instalments
expected:
  reduced_slice: 1200000000
  remaining_slice: 300000000
  tax: 198000000
  annual_balance: 78000000
  following_numerator: 158000000
  incorrect_numerator: 78000000
```

## When to refuse or refer

Apply R-ID-ASM-1 to 7 above. Continue useful draft preparation but do not manufacture a completed computation, acceptance receipt, authority, code or accountant sign-off. If the user asks how to resolve an open tax fact, search the actual cited Indonesian law and document first; refer the bounded unanswered question with its evidence where necessary. A bank-only package with unsupported gross, credits, residence, method or material reconciliation cannot become filing ready merely because every worksheet tab exists.

## Completion checklist and reviewer brief

Retain all original ID-ASM-1 through 13 checks, corrected as follows:

1. Every required upstream computation is present or explicitly missing, including ordinary individual income tax where needed.
2. Commercial revenue, VAT price/base and income-tax bases reconcile through explicit documented adjustments, without an invented tolerance write-off.
3. Own non-final credits, foreign cap and instalments reconcile to the appropriate evidence; agent taxes and final settlement stay separate.
4. Final-tax monthly turnover, individual untaxed portion and actual customer collections/self-deposits reconcile; no duplicated payment or instant crossing-month regime switch.
5. Payroll final-period liability and employment certificates reconcile to monthly withholding/refunds; no fictitious annual employer return.
6. Entity fiscal reconciliation and loss year/usage schedule support PKP and the actual ordinary/facility computation.
7. The actual amended final-tax eligibility, transition/election and following-year position are named, with unresolved facts preserved.
8. Current payment article/code/period and annual balance are confirmed, or clearly marked unconfirmed with no code generated.
9. The actual annual deadline/extension and payment-before-submission rule are stated; monthly tax, BPJS, certificate and return obligations are separated.
10. Retention of books and supporting electronic evidence for ten years in Indonesia is recorded, without inventing an offshore-storage approval route. [KUP art. 28(11)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).
11. Every tax position has its operative legal source, period, method/version and actual assumption/evidence.
12. Accepted-return receipt, complete return and attachments are retained separately from payment receipts and drafts.
13. The original professional review and taxpayer/authorised-filer submission responsibility remain clear; no success/sign-off is invented.

The reviewer brief contains: executive summary with identity/period/regimes/PKP and supported balances; ordinary income-tax computation and fiscal bridge; loss and foreign-credit schedules; final-tax monthly/transition evidence; employment/payroll and BPJS reconciliation with pending portions; VAT reconciliation including compensation/corrections; own-versus-agent withholding; all seven cross-checks and their failures; legal positions and sources; missing facts/documents; related-party and special-regime flags; and following-year instalment, NPPN, final-regime, VAT and TP actions. Entertainment/nominatif lists, mixed-use costs and related-party reasonableness remain checks, not an unsupported universal deduction prohibition.

## Taxpayer action list and output files

Produce the original three deliverables, using calendar 2026 in filenames and actual working directory/output support rather than an assumed platform-only directory:

1. `[taxpayer_slug]_2026_id_master.xlsx`: Cover, identity/status, ordinary individual OR entity computation, actual current return mapping, commercial/fiscal schedules, final-tax tracker, income/credit/slip register, own payment/NTPN register, payroll/BPJS, VAT/compensation, cross-check summary and confirmed/provisional billing schedule. Add assets/liabilities/family or owners/directors/affiliates as appropriate. Use formulas, retain source inputs and verify no broken references or hidden hard-coded total.
2. `reviewer_brief.md`: the complete evidence/position/gap brief above, including named material blockers and what would close them.
3. `taxpayer_action_list.md`: dated pre-filing payment and confirmation actions, annual submission/receipt retention, required monthly corrections, applicable audit/TP attachments, and following-year compliance.

The action list tells the individual to settle the supported annual balance before the ordinary March deadline and the entity before the ordinary April deadline, subject to its actual period/extension. It separately lists outstanding monthly payroll, ordinary instalment and final-tax settlement, VAT and supplier withholding, with current rules and receipt evidence. Never demand all categories from a taxpayer who has no such duty, never instruct an unconfirmed payment code and never file an employee certificate as a standalone annual employer return.

Record retention includes general ledger, supporting invoices/documents, slips issued/received, VAT invoices, state-payment receipts, accepted-return receipts, amendments/refunds/compensation and the complete signed/approved return package. If work is interrupted, save the workbook inputs/formulas, completed reconciliations, draft brief and exact remaining gaps; present partial deliverables as partial. Do not prioritise formatting over completing the core calculation checks.

## Known gaps retained from the original scope

PDF filling, live filing, Coretax XML generation, ERP integration, CbCR XML, audit performance, TP file drafting, non-resident branch/foreign-credit specialist calculations, tax holidays, KEK and special facilities are not supplied by this assembly method. Current form fields, certificate details, payment-code combinations and channel availability require the official version for that actual filing. A gap in these operations does not permit a wrong line map or a claimed successful live action.

## Sources

| Official source | Read for and read date |
|---|---|
| [DJP consolidated Income Tax/KUP laws](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) | KUP arts. 3,7,9,28; Income Tax arts. 6,9,17,21,25,31E, with relevant explanations: liability, records, deadlines, loss/fiscal/instalment boundaries. Read 2026-11-14. |
| [PP 55/2022](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan) | Arts. 59-63 and historical art. 69, monthly base, individual allowance, crossing year and collections. Read 2026-11-14. |
| [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) | Amended arts. 56-58/deleted art. 59, permanent exits and exact art. II entity/household transitions. Read 2026-11-14. |
| [PMK 164/2023](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau) | Arts. 5-9,16-19: election, monthly/annual evidence, instalment transition and independent PKP reporting. Read 2026-11-14. |
| [PMK 168/2023](https://www.pajak.go.id/id/peraturan/petunjuk-pelaksanaan-pemotongan-pajak-atas-penghasilan-sehubungan-dengan-pekerjaan-jasa-1) | Arts. 2-3,5-16,19-22: employee/agent classifications, final period, documentation and refunds. Read 2026-11-14. |
| [PMK 81/2024](https://pajak.go.id/en/node/113110) | Arts. 94-100 and 226-237: actual deposit/payment timing and ordinary/special instalments; no current-code/expiry assumption inferred. Read 2026-11-14. |
| [PMK 131/2024](https://jdih.kemenkeu.go.id/api/download/f128868e-3cf6-4596-8407-c34eeca0e7be/2024pmkeuangan131.pdf) | Arts. 2-4 VAT price-to-base bridge and separately regulated supplies. Read 2026-11-14. |
| [PMK 172/2023](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan) | Arts. 16-19 prior-year/documentation/CbCR triggers, availability and annual reporting distinctions. Read 2026-11-14. |
| [PER-3/PJ/2026](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) | Arts. 2-8 annual/part-year deadlines, extension, electronic/paper channel and receipt conditions. Read 2026-11-14. |
| [PER-12/PJ/2026 operative DJP text](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan) | Amended arts. 29A-29E,80A,129A-129B and art. II, correction accounting and transition from 1 October 2026. The JDIH metadata's downloaded wrong printer-regulation PDF was rejected as evidence. Read 2026-11-14. |

- Read 2026-11-14: [PER-12/PJ/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-11pj2025-tentang-ketentuan): actual amended arts. 6-7 certificate names, final period and delivery timing.
- Read 2026-11-14: [PER-8/PJ/2026](https://pajak.go.id/id/peraturan/perubahan-atas-peraturan-direktur-jenderal-pajak-nomor-10pj2024-tentang-ketentuan): amended billing art. 5, 336-hour validity separate from legal payment due date.

Not yet confirmed: exact calendar-2026 Coretax form field/attachment mapping, annual/mobile/offline/XML eligibility, current payment-code pairings/code length, detailed certificate field mapping and accepted-receipt format; taxpayer-specific audit/foreign-credit/special-regime obligations; ministerial interest and permitted payment rounding; any missing upstream ordinary individual computation. Each blocks only the dependent filing-ready assertion, not supported draft work. No future extension or relief is assumed.

## Footer disclaimer

OpenAccountants: open-source accounting skills for AI. This is not tax advice. All outputs must be reviewed and signed off by a qualified Indonesian tax consultant (Konsultan Pajak bersertifikat) before filing via Coretax DJP.
