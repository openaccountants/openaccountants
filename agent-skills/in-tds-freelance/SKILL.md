---
name: in-tds-freelance
description: "Use this skill whenever asked about Indian TDS (Tax Deducted at Source) on payments to freelancers, contractors, or professionals. Trigger on phrases like \"TDS freelance India\", \"Section 194J\", \"Section 194C\", \"Section 194O\", \"TDS rate professional services\", \"Form 26Q\", \"Form 16A\", \"TDS certificate\", \"26AS\", \"AIS reconciliation\", \"TDS return India\", \"lower deduction certificate\", \"Section 197\", \"Section 206AA\", \"PAN not provided TDS\", or any question about TDS obligations when paying or receiving freelance/contractor payments in India. Covers Section 194J (professional/technical services), 194C (contractor payments), 194O (e-commerce), TDS return filing (Form 26Q), TDS certificates (Form 16A), Form 26AS/AIS reconciliation, higher rate for missing PAN (Section 206AA), and lower deduction certificates (Section 197). ALWAYS read this skill before touching any India TDS work involving freelancers or contractors."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/in-tds-freelance"
  jurisdiction: "IN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# India: TDS on Payments to Freelancers, Professionals and Contractors

This Guide covers tax deducted at source (TDS) when a business pays a resident freelancer, professional or contractor in India, and what the freelancer does with the credit. Figures are for tax year 2026. This means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act 2025, which replaced the Income-tax Act 1961 from 1 April 2026. The TDS rules now sit in Chapter XIX-B of the 2025 Act, mainly the Table in section 393(1), with the PAN rule, deposit and statements in section 397 and the consequences of default in section 398. The section numbers changed: this Guide cites the 2025 Act numbers and the Income-tax Rules 2026 form numbers. The earlier credit/payment event decides the Act: amounts credited or paid before 1 April 2026 fall under the 1961 Act, even if the other event is later. Section536 of the 2025 Act repeals the 1961 Act while saving its previous operation; this Guide does not cover those older transactions.

## Scope

- **Jurisdiction**: India (IN)
- **Primary legislation**: Income-tax Act 2025 (30 of 2025), Chapter XIX-B, sections 393, 395, 396, 397, 398 and 402; fees and penalties in sections 427 and 461
- **Amending law**: Finance Act 2026 (4 of 2026), sections 2 to 129 in force from 1 April 2026 unless the Act says otherwise
- **Rules**: Income-tax Rules 2026 (G.S.R. 198(E), 20 March 2026), rules 203, 213, 215, 218, 219 and 245
- **Tax authority**: Central Board of Direct Taxes (CBDT) / Income Tax Department
- **Tax year covered**: 1 April 2026 to 31 March 2027 (tax year 2026-27)
- **Out of scope**: payments to non-residents (section 393(2)), salary (section 392; see `india-payroll`), virtual digital assets (see `india-crypto-tax`), rent and property purchase TDS

**[T1] Deterministic calculation category.** Apply the stated facts and confirmed law; this internal routing tag is not professional approval or permission to skip final review.
**[T2] Reviewer judgement required.** The assistant flags and presents options. A Chartered Accountant must confirm.
**[T3] Out of scope / escalate.** Do not guess. Escalate and document.

## Ask the client first

- Are you paying, or being paid? If paying, are you a company, firm or other entity, or an individual or HUF, and what were your business turnover or professional receipts in the previous tax year? (Specified person, designated person, or serial 6(ii).)
- What exactly is the service: professional work in the section 402(28) list, technical or consultancy work, or a contract for work such as catering, transport, manpower supply or manufacturing to your specification? (Serial and rate.)
- Is the payee ordinarily resident or RNOR in India, and has the payee given a valid PAN? (Section 393(2) and section 397(2).)
- What is each payment, and what will the total to this payee be for the tax year? (Thresholds.)
- Was the sale or service booked through an online platform that takes the payment? (Serial 8(v).)
- Does the payee hold a section 395 certificate for this payer? (Rate.)

### Full onboarding record

Before computing any TDS figure, you MUST know:

1. **Is the client the PAYER (deductor) or the PAYEE (deductee)?** [T1] This decides the obligation: deduct, deposit and report, or check and claim the credit.
2. **Nature of the payment** [T1]: contract work (serial 6(i)), professional fees or fees for technical services (serial 6(iii)), a benefit or perquisite (serial 8(iv)), or a sale or service through an e-commerce platform (serial 8(v)).
3. **Who the payer is** [T1]: a company, firm or other entity, or an individual or HUF. An individual or HUF deducts under serial 6(i) or 6(iii) only if its business or professional turnover in the previous tax year passed the tests in Step 1; otherwise serial 6(ii) may apply.
4. **PAN of the payee** [T1]: without a valid PAN, section 397(2)(b) applies (Step 4).
5. **Legal status of the payee** [T1]: individual or HUF versus any other person (decides the contract-work rate).
6. **Amounts**: each single sum and the total for the tax year, per payee, and per serial 6(iii) category where there is more than one [T2] (threshold tests).
7. **Does the payee hold a section 395 certificate for a lower rate or no deduction?** [T2]
8. **Is the payee ordinarily resident, RNOR or non-resident in India?** [T1] Payments to non-residents fall under section 393(2), not under this Guide. Escalate to [T3].
9. **Tax deduction and collection account number (TAN) of the payer** [T1]: section 397(1) requires one, except for the cases listed there (Step 6).

**If the payee is a non-resident, STOP. Section 393(2) applies, not serial 6. Escalate to [T3].**

## The method, step by step

### Answer layer: classify before calculating

