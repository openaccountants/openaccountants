---
name: in-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing their India tax returns AND mentions freelancing, self-employment, contracting, professional services, or independent practice. Trigger on phrases like "help me do my taxes", "prepare my ITR", "I'm self-employed in India", "I'm a freelancer in India", "do my taxes as a consultant", "prepare my income tax return", or any similar phrasing where the user is an India-resident self-employed individual needing tax return preparation. This is the REQUIRED entry point for the India self-employed tax workflow -- every other skill in the stack (india-gst, in-income-tax, in-advance-tax, in-tds-freelance, in-return-assembly) depends on this skill running first to produce a structured intake package. Uses upload-first workflow -- the user dumps all their documents and the skill infers as much as possible before asking questions. Uses ask_user_input_v0 for structured questions instead of one-at-a-time prose. Built for speed. India full-year residents only; self-employed individuals and professionals only.
version: 0.1
jurisdiction: IN
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India intake for freelancers and professionals: residence, presumptive income (44ADA/44AD), regime, advance tax, TDS and GST (Tax Year 2026-27, with AY 2026-27 returns)

## Scope and who this is for ([Income Tax Department: objective and scope of the new Act](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq))

- This Guide is the intake step for a resident individual in India who earns freelance, consulting, contract or professional income as a sole proprietor. It collects the facts and documents, screens out cases it cannot handle, and fixes the decisions that change the whole computation: the year, residence, regime, presumptive or actual profit, and the ITR form. It does not compute tax.
- For the tax computation itself (slabs, rebate, surcharge, deductions, interest), use the **in-income-tax** Guide. For residence and RNOR tests, use the **in-tax-residency** Guide. This Guide does not repeat them.
- **Two years are live on 25 September 2026. Always ask which one.**
  - **Tax Year 2026-27** (1 April 2026 to 31 March 2027) is the current year. It is governed by the Income-tax Act, 2025. The portal says: "The 1961 Act stands repealed on the 01.04.2026." Income "earned during FY 2026 -27 onwards ... will be referred to as Tax Year 2026-27 under the Income Tax Act ,2025." Intake for this year is about advance tax, TDS on current receipts and records.
  - **AY 2026-27** (income of FY 2025-26, 1 April 2025 to 31 March 2026) is the return being filed or chased now. It stays under the Income-tax Act, 1961 and the old ITR forms. See "AY 2026-27 returns (FY 2025-26), dated 25 September 2026" below.
- **Regime default.** The new tax regime is the default for individuals ("new tax regime the default tax regime", [Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession)). Under the 2025 Act "the new tax regime is provided under section 202" ([objective and scope FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq)). A client with business or professional income leaves the default only by filing Form 10-IEA on time (see "Regime" below).
- Out of scope, refer: non-residents and RNORs; HUFs, firms, LLPs and companies; tax audit cases; clients with capital gains beyond the ITR-4 limit, foreign income or assets; GST computations (see the GST note below).
- Currency is Indian rupees in Indian grouping (₹12,00,000 is twelve lakh).
- **GST note.** The GST authorities' sites are not among the official sources this Guide can cite. This Guide therefore asks the GST questions but states no GST threshold, rate or deadline. Confirm every GST point on the GST portal before advising (check).

## Ask the client first

Sources: [ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs) and [Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession).

Ask these in one or two batches. Anything already visible in the documents is confirmed, not re-asked.

**Blocking questions (ask first; a "no" ends the intake):**

