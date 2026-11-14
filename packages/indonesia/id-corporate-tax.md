---
name: id-corporate-tax
description: >
  Compute calendar-2026 Indonesian resident-company income tax from books,
  fiscal adjustments, losses and credits. Covers Article 31E, listed-company
  conditions, ordinary depreciation, instalments, transfer-pricing documentation
  and the evidence required for incentives. Trigger on PPh Badan, SPT Tahunan
  Badan, Pasal 31E, PPh 25, corporate tax and fiscal reconciliation. Special
  sectors, permanent establishments and unverified facilities require separate work.
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
# Indonesia Corporate Income Tax v2.0

## Scope

> **Produced by OpenAccountants (openaccountants.com)**
>
> This skill is for informational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a licensed Indonesian tax consultant (Konsultan Pajak) before filing or acting upon.

## Rates, bands and thresholds

| Item | Calendar-2026 rule and boundary | Official source |
|---|---|---|
| Standard resident-company rate | 22% of taxable income | [Income Tax Law art. 17(1)(b)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Article 31E turnover ceiling | IDR 50,000,000,000; facility relates to income proportionate to the first IDR 4,800,000,000 of gross turnover | [Income Tax Law art. 31E](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Article 31E rate | 50% reduction of the standard rate; computed qualifying rate 11%, remaining ordinary income 22% | [Income Tax Law arts. 17(1)(b),31E](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Listed-company reduction | Three percentage points, computed rate 19%; at least 40% qualifying publicly traded shares held by at least 300 parties, each below 5%, for at least 183 calendar days, with reporting and excluded-holdings conditions | [PP 55/2022 arts. 64-65](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan) |
| Ordinary loss carryforward | Five consecutive tax years following the loss year; a separate granted facility may alter this, not a blanket pioneer-industry rule | [Income Tax Law art. 6(2)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Master/local-file revenue trigger | Related-party transactions and preceding-year gross turnover over IDR 50,000,000,000 | [PMK 172/2023 art. 16(3)](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan) |
| Master/local-file transaction trigger | Preceding-year related-party tangible goods over IDR 20,000,000,000 or each services, interest, intangibles or other category over IDR 5,000,000,000; lower-tax-jurisdiction affiliate is a separate trigger | [PMK 172/2023 art. 16(3)](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan) |
| Domestic ultimate-parent CbCR threshold | Consolidated preceding-year gross turnover at least IDR 11,000,000,000,000, including equality | [PMK 172/2023 art. 16(4)](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan) |
| Documentation availability | Master/local files within four months; CbCR within twelve months, with statement/summary and annual-return rules separate | [PMK 172/2023 arts. 17-19](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan) |
| Annual ordinary filing deadline | Four months after book-year end; calendar 2026 ordinarily 30 April 2027, before any applicable specific relief | [KUP art. 3(3)(c)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Annual extension | Notification for up to two months, supported by provisional computation and required settlement; not automatic time to pay | [KUP art. 3(4)-(5)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Late annual corporate filing | IDR 1,000,000, subject to KUP art. 7 exceptions and actual relief | [KUP art. 7](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Late-payment interest | Actual ministerial monthly rate, maximum 24 months, any part-month counted in full; no fixed approximate rate or daily proration | [KUP art. 9(2a)-(2c)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Books/supporting records | Retain ten years in Indonesia | [KUP art. 28(11)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

### Identify the return and the taxpayer

Use the actual accounting period, residence, NPWP, company type, ownership and activity. The default currency is rupiah; a permitted foreign-language/currency method needs its actual permission or applicable notice conditions. A non-calendar year is not automatically prohibited. [KUP art. 28](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

Coretax covers tax year 2025 onward, but current forms and transmission rules must be matched to the applicable period. Historical 1771 names remain search terms, not certified 2026 field numbers. This method covers ordinary resident PT income tax; final turnover tax, payroll, VAT, BUT, regulated finance, extractive contracts, Islamic finance and consolidated/group-return questions use separate methods. [PER-3/PJ/2026](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0).

Unknown turnover, ownership, expense purpose, related-party status, asset class or final-regime history stays unresolved. Never default an unknown taxpayer to a fabricated revenue band, private-use fact or related-party relationship. Preserve a document request and a labelled comparison instead.

## Ask the client first

### 2.1 Required Inputs

**Minimum viable** , Full-year financial statements (income statement, balance sheet), prior-year return where one exists (otherwise registration evidence), and confirmation of (i) turnover band, (ii) listed-company status, (iii) any tax incentive elections.

**Recommended** , General ledger, fixed-asset register, related-party transactions schedule, PPh 25 payment confirmations, eligible PPh 22/23 and foreign-credit documents, separating taxes withheld by the company from its own credits, prior-year loss carry-forward schedule.

**Ideal** , Audited statements signed by an Akuntan Publik (KAP), complete fiscal reconciliation, Master/Local File/CbCR if thresholds met, NPWP and KSWP certificates, ratified RUPS minutes.

**HARD STOP if minimum is missing.** Without financial statements and the prior-year return, no corporate computation may be produced.

## The method, step by step

## Section 3 , Tier 1 Rules (Standard Computation)

### 3.1 The 22% Standard Rate

- **Standard corporate income tax rate** , PPh Badan = 22% × PKP  _(Pasal 17(1)(b) UU PPh, as amended by UU 7/2021 (HPP))_
- **22% standard rate context** , Standard corporate income tax rate: 22% of Penghasilan Kena Pajak. In force from fiscal year 2022 (reduced from 25% by UU 2/2020; confirmed by UU HPP).  _(Pasal 17(1)(b) UU PPh, as amended by UU 7/2021 (HPP))_

### 3.2 The Small-Company Facility , Pasal 31E UU PPh

- **Small-company facility scope** , Companies with annual gross turnover (peredaran bruto) up to IDR 50,000,000,000 receive a 50% reduction of the 22% rate applied to the slice of taxable income proportional to the first IDR 4,800,000,000 of gross turnover. Effective rate on the facility slice: 11%.  _(Pasal 31E UU 36/2008 (unchanged by UU HPP); SE-66/PJ/2010)_
- **Pasal 31E formula** , Turnover ≤ IDR 4.8B:         PPh Badan = 11% × PKP IDR 4.8B < Turnover ≤ 50B:   Facility slice    = (4.8B / Turnover) × PKP Non-facility slice = PKP − Facility slice PPh Badan          = 11% × Facility + 22% × Non-facility Turnover > IDR 50B:           PPh Badan = 22% × PKP   (no facility)  _(Pasal 31E UU 36/2008 (unchanged by UU HPP); SE-66/PJ/2010)_
- **Important** , Pasal 31E applies automatically , not a discretionary election. Computed for each fiscal year independently. A company that exits the IDR 50B band loses the facility for that year.  _(Pasal 31E UU 36/2008 (unchanged by UU HPP); SE-66/PJ/2010)_
- **Interaction with final turnover tax:** Do not stack final turnover tax with Article 31E on the same income. A new ordinary PT is not among the amended ordinary eligible classes; legacy PT/CV/firma and other entities need the exact PP 20/2026 transition, while a single-founder company follows its own eligibility rules. Obtain registration and election history and use `id-pph-final-umkm`. [PP 20/2026 amended arts. 56-59 and art. II](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0).

### 3.3 Listed-Company Reduction , Pasal 17(2b)

- **Listed-company reduction conditions:** Use PP 55/2022 arts. 64-65, not repealed PP 55/2022 arts. 64-65. All qualifying-trade, holder, ownership-percentage, calendar-day and DJP-reporting conditions must hold; exclude the holdings identified by art. 65, including the specified treasury and related-party holdings. Record evidence rather than presuming every IDX listing qualifies. [PP 55/2022 arts. 64-65](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan).
- **Interaction with Article 31E:** Not yet confirmed: the exact interaction for a listed company also claiming Article 31E. The old 11%-on-one-slice/19%-on-the-other recipe was not supported by the law read. Do not use that combination; obtain an official ruling or applicable operative provision and have the reviewer resolve the computation. [Income Tax Law arts. 17(2b),31E](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PP 55/2022 arts. 64-65](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan).
- **Listed status unresolved:** Keep the rate decision open. A clearly labelled ordinary-rate comparison is possible; it is not evidence that the taxpayer is private or has lost an available facility. [PP 55/2022 arts. 64-65](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan).

### 3.4 Taxable Income (Penghasilan Kena Pajak)

- **PKP formula** , PKP = Penghasilan Bruto − Deductible costs (Pasal 6) − Tax loss carry-forward (Pasal 6(2))  _(Pasal 6(2) UU PPh)_
- **Loss carry-forward window:** Ordinary losses are carried to the five consecutive following tax years. Keep a year-by-year assessed/returned loss register and prior usage. Extended carryforward requires its own granted facility and conditions; it is not a generic tax-holiday consequence. [Income Tax Law art. 6(2)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 81/2024 art. 408(1)(d)](https://pajak.go.id/en/node/113110).

### 3.5 Fiscal Reconciliation (Rekonsiliasi Fiskal)

- **Fiscal reconciliation method** , PPh Badan is computed from the commercial profit per the financial statements, audited only where required, adjusted by: (+) non-deductible expenses under Pasal 9; (+) income previously excluded from book profit but taxable; (−) income subject to final tax (PPh Final, already separately taxed); (−) non-taxable income under Pasal 4(3); (±) timing differences (depreciation, provisions). Reported in SPT 1771 Lampiran I.  _(Pasal 9; Pasal 4(3) UU PPh)_

## Section 4 , Deductible vs Non-Deductible Expenses

### 4.1 The 3M Test , Pasal 6 UU PPh

- **3M test definition** , An expense is deductible only if incurred to obtain, collect, and maintain income (untuk mendapatkan, menagih, dan memelihara penghasilan , the "3M" test). Pasal 6(1) lists principal categories:  _(Pasal 6(1) UU PPh)_

**Pasal 6(1) categories table**

| Category | Reference |
| --- | --- |
| Direct/indirect business costs (raw materials, salaries, rent, utilities, interest, royalties, travel, waste) | Pasal 6(1)(a) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Depreciation and amortisation (Pasal 11, 11A) | Pasal 6(1)(b) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Pension contributions to funds authorised by the Minister or OJK, as applicable | Pasal 6(1)(c) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Losses on disposal of business assets | Pasal 6(1)(d) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Forex losses | Pasal 6(1)(e) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Approved domestic R&D | Pasal 6(1)(f) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Scholarship, apprenticeship, training | Pasal 6(1)(g) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Bad debts meeting Pasal 6(1)(h) conditions | Pasal 6(1)(h) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Donations under PP 93/2010 (disaster, R&D, education, sports, social infrastructure) | Pasal 6(1)(i) to (m) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

### 4.2 Non-Deductible Expenses , Pasal 9 UU PPh

- **Non-deductible expenses intro** , The following are not deductible in computing taxable income:  _(Pasal 9 UU PPh)_

**Pasal 9(1) categories table**

| Item | Reference |
| --- | --- |
| Profit distributions to shareholders (dividends, share of profit) | Pasal 9(1)(a) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Costs for personal benefit of shareholders / partners / members | Pasal 9(1)(b) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Reserves and provisions, except specific allowances for banks, leasing, insurance, mining reclamation | Pasal 9(1)(c) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Personal life/health/accident insurance premiums (subject to PMK 66/2023 BIK rules) | Pasal 9(1)(d) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Work-related benefits in kind are considered under art. 6(1)(n); former art. 9(1)(e) is deleted. Do not add them back automatically | [Income Tax Law arts. 6,9](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Excessive payments to shareholders / related parties (TP arm's-length test) | Pasal 9(1)(f) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Gifts and donations except qualifying Pasal 6(1)(i) to (m) and approved zakat | Pasal 9(1)(g) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Income tax itself (PPh Badan, PPh 25, PPh 29) | Pasal 9(1)(h) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Private living expenses of taxpayer or dependents | Pasal 9(1)(i) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Salary paid to members of a partnership, firm or CV whose capital is not divided into shares is non-deductible; a PT director is not automatically in that category | [Income Tax Law art. 9(1)(j)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Administrative sanctions and criminal fines | Pasal 9(1)(k) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

### 4.3 Benefit-in-Kind Rules , PMK 66/2023

- **Benefits in kind:** Work-related benefits may be deductible under the business-purpose test and art. 6(1)(n), while employee taxation and exceptions require the actual benefit and period. The old blanket 1 July start conflated withholding implementation with substantive treatment. Obtain benefit records and route employee withholding to `id-payroll-pph21`. [Income Tax Law arts. 4(1)(a),6(1)(n),9](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).
- **Employee exemptions:** PMK 66 arts. 4-6 distinguish meals for all staff, designated remote areas, required work benefits, government-funded benefits and specific annex categories. Annex A covers religious-holiday gifts received by all employees; other gifts have the IDR 3,000,000 annual employee limit. Sports facilities have their own IDR 1,500,000 annual limit and excluded sports; individual housing has an IDR 2,000,000 monthly employee limit while communal housing is separate. Work equipment must support the job; worship facilities must be exclusively for worship. Apply the actual entry and excess-value rule, not a universal gift exemption. [PMK 66 arts. 4-8 and annex A](https://jdih.kemenkeu.go.id/api/download/dce5daf1-d4e5-4bd1-bc4e-2c086ae33c04/2023pmkeuangan066.pdf).
- **Benefits boundary:** Document business purpose and employee category separately. An unresolved employee exemption stays unresolved; do not invent a factual conclusion for convenience.

### 4.4 Depreciation and amortisation

PMK 72/2023 replaced the old PMK 96/2009 group reference. Classify the exact asset using its annex and use date, not a generic claim that every computer, vehicle, furniture item or ship is in a particular group. [PMK 72/2023 arts. 2-7](https://www.pajak.go.id/id/peraturan/penyusutan-harta-berwujud-danatau-amortisasi-harta-tak-berwujud).

| Ordinary asset class | Life | Straight line | Declining balance | Official source [Official provision](https://www.pajak.go.id/id/peraturan/penyusutan-harta-berwujud-danatau-amortisasi-harta-tak-berwujud) |
|---|---|---|---|---|
| Non-building group I | Four years | 25% | 50% | [PMK 72 art. 2](https://www.pajak.go.id/id/peraturan/penyusutan-harta-berwujud-danatau-amortisasi-harta-tak-berwujud) |
| Non-building group II | Eight years | 12.5% | 25% | [PMK 72 art. 2](https://www.pajak.go.id/id/peraturan/penyusutan-harta-berwujud-danatau-amortisasi-harta-tak-berwujud) |
| Non-building group III | Sixteen years | 6.25% | 12.5% | [PMK 72 art. 2](https://www.pajak.go.id/id/peraturan/penyusutan-harta-berwujud-danatau-amortisasi-harta-tak-berwujud) |
| Non-building group IV | Twenty years | 5% | 10% | [PMK 72 art. 2](https://www.pajak.go.id/id/peraturan/penyusutan-harta-berwujud-danatau-amortisasi-harta-tak-berwujud) |
| Permanent building, ordinary schedule | Twenty years | 5% | Not available | [PMK 72 arts. 2,6](https://www.pajak.go.id/id/peraturan/penyusutan-harta-berwujud-danatau-amortisasi-harta-tak-berwujud) |
| Non-permanent building | Ten years | 10% | Not available | [PMK 72 art. 2](https://www.pajak.go.id/id/peraturan/penyusutan-harta-berwujud-danatau-amortisasi-harta-tak-berwujud) |

For a permanent building with a longer actual accounting life, art. 6 permits the actual-life method subject to consistency, election/notice and transition conditions. An unlisted non-building asset ordinarily uses group III unless DJP grants the permitted different grouping under art. 4. Start in the expenditure month or the construction-completion month, subject to the specific unused-asset approval rule. Improvements lasting beyond a year are capitalised under art. 7. Land and its renewal/acquisition rights need their own treatment; do not depreciate land simply because it was purchased for business. [PMK 72 arts. 1-7](https://www.pajak.go.id/id/peraturan/penyusutan-harta-berwujud-danatau-amortisasi-harta-tak-berwujud).

Intangibles, software, special industries, asset disposals, insurance recoveries, actual-life options and accelerated facility schedules remain part of the fixed-asset review. Not yet confirmed: their asset-specific classification and current amortisation/transition rule beyond the ordinary tangible provisions read here. Do not silently apply the non-building table to every licence or software purchase. The old blanket per-group binding-election assertion is not certified; keep the actual taxpayer's consistent accounting method and permissions.

## Section 5 , Tier 2 Catalogue (Reviewer Judgement Required)

### 5.1 Tax Holiday , PMK 130/2020

- **Pioneer industries:** PMK 130 art. 3 lists eighteen categories covering the specified upstream industries, infrastructure and digital data-processing/hosting activities. The actual licensed business and product must match; other industries have a separate scoring route. The list is not an approval for every business called digital. [PMK 130 arts. 3-5](https://pajak.go.id/id/peraturan/pemberian-fasilitas-pengurangan-pajak-penghasilan-badan).
- **Tax-holiday scale:** Under PMK 130 art. 2, qualifying investment at least IDR 100 billion but below IDR 500 billion receives a 50% reduction for five years, then 25% for two years. Investment at least IDR 500 billion has a 100% reduction for five/seven/ten/fifteen/twenty years according to the stated IDR 500 billion, one trillion, five trillion, fifteen trillion and thirty trillion bands, followed by 50% for two years. The old assertion of full relief from the lowest band was wrong. Obtain the actual grant, utilisation decision and commercial-production date. Not yet confirmed: a fresh 2026 application window and any current global-minimum-tax interaction; do not sell this historic scale as a currently open entitlement. [PMK 130 arts. 2-5,12](https://pajak.go.id/id/peraturan/pemberian-fasilitas-pengurangan-pajak-penghasilan-badan).
- **Conservative default** , Do not apply until the Decree of the Minister of Finance (KMK) is in hand. Reviewer must verify the KMK and commercial operation date.  _(PMK 130/2020)_

### 5.2 Tax Allowance , PP 78/2019

- **Scope and benefits:** The PP 78/2019 facility for listed business fields/regions can include a 30% net-income reduction over six years (5% per year), accelerated depreciation, a 10% foreign-shareholder dividend rate or lower treaty rate, and conditional loss extension up to ten years. Each benefit and start date must match its grant, asset schedule and conditions. [PMK 81/2024 arts. 407-418](https://pajak.go.id/en/node/113110).
- **Conservative default** , Apply only after the BKPM Decree is issued.  _(PP 78/2019)_

### 5.3 Super-Deduction R&D , PMK 153/2020

- **R&D deduction:** At most 300% TOTAL, consisting of the ordinary 100% plus at most 200% additional relief. The additional components depend on the specified patent/plant-variety, overseas-registration, commercialisation and Indonesian institutional-cooperation conditions. It is not an additional 300%. Keep costs, approved project, intellectual-property and commercialisation evidence; confirm the current application and utilisation requirements before claiming. [PMK 81/2024 art. 432](https://pajak.go.id/en/node/113110).
- **Conservative default** , Apply base 100% only. Apply super-deduction only after KMK is issued.  _(PMK 153/2020)_

### 5.4 Super-Deduction Vocational Training , PMK 128/2019

- **Vocational training:** Retain the separate enhanced-deduction review for qualifying practical work, apprenticeships and competency training. Not yet confirmed: the current qualifying agreement, OSS notification/approval route, additional deduction and utilisation cap for this taxpayer. Do not claim enhanced relief merely because a training invoice exists.

### 5.5 Investment Allowance for Labour-Intensive Industries , PMK 16/2020

- **Labour-intensive investment allowance:** Retain the specialist review for tangible investment under the labour-intensive facility. Not yet confirmed: the current eligible fields, workforce conditions, annual schedule and actual grant for this taxpayer. The old unqualified percentage schedule is not a calculation instruction until the operative law and grant are checked.

### 5.6 KEK, Free Trade Zones, Bonded Zones

- **Special zones detail** , Special Economic Zones (KEK), Free Trade Zones (Batam, Bintan, Karimun), and Bonded Zones (Kawasan Berikat) carry sector-specific PPh, PPN, PPnBM, and customs facilities under PP 12/2020 and PP 41/2021. Flag to a specialist.  _(PP 12/2020; PP 41/2021)_

### 5.7 Director Remuneration Reasonableness

- **Director remuneration deductibility** , Director / komisaris salaries are deductible if ratified by RUPS, commercially reasonable, and subject to PPh 21 withholding. Excessive remuneration may be reclassified by DJP as a deemed dividend under Pasal 9(1)(f). Flag where remuneration is materially above market.  _(Pasal 9(1)(f))_

### 5.8 Bad Debt Write-Off , Pasal 6(1)(h)

- **Bad debts:** Require commercial P&L recognition, the debtor list furnished to DJP and one of the statutory recovery/settlement/publication/acknowledgement conditions. The recovery-condition exception for the specified small debtors must also be tested, not discarded. Financial institutions may have different rules. The law does not make every uncollected invoice deductible. [Income Tax Law art. 6(1)(h)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

## Monthly PPh 25 instalments

1. Ordinary prior-year tax less eligible PPh 22/23 and permitted art. 24 foreign credits, divided by the number of months in the relevant year/part year, supplies the base. Do not deduct prior-year PPh 25 again in that formula. Employee PPh 21 is not the resident PT's own credit; PPh 26 paid as a withholding agent is not its credit either. [Income Tax Law art. 25(1)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 81/2024 arts. 226-237](https://pajak.go.id/en/node/113110).
2. Before the annual return is filed within its filing period, art. 25(2) carries forward the final instalment of the preceding year. Do not impose a universal May-to-April start when the return is filed earlier, late or under extension, amended, or an assessment intervenes. Each special case has its own rule. [Income Tax Law art. 25(2),(4),(6)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).
3. An ordinary newly registered taxpayer covered by PMK 81 art. 237 has nil instalments in its registration year. Banks, listed companies, state-owned enterprises, taxpayers required to prepare periodic statements, certain individual traders, conversions and reorganisations have separate arts. 227-236 rules. Do not impose forecast-profit instalments on every new company or extend the nil rule to those exceptions. [PMK 81 arts. 226-237](https://pajak.go.id/en/node/113110).
4. Payment is ordinarily by the following month's fifteenth, with applicable holiday relief and validated state receipt. A proposed reduction is not an automatic percentage discount; confirm the current application rule and actual DJP decision. Not yet confirmed: an individual reduction application's permitted basis, evidence and effective period. The old no-proof 25% allowance is not certified. [PMK 81 arts. 94,100](https://pajak.go.id/en/node/113110).
5. Late payment uses the minister's actual applicable monthly interest, with any part-month counting in full and the statutory cap. Never use a fixed percentage or daily proration as an estimate of the legal charge. [KUP art. 9(2a)-(2c)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

## Section 7 , Transfer Pricing

**Legislation:** Pasal 18 UU PPh; PMK 172/2023 (TP-Doc); the current **PMK 172/2023** (implementation of arm's-length principle and dispute resolution, with the actual transaction period and transition checked).

### 7.1 The Arm's-Length Principle , PKKU

- **PKKU definition** , Related-party transactions (hubungan istimewa, Pasal 18(4) UU PPh) must apply Prinsip Kewajaran dan Kelaziman Usaha (PKKU) , the Indonesian arm's-length principle. Five OECD methods (CUP, RPM, CPM, TNMM, Profit Split) plus valuation techniques for intangibles.  _(Pasal 18(4) UU PPh)_

### 7.2 Related-Party Definition , Pasal 18(4)

- **Special relationship:** Test at least 25% direct/indirect participation or common participation, direct/indirect control, or blood/marriage relationships in the straight or lateral line **one degree**. The old blood-relative second-degree statement was wrong. PMK 172 also requires the actual influence/control facts and arm's-length analysis. [Income Tax Law art. 18(4)](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 172/2023](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan).

### 7.3 Documentation Thresholds , PMK 172/2023

- **Documentation trigger:** Master/local-file thresholds use the PRECEDING tax year and require related-party transactions; lower-tax affiliate dealings are a separate limb. Apply short-year annualisation and permitted foreign-currency conversion in art. 16. Being below the documentation thresholds does not remove the arm's-length obligation. [PMK 172/2023 art. 16](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan).

**Documentation thresholds table**  _(PMK 172/2023)_

| Document | Threshold |
| --- | --- |
| **Master File & Local File** | Prior-year gross revenue > IDR 50B; OR related-party tangible-goods transactions > IDR 20B; OR related-party services / interest / royalty / other transactions > IDR 5B per category [Official provision](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan) |
| **CbCR** | Ultimate parent of a group with consolidated preceding-year revenue at least IDR 11 trillion; equality qualifies [Official provision](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan) |
| Affiliate in a jurisdiction whose statutory income-tax rate is lower than Indonesia's applicable statutory rate | Documentation required regardless of value [Official provision](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan) |

### 7.4 PMK 172/2023 Key Updates (effective 2024)

- **PMK 172/2023 updates** , Clarifies the ex-ante pricing approach (support pricing at transaction time, not retrospectively); details guidance for intangibles, intra-group services (benefit test), financial transactions, and business restructuring; confirms MAP and APA routes; reinforces secondary adjustments where retained cash is treated as a constructive dividend.  _(PMK 172/2023)_

### 7.5 Filing Mechanics

- **Master File / Local File deadline** , Must exist within 4 months after fiscal year-end; submitted on DJP request during examination; summary statement filed with SPT 1771.  _(PMK 172/2023)_
- **CbCR:** Domestic ultimate parent at the inclusive threshold prepares the report within twelve months. Foreign-parent constituent obligations have the separate art. 16(5)-(6) conditions. Art. 19 distinguishes the master/local summary with the current annual return from CbCR with the following-year return; check current portal delivery and notifications rather than treating both as the same deadline. [PMK 172/2023 arts. 16-19](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan).
- **TP disclosure** , SPT 1771 Lampiran Khusus 3A / 3A-1 / 3A-2 , discloses related-party transactions and methods used.
- **Conservative default** , If revenue > IDR 50B or any PMK 172/2023 threshold is crossed, flag TP documentation as mandatory. Treat undocumented related-party transactions as TP adjustment risk.  _(PMK 172/2023)_

## Worked cases

### Case 1. Small PT with Article 31E facility

**Facts:** PT Sumber Makmur (resident PT, fiscal year 2026 calendar).
- Gross turnover (peredaran bruto): **IDR 6,000,000,000**.
- Commercial profit before tax: IDR 1,560,000,000.
- Fiscal adjustments: + IDR 30,000,000 non-deductible entertainment (Pasal 9); + IDR 10,000,000 non-deductible private car; − IDR 100,000,000 bank interest already taxed via PPh Final.
- Tax credits: PPh 22 IDR 15,000,000; PPh 23 IDR 25,000,000; PPh 25 paid IDR 80,000,000.

### 8.1 Taxable income (PKP):

- **PKP calculation** , 1,560,000,000 + 30,000,000 + 10,000,000 − 100,000,000 = IDR 1,500,000,000

### 8.2 Apply Pasal 31E.

- **Facility/non-facility slice calculation** , Turnover sits between IDR 4.8B and IDR 50B, so the facility applies to a proportional slice: Facility slice     = (4,800,000,000 / 6,000,000,000) × 1,500,000,000 = IDR 1,200,000,000 Non-facility slice = 1,500,000,000 − 1,200,000,000                   = IDR   300,000,000

### 8.3 PPh Badan:

- **PPh Badan total calculation** , 11% × 1,200,000,000 = IDR 132,000,000 22% ×   300,000,000 = IDR  66,000,000 Total PPh Badan      IDR 198,000,000

### 8.4 PPh 29 (annual underpayment):

- **PPh 29 calculation** , 198,000,000 − 15,000,000 − 25,000,000 − 80,000,000 = IDR 78,000,000 Pay IDR 78,000,000 before filing SPT 1771, no later than 30 April 2027.

### 8.5 Following-year PPh 25:

- **Following-year monthly instalment illustration:** (198,000,000 - 15,000,000 - 25,000,000) / 12 = 13,166,666.666... before prescribed payment rounding. This is the ordinary 2027 base from the 2026 return, not a second subtraction of the 80,000,000 instalments used in annual settlement. Determine the exact effective period from actual filing/extension history. [Income Tax Law art. 25](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).



### Recomputing Case 1

The original PT's calendar-2026 turnover is 6,000,000,000, commercial profit 1,200,000,000, positive fiscal adjustments 400,000,000 and negative adjustments 100,000,000. No losses, special-sector rate, listed reduction, incentive or final-tax income is assumed. Annual eligible credits are 15,000,000 and 25,000,000; instalments paid are 80,000,000. The facility is proportional to turnover, not the first slice of profit. [Income Tax Law arts. 17,25,31E](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

```oa-check
name: Ordinary PT Article 31E and separate annual settlement
inputs:
  turnover: 6000000000
  profit: 1200000000
  addbacks: 400000000
  reductions: 100000000
  eligible_turnover: 4800000000
  facility_rate: 0.11
  standard_rate: 0.22
  pph22: 15000000
  pph23: 25000000
  instalments: 80000000
steps:
  - taxable: profit + addbacks - reductions
  - facility_slice: taxable * eligible_turnover / turnover
  - other_slice: taxable - facility_slice
  - tax: facility_slice * facility_rate + other_slice * standard_rate
  - balance: tax - pph22 - pph23 - instalments
  - next_annual_instalment_base: tax - pph22 - pph23
expected:
  taxable: 1500000000
  facility_slice: 1200000000
  other_slice: 300000000
  tax: 198000000
  balance: 78000000
  next_annual_instalment_base: 158000000
```

### Case 2. Exact ceiling and ordinary new-company boundary

Assume established ordinary-tax companies, no special income, turnover exactly 50,000,000,000 and taxable income 5,000,000,000. The facility slice is 480,000,000 and tax 1,047,200,000. At turnover 50,000,000,001 the same taxable profit has no Article 31E facility, giving 1,100,000,000. Separately, if an ordinary company is newly registered in 2026 and falls under PMK 81 art. 237, registration-year PPh 25 is nil, even if it forecasts that taxable profit; the annual liability is not erased. [Income Tax Law art. 31E](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PMK 81 art. 237](https://pajak.go.id/en/node/113110).

```oa-check
name: Inclusive Article 31E turnover ceiling
inputs:
  at_ceiling: 50000000000
  taxable: 5000000000
  facility_turnover: 4800000000
  standard_rate: 0.22
  facility_rate: 0.11
steps:
  - qualifying_slice: taxable * facility_turnover / at_ceiling
  - at_ceiling_tax: qualifying_slice * facility_rate + (taxable - qualifying_slice) * standard_rate
  - above_ceiling_tax: taxable * standard_rate
  - difference: above_ceiling_tax - at_ceiling_tax
expected:
  qualifying_slice: 480000000
  at_ceiling_tax: 1047200000
  above_ceiling_tax: 1100000000
  difference: 52800000
```

## Boundary and exception table

| Boundary | Required action |
|---|---|
| BUT, banking, insurance, oil/gas, mining contract, Islamic finance or consolidation | Separate sector method; no ordinary-PT computation presented as sufficient |
| Missing prior return because first registration | Establish actual registration and PMK 81 special/new-taxpayer category; do not require a nonexistent return or forecast instalments automatically |
| Unknown turnover, losses, credits, asset category or approval | Preserve the question and supporting-document request; a comparison with stated hypothetical assumptions is not the taxpayer's answer |
| Tax incentive or related-party arrangement | Obtain actual grant/contract, timing, applicable source and documentation; ordinary base case can be shown separately |

## When to refuse or refer

- **R-ID-CT-1** , Non-resident / Permanent Establishment (BUT). Resident PTs only. BUT under tax treaty attribution rules is out of scope. Escalate to a Konsultan Pajak.
- **R-ID-CT-2** , Sector-specific regimes. Banking, insurance, oil & gas (production sharing / cost recovery), mining contract of work, plantation contracts. Out of scope.
- **R-ID-CT-3** , Group / consolidated reporting. Out of scope.
- **R-ID-CT-4** , Tax holiday / enhanced deduction not established. Obtain the actual eligibility, application, grant or utilisation evidence required by the particular facility. Show the ordinary-law comparison separately and flag the unresolved claim.
- **R-ID-CT-5** , Arrears / SKPKB enforcement. Outstanding STP, SKPKB, SKPKBT, or active pemeriksaan. Pasal 9(2a) UU KUP monthly interest applies. Escalate immediately.
- **R-ID-CT-6** , TP controversy. Related-party disputes or active MAP/APA proceedings. Out of scope.
- **R-ID-CT-7** , Cross-skill scope. Payroll → `id-payroll-pph21`. VAT → `indonesia-vat`. PPh Final UMKM 0.5% → `id-pph-final-umkm`.
- **R-ID-CT-8** , Islamic finance (syariah banking, takaful). Specific PSAK Syariah and DJP rulings apply. Out of scope.


## What to search and what to ask next

Search this method's cited articles and the taxpayer's books, prior return, loss register, asset register, withholding slips, grant, ownership and connected-party schedule first. Request only missing facts. Resolve form-field and software-version questions from the current official Coretax manual for that return, then hand the complete reconciliation and evidence to the reviewing Indonesian practitioner. Do not submit a return or change a live ledger through this method.

## Section 9 , Filing and Payment Mechanics

### 9.1 Annual corporate return schedule map

Preserve schedules for commercial profit, fiscal adjustments, COGS and expenses, financial statements, eligible credits, final and exempt income, shareholders/directors/commissioners, investments, related-party transactions, depreciation/amortisation and loss carryforward. The old 1771-I to VI and special 1A/1B/2A/3A references are historical navigation aids only; their exact 2026 Coretax counterparts have not been confirmed. Do not place employee PPh 21 or tax withheld from a non-resident supplier in the resident company's own credit schedule. Match the actual official form before producing a filing-ready mapping. [Income Tax Law arts. 6,9,25,28,31E](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf); [PER-3/PJ/2026](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0).

### 9.2 Filing Deadlines

**Filing deadlines table**

| Item | Deadline |
| --- | --- |
| SPT 1771 (calendar year) | **30 April of the following year** [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| SPT 1771 (non-calendar FY) | Last day of the 4th month after FY-end [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Extension request | Up to 2 months under Pasal 3(4) UU KUP, with provisional payment based on reasonable estimate [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| PPh 29 (annual underpayment) | Before SPT is filed [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Monthly PPh 25 | 15th of the following month [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

### 9.3 Filing Portal , Coretax DJP

- **Coretax:** Use the current DJP channel for tax year 2025 onward. Select the actual tax year, return and submission/correction type; confirm the authorised signer, current attachments, receipt and supported channel. Do not certify old form numbers or portal screens from memory. [PER-3/PJ/2026](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0).

### 9.4 Audit and Statute of Limitations

- **Assessment and criminal time limits:** Keep the ordinary assessment, additional assessment and criminal-prosecution limits separate. Not yet confirmed: the exact exceptional time limit and procedural route for the taxpayer's facts. The old suggestion that a five-year assessment period universally becomes ten years for fraud is not certified. Keep the SP2/audit notice and SKPKB, SKPLB, SKPN or SKPKBT documents and route disputes to a specialist. [KUP assessment and criminal provisions, consolidated official text](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf).

### 9.5 Common Penalty Headings

**Common penalty headings table**

| Infraction | Sanction [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| --- | --- |
| Late filing of SPT 1771 | IDR 1,000,000 administrative fine (Pasal 7 UU KUP) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Late payment of PPh 25 / PPh 29 | Monthly interest per Menkeu rate (actual applicable rate, capped 24 months; part-month counts in full) , Pasal 9(2a) UU KUP [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| SKPKB underpayment | Tax due + monthly interest under UU HPP framework [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Incorrect return, negligence or an assessment | Identify the actual assessment/correction/criminal provision first; no universal percentage is certified [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Tax evasion | Imprisonment 6 months to 6 years + 2× to 4× tax shortfall (Pasal 39 UU KUP) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

- **Conservative default** , File on time. Pay PPh 29 before filing. Do not advise on late-filing strategies.

## Section 10 , Conservative Defaults Summary

**Conservative defaults summary table**

| Item | Default |
| --- | --- |
| Turnover band unknown | Obtain actual turnover; no final rate/facility decision on an unknown band [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Listed-company status unknown | Obtain listing and ownership evidence; show ordinary-rate comparison separately if useful [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Tax holiday / allowance unverified | Apply standard rate; flag pending application [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Related-party status unknown | Obtain ownership, control and family facts; unresolved status is flagged [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| TP documentation unknown | Test all preceding-year and lower-tax-affiliate triggers, not revenue alone [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| BIK treatment unknown | Apply business-purpose test and the actual PMK 66 benefit/exemption entry [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Expense purpose unclear | Request business-purpose evidence; no invented private-use conclusion [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Asset useful life unknown | Classify the asset under PMK 72/2023; unresolved classification stays open [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Bookkeeping currency | IDR (USD requires DJP permission) [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Tax loss carry-forward | Verify 5-year window per loss year [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

## Section 11 , Cross-References

**Cross-references table**

| Topic | Skill |
| --- | --- |
| Payroll withholding (PPh 21) | `id-payroll-pph21` [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| PPN / VAT / e-Faktur / PKP | `indonesia-vat` [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Foundation principles | `foundation` [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| Intake checklist | `intake` [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |
| PPh Final UMKM 0.5% (alternative regime) | `id-pph-final-umkm` [Official provision](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) |

When a topic crosses skills (e.g., a PPh 21 BIK question with PPh Badan deductibility impact), address both , load the relevant cross-skill before answering.

## Sources

All following readings were made on 14 November 2026. A source date is not a claim that every annex or later amendment was read.

| Official source | Read for |
|---|---|
| [DJP consolidated tax laws through UU 6/2023](https://www.pajak.go.id/sites/default/files/2023-05/SDSN%202023%207.1_0.pdf) | KUP arts. 3,7,9,28; Income Tax Law arts. 6,9,14,17,18(4),25,31E and their relevant explanations; deductions, liability, loss, credits and reporting framework Read 2026-11-14. |
| [PP 55/2022](https://www.pajak.go.id/peraturan/penyesuaian-pengaturan-di-bidang-pajak-penghasilan) | Arts. 56-65, including listed-company conditions and the earlier turnover regime Read 2026-11-14. |
| [PP 20/2026](https://www.pajak.go.id/id/peraturan/perubahan-atas-peraturan-pemerintah-nomor-55-tahun-2022-tentang-penyesuaian-pengaturan-0) | Changed final-tax eligibility, owner/household aggregation, utilisation periods and transitions; no automatic new ordinary-PT entitlement Read 2026-11-14. |
| [PMK 72/2023](https://www.pajak.go.id/id/peraturan/penyusutan-harta-berwujud-danatau-amortisasi-harta-tak-berwujud) | Arts. 1-7 ordinary tangible depreciation, groups, start date, unlisted assets, buildings and improvements Read 2026-11-14. |
| [PMK 66/2023](https://jdih.kemenkeu.go.id/api/download/dce5daf1-d4e5-4bd1-bc4e-2c086ae33c04/2023pmkeuangan066.pdf) | Arts. 2-4, transition arts. 23-24 and annex A; deduction start, benefit categories, distinct gift/sport/housing conditions and withholding transition Read 2026-11-14. |
| [PMK 130/2020](https://pajak.go.id/id/peraturan/pemberian-fasilitas-pengurangan-pajak-penghasilan-badan) | Arts. 2-5,12; investment and reduction bands, pioneer-sector scope and grant/utilisation boundaries. Fresh 2026 application entitlement is not certified Read 2026-11-14. |
| [PMK 172/2023](https://pajak.go.id/index.php/id/peraturan/penerapan-prinsip-kewajaran-dan-kelaziman-usaha-dalam-transaksi-yang-dipengaruhi-hubungan) | Arts. 16-19, prior-year thresholds, inclusive domestic-parent CbCR threshold, availability and annual reporting; other case-specific method/APA/MAP detail not recertified here Read 2026-11-14. |
| [PMK 81/2024 operative DJP text](https://pajak.go.id/en/node/113110) | Arts. 94,100,226-237 and 407-418,432: payments, instalments, investment allowance and maximum total R&D deduction. Later amendments and any taxpayer-specific incentive remain part of the separate grant check Read 2026-11-14. |
| [PER-3/PJ/2026](https://www.pajak.go.id/id/peraturan/tata-cara-penyampaian-penerimaan-dan-pengolahan-surat-pemberitahuan-0) | Current filing/receipt/processing framework, to be matched to the applicable return and supported submission channel Read 2026-11-14. |

Not yet confirmed: listed-company/Article 31E interaction; particular intangible/sector classification and actual-life/accelerated schedules; monthly ministerial interest; exact 2026 annual form fields, payment codes and instalment-reduction procedure; individual incentive eligibility and utilisation; gift/benefit exceptions; exceptional assessment/dispute limits. These are named work items, not permission to supply an old figure.


## PROHIBITIONS

- NEVER apply enhanced relief without the actual eligibility, procedural and grant/utilisation evidence required by that particular facility.
- NEVER ignore Pasal 31E when turnover ≤ IDR 50B , the facility is automatic.
- NEVER substitute current-year forecasts for the ordinary prior-year instalment basis; identify special taxpayers and permitted adjustment rules separately.
- NEVER include PPh Final income in the PPh Badan computation , reconcile it out.
- NEVER deduct income tax itself (PPh Badan, 25, 29) , Pasal 9(1)(h).
- NEVER deduct dividends , Pasal 9(1)(a).
- NEVER deduct administrative or criminal fines , Pasal 9(1)(k).
- NEVER treat related-party transactions as arm's length without supporting analysis.
- NEVER skip TP documentation when PMK 172/2023 thresholds are crossed.
- NEVER advise late filing or late payment as a strategy , the applicable interest and penalties must be computed from the actual legal provision and period.
- NEVER stack PPh Final UMKM 0.5% with Pasal 31E , they are alternative regimes.
- NEVER apply Pasal 17(2b) 19% rate without confirming the 40%/300-party/<5%/183-day conditions and the applicable DJP reporting evidence.
- NEVER present figures as definitive , always label as estimates pending reviewer sign-off.

## Disclaimer

This skill and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Indonesian Konsultan Pajak (holding a USKP certificate) before filing or acting upon. The latest verified version is maintained at [openaccountants.com](https://openaccountants.com).

## OpenAccountants footer

*OpenAccountants , open-source accounting skills for AI*