| Payment category, all resident-payee and payer/threshold conditions required | Current rate and threshold | Official source |
|---|---|---|
| Professional/other 6(iii) fees; qualifying technical/film/call-centre alternative | 10% ordinarily;2% specified alternatives; annual aggregate strictly aboveINR 50,000; director fees no threshold. Mixed-category aggregation held | s.393(1)serial 6(iii); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Contract work, designated payer | 1% individual/HUF contractor,2% other; single sum aboveINR 30,000 OR annual aggregate aboveINR 100,000 | s.393(1)serial 6(i); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Individual/HUF not otherwise required under 6(i)/(iii)/1(ii) | 2% whole sum if annual aggregate aboveINR 5,000,000 (in words on the page) | s.393(1)serial 6(ii); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| E-commerce | 0.1% gross; individual/HUF participant up toINR 500,000 with PAN/Aadhaar exemption; Note 4VDA priority | s.393(1)serial 8(v),393(4)serial 11; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Business/profession benefit, specified provider | 10% whole value if aggregate aboveINR 20,000; deduction before provision; Note6 tax PAID before kind/insufficient-cash release | s.393(1)serial 8(iv),Notes 2/6; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Missing validPAN | Higher of relevant rate/rates in force/20%floor;8(ii)/8(v)floor 5% | s.397(2)(b); https://egazette.gov.in/WriteReadData/2025/265620.pdf |

1. **Confirm the year and the law.** If the earlier credit/payment event is on or after 1 April 2026, apply Chapter XIX-B of the Income-tax Act 2025 (section 1(3): in force from 1 April 2026; section 536 repeals the 1961 Act): https://egazette.gov.in/WriteReadData/2025/265620.pdf
2. **Classify the payment** under the section 393(1) Table: serial 6(i) contract work, 6(ii) individual payer, 6(iii) professional or technical fees, 8(iv) benefit, 8(v) e-commerce, using the definitions in section 402 (same link).
3. **Check the payer** is a specified or designated person (section 402(37) and 402(11)), and the exclusions in section 393(4) and 393(5) (same link).
4. **Test the threshold** for the tax year (section 393(1)(a)) and, if exceeded, take the entire amount (same link).
5. **Fix the rate**: the Table rate, a section 395 certificate rate, or the section 397(2)(b) no-PAN rate (same link).
6. **Deduct at credit or payment, whichever is earlier** (section 393(1)(c)), and deposit by the rule 218 date, Income-tax Rules 2026: https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
7. **File the applicable statement**: ordinary-resident section393(1) deductions use Form No.140 (rule219) and Form No.131 (rule215); serial6(ii) uses Form No.141 and Form No.132. The RNOR section393(1) form is held pending resolution of the rule219 enumeration gap described in Step7, not automatically140 or144.
8. **Check fees and interest** for any delay: section 427 fee as substituted by the Finance Act 2026 (https://egazette.gov.in/WriteReadData/2026/271439.pdf) and section 398(3) interest (https://egazette.gov.in/WriteReadData/2025/265620.pdf).
9. **For the payee**, reconcile the Annual Information Statement (Form No. 168, rule 245) and claim the credit (rule 203) in the return, using the Rules link in step 6.

### Step 1: Professional and Technical Fees (section 393(1), Table serial 6(iii)) [T1]

Serial 6(iii) covers fees for professional services, fees for technical services, remuneration or commission to a company director (other than salary), royalty, and sums referred to in section 26(2)(h). The payer in column C is a "specified person". Section 402(37) defines that as any person that is not an individual or HUF, or an individual or HUF whose business turnover or professional gross receipts in the tax year before the year of payment exceeded the limits in the table below.

| Item | Value | Note |
| --- | --- | --- |
| Rate (a): fees for technical services (not professional services), royalty for sale, distribution or exhibition of films, and any sum paid to a payee engaged only in running a call centre | 2% | "2% of such sum"; full serial 6(iii)(a)(i)-(iii) categories; before applying confirm service classification; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate (b): professional fees, director remuneration or commission, other royalty, section 26(2)(h) sums, and every other serial 6(iii) case | 10% | "(b) 10% of such sum in cases other than (a)."; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Threshold for professional fees (a), technical fees (b), royalty (d) and section 26(2)(h) sums (e): tax year amount or aggregate [T 2: whether the four are tested separately or together] | INR 50,000 | "(i) for (a), (b), (d) and (e) of Col. B: ₹ 50,000."; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Threshold for director remuneration or commission | Nil | "(ii) for (c) of Col. B: Nil."; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| "Specified person" test for an individual or HUF payer: business turnover in the previous tax year exceeded | INR 10,000,000 (in words on the page) | "one crore rupees in case of business"; s.402(37), strict exceeds in immediately preceding year; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| "Specified person" test for an individual or HUF payer: professional gross receipts in the previous tax year exceeded | INR 5,000,000 (in words on the page) | "fifty lakh rupees in case of profession"; s.402(37), strict exceeds in immediately preceding year; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

**How the threshold works.** Section 393(1)(a) requires tax "on the entire amount of such income or sum, where the amount or aggregate of amounts exceeds the threshold limit". So the test is "more than", not "at least". A tax year total equal to the threshold in the table above needs no deduction. Once the total goes above it, tax is due on the whole amount, including the part below the threshold, not only on the excess. It is a cliff, not an allowance.

The Table gives one threshold line "for (a), (b), (d) and (e)". It does not say whether professional fees and technical fees paid to the same payee are added together. [T2] where one payee receives fees in more than one of these categories.

**When to deduct.** Section 393(1)(c): at the time the sum is credited to the payee's account or at the time it is paid (in cash, by cheque, draft or any other mode), whichever is earlier.

**Personal payments.** Section 393(4), Table serial 9: no deduction under serial 6(iii) where an individual or HUF pays the fees exclusively for personal purposes.

**Tax borne by the payer.** Section 393(10): the income is increased so that after deduction it equals the net amount payable.

**Suspense account.** Section 393(11): a credit to a "suspense account" or any other account counts as credit to the payee.

#### What constitutes "professional services"

Section 402(28): services rendered in the course of carrying on a legal, medical, engineering or architectural profession, the profession of accountancy, technical consultancy, interior decoration or advertising, or any other profession the Board notifies.

| Included (section 402(28)) | Excluded; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| Legal services | Salary (section 392; see `india-payroll`); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Medical services | Purchase of goods; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Engineering services | Amounts payable to the Government or the Reserve Bank of India (section 393(5)); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Architectural services | Payments by an individual or HUF exclusively for personal purposes (section 393(4), Table serial 9); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Accountancy services | ; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Technical consultancy | ; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Interior decoration | ; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Advertising (the profession; advertising is also "work" under section 402(47), so see Step 2) | ; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Other professions notified by the Board (the notifications were not read for this Guide) | ; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

#### What constitutes "fees for technical services" (rate (a))

Section 402(15) points to section 9(7)(b): any consideration for managerial, technical or consultancy services, including the services of technical or other personnel. It does NOT include consideration for a construction, assembly, mining or like project undertaken by the recipient, or consideration that is salary income of the recipient.

- **Key distinction** [T2]: professional services in the section 402(28) list take rate (b) in the table above. Fees for technical services that are not professional services take rate (a). Rate (a) covers only fees for technical services "not being a professional services", so a fee for professional services (the section 402(28) list includes technical consultancy) takes rate (b) even if it is also a technical service. [T2] whether a given service, such as software development, is a profession in that list or only a technical service.

### Step 2: Contract Work (section 393(1), Table serial 6(i)) [T1]

Serial 6(i) covers any sum paid to a resident contractor for carrying out any work (including supply of labour for carrying out any work) under a contract between the contractor and a "designated person". Section 402(11) lists designated persons: governments, local authorities, statutory corporations, companies, co-operative societies, housing and planning authorities, registered societies, trusts, universities, foreign governments and enterprises, firms, and any individual, HUF, association of persons or body of individuals whose business turnover or professional gross receipts in the previous tax year exceeded the same limits as in Step 1.

| Item | Value | Note |
| --- | --- | --- |
| Rate where the contractor is an individual or HUF | 1% | "1%, if contractor is individual or Hindu undivided family"; designated payer and threshold conditions; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate where the contractor is any other person (company, firm, LLP, association) | 2% | "2%, if contractor is a person other than the person mentioned in (a)"; designated payer and threshold conditions; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Threshold: any single sum | INR 30,000 | "(a) ₹ 30000; for any such sum; and (b) ₹ 100000 in case of aggregate of such sums."; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Threshold: aggregate of such sums in the tax year | INR 100,000 | "(a) ₹ 30000; for any such sum; and (b) ₹ 100000 in case of aggregate of such sums."; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

**Threshold rule (OR, not AND).** Deduct where a single sum exceeds the single-sum threshold OR where the tax year aggregate to that contractor exceeds the aggregate threshold, both in the table above. Section 393(1)(a) then applies the rate to the entire amount, not only the excess.

**Material in the invoice.** Note to serial 6: for manufacturing or supplying a product to the customer's specification using material bought from the customer or its associate (section 402(47)(e)), tax is deducted on the invoice value excluding the material if the invoice shows the material separately, and on the whole invoice value if it does not.

**Exclusions (section 393(4), Table serial 8).** No deduction under serial 6(i):
- for a contractor in the business of plying, hiring or leasing goods carriages who owns 10 or fewer (in words on the page) goods carriages at any time in the tax year AND gives the payer a declaration with PAN, AND the payer reports the particulars to the prescribed authority; or
- where an individual or HUF pays exclusively for personal purposes.

#### What constitutes "work"

Section 402(47) says "work" includes advertising; broadcasting and telecasting including programme production; carriage of goods or passengers by any mode other than railways; catering; and manufacturing or supplying a product to a customer's specification using material bought from that customer or its associate (but not using material bought from anyone other than that customer or its associate). It does not include any sum covered by serial 6(iii), so professional and technical fees are never contract work. From 1 April 2026 the Finance Act 2026 added clause (f): supply of manpower to a person to work under that person's supervision, control or direction.

| Included | Excluded; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| Manufacturing or supply of a product to the buyer's specification, using material bought from the buyer or its associate | Manufacturing to specification using material bought from someone other than the customer or its associate (section 402(47)); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Catering | Any sum under serial 6(iii), such as professional or technical fees (section 402(47)); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Carriage of goods or passengers, other than by railways | Payments to employees (salary); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Advertising, broadcasting and telecasting (fees for advertising as a profession fall under serial 6(iii), which section 402(47)(B) excludes from work) | Purchase of goods from the seller's stock, which is not a contract for work [T 2: ordinary meaning, confirm]; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Supply of manpower working under the customer's supervision, control or direction (from 1 April 2026) | ; https://egazette.gov.in/WriteReadData/2025/265620.pdf; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Construction, printing, housekeeping and security contracts, software written under a contract for work [T 2: the Act's list is "includes", so these sit on the ordinary meaning of "work"; confirm] | ; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

