---
name: in-tds-freelance
description: Use this skill whenever asked about Indian TDS (Tax Deducted at Source) on payments to freelancers, contractors, or professionals. Trigger on phrases like "TDS freelance India", "Section 194J", "Section 194C", "Section 194O", "TDS rate professional services", "Form 26Q", "Form 16A", "TDS certificate", "26AS", "AIS reconciliation", "TDS return India", "lower deduction certificate", "Section 197", "Section 206AA", "PAN not provided TDS", or any question about TDS obligations when paying or receiving freelance/contractor payments in India. Covers Section 194J (professional/technical services), 194C (contractor payments), 194O (e-commerce), TDS return filing (Form 26Q), TDS certificates (Form 16A), Form 26AS/AIS reconciliation, higher rate for missing PAN (Section 206AA), and lower deduction certificates (Section 197). ALWAYS read this skill before touching any India TDS work involving freelancers or contractors.
version: 1.0
jurisdiction: IN
tax_year: 2026
last_updated: 2026-10-17
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India: TDS on Payments to Freelancers, Professionals and Contractors

This Guide covers tax deducted at source (TDS) when a business pays a resident freelancer, professional or contractor in India, and what the freelancer does with the credit. Figures are for tax year 2026. This means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act 2025, which replaced the Income-tax Act 1961 from 1 April 2026. The TDS rules now sit in Chapter XIX-B of the 2025 Act, mainly the Table in section 393(1), with the PAN rule, deposit and statements in section 397 and the consequences of default in section 398. The section numbers changed: this Guide cites the 2025 Act numbers and the Income-tax Rules 2026 form numbers. Amounts credited or paid before 1 April 2026 fall under the 1961 Act, which section 536 of the 2025 Act repeals while saving its previous operation; this Guide does not cover them.

## Confidence Tier Definitions

**[T1] Tier 1: Deterministic.** Apply exactly as written. No reviewer judgement required.
**[T2] Tier 2: Reviewer Judgement Required.** The assistant flags and presents options. A Chartered Accountant must confirm.
**[T3] Tier 3: Out of Scope / Escalate.** Do not guess. Escalate and document.

## Guide Metadata

- **Jurisdiction**: India (IN)
- **Primary legislation**: Income-tax Act 2025 (30 of 2025), Chapter XIX-B, sections 393, 395, 396, 397, 398 and 402; fees and penalties in sections 427 and 461
- **Amending law**: Finance Act 2026 (4 of 2026), sections 2 to 129 in force from 1 April 2026 unless the Act says otherwise
- **Rules**: Income-tax Rules 2026 (G.S.R. 198(E), 20 March 2026), rules 203, 213, 215, 218, 219 and 245
- **Tax authority**: Central Board of Direct Taxes (CBDT) / Income Tax Department
- **Tax year covered**: 1 April 2026 to 31 March 2027 (tax year 2026-27)
- **Out of scope**: payments to non-residents (section 393(2)), salary (section 392; see `india-payroll`), virtual digital assets (see `india-crypto-tax`), rent and property purchase TDS

## Step 0: Client Onboarding Questions

Before computing any TDS figure, you MUST know:

1. **Is the client the PAYER (deductor) or the PAYEE (deductee)?** [T1] This decides the obligation: deduct, deposit and report, or check and claim the credit.
2. **Nature of the payment** [T1]: contract work (serial 6(i)), professional fees or fees for technical services (serial 6(iii)), a benefit or perquisite (serial 8(iv)), or a sale or service through an e-commerce platform (serial 8(v)).
3. **Who the payer is** [T1]: a company, firm or other entity, or an individual or HUF. An individual or HUF deducts under serial 6(i) or 6(iii) only if its business or professional turnover in the previous tax year passed the tests in Step 1; otherwise serial 6(ii) may apply.
4. **PAN of the payee** [T1]: without a valid PAN, section 397(2)(b) applies (Step 4).
5. **Legal status of the payee** [T1]: individual or HUF versus any other person (decides the contract-work rate).
6. **Amounts**: each single sum and the total for the tax year, per payee, and per serial 6(iii) category where there is more than one [T2] (threshold tests).
7. **Does the payee hold a section 395 certificate for a lower rate or no deduction?** [T2]
8. **Is the payee resident in India?** [T1] Payments to non-residents fall under section 393(2), not under this Guide. Escalate to [T3].
9. **Tax deduction and collection account number (TAN) of the payer** [T1]: section 397(1) requires one, except for the cases listed there (Step 6).

**If the payee is a non-resident, STOP. Section 393(2) applies, not serial 6. Escalate to [T3].**

## Step 1: Professional and Technical Fees (section 393(1), Table serial 6(iii)) [T1]