1. **Which year?** Tax Year 2026-27 (current, 2025 Act), AY 2026-27 (FY 2025-26 income, 1961 Act), or both.
2. **Residence for that year.** Days in India in the year, days in the four and seven preceding years, citizenship or Indian origin. If the client may be non-resident, RNOR or deemed resident, stop and use the in-tax-residency Guide. ITR-4 "cannot be filed by" a person who "is a Resident but Not Ordinarily Resident (RNOR), or Non-Resident Indian".
3. **Structure.** Does the client invoice in their own name under their own PAN (sole proprietor)? HUF, partnership firm, LLP or company: stop and refer.
4. **PAN and Aadhaar.** No PAN: stop; the client must get one first. PAN not linked to Aadhaar: continue with a flag. The portal says an unlinked PAN "will become inoperative" ([Link Aadhaar](https://www.incometax.gov.in/iec/foportal/help/how-to-link-aadhaar)), and that the ITR can still be filed "but you will have limited access on the portal" ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs)). Tell the client to link before filing. The TDS consequences of an inoperative PAN are not stated on the pages cited here (check).

**Scope questions:**

5. **What exactly is the work?** Name the service. Is it one of the specified professions (legal, medical, engineering or architectural, accountancy, technical consultancy, interior decoration, or a profession notified by CBDT), or a business (trading, reselling, agency, commission, content or platform work that is not a listed profession)? This decides 44ADA versus 44AD.
6. **Gross receipts for the year**, and how much came in cash as opposed to bank transfer, cheque, draft or other electronic mode.
7. **Age at any time in the year**: below 60, 60 to below 80, or 80 or more.
8. **Regime history.** Which regime was used last year? Has the client ever filed Form 10-IEA to opt out of the new regime, and have they already used the one-time switch back?
9. **Presumptive history.** Which ITR was filed last year (ITR-3 or ITR-4), and under which section (44AD or 44ADA)?
10. **ITR-4 bars.** Director in a company? Unlisted equity shares at any time in the year? Short-term capital gains, or s.112A long-term gains above ₹1,25,000? Any foreign asset, foreign signing authority or foreign income? Any loss brought forward or to carry forward? More than two house properties? Total income above ₹50 lakh? Any "yes" rules out ITR-4 ([Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession)).
11. **GST.** Is the client registered (GSTIN), regular or composition? Do they invoice clients outside India?
12. **Other income.** Salary, savings or deposit interest, rent, dividends, capital gains.

**Documents to request in one go** (list from the [ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs), "documents do I need to file ITR-4", plus business records):

- Bank statements for every account used for the work, for the whole year.
- Sales invoices issued, and purchase invoices or receipts for expenses (needed only if actual profit is being considered).
- If actual profit is being considered: equipment and other assets bought in the year (invoices and dates; potential capital items), and last year's depreciation schedule with the written-down value of each asset block. This Guide states no depreciation rate; the reviewer applies it.
- Form 26AS and AIS, downloaded from the e-Filing portal after login.
- Form 16A from each client that deducted TDS ("a Tax Deducted at Source (TDS) Certificate issued quarterly", [Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession)), and Form 16 if there was also salary.
- Challans for advance tax and self-assessment tax.
- Last year's ITR and acknowledgement, and any Form 10-IEA acknowledgement.
- GST returns filed and the GST registration certificate, if registered.
- Old-regime proofs only if the old regime is in play: life insurance, provident fund, pension (NPS) and health insurance premiums, rent receipts and Form 10BA for 80GG, home-loan interest certificate.
- Any notice or letter from the Income Tax Department.

If the client does not know what they have, point them to: the e-Filing portal (Form 26AS, AIS, filed returns, challans), their bank's net banking (statements), email searches for "invoice", "TDS", "ITR" and "challan", and last year's accountant.

## The method, step by step

Sources: [ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs), [Tax Payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq).

1. **Fix the year and the Act.** Label every figure and document with its year. FY 2025-26 income is AY 2026-27 (1961 Act). Income from 1 April 2026 is Tax Year 2026-27 (2025 Act). A challan paid for the wrong year credits the wrong year.
2. **Run the blocking screen** (questions 1 to 4). Stop cleanly on any refusal: state the reason in one sentence and the kind of professional to see.
3. **Read the documents before asking anything else.** From the bank statements, total the receipts from clients and split them into cash deposits and bank or electronic receipts. Exclude own-account transfers, loans, income-tax refunds and GST refunds. Separate salary and interest from business receipts.
4. **Gross up receipts for TDS.** A client that deducted TDS paid a net amount; the receipt to report is the invoice amount, and the TDS is a credit. Match TDS deductor by deductor against Form 26AS and AIS. The credit "is restricted/provided to the amount as reflected in your Form 26 AS" ([Tax Credit Mismatch FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/Tax%20Credit%20Mismatch%20-FAQ)). A missing TDS entry is fixed by the deductor, not by the client.
5. **Read AIS for what the client did not mention.** AIS shows TDS and TCS, SFT information, tax payments, demand and refund, and "Other information (like Pending/Completed proceedings, GST Information, Information received from foreign government etc.)" ([Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession)). Anything in AIS that the client has not explained becomes a question.
6. **Classify the work** as a specified profession (44ADA) or a business (44AD), using the client's own description and the invoices. If the service is not clearly on the specified list, do not assume 44ADA; flag it (see the boundary table). If the client has both professional and business income, record each stream separately (receipts, cash part, section) and flag it for the reviewer.
7. **Test presumptive eligibility.** Compare gross receipts to the limit, using the cash share to pick the limit. Check the ITR-4 bars. If eligible, the client chooses presumptive (ITR-4) or actual profit from books (ITR-3). Record the choice and the prior-year choice.
8. **Fix the regime.** New regime unless the client has filed, or will file on time, Form 10-IEA to opt out. Check whether the one-time switch back has been used. The comparison itself is done with the in-income-tax Guide.
9. **Check advance tax paid** against the rule for the client's case (presumptive: all by 15 March; others: four instalments). Note dates and amounts from challans and Form 26AS.
10. **Fill the gaps** that the documents cannot answer: private use of phone and internet, home office, other income, old-regime deductions, anything unclear in AIS.
11. **Show one summary** of everything found and decided, with open flags, and ask the client to correct it. Then hand over to the computation (in-income-tax Guide) and, if registered, the GST review.
12. **Say that a qualified professional must review** the output before anything is filed.

## Figures by year

**Which year these figures are for.** The figures below are the ones the Income Tax Department publishes for AY 2026-27 (income of FY 2025-26, 1961 Act). At 25 September 2026 the portal pages cited here do not restate them for Tax Year 2026-27. The portal says the presumptive schemes "have been consolidated into one section (section 58)" of the 2025 Act ([objective and scope FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq)). Use these figures for Tax Year 2026-27 intake, labelled as AY 2026-27 figures, and confirm them in s.58 and s.202 of the 2025 Act before relying on them for that year (check).

### Presumptive income, AY 2026-27 ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs))

| Scheme | Who | Receipts limit | Deemed profit |
| --- | --- | --- | --- |
| 44ADA (profession) | Resident individual or firm (not LLP) carrying on a specified profession | ₹75 lakh where cash receipts do not exceed 5% of total gross receipts; ₹50 lakh otherwise | At least 50% of gross receipts |
| 44AD (business) | Resident individual, resident HUF or resident firm (not LLP) in an eligible business | ₹3 crore where cash receipts do not exceed 5% of total gross receipts; ₹2 crores otherwise | At least 6% of receipts by account-payee cheque, draft, bank electronic clearing or prescribed electronic mode (received by the specified date); at least 8% of the rest |

- The 50%, 6% and 8% rates are minimums. The ITR-4 validation rules reject presumptive income under 44ADA that "is less than 50%" and require 44AD income to be "more than or equal to" 6% or 8% ([ITR-4 validation rules](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-05/CBDT_e-Filing_ITR%204_Validation%20Rules_AY%202026-27.pdf)).
- The 5% test is "does not exceed": cash of exactly 5% of gross receipts still gets the higher limit.
- Specified professions for 44ADA: "Legal, Medical, Engineering or Architectural, Accountancy, Technical Consultancy, Interior Decoration, Any other Profession as notified by CBDT". The notified list is not reproduced on the pages cited here (check before placing a freelancer in it).
- 44AD is not available for goods carriages (44AE), agency business, commission or brokerage income, or "a person who is required to maintain books of accounts as referred to in Section 44AA (1)", that is, the specified professions.
- Once presumptive income is declared, the client "is deemed to have claimed all deduction of expenses". No further business expense is deductible. Chapter VI-A deductions (old regime) remain.
- A 44ADA professional who declares at least 50% need not keep books under s.44AA for that profession.
- **Tax Year 2026-27:** 44AD, 44ADA and 44AE sit together in s.58 of the 2025 Act. The portal pages cited here do not restate the s.58 limits (check).

### Regime, AY 2026-27 and after ([Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession))

- New regime is the default. A client with business or professional income opts out by filing Form 10-IEA "on or before the due date u/s 139(1)" for the return. Returning to the new regime is also by Form 10-IEA, and is "available only in subsequent AY and only once in lifetime".
- The [ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs) put it plainly: "Once they switch back, they cannot opt for the old tax regime again."
- If Form 10-IEA was not filed by the due date, the return is on the new regime.
- **Tax Year 2026-27:** the portal says that "a particular tax option under the old Act (like opting for a special tax scheme)" carries over to the 2025 Act under s.536(2)(f) (question 26 of the [objective and scope FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq)). The FAQ does not name the Form 10-IEA regime choice itself. Before relying on a carried-over opt-out, confirm that it is covered, and check the replacement for Form 10-IEA under the new rules (check).

### Age bands that change the answer, AY 2026-27 ([Business / Profession page: tax slabs](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession))

| Age at any time in the year | Old regime nil band | New regime nil band |
| --- | --- | --- |
| Below 60 | Up to ₹2,50,000 | Up to ₹4,00,000 |
| 60 or more but below 80 | Up to ₹3,00,000 | Up to ₹4,00,000 |
| 80 or more | Up to ₹5,00,000 | Up to ₹4,00,000 |

- These bands are before the rebate. The full slabs, the rebate (₹60,000 new regime where taxable income does not exceed ₹12,00,000; ₹12,500 old regime where it does not exceed ₹5,00,000) and surcharge are in the in-income-tax Guide.
- A super senior citizen (80 or more) may file ITR-1 or ITR-4 on paper: "have the option to submit their ITR using Form 1 or 4 in offline / paper mode. The e-Filing option also remains available to them" ([Senior Citizens page](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-2)).
- A resident senior citizen with no business or professional income is not liable to advance tax. A senior freelancer has business or professional income, so the relief does not apply.

### Advance tax ([Tax Payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq))

| Client | What is due | By |
| --- | --- | --- |
| Presumptive under 44ADA or 44AD (s.58 from Tax Year 2026-27) | 100% of advance tax in one instalment | 15 March of the year; amounts paid by 31 March count as advance tax for that year |
| Actual profit (ITR-3) | 15%, 45%, 75% and 100% of the liability, cumulative | 15 June, 15 September, 15 December, 15 March |

- Presumptive: "liable to pay 100% of Advance Tax on or before 15 th March of the previous year" ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs)). Tax Year 2026-27: "single instalment on or before 15 March ... in accordance with Section 408(2)".
- Instalment percentages: [ITR-1 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/ITR1-FAQ).
- Advance tax applies where the tax for the year, after TDS, is ₹10,000 or more (the in-income-tax Guide covers the wording and interest).
- Interest for late or short advance tax is under 234B and 234C for AY 2026-27, and s.424 and s.425 of the 2025 Act for Tax Year 2026-27: 1% per month or part of a month under s.424.
- For Tax Year 2026-27, 15 September 2026 has passed. A presumptive client still has until 15 March 2027 for the single instalment. An ITR-3 client who missed June or September should pay now and expect interest.

