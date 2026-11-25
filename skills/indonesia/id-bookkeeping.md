---
name: id-bookkeeping
description: >
  Prepare Indonesian bookkeeping and NPPN classification working papers for
  calendar 2026. Establish books versus simple records, actual statutory KLU
  and region, gross revenue and withholding reconciliations, inventory, capital
  assets, fiscal add-backs and an evidence-linked handoff. Does not file a return
  or infer a tax credit from a bank deposit. Trigger on pembukuan, pencatatan,
  NPPN, bank classification and Indonesian tax bookkeeping.
jurisdiction: ID
tax_year: 2026
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: bookkeeping
version: "2.1"
category: bookkeeping
type: computation
---

# Indonesia bookkeeping and NPPN working papers v2.1

**Answer first.** NPPN multiplies eligible non-final turnover by the statutory **net-income percentage** for the activity and region. An otherwise eligible individual must have prior-year gross turnover strictly below IDR 4.8 billion and give timely notice. A separate records exception can apply at exactly IDR 4.8 billion when all business or independent professional receipts are subject to final income tax or outside the income tax base. Companies keep books. [Income Tax Act art. 14](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a), [PER-17/PJ/2015 arts. 1–6](https://pajak.go.id/id/peraturan/norma-penghitungan-penghasilan-neto), [PMK 81/2024 arts. 450–452](https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf).

## Scope

Calendar-2026 transaction classification and evidence preparation for Indonesian resident individuals and ordinary resident businesses. Pembukuan means books; pencatatan means records; NPPN determines net income from a statutory percentage. Produce the working paper and reviewer brief, not a filed SPT or an assertion that the income tax was paid. Corporate tax goes to `id-corporate-tax`, final small-business tax to `id-pph-final-umkm`, payroll to `id-payroll-pph21`, VAT to `indonesia-vat`, Coretax to `id-einvoice-coretax`, and annual assembly to `id-return-assembly`. The old route `id-income-tax` resolves to the US state of Idaho, not an Indonesian individual-income method. Never load it for Indonesia; prepare the Indonesian ordinary-income computation separately from its official law and record any missing work.

Preserve specialised-sector, BUT/permanent-establishment, foreign-currency-permission, cross-border related-party, concession, crypto/capital-market and mixed-regime checks below. An accountant's approval of another file does not establish approval of this method.

## Ask the client first

1. Taxpayer/entity, actual period, residence, NIK/NPWP and registered activity; prior returns and complete prior/current-year turnover from all activities.
2. Actual chosen accounting basis and inventory method, earlier books/records, notice and receipt for NPPN, and any permission changing method/year or using foreign language/currency.
3. Actual statutory KLU, activity description and the place where each business/profession is performed, not just a newer KBLI label or registered address.
4. Full-year bank/card/platform statements, cash books, sales and purchase invoices, returns, payroll, expenses and fixed-asset/inventory records, with source identifiers.
5. Withholding slips and payment confirmations, loan/lease/related-party contracts, VAT registration/invoices and the separation of final, non-final and non-taxable income.
6. Supporting evidence for personal/business allocation, concessions, source-specific deductions, tax-basis differences and unresolved notices/audits.

Read existing records first. Minimum missing taxpayer, period, gross-turnover evidence or accounting regime prevents an asserted final classification. Missing detail can remain an explicit unresolved item while independently supported bank reconciliation continues.

## The method, step by step

## Rates, bands and thresholds

| Item | Rule, 2026 | Official source |
|---|---|---|
| NPPN ceiling and turnover base | Individual's total gross turnover from all businesses and independent professional activities in the preceding tax year must be below IDR 4,800,000,000. Combine spouses’ amounts where property and income are separated by agreement or the wife elects separate tax administration under Income Tax Act art. 8(2)(b) or (c). | [PMK 81/2024 arts. 450 and 452](https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf) |
| NPPN notice | First three months of the tax year for existing registrants (31 March 2026 for a calendar-year taxpayer). Eligible individuals newly registered during 2026 notify by the earlier of three months from registration and the end of the tax year. A missed applicable deadline is treated as choosing books. | [PMK 81/2024 art. 450(2)–(4)](https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf), [DJP 2026 Coretax notice](https://www.pajak.go.id/sites/default/files/2026-02/Penyampaian%20Pemberitahuan%20NPPN%20Melalui%20Coretax%20DJP%20Tahun%20Pajak%202026.pdf) |
| Books and retention | Companies and otherwise required individuals keep books. An individual whose total prior-year business or professional receipts are entirely subject to final tax or outside the income tax base and do not exceed IDR 4,800,000,000 may keep records without an NPPN notice. Keep supporting material, including electronic records, for ten years in Indonesia. | [KUP art. 28](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a), [PMK 81/2024 arts. 448 and 451–452](https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf) |
| Inventory | Cost by weighted average or first-in-first-out; no LIFO | [UU PPh art.10(6)](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |
| Income-generating expenditure with benefit beyond one year | Capitalise and apply the actual depreciation/amortisation rule; no invented low-value safe harbour | [UU PPh art.9(2)](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |

The table below replaces the old approximate samples with the actual **PER-17 annex I KLU** rows. The three percentage columns are, in order, the ten specified provincial capitals, other provincial capitals and other areas. The ten are Medan, Palembang, Jakarta, Bandung, Semarang, Surabaya, Denpasar, Manado, Makassar and Pontianak. These are not three freely chosen tax brackets. Determine the actual activity and region before applying a row, and establish that the income is non-final and NPPN eligible. [PER-17 art.4](https://pajak.go.id/id/peraturan/norma-penghitungan-penghasilan-neto).

| Statutory KLU | Actual annex activity and condition | Ten capitals | Other capitals | Other areas | Official source |
|---|---|---|---|---|---|
| 47111 | Supermarket/minimarket principally food, drink or tobacco | 30% | 25% | 20% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 47711 | Clothing retail | 30% | 25% | 20% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 47911 | Retail through media for the specified food/drink/tobacco/chemical/pharmacy/cosmetic/lab products, not every online seller | 30% | 25% | 20% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 56101 | Restaurant | 25% | 20% | 20% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 41011 | Residential building construction; test separate final-tax treatment first | 20% | 19% | 18% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 49429 | Other land passenger transport, not an automatic taxi/ride-hailing classification | 20% | 15% | 15% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 77100 | Motor-vehicle operating rental without operator | 32% | 31% | 29% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 86202 | Specialist medical practice | 50% | 50% | 50% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 69100 | Legal services including notarial work | 51% | 50% | 50% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 69200 | Accounting, bookkeeping, audit and tax consultancy | 50% | 50% | 50% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 71100 | Architecture, civil engineering and technical consultancy | 50% | 50% | 50% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 62010 | Computer programming | 50% | 50% | 50% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 90001 | Performing-arts production, not an automatic author classification | 35% | 32.5% | 31.5% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 14111 | Textile garment manufacture | 13.5% | 13% | 12.5% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 45201 | Motor-car repair | 20% | 18.5% | 17.5% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 85495 | Private tutoring and counselling | 30% | 27.5% | 25% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 74201 | Photography | 50% | 50% | 50% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 74100 | Specialised design | 32% | 31% | 29% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 96111 | Hair cutting | 30% | 28% | 27% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |
| 96112 | Beauty salon | 30% | 28% | 27% | [PER-17 annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf) |

The earlier codes 96021,69201/69202,71101 and85490 were not located as those exact annex-I entries. Their activities are retained above through the actual salon, accounting, architecture and tutoring entries, but no automatic newer-KBLI-to-statutory-KLU crosswalk is certified. The old author's classification of 90001 as independent writing is wrong; 90001 describes performing-arts production. Determine the actual writer/artist activity rather than borrowing its rate. Construction can have its own final tax, so the presence of a norm in the annex does not authorise NPPN for separately-final receipts.

### 1. Establish books versus records

KUP art. 28(1)–(2) requires books for Indonesian companies and individuals carrying on business or independent professional work, subject to the statutory records exceptions. At exactly IDR 4.8 billion, an individual cannot elect NPPN. Test the separate records exception for receipts entirely subject to final tax or outside the income tax base. Use `id-pph-final-umkm` for final-turnover tax eligibility, professional exclusions, aggregation, election-out and the 2026 transitions. [KUP art. 28 and Income Tax Act art. 14](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a), [PMK 81/2024 arts. 448 and 450–452](https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf), [PP 20/2026 arts. 56–58 as amended](https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf).

PER-17 art.8 expressly repeals KEP-536/PJ./2000 from the regulation's effective tax year. Do not describe the earlier schedule as the current coefficient source or use a retail proxy for an unlocated online seller. Use annex I for an individual validly using NPPN; annex II and III concern the audit fallback for failure to keep/show records, not an elective company concession. [PER-17 arts.3-9](https://pajak.go.id/id/peraturan/norma-penghitungan-penghasilan-neto).

Changing the accounting method or book year needs DJP approval under KUP art.28(6), and the chosen basis must be consistent. Do not invent an automatic annual election from books/NPPN into final tax by March. A previous notice choosing general rates can prevent future final-tax access. Missing election records remain missing; the absence of a document in this chat does not prove no notice was filed. [KUP art.28](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a); [PP 20 amended art.57(4)](https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf).

### 2. Maintain good-faith books and actual recognition

Maintain books or records in good faith and reflect the actual activity. Use Latin letters, Arabic numbers, Indonesian and rupiah unless authorised. When using English and US dollars, check the permission or notification route for the taxpayer. Qualifying mineral and coal contract taxpayers, oil and gas cooperation contractors and qualifying joint operations use the notification route in PER-8/PJ/2025 art. 19. A bilingual export or USD bank account establishes neither route. Obtain approval before changing the bookkeeping method or year. [KUP art. 28](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a), [PER-8/PJ/2025 arts. 16 and 19–21](https://www.jdih.kemenkeu.go.id/download/c391f62b-eac4-47ec-8cc2-50e4fe748b13/PER-8_PJ_2025.pdf).

Use a consistent accounting basis. The tax cash method is restricted to the eligible taxpayers in PMK 81/2024 art. 456, subject to annual notification under art. 458. For an eligible body, the turnover ceiling is IDR 4.8 billion from all activities and locations in the prior tax year. Include cash and non-cash sales, all purchases and stock in cost of goods sold and the required depreciation and amortisation. Retain supporting documents and ledgers with the financial statements. [PMK 81/2024 arts. 455–460](https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf).

For inventory, apply the supported FIFO/average method consistently. An undocumented method is unresolved, not automatically weighted-average. Separate purchase of inventory from period consumption and closing stock. For assets, capitalise qualifying expenditure with benefit beyond one year and preserve cost, in-service date, business use, prior tax basis and actual classification; do not expense/capitalise by an arbitrary rupiah cutoff. The current depreciation schedule and special useful-life conditions must be read in the applicable current regulation; do not default an unclassified asset to obsolete PMK96/2009. [UU PPh arts.9(2),10(6),11](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a).

### 3. Classify the source transaction before its bank movement

For every inflow/outflow identify counterparty, underlying contract/invoice, period, sign/currency, gross amount, withholding, fees/VAT and net bank movement. Preserve the chain of source identifiers and any unreconciled difference. A Shopee/Tokopedia/Stripe payout is not necessarily gross revenue; a loan or capital transfer is not automatically sales. A foreign customer does not alone prove VAT export treatment or eliminate every withholding responsibility.

| Working-paper bucket | Retained examples | Required treatment or handoff |
|---|---|---|
| Peredaran bruto dari usaha | Sales invoices, POS, marketplace receipts | Reconcile gross and settlement; distinguish non-final, final and exempt receipts. No brand-based rate  [KUP art.28 and UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |
| Pekerjaan bebas | Doctor, lawyer, consultant, designer fees | Actual professional classification/KLU; route payer withholding separately rather than presume corporate-service PPh 23  [KUP art.28 and UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |
| HPP/cost of goods sold | Stock, freight-in, direct labour, factory overhead | Actual books and inventory movement. NPPN does not deduct these expenses again  [KUP art.28 and UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |
| Beban usaha | Gaji, sewa, listrik, internet, ATK, software, depreciation, insurance | Apply business purpose, period and specific deduction rules under books; do not add actual deductions on top of NPPN  [KUP art.28 and UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |
| Penghasilan lain-lain | Bank interest, foreign-exchange gains, disposal gains | Determine actual ordinary/final/exempt treatment and keep it separate; no blanket final-tax assumption  [KUP art.28 and UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |
| Fiscal add-backs | Prive, personal use, unsupported donations/provisions, penalties | Apply the statutory exclusion and exception, not a blanket add-back for all employee benefits  [KUP art.28 and UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |
| Fixed assets | Computers, equipment, vehicles | Capitalise and calculate through the current asset-specific rule, not by merchant label  [KUP art.28 and UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |
| Owner capital/prive | Contributions and withdrawals | Equity movements; document whether capital, distribution, loan or remuneration. No automatic income/expense  [KUP art.28 and UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |
| Loan principal/interest | Drawdowns, repayments, leases | Principal is a balance-sheet movement; test interest's business purpose and actual related-party/limitation rules separately  [KUP art.28 and UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |
| Tax settlement | PPh instalments, withholding, VAT settlement | Separate prepaid tax, own non-deductible income tax and third-party collections. A bank payment is not proof of a legally creditable slip  [KUP art.28 and UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a) |
For company books, retain the sequence gross revenue, HPP, gross profit, operating expense/profit, non-operating items, positive/negative fiscal adjustments, final and exempt income, assets/liabilities/equity. For individual books retain the analogous business/professional split. Earlier 1770/1771 appendix and line references are historical navigation only; no exact 2026 Coretax field map is certified here. Supply the current tax computation/assembly method with the reconciled category totals instead of silently placing them in a legacy box.

### 4. Apply deduction rules under books, without inventing them under NPPN

UU PPh art.9 excludes profit distributions (including cooperative SHU), personal shareholder/partner/member costs, unqualified reserves, the individual's specified personal insurance unless the statutory employer-payment treatment applies, excessive related-party remuneration, unqualified gifts/donations, own income tax, private living costs, salaries to members of partnerships/firma/CV whose capital is not divided into shares, and administrative tax sanctions/criminal tax fines. Its reserve exceptions include specified credit institutions/factoring/insurance/BPJS/LPS and mining/forestry/waste restoration, with actual conditions. Qualifying statutory donations and approved religious contributions have exceptions. Former art.9(1)(e)'s benefits-in-kind prohibition is deleted; do not automatically add back every natura item. Apply actual current employee/employer treatment separately. [UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a).

Allocate mixed private/business expenses on an evidenced basis. Missing business use or documentation means the deduction is unsupported, not that a legal all-or-nothing allocation has been proved. Income-generating capital expenditure is relieved through the appropriate depreciation/amortisation rule. Bribes/gratuities and the specified foreign-public-official payments are independently excluded by amended art.20A. No expense is deducted from the small-business final-turnover base; final-tax costs and ordinary costs must remain segregated. [UU PPh art.9](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a); [PP 20 amended art.20A](https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf).

### 5. Compute NPPN by actual activity and region

For each qualifying non-final activity, statutory net income = its applicable annex-I percentage times that activity's supported gross turnover. Sum the activities' net incomes under PER-17 art.5, then route PTKP, individual brackets, other ordinary income and valid credits to the actual individual return method. No separate COGS/operating expense deduction or accounting loss is appended to this deemed-net-income computation. A final/exempt receipt is handled under its own rules. VAT input credit rights depend separately on actual PKP/tax conditions; NPPN does not turn VAT into an ordinary income-tax expense deduction. [PER-17 arts.1,5-6](https://pajak.go.id/id/peraturan/norma-penghitungan-penghasilan-neto).

If required books/records were not kept/shown, UU PPh art.14(5) and PER-17 art.3 permit the stated assessment method with KUP sanctions. They do not prescribe the old file's automatic 50%/20% uplift to net income. Identify the real assessment article and notice before calculating any penalty. Failure to notify NPPN makes the individual deemed to choose books; it does not itself prove that precise invented uplift. [UU PPh art.14](https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a); [PER-17 arts.2-3](https://pajak.go.id/id/peraturan/norma-penghitungan-penghasilan-neto).

## Boundary and exception table

| Retained code/topic | Action |
|---|---|
| R-ID-1, foreign BUT/PE | Refer source attribution, treaty and specific books/return rules |
| R-ID-2, mining/oil/gas/shariah banking | Specialist accounting and tax regime; no generic deduction/concession assumption |
| R-ID-3, USD/foreign-currency books | Verify the permission or notification route and supporting evidence before using currency-sensitive return totals |
| R-ID-4, cross-border related parties/TP | Preserve contracts, relationship, price and documentation questions. No unverified copied threshold or obsolete PMK213 shortcut |
| R-ID-5, final-turnover regime | Retain accounting evidence but compute final tax through `id-pph-final-umkm`, not NPPN |
| R-ID-6, yayasan/cooperative/education concessions | Confirm actual income/exemption conditions separately |
| R-ID-7, unknown KLU/region | No coefficient by analogy or highest-rate default; obtain the classification evidence |
| R-ID-8, crypto/derivative/capital markets | Refer actual current final/non-final rule; do not merge into ordinary professional turnover automatically |
| R-ID-9, missing NPPN notice | Obtain receipt; if legally not timely, use the books branch rather than invented net-income uplift |
| R-ID-10, mixed books/NPPN within year | Resolve the applicable consistent regime; do not switch by whichever transaction gives lower tax |
| Foreign-currency receipt | Preserve amount/currency/date and actual conversion evidence; no automatic BI middle-rate instruction |
| Missing bukti potong | Do not claim a documented credit that has not been obtained or reconciled; continue supported gross-revenue classification |
| Two plausible activities | Determine actual statutory classification, not the more punitive coefficient |

## Worked cases

### Designer's bank reconciliation

The taxpayer is a resident graphic designer with timely NPPN notice, working in Jakarta under the actual statutory specialised-design activity KLU 74100, tax year 2026. Retain prior-year turnover 380m and the recorded 28 February notice as hypothetical evidence inputs, updated to the current year where applicable. Annex I gives **32%**, not the old assumed50%; this does not classify every modern graphic-design business automatically. The client's actual KLU must fit the annex description. [PER-17 arts.1-6/annex I](https://pajak.go.id/id/peraturan/norma-penghitungan-penghasilan-neto), [annex I](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf).

Retain every original statement item: PT XYZ deposit18.5m; co-working rent2.5m; cash project A6m; Adobe 812,000; private withdrawal5m; CV ABC deposit24.5m against stated gross25m; PPh 25 payment1.2m; cancelled-project refund3m; bank giro interest84,000; Stripe payout19.2m identified as USD1,200. Rent/software are not deducted again under NPPN, private withdrawal is not a business expense, instalment is not an expense and bank interest needs its own classification. The Stripe net settlement is not proved to be gross export turnover or the correct statutory currency conversion.

The first deposit's old annotations conflict: assumed gross18.87m implies withholding370,000, while its note says377,000. The credit total877,000 therefore cannot be accepted through a7,000 "rounding" plug. The second slip indicates500,000. If documents actually establish gross18.87m and withheld370,000, the two withholding amounts total870,000, not877,000; their legal article and creditability still require valid slips. In particular, a professional individual should not automatically be treated as a company subject to2% PPh 23. Route the actual payer/recipient facts to the payroll/withholding method.

Conditionally assume documents establish those first two gross amounts, cash6m, supported ordinary refund3m and actual gross foreign turnover19.2m with the proper conversion and no additional fees. Then gross is66.07m and deemed net income21.1424m at the actual Jakarta 32% row. This is the bookkeeping handoff, not a tax or refund award. The old NIL-tax outcome depended additionally on the actual applicable allowance and other income, which the separate individual return calculation must establish.

```oa-check
name: Source-document reconciliation and design norm
inputs:
  first_gross: 18870000
  first_net: 18500000
  second_gross: 25000000
  second_net: 24500000
  cash: 6000000
  supported_refund: 3000000
  supported_foreign_gross: 19200000
  jakarta_design_norm: 0.32
steps:
  - first_difference: first_gross - first_net
  - second_difference: second_gross - second_net
  - total_differences: first_difference + second_difference
  - gross: first_gross + second_gross + cash - supported_refund + supported_foreign_gross
  - deemed_net: gross * jakarta_design_norm
  - old_unsupported_credit_difference: 877000 - total_differences
expected:
  first_difference: 370000
  second_difference: 500000
  total_differences: 870000
  gross: 66070000
  deemed_net: 21142400
  old_unsupported_credit_difference: 7000
```

### Same gross, different statutory region, no highest-rate default

A properly qualifying specialised-design activity has supported non-final gross100m. The actual ten-capital region gives net32m, another provincial capital31m, another area29m. At exactly4.8b of turnover the NPPN eligibility branch fails regardless of which percentage gives less tax. The old 50% guess would overstate the first hypothetical net by18m. These are net-income figures before the individual's separate tax/allowance/credit calculation. [PER-17 art.1,4-6](https://pajak.go.id/id/peraturan/norma-penghitungan-penghasilan-neto); [annex I KLU 74100](https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf).

```oa-check
name: Actual design region instead of the old professional proxy
inputs:
  gross: 100000000
steps:
  - ten_capitals_net: gross * 0.32
  - other_capital_net: gross * 0.31
  - other_area_net: gross * 0.29
  - old_guess_net: gross * 0.50
  - old_guess_overstatement: old_guess_net - ten_capitals_net
expected:
  ten_capitals_net: 32000000
  other_capital_net: 31000000
  other_area_net: 29000000
  old_guess_overstatement: 18000000
```

## When to refuse or refer

Retain the ten codes above. Refer unsupported KLU/permission/regime, specialised sector, professional withholding, source-sensitive currency/foreign receipts, concession, audit or material related-party matters to a qualified Indonesian tax reviewer. Stop the unsupported calculation, explain the specific missing evidence, and continue a supported transaction reconciliation if possible. No SPT total leaves this method without its source or a clearly identified unresolved field. No unsupported NPPN coefficient is printed as an illustrative rate.

## Filing and payment

This method does not file or pay. Deliver the supported books/records, category totals, adjustment schedules, KLU/region/notice evidence, final/ordinary split, source-currency reconciliation and candidate tax-credit slips to the return assembler. Use the actual taxpayer's current authorised Coretax workflow and official forms, not a legacy attachment map guessed from the old text. Preserve accepted annual returns, payment/BPN/NTPN and withholding evidence when provided; a proposed posting list or import file is not proof of an accepted filing.

## Completion checklist

1. Working paper: one row per transaction with date, counterparty, source/net/gross currency amounts, working-paper category, tax regime, PPh/PPN flag, document reference and unresolved/reviewer note.
2. Regime summary: actual books/records method, prior/current turnover, timely notice, actual statutory KLU and activity/region; for NPPN, the applicable row/percentage/source.
3. Reconciliation: bank-to-gross differences, withholding/fees, loan/capital/prive, inventory/capital assets, final/exempt/ordinary income and separate fiscal adjustments all traced.
4. Reviewer brief: missing documents, unsupported assumptions and monetary differences ranked by actual cash impact; exact permission, concession and source gaps retained.
5. Sign-off handoff: independent recomputation, source passages/read dates, actual return-version/field map and accountable qualified review. Preparation is not professional approval or payment.

## Sources

| Source and scope actually read | Official URL | Read on |
|---|---|---|
| PER-17/PJ/2015 operative arts.1-9. Read for strict ceiling, notice, books/records branches, audit fallback, exact ten-capital regions, separate activity computations and repeal of KEP 536 | https://pajak.go.id/id/peraturan/norma-penghitungan-penghasilan-neto | 2026-11-14 |
| PER-17 annex I, header and the twenty exact KLU rows shown above, with adjacent descriptions. Read for actual activity wording and all three regional net-income percentages, not a complete certification of the whole annex or a new KBLI crosswalk | https://pajak.go.id/sites/default/files/2019-06/Lampiran%201_PER_17_PJ_2015.pdf | 2026-11-14 |
| DJP consolidated tax laws through UU 6/2023. Read for KUP art.28 and explanation, UU PPh arts.9,10(6),14, including records, consistency, foreign-language/currency permission, deductions, inventory and NPPN. This is not claimed to consolidate later laws | https://pajak.go.id/media/sdsn-2023-7-1-0-2816268a | 2026-11-14 |
| PP 20/2026 amended arts.20A,56-58 and art.II. Read for bribery exclusion and final-turnover eligibility/aggregation/election/transition interactions, whose calculation remains in the final-tax owner | https://jdih.kemenkeu.go.id/api/download/d057ff82-50e7-4127-b66b-f704a36f071d/2026pp020.pdf | 2026-11-14 |
| PMK 81/2024 arts. 448, 450–452 and 455–460 | https://jdih.kemenkeu.go.id/api/download/637047be-3dba-4347-aba1-98fa7fd5ab3f/2024pmkeuangan081.pdf | 2026-11-24 |
| PER-8/PJ/2025 arts. 16 and 19–21, language and currency permissions or notifications | https://www.jdih.kemenkeu.go.id/download/c391f62b-eac4-47ec-8cc2-50e4fe748b13/PER-8_PJ_2025.pdf | 2026-11-24 |
| DJP 2026 notice and FAQ | https://www.pajak.go.id/sites/default/files/2026-02/Penyampaian%20Pemberitahuan%20NPPN%20Melalui%20Coretax%20DJP%20Tahun%20Pajak%202026.pdf and https://www.pajak.go.id/sites/default/files/2026-10/FAQ%20PP%20NOMOR%2020%20TAHUN%202026%20Penyesuaian%20Pengaturan%20di%20Bidang%20Pajak%20Penghasilan.pdf | 2026-11-24 |

Not yet confirmed: current exact Coretax individual/company field mappings replacing the historical1770/1771 references; activity-specific crosswalk for the old96021,69201/69202,71101,85490 codes and the actual independent writer/author classification; client-specific foreign-language or foreign-currency authorisation and transaction conversion, interest/thin-cap ratios, specialised TP thresholds and benefits-in-kind exceptions; the actual legal category/creditability of the designer's payer slips, his foreign gross/fees/conversion and any final tax on giro interest; current personal allowance and total individual-return outcome through the missing general individual-income-tax companion. Old generic NPPN ranges, the50% design assumption, the7,000 rounding plug, an automatic50%/20% uplift, a universal BI midpoint and copied legacy return fields are not usable guidance. The supported bookkeeping method and actual annex rows remain available.