Serial 6(iii) covers fees for professional services, fees for technical services, remuneration or commission to a company director (other than salary), royalty, and sums referred to in section 26(2)(h). The payer in column C is a "specified person". Section 402(37) defines that as any person that is not an individual or HUF, or an individual or HUF whose business turnover or professional gross receipts in the tax year before the year of payment exceeded the limits in the table below.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate (a): fees for technical services (not professional services), royalty for sale, distribution or exhibition of films, and any sum paid to a payee engaged only in running a call centre | 2% | "Rate: (a) 2% of such of–– person. sum in case of— (a) fees for (i) fees for technical professional services" |
| Rate (b): professional fees, director remuneration or commission, other royalty, section 26(2)(h) sums, and every other serial 6(iii) case | 10% | "(b) 10% of such sum in cases other than (a)." |
| Threshold for professional fees (a), technical fees (b), royalty (d) and section 26(2)(h) sums (e): tax year amount or aggregate [T2: whether the four are tested separately or together] | INR 50,000 | "(i) for (a), (b), (d) and (e) of Col. B: ₹ 50,000." |
| Threshold for director remuneration or commission | Nil | "(ii) for (c) of Col. B: Nil." |
| "Specified person" test for an individual or HUF payer: business turnover in the previous tax year exceeded | one crore rupees | "turnover from the business or profession carried on by him exceed one crore rupees in case of business" |
| "Specified person" test for an individual or HUF payer: professional gross receipts in the previous tax year exceeded | fifty lakh rupees | "fifty lakh rupees in case of profession during the tax year immediately preceding" |

**How the threshold works.** Section 393(1)(a) requires tax "on the entire amount of such income or sum, where the amount or aggregate of amounts exceeds the threshold limit". So the test is "more than", not "at least". A tax year total equal to the threshold in the table above needs no deduction. Once the total goes above it, tax is due on the whole amount, including the part below the threshold, not only on the excess. It is a cliff, not an allowance.

The Table gives one threshold line "for (a), (b), (d) and (e)". It does not say whether professional fees and technical fees paid to the same payee are added together. [T2] where one payee receives fees in more than one of these categories.

**When to deduct.** Section 393(1)(c): at the time the sum is credited to the payee's account or at the time it is paid (in cash, by cheque, draft or any other mode), whichever is earlier.

**Personal payments.** Section 393(4), Table serial 9: no deduction under serial 6(iii) where an individual or HUF pays the fees exclusively for personal purposes.

**Tax borne by the payer.** Section 393(10): the income is increased so that after deduction it equals the net amount payable.

**Suspense account.** Section 393(11): a credit to a "suspense account" or any other account counts as credit to the payee.

### What constitutes "professional services"

Section 402(28): services rendered in the course of carrying on a legal, medical, engineering or architectural profession, the profession of accountancy, technical consultancy, interior decoration or advertising, or any other profession the Board notifies.

| Included (section 402(28)) | Excluded |
| --- | --- |
| Legal services | Salary (section 392; see `india-payroll`) |
| Medical services | Purchase of goods |
| Engineering services | Amounts payable to the Government or the Reserve Bank of India (section 393(5)) |
| Architectural services | Payments by an individual or HUF exclusively for personal purposes (section 393(4), Table serial 9) |
| Accountancy services | |
| Technical consultancy | |
| Interior decoration | |
| Advertising (the profession; advertising is also "work" under section 402(47), so see Step 2) | |
| Other professions notified by the Board (the notifications were not read for this Guide) | |

### What constitutes "fees for technical services" (rate (a))

Section 402(15) points to section 9(7)(b): any consideration for managerial, technical or consultancy services, including the services of technical or other personnel. It does NOT include consideration for a construction, assembly, mining or like project undertaken by the recipient, or consideration that is salary income of the recipient.

- **Key distinction** [T2]: professional services in the section 402(28) list take rate (b) in the table above. Fees for technical services that are not professional services take rate (a). Rate (a) covers only fees for technical services "not being a professional services", so a fee for professional services (the section 402(28) list includes technical consultancy) takes rate (b) even if it is also a technical service. [T2] whether a given service, such as software development, is a profession in that list or only a technical service.

## Step 2: Contract Work (section 393(1), Table serial 6(i)) [T1]

Serial 6(i) covers any sum paid to a resident contractor for carrying out any work (including supply of labour for carrying out any work) under a contract between the contractor and a "designated person". Section 402(11) lists designated persons: governments, local authorities, statutory corporations, companies, co-operative societies, housing and planning authorities, registered societies, trusts, universities, foreign governments and enterprises, firms, and any individual, HUF, association of persons or body of individuals whose business turnover or professional gross receipts in the previous tax year exceeded the same limits as in Step 1.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate where the contractor is an individual or HUF | 1% | "Rate: (a) 1%, if carrying out any work designated contractor is individual" |
| Rate where the contractor is any other person (company, firm, LLP, association) | 2% | "(b) 2%, if contractor of a contract between the is a person other than the" |
| Threshold: any single sum | INR 30,000 | "(a) ₹ 30000; for any such sum; and (b) ₹ 100000 in case of aggregate of such sums." |
| Threshold: aggregate of such sums in the tax year | INR 100,000 | "(a) ₹ 30000; for any such sum; and (b) ₹ 100000 in case of aggregate of such sums." |

