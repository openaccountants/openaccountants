---
name: in-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their India tax returns AND mentions freelancing, self-employment, contracting, professional services, or independent practice. Trigger on phrases like "help me do my taxes", "prepare my ITR", "I'm self-employed in India", "I'm a freelancer in India", "do my taxes as a consultant", "prepare my income tax return", or any similar phrasing where the user is an India-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the India self-employed tax workflow -- every other skill in the stack (india-gst, india-income-tax, in-advance-tax, in-tds-freelance, in-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. India full-year residents only; self-employed individuals and professionals only.
version: 0.3
jurisdiction: IN
tax_year: 2026
last_updated: 2026-11-22
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: filing-howto
---

# India intake for freelancers and professionals: residence, presumptive income (44ADA/44AD), regime, advance tax, TDS and GST (Tax Year 2026-27, with AY 2026-27 returns)

## Scope

- This skill is the intake step for a resident individual in India who earns freelance, consulting, contract or professional income as a sole proprietor. It collects the facts and documents, screens out cases it cannot handle, and fixes the decisions that change the whole computation: the year, residence, regime, presumptive or actual profit, and the ITR form. It does not compute tax.
- For the tax computation itself (slabs, rebate, surcharge, deductions, interest), use the **india-income-tax** skill. For residence and RNOR tests, use the **in-tax-residency** skill. This skill does not repeat them.
- **Two periods are live. Fix the period from the documents before asking anything else.**
  - **Tax Year 2026-27** (1 April 2026 to 31 March 2027) is the current year. It is governed by the Income-tax Act, 2025. The portal says: "The 1961 Act stands repealed on the 01.04.2026." Income "earned during FY 2026 -27 onwards ... will be referred to as Tax Year 2026-27 under the Income Tax Act ,2025." Intake for this year is about advance tax, TDS on current receipts and records.
  - **AY 2026-27** (income of FY 2025-26, 1 April 2025 to 31 March 2026) is the return being filed or chased now. It stays under the Income-tax Act, 1961 and the old ITR forms. See "AY 2026-27 returns (FY 2025-26), dated 25 September 2026" below.
- **Regime default.** The new tax regime is the default for individuals ("new tax regime the default tax regime", [Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession)). Under the 2025 Act "the new tax regime is provided under section 202" ([objective and scope FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq)). For the 2025-2026 filing cycle, an opt-out by a business/profession taxpayer uses Form 10-IEA on time. For Tax Year 2026-27, use s.202(4) and rule 136: the option/withdrawal is in the timely return itself, not an assumed replacement separate form. [s.202(4)](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [rule 136](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).
- Out of scope, refer: non-residents and RNORs; HUFs, firms, LLPs and companies; tax audit cases; clients with capital gains beyond the ITR-4 limit, foreign income or assets; GST computations (see the GST note below).
- Currency is Indian rupees in Indian grouping (₹12,00,000 is INR 1,200,000 (unit conversion, derived)).
- **GST note.** This intake asks the GST questions and hands them to the existing india-gst skill. It states no GST rate, threshold or deadline; the GST computation and export/composition/credit analysis remain a separate review. The old version's arbitrary restriction on citing GST official sites is removed.

## Ask the client first

Sources: [ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs) and [Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession).

Ask these in one or two batches. Anything already visible in the documents is confirmed, not re-asked. The old form/section labels in this question list refer to the 2025-2026 filing cycle; map current-year decisions through the current answer table below.

**Blocking screen (a failed in-scope condition ends this intake):**

1. **Which year?** Tax Year 2026-27 (current, 2025 Act), AY 2026-27 (FY 2025-26 income, 1961 Act), or both.
2. **Residence for that year.** Days in India in the year, days in the four and seven preceding years, citizenship or Indian origin. If the client may be non-resident, RNOR or deemed resident, stop and use the in-tax-residency skill. ITR-4 "cannot be filed by" a person who "is a Resident but Not Ordinarily Resident (RNOR), or Non-Resident Indian".
3. **Structure.** Does the client invoice in their own name under their own PAN (sole proprietor)? HUF, partnership firm, LLP or company: stop and refer.
4. **PAN and Aadhaar.** No PAN: stop and obtain one. If PAN is unlinked, check the linking requirement and any exemption. An inoperative PAN can trigger higher withholding. For AY 2026-27 check the conditions for deductor relief in [CBDT Circular 9/2025](https://www.incometaxindia.gov.in/documents/20117/6507196/Circular-9-2025.pdf/c93e8e33-6029-c652-9fe7-abc9f8b021cd?t=1762868920211&version=1.0). For Tax Year 2026-27 apply [rule 162(3)(c)](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf#page=130) and s.397(2). Check the applicable rule with the deductor and resolve the account status before filing. [Link Aadhaar](https://www.incometax.gov.in/iec/foportal/help/how-to-link-aadhaar)

**Scope questions:**

5. **What exactly is the work?** Name the service. Is it one of the specified professions (legal, medical, engineering or architectural, accountancy, technical consultancy, interior decoration, or a profession notified by CBDT), or a business (trading, reselling, agency, commission, content or platform work that is not a listed profession)? For the older cycle this distinguishes 44ADA from 44AD; current-year equivalents are s.58(2) serial 3 and serial 1. Current s.62(4) expressly includes information technology and company secretary as well as the listed professions.
6. **Gross receipts for the year**, and how much came in cash as opposed to bank transfer, cheque, draft or other electronic mode.
7. **Age at any time in the year**: below 60, 60 to below 80, or 80 or more.
8. **Regime history.** Which regime was used last year? Has the client ever filed Form 10-IEA to opt out of the new regime, and have they already used the one-time switch back?
9. **Presumptive history.** Which ITR was filed last year (ITR-3 or ITR-4), and under which section (44AD or 44ADA)?
10. **ITR-4 bars.** Director in a company? Unlisted equity shares at any time in the year? Short-term capital gains, or s.112A long-term gains above ₹1,25,000? Any foreign asset, foreign signing authority or foreign income? Any loss brought forward or to carry forward? More than two house properties? Total income above ₹50 lakh? For the 2025-2026 filing cycle any "yes" rules out ITR-4 ([Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession)).
11. **GST.** Is the client registered (GSTIN), regular or composition? Do they invoice clients outside India?
12. **Other income.** Salary, savings or deposit interest, rent, dividends, capital gains.

**Documents to request in one go** (list from the [ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs), "documents do I need to file ITR-4", plus business records):

- Bank statements for every account used for the work, for the whole year.
- Sales invoices issued, and purchase invoices or receipts for expenses (needed only if actual profit is being considered).
- If actual profit is being considered: equipment and other assets bought in the year (invoices and dates; potential capital items), and last year's depreciation schedule with the written-down value of each asset block. This skill states no depreciation rate; the reviewer applies it.
- For AY 2026-27, download Form 26AS and AIS from the e-Filing portal. For Tax Year 2026-27, download [Form 168](https://www.incometaxindia.gov.in/tax-services/process-annual-tax-statement-e-filing-form-26as-form-168).
- For the 2025-2026 filing cycle, Form 16A from each client that deducted TDS ("a Tax Deducted at Source (TDS) Certificate issued quarterly", [Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession)), and Form 16 if there was also salary.
- Challans for advance tax and self-assessment tax.
- Last year's ITR and acknowledgement, and any Form 10-IEA acknowledgement from the older-Act regime history. For current-year TDS collect the applicable certificate/statement too; do not rename an older certificate without the period mapping.
- GST returns filed and the GST registration certificate, if registered.
- Old-regime proofs only if the old regime is in play: life insurance, provident fund, pension (NPS) and health insurance premiums, rent receipts and Form 10BA for 80GG, home-loan interest certificate.
- Any notice or letter from the Income Tax Department.

If the client does not know what they have, point them to the e-Filing portal (Form 26AS and AIS or Form 168 for the relevant period, filed returns and challans), their bank's net banking (statements), email searches for "invoice", "TDS", "ITR" and "challan", and last year's accountant.

## The method, step by step

Sources: [ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs), [Tax Payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq).

1. **Fix the year and the Act.** Label every figure and document with its year. FY 2025-26 income is AY 2026-27 (1961 Act). Income from 1 April 2026 is Tax Year 2026-27 (2025 Act). A challan paid for the wrong year credits the wrong year.
2. **Run the blocking screen** (questions 1 to 4). Stop cleanly on any refusal: state the reason in one sentence and the kind of professional to see.
3. **Read the documents before asking anything else.** From the bank statements, total the receipts from clients and split them into cash deposits and bank or electronic receipts. Exclude own-account transfers, loans, income-tax refunds and GST refunds. Separate salary and interest from business receipts.
4. **Gross up receipts for TDS.** Reconcile each invoice to the gross amount settled, including TDS withheld. On the cash basis, a part-payment only settles part of the invoice. On the mercantile basis, check when the income accrued. Use the regularly employed method and check any notified standards under [1961 Act s.145](https://www.incometaxindia.gov.in/w/section-145-9) or [2025 Act s.276](https://egazette.gov.in/WriteReadData/2025/265620.pdf#page=314). Match the TDS separately for each deductor using Form 26AS and AIS for AY 2026-27, or Form 168 for Tax Year 2026-27. Ask the deductor to investigate and correct a missing entry. [Tax Credit Mismatch FAQ](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/Tax%20Credit%20Mismatch%20-FAQ) · [TDS compliance FAQ Q24–26](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tds-compliance)
5. **Read the annual information statement.** Check TDS and TCS, specified financial transactions, tax payments, demands, refunds and other reported information. Ask the client about unexplained entries. Use AIS for AY 2026-27 and Form 168 for Tax Year 2026-27. [Tax Payments FAQ Q23](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq)
6. **Classify the work** as a specified profession (old 44ADA; current s.58 serial 3) or an eligible business (old 44AD; current s.58 serial 1), using the client's own description and the invoices. If the service is not clearly on the specified list, do not assume 44ADA; flag it (see the boundary table). If the client has both professional and business income, record each stream separately (receipts, cash part, section) and flag it for the reviewer.
7. **Test presumptive eligibility.** Compare gross receipts to the limit, using the cash share to pick the limit. Check the ITR-4 bars. If eligible, record presumptive versus actual-profit choice and separately test form eligibility: presumptive income can appear in ITR-3 when ITR-4 is barred. Record the choice and the prior-year choice.
8. **Fix the regime.** Apply the period-specific opt-out rule below: old Form 10-IEA for the older cycle; current s.202(4)/rule 136 in the timely return, taking account of a saved prior option. Check whether the one-time switch back has been used. The comparison itself is done with the india-income-tax skill.
9. **Check advance tax paid** against the rule for the client's case (presumptive serial 1/3: all by 15 March; others, including goods-carriage serial 2: four instalments). Reconcile dates and amounts against challans and the statement for the relevant year.
10. **Fill the gaps** that the documents cannot answer: private use of phone and internet, home office, other income, old-regime deductions, anything unclear in AIS. For Tax Year 2026-27, the evolved annual statement is Form 168, as the transition FAQ explains; keep old AIS/26AS records for the older period.
11. **Show one summary** of everything found and decided, with open flags, and ask the client to correct it. Then hand over to the computation (india-income-tax skill) and, if registered, the GST review.
12. **Say that a qualified professional must review** the output before anything is filed.

### Current-year answer layer: Tax Year 2026-27

The enacted Act and notified Rules were opened, including the Finance Act2026 amendment to s.58(11)(a)(i). Rates below do not depend on guessing continuity from an older FAQ. Numbers expressed in words in law are labelled. All individual intake remains ROR sole-proprietor only even where the statute covers other persons.

| Rule | Value and complete condition | Official source |
|---|---|---|
| s.58(2) serial 3 profession | Resident individual or resident firm other than LLP, specified profession under s.62(4); receipts no more than INR 5,000,000, or INR 7,500,000 if cash receipts do not exceed 5% of gross receipts; non-account-payee cheques/drafts count as cash. Limits in words on the page. Profit is 50% of gross receipts or higher actual profit claimed | [s.58(2),(9),(11)(b)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| s.58(2) serial 1 business | Resident eligible individual/HUF/non-LLP firm; exclude goods-carriage serial 2, specified professions, agency, commission/brokerage and Chapter VIII-C deduction claimants. Turnover no more than INR 20,000,000 or INR 30,000,000 if cash receipts do not exceed 5%; non-account-payee cheques/drafts count as cash. Limits in words on the page | [s.58(2),(9),(11)(a), amended by FA s.40](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Finance Act 2026s.40](https://egazette.gov.in/WriteReadData/2026/271439.pdf) |
| Business deemed profit | Aggregate 6% of turnover received by specified banking/online mode during the year or before s.263(1) return due date plus 8% of the remainder, or higher actual profit claimed | [s.58(2) serial 1](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Current specified professions | Legal, medical, engineering, architectural, accountancy, technical consultancy, interior decoration, information technology, company secretary, and any other CBDT-notified profession | [s.62(4)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Cash higher-limit boundary | Exactly 5% qualifies; above 5% uses the lower receipts limit. Check deemed-cash non-account-payee instruments, not merely cash deposits | [s.58(2),(9)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Lower profit/current records | Claiming lower actual profit than the deemed amount AND total income above the maximum not chargeable requires books and audit under s.58(3),62,63; current s.62 book conditions also need review. No automatic current-year no-books assurance is inferred from the old FAQ | [ss.58(3),62-63](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Presumptive deductions/asset history | No extra loss/allowance/deduction against computed presumptive income; asset WDV proceeds as if depreciation had been allowed. Preserve the asset schedule even on presumption | [s.58(4),(6)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Business lockout | If serial 1 profit was declared then a contravening declaration occurs in any of the succeeding 5 tax years, benefit unavailable for 5 tax years after the contravening year; books/audit if s.58(8) income condition met.5 in words on the page | [s.58(7)-(8)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Regime default/option | s.202 default. Business/profession opt-out on or before s.263(1) due date, continuing to subsequent years; withdrawal only once in a later year. After withdrawal no new opt-out while business/profession income continues; cessation permits the nonbusiness route | [s.202(1),(4)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Current option procedure/saved history | Rule136 puts option/withdrawal in return furnished under s.263(1), not a presumed new standalone Form 10-IEA. Earlier option must have been in force immediately before commencement to be saved under s.536(2)(f) | [rule 136](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf); [s.536(2)(f)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Advance-tax threshold | INR 10,000 or more of net advance tax. For the s.405(1) reduction, use the deductible or collectible tax on income included in the estimate where the payer has deducted it on payment or credit, or the collector has collected it on receipt or debit. Senior freelance income prevents the no-business senior exemption | [ss.403(3), 404–405](https://egazette.gov.in/WriteReadData/2025/265620.pdf#page=432) |
| Presumptive serial 1/3 advance tax | Whole amount on or before 15 March; payments by 31 March still count as advance tax. Goods-carriage serial 2 uses the ordinary schedule | [s.408(1)-(3)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Ordinary advance tax | Cumulative 15%/45%/75%/whole amount by 15 June/15 September/15 December/15 March, respectively; compute current tax and credits first | [s.408(1)](https://egazette.gov.in/WriteReadData/2025/265620.pdf) |
| Current ITR eligibility | Rule164(5)-(7): ITR-4 for resident non-RNOR individual/HUF or resident non-LLP firm with s.58 income and only allowed s.198 LTCG up to INR 125,000, subject to ALL subrule 6 bars; ITR-3 otherwise for business/profession. Final fields/utility still need the current form | [rule 164(5)-(7)](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf) |
| Current ITR-4 bars | Foreign asset/signing authority/income; s.10 apportionment; nonpermitted s.93 deduction; directorship; unlisted shares; total income above INR 5,000,000 (in words on the page); more than 2 chargeable house properties; brought-forward/carryforward loss; TDS on income in another person's hands; treaty-relief/deduction condition in164(6)(l); agriculture above INR 5,000; deferred ESOP tax; special-rate income under Part A of Chapter XIII. Two houses in words on page | [rule 164(6), complete list](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf) |
| Paper filing | Individual 80 or older at any time in tax year, eligible for ITR-1/4, may file paper; other electronic modes remain.80 in words on page | [rule 164(12)Table4](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf) |

The notified rule 164(6)(l) contains a defective-looking cross-reference. Do not infer permission to use ITR-4 for a foreign-credit/treaty case from that wording: all foreign-income/assets are already outside this intake. Refer such cases. Final current-year return fields and any corrective text affecting that clause remain on Not yet confirmed.


### Earlier-period figures: 2025-2026 filing cycle

#### Presumptive income, AY 2026-27 ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs))

| Scheme | Who | Receipts limit | Deemed profit | Official source |
| --- | --- | --- | --- | --- |
| 44ADA (profession) | Resident individual or firm (not LLP) carrying on a specified profession | ₹75 lakh where cash receipts do not exceed 5% of total gross receipts (non-account-payee cheque/draft receipts count as cash); ₹50 lakh otherwise | 50% of gross receipts or higher profit claimed actually earned | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs  ; https://www.incometaxindia.gov.in/documents/20117/11892059/Section%2B-%2B44AB_en_8cf1cc.pdf/2d0c4085-9682-5576-ee00-23985588b899?t=1765997029192&version=1.0 |
| 44AD (business) | Resident individual, resident HUF or resident firm (not LLP) in an eligible business, excluding specified profession, agency, commission/brokerage, goods carriages and disqualifying s.10A/10AA/10B/10BA or Chapter VI-A-C deduction claims | ₹3 crore where cash receipts do not exceed 5% of total gross receipts (non-account-payee cheque/draft receipts count as cash); ₹2 crores otherwise | At least 6% of eligible account-payee/bank-electronic/prescribed-mode receipts received during the year or before the s.139(1) return due date; at least 8% of the rest; higher actual profit declared controls | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs  ; https://www.incometaxindia.gov.in/documents/20117/11892059/Section%2B-%2B44AB_en_8cf1cc.pdf/2d0c4085-9682-5576-ee00-23985588b899?t=1765997029192&version=1.0 |

- The 50%, 6% and 8% rates are minimums. The ITR-4 validation rules reject presumptive income under 44ADA that "is less than 50%" and require 44AD income to be "more than or equal to" 6% or 8% ([ITR-4 validation rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%204_Validation%20Rules_AY%202026-27.pdf)).
- The 5% test is "does not exceed": cash of exactly 5% of gross receipts still gets the higher limit.
- Specified professions listed for 44ADA: legal, medical, engineering or architectural, accountancy, technical consultancy, interior decoration and any other profession notified by CBDT. The notified list is not reproduced on the pages cited here (check before placing a freelancer in it).
- 44AD is not available for goods carriages (44AE), agency business, commission or brokerage income, or "a person who is required to maintain books of accounts as referred to in Section 44AA (1)", that is, the specified professions.
- Once presumptive income is declared, the client "is deemed to have claimed all deduction of expenses". No further business expense is deductible. Chapter VI-A deductions (old regime) remain.
- A 44ADA professional who declares at least 50% is described by the old FAQ as not needing s.44AA books for that profession; this is not the current s.62/63 rule and does not remove the need to evidence receipts.
- **Tax Year 2026-27:** the current s.58 table above confirms the operative limits and eligibility; do not merely project this older-cycle table forward.

For the older cycle, s.44AD(4)-(5) also confirms the lockout: a contravening declaration in any of the succeeding 5 assessment years removes eligibility for the 5 assessment years after that contravening year's relevant assessment year; books/audit are required where subsection5 applies and total income exceeds the maximum not chargeable. Do not apply this business lockout to a professional merely because the professional uses 44ADA. Lower professional profit under s.44ADA(4) has its separate income/books/audit condition. [Old Act ss.44AD,44ADA, PDF pp.4-5](https://www.incometaxindia.gov.in/documents/20117/11892059/Section%2B-%2B44AB_en_8cf1cc.pdf/2d0c4085-9682-5576-ee00-23985588b899?t=1765997029192&version=1.0).

#### Regime for the 2025-2026 filing cycle ([Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession))

- New regime is the default. A client with business or professional income opts out by filing Form 10-IEA "on or before the due date u/s 139(1)" for the return. Returning to the new regime is also by Form 10-IEA, and is "available only in subsequent AY and only once in lifetime".
- The [ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs) put it plainly: "Once they switch back, they cannot opt for the old tax regime again."
- If no earlier valid old-regime option continues and Form 10-IEA was not filed by the due date, the older-cycle return is on the new regime. A continuing valid earlier option is not discarded merely because a fresh form was not filed this year. The cessation exception and bar on revising or withdrawing the form in the same year remain relevant. [Official Form 10-IEA FAQ Q7,12-18](https://www.incometax.gov.in/iec/foportal/newformpage/forms/form10-iea).
- **Tax Year 2026-27:** use s.202(4), rule 136 and the saved-option condition in s.536(2)(f), set out in the current-year table above. The separate old Form 10-IEA is not the current rule 136 instruction. [Act](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).

#### Age bands that change the answer, AY 2026-27 ([Business / Profession page: tax slabs](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession))

| Age at any time in the year | Old regime nil band | New regime nil band | Official source |
| --- | --- | --- | --- |
| Below 60 | Up to ₹2,50,000 | Up to ₹4,00,000 | https://www.incometax.gov.in/iec/foportal/help/individual-business-profession |
| 60 or more but below 80 | Up to ₹3,00,000 | Up to ₹4,00,000 | https://www.incometax.gov.in/iec/foportal/help/individual-business-profession |
| 80 or more | Up to ₹5,00,000 | Up to ₹4,00,000 | https://www.incometax.gov.in/iec/foportal/help/individual-business-profession |

- These bands are before the rebate. The full slabs, the rebate (₹60,000 new regime where taxable income does not exceed ₹12,00,000; ₹12,500 old regime where it does not exceed ₹5,00,000) and surcharge are in the india-income-tax skill. These are resident-individual caps, limited to the eligible tax; the new-regime rebate cannot exceed tax at s.115BAC(1A) slab rates, so does not rebate tax at a special rate. Marginal relief needs the separate computation, not an intake promise of zero tax. [Finance Act 2025 s.20](https://egazette.gov.in/WriteReadData/2025/262125.pdf).
- A super senior citizen (80 or more) may file ITR-1 or ITR-4 on paper: "have the option to submit their ITR using Form 1 or 4 in offline / paper mode. The e-Filing option also remains available to them" ([Senior Citizens page](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-2)).
- A resident senior citizen with no business or professional income is not liable to advance tax. A senior freelancer has business or professional income, so the relief does not apply; the net advance-tax threshold still must be met.

#### Advance tax ([Tax Payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq))

| Client | What is due | By | Official source |
| --- | --- | --- | --- |
| Presumptive under 44ADA or 44AD (s.58 from Tax Year 2026-27) | 100% of advance tax in one instalment | 15 March of the year; amounts paid by 31 March count as advance tax for that year | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Ordinary schedule, including actual-profit business and goods-carriage presumption; ITR-3 alone does not determine schedule | 15%, 45%, 75% and 100% of the liability, cumulative | 15 June, 15 September, 15 December, 15 March | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

- Presumptive: "liable to pay 100% of Advance Tax on or before 15 th March of the previous year" ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs)). Tax Year 2026-27: "single instalment on or before 15 March ... in accordance with Section 408(2)".
- Instalment percentages: [ITR-1 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/ITR1-FAQ).
- Advance tax applies where the tax for the year, after TDS, is ₹10,000 or more (the india-income-tax skill covers the wording and interest).
- Interest for late or short advance tax is under 234B and 234C for AY 2026-27, and s.424 and s.425 of the 2025 Act for Tax Year 2026-27: 1% per month or part of a month under s.424.
- As at 14 November 2026, the June and September instalments for Tax Year 2026-27 have passed. A presumptive client still has until 15 March 2027 for the single instalment. An ordinary-schedule client who missed June or September should update the estimate and obtain the interest working. ITR-3 alone does not decide the schedule; a serial 1/3 presumptive taxpayer can use ITR-3. Section 425 construction remains explicitly held in in-advance-tax; do not finalize that interest here.

#### TDS on the freelancer's receipts ([Tax Payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq))

- The 2025 Act applies where the earlier of credit or payment falls on or after 1 April 2026: "If earlier event of credit or payment lies on or after 01 April 2026 → TDS provisions under section 393 of Income Tax Act, 2025 apply". Earlier events stay under the 1961 Act. Deductors under the 2025 Act quote a table item of s.393. The portal warns that "Quoting old section numbers such as 194C, 194J, or 194H ... may result in system -level validation errors."
- For AY 2026-27 reconcile Form 16A to Form 26AS and AIS. For Tax Year 2026-27 ordinary freelance withholding, reconcile Form 131 to Form 168. Check any mismatch with the deductor. [Rule 215](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf#page=160) · [Annual Tax Statement](https://www.incometaxindia.gov.in/tax-services/process-annual-tax-statement-e-filing-form-26as-form-168)
- AIS continues for AY 2026-27; for the 2025 Act it "will stand replaced by Form No. 168 as the evolved Annual Information Statement".

#### Which ITR form, AY 2026-27 ([Business / Profession page: returns and forms](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession))

| Form | Use when | Official source |
| --- | --- | --- |
| ITR-4 (Sugam) | Resident individual (not RNOR) with total income up to ₹50 lakh, presumptive income under 44AD, 44ADA or 44AE, and only these other kinds of income: salary or pension, up to two house properties, other sources, agricultural income up to ₹5,000, s.112A long-term gains up to ₹1,25,000. Optional ("not mandatory") | https://www.incometax.gov.in/iec/foportal/help/individual-business-profession |
| ITR-3 | Individual with business or professional income who cannot use ITR-1, ITR-2 or ITR-4, including anyone computing actual profit from books | https://www.incometax.gov.in/iec/foportal/help/individual-business-profession |

- ITR-4 "cannot be used by a person who" is a company director; has short-term capital gains; has s.112A gains above ₹1,25,000; held unlisted equity shares at any time in the year; has a foreign asset, foreign signing authority or foreign income; has deferred tax on start-up ESOPs; has any loss brought forward or to carry forward; has total income above ₹50 lakh; or has income chargeable at a special rate other than the expressly permitted s.112A gains. The business/profession overview's blanket special-rate line is read with its explicit s.112A eligibility row; refer any conflict at a boundary.
- Tax Year 2026-27 form eligibility is prescribed by notified rule 164, set out below; final year-specific form fields/utility availability are not inferred from the old-cycle screen.

### AY 2026-27 return follow-up, as at 14 November 2026

These returns are governed by the Income-tax Act, 1961, use the old forms, and select AY 2026-27 on the portal.

| Item | Date or rule | Official source |
| --- | --- | --- |
| ITR-4 due date | "31 st August 2026" ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs)). Historical old-cycle date, passed as at 14 November 2026 | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| Audit cases | The tax audit report is due one month before the applicable return due date, subject to any extension. Use Form 3CA with 3CD where an audit is required by another law and Form 3CB with 3CD otherwise. Refer audit clients | [Section 44AB](https://wm.incometaxindia.gov.in/w/section-44ab-37) · [Rule 6G](https://wmstatic-prd.incometaxindia.gov.in/web/guest/w/rule-6g) |
| Belated return, s.139(4) | "on or before 31st December 2026, or prior to the completion of the assessment, whichever occurs earlier" | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/%20income%20tax%20returns-faq |
| Late fee, s.234F | ₹1,000 where total income does not exceed ₹5,00,000; ₹5,000 in all other cases | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/%20income%20tax%20returns-faq |
| Old regime | Only with a valid continuing earlier option or Form 10-IEA filed by the s.139(1) due date. Without either, use the new regime | https://www.incometax.gov.in/iec/foportal/newformpage/forms/form10-iea |

- A freelancer required to file who has not filed AY 2026-27 can use the belated route by 31 December 2026 or before completed assessment, whichever is earlier, subject to any applicable notified extension. Late fee applies to required returns; interest depends on unpaid statutory tax base. Ordinary business-loss carryforward requires timely filing; unabsorbed depreciation is a separate review, not automatically lost.
- Self-assessment tax for AY 2026-27 is paid under the 1961 Act selecting AY 2026-27 on the challan, before filing.
- Returns for AY 2025-26 or earlier: ordinary revised/belated windows have expired; ITR-U eligibility/time limits, notice routes and condonation need separate review. Do not promise that every older case can use ITR-U.

## Boundary and exception table

The older section/form references in this table are for the **2025-2026 filing cycle**; use the current-year answer layer for Tax Year 2026-27.

| Boundary | Inside | Outside | Official source |
| --- | --- | --- | --- |
| Residence | Resident and not RNOR for the year (see in-tax-residency) | Non-resident, RNOR or deemed resident: refuse and refer | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| Structure | Sole proprietor under own PAN | HUF, firm, LLP, company: refuse and refer | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| 44ADA limit | Gross receipts up to ₹75 lakh with cash at most 5% of gross receipts | Cash above 5%: limit ₹50 lakh. Above the limit: actual profit (ITR-3), refer for books and audit | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| 44AD limit | Turnover up to ₹3 crore with cash at most 5% of gross receipts | Cash above 5%: limit ₹2 crores. Above the limit: 44AD not available | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| 44ADA work type | Legal, medical, engineering or architectural, accountancy, technical consultancy, interior decoration, or a CBDT-notified profession | Other work requires classification/notified-profession research; do not assume presumptive business eligibility | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| 44AD work type | Eligible business | Agency, commission or brokerage, goods carriage, or a specified profession: not 44AD | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| Profit declared | At least 50% (44ADA) or 6%/8% (44AD) | Below the rate: books and audit questions arise; refer | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| ITR-4 | Total income up to ₹50 lakh and none of the bars | Otherwise for a business/profession individual, ITR-3 | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| Old regime, business income | Valid continuing earlier old-regime option, or Form 10-IEA filed on or before the s.139(1) due date | No continuing valid option and not filed in time: new regime | https://www.incometax.gov.in/iec/foportal/newformpage/forms/form10-iea |
| Switch back to new regime | First switch back after opting out | Already switched back once: no further opt-out while business/profession continues; cessation requires separate regime review | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| Advance tax timing | Presumptive: everything by 15 March | Ordinary-schedule taxpayer: four instalments; serial 1/3 can still have one instalment even on ITR-3; interest review if short | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| Senior advance tax relief | Resident senior citizen with no business or professional income | A senior with freelance income has no senior exemption; pays if net threshold is met | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| Paper return | Super senior citizen (80 or more) filing ITR-1 or ITR-4 | Other eligible taxpayers use applicable electronic modes; current rule 164 also covers this boundary | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |
| Leaving presumption | Client stays on the same scheme as last year | Client used 44AD last year and now declares less or leaves: lock-out rules in s.44AD(4)-(5) apply as stated above; refer the transition/history before filing; current s.58(7)-(8) is also stated above | https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs |

## Worked cases

All clients are resident, not RNOR, sole proprietors with a PAN linked to Aadhaar, unless stated. Current case1 is confirmed under s.58; the explicitly labelled AY 2026-27 cases use the older filing cycle. All amounts are hypothetical inputs or derived. Assume no applicable deadline extension and no earlier continuing opt-out in case4; no prior assessment has been completed.

1. **Technical consultant, Tax Year 2026-27.** Expected receipts ₹40,00,000, all by bank transfer. Technical consultancy is a specified profession. Cash is nil, so the ₹75 lakh limit applies and the client is inside it. If current s.58(2) serial 3 presumption is chosen, the profit floor is ₹20,00,000 (50%). A higher actual profit claimed controls. Keep receipts and asset records for the statutory books and audit review. Calculate net advance tax under s.405 and reconcile eligible TDS with Form 168. If the result is at least ₹10,000, pay that advance tax in one instalment by 15 March 2027. Hand the ₹20,00,000 profit floor to the india-income-tax skill for the tax computation.
2. **Cash above 5%, AY 2026-27.** Architect, gross receipts ₹60,00,000, of which ₹4,00,000 in cash. 5% of ₹60,00,000 is ₹3,00,000; cash is more than that, so the limit is ₹50 lakh, and receipts exceed it. 44ADA is not available. Actual profit from books (ITR-3) applies. Refer for books and audit.
3. **Freelancer whose work is not on the list.** Content writer, receipts ₹18,00,000 by bank transfer. Writing is not one of the listed professions on the pages cited here. Do not put the client in 44ADA. Flag it: either a CBDT notification covers the work (check), or it is a business and the reviewer decides between 44AD and actual profit. Record the flag; do not compute.
4. **Wants the old regime, too late.** Consultant under 44ADA, receipts ₹16,00,000, deemed profit ₹8,00,000, has never filed Form 10-IEA, and comes to file AY 2026-27 on 10 October 2026. Assuming no applicable extension and no saved earlier option, the ITR-4 page date of 31 August 2026 has passed, so Form 10-IEA can no longer be filed in time. The return is belated (by 31 December 2026), on the new regime, and, assuming a required return with total income ₹8,00,000 and no other income/deduction, the late fee is ₹5,000 because total income exceeds ₹5,00,000.
5. **Senior freelancer.** Client aged 65, freelance engineering receipts. The senior-citizen relief from advance tax is only for a resident senior "not having any Income from Business or Profession", so this client has no senior exemption and pays advance tax if the net statutory threshold is met (all by 15 March if on 44ADA and net advance tax is at or above the threshold). Old-regime nil band ₹3,00,000; new-regime nil band ₹4,00,000.
6. **Director as well.** Freelance lawyer who is also a director of a private company. ITR-4 cannot be used by a company director, so the return is ITR-3 even if 44ADA income is declared. Continue the intake; flag the form.

```oa-check
name: Technical consultant current-year presumptive floor and headroom
inputs:
  gross_receipts: 4000000
  cash_receipts: 0
steps:
  cash_share: cash_receipts / gross_receipts * 100
  headroom: 7500000 - gross_receipts
  presumptive_floor: gross_receipts * 0.50
expected:
  cash_share: 0
  headroom: 3500000
  presumptive_floor: 2000000
```

```oa-check
name: Architect cash share changes the older-cycle receipts limit
inputs:
  gross_receipts: 6000000
  cash_receipts: 400000
steps:
  cash_ceiling: gross_receipts * 0.05
  excess_cash: cash_receipts - cash_ceiling
  excess_receipts_over_lower_limit: gross_receipts - 5000000
expected:
  cash_ceiling: 300000
  excess_cash: 100000
  excess_receipts_over_lower_limit: 1000000
```


## When to refuse or refer

Sources: [Non Resident FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/non%20resident%20-faq) and [Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession).

Refuse and refer (stop the intake, one sentence of reason, name the kind of professional):

- Non-resident, RNOR or deemed resident for the year, or a day count close to the thresholds. The basic resident limb is 182 days or more; the alternative has 60 current days and 365 in preceding 4 years with departure/visitor exceptions; use the in-tax-residency skill and refer if uncertain.
- HUF, partnership firm, LLP or company: separate return, separate rules.
- No PAN.
- Tax audit case, or receipts above the presumptive limits with books to be written up: refer to a Chartered Accountant.
- Foreign income or foreign assets, treaty relief, capital gains beyond the ITR-4 limit, virtual digital assets.
- A pending notice, scrutiny or demand.

Continue but flag for the reviewer:

- Work not clearly on the specified-professions list (see case 3).
- Declared profit below the presumptive rate, or a move out of 44AD after using it (old s.44AD lock-out; current s.58(7)-(8) in the answer layer).
- PAN not linked to Aadhaar.
- Any GST question: threshold, composition, zero-rating of exports or input tax credit. Hand to india-gst for official-source review.
- Private-use percentages for phone, internet and vehicle, and any home-office claim, if actual profit is used. Under presumptive income none of these is deducted.
- Professional tax paid: under presumptive income it is not deductible separately. On actual profit, the reviewer decides its treatment.

Refusal wording (keep it to this): "Stop: you [reason]. This intake covers resident sole proprietors only. You need a Chartered Accountant who handles [NRI / firm / company / audit] returns."

## Filing and payment

- Tax is paid through challans generated on the e-Filing portal, by net banking, debit card, payment gateway (including credit card and UPI) and other listed modes ([e-Pay Tax FAQ](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/e-pay-tax)).
- Pick the right Act and year on the challan: Tax Year 2026-27 (2025 Act) for current advance tax; AY 2026-27 (1961 Act) for self-assessment tax on FY 2025-26 income. The portal ties advance tax "to the tax year to which the income pertains, not the date on which the new Act" came in.
- Returns are filed on the e-Filing portal and then verified. Super senior citizens may file ITR-1 or ITR-4 on paper.
- ITR-4 for AY 2026-27 was due 31 August 2026; belated return route is 31 December 2026 or before completed assessment, whichever earlier; applicable extensions and required-return fee conditions still matter.
- The Tax Year 2026-27 return is not due until 2027; non-audited business/profession due date under amended s.263(1)(c) is 31 August 2027, excluding s.172 cases and subject to a notified extension; other categories differ. [Finance Act 2026s.66](https://egazette.gov.in/WriteReadData/2026/271439.pdf). Final form fields/utility and extensions still need confirmation.
- GST returns and payments are a separate india-gst review; record registration, filing frequency and open dates in the handover.

## Completion checklist

### Summary to show the client before handover

Show one compact summary and ask "Is anything wrong?". It should contain:

- **Year and Act**: Tax Year 2026-27 (2025 Act) or AY 2026-27 (1961 Act).
- **Identity**: name, age band, resident (not RNOR), PAN and Aadhaar link status, GSTIN and type.
- **Work**: the service, and whether it is a specified profession or a business.
- **Receipts**: total, cash part, bank part, the resulting limit, each major client (domestic or outside India).
- **TDS**: by deductor, reconciled to Form 26AS and AIS or Form 168 for the relevant year.
- **Advance tax and self-assessment tax paid**: dates and amounts, and the rule that applies (single instalment or four).
- **Decisions**: regime (with older Form 10-IEA history or current rule 136 status), presumptive section or actual profit, ITR form.
- **Last year**: form, section, regime, losses carried forward, depreciation schedule (written-down value of each asset block).
- **Assets bought this year** (actual-profit path only): item, date, amount, flagged as potential capital items.
- **Open flags**: every item from "Continue but flag", plus anything in AIS not yet explained.

Keep the conversation short: one batch of blocking questions, one document request, one summary, one or two rounds of gap questions. Do not ask what the documents already show.

### Checks before handover

- [ ] Year and Act fixed and written on every figure: Tax Year 2026-27 (2025 Act) or AY 2026-27 (1961 Act).
- [ ] Resident and not RNOR confirmed (in-tax-residency skill if in doubt).
- [ ] Sole proprietor with a PAN; PAN-Aadhaar link checked.
- [ ] Work classified: specified profession (old 44ADA/current serial 3) or eligible business (old 44AD/current serial 1); unlisted work flagged.
- [ ] Receipts totalled, grossed up for TDS, with cash and bank parts; refunds, loans and transfers excluded.
- [ ] Limit picked using the 5% cash test; receipts inside or outside it.
- [ ] ITR-4 bars checked (director, unlisted shares, foreign items, losses, short-term gains, total income above ₹50 lakh).
- [ ] Regime fixed; older Form 10-IEA history/current rule 136 and saved-option status plus one-time switch back checked.
- [ ] TDS reconciled to the statements for the relevant year, with differences and unexplained items recorded.
- [ ] Advance tax checked against the right rule (15 March for presumptive).
- [ ] For AY 2026-27: filed or not; if not, belated by 31 December 2026 or earlier assessment, subject to extensions; new regime unless valid continuing old option/timely Form 10-IEA.
- [ ] GST questions asked and flagged for checking on the GST portal.
- [ ] Summary confirmed by the client; open flags listed.
- [ ] Client told that a qualified professional must review before filing.

## Sources

| Official source | Read for | Actual read date |
|---|---|---|
| https://egazette.gov.in/WriteReadData/2025/265620.pdf | Read for complete s.58 tables/subsections3-11, s.62(4), s.156,202,403-410 and536(2)(f): current presumption, profession, regime, advance tax and savings | 2026-11-14 |
| https://egazette.gov.in/WriteReadData/2026/271439.pdf | Read for s.40 omission in58eligibleassessee; s.56 change in202deductions and s.66 returndates; no current limit guessed | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf | Read for rule136 and entire164: regime option inreturn, ITReligibility/exclusions/paperfiling; current references read with notifiedcorrigendum | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq | Read for Q2,21-26: repeal, period, regime/savings and s58consolidation | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/individual-business-profession | Read for returns/forms/ITR4exclusions, AIS/26AS/certificates, regime and complete age/nilband/rebate tables; 2025-2026 filing cycle | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs | Read for Q1-18 and22: eligibility/exclusions, records, regimes, presumptive limits/rates/books, advance and deadline; oldercycle | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/how-to-link-aadhaar | Read for overview/exempt-category qualification, prerequisites and status/linking workflow | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/Tax%20Credit%20Mismatch%20-FAQ | Read for all4questions: 26AS, challan/PAN mismatch, deductor correction and creditreconciliation | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq | Read for Q3-6,14-23: TDStransition, advance/schedules, yearselection and Form168 | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/%20income%20tax%20returns-faq | Read for Q7-12,24-27: belated/earlier returns, fees, auditdate, periodselection; stale proposedrevisedlabel not reliedon | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-2 | Read for paperfiling and senioradvance exemption nearpageend; not all deductions onpage | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%204_Validation%20Rules_AY%202026-27.pdf | Read for rules5-17: old44AD/44ADAprofitminimum, businesscode and exclusions; oldcycle only | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/e-pay-tax | Read for FAQ4-15 and38: CRN/payment modes/receipt/wrongpayment; paymentproof retained | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/ITR1-FAQ | Read for Q14-15 and neighbors: cumulative old-cycle instalments, self-assessment and verification; loose more-than threshold text not used instead of enacted inclusive threshold | 2026-11-14 |
| https://egazette.gov.in/WriteReadData/2025/262125.pdf | Read for s.20 complete operative amendments/proviso to oldAct87A: AY2026-27 income/rebate limits and cap to115BAC(1A)slabtax, not special-ratetax | 2026-11-14 |
| https://www.incometaxindia.gov.in/documents/20117/11892059/Section%2B-%2B44AB_en_8cf1cc.pdf/2d0c4085-9682-5576-ee00-23985588b899?t=1765997029192&version=1.0 | Read for old ss.44AB (PDFp.1),44ADA (p.4),44AD (p.5), including Finance2023effectiveprovisos: rates/timing, higher actual profit, cashdeeming, eligibility, lockout and audit; not all22pages | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/newformpage/forms/form10-iea | Read for Q7-8 and12-21: old-cycle due date, continuing option without annual refiling, withdrawal, cessation exception and same-year prohibition | 2026-11-14 |
| https://www.incometaxindia.gov.in/tax-services/process-annual-tax-statement-e-filing-form-26as-form-168 | Period-specific annual tax statement routes. | 2026-11-24 |
| https://www.incometaxindia.gov.in/w/section-145-9 | Earlier-cycle method of accounting. The current counterpart is s.276 in the Gazette above. | 2026-11-24 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tds-compliance | Q24–26 on the transition, Form 168 and deductor corrections. | 2026-11-24 |
| https://www.incometaxindia.gov.in/documents/20117/6507196/Circular-9-2025.pdf/c93e8e33-6029-c652-9fe7-abc9f8b021cd?t=1762868920211&version=1.0 | Earlier-cycle inoperative-PAN rules and conditional relief. The current rule is notified rule 162. | 2026-11-24 |
| https://wmstatic-prd.incometaxindia.gov.in/web/guest/w/rule-6g | Earlier-cycle audit reports and prescribed particulars. | 2026-11-24 |

| Notified Rules 2026, targeted reread | Read for rule 164(1)-(12), particularly the exact fifty-lakh wording in 164(3)(k) and 164(6)(h), surrounding exclusions and verification table; no new resolution of the held cross-reference or gain interaction | 2026-11-16; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

**Not yet confirmed:** final Tax Year 2026-27 ITR fields/utility and corrective text for rule 164(6)(l); notified extensions that apply to an individual filing date; any books/audit exception beyond the cited old ss.44AB/44AD/44ADA, loss/depreciation carryforward and the specific special-income rebate computation; notified professions beyond current s.62(4) list; GST computation/thresholds/export/composition/credit. These require the named sibling/professional review before filing. Old paper/age/rate examples remain labelled 2025-2026 filing cycle; no arbitrary exclusion of official GST sources is imposed. Section 425 construction remains held in in-advance-tax.