#### Serial 6(i) or serial 6(iii): decision matrix [T2]

| Nature of service | Serial | Rate; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- | --- |
| Freelance software developer writing custom code | 6(iii) if fees for technical services or professional services; 6(i) if a contract for work | [T2] confirm which; rates in the tables above; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Licence or subscription for the right to use computer software (including SaaS) | 6(iii)(d) royalty: section 402(30) takes the meaning in section 9(6)(b), which by section 9(6)(c)(i) includes "right to use a computer software (including granting of a licence)" | Rate (b) [T 2: whether a given SaaS fee is for a right to use software or for a service]; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| IT company supplying manpower that works under the client's supervision | 6(i) (section 402(47)(f), from 1 April 2026) | Contract-work rate for the contractor's status; https://egazette.gov.in/WriteReadData/2025/265620.pdf; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Architect designing a building | 6(iii), professional services | Rate (b); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Construction contractor building the design | 6(i) | Contract-work rate for the contractor's status; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Chartered Accountant preparing accounts | 6(iii), professional services (accountancy) | Rate (b); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Data entry operator on contract | 6(i) [T2] | Contract-work rate for the contractor's status; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

- **Mixed contract flag** [T2]: if the contract has both professional services and execution work (for example an architect who also supervises construction), flag it for a Chartered Accountant to settle the dominant nature of the contract.

#### Individual or HUF payers who are not "specified" or "designated" (serial 6(ii)) [T1]

An individual or HUF that is not required to deduct under serial 6(i) or 6(iii) (or serial 1(ii)) deducts under serial 6(ii) on sums for work, professional fees, or commission or brokerage, but only above a much higher threshold.

| Item | Value | Note |
| --- | --- | --- |
| Rate under serial 6(ii) | 2% | "Rate: 2%"; individual/HUF not otherwise required under 6(i)/(iii)/1(ii), whole sum after aggregate threshold; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Threshold under serial 6(ii) | INR 5,000,000 (in words on the page) | "Fifty lakh rupees"; strict exceeds annual aggregate, qualifying individual/HUF payer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