**Threshold rule (OR, not AND).** Deduct where a single sum exceeds the single-sum threshold OR where the tax year aggregate to that contractor exceeds the aggregate threshold, both in the table above. Section 393(1)(a) then applies the rate to the entire amount, not only the excess.

**Material in the invoice.** Note to serial 6: for manufacturing or supplying a product to the customer's specification using material bought from the customer or its associate (section 402(47)(e)), tax is deducted on the invoice value excluding the material if the invoice shows the material separately, and on the whole invoice value if it does not.

**Exclusions (section 393(4), Table serial 8).** No deduction under serial 6(i):
- for a contractor in the business of plying, hiring or leasing goods carriages who owns ten or fewer goods carriages at any time in the tax year AND gives the payer a declaration with PAN, AND the payer reports the particulars to the prescribed authority; or
- where an individual or HUF pays exclusively for personal purposes.

### What constitutes "work"

Section 402(47) says "work" includes advertising; broadcasting and telecasting including programme production; carriage of goods or passengers by any mode other than railways; catering; and manufacturing or supplying a product to a customer's specification using material bought from that customer or its associate (but not using material bought from anyone other than that customer or its associate). It does not include any sum covered by serial 6(iii), so professional and technical fees are never contract work. From 1 April 2026 the Finance Act 2026 added clause (f): supply of manpower to a person to work under that person's supervision, control or direction.