### TDS on the freelancer's receipts ([Tax Payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq))

- The 2025 Act applies where the earlier of credit or payment falls on or after 1 April 2026: "If earlier event of credit or payment lies on or after 01 April 2026 → TDS provisions under section 393 of Income Tax Act, 2025 apply". Earlier events stay under the 1961 Act. Deductors under the 2025 Act quote a table item of s.393. The portal warns that "Quoting old section numbers such as 194C, 194J, or 194H ... may result in system -level validation errors."
- TDS rates and thresholds are not restated here. Take the amount from Form 16A and Form 26AS, not from an assumed rate.
- AIS continues for AY 2026-27; for the 2025 Act it "will stand replaced by Form No. 168 as the evolved Annual Information Statement".

### Which ITR form, AY 2026-27 ([Business / Profession page: returns and forms](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession))

| Form | Use when |
| --- | --- |
| ITR-4 (Sugam) | Resident individual (not RNOR) with total income up to ₹50 lakh, presumptive income under 44AD, 44ADA or 44AE, and only these other kinds of income: salary or pension, up to two house properties, other sources, agricultural income up to ₹5,000, s.112A long-term gains up to ₹1,25,000. Optional ("not mandatory") |
| ITR-3 | Individual with business or professional income who cannot use ITR-1, ITR-2 or ITR-4, including anyone computing actual profit from books |

