---
name: ph-withholding
description: >
  Philippine creditable and final withholding tax for 2026, centred on resident
  professional fees. Determines the payee’s status, annual income, VAT registration,
  declaration and correct ATC before applying the 5%, 10% or 15% professional-fee
  rate. Covers other common resident EWT payments, certificates, gross-income
  reporting and tax credits, monthly and quarterly remittances, annual information
  returns, and current invoice disclosure. Distinguishes final passive-income tax
  from ordinary income-tax credits, including the CMEPA changes to deposits and
  shares. Use for a payer preparing a withholding payment or a professional
  reconciling Form 2307. Penalties require taxpayer-size and offence classification;
  nonresident payments, treaties, payroll and specialised transactions need their
  separate rules before a final filing position.
version: 1.1
jurisdiction: PH
tax_year: 2026
last_updated: 2026-11-16
depends_on:
  - ph-income-tax
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
type: computation
---

# Philippines Withholding Tax

2026 rules checked on 2026-11-16; version 1.1. Source-cited draft; computations are estimates until the responsible professional confirms the facts and filing treatment.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Scope

Use this Guide for Philippine withholding in **PHP**. Calendar-quarter remittance and annual information reporting are distinct from the payee’s annual income-tax computation. Identify whether the payment is creditable or final before selecting its form and rate. The resident professional-fee table is not a cross-border treaty table. [NIRC sections 57-58](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896); [RR 11-2018, sections 2 and 5](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf).