| Included | Excluded |
| --- | --- |
| Manufacturing or supply of a product to the buyer's specification, using material bought from the buyer or its associate | Manufacturing to specification using material bought from someone other than the customer or its associate (section 402(47)) |
| Catering | Any sum under serial 6(iii), such as professional or technical fees (section 402(47)) |
| Carriage of goods or passengers, other than by railways | Payments to employees (salary) |
| Advertising, broadcasting and telecasting (fees for advertising as a profession fall under serial 6(iii), which section 402(47)(B) excludes from work) | Purchase of goods from the seller's stock, which is not a contract for work [T2: ordinary meaning, confirm] |
| Supply of manpower working under the customer's supervision, control or direction (from 1 April 2026) | |
| Construction, printing, housekeeping and security contracts, software written under a contract for work [T2: the Act's list is "includes", so these sit on the ordinary meaning of "work"; confirm] | |

### Serial 6(i) or serial 6(iii): decision matrix [T2]

| Nature of service | Serial | Rate |
| --- | --- | --- |
| Freelance software developer writing custom code | 6(iii) if fees for technical services or professional services; 6(i) if a contract for work | [T2] confirm which; rates in the tables above |
| Licence or subscription for the right to use computer software (including SaaS) | 6(iii)(d) royalty: section 402(30) takes the meaning in section 9(6)(b), which by section 9(6)(c)(i) includes "right to use a computer software (including granting of a licence)" | Rate (b) [T2: whether a given SaaS fee is for a right to use software or for a service] |
| IT company supplying manpower that works under the client's supervision | 6(i) (section 402(47)(f), from 1 April 2026) | Contract-work rate for the contractor's status |
| Architect designing a building | 6(iii), professional services | Rate (b) |
| Construction contractor building the design | 6(i) | Contract-work rate for the contractor's status |
| Chartered Accountant preparing accounts | 6(iii), professional services (accountancy) | Rate (b) |
| Data entry operator on contract | 6(i) [T2] | Contract-work rate for the contractor's status |

- **Mixed contract flag** [T2]: if the contract has both professional services and execution work (for example an architect who also supervises construction), flag it for a Chartered Accountant to settle the dominant nature of the contract.

### Individual or HUF payers who are not "specified" or "designated" (serial 6(ii)) [T1]

An individual or HUF that is not required to deduct under serial 6(i) or 6(iii) (or serial 1(ii)) deducts under serial 6(ii) on sums for work, professional fees, or commission or brokerage, but only above a much higher threshold.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate under serial 6(ii) | 2% | "(ii) Any sum–– Any person, Rate: 2%" |
| Threshold under serial 6(ii) | Fifty lakh rupees | "Threshold limit: supply of labour for Fifty lakh rupees." |

Such a payer does not need a TAN (section 397(1)(c)). It deposits the tax with a challan-cum-statement in Form No. 141 within thirty days from the end of the month of deduction (rule 218(3) and rule 219(5) of the Income-tax Rules 2026) and issues the certificate in Form No. 132 (rule 215).

## Step 3: E-commerce Operators (section 393(1), Table serial 8(v)) [T1]

An e-commerce operator (section 402(13): a person who owns, operates or manages a digital or electronic facility or platform for electronic commerce) deducts on the gross amount of sales of goods or provision of services by an e-commerce participant that it facilitates. An e-commerce participant (section 402(14)) is a person resident in India selling goods or providing services through such a platform. Section 402(34) says "services" here includes fees for technical services and fees for professional services.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate on the gross amount of sales or services | 0.1% | "Rate: 0.1% of gross" |
| No deduction where the participant is an individual or HUF AND gross sales or services in the tax year do not exceed this amount AND the participant has given PAN or Aadhaar to the operator (section 393(4), Table serial 11) | INR 500,000 | "gross amount of the sales or services or both during the tax year does not exceed ₹ 500000" |

### Key points (Note 3 to serial 8(v))

- The OPERATOR deducts, not the buyer. A payment the buyer makes directly to the participant for a sale or service facilitated by the operator counts as paid by the operator and is included in the gross amount.
- Serial 8(v) takes precedence over the other provisions of Chapter XIX-B. If tax was deducted under serial 8(v), or the transaction is exempt under section 393(4) Table serial 11, no tax is deducted on that transaction under any other provision. The client who books through the platform does not also deduct under serial 6.
- The precedence rule does not apply to amounts the operator itself receives for hosting advertisements or for other services not connected with the facilitated sale or service (Note 3(e)).
- The individual or HUF exemption in the table above needs all three conditions (AND). A company or firm participant has no exemption.

## Step 4: Payee Without a Valid PAN (section 397(2)) [T1]

Every person entitled to receive an amount on which tax is deductible must give the payer a valid PAN (section 397(2)(a)). If not, section 397(2)(b)(i) requires deduction at the HIGHER of the rate in the relevant provision, the rates in force, or the rate in the table below.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| No-PAN rate for e-commerce (serial 8(v)) and purchase of goods (serial 8(ii)) | 5% | "at the rate of 5% where tax is required to be deducted under section 393(1)" |
| No-PAN rate in any other case | 20% | "at the rate of 5% where tax is required to be deducted under section 393(1) [Table: Sl. No. 8(ii) or 8(v)]; or 20% in any other case" |

### Practical application

| Serial | Normal rate | Rate without PAN |
| --- | --- | --- |
| 6(iii) professional fees, rate (b) | 10% | 20% |
| 6(iii) fees for technical services, rate (a) | 2% | 20% |
| 6(i) contractor is an individual or HUF | 1% | 20% |
| 6(i) any other contractor | 2% | 20% |
| 8(v) e-commerce | 0.1% | 5% |

- **WARNING**: the no-PAN rate is a floor, not a fixed rate: it is the higher of the three. It is 5%, not 20%, for e-commerce. Without a PAN, the payee also cannot get a section 395 certificate (section 397(2)(f)(ii)). The PAN must appear on all bills, vouchers and correspondence between the two (section 397(2)(h)).

## Step 5: Benefits or Perquisites to Freelancers (section 393(1), Table serial 8(iv)) [T2]

A "specified person" (Step 1) that provides a resident with a benefit or perquisite, convertible into money or not, arising from that resident's business or profession, deducts tax on the value. Note 2 to the Table: this applies to benefits in cash, in kind or partly in each, and the provider must ensure tax has been deducted BEFORE providing the benefit.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate on the value or aggregate value of the benefit | 10% | "Rate: 10% of value or perquisite, whether person." |
| Threshold (tax year aggregate) | INR 20,000 | "of a profession of any resident. Threshold limit: ₹ 20,000." |

[T2] Valuation of a benefit in kind and how the payer funds the tax are for a Chartered Accountant.

## Step 6: TAN, Deposit and Payment to Government [T1]

- **TAN.** Every person deducting tax applies for a tax deduction and collection account number and quotes it in all challans, statements and certificates (section 397(1)(a) and (b)). Not needed by a person deducting under serial 6(ii) (and the other cases listed in section 397(1)(c)). From 1 October 2026 the Finance Act 2026 substitutes a new section 397(1)(c), which keeps the serial 6(ii) exception "in respect of a transaction" and adds cases for virtual digital assets and property bought from non-residents.
- **Deposit dates** (section 397(3)(a); rule 218 of the Income-tax Rules 2026):

| Deductor | Due date for payment to the Government |
| --- | --- |
| Office of the Government, tax paid without an income-tax challan | Same day |
| Office of the Government, tax paid with an income-tax challan | On or before seven days from the end of the month of deduction |
| Any other deductor, amount credited or paid in March | On or before 30th April |
| Any other deductor, any other month | On or before seven days from the end of the month of deduction |
| Individual or HUF deducting under serial 6(ii) | Within thirty days from the end of the month of deduction, with Form No. 141 |

## Step 7: Quarterly TDS Statement (section 397(3)(b); rule 219) [T1]

The quarterly statement for TDS on payments to residents under section 393(1) (other than serial 8(iii)) is **Form No. 140** (rule 219(1), Table serial 3). Rule 219(4) sets the due dates:

| Quarter ending | Statement due |
| --- | --- |
| 30th June | 31st July of the financial year |
| 30th September | 31st October of the financial year |
| 31st December | 31st January of the financial year |
| 31st March | 31st May of the financial year immediately following the tax year |

### Filing requirements

| Item | Detail |
| --- | --- |
| Who must file | Every person responsible for deducting tax, after paying it to the Government (section 397(3)(b)) |
| Interest | Interest for late deduction or late payment (Step 10) must be paid BEFORE the statement is filed (section 398(3)(b)) |
| Corrections | A correction statement may be delivered within two years from the end of the tax year in which the statement was due (section 397(3)(f)) |
| Serial 6(ii) deductors | No quarterly statement: Form No. 141 instead (rule 219(5)) |

### Late filing: fee and penalty

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Fee for each day the statement is late (section 427(1) as substituted by the Finance Act 2026, from 1 April 2026); total fee capped at the tax deductible and paid before the statement is delivered | INR 200 | "section 397(3)(b) within the time prescribed therein, he shall be liable to pay by way of fee, a sum of ₹ 200 for every day" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Penalty for not filing the statement on time, or for incorrect information (section 461(1)): at least | INR 10,000 | "a penalty of a sum which shall not be less than ₹10000 but which may extend to ₹100000" |
| Penalty under section 461(1): at most | INR 100,000 | "a penalty of a sum which shall not be less than ₹10000 but which may extend to ₹100000" |

No penalty for late filing under section 461(1)(a) if the person proves that the tax, with the fee and any interest, was paid to the Government AND the statement was delivered before the expiry of one month from the prescribed time (section 461(2)).

## Step 8: TDS Certificates (section 395(4); rule 215) [T1]

| Item | Detail |
| --- | --- |
| Form | Form No. 131 for deductions under section 393(1) other than serial 2(i), 3(i), 6(ii) and 8(vi); Form No. 132 for serial 6(ii) |
| Issued by | Deductor to deductee, generated and downloaded from the portal specified by the Director General of Income-tax (Systems) |
| Content | Amount of tax deducted, rate, and other prescribed particulars (section 395(4)(a)) |
| Due date, Form No. 131 | Within fifteen days from the due date for furnishing the statement under rule 219 |
| Due date, Form No. 132 | Within fifteen days from the due date for furnishing Form No. 141 |
| Duplicate | May be issued on request if the original is lost, marked as duplicate (rule 215(3)) |

## Step 9: Annual Information Statement and Credit Reconciliation [T1]

| Item | Purpose |
| --- | --- |
| Form No. 168, Annual Information Statement (rule 245) | Uploaded to the taxpayer's registered account; includes information on tax deducted or collected at source, specified financial transactions, tax payments, demands and refunds, and proceedings |
| Credit rule (rule 203) | Credit for tax deducted is given on the basis of the information the DEDUCTOR furnishes to the income-tax authority, to the person paid or credited |

### Reconciliation steps (for the payee)

1. Download the Annual Information Statement (Form No. 168) from your registered account on the income-tax portal.
2. Match each TDS entry against the payer, the invoice and the payment received.
3. Check the payer used your correct PAN and the right serial.
4. If an entry is missing or wrong, ask the payer to file a correction statement (section 397(3)(f)).
5. Claim the credit in the return of income. Section 396 treats the sums deducted as income received, so the gross fee, not the net receipt, is income.

**WARNING:** credit follows the deductor's statement (rule 203). If the payer deducted tax but did not pay it or did not file the statement, the credit does not show. The payee should pursue the payer.

## Step 10: Payer in Default: Interest and Consequences (section 398) [T1]

A person who does not deduct, or deducts but does not pay, is an assessee in default for that tax (section 398(1)).

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Interest per month or part of a month from the date tax was deductible to the date it is deducted (section 398(3)(a)(i)) | 1% | "(i) at 1% for every month or part of a month on the amount of such tax from the date on which such tax was deductible" |
| Interest per month or part of a month from the date of deduction to the date of payment (section 398(3)(a)(ii)) | 1.5% | "(ii) at 1.5% for every month or part of a month" |

- **Not in default** (section 398(2)): a payer who failed to deduct is not treated as an assessee in default if the payee filed the return of income under section 263, included the amount in it, and paid the tax due on that return, AND the payer furnishes an accountant's certificate in the prescribed form. Interest under 398(3)(a)(i) then runs to the date the payee filed the return (section 398(3)(c)).
- **Time limit** (section 398(5)): no order for failure to deduct after six years from the end of the tax year in which tax was deductible, or two years from the end of the tax year in which a correction statement was delivered, whichever is later.
- Failure to pay tax deducted to the Government can also be prosecuted under section 476, which the Finance Act 2026 substituted [T3: refer].

## Step 11: Lower or No Deduction Certificate (section 395) [T2]

- **Legislation**: section 395(1) and (6) of the 2025 Act; rule 213 of the Income-tax Rules 2026.
- **Condition**: the payee applies; the Assessing Officer issues a certificate for a lower rate or no deduction if satisfied that the payee's total income justifies it.

| Item | Detail |
| --- | --- |
| Application | Form No. 128 (rule 213(1)), filed by the payee. From 1 April 2026 it may also be filed before the prescribed income-tax authority, which can issue or reject it on electronic verification (section 395(6), inserted by the Finance Act 2026) |
| What the officer considers | Tax on the estimated income for the year, tax on income of the last four tax years, existing liabilities, and advance tax and TDS already at the payee's credit (rule 213(3)) |
| Certificate specifies | A lower rate or no deduction |
| Issued in the name of | The person responsible for deducting tax, under advice to the applicant; valid only for a specified payment from the specified deductor, up to the amount specified (rule 213(8)) |
| Many payers | Where the deductors are likely to exceed one hundred and their details are not available, the certificate may be issued in the applicant's name (rule 213(9)) |
| Validity | The period of the tax year specified in the certificate, unless cancelled earlier (rule 213(7)) |
| Deductor obligation | Deduct at the rate in the certificate, or not at all, while it is valid (section 395(1)(c)) |
| No PAN | No certificate is granted (section 397(2)(f)(ii)) |
| Nil-tax declaration | Not available for professional fees or contract work: the section 393(6) Table lists other incomes (interest, dividends, rent under serial 2(ii), insurance commission and others), not serial 6 |

### When to recommend

| Scenario | Action |
| --- | --- |
| Freelancer whose total income will be below the taxable level | Consider an application for no deduction |
| Professional with high expenses and low taxable income | Consider an application for a lower rate |
| Several payers deducting at the full rate and causing cash-flow problems | Consider an application for a lower rate |

- **CA flag** [T2]: always flag for a Chartered Accountant before advising on section 395. The application needs a projection of income and supporting documents.

## Step 12: Edge Case Registry

### EC1: Payment mixes goods and services [T2]

**Situation:** One invoice covers software development (a service) and hardware (goods).
**Resolution:** Serial 6(iii) applies to fees for services, not to the price of goods. The Act does not say how to split a single invoice. Options: deduct only on the service part where the invoice shows it separately, or on the whole amount where it does not. [T2] flag for a Chartered Accountant.

### EC2: Reimbursement of expenses in the invoice [T2]

**Situation:** A freelancer invoices consulting fees plus a separately billed travel reimbursement.
**Resolution:** The 2025 Act Table does not exclude reimbursements. Whether a separately billed, receipted reimbursement is outside the fee depends on Board guidance and case law that this Guide could not read on an allowed page. [T2] flag for a Chartered Accountant.

### EC3: Payee is a partnership firm: which contract rate? [T1]

**Situation:** Contract work paid to a partnership firm.
**Resolution:** A firm is not an individual or HUF. Use the rate for "a person other than" an individual or HUF in the Step 2 table.

### EC4: Contract aggregate threshold crossed mid-year [T2]

**Situation:** Several payments to the same contractor, none above the single-sum threshold, but the year's total goes above the aggregate threshold in the Step 2 table.
**Resolution:** Once the aggregate goes above the aggregate threshold in the Step 2 table, section 393(1)(a) requires tax "on the entire amount of such income or sum", so the earlier payments count in the amount taxed, not only the payment that crosses the line. The Act does not say whether tax on the earlier payments was "deductible" on the dates they were credited, which would start interest under section 398(3)(a)(i) from those dates, or only when the aggregate was crossed. [T2] a Chartered Accountant must confirm the timing and any interest before advising.

### EC5: Freelancer selling services through an e-commerce platform [T2]

**Situation:** A designer sells services through an online platform operated by an e-commerce operator.
**Resolution:** The operator deducts under serial 8(v) (Step 3). The hiring client does not also deduct under serial 6 for a transaction facilitated by the platform, because Note 3(d) excludes deduction under any other provision once serial 8(v) tax was deducted or the serial 11 exemption applies. If the client hires the freelancer directly, off the platform, serial 6 applies. [T2] whether a particular platform is an "e-commerce operator" facilitating the sale.

### EC6: Tax deducted but not paid by the payer [T1]

**Situation:** The payer deducted tax but did not pay it to the Government or did not file the statement. The Annual Information Statement shows no credit.
**Resolution:** Credit follows the payer's statement (rule 203). The payee should (1) ask the payer for the certificate in Form No. 131, (2) ask the payer to pay and file or correct the statement, and (3) consider the credit in the return only once it is reported. The payer remains in default and liable to interest (section 398). Section 401: where tax is deductible at source, the payee "shall not be called upon to pay the tax himself to the extent to which tax has been deducted from that income". [T2] how to show the deduction when the credit is missing.

### EC7: Several professional services to one freelancer [T1]

**Situation:** A client pays one freelancer for accounting and for tax advice in the same tax year. Each payment is below the professional-fees threshold in the Step 1 table, but the total is above it.
**Resolution:** Both are fees for professional services, the same category, so the threshold tests their tax year total. Once that total exceeds the threshold, tax applies to the entire amount, not only the excess.

### EC8: GST shown on the invoice [T2]

**Situation:** The freelancer's invoice shows the fee and GST separately.
**Resolution:** The 2025 Act Table taxes "any sum by way of fees" and does not mention GST. Whether GST shown separately is left out of the amount on which tax is deducted depends on CBDT guidance that this Guide could not read on an allowed page. Check the current CBDT circular before relying on either treatment. [T2] flag for a Chartered Accountant.

### EC9: Presumptive-scheme professional with excess TDS [T1]

**Situation:** A freelancer under the presumptive scheme for professions (section 58 of the 2025 Act; see `in-income-tax`) had more TDS deducted than the tax due for the year.
**Resolution:** The excess is refundable under section 431, and section 433 says every refund claim is made by furnishing the return under section 263. The freelancer MUST file the return to get it back.

### EC10: Benefit or perquisite given to a freelancer [T2]

**Situation:** A company gives a freelancer a laptop as part of the engagement.
**Resolution:** If the company is a specified person and the year's benefits to that freelancer exceed the threshold in the Step 5 table, tax at the Step 5 rate is due on the value, and the company must ensure it was deducted before giving the benefit (Note 2 to Table serial 8). [T2] valuation for a Chartered Accountant.

## Step 13: Reviewer Escalation Protocol

When the assistant identifies a [T2] situation:

~~~
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Chartered Accountant must confirm before advising client.
~~~

When the assistant identifies a [T3] situation:

~~~
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside Guide scope]
Action Required: Do not advise. Refer to Chartered Accountant. Document gap.
~~~