- ITR-4 "cannot be used by a person who" is a company director; has short-term capital gains; has s.112A gains above ₹1,25,000; held unlisted equity shares at any time in the year; has a foreign asset, foreign signing authority or foreign income; has deferred tax on start-up ESOPs; has any loss brought forward or to carry forward; has total income above ₹50 lakh; or has income chargeable at a special rate.
- Tax Year 2026-27 returns will use new ITR forms under the new rules; they are not on the pages cited here.

## Boundary and exception table ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs))

| Boundary | Inside | Outside |
| --- | --- | --- |
| Residence | Resident and not RNOR for the year (see in-tax-residency) | Non-resident, RNOR or deemed resident: refuse and refer |
| Structure | Sole proprietor under own PAN | HUF, firm, LLP, company: refuse and refer |
| 44ADA limit | Gross receipts up to ₹75 lakh with cash at most 5% of gross receipts | Cash above 5%: limit ₹50 lakh. Above the limit: actual profit (ITR-3), refer for books and audit |
| 44AD limit | Turnover up to ₹3 crore with cash at most 5% of gross receipts | Cash above 5%: limit ₹2 crores. Above the limit: 44AD not available |
| 44ADA work type | Legal, medical, engineering or architectural, accountancy, technical consultancy, interior decoration, or a CBDT-notified profession | Anything else is a business: 44AD may apply, never 44ADA |
| 44AD work type | Eligible business | Agency, commission or brokerage, goods carriage, or a specified profession: not 44AD |
| Profit declared | At least 50% (44ADA) or 6%/8% (44AD) | Below the rate: books and audit questions arise; refer |
| ITR-4 | Total income up to ₹50 lakh and none of the bars | Otherwise ITR-3 |
| Old regime, business income | Form 10-IEA filed on or before the s.139(1) due date | Not filed in time: new regime |
| Switch back to new regime | First switch back after opting out | Already switched back once: old regime no longer available |
| Advance tax timing | Presumptive: everything by 15 March | ITR-3: four instalments; interest if short |
| Senior advance tax relief | Resident senior citizen with no business or professional income | A senior with freelance income pays advance tax |
| Paper return | Super senior citizen (80 or more) filing ITR-1 or ITR-4 | Everyone else files electronically |
| Leaving presumption | Client stays on the same scheme as last year | Client used 44AD last year and now declares less or leaves: lock-out rules in s.44AD apply; not stated on the pages cited here, refer (check) |