| Treatment | Payee and payer consequences | Authority |
|---|---|---|
| Creditable withholding tax (CWT/EWT) | Payee reports the corresponding **gross income** and substantiates the withholding credit against ordinary income tax. The amount withheld is not the payee’s final tax calculation. Payer withholds/remits and issues Form 2307. | [NIRC 58(E), amended by EOPT section 9](https://lawphil.net/statutes/repacts/ra2024/ra_11976_2024.html); [RR 11-2018, 2.58(B)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| Final withholding tax (FWT) | The applicable final tax settles that separately taxed income; do not add it to the regular taxable-income base or claim it as an EWT credit. Applicable return disclosure and special capital-gains filings still need checking. A person with only final-taxed income has the stated individual ITR exception, not a universal exemption for someone with other income. | [NIRC 57(A)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896); [RR 4-2024, section 5(C)](https://naro.law.upd.edu.ph/storage/01JT27H00Q1JABYK2R53AB4D14.pdf); [CMEPA section 4](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213) |

## Ask the client first

- Who are the payer and payee, their TINs, legal form and Philippine residence/tax status? Is there an employment relationship, nonresident recipient or treaty claim?
- What is the actual service, rental, commission or investment income, and the supported gross withholding base? Separate VAT, reimbursements and other charges before approving a base.
- What is the payee’s current-year gross income, VAT registration and cumulative payments from this payer? Obtain the COR and the applicable sworn declaration, including its receipt date.
- Is the payer a withholding agent for this payment, a designated top withholding agent, government body or joint venture? Obtain its registration/designation and taxpayer-size classification; small size alone is not a withholding exemption.
- When did the obligation become payable, when was it recorded/invoiced, and which applicable month/quarter/year does it belong to? Obtain payment, return and remittance records.
- Are there missing or corrected 2307s, prior credits, late returns, an assessment or alleged wilful conduct? Reconcile them before computing a credit, refund or penalty.

## The method, step by step

### 1. Establish the withholding obligation and its time

Confirm the payer’s withholding obligations for the actual payment; the presence of the word “consultant” on an invoice does not establish employment, the correct income category or the ATC. Professional services, non-employee director fees, contractors and designated top-agent payments have different provisions. If the recipient is an employee of the lone payer, fees within the specified professional-fee rule become supplemental compensation, subject to payroll withholding instead. [RR 11-2018, 2.57.2(A), (C) and (I)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf).

Do **not** treat a micro taxpayer as automatically exempt from creditable withholding. The published EOPT text includes a proposed micro-taxpayer exemption, but **that proviso was vetoed**; the BIR’s tax-code footnote identifies the veto. Reduced penalties for eligible micro/small taxpayers are a separate matter. [EOPT section 8, read with the BIR veto footnote 119](https://www.bir.gov.ph/tax-code?datasetCode=119&idTag=tcfn95&label=95&tab=Footnote&type=TAB+LINK); [RR 6-2024, sections 2-5](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf).

Withhold when income becomes **payable**. RR 4-2024 section 7 defines this by when the obligation is due, demandable or legally enforceable, and specifies the earlier of accrual/recording as expense or asset in the payer’s books or the seller’s invoice/adequate payable document. Do not wait mechanically for a cash transfer. EOPT’s removal of withholding as an additional expense-deductibility condition did not remove the payer’s withholding/remittance obligation. [RR 4-2024, sections 6-7](https://naro.law.upd.edu.ph/storage/01JT27H00Q1JABYK2R53AB4D14.pdf); [NIRC 58(C), EOPT section 9](https://lawphil.net/statutes/repacts/ra2024/ra_11976_2024.html).

### 2. Classify resident professional fees and apply the declaration rules

| Resident payee and condition | EWT rate on the proper gross professional-fee base | Authority |
|---|---|---|
| Individual, current-year gross income **not over PHP 3,000,000**, not VAT registered, with the required declaration/COR | **5%** | [RR 14-2018, section 2](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf); [RR 11-2018, 2.57.2(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| Individual, gross income **over PHP 3M**, **or VAT registered regardless of amount** | **10%** | [RR 14-2018, section 2](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf) |
| Individual missing the required declaration | **10%** default; a low-income assertion alone does not authorise 5% | [RR 11-2018, 2.57.2(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| Non-individual/corporate professional-fee payee, current-year gross income **not over PHP 720,000**, with required sworn statement/COR | **10%** | [RR 14-2018, section 2](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf); [RR 11-2018, 2.57.2(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| Non-individual/corporate professional-fee payee **over PHP 720,000**, or missing the required sworn statement | **15%** | [RR 14-2018, section 2](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf); [RR 11-2018, 2.57.2(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |

The **annual** threshold is not the size of one invoice. Monitor both the declaration and cumulative payments: the regulation requires the higher rate when the payment threshold is exceeded despite a declaration. Do not assume the first PHP 3 million or PHP 720,000 remains permanently protected at the lower rate. Check the required adjustment when a threshold is crossed. [RR 11-2018, 2.57.2(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf).

| Declaration or record | Use and timing | Authority |
|---|---|---|
| Annex **B-1** plus COR | Individual with multiple income payers claiming the qualifying lower rate; submit by **15 January each year** or before the initial payment, as applicable | [RR 11-2018, 2.57.2(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| Annex **B-2**, lone payer | The separate exemption rule covers individuals earning **PHP 250,000 or less from a lone income payer** with the prescribed declaration by **15 January** or before initial payment. It is not permission for every single-payer professional to claim an exemption. Check COR/registration evidence and actual income. | [RR 11-2018, 2.57.5(B)(6)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf); [RMC 50-2018, Q29-Q32](https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No%2050-2018.pdf) |
| Annex **B-3** plus COR | Non-individual estimated annual gross income not over PHP 720,000; president/managing partner executes the notarised statement by **15 January** or before initial payment | [RR 11-2018, 2.57.2(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| Payer Annex **C** and list | Payer’s reporting of declarations/CORs received: by **31 January**, or **15 days following the month** a new recipient submits the declaration | [RR 11-2018, 2.57.2(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |

The covered fee categories include licensed **CPAs, lawyers, engineers, architects, doctors and real-estate service practitioners**, entertainers, athletes, production directors/producers, insurance agents/adjusters, management/technical consultants, bookkeeping agents, other talent recipients, non-employee corporate directors, specified brokers, and independent/exclusive sales or marketing agents. Their precise ATCs differ. A professional’s **8% income-tax election** does not by itself remove EWT or change its professional-fee rate. [RR 11-2018, 2.57.2(A)(1)-(11)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf); [RMC 50-2018, Q34-Q41](https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No%2050-2018.pdf).

### 3. Use the payment-specific rule for other common EWT

The following are resident-payment categories, not a rule that every personal payer must withhold on every purchase. Specific payment rules take precedence over the residual top-withholding-agent supplier rule. [RR 11-2018, 2.57.2](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf).

| Payment category | EWT rate and boundary | Authority |
|---|---|---|
| Business-use real-property rent | **5%** of gross rental for use/possession without acquiring title/equity | [RR 11-2018, 2.57.2(B)(1)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| Business-use personal-property rent | **5%** when annual gross rent **exceeds PHP 10,000**; if accumulated/expected rent exceeds it, withhold on the entire amount. Exactly PHP 10,000 is not automatically “exceeds”; authorised financing-company financial leases have the stated exception. | [RR 11-2018, 2.57.2(B)(2)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| Certain contractors | **2%** of gross payments to covered contractors, whether individual or corporate. Check the actual 2.57.2(C) category rather than treating every independent professional as a 2% contractor. | [RR 11-2018, 2.57.2(C)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| Designated top withholding agent’s local/resident supplier of goods | **1%** under the residual supplier rule, subject to actual designation and regular/casual-purchase conditions; another specified rate can govern | [RR 11-2018, 2.57.2(I)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| Designated top withholding agent’s local/resident supplier of services | **2%** under the same residual rule and qualifications | [RR 11-2018, 2.57.2(I)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| Specified individual brokers/independent sales or marketing agents | The applicable **5%/10%** professional-fee-category rules and declaration/VAT conditions; determine the actual category/ATC | [RR 11-2018, 2.57.2(A)(10)-(11)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf); [RR 14-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf) |

The earlier reference to **RR 14-2023** is retained with its correct scope: it addresses specified **joint-venture/consortium** supplier payments and distributive shares. It is not the instrument establishing the generic professional-fee 5%/10% table. For that use **RR 14-2018**. No additional joint-venture rate is calculated here. [RR 14-2023, sections 1-2](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2023.pdf); [RR 14-2018, section 2](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf).

### 4. Issue, collect and reconcile Form 2307 and invoice disclosure

The withholding agent issues **Form 2307** for CWT and **Form 2306** for FWT. Under RR 11-2018 2.58(B), furnish the statement within **20 days after quarter-end**, or simultaneously with the income payment if the payee requests it. Obtain every payer’s certificate and reconcile monthly payments, quarterly totals, payer/payee names and **TINs**, period, income category/**ATC**, gross income and tax withheld. A corrected certificate must replace the erroneous one; never claim both for the same income/payment period. [RR 11-2018, section 5, 2.58(B)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf); [RR 14-2018, correction/no-double-use provisions](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf).

| Professional-fee ATC | Current category | Rate | Authority |
|---|---|---|---|
| **WI010** | Individual qualifying lower-rate professional fee | **5%** | [RMO 38-2018, page 2, modified/new columns](https://bir-cdn.bir.gov.ph/local/pdf/RMO_No.38-2018.pdf) |
| **WI011** | Individual higher-rate professional fee, including VAT registration regardless of amount | **10%** | [RMO 38-2018, page 2](https://bir-cdn.bir.gov.ph/local/pdf/RMO_No.38-2018.pdf); [RR 14-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf) |
| **WC010** | Corporate qualifying lower-rate professional fee | **10%** | [RMO 38-2018, page 2](https://bir-cdn.bir.gov.ph/local/pdf/RMO_No.38-2018.pdf) |
| **WC011** | Corporate higher-rate professional fee | **15%** | [RMO 38-2018, page 2](https://bir-cdn.bir.gov.ph/local/pdf/RMO_No.38-2018.pdf) |

These correct the prior WI100/WI010 and WC100/WC010 pairings. The table is for the identified professional-fee category; a bookkeeping agency, entertainer, insurance agent or sales agent may need a different ATC even where its rate is the same. Do not select an ATC from the percentage alone. [RMO 38-2018, category tables](https://bir-cdn.bir.gov.ph/local/pdf/RMO_No.38-2018.pdf).

The payee reports the corresponding **gross income**, then substantiates the withholding credit. Missing Form 2307 requires recovery/correction and evidence of the actual withholding; do not invent the certificate or claim a duplicate credit. EOPT 58(E) requires both the income declaration and proof of withholding, and permits the stated later-period credit where the corresponding income was reported. The old absolute statement that a missing certificate automatically extinguishes every possible credit is too broad. The applicable ITR attachment/SAWT and electronic submission instructions must also be followed; RMC 20-2026 concerns **2025 income filed in 2026**, not an unissued future filing cycle. [EOPT section 9, NIRC 58(E)](https://lawphil.net/statutes/repacts/ra2024/ra_11976_2024.html); [BIR RMC 20-2026](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%2020-2026.pdf).

**Current invoice change:** RR **6-2026** requires applicable CWT to appear as a **separate invoice item**. Existing unused/unissued invoices may be consumed with **“Less: Withholding Tax”** conspicuously stamped; newly printed invoices must reflect that phrase before use. This documents the deduction; it does not replace Form 2307 or change the tax base/rate. [RR 6-2026, sections 2-3](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%206-2026.pdf).

### 5. Remit on the correct monthly, quarterly and annual calendar

Annual-reporting correction credit retained: **Corrected by Jonathan I. Ruiz (CPA, Philippines)**.

| Form/report | Purpose and ordinary deadline | Authority |
|---|---|---|
| **0619-E** | CWT remittance for **months 1 and 2 of each calendar quarter**. Non-eFPS: **10th of the following month**; eFPS: applicable industry-group due date, **on or before the 15th**. Check the actual group/date and current extension. | [BIR RMC 73-2018, official digest](https://bir-cdn.bir.gov.ph/local/pdf/RMC%2073-2018.pdf) |
| **1601-EQ + QAP** | Calendar-quarter EWT return and Quarterly Alphalist of Payees: **last day of the month after quarter-end**. Include monthly details/quarter totals and reconcile earlier 0619-E remittances; do not pay them twice. | [RR 11-2018, 2.58(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| **1604-E + annual alphalist** | Annual CWT information return: **on or before 1 March of the following year**. It is not the 31 January final-tax or compensation annual return. | [RR 11-2018, 2.58(C)(1)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| **0619-F** | First two calendar-quarter months’ final-tax remittance, with the corresponding non-eFPS/eFPS timetable; use the correct final-tax type/ATC | [BIR RMC 73-2018, digest](https://bir-cdn.bir.gov.ph/local/pdf/RMC%2073-2018.pdf) |
| **1601-FQ + QAP** | Other final withholding taxes: **last day of the month after quarter-end**. Bank-deposit interest/fringe-benefit and capital-gains transactions have their specific forms; do not route every final tax through 1601-FQ. | [RR 11-2018, 2.58(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |
| **1604-F + annual alphalist** | Annual final-tax information return: **31 January of the following year** | [RR 11-2018, 2.58(C)(2)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) |

Use the required electronic filing system and pay through an authorised route. The EOPT implementing regulation generally requires electronic filing, with manual filing when electronic platforms are unavailable under the applicable instructions; do not recycle RR 11-2018’s older exclusive RDO/bank-venue wording as the current rule. Keep filing acknowledgements, payment confirmations, alphalists, certificates and corrections together. Ordinary dates above remain subject to applicable weekend/holiday rules and a specifically issued extension; check the BIR calendar/advisory for the actual filing rather than inventing a future special extension. [RR 4-2024, filing/payment provisions and official digest](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%204-2024%20%28final%29.pdf); [EOPT section 9](https://lawphil.net/statutes/repacts/ra2024/ra_11976_2024.html).

### 6. Apply final-tax rates only to the matching recipient and income

The following personal passive-income table is for **Philippine-source income of a citizen or resident alien**, unless the row states otherwise. Corporate recipients and nonresident aliens have different rules; the domestic-individual 10% dividend rate is not a universal dividend rate. Investment income that is business income rather than passive income needs its own classification. [CMEPA sections 4-7](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213); [BIR RR 21-2025 official digest, individual table](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2021-2025%20Digest.pdf).

| Income | Rate, base or exception | Authority |
|---|---|---|
| Bank-deposit/deposit-substitute/trust interest or yield | **20%**, any currency and regardless of tenure under the current CMEPA rule from **1 July 2025**; review the grandfathered instrument exception separately | [CMEPA sections 4 and 28](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213); [RR 21-2025 digest](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2021-2025%20Digest.pdf) |
| Long-term deposit/investment | **No blanket exemption merely because the term exceeds 5 years.** Pre-1 July 2025 instruments can retain the prevailing issuance-date treatment for the remaining maturity if the statutory transition conditions are met; renewal/replacement/alteration requires fresh analysis. | [CMEPA section 28](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213); [RR 21-2025 digest, transition](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2021-2025%20Digest.pdf) |
| Passive royalties on books/literary works/musical compositions | **10%** | [CMEPA section 4, NIRC 24(B)(5)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213) |
| Other passive royalties | **20%** | [CMEPA section 4](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213) |
| Prizes **over PHP 10,000** | **20%**; prizes of PHP 10,000 or less instead enter the applicable graduated-income analysis | [CMEPA section 4, 24(B)(1)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213) |
| PCSO/lotto winnings **over PHP 10,000** | **20%**; PCSO/lotto winnings of PHP 10,000 or less are exempt. Other winnings do not inherit that specific exemption. | [CMEPA section 4](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213) |
| Cash/property dividends from a domestic corporation | **10%** for this citizen/resident-alien table; classify other recipients separately | [CMEPA section 4, 24(B)(2)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213) |
| Net capital gain on shares not traded through a local/foreign stock exchange | **15%** on the net gain, within the applicable residence/source rule. It is not 15% of gross sale proceeds; exchange-traded transactions use their separate regime. | [CMEPA section 4, 24(B)(3)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213) |
| Qualifying Philippine real property held as a capital asset | **6%** of the statutory presumed-gain base, generally the higher of gross selling price and statutory fair market value, subject to applicable exemption/election rules. Ordinary business property is a different case. | [NIRC original 24(D)(2), retained/renumbered by CMEPA 24(B)(4)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896); [RR 21-2025 digest, individual table](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2021-2025%20Digest.pdf) |

Do not include separately final-taxed passive income in the regular tax base or deduct FWT as an ordinary EWT credit. A capital-gains tax can require the seller’s separate transaction return rather than a generic payer certificate/1601-FQ; identify the transaction before filing. Treaty and nonresident rates require the recipient’s status and the applicable treaty evidence, not the resident fee table. [NIRC sections 57-58](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896); [RR 11-2018, 2.58(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf); [CMEPA sections 4-7 and 13](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213).

### 7. Classify a compliance failure before computing penalties

Penalty correction credit retained: **Corrected by Jonathan I. Ruiz (CPA, Philippines)**. The former blanket **25% surcharge/12% interest** table needs the EOPT micro/small distinction. RR 6-2024 defines micro as annual gross sales **below PHP 3,000,000**, small as **PHP 3,000,000 to below PHP 20,000,000**. Confirm the recorded classification, applicable period and offence before quoting an assessment. [RR 6-2024, sections 2-5](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf); [EOPT section 45](https://lawphil.net/statutes/repacts/ra2024/ra_11976_2024.html).

| Failure or condition | Applicable treatment and limit | Authority |
|---|---|---|
| Failure to withhold or remit | Reconcile the underlying tax/withholding-agent liability and the actual due date; late-payment civil penalties/interest depend on the applicable trigger and category. Do not present all additions as automatic or substitute a flat information-return fee for tax due. | [NIRC sections 248, 251 and 255](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896); [EOPT section 45](https://lawphil.net/statutes/repacts/ra2024/ra_11976_2024.html) |
| Ordinary late filing/payment with tax due | General section 248(A) surcharge **25%**; eligible micro/small ordinary default **10%** under RR 6-2024. Check its timely-original-return amendment and assessment qualifications. | [NIRC 248(A)](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896); [RR 6-2024, section 3](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf) |
| Interest on unpaid tax | General current benchmark **12% per annum**; qualifying micro/small **6%**, a 50% reduction. Apply the proper period/base; deficiency and delinquency interest cannot run simultaneously for the same period. The pre-TRAIN blanket 20% is not the 2026 rule. | [TRAIN section 75, NIRC 249](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html); [RR 6-2024, section 4, 6% as 50% of statutory rate](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf) |
| Failure to file/supply a required information return, list or statement, including the applicable 1604-E obligation | General section 250 **PHP 1,000 per failure**, annual aggregate cap **PHP 25,000**; qualifying micro/small **PHP 500**, cap **PHP 12,500**, subject to its notice/demand and reasonable-cause rules. | [NIRC 250](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896); [RR 6-2024, section 5](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf); [official BIR digest](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%206-2024%20%28final%29.pdf) |
| Missing Form 2307 | Correct/issue the required statement; classify the actual information-statement violation and taxpayer-size rules. The former universal PHP 1,000 statement is not an unconditional all-taxpayer assessment. | [RR 11-2018, 2.58(B)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf); [NIRC 250](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896); [RR 6-2024, section 5](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf); [official BIR digest](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%206-2024%20%28final%29.pdf) |
| Wilful non-filing or false/fraudulent return | The **50%** section 248(B) surcharge is distinct from an ordinary late return; potential section 255 criminal liability requires its statutory elements. Do not label every late filer fraudulent. | [NIRC 248(B), 255](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896); [RR 6-2024, section 3](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf) |

An actual **1601-EQ remittance return with tax due** is not resolved by paying a flat PHP 1,000 information-return penalty. Conversely, an annual information return is not automatically a tax-underpayment calculation. Resolve missing returns, tax, payments and period-specific extensions, then obtain a supported assessment and Philippine professional review. RR 21-2018 was the historical interest reference in the earlier Guide; its full text was blocked here, so the current statement above uses the read TRAIN provision and RR 6-2024, not an unread claim of having reviewed RR 21-2018.

## Worked cases

Each case assumes a resident payee, a payer with the required withholding obligation, a correctly established professional-fee withholding base, no employment relationship, and no separate VAT/reimbursement calculation. The figures estimate **withholding and cash paid**, not the payee’s final income-tax liability. [RR 11-2018, 2.57.2(A)](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf); [RR 14-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf).

### A. CPA’s PHP 100,000 fee: declaration versus default

The CPA is **not VAT registered**, has annual gross income below **PHP 3 million** and more than one payer. If the payer holds the timely valid **B-1/COR**, **5% × PHP 100,000 = PHP 5,000** is withheld and cash paid is **PHP 95,000**. The CPA reports PHP 100,000 gross and substantiates the PHP 5,000 CWT credit. If the same payer has no required declaration, **10% = PHP 10,000** is withheld and cash paid is **PHP 90,000**. The **PHP 5,000 cash difference** is a withholding-timing difference; it does not prove the CPA owes PHP 5,000 more final tax. A VAT-registered CPA would use 10% regardless of the below-PHP-3-million assertion. [RR 14-2018, section 2](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf); [RR 11-2018, declaration/default provisions](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf).

```oa-check
name: CPA fee with valid declaration versus missing declaration
inputs:
  fee_base: 100000
steps:
  lower_withholding: fee_base * 0.05
  lower_cash: fee_base - lower_withholding
  default_withholding: fee_base * 0.10
  default_cash: fee_base - default_withholding
  cash_difference: lower_cash - default_cash
expected:
  lower_withholding: 5000
  lower_cash: 95000
  default_withholding: 10000
  default_cash: 90000
  cash_difference: 5000
```

### B. Corporate accounting firm: test annual income, not the invoice

A resident **corporation**, rather than a general professional partnership distributing to partners, invoices a supported fee base of **PHP 500,000**. Its annual gross income **exceeds PHP 720,000**. Professional-fee EWT is **15% × PHP 500,000 = PHP 75,000**; cash paid is **PHP 425,000**. A valid low-income statement cannot override the known higher annual income. If an otherwise qualifying corporate payee instead had annual gross income not exceeding PHP 720,000 and the required B-3/COR, the 10% alternative on the same hypothetical base would withhold PHP 50,000, leaving PHP 450,000. The decision therefore needs the annual-income evidence before selecting the rate. [RR 14-2018, section 2](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf); [RR 11-2018, corporate sworn statement/default](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf).

```oa-check
name: Corporate professional fee and annual-income classification
inputs:
  fee_base: 500000
steps:
  higher_withholding: fee_base * 0.15
  higher_cash: fee_base - higher_withholding
  qualifying_lower_withholding: fee_base * 0.10
  qualifying_lower_cash: fee_base - qualifying_lower_withholding
  withholding_difference: higher_withholding - qualifying_lower_withholding
expected:
  higher_withholding: 75000
  higher_cash: 425000
  qualifying_lower_withholding: 50000
  qualifying_lower_cash: 450000
  withholding_difference: 25000
```

## When to refuse or refer

- Do not ignore or fabricate Form 2307. Recover/correct missing evidence, reconcile gross income and the actual tax withheld, and prevent duplicate credits.
- Do not apply the lower fee rate without the required declaration/COR or despite disqualifying VAT/annual-income facts. A single payer alone does not establish the B-2 exemption.
- Do not combine final-taxed income with the ordinary tax base or claim FWT as CWT. Follow any separately required disclosure or transaction return.
- Do not confuse CWT with FWT, apply a resident rate to a nonresident recipient, or choose an ATC only because the rate looks familiar. Refer treaty/foreign-source or specialised cases for their specific analysis.
- Do not skip monthly 0619-E/0619-F remittance because a quarterly return will follow; reconcile both rather than paying twice.
- Do not call an estimate a definitive tax bill, assert a micro withholding exemption, or use a universal penalty percentage. Obtain the facts, current filing instructions and responsible Philippine professional’s review.

## Sources

| Source | Read date | Read for |
|---|---|---|
| [RR 11-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2011-2018.pdf) | 2026-11-16 | Read for: section 2’s 2.57.2(A)-(C), (I), professional categories/declarations, rentals, contractors and residual top-agent rules; 2.57.5(B)(6) lone-payer exemption; section 5’s 2.58(A)-(C) forms/certificates/deadlines. Selected provisions, not all payroll rules. |
| [RR 14-2018](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2018.pdf) | 2026-11-16 | Read for: full two-page operative text, VAT-registered individual 10% regardless of amount, corporate rates and certificate corrections/no double use. April 2018 transitional dates are not generic current filing deadlines. |
| [RMO 38-2018](https://bir-cdn.bir.gov.ph/local/pdf/RMO_No.38-2018.pdf) | 2026-11-16 | Read for: page 2 modified/new professional ATC table, visually checked; other listed categories require their own ATC rather than a guessed WI/WC code. |
| [RMC 50-2018](https://bir-cdn.bir.gov.ph/local/pdf/RMC%20No%2050-2018.pdf) | 2026-11-16 | Read for: Q29-Q32 registration/lone-payer context and Q34-Q41 director, contractor, professional/declaration and 8%-election clarification. Scanned/OCR text, selected Q&A only. |
| [RMC 73-2018, official digest](https://bir-cdn.bir.gov.ph/local/pdf/RMC%2073-2018.pdf) | 2026-11-16 | Read for: entire one-page digest, first two months’ 0619-E/F use and non-eFPS/eFPS dates. Not misrepresented as the complete underlying circular. |
| [Original NIRC, RA 8424](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/3896) | 2026-11-16 | Read for: sections 57-58 framework, original 24(D)(2) real-property capital gain base, and sections 248/250/251/255. Read with later amendments; old 20% interest and old venue/timing are not treated as current. |
| [RA 11976](https://lawphil.net/statutes/repacts/ra2024/ra_11976_2024.html) and [BIR tax-code veto footnote 119](https://www.bir.gov.ph/tax-code?datasetCode=119&idTag=tcfn95&label=95&tab=Footnote&type=TAB+LINK) | 2026-11-16 | Read for: EOPT sections 8-9 and 45; actual BIR indexed footnote identifies the vetoed micro-taxpayer withholding proviso. Dynamic footnote page did not expose its full body on direct fetch; no exemption inferred from the unqualified statute mirror. |
| [RR 4-2024, ONAR official copy](https://naro.law.upd.edu.ph/storage/01JT27H00Q1JABYK2R53AB4D14.pdf); [BIR digest](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%204-2024%20%28final%29.pdf) | 2026-11-16 | Read for: full official digest and visually read pages 3-4, sections 4-8, especially payable timing and continuing withholding obligation. Complete five-page scan downloaded; other page detail is not claimed read. |
| [RR 6-2024, ONAR official copy](https://naro.law.upd.edu.ph/storage/01JT28JRH6YRBG857QWTQ0JJFH.pdf); [BIR digest](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%206-2024%20%28final%29.pdf) | 2026-11-16 | Read for: all three pages visually read and entire official digest, micro/small sales boundaries, ordinary/fraud surcharge, interest, information-return fine/cap, prospective application and effectivity. |
| [RR 6-2026](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%206-2026.pdf) | 2026-11-16 | Read for: both pages visually read, applicable CWT invoice item, stamp/new-print transition and effectivity. The signed circular was reached from the BIR’s official press-release link. |
| [TRAIN, RA 10963](https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html) | 2026-11-16 | Read for: section 75 replacing NIRC 249 interest, double legal rate and no simultaneous deficiency/delinquency interest. |
| [CMEPA, RA 12214](https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/99213); [RR 21-2025 official digest](https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%2021-2025%20Digest.pdf) | 2026-11-16 | Read for: CMEPA sections 4-7, 13 and 28; individual/corporate passive-income tables and full transition paragraphs in the digest. Full RR 21-2025 was blocked; only the identified digest is claimed. |
| [RR 14-2023](https://bir-cdn.bir.gov.ph/local/pdf/RR%20No.%2014-2023.pdf) | 2026-11-16 | Read for: both scanned pages visually read, joint-venture supplier payments and distributive-share scope. It is not generic professional-fee authority. |
| [RMC 20-2026](https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%2020-2026.pdf) | 2026-11-16 | Read for: first page visually read and entire official digest, forms/electronic filing and the 2025-income/2026-filing scope. No future-cycle date inferred. |

Not yet confirmed:

The older references to **RMO 23-2018** for the 8% election and **RR 21-2018** for interest are preserved for recovery; their complete operative texts were not read in this review. The Guide uses the independently read professional-fee rules, TRAIN and RR 6-2024 for the statements made above. Special nonresident/treaty rates, all-industry ATCs, VAT/reimbursement adjustments to a fee base, transaction-specific electronic filing attachments and a full penalty/compromise assessment require their own current primary evidence before calculation.