## Step 14: Test Suite

All cases are described against the thresholds and rates in the tables above; the arithmetic for hypothetical amounts is kept outside the Guide.

### Test 1: Professional fees above the threshold

**Input:** A company pays a resident freelance chartered accountant audit fees whose tax year total is above the professional-fees threshold. PAN given.
**Expected output:** Serial 6(iii), rate (b), on the entire amount. Deposit within seven days from the end of the month of deduction (30th April for a March deduction).

### Test 2: Single contract payment above the single-sum threshold

**Input:** A company makes one payment above the single-sum threshold to a resident individual contractor for office renovation. PAN given.
**Expected output:** Serial 6(i), individual or HUF rate, on that payment.

### Test 3: Professional fees at or below the threshold

**Input:** A company pays a freelance designer two professional fees whose tax year total is equal to or below the professional-fees threshold. PAN given.
**Expected output:** No deduction. The threshold is "exceeds", so a total equal to it is below the line.

### Test 4: Missing PAN

**Input:** Professional fees above the threshold; the payee has NOT given a PAN.
**Expected output:** Section 397(2)(b)(i): the higher of rate (b) and the no-PAN rate for "any other case", which is the no-PAN rate.

### Test 5: Contract aggregate crossed in the fourth quarter

**Input:** Quarterly payments to one individual contractor, none above the single-sum threshold, with the fourth payment taking the year's total above the aggregate threshold. PAN given.
**Expected output:** Tax at the individual or HUF rate on the entire year's amount once the aggregate is crossed (section 393(1)(a)). Whether interest under section 398(3)(a)(i) runs on the earlier payments is [T2].