## AY 2026-27 returns (FY 2025-26), dated 25 September 2026 ([Income Tax Returns FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/%20income%20tax%20returns-faq))

These returns are governed by the Income-tax Act, 1961, use the old forms, and select AY 2026-27 on the portal.

| Item | Date or rule |
| --- | --- |
| ITR-4 due date | "31 st August 2026" ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs)). Passed on 25 September 2026 |
| Audit cases | The tax audit report (Form 3CB-3CD) is furnished at least one month before the return due date; audit clients are out of scope here |
| Belated return, s.139(4) | "on or before 31st December 2026, or prior to the completion of the assessment, whichever occurs earlier" |
| Late fee, s.234F | ₹1,000 where total income does not exceed ₹5,00,000; ₹5,000 in all other cases |
| Old regime | Only if Form 10-IEA was filed by the s.139(1) due date. A client who missed it files on the new regime |

- A freelancer who has not filed AY 2026-27 by 25 September 2026 can file a belated return until 31 December 2026, pays the late fee and interest on unpaid tax, and cannot carry forward business losses of the year.
- Self-assessment tax for AY 2026-27 is paid under the 1961 Act selecting AY 2026-27 on the challan, before filing.
- Returns for AY 2025-26 or earlier: only an updated return (ITR-U) remains; refer.