Such a payer does not need a TAN (section 397(1)(c)). It deposits the tax with a challan-cum-statement in Form No. 141 within 30 days (in words on the page) from the end of the month of deduction (rule 218(3) and rule 219(5) of the Income-tax Rules 2026) and issues the certificate in Form No. 132 (rule 215).

### Step 3: E-commerce Operators (section 393(1), Table serial 8(v)) [T1]

An e-commerce operator (section 402(13): a person who owns, operates or manages a digital or electronic facility or platform for electronic commerce) deducts on the gross amount of sales of goods or provision of services by an e-commerce participant that it facilitates. An e-commerce participant (section 402(14)) is a person resident in India selling goods or providing services through such a platform. Section 402(34) says "services" here includes fees for technical services and fees for professional services.

| Item | Value | Note |
| --- | --- | --- |
| Rate on the gross amount of sales or services | 0.1% | "Rate: 0.1% of gross"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| No deduction where the participant is an individual or HUF AND gross sales or services in the tax year do not exceed this amount AND the participant has given PAN or Aadhaar to the operator (section 393(4), Table serial 11) | INR 500,000 | "gross amount of the sales or services or both during the tax year does not exceed ₹ 500000"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

#### Key points (Note 3 to serial 8(v))

- The OPERATOR deducts, not the buyer. A payment the buyer makes directly to the participant for a sale or service facilitated by the operator counts as paid by the operator and is included in the gross amount.
- Serial 8(v) takes precedence over the other provisions of Chapter XIX-B. If tax was deducted under serial 8(v), or the transaction is exempt under section 393(4) Table serial 11, no tax is deducted on that transaction under any other provision. The client who books through the platform does not also deduct under serial 6.
- The precedence rule does not apply to amounts the operator itself receives for hosting advertisements or for other services not connected with the facilitated sale or service (Note 3(e)).
- The individual or HUF exemption in the table above needs all three conditions (AND). A company or firm participant has no exemption.

### Step 4: Payee Without a Valid PAN (section 397(2)) [T1]

Every person entitled to receive an amount on which tax is deductible must give the payer a valid PAN (section 397(2)(a)). If not, section 397(2)(b)(i) requires deduction at the HIGHER of the rate in the relevant provision, the rates in force, or the rate in the table below.

| Item | Value | Note |
| --- | --- | --- |
| No-PAN rate for e-commerce (serial 8(v)) and purchase of goods (serial 8(ii)) | 5% | "at the rate of 5% where tax is required to be deducted under section 393(1)"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| No-PAN rate in any other case | 20% | "at the rate of 5% where tax is required to be deducted under section 393(1) [Table: Sl. No. 8(ii) or 8(v)]; or 20% in any other case"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

#### Practical application

| Serial | Normal rate | Rate without PAN; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- | --- |
| 6(iii) professional fees, rate (b) | 10% | 20%; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| 6(iii) fees for technical services, rate (a) | 2% | 20%; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| 6(i) contractor is an individual or HUF | 1% | 20%; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| 6(i) any other contractor | 2% | 20%; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| 8(v) e-commerce | 0.1% | 5%; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

- **WARNING**: the no-PAN rate is a floor, not a fixed rate: it is the higher of the three. It is 5%, not 20%, for e-commerce. Without a PAN, the payee also cannot get a section 395 certificate (section 397(2)(f)(ii)). The PAN must appear on all bills, vouchers and correspondence between the two (section 397(2)(h)).

### Step 5: Benefits or Perquisites to Freelancers (section 393(1), Table serial 8(iv)) [T2]

A "specified person" (Step 1) that provides a resident with a benefit or perquisite, convertible into money or not, arising from that resident's business or profession, deducts tax on the value. Note2 covers cash, kind or mixed benefits and requires deduction before provision. Note6 additionally requires the provider to ensure the required tax has been PAID before releasing a wholly-in-kind benefit, or a mixed benefit whose cash part cannot meet the whole tax liability.

| Item | Value | Note |
| --- | --- | --- |
| Rate on the value or aggregate value of the benefit | 10% | "10% of value or aggregate of values"; specified provider, business/profession benefit; ensure deduction before providing and Note6 tax paid before wholly-kind/insufficient-cash release; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Threshold (tax year aggregate) | INR 20,000 | "20,000"; strict exceeds, whole value after threshold; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

[T2] Valuation of a benefit in kind and how the payer funds the tax are for a Chartered Accountant.

### Step 6: TAN, Deposit and Payment to Government [T1]

- **TAN.** Every person deducting tax applies for a tax deduction and collection account number and quotes it in all challans, statements and certificates (section 397(1)(a) and (b)). Not needed by a person deducting under serial 6(ii) (and the other cases listed in section 397(1)(c)). From 1 October 2026 the Finance Act 2026 substitutes a new section 397(1)(c), which keeps the serial 6(ii) exception "in respect of a transaction" and adds cases for virtual digital assets and property bought from non-residents.
- **Deposit dates** (section 397(3)(a); rule 218 of the Income-tax Rules 2026):

| Deductor | Due date for payment to the Government |
| --- | --- |
| Office of the Government, tax paid without an income-tax challan | Same day; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Office of the Government, tax paid with an income-tax challan | On or before 7 days (in words on the page) from the end of the month of deduction; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Any other deductor, amount credited or paid in March | On or before 30th April; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Any other deductor, any other month | On or before 7 days (in words on the page) from the end of the month of deduction; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Individual or HUF deducting under serial 6(ii) | Within 30 days (in words on the page) from the end of the month of deduction, with Form No. 141; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

### Step 7: Quarterly TDS Statement (section 397(3)(b); rule 219) [T1]

The ordinary-resident section393(1) quarterly route (other than serial8(iii), and subject to the serial6(ii) Form141 exception) is **Form No.140**, rule219(1) Table serial3. **RNOR section393(1) form held:** serial2 names RNOR deductees but enumerates only392(7),393(2),393(3), not393(1); serial3 enumerates393(1) but excludes deductees referred to in serial2. Do not silently add393(1) to serial2 or choose140/144 without authoritative clarification. Rule219(4) sets ordinary quarterly dates:

| Quarter ending | Statement due |
| --- | --- |
| 30th June | 31st July of the financial year; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| 30th September | 31st October of the financial year; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| 31st December | 31st January of the financial year; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| 31st March | 31st May of the financial year immediately following the tax year; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