### Test 6: Statement and certificate timeline

**Input:** TDS deducted in July, August and September.
**Expected output:** Form No. 140 for the quarter ending 30th September is due by 31st October. Form No. 131 is due within fifteen days from that due date.

## PROHIBITIONS

- NEVER apply serial 6 to payments to non-residents: section 393(2) applies (out of scope, T3).
- NEVER deduct below the applicable threshold. Check both the single-sum and the aggregate tests for contract work, and remember the test is "exceeds".
- NEVER deduct only on the excess over a threshold: section 393(1)(a) taxes the entire amount once it is crossed.
- NEVER skip the PAN check: section 397(2)(b) applies when there is no valid PAN, and it is 5%, not 20%, for e-commerce.
- NEVER apply the old non-filer higher rate: the 2025 Act has no such deduction rule (section 397(2)(b)(ii) "twice the rate" is for tax COLLECTED at source only).
- NEVER hand-make the certificate: Form No. 131 is generated and downloaded from the portal (rule 215).
- NEVER advise a payee to claim TDS credit that the payer has not reported (rule 203).
- NEVER apply the contract-work rates to professional services that fall under serial 6(iii).
- NEVER deduct under serial 6 on a transaction where the e-commerce operator deducted under serial 8(v) or serial 11 exempts it.
- NEVER estimate the outcome of a section 395 application without a Chartered Accountant.
- NEVER ignore the late statement fee under section 427: it accrues every day.
- NEVER cite 1961 Act section numbers or forms for tax year 2026-27 payments.