## Worked cases ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs))

All clients are resident, not RNOR, sole proprietors with a PAN linked to Aadhaar, unless stated. The figures are the AY 2026-27 figures; for Tax Year 2026-27 confirm them in s.58 (check).

1. **Technical consultant, Tax Year 2026-27.** Expected receipts ₹40,00,000, all by bank transfer. Technical consultancy is a specified profession. Cash is nil, so the ₹75 lakh limit applies and the client is inside it. If 44ADA is chosen, deemed profit is at least 50%: ₹20,00,000. No expenses are deducted on top. Advance tax: the whole year's tax, net of TDS shown in Form 26AS, by 15 March 2027. Hand the ₹20,00,000 to the in-income-tax Guide for the tax.
2. **Cash above 5%, AY 2026-27.** Architect, gross receipts ₹60,00,000, of which ₹4,00,000 in cash. 5% of ₹60,00,000 is ₹3,00,000; cash is more than that, so the limit is ₹50 lakh, and receipts exceed it. 44ADA is not available. Actual profit from books (ITR-3) applies. Refer for books and audit.
3. **Freelancer whose work is not on the list.** Content writer, receipts ₹18,00,000 by bank transfer. Writing is not one of the listed professions on the pages cited here. Do not put the client in 44ADA. Flag it: either a CBDT notification covers the work (check), or it is a business and the reviewer decides between 44AD and actual profit. Record the flag; do not compute.
4. **Wants the old regime, too late.** Consultant under 44ADA, receipts ₹16,00,000, deemed profit ₹8,00,000, has never filed Form 10-IEA, and comes to file AY 2026-27 on 10 October 2026. The ITR-4 due date of 31 August 2026 has passed, so Form 10-IEA can no longer be filed in time. The return is belated (by 31 December 2026), on the new regime, and the late fee is ₹5,000 because total income exceeds ₹5,00,000.
5. **Senior freelancer.** Client aged 65, freelance engineering receipts. The senior-citizen relief from advance tax is only for a resident senior "not having any Income from Business or Profession", so this client pays advance tax (all by 15 March if on 44ADA). Old-regime nil band ₹3,00,000; new-regime nil band ₹4,00,000.
6. **Director as well.** Freelance lawyer who is also a director of a private company. ITR-4 cannot be used by a company director, so the return is ITR-3 even if 44ADA income is declared. Continue the intake; flag the form.

## When to refuse or refer

