---
name: id-pph-final-umkm
description: >
  Compute Indonesian final income tax on qualifying small-business turnover for
  calendar 2026 under PP 55/2022 as amended by PP 20/2026. Covers the individual
  turnover relief, owner and spouse aggregation, excluded professional activities,
  cooperative and legacy-entity transitions, permanent opt-out, monthly settlement
  and annual reporting. Trigger on PPh Final UMKM, PP 20/2026, PP 55/2022,
  0.5 percent tax, omzet and perseroan perorangan. Route VAT and general-rate
  income tax to their separate methods.
jurisdiction: ID
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: "2.0"
category: international
type: computation
---

# Indonesia PPh Final UMKM v2.0

> Load alongside `foundation` and `intake`. Employment withholding belongs to `id-payroll-pph21`; VAT belongs to `indonesia-vat`. This method prepares a calculation and evidence for a Konsultan Pajak, not an accepted return.

**Answer first.** The final rate remains **0.5%**, but small turnover alone does not qualify someone. PP 20/2026 changed the eligible taxpayers and aggregation rules from **22 April 2026**. Individuals have an annual **IDR 500,000,000** untaxed business-turnover portion; companies do not. First establish the entity, actual activity, combined turnover, earlier elections and transition entitlement. [PP 20/2026 art. I, amended arts. 56 to 58 and art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [PP 55/2022 art. 60](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan).

## Scope

Calendar-2026 Indonesian resident individuals carrying on business, qualifying single-founder perseroan perorangan, cooperatives and expressly grandfathered entities. Preserve the distinction between current rules, the earlier PP 55/2022 rules and transitional access. An ordinary PT, CV, firma or BUMDes is not a new eligible entity merely because its turnover is small. [PP 20/2026 amended art. 57 and art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

The computation is final tax on qualifying business gross turnover. It is not Article 17 tax on profit, NPPN, payroll tax, VAT, foreign-tax-credit computation or a withholding schedule for passive income. Ordinary company tax goes to `id-corporate-tax`, individual NPPN/bookkeeping evidence to `id-bookkeeping`, with any ordinary individual-income computation separately prepared under Indonesian law, annual assembly to `id-return-assembly`, accounting evidence to `id-bookkeeping`, Coretax operations to `id-einvoice-coretax`, and entity formation to `id-formation`. `references` is the bibliography. The old `id-income-tax` route resolves to Idaho in this library, not Indonesia. Never load it for an Indonesian return. Resolve missing computation or conflicting figures under the official Indonesian source and record the gap.

## Ask the client first

1. **Person and period:** Indonesian residence, exact taxpayer form and NPWP/NIK, start/registration dates, calendar or approved different book year, and the actual return year.
2. **Activity and income:** describe each business/professional activity and supply; obtain contracts, invoices, foreign-source receipts and income already finally taxed or exempt. A platform or company name is not a legal classification.
3. **Turnover:** reconcile the preceding year's full turnover and every current month, all branches and businesses, gross sales before discounts, platform fees and expenses, and separately identified VAT. Obtain bank, platform and cash records rather than net settlements only.
4. **Connected taxpayers:** marriage and PH/MT separate-filing status, spouse and minor-child receipts and every single-founder company created by either spouse. Record owner/company totals separately from the amount actually subject to this final tax.
5. **History:** prior returns, final-tax certificates, registration year and original utilisation period, notices choosing general rates, incentive decrees, any certificate cancellation and the exact PP 20/2026 transition relied upon.
6. **Settlement:** monthly BPN/NTPN state receipts, withholding slips, the certificate or turnover statement supplied to customers, annual-return receipts, Coretax access/authorised signer, PKP status, payroll and distributions from a company to its owner.

Do not compute a final liability when turnover cannot be quantified or eligibility is unresolved. An annual aggregate permits a labelled annual cross-check, but does not reconstruct monthly deposits or payment dates. Record the missing months explicitly.

## The method, step by step

## Rates, bands and thresholds

| Item | Rule for 2026 and conditions | Official source |
|---|---|---|
| Final income-tax rate | 0.5% of qualifying monthly business gross turnover, not profit | [PP 20/2026 amended art. 56(1)-(3)](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Eligibility ceiling | Not more than IDR 4,800,000,000 under the preceding-year test and connected-taxpayer rules; eligibility turnover is wider than the monthly taxable base | [PP 20/2026 amended arts. 57-58](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Individual untaxed turnover | First IDR 500,000,000 cumulatively in the tax year across all places of business; no relief for a company, including a PT Perorangan | [PP 55/2022 art. 60(2)-(5)](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan) |
| Individuals and single-founder companies | No fixed utilisation-year cap in the new general rule because art. 59 is deleted; all other eligibility and permanent-exit conditions remain | [PP 20/2026 art. I items 4-6](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| New cooperative's utilisation period | Four tax years from registration, including its registration year; pre-existing cooperatives have the separate transition below | [PP 20/2026 amended art. 57(2)(f), explanation and art. II(1)(b)](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Legacy ordinary PT period | Earlier three-tax-year period survives only to its existing end if art. II(1)(e) applies; it is not a new election for a 2026 PT | [PP 55/2022 former art. 59](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PP 20/2026 art. II(1)(e)](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Legacy CV/firma/BUMDes period | Earlier four-tax-year period survives only while the grandfathering and old eligibility conditions hold | [PP 55/2022 former arts. 59,69](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PP 20/2026 art. II(1)(e)](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Self-paid monthly final tax | Ordinary due date is the 15th of the following month; determine actual non-business-day relief from the applicable administration rule before assigning a shifted date | [PMK 164/2023 art. 7(2)](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau) |
| Monthly reporting | Ordinary 20 days after period end, with no-payment exceptions and deemed filing through validated NTPN payment in art. 7(4)-(5); keep the collector's separate reporting duty distinct | [PMK 164/2023 arts. 7-8](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau) |
| Individual annual return | Three months after year-end, ordinarily 31 March 2027 for calendar 2026 | [KUP art. 3(3)(b), DJP consolidated text](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Entity annual return | Four months after year-end, ordinarily 30 April 2027 for calendar 2026 | [KUP art. 3(3)(c), DJP consolidated text](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Late annual return, individual | IDR 100,000, subject to KUP art. 7(2) exclusions and actual relief | [KUP art. 7, DJP consolidated text](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Late annual return, entity | IDR 1,000,000, subject to KUP art. 7(2) exclusions and actual relief | [KUP art. 7, DJP consolidated text](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Late-payment interest | Minister's applicable monthly rate; maximum 24 months, any part-month counts as a full month. No fixed approximate percentage is certified | [KUP art. 9(2a)-(2c), DJP consolidated text](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Record retention | Ten years in Indonesia for books, records and supporting electronic documents | [KUP art. 28(11), DJP consolidated text](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

### 1. Classify the taxpayer before applying a rate

Under amended art. 57(1), the ordinary eligible classes are resident individuals, a perseroan perorangan founded by one person and cooperatives. BUT/permanent establishments are excluded; non-residents are outside this resident-taxpayer method. A foundation/yayasan is not added to the list. A company benefiting from art. 31A, PP 94/2010 facilities or PP 40/2021 arts. 75/78 is excluded as specified by art. 57(2)(c). [PP 20/2026 art. I item 4](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

An individual's professional services (pekerjaan bebas) do not enter the final-tax base. The full amended list covers lawyers, accountants, architects, doctors, consultants, notaries, land-deed officials/PPAT, appraisers, actuaries and similar experts; musicians, presenters, singers, comedians, film/TV/advertising performers, directors, film crew, models, actors, dancers, sculptors, painters, online content creators/influencers/selebgram/bloggers/vloggers and other artists; athletes; advisers, teachers, trainers, speakers, extension workers, moderators and similar professions; writers, researchers, translators and similar professions; advertising agents; project supervisors/managers; brokers or people finding customers; travelling sales agents; insurance agents; MLM/direct-selling distributors and similar activities. [Amended art. 56(3)(a),(4)](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

The explanation distinguishes teaching piano personally from operating a piano-course business that employs other people. It also excludes a tax consultant's single-founder company providing the same professional services as its founder under art. 57(2)(b). Do not turn a professional fee into qualifying business income merely by invoicing through a PT Perorangan, selling online or serving several customers. A software/SaaS, template, photography or training business needs its actual activity and organisation analysed; the brand or the number of customers alone does not settle it. If materially uncertain, retain the classification question for the reviewer and withhold the affected final-tax conclusion. [PP 20/2026 explanations to arts. 56(4),57(2)(b)](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

### 2. Separate the eligibility ceiling from the tax base

For the ceiling, amended art. 58(1) counts preceding-year business AND professional-service gross turnover, final and non-final, including foreign turnover, before sales/cash/similar discounts. Aggregate all branches and businesses; professional or separately-final receipts can count toward eligibility even though they never enter this monthly final-tax base. Do not test only the turnover on which 0.5% was paid. [Amended arts. 57-58](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

Amended art. 57(2)(e) aggregates the individual with every PT Perorangan they founded. Under art. 58(2)-(3), PH/MT spouses' turnover and companies are combined for the ceiling; the statutory explanation expressly includes the minor child's income under the income-tax rules. The explanation gives a notary, boutique owner and child singer total that denies the boutique owner's next-year access. Keep the separate spouses' actual tax calculations and the eligibility aggregation distinct. PMK 164 art. 6(5) gives each PH/MT spouse their own untaxed individual-turnover portion; combining the ceiling is not permission to invent a shared company allowance. [PP 20/2026 amended arts. 57-58 and explanations](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [PMK 164/2023 art. 6(5)](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

For the monthly tax, PP 55 art. 60 counts money or money's-worth received OR accrued from qualifying business before discounts. Do not impose a universal cash-only convention. No COGS, operating expenses, biaya jabatan, PTKP income allowance, capital allowance or loss carryforward reduces this gross-turnover tax. Zero qualifying turnover gives zero tax. Recoverable VAT is analysed separately through `indonesia-vat`, not treated as business profit. Foreign-currency conversion and any unclear VAT-inclusive base remain specific unresolved facts until the applicable official rule and invoices are obtained. [PP 55/2022 art. 60](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan).

Income excluded by amended art. 56(3) includes individual professional services, foreign income whose tax is due or paid abroad, income separately subject to final tax and non-taxable income. Do not label all dividends, royalties, capital gains or one-off receipts automatically excluded: establish their actual income category and applicable provision. Keep employment salary under payroll, rent/construction and other specific final taxes under their own rules, and foreign-tax-credit questions under ordinary income tax. [PP 20/2026 amended art. 56(3)](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

### 3. Test earlier elections, utilisation periods and the transition

A notification choosing general rates is not an annual opt-out that silently lapses. Amended art. 57(4) prevents subsequent-year access after that notification; it also prevents later return after the aggregated-ceiling exclusion or cooperative period expiry described there. PMK 164 art. 5 ordinarily requires the notice by year-end for general rates from the following year; a new registrant can notify on registration for immediate general-rate treatment. Obtain the actual notice before comparing choices. [PP 20/2026 amended art. 57(2)-(5)](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [PMK 164/2023 art. 5](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

Record each specific art. II transition rather than using a general "everyone extended to 2029" claim:

| Earlier position | Transition and boundary | Official source |
|---|---|---|
| Individual's old period ended in tax year 2024 | Access for 2025 and 2026 while the stated earlier eligibility criteria hold; corresponding certificate continued for those years | [PP 20/2026 art. II(1)(a)(1),(c)(1)](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Individual or single-founder company's old period ended in 2025 | Access for 2026 under the stated criteria, with the corresponding certificate rule | [PP 20/2026 art. II(1)(a)(2),(c)(2)](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Cooperative registered before commencement, earlier period ends in 2024 to 2029 | The express 2025 to 2029 transition applies while old eligibility continues; explanation's cooperative registered in 2023 can continue through 2029 | [PP 20/2026 art. II(1)(b),(d) and explanation](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Existing CV, firma, ordinary PT or BUMDes/BUMDesma with an unexpired earlier period | Continue only until that period ends and while earlier eligibility holds. No fresh three/four-year period | [PP 20/2026 art. II(1)(e)](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |
| Previously qualifying individual/company newly affected by professional-company exclusion or owner/company aggregation | Art. II(1)(f) continues the stated existing final-tax treatment to the end of 2026; this is not a concession for a new taxpayer or every failed criterion | [PP 20/2026 art. II(1)(f), explanations](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) |

Historically PP 55 art. 59 gave individuals seven years, cooperatives/CV/firma/BUMDes/single-founder companies four years, and ordinary PTs three years. The original old file's suggestion that a PT Perorangan always had a three-year period was wrong. Earlier registrations use art. 69, and pre-commencement BUMDes and single-founder companies have art. 59(2)(b)'s start-year rule. Preserve the actual registration and used-period evidence rather than counting from the first tax payment automatically. Article 59 is now deleted; the table above describes transitional history, not fresh 2026 caps for individuals or single-founder companies. [PP 55/2022 former arts. 59,69](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PP 20/2026 art. I item 6](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

### 4. Compute each month and reconcile once at year-end

For an individual, set C to cumulative qualifying turnover before the month and M to that month's qualifying turnover. Taxable monthly portion = max(C+M-500,000,000,0) minus max(C-500,000,000,0); multiply by 0.005. This gives only the crossing-month excess, then the full qualifying turnover in later months. Do not renew the allowance per branch, marketplace, month or quarter. For a company, tax is 0.005 times its full qualifying monthly turnover; there is no individual allowance. [PP 55/2022 art. 60](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PMK 164/2023 art. 6](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

Reconcile the computed liability to actual final-tax slips and self-deposits, preventing double payment of an amount already lawfully withheld. PP 55 art. 62 permits both monthly self-payment and withholding/collection; it is not always self-deposited. The final tax does not credit against ordinary PPh 21/22/23/25/29. Keep non-final credits separate. If the individual paid tax on turnover later covered by the annual untaxed portion, PMK 164 art. 9 provides the refund-request route for tax not actually due; do not invent an automatic ordinary-income-tax credit. [PP 55 arts. 62-63](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PMK 164/2023 arts. 7-9](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

A taxpayer qualifying at the start whose current-year turnover crosses the ceiling continues the stated final-tax treatment through that year under PP 55 art. 61, then goes to ordinary tax in following years. Owner/company permanent exclusion and the PP 20 transition still need their separate analysis. Do not stop the final tax automatically on the sale crossing the ceiling or declare a fresh next-year election without checking art. 57(4). New registration, acquisitions, mergers, cessation and disputed partial-year facts require their own evidence and reviewer handoff. [PP 55/2022 art. 61](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PP 20/2026 amended art. 57 and art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

## Boundary and exception table

| Situation, retained from the old method | Treatment and handoff |
|---|---|
| R-ID-UMKM-1, turnover above the ceiling | Test the preceding/current year and aggregation separately; apply the statutory year-end transition where it actually applies, then ordinary individual or company tax |
| R-ID-UMKM-2, pekerjaan bebas or disputed activity | No final-tax treatment for the individual's professional receipts; analyse the professional-company exclusion and exact grandfathering rather than treating every new company as eligible |
| R-ID-UMKM-3, utilisation period expired | Check entity and original start date. Current cooperative cap and legacy-entity transition differ from the now-deleted individual/company cap |
| R-ID-UMKM-4, BUT or non-resident | Outside this resident final-tax method; refer for the proper source/residence/treaty computation |
| R-ID-UMKM-5, mid-year change, new registration, crossing or cessation | Preserve actual monthly receipts, start/stop dates and election. Continue only the route supported by art. 61/art. II; unusual partial years need review |
| R-ID-UMKM-6, multiple branches, taxpayers or entities | Aggregate branches and apply the owner/spouse/company rules. A legal-entity-only test is insufficient |
| R-ID-UMKM-7, foreign-source income | Apply amended art. 56(3)(b)'s tax-due/paid-abroad exclusion, while foreign business/professional turnover still enters art. 58 eligibility; ordinary foreign-tax-credit work is separate |
| R-ID-UMKM-8, rent, interest, dividends, royalties or gains | Establish the actual separate-final, exempt or ordinary treatment. Do not blanket-exclude every passive or one-off receipt without its rule |
| Employment plus qualifying business | Payroll withholding and final business tax run separately, both reported appropriately in the annual return; final tax is not a credit against salary tax |
| Voluntary PKP or later compulsory PKP | VAT is independent. Obtain registration/effective date and apply `indonesia-vat`; do not assume an unregistered small taxpayer may issue tax invoices or quote a universal invoice rate |
| PT paying its owner salary or dividends | Company final tax does not settle the shareholder's salary, dividend/reinvestment or payroll obligations; route those separately |
| Costs include bribes or gratuities | No expense is deducted from this final-tax base anyway; amended art. 20A separately bars the specified corruption/bribery payments, including foreign-public-official payments, under general income tax |
| Low-margin business considering general rates | Compare an actual ordinary-tax calculation, record keeping and the permanent opt-out consequence. No universal 5% margin breakpoint is asserted |

The operative source for the eligibility and transition entries is [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); for independent VAT/PKP and payment/certificate mechanics it is [PMK 164/2023](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

### Missing facts and safe defaults

Unknown activity stays unclassified, with the professional-service possibility flagged. Unknown turnover, household/company total or historical election means no affirmative eligibility conclusion, rather than a fabricated low-risk default. Preserve unresolved monthly amounts, exact foreign-exchange conversion, payment code, certificate and PKP facts in the workpaper. Request documents instead of assuming cash receipts, a fresh opt-out or automatic access. A calculation based on expressly supplied hypothetical inputs is permitted if its boundaries are stated; it is not a filed assessment.

## Worked cases

### Case 1. Pak Andi, individual trader crossing the untaxed portion

Retain the original online reseller's numbers, advanced to calendar 2026: January to December turnover is IDR 40m,45m,50m,55m,60m,55m,65m,70m,70m,75m,80m,85m, total 750m. Assume all is qualifying domestic business turnover, no election out, no excluded professional activity, residence and earlier eligibility established, and no connected-taxpayer disqualification. January to August total 440m. September brings cumulative turnover to 510m, so 10m is taxable; October, November and December add 75m,80m,85m. Final tax is respectively 50,000,375,000,400,000,425,000, total **1,250,000**. Each amount is reconciled to actual collection/self-payment records and the ordinary following-month due rule, not automatically deposited twice. [PP 55 art. 60](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan); [PMK 164 arts. 6-9](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

```oa-check
name: Pak Andi monthly crossing and annual reconciliation in 2026
inputs:
  january_august: 440000000
  september: 70000000
  october: 75000000
  november: 80000000
  december: 85000000
  untaxed: 500000000
  final_rate: 0.005
steps:
  - annual_turnover: january_august + september + october + november + december
  - september_base: max(january_august + september - untaxed, 0) - max(january_august - untaxed, 0)
  - september_tax: september_base * final_rate
  - october_tax: october * final_rate
  - november_tax: november * final_rate
  - december_tax: december * final_rate
  - monthly_total: september_tax + october_tax + november_tax + december_tax
  - annual_check: max(annual_turnover - untaxed, 0) * final_rate
expected:
  annual_turnover: 750000000
  september_base: 10000000
  september_tax: 50000
  october_tax: 375000
  november_tax: 400000
  december_tax: 425000
  monthly_total: 1250000
  annual_check: 1250000
```

### Case 2. PT Mawar Digital Perorangan, conditional business example

Retain the original company, incorporated March 2024, selling templates/stock photos through Etsy with total qualifying turnover 2,200m. These are hypothetical business-classification facts, not proof that every creative seller qualifies. Establish whether its founder's own professional services trigger art. 57(2)(b), the owner/company aggregation, foreign-income exclusion, prior election and any art. II(1)(f) grandfathering before using the result. If all supplies are established as qualifying business receipts, quarterly aggregates 480m,520m,560m,640m give 2.4m,2.6m,2.8m,3.2m, total **11m**. The aggregates are only a display; actual settlement is monthly. Applying an individual's allowance would incorrectly understate company tax by **2.5m**. If those eligibility facts fail, hand off to the ordinary company computation; do not present 11m as the legal answer to an unclassified Etsy statement. [PP 20 amended arts. 56-58/art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [PP 55 art. 60](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan).

```oa-check
name: PT Mawar company allowance boundary in 2026
inputs:
  q1: 480000000
  q2: 520000000
  q3: 560000000
  q4: 640000000
  final_rate: 0.005
steps:
  - total: q1 + q2 + q3 + q4
  - q1_tax: q1 * final_rate
  - q2_tax: q2 * final_rate
  - q3_tax: q3 * final_rate
  - q4_tax: q4 * final_rate
  - company_tax: total * final_rate
  - incorrect_individual_formula: max(total - 500000000, 0) * final_rate
  - understatement: company_tax - incorrect_individual_formula
expected:
  total: 2200000000
  q1_tax: 2400000
  q2_tax: 2600000
  q3_tax: 2800000
  q4_tax: 3200000
  company_tax: 11000000
  understatement: 2500000
```

### Decision case. Same shop, low versus high supported ordinary profit

For an eligible individual with qualifying annual turnover 750m and the individual untaxed portion, final tax is 1.25m. Suppose the separate ordinary-income-tax method, with all other income/allowances/credits supported, supplies ordinary tax of 0 in one option and 3m in another. The first option is 1.25m cheaper under general rates; the second is 1.75m cheaper under final tax. These supplied ordinary-tax outputs are not calculated by assuming a universal margin or PTKP here. Before choosing, record the notice timing, bookkeeping obligations and permanent future exclusion under amended art. 57(4). [PP 20/2026 amended art. 57](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0); [PMK 164/2023 art. 5](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

```oa-check
name: Conditional general-rate decision from separately established ordinary tax
inputs:
  turnover: 750000000
  untaxed: 500000000
  final_rate: 0.005
  ordinary_low: 0
  ordinary_high: 3000000
steps:
  - final_tax: max(turnover - untaxed, 0) * final_rate
  - general_saving_low: final_tax - ordinary_low
  - final_saving_high: ordinary_high - final_tax
expected:
  final_tax: 1250000
  general_saving_low: 1250000
  final_saving_high: 1750000
```

## When to refuse or refer

Retain refusal codes R-ID-UMKM-1 to R-ID-UMKM-8 above. Refer material residence/BUT, classification, acquisition/merger, incentive, foreign-tax, overlapping taxpayer or disputed grandfathering questions to a Konsultan Pajak. Do not auto-deny the supported current-year computation merely because art. 61 provides a next-year exit; explain the actual unresolved part. Never assist turnover splitting or use a company wrapper to conceal professional receipts.

Never deduct costs or losses from this gross tax, treat final payments as ordinary income-tax credits, give a company the individual allowance, ignore utilisation or aggregation, or quote an unchecked billing code. Do not mix other final-tax bases into the monthly base merely because they count toward the eligibility ceiling. An unresolved activity is not resolved by the most conservative label. A late payment or filing needs its actual date, applicable relief and official interest decision, not an estimated rate.

## Filing and payment

### Monthly evidence and settlement

1. Reconcile the qualifying business-turnover schedule for the tax period and every place of business. Keep the eligibility-ceiling schedule separate. Compute the individual's cumulative relief or the company's full base, then tie to invoices/platform sales, cash and bank receipts. [PMK 164 arts. 6-7](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).
2. For transactions subject to collection/withholding, obtain the final-tax certificate and supply its copy as required. An individual still within the untaxed portion uses the prescribed turnover statement instead. The payer issues the proper withholding evidence, including nil slips in the stated cases. Imports/purchases and threshold statements have specific exceptions in art. 8, so do not tell every payer to withhold automatically. [PMK 164 art. 8](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).
3. Reconcile tax already lawfully collected against that monthly liability. For self-payment, use authorised Coretax access at `coretaxdjp.pajak.go.id` and the official payment/billing route for the correct taxpayer, article, period and amount. Confirm the live KAP/KJS selection from the current official schedule; the old file's unconfirmed code is not an instruction here. A platform manual never grants permission to use another person's credentials. [DJP Coretax announcement](https://www.pajak.go.id/en/node/112032); [PMK 164 art. 7](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).
4. Pay the supported self-paid balance by the applicable due date. Save kode billing, BPN and validated NTPN, and match actual bank payment and taxpayer ledger. A generated billing code is not a payment. Article 7(5) provides deemed monthly filing with validated payment; record the actual validation date. The nil/no-self-payment exceptions and the withholding payer's own Unifikasi return are separate. [PMK 164 arts. 7-8](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).
5. A later finding that a threshold statement was incorrect requires the taxpayer's own settlement under art. 8(8), allocated to the transaction month; do not retain an unsupported nil position. Incorrect/overpaid final tax has art. 9's request procedure, not automatic conversion to a general-rate credit. [PMK 164 arts. 8-9](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

### Annual return and other taxes

Report gross turnover and final tax as the annual SPT attachment required by art. 9. Reconcile the annual gross, individual relief, qualifying tax, monthly self-payments, collector slips and outstanding difference. Keep final and ordinary income, assets/liabilities, salary and company-owner distributions separate. The earlier 1770 Lampiran III/1771 Lampiran IV references are historical form navigation, not certified 2026 Coretax field numbers; obtain the current official form manual before populating a field. Retain the accepted annual return and BPE, not just a draft PDF or billing receipt. [PMK 164 art. 9](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau); [KUP arts. 3,9](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [DJP Coretax announcement](https://www.pajak.go.id/en/node/112032).

A general-rate transition has PPh 25 instalment consequences under PMK 164 art. 16, including the first ordinary-tax year's special computation; route to the individual/company method rather than assume last year's final tax divided by twelve. PKP registration is a separate VAT test: PMK 164 arts. 17-18 set the year-end business-reporting route and the stated following-book-year VAT start for its cases. A voluntary earlier PKP registration requires its own effective-date analysis. Do not copy the old flat 11% sentence into every invoice. [PMK 164 arts. 16-19](https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau).

Late annual filing uses the applicable KUP art. 7 fine and exclusions; late payment uses the applicable ministerial rate and art. 9 calculation. Audit understatement is not a universal "up to 50%" add-on: obtain the exact assessment provision and notice. Keep all turnover, invoices, contracts, account statements, certificates, BPN/NTPN, billing and BPE evidence for the statutory retention period. Ordinary-tax bribery deductibility is separately barred by amended art. 20A; it never creates an expense deduction from this final turnover base. [KUP arts. 7,9,28](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PP 20/2026 art. I item 2](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

## Completion checklist

- Taxpayer, period, residence and actual business/professional classifications documented.
- Prior/current turnover, branches, owner/company and applicable spouse/minor-child aggregation reconciled.
- Earlier opt-out, certificate, incentive and original utilisation period checked; exact art. II transition identified.
- Eligibility turnover and monthly final-tax base separated; individual cumulative relief applied only where permitted.
- Both original worked scenarios retained with explicit eligibility limits, and the actual client's numbers recomputed.
- Final slips and self-payments reconciled without double payment or ordinary-income-tax credit.
- Actual billing choice, official portal, due date, payment validation and annual reporting/receipt confirmed.
- PKP, payroll, company-owner salary/dividends and general-rate instalments routed separately.
- Missing source-dependent details listed below and assigned to a qualified reviewer before filing.

## Sources

| Source and what was actually read | Official URL | Read on |
|---|---|---|
| PP 20/2026 operative art. I items 1-6, amended arts. 20A/56-58, deletion of art. 59, art. II and relevant statutory explanations. Read for professions, owner/spouse/minor-child aggregation, permanent opt-out, old-cap transitions, certificate continuity and 22 April commencement. The page's catalogue header misclassifies the instrument/date; the reproduced law's signed text and commencement are used | https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0 | 2026-11-14 |
| PP 55/2022 arts. 56-63 and 69, including former art. 59. Read for the original regime, gross received/accrued before discounts, individual relief, current-year crossing, settlement/certificates and historical period counting; superseded parts are read with PP 20/2026 | https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan | 2026-11-14 |
| PMK 164/2023 arts. 5-9,14,16-19. Read for notice timing and permanent exit, gross-base/PH-MT relief, payment/withholding/nil and deemed monthly filing, certificate cancellation, annual report/refund and PKP/instalment handoffs. Apply only where consistent with the later PP 20/2026 | https://www.pajak.go.id/id/peraturan/tata-cara-pengenaan-pajak-penghasilan-atas-penghasilan-dari-usaha-yang-diterima-atau | 2026-11-14 |
| DJP consolidated tax laws through UU 6/2023, KUP arts. 3,7,9,28 and art. 28 explanatory cash/accrual passage. Read for annual deadlines, fine exclusions, variable interest/part-month limit, payment before filing, good-faith books and retention. This is not represented as a later-law consolidated edition | https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf | 2026-11-14 |
| DJP official Coretax implementation announcement. Read for 1 January 2025 commencement, taxpayer account/payment facilities and prefilled final-withholding information; no live private portal or filing was tested | https://www.pajak.go.id/en/node/112032 | 2026-11-14 |

Not yet confirmed: current Coretax UMKM KAP/KJS and exact 2026 annual form/attachment field identifiers; current billing and any detailed marketplace-collection implementation; operative holiday-adjustment provision and period-specific relief for an actual due date; exact ministerial interest rate for a late-payment start date and assessment-specific penalties; statutory foreign-currency conversion and VAT-inclusive turnover treatment for the actual invoice; detailed foreign-source, professional-company, merger/acquisition and unusual partial-year facts; any later amendment to the cited administration provisions affecting the client's period. The old approximate interest range, reusable opt-out, automatic creator/SaaS classification and claimed three-year historical PT Perorangan cap are not usable rules. Ordinary eligibility, cumulative relief and the bounded computations above are supported by the cited law.