## The method, step by step

1. **Confirm the year and the law.** For an amount credited or paid from 1 April 2026, apply Chapter XIX-B of the Income-tax Act 2025 (section 1(3): in force from 1 April 2026; section 536 repeals the 1961 Act): https://egazette.gov.in/WriteReadData/2025/265620.pdf
2. **Classify the payment** under the section 393(1) Table: serial 6(i) contract work, 6(ii) individual payer, 6(iii) professional or technical fees, 8(iv) benefit, 8(v) e-commerce, using the definitions in section 402 (same link).
3. **Check the payer** is a specified or designated person (section 402(37) and 402(11)), and the exclusions in section 393(4) and 393(5) (same link).
4. **Test the threshold** for the tax year (section 393(1)(a)) and, if exceeded, take the entire amount (same link).
5. **Fix the rate**: the Table rate, a section 395 certificate rate, or the section 397(2)(b) no-PAN rate (same link).
6. **Deduct at credit or payment, whichever is earlier** (section 393(1)(c)), and deposit by the rule 218 date, Income-tax Rules 2026: https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
7. **File the quarterly statement** in Form No. 140 (rule 219) and issue Form No. 131 (rule 215) from the same Rules link; serial 6(ii) payers use Form No. 141 and Form No. 132.
8. **Check fees and interest** for any delay: section 427 fee as substituted by the Finance Act 2026 (https://egazette.gov.in/WriteReadData/2026/271439.pdf) and section 398(3) interest (https://egazette.gov.in/WriteReadData/2025/265620.pdf).
9. **For the payee**, reconcile the Annual Information Statement (Form No. 168, rule 245) and claim the credit (rule 203) in the return, using the Rules link in step 6.

## Ask the client first

- Are you paying, or being paid? If paying, are you a company, firm or other entity, or an individual or HUF, and what were your business turnover or professional receipts in the previous tax year? (Specified person, designated person, or serial 6(ii).)
- What exactly is the service: professional work in the section 402(28) list, technical or consultancy work, or a contract for work such as catering, transport, manpower supply or manufacturing to your specification? (Serial and rate.)
- Is the payee resident in India, and has the payee given a valid PAN? (Section 393(2) and section 397(2).)
- What is each payment, and what will the total to this payee be for the tax year? (Thresholds.)
- Was the sale or service booked through an online platform that takes the payment? (Serial 8(v).)
- Does the payee hold a section 395 certificate for this payer? (Rate.)

## When to refuse or refer

- **Non-resident payee**: section 393(2) and treaty questions. Refer [T3].
- **Salary or employee payments**: see `india-payroll`.
- **Virtual digital assets** (serial 8(vi)): see `india-crypto-tax`.
- **Amounts credited or paid before 1 April 2026**, or statements and certificates for those periods: 1961 Act rules, not covered here. Refer.
- **Prosecution** for not paying tax deducted (section 476): refer to a Chartered Accountant or lawyer.
- **Classification disputes** between serial 6(i) and 6(iii), mixed contracts, reimbursements and GST on invoices: [T2], a Chartered Accountant must confirm.
- **Section 395 applications** and anything that needs a projection of the payee's income: [T2].

## Sources

- Income-tax Act 2025 (30 of 2025), Gazette of India Extraordinary, 21 August 2025: https://egazette.gov.in/WriteReadData/2025/265620.pdf
- Finance Act 2026 (4 of 2026), assented to on 30 March 2026, Gazette of India Extraordinary: https://egazette.gov.in/WriteReadData/2026/271439.pdf
- Income-tax Rules 2026 (G.S.R. 198(E), 20 March 2026): https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained on the OpenAccountants site. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