Sources: [Non Resident FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/non%20resident%20-faq) and [Business / Profession page](https://www.incometax.gov.in/iec/foportal/help/individual-business-profession).

Refuse and refer (stop the intake, one sentence of reason, name the kind of professional):

- Non-resident, RNOR or deemed resident for the year, or a day count close to the thresholds. The basic test is "182 days or more in the relevant tax year, or for 60 days or more in that year coupled w[ith]" days in earlier years; use the in-tax-residency Guide and refer if uncertain.
- HUF, partnership firm, LLP or company: separate return, separate rules.
- No PAN.
- Tax audit case, or receipts above the presumptive limits with books to be written up: refer to a Chartered Accountant.
- Foreign income or foreign assets, treaty relief, capital gains beyond the ITR-4 limit, virtual digital assets.
- A pending notice, scrutiny or demand.

Continue but flag for the reviewer:

- Work not clearly on the specified-professions list (see case 3).
- Declared profit below the presumptive rate, or a move out of 44AD after using it (s.44AD lock-out, check).
- PAN not linked to Aadhaar.
- Any GST question: threshold, composition, zero-rating of exports, or input tax credit. These must be checked on the GST portal (check).
- Private-use percentages for phone, internet and vehicle, and any home-office claim, if actual profit is used. Under presumptive income none of these is deducted.
- Professional tax paid: under presumptive income it is not deductible separately. On actual profit, the reviewer decides its treatment.

Refusal wording (keep it to this): "Stop: you [reason]. This intake covers resident sole proprietors only. You need a Chartered Accountant who handles [NRI / firm / company / audit] returns."

## Filing and payment ([Tax Payments FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq))

- Tax is paid through challans generated on the e-Filing portal, by net banking, debit card, payment gateway (including credit card and UPI) and other listed modes ([General Questions FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/General%20Questions-faqs)).
- Pick the right Act and year on the challan: Tax Year 2026-27 (2025 Act) for current advance tax; AY 2026-27 (1961 Act) for self-assessment tax on FY 2025-26 income. The portal ties advance tax "to the tax year to which the income pertains, not the date on which the new Act" came in.
- Returns are filed on the e-Filing portal and then verified. Super senior citizens may file ITR-1 or ITR-4 on paper.
- ITR-4 for AY 2026-27 was due 31 August 2026; belated returns run to 31 December 2026 with the s.234F fee.
- The Tax Year 2026-27 return is not due until 2027; the dates for it are not stated on the pages cited here (check the e-Filing calendar).
- GST returns and payments are outside the pages this Guide can cite; confirm the client's GST filing frequency and dates on the GST portal (check).

## Summary to show the client before handover

Show one compact summary and ask "Is anything wrong?". It should contain:

- **Year and Act**: Tax Year 2026-27 (2025 Act) or AY 2026-27 (1961 Act).
- **Identity**: name, age band, resident (not RNOR), PAN and Aadhaar link status, GSTIN and type.
- **Work**: the service, and whether it is a specified profession or a business.
- **Receipts**: total, cash part, bank part, the resulting limit, each major client (domestic or outside India).
- **TDS**: by deductor, matched or not matched to Form 26AS.
- **Advance tax and self-assessment tax paid**: dates and amounts, and the rule that applies (single instalment or four).
- **Decisions**: regime (with Form 10-IEA status), presumptive section or actual profit, ITR form.
- **Last year**: form, section, regime, losses carried forward, depreciation schedule (written-down value of each asset block).
- **Assets bought this year** (actual-profit path only): item, date, amount, flagged as potential capital items.
- **Open flags**: every item from "Continue but flag", plus anything in AIS not yet explained.

Keep the conversation short: one batch of blocking questions, one document request, one summary, one or two rounds of gap questions. Do not ask what the documents already show.

## Completion checklist ([ITR-4 FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/itr%204-faqs))

- [ ] Year and Act fixed and written on every figure: Tax Year 2026-27 (2025 Act) or AY 2026-27 (1961 Act).
- [ ] Resident and not RNOR confirmed (in-tax-residency Guide if in doubt).
- [ ] Sole proprietor with a PAN; PAN-Aadhaar link checked.
- [ ] Work classified: specified profession (44ADA) or business (44AD); unlisted work flagged.
- [ ] Receipts totalled, grossed up for TDS, with cash and bank parts; refunds, loans and transfers excluded.
- [ ] Limit picked using the 5% cash test; receipts inside or outside it.
- [ ] ITR-4 bars checked (director, unlisted shares, foreign items, losses, short-term gains, total income above ₹50 lakh).
- [ ] Regime fixed; Form 10-IEA status and one-time switch back checked.
- [ ] TDS matched to Form 26AS and AIS; AIS items explained.
- [ ] Advance tax checked against the right rule (15 March for presumptive).
- [ ] For AY 2026-27: filed or not; if not, belated by 31 December 2026 on the new regime unless Form 10-IEA was filed in time.
- [ ] GST questions asked and flagged for checking on the GST portal.
- [ ] Summary confirmed by the client; open flags listed.
- [ ] Client told that a qualified professional must review before filing.

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