#### Filing requirements

| Item | Detail |
| --- | --- |
| Who must file | Every person responsible for deducting tax, after paying it to the Government (section 397(3)(b)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Interest | Interest for late deduction or late payment (Step 10) must be paid BEFORE the statement is filed (section 398(3)(b)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Corrections | A correction statement may be delivered within 2 years (in words on the page) from the end of the tax year in which the statement was due (section 397(3)(f)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Serial 6(ii) deductors | No quarterly statement for that transaction: Form No. 141 instead (rule 219(5)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

#### Late filing: fee and penalty

| Item | Value | Note |
| --- | --- | --- |
| Fee for each day the statement is late (section 427(1) as substituted by the Finance Act 2026, from 1 April 2026); total fee capped at the tax deductible and paid before the statement is delivered | INR 200 | "section 397(3)(b) within the time prescribed therein, he shall be liable to pay by way of fee, a sum of ₹ 200 for every day"; https://egazette.gov.in/WriteReadData/2026/271439.pdf; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

| Item | Value | Note |
| --- | --- | --- |
| Penalty for not filing the statement on time, or for incorrect information (section 461(1)): at least | INR 10,000 | "a penalty of a sum which shall not be less than ₹10000 but which may extend to ₹100000"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Penalty under section 461(1): at most | INR 100,000 | "a penalty of a sum which shall not be less than ₹10000 but which may extend to ₹100000"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

No penalty for late filing under section 461(1)(a) if the person proves that the tax, with the fee and any interest, was paid to the Government AND the statement was delivered before the expiry of 1 month (in words on the page) from the prescribed time (section 461(2)).

### Step 8: TDS Certificates (section 395(4); rule 215) [T1]

| Item | Detail |
| --- | --- |
| Form | Form No. 131 for deductions under section 393(1) other than serial 2(i), 3(i), 6(ii) and 8(vi); Form No. 132 for serial 6(ii); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Issued by | Deductor to deductee, generated and downloaded from the portal specified by the Director General of Income-tax (Systems); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Content | Amount of tax deducted, rate, and other prescribed particulars (section 395(4)(a)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Due date, Form No. 131 | Within 15 days (in words on the page) from the due date for furnishing the statement under rule 219; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Due date, Form No. 132 | Within 15 days (in words on the page) from the due date for furnishing Form No. 141; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Duplicate | Form 131 may be issued on request if the original is lost, certified as duplicate; rule 215(3) does not list Form 132; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

### Step 9: Annual Information Statement and Credit Reconciliation [T1]

| Item | Purpose |
| --- | --- |
| Form No. 168, Annual Information Statement (rule 245) | Uploaded to the taxpayer's registered account; includes information on tax deducted or collected at source, specified financial transactions, tax payments, demands and refunds, and proceedings; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Credit rule (rule 203) | Credit for TDS paid to the Government follows deductor information and return claim, subject to verification; ordinarily to person paid/credited, with rule 203(2)-(6) other-person declarations and assessable-year/proportionate allocation; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

#### Reconciliation steps (for the payee)

1. Download the Annual Information Statement (Form No. 168) from your registered account on the income-tax portal.
2. Match each TDS entry against the payer, the invoice and the payment received.
3. Check the payer used your correct PAN and the right serial.
4. If an entry is missing or wrong, ask the payer to file a correction statement (section 397(3)(f)).
5. Match credit to the tax year in which the income is assessable; if spread over years, allocate proportionately under rule 203(5)-(6). An other-person declaration under rule 203(2)-(4) changes the recipient of the credit and certificate. Claim the supported credit in the return of income. Section 396 treats the sums deducted as income received, so the gross fee, not the net receipt, is income.

**WARNING:** credit follows the deductor's statement (rule 203). If the payer deducted tax but did not pay it or did not file the statement, the credit does not show. The payee should pursue the payer and obtain professional help for the claim/correction. Section 401 separately bars collecting the same tax directly from the payee to the extent actually deducted; absence from the statement is not proof that no deduction occurred or that the payee must pay it again.

### Step 10: Payer in Default: Interest and Consequences (section 398) [T1]

A person who does not deduct, or deducts but does not pay, is an assessee in default for that tax (section 398(1)).

| Item | Value | Note |
| --- | --- | --- |
| Interest per month or part of a month from the date tax was deductible to the date it is deducted (section 398(3)(a)(i)) | 1% | "(i) at 1% for every month or part of a month on the amount of such tax from the date on which such tax was deductible"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Interest per month or part of a month from the date of deduction to the date of payment (section 398(3)(a)(ii)) | 1.5% | "(ii) at 1.5% for every month or part of a month"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

- **Not in default** (section 398(2)): a payer who failed to deduct is not treated as an assessee in default if the payee filed the return of income under section 263, included the amount in it, and paid the tax due on that return, AND the payer furnishes an accountant's certificate in the prescribed form. Interest under 398(3)(a)(i) then runs to the date the payee filed the return (section 398(3)(c)).
- **Time limit** (section 398(5)): no order for failure to deduct after 6 years (in words on the page) from the end of the tax year in which tax was deductible, or 2 years (in words on the page) from the end of the tax year in which a correction statement was delivered, whichever is later.
- Failure to pay tax deducted to the Government can also be prosecuted under section 476, which the Finance Act 2026 substituted [T 3: refer].

### Step 11: Lower or No Deduction Certificate (section 395) [T2]

- **Legislation**: section 395(1) and (6) of the 2025 Act; rule 213 of the Income-tax Rules 2026.
- **Condition**: the payee applies; the Assessing Officer issues a certificate for a lower rate or no deduction if satisfied that the payee's total income justifies it.

| Item | Detail |
| --- | --- |
| Application | Form No. 128 (rule 213(1)), filed by the payee. From 1 April 2026 it may also be filed before the prescribed income-tax authority, which can issue or reject it on electronic verification (section 395(6), inserted by the Finance Act 2026); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| What the officer considers | Tax on the estimated income for the year, tax on income of the last 4 tax years (in words on the page), existing liabilities, and advance tax and TDS already at the payee's credit (rule 213(3)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Certificate specifies | A lower rate or no deduction; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Issued in the name of | The person responsible for deducting tax, under advice to the applicant; valid only for a specified payment from the specified deductor, up to the amount specified (rule 213(8)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Many payers | Where the deductors are likely to exceed 100 (in words on the page) and their details are not available, the certificate may be issued in the applicant's name (rule 213(9)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Validity | The period of the tax year specified in the certificate, unless cancelled earlier (rule 213(7)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Deductor obligation | Deduct at the rate in the certificate, or not at all, while it is valid (section 395(1)(c)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| No PAN | No certificate is granted (section 397(2)(f)(ii)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Nil-tax declaration | Not available for professional fees or contract work: the section 393(6) Table lists other incomes (interest, dividends, rent under serial 2(ii), insurance commission and others), not serial 6; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

#### When to recommend

| Scenario | Action |
| --- | --- |
| Freelancer whose total income will be below the taxable level | Consider an application for no deduction; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Professional with high expenses and low taxable income | Consider an application for a lower rate; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Several payers deducting at the full rate and causing cash-flow problems | Consider an application for a lower rate; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

- **CA flag** [T2]: always flag for a Chartered Accountant before advising on section 395. The application needs a projection of income and supporting documents.

#### Confirmed conditions and remaining boundaries

- Earlier credit or payment controls, including suspense accounts. For March 2026credit/Aprilpayment use the older Act; for an event on/after 1April 2026 use current law. No duplicate deduction for the same sum solely on the later event. [s.393(1),(11),536](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Tax Payments FAQ 3-6](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq).
- Section 393(5) also exempts amounts payable to a qualifying Central-Act corporation exempt on its income and a specified mutual fund, not merely Government/RBI; section 393(9) covers payment for/on behalf of New Pension System Trust. Check the actual statutory identity before claiming the exemption. The serial 6(i)/(iii) personal-purpose exceptions do not automatically excuse a large personal payment covered independently by serial 6(ii). [s.393(4)-(6),(9)](https://egazette.gov.in/WriteReadData/2025/265620.pdf).
- E-commerce precedence is subject to Note 4: if serial 8(v) and VDA serial 8(vi) both apply, only 8(vi) deduction applies; send VDA to `india-crypto-tax`. Direct buyer payments for facilitated sales still count; advertising/unconnected operator services are excluded from the no-duplicate rule. A website alone does not settle operator/participant classification. [s.393(1),Notes 3-6](https://egazette.gov.in/WriteReadData/2025/265620.pdf).
- Rule219(1) has an unresolved enumeration gap for RNOR section393(1) deductions: serial2 names RNOR but not393(1), while serial3 excludes the serial2 deductees. Hold the RNOR form pending clarification, preserving the ordinary140 route and specific exceptions. Serial 6(ii) transactions use Form 141 instead of a quarterly form; rule 218(3)/219(5)30 day monthly-end limit and rule 21515 day certificate limit apply. Duplicate-certificate permission in rule 215(3) lists 130/131/133, not 132. [rules 215,218,219](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).
- The no-PAN practical rates assume the stated provision/rates-in-force do not exceed the displayed floor; use the higher of all 3, not a universal fixed 20%/5%. PAN validity/inoperative status needs period-specific confirmation. Rule 203 credit follows assessability year and proportionate multi-year allocation, not simply deduction year; other-person declarations alter credit/certificate recipient. Section 401 preserves protection for amounts actually deducted. [ss.397,401](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [rule 203](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).
- Interest/default time limits in s.398(5) are subject to s.398(6) importing ss.286(1),(3); do not treat the displayed 6/2 year endpoints as unconditional in extended/excluded-period cases. Section 398(4) charges unpaid deducted tax plus interest on payer assets. Payer-default relief requires all payee-return/inclusion/payment facts and accountant certificate; interest still runs to payee return date. No criminal penalty computation is provided here. [s.398](https://egazette.gov.in/WriteReadData/2025/265620.pdf).
- Rule 245 uploads information held by the authority within 90 days from the end of the month it is received; the statement is not proof that all underlying income or deductions have been captured. [rule 245](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).

### Step 12: Edge Case Registry

#### EC 1: Payment mixes goods and services [T2]

**Situation:** One invoice covers software development (a service) and hardware (goods).
**Resolution:** Serial 6(iii) applies to fees for services, not to the price of goods. The Act does not say how to split a single invoice. Options: deduct only on the service part where the invoice shows it separately, or on the whole amount where it does not. [T2] flag for a Chartered Accountant.

#### EC 2: Reimbursement of expenses in the invoice [T2]

**Situation:** A freelancer invoices consulting fees plus a separately billed travel reimbursement.
**Resolution:** The 2025 Act Table does not exclude reimbursements. Whether a separately billed, receipted reimbursement is outside the fee depends on Board guidance and case law that this Guide could not read on an allowed page. [T2] flag for a Chartered Accountant.

#### EC 3: Payee is a partnership firm: which contract rate? [T1]

**Situation:** Contract work paid to a partnership firm.
**Resolution:** A firm is not an individual or HUF. Use the rate for "a person other than" an individual or HUF in the Step 2 table.

#### EC 4: Contract aggregate threshold crossed mid-year [T2]

**Situation:** Several payments to the same contractor, none above the single-sum threshold, but the year's total goes above the aggregate threshold in the Step 2 table.
**Resolution:** Once the aggregate goes above the aggregate threshold in the Step 2 table, section 393(1)(a) requires tax "on the entire amount of such income or sum", so the earlier payments count in the amount taxed, not only the payment that crosses the line. The Act does not say whether tax on the earlier payments was "deductible" on the dates they were credited, which would start interest under section 398(3)(a)(i) from those dates, or only when the aggregate was crossed. [T2] a Chartered Accountant must confirm the timing and any interest before advising.

#### EC 5: Freelancer selling services through an e-commerce platform [T2]

**Situation:** A designer sells services through an online platform operated by an e-commerce operator.
**Resolution:** The operator deducts under serial 8(v) (Step 3). The hiring client does not also deduct under serial 6 for a transaction facilitated by the platform, because Note 3(d) excludes deduction under any other provision once serial 8(v) tax was deducted or the serial 11 exemption applies. If the client hires the freelancer directly, off the platform, serial 6 applies. [T2] whether a particular platform is an "e-commerce operator" facilitating the sale.

#### EC 6: Tax deducted but not paid by the payer [T1]

**Situation:** The payer deducted tax but did not pay it to the Government or did not file the statement. The Annual Information Statement shows no credit.
**Resolution:** Credit follows the payer's statement (rule 203). The payee should (1) ask the payer for the certificate in Form No. 131, (2) ask the payer to pay and file or correct the statement, and (3) obtain professional advice on how to show and substantiate the deduction/credit while the statement is corrected. Do not fabricate a reported credit or automatically pay the same deducted amount again. The payer remains in default and liable to interest (section 398). Section 401: where tax is deductible at source, the payee "shall not be called upon to pay the tax himself to the extent to which tax has been deducted from that income". [T2] how to show the deduction when the credit is missing.

#### EC 7: Several professional services to one freelancer [T1]

**Situation:** A client pays one freelancer for accounting and for tax advice in the same tax year. Each payment is below the professional-fees threshold in the Step 1 table, but the total is above it.
**Resolution:** Both are fees for professional services, the same category, so the threshold tests their tax year total. Once that total exceeds the threshold, tax applies to the entire amount, not only the excess.

#### EC 8: GST shown on the invoice [T2]

**Situation:** The freelancer's invoice shows the fee and GST separately.
**Resolution:** The 2025 Act Table taxes "any sum by way of fees" and does not mention GST. Whether GST shown separately is left out of the amount on which tax is deducted depends on CBDT guidance that this Guide could not read on an allowed page. Check the current CBDT circular before relying on either treatment. [T2] flag for a Chartered Accountant.

#### EC 9: Presumptive-scheme professional with excess TDS [T1]

**Situation:** A freelancer under the presumptive scheme for professions (section 58 of the 2025 Act; see `india-income-tax`) had more TDS deducted than the tax due for the year.
**Resolution:** The excess is refundable under section 431, and section 433 says every refund claim is made by furnishing the return under section 263. The freelancer MUST file the return to get it back.

#### EC 10: Benefit or perquisite given to a freelancer [T2]

**Situation:** A company gives a freelancer a laptop as part of the engagement.
**Resolution:** If the company is a specified person and the year's benefits to that freelancer exceed the threshold in the Step 5 table, tax at the Step 5 rate is due on the value, and the company must ensure deduction before provision (Note2) and, because it is in kind, that the required tax has been PAID before release (Note6). [T2] valuation for a Chartered Accountant.

## Worked cases

Hypothetical inputs and derived outputs below assume resident ordinary deductee, company payer, validPAN except explicitly changed, no lower certificate, no separateGST/reimbursement, and correct service classification. Values are INR. These are deduction computations, not final income-tax liabilities.

### Case 1: professional threshold equality and missing PAN

Professional fees total 50,000 exactly: no TDS. At 50,100 the whole amount is taxed at 10%=5,010, leaving 45,090 cash. If validPAN is missing and no higher rates-in-force apply, the 20%floor makes TDS 10,020, cash 40,080. Do not tax only the100excess. This assumes a single professional-fee category, so it does not settle the mixed-category threshold referral. [s.393(1)serial 6(iii),397(2)](https://egazette.gov.in/WriteReadData/2025/265620.pdf).

```oa-check
name: India professional threshold and PAN deduction decision
inputs:
  exact_threshold: 50000
  above_threshold: 50100
steps:
  exact_tds: 0 * exact_threshold
  normal_tds: above_threshold * 0.10
  normal_net: above_threshold - normal_tds
  missing_pan_tds: above_threshold * 0.20
  missing_pan_net: above_threshold - missing_pan_tds
expected:
  exact_tds: 0
  normal_tds: 5010
  normal_net: 45090
  missing_pan_tds: 10020
  missing_pan_net: 40080
```

### Case 2: aggregate contract threshold changes the result

Individual contractor receives 4 sums of 28,000: each below 30,000 but total 112,000 exceeds 100,000. Deduction is 1% of the entire 112,000=1,120, not 1% of the 12,000 excess. After 3 such payments total 84,000 had not crossed either test. If the contractor is a firm the same whole 112,000 is taxed at 2%=2,240. Timing of deduction/interest on earlier payments remains the explicit EC 4 referral; this arithmetic does not backdate a liability automatically. [s.393(1)serial 6(i),398](https://egazette.gov.in/WriteReadData/2025/265620.pdf).

```oa-check
name: India contractor aggregate threshold and status comparison
inputs:
  payment: 28000
  threshold: 100000
steps:
  first_three: payment * 3
  aggregate: payment * 4
  excess: aggregate - threshold
  individual_tds: aggregate * 0.01
  firm_tds: aggregate * 0.02
  wrong_excess_only: excess * 0.01
expected:
  first_three: 84000
  aggregate: 112000
  excess: 12000
  individual_tds: 1120
  firm_tds: 2240
  wrong_excess_only: 120
```

### Original qualitative test suite

All cases are described against the thresholds and rates in the tables above; the added worked cases above show hypothetical arithmetic in this Guide.

#### Test 1: Professional fees above the threshold

**Input:** A company pays a resident freelance chartered accountant audit fees whose tax year total is above the professional-fees threshold. PAN given.
**Expected output:** Serial 6(iii), rate (b), on the entire amount. Deposit within 7 days (in words on the page) from the end of the month of deduction (30th April for a March deduction).

#### Test 2: Single contract payment above the single-sum threshold

**Input:** A company makes one payment above the single-sum threshold to a resident individual contractor for office renovation. PAN given.
**Expected output:** Serial 6(i), individual or HUF rate, on that payment.

#### Test 3: Professional fees at or below the threshold

**Input:** A company pays a freelance designer two professional fees whose tax year total is equal to or below the professional-fees threshold. PAN given.
**Expected output:** No deduction. The threshold is "exceeds", so a total equal to it is below the line.

#### Test 4: Missing PAN

**Input:** Professional fees above the threshold; the payee has NOT given a PAN.
**Expected output:** Section 397(2)(b)(i): the highest of the relevant provision rate, rates in force, and20% for this ordinary professional-fee case. With an explicit assumption that no higher rates-in-force rate applies, the result is20%.

#### Test 5: Contract aggregate crossed in the fourth quarter

**Input:** Quarterly payments to one individual contractor, none above the single-sum threshold, with the fourth payment taking the year's total above the aggregate threshold. PAN given.
**Expected output:** Tax at the individual or HUF rate on the entire year's amount once the aggregate is crossed (section 393(1)(a)). Whether interest under section 398(3)(a)(i) runs on the earlier payments is [T2].

#### Test 6: Statement and certificate timeline

**Input:** Ordinary-resident deductee; only section393(1) serial6(i)/6(iii)/8(iv)/8(v) deductions, made in July, August and September.
**Expected output:** Form No. 140 for the quarter ending 30th September is due by 31st October. Form No. 131 is due within 15 days (in words on the page) from that due date.

## When to refuse or refer

- **Non-resident payee**: section 393(2) and treaty questions. Refer [T3].
- **Salary or employee payments**: see `india-payroll`.
- **Virtual digital assets** (serial 8(vi)): see `india-crypto-tax`.
- **Amounts credited or paid before 1 April 2026**, or statements and certificates for those periods: 1961 Act rules, not covered here. Refer.
- **Prosecution** for not paying tax deducted (section 476): refer to a Chartered Accountant or lawyer.
- **Classification disputes** between serial 6(i) and 6(iii), mixed contracts, reimbursements and GST on invoices: [T2], a Chartered Accountant must confirm.
- **Section 395 applications** and anything that needs a projection of the payee's income: [T2].

### Reviewer escalation protocol

When the assistant identifies a [T2] situation:

~~~
REVIEWER FLAG
Tier: T 2
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
Tier: T 3
Client: [name]
Situation: [description]
Issue: [outside Guide scope]
Action Required: Do not advise. Refer to Chartered Accountant. Document gap.
~~~

## Filing and payment

Use the applicable current-Act form/tab and supported official statement utility for the deduction event. Deduct at the earlier credit/payment event; deposit under rule 218, furnish ordinary Form140 or the applicable Form141 exception under rule219; hold RNOR393(1) form selection until the enumeration gap is resolved, then issue the rule 215 certificate by its deadline. Retain receipt, statement acknowledgement and portal-generated certificate; reconcile PAN, period, amount, serial and credit year. Final portal field names, current extensions, filing modes and authorized account access must be confirmed before submission; these instructions do not authorize filing/payment. [rules 215,218,219](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf).

## Completion checklist

- Confirm payer/payee roles, residence including RNOR, classification, period and earlier deduction event.
- Verify specified/designated payer tests, personal-payment versus serial 6(ii) boundary, all thresholds, PAN and any valid certificate.
- Recompute whole-sum TDS, gross-up if contracted, platform/VDA precedence and kind-benefit funding.
- Match deposit, statement, certificate and payee credit to correct period/person/year; do not conceal an unmatched deduction or duplicate tax.
- Record interest/fees/penalty/referrals separately and preserve evidence.
- Obtain professional confirmation for every T 2/T 3 flag before advice/submission.

### Original prohibitions

- NEVER apply serial 6 to payments to non-residents: section 393(2) applies (out of scope, T 3).
- NEVER deduct below the applicable threshold. Check both the single-sum and the aggregate tests for contract work, and remember the test is "exceeds".
- NEVER deduct only on the excess over a threshold: section 393(1)(a) taxes the entire amount once it is crossed.
- NEVER skip the PAN check: section 397(2)(b) applies when there is no valid PAN, and it is 5%, not 20%, for e-commerce.
- NEVER apply the old non-filer higher rate: the 2025 Act has no such deduction rule (section 397(2)(b)(ii) "twice the rate" is for tax COLLECTED at source only).
- NEVER hand-make the certificate: Form No. 131 is generated and downloaded from the portal (rule 215).
- NEVER present an unreported credit as statement-matched or fabricate it. Preserve section 401 protection for tax actually deducted; escalate substantiation and return treatment rather than imposing an absolute forfeiture of credit (rule 203; section 401).
- NEVER apply the contract-work rates to professional services that fall under serial 6(iii).
- NEVER deduct under serial 6 on a transaction where the e-commerce operator deducted under serial 8(v) or serial 11 exempts it.
- NEVER estimate the outcome of a section 395 application without a Chartered Accountant.
- NEVER ignore the late statement fee under section 427: it accrues every day.
- NEVER cite 1961 Act section numbers or forms for tax year 2026-27 payments.

## Sources

| Official source | Read for | Actual read date |
|---|---|---|
| https://egazette.gov.in/WriteReadData/2025/265620.pdf | Read for s.9(6)-(7); s.393(1)serial 6/8andNotes,393(4)serial 8-12,393(5)-(11),395-398,400-402relevant definitions 10-15/28/30/34/37/47,431-433 and 461: complete operative paragraphs and neighboring exceptions; not wholeAct | 2026-11-14 |
| https://egazette.gov.in/WriteReadData/2026/271439.pdf | Read for s.1 commencement,84-90,96 and 111: current TDS amendments/certificates/TAN Oct 2026/manpower/fee/prosecution; no unchanged blanket 1961rules projected | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf | Read for entire rules 203,213,215,218,219,245 including neighboring exclusions/other-person allocation/RNORforms/duplicatecertificates; partial neighboring 214/216 read but not new obligations inferred | 2026-11-14 |
| https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/tax-payments-faq | Read for Q 3-6 and 14-23: earlier credit/payment event, TDStransition, current 393references/Form 168; not old-year rate guidance | 2026-11-14 |

**Not yet confirmed:** RNOR section393(1) statement form because rule219 serial2/3 enumerations conflict; aggregation across different 6(iii)fee categories; notified professions beyond the cited s.402(28)list; specific software/SaaS/mixed contracts and ordinary-meaning work classification; GST exclusion/reimbursements and current binding guidance; EC 4earlier-payment deduction/interest timing; benefit valuation and funding; inoperative-PAN consequences; disputed/missing-credit return treatment; actual current portal fields/modes/extensions; application-specific lower/nil-certificate outcomes and prescribed electronic-authority conditions; excluded-period s.398(6) time-limit cases. Preserve these as referrals, not usable unsupported tax rules. Older-Act transactions remain out of scope.

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained on the OpenAccountants site. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `in-tds-freelance` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/in-tds-freelance. If neither is available, confirm every figure against the official source pages cited above before relying on it.
