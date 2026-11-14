---
name: india-formation
description: "Use this skill whenever asked about forming a company or LLP in India in FY 2026-27. Trigger on phrases like set up a company in India, Pvt Ltd India, private limited company India, One Person Company, OPC, LLP India, MCA registration, SPICe+, INC-32, RUN name reservation, INC-20A, commencement of business, DIR-3 KYC, registered office verification, first auditor, Indian company formation, register a business India, foreign founder India, or any question about incorporating and the first filings after incorporation. It covers entity choice, the SPICe+ steps, post-incorporation deadlines (30-day office and first auditor, 180-day INC-20A), director KYC from 31 March 2026, annual return and AOC-4 periods and penalties, small company limits from 1 December 2025, and company income tax for tax year 2026-27 under the Income-tax Act 2025. Tier 2, not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/india-formation"
  jurisdiction: "IN"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Forming a Company or LLP in India, FY 2026-27

> **General reference only.** This skill is general reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to incorporate, file or take a tax position without review by a qualified professional (a company secretary or chartered accountant) in India.

This skill covers setting up a private limited company, a One Person Company (OPC), a public company or a limited liability partnership (LLP) in India, and the first filings after incorporation. Tax year: FY 2026-27. For Indian income tax this means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act 2025, which replaced the Income-tax Act 1961 from 1 April 2026 (Income-tax Act 2025, sections 1(3) and 536(1): https://egazette.gov.in/WriteReadData/2025/265620.pdf). Company law is not year-based: the company law rules below are those in force on 14 November 2026, with their start dates where a change is recent. The Corporate Laws (Amendment) Bill 2026 is pending in Parliament and is not law (see "Pending law" under Penalties and interest).

## Who this applies to

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Currency | INR |
| Company registrar | Ministry of Corporate Affairs (MCA) and the Registrar of Companies (ROC), filed online on the MCA portal |
| Key legislation | Companies Act 2013; Limited Liability Partnership Act 2008; Companies (Incorporation) Rules 2014; Companies (Registration Offices and Fees) Rules 2014 |
| Incorporation form for a company | SPICe+ (Form No. INC-32), with e-MoA (Form No. INC-33) and e-AoA (Form No. INC-34) |
| Company income tax | Income-tax Act 2025 and Finance Act 2026; rates in the rates table |
| Government fees and stamp duty | Not stated in this skill; see Costs under The base for where to check |

### Entity types compared

| Feature | LLP | OPC | Private Limited (Pvt Ltd) | Public Limited |
| --- | --- | --- | --- | --- |
| Separate legal entity | Yes | Yes | Yes | Yes |
| Minimum founders | Two partners, at least two designated partners who are individuals, one of them resident in India | One member (section 2(62)), plus a nominee | Check section 3(1) | Check section 3(1) |
| Maximum members | No limit in the Act | One member | Two hundred (joint holders count as one; employee members, and former employees who were members while employed and stayed members, are not counted) | No limit |
| Directors | Not applicable (designated partners) | Check section 149 of the Companies Act 2013 | Check section 149 | Check section 149 |
| Minimum capital | No rupee minimum found on an allowed page | The Act refers to a "prescribed" minimum; no rupee figure found | Same as OPC | No rupee figure found |
| Statutory audit | Accounts audited under rules prescribed under section 34(4) of the LLP Act; the thresholds are not stated here | Yes: every company appoints an auditor | Yes | Yes |
| Annual return form | Not covered here | MGT-7A | MGT-7A if a small company, otherwise MGT-7 | MGT-7 |
| Who can found it | Any two persons | Set by rule 3; check it | Any person, subject to the foreign-founder points in Cross-border points | Any person, same |

Sources for this table: sections 2(62) and 2(68), the One Person Company and private company definitions (ICAI study material, chapter 1: https://resource.cdn.icai.org/74729bos60488-m1-cp1.pdf); LLP sections 6, 7 and 34 (ICAI study material, chapter 12: https://resource.cdn.icai.org/74743bos60488-m3-cp12.pdf); annual return forms under rule 11 (ICAI study material, chapter 7: https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf); auditor appointment under section 139 (ICAI study material, chapter 10: https://resource.cdn.icai.org/74738bos60488-m2-cp10.pdf).

A sole proprietorship is not a company or an LLP and is not covered by this skill; its income is taxed as the owner's income (see `india-income-tax`).

**Which form to choose.** A private limited company is the usual vehicle for a business that will raise equity or bring in foreign investors. Rule 3 limits who may form an OPC (check it). An LLP suits a professional or partnership business that wants limited liability without share capital. This is a practical default, not a legal rule; the client's facts decide.

### Private company and One Person Company: the definitions

- Section 2(68) of the Companies Act 2013 defines a private company as one "having a minimum paid-up share capital as may be prescribed", whose articles "(i) restricts the right to transfer its shares; (ii) except in case of One Person Company, limits the number of its members to two hundred" and "(iii) prohibits any invitation to the public to subscribe for any securities of the company". The definition itself prints no rupee amount. This skill found no allowed page that prints a prescribed minimum paid-up capital (ICAI chapter 1: https://resource.cdn.icai.org/74729bos60488-m1-cp1.pdf).
- Section 3(1) sets the minimum number of persons who may form each type of company. No allowed page prints its wording; check it on the MCA portal.
- One Person Company: "One Person Company means a company which has only one person as a member" (section 2(62), ICAI chapter 1: https://resource.cdn.icai.org/74729bos60488-m1-cp1.pdf). Rule 3 of the Companies (Incorporation) Rules 2014 sets who may form an OPC or be its nominee, and what an OPC may not do. No allowed page prints the rule's wording; check it before advising on an OPC.

### LLP: partners and designated partners

- Section 6 of the LLP Act 2008: every LLP shall have at least two partners (ICAI chapter 12: https://resource.cdn.icai.org/74743bos60488-m3-cp12.pdf).
- Section 7(1): "Every LLP shall have at least two designated partners who are individuals and at least one of them shall be a resident in India." Where all partners are bodies corporate, or some partners are bodies corporate, at least two individuals who are partners or nominees of those bodies corporate act as designated partners. For this section, "resident in India" means "a person who has stayed in India for a period of not less than one hundred twenty days during the financial year" (ICAI chapter 12: https://resource.cdn.icai.org/74743bos60488-m3-cp12.pdf).
- The LLP audit thresholds under the LLP Rules are not stated in this skill: no allowed page prints the rule's own wording. Check rule 24 of the LLP Rules 2009 on the MCA portal.

## Rates, bands and thresholds

### Deadlines after incorporation

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Registered office in place (section 12(1)) | within thirty days of incorporation | "A company shall, within thirty days of its incorporation and at all times thereafter, have a registered office" | https://resource.cdn.icai.org/74730bos60488-m1-cp2.pdf |
| Verification of registered office filed (section 12(2)) | within thirty days of incorporation | "furnish to the Registrar verification of its registered office within a period of thirty days of its incorporation" | https://resource.cdn.icai.org/74730bos60488-m1-cp2.pdf |
| Commencement of business declaration, Form No. INC-20A (section 10A), company with share capital | Within 180 days of the date of incorporation | Filed by a director, verified by a practising CS, CA or cost accountant; no business or borrowing before it and the office verification | https://resource.cdn.icai.org/74730bos60488-m1-cp2.pdf |
| First auditor, appointed by the Board (section 139(6)) | Within 30 days of the date of registration | Company other than a Government company; holds office until the first AGM | https://resource.cdn.icai.org/74738bos60488-m2-cp10.pdf |
| Name reservation for a new company (section 4(5)) | Twenty days from the date of approval | RUN or SPICe+ Part A | https://resource.cdn.icai.org/74730bos60488-m1-cp2.pdf |
| LLP designated partner resident in India (LLP Act s 7(1)) | Stayed in India not less than one hundred twenty days during the financial year | At least one of two designated partners who are individuals | https://resource.cdn.icai.org/74743bos60488-m3-cp12.pdf |
| AGM, every company except an OPC (section 96(1)) | Within 6 months of the close of the financial year; first AGM within 9 months of the close of the first financial year; gap not over 15 months | Registrar may extend for a special reason | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf |
| OPC financial statements (section 137(1) proviso) | Within 180 days from the close of the financial year | OPC need not hold an AGM | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf |

### Director KYC fees (G.S.R. 300(E), 21 April 2026)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Form DIR-3 KYC Web filed within the rule 12A(1) timeline | NIL | "The form is filed within the timeline provided in sub-rule (1) of rule 12A" | https://egazette.gov.in/WriteReadData/2026/271973.pdf |
| Filed after that timeline, or filed to re-activate a DIN | INR 5,000 | "(ii) The form is filed after the timeline referred to in serial number (i), or filed for re- 5000 activation of DIN" | https://egazette.gov.in/WriteReadData/2026/271973.pdf |
| Filed again for a change under rule 12A(2), each filing | INR 500 | "Form DIR-3-KYC Web filed again at any time for any change as provided in sub- 500 (for every filing)" | https://egazette.gov.in/WriteReadData/2026/271973.pdf |

### Annual filings and penalties

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Annual return, section 92(4) (MGT-7, or MGT-7A for an OPC or small company) | sixty days | "every company shall file with the Registrar a copy of the annual return, within sixty days from the date on which the annual general meeting is held" | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf |
| Penalty for late annual return, company and every officer in default, section 92(5) | ten thousand rupees | "such company and its every officer who is in default shall be liable to a penalty of ten thousand rupees" | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf |
| Further penalty per day of continuing failure | one hundred rupees | "with further penalty of one hundred rupees for each day during which such failure continues" | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf |
| Maximum, company | two lakh rupees | "subject to a maximum of two lakh rupees in case of a company and fifty thousand rupees in case of an officer who is in default" | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf |
| Maximum, officer in default | fifty thousand rupees | "subject to a maximum of two lakh rupees in case of a company and fifty thousand rupees in case of an officer who is in default" | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Financial statements, section 137(1) (Form AOC-4) | thirty days | "shall be filed with the Registrar within thirty days of the date of annual general meeting in such manner, with such fees or additional fees as may be prescribed" | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf |
| Penalty on the company for not filing, section 137(3) | ten thousand rupees | "The company shall be liable to a penalty of ten thousand rupees and in case of continuing failure, with a further penalty of one hundred rupees for each day" | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf |

### Small company limits (from 1 December 2025)

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Paid-up share capital must not exceed | rupees ten crores | "paid up capital and turnover of the small company shall not exceed rupees ten crores and rupees one hundred crores respectively" | https://egazette.gov.in/WriteReadData/2025/268124.pdf |
| Turnover must not exceed | rupees one hundred crores | "paid up capital and turnover of the small company shall not exceed rupees ten crores and rupees one hundred crores respectively" | https://egazette.gov.in/WriteReadData/2025/268124.pdf |

### Company income tax, tax year 2026-27

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Domestic company, total turnover or gross receipt in tax year 2024-25 not above 400 crore | 25% | "where its total turnover or the 25% of the total gross receipt in the tax year 2024-25 income; does not exceed ₹ 400 crores" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Turnover or gross receipt limit, tested on tax year 2024-25 | INR 400 crore | "where its total turnover or the 25% of the total gross receipt in the tax year 2024-25 income; does not exceed ₹ 400 crores" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Any other domestic company | 30% | "(ii) other than that referred to in 30% of the total item (i) income" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge, domestic company taxed under section 200 or 201, every income level | 10% | "9. 200 or 201. Every domestic 10%. company." | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Health and Education Cess on income-tax plus surcharge | 4% | "calculated at the rate of 4% of such income-tax and surcharge" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Return due date, company where section 172 does not apply (section 263(1)(c), as substituted) | 31 October | "2. (i) Company; Where the 31st October. provisions of (ii) assessee (other than a section 172" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Return due date where section 172 applies (transfer pricing report) | 30 November | "1. Assessee, including the partners Where the 30th November. of the firm" | https://egazette.gov.in/WriteReadData/2026/271439.pdf |

| Item | Value | Note | Source |
| --- | --- | --- | --- |
| Section 200: domestic company that opts in, on total income computed without the listed deductions | 22% | "at the rate of 22%, at the option of a person being a domestic company" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 201: new manufacturing company, on income from manufacturing | 15% | "1. A (a) 15% on the total Such domestic company" | https://egazette.gov.in/WriteReadData/2025/265620.pdf |

## The base

### Capital

- The Companies Act definition of a private company refers to "a minimum paid-up share capital as may be prescribed" and prints no rupee figure (section 2(68), ICAI chapter 1: https://resource.cdn.icai.org/74729bos60488-m1-cp1.pdf). No allowed page prints a prescribed minimum for a private, OPC or public company.
- Authorised capital is a choice made in the memorandum. It drives the incorporation fee and the stamp duty, which are set by the fee rules and the state stamp laws (see Costs below).
- For an LLP, capital is the partners' contribution under the LLP agreement; no minimum was found on an allowed page.
- Foreign investment in equity is governed by the Foreign Exchange Management (Non-debt Instruments) Rules 2019 (amended, among others, by the Third Amendment Rules 2026 of 12 June 2026: https://egazette.gov.in/WriteReadData/2026/273406.pdf). Sector limits, pricing and the reporting forms are not covered here; refer.

### Costs

No allowed page prints the current incorporation fees, name reservation fee or stamp duty, so this skill states none. Check:

- the fee schedule in the Annexure to the Companies (Registration Offices and Fees) Rules 2014, on the MCA portal (incorporation fee by authorised capital, RUN fee, INC-20A fee);
- the stamp duty on the memorandum and articles under the stamp law of the state where the registered office will be, which SPICe+ collects with the filing;
- the Certifying Authority's charge for each digital signature certificate.

The one fee schedule this skill can prove is the director KYC fee, in the rates table.

This fee schedule was substituted by the Companies (Registration Offices and Fees) Amendment Rules 2026 (G.S.R. 300(E)), dated 21 April 2026, in force from its publication in the Gazette.

### Small company status

A small company has lighter duties (shorter annual return, no cash flow statement, outside the Companies (Auditor's Report) Order 2020). The limits changed on 1 December 2025 (rates table).

- Both limits must be met (AND), under rule 2(1)(t) of the Companies (Specification of Definitions Details) Rules 2014 as substituted by G.S.R. 880(E), in force from 1 December 2025; turnover as per profit and loss account for the immediately preceding financial year (section 2(85)(ii)).
- Section 2(85) excludes a public company and, whatever its size, "(A) a holding company or a subsidiary company; (B) a company registered under section 8; or (C) a company or body corporate governed by any special Act" (ICAI chapter 1: https://resource.cdn.icai.org/74729bos60488-m1-cp1.pdf). An Indian subsidiary of a foreign company is therefore never a small company.
- Cash flow statement: under the proviso to section 2(40), "the financial statement, with respect to One Person Company, small company and dormant company, may not include the cash flow statement". For a private company the proviso, as modified by the exemption notification, also covers a private company that is a recognised start-up, provided it has not defaulted in filing its financial statements or annual return (ICAI chapter 1: https://resource.cdn.icai.org/74729bos60488-m1-cp1.pdf).
- The Companies (Auditor's Report) Order 2020 does not apply to "a one person company as defined under clause (62) of section 2 of the Act and a small company as defined under clause (85) of section 2" (ICAI Guidance Note on the Companies (Auditor's Report) Order 2020: https://resource.cdn.icai.org/60117aasb48979-a.pdf).

### Company income tax at a glance (tax year 2026-27)

Section 3(1) of the Finance Act 2026 charges income-tax for tax year 2026-27 under the Income-tax Act 2025 "at the rates specified in Part I-B of the First Schedule". Part I-B and Part III (advance tax), Paragraph E, print the same company rates. The surcharge and cess are in section 3. (Section 2 covers assessment year 2026-27 under the 1961 Act.)

The due dates fall in the financial year after the tax year: for tax year 2026-27, in 2027. The surcharge for a domestic company that does not opt for section 200 or 201 depends on its total income; see the section 3 surcharge table of the Finance Act 2026, serial 6, or `india-financial-statements`, which carries the 7% and 12% surcharge rows. Do not add the rate, surcharge and cess into one "effective" rate in a client answer without showing each part.

The concessional regimes are in the Income-tax Act 2025 (rates table):

- **Section 200.** Any domestic company may opt in. (Its 1961 Act section number changed; the 2025 Act prints no mapping, so none is given here.) The option must be exercised on or before the section 263(1) due date for the return, applies to later tax years, and cannot be withdrawn once exercised. Income is computed without the deductions listed in section 200(1)(a) and without set-off of losses attributable to them.
- **Section 201 is closed to a company formed now.** Among the conditions in column D of its Table, the company must have been set up and registered on or after 1 October 2019 AND must have commenced manufacturing or production of an article or thing on or before 31 March 2024 (the PDF table text is interleaved across columns, so it is not quoted here). A company incorporated in 2026 cannot meet the second condition, so it cannot use section 201.
- Minimum alternate tax, credit carry-forward, and which rate a newly formed company with no tax year 2024-25 turnover falls under are questions for the accountant (see the refer list).

## Deadlines and filing

### Registration process (company)

#### Step 1: Digital signature and director identification

Each subscriber and proposed director signs the forms electronically. In practice, each needs a digital signature certificate from a licensed Certifying Authority. The first directors' particulars, including each one's Director Identification Number (DIN), are filed with the incorporation application; check the list in section 7 on the MCA portal. The cost of a digital signature certificate is not stated here; it is set by the Certifying Authority.

#### Step 2: Reserve the company name

A name can be reserved through the RUN (Reserve Unique Name) web service or in Part A of SPICe+. For a new company the Registrar may "reserve the name for a period of twenty days from the date of approval" (section 4(5)). If the name was reserved by giving wrong or incorrect information, the reservation is cancelled before incorporation, and after incorporation the Registrar may direct a change of name, strike the company off, or petition for winding up (ICAI chapter 2: https://resource.cdn.icai.org/74730bos60488-m1-cp2.pdf). The RUN fee and the extension fees are not stated here; check the fee schedule on the MCA portal.

#### Step 3: File SPICe+ (Form No. INC-32)

The application for registration is filed with the Registrar in whose jurisdiction the registered office will be situated, in SPICe+ (INC-32), with the fee under the Companies (Registration Offices and Fees) Rules 2014. The memorandum (e-MoA, Form No. INC-33) and articles (e-AoA, Form No. INC-34) are signed by all subscribers. The exact list of registrations bundled into SPICe+ at the date of filing (PAN, TAN, EPFO, ESIC, GSTIN, bank account) is on the MCA portal, not on an allowed page; check it there.

#### Step 4: Certificate of incorporation

The Registrar registers the company and issues a certificate of incorporation with the Corporate Identity Number. Processing times are not stated in this skill.

#### Step 5: First steps after incorporation (these carry deadlines)

- **Commencement of business (section 10A).** A company with share capital incorporated after the Companies (Amendment) Ordinance, 2019 may commence business or borrow only after it has filed the section 12(2) verification of its registered office and a director has filed a declaration in Form No. INC-20A within 180 days of incorporation, verified by a practising company secretary, chartered accountant or cost accountant, that every subscriber has paid for the shares agreed to be taken (ICAI chapter 2).
- **Auditor (section 139).** At the first annual general meeting every company shall "appoint an individual or a firm as an auditor who shall hold office from the conclusion of that meeting till the conclusion of its sixth annual general meeting" (ICAI chapter 10: https://resource.cdn.icai.org/74738bos60488-m2-cp10.pdf). The first auditor of a company other than a Government company is appointed by the Board within 30 days of the date of registration and holds office until the first AGM (section 139(6), ICAI chapter 10).
- **Share certificates.** The time limit for issuing certificates to subscribers is in section 56(4) of the Companies Act 2013; no allowed page prints its wording, so it is not stated here.
- **Bank account.** Subscribers pay for their shares into the company's bank account.

### Documents for foreign subscribers

Rule 13 of the Companies (Incorporation) Rules 2014 sets how subscribers sign the memorandum and articles, including how a foreign national's signature, address and proof of identity are notarised and authenticated. No allowed page prints the rule's wording; check it on the MCA portal, and refer where a subscriber lives outside India.

### Director KYC: the rule changed on 31 March 2026

From 31 March 2026, rule 12A of the Companies (Appointment and Qualification of Directors) Rules 2014 (as substituted by G.S.R. 943(E)) says: every individual who holds a DIN as on 31 March of a financial year files the KYC intimation in Form No. DIR-3 KYC Web "on or before the 30th June of the immediately following every third consecutive financial year". Separately, a DIN holder whose personal mobile number, email address or residential address changes must file Form DIR-3 KYC Web "within a period of thirty days of such change" with the fee in the rates table (https://egazette.gov.in/WriteReadData/2025/268970.pdf). The older annual 30 September KYC is gone. The fees for late filing and re-activation are in the rates table.

### Annual filings with the Registrar

Where no annual general meeting is held in a year, the sixty days run from the date on which it should have been held, and the return carries a statement of the reasons. One Person Companies and small companies file Form No. MGT-7A; other companies file Form No. MGT-7.

Section 446B can reduce these penalties for a One Person Company, small company, start-up company or Producer Company. Its current words are "liable to a penalty which shall not be more than one-half of the penalty" (quoted in the Corporate Laws (Amendment) Bill 2026, which would change them: https://egazette.gov.in/WriteReadData/2026/271201.pdf). Check section 446B before quoting a penalty to these companies.

The section 137(3) penalty is also capped; the company and officer caps are in section 137(3) itself. Late filing of either form also attracts the additional fees under section 403 at the rates in the fee rules, which are not stated here.

The thirty and sixty days run from the annual general meeting. A One Person Company, which need not hold an AGM, files its financial statements within 180 days from the close of the financial year (section 137(1) proviso); check the section 92 proviso for its annual return.

### Meetings

- **Annual general meeting.** Every company except an OPC holds its AGM within six months of the close of the financial year (first AGM within nine months of the close of the first financial year), with no more than fifteen months between AGMs (section 96(1), ICAI chapter 7). The annual return and AOC-4 periods run from the meeting date.
- **Board meetings.** Section 173 sets the minimum number of Board meetings and the maximum gap between them, with a lighter rule for an OPC, a small company and a dormant company. No allowed page prints the current wording; check section 173 on the MCA portal.

### Tax registrations and returns

| Obligation | When | Where in the library |
| --- | --- | --- |
| Company income tax return, tax year 2026-27 | Due date in the rates table (falls in 2027) | Rates table |
| GST registration and returns | Once a registration threshold or a compulsory category applies | `india-gst` |
| TDS on payments to contractors and professionals | As payments are made | `in-tds-freelance` |
| Provident fund and ESI for employees | Once the company employs staff | `in-pf-esi-employer` |
| Payroll | Once the company employs staff | `india-payroll` |
| Financial statements, Schedule III, Ind AS and audit | Each financial year | `india-financial-statements` |
| Transfer pricing with foreign group companies | Each tax year | `india-transfer-pricing` |

### Timeline (order of steps)

1. Digital signature certificates for subscribers and directors; DIN particulars for first directors.
2. Name reservation (RUN or SPICe+ Part A); reserved for twenty days from approval for a new company.
3. Memorandum, articles and supporting documents (foreign subscribers: rule 13).
4. SPICe+ filing with fees and stamp duty.
5. Certificate of incorporation.
6. Bank account; subscribers pay for their shares.
7. Within thirty days: registered office in place and verified. First auditor appointed by the Board within thirty days.
8. INC-20A declaration under section 10A within 180 days of incorporation.
9. GST, payroll and other registrations as they apply .

The time each step takes depends on the Registrar's queue, the bank and the Certifying Authority; this skill gives no day counts.

## Penalties and interest

The annual return and financial statement penalties are in the rates table. Common mistakes and refusals:

- **R-IN-F1: No qualifying resident director or designated partner.** For an LLP, at least one designated partner must meet the one hundred twenty days test for the financial year. For a company, check the section 149(3) residence condition before filing.
- **R-IN-F2: Treating section 10A as optional.** No business or borrowing until the office is verified and INC-20A is filed within 180 days of incorporation.
- **R-IN-F3: Missing annual filings.** The annual return and AOC-4 carry the section 92(5) and 137(3) penalties in the rates table, on the company and on the officers each section names, on top of the section 403 additional fees. Other consequences of continued non-filing, such as director disqualification under section 164(2), are in the Act; check them on the MCA portal.
- **R-IN-F4: Working from the old director KYC rule.** The annual 30 September DIR-3 KYC was replaced on 31 March 2026 by the every-third-year 30 June filing, plus a filing within thirty days of any change in mobile number, email or address (Deadlines and filing).
- **R-IN-F5: Promising the section 201 rate to a new manufacturer.** The section 201 rate needs manufacturing to have started on or before 31 March 2024 (rates table).
- **R-IN-F6: Claiming small company relief for a subsidiary.** A holding or subsidiary company is never a small company, whatever its capital and turnover.
- **R-IN-F7: Shell companies.** This skill will not help form a company with no genuine business activity or a company meant to hide its beneficial owners. Refer such requests.
- **Pending law, not in force.** The Corporate Laws (Amendment) Bill 2026 (Bill No. 85 of 2026, introduced in Lok Sabha on 23 March 2026) would, among other things, raise the small company ceilings and change the section 403 additional fee. It is a Bill. Apply the current rules in this skill until it is enacted and notified (https://egazette.gov.in/WriteReadData/2026/271201.pdf).

## Cross-border points

| Question | Answer |
| --- | --- |
| Can a foreign national form an OPC? | Rule 3 of the Companies (Incorporation) Rules 2014 governs this. Check it on the MCA portal; refer if the founder's eligibility is unclear. |
| Resident director for a company? | Section 149(3) of the Companies Act 2013 sets a residence condition for at least one director. No allowed page prints its current wording; check it on the MCA portal before choosing the board. Do not rely on a previous-calendar-year test from older material. |
| Resident partner for an LLP? | At least one designated partner must be resident in India: stayed in India not less than one hundred twenty days during the financial year (section 7(1) LLP Act, ICAI chapter 12). |
| DIN for a foreign director | Each first director needs a DIN; the particulars filed with the incorporation application are listed in section 7 of the Companies Act 2013. Check them on the MCA portal. |
| Small company relief for a foreign-owned subsidiary? | No. A subsidiary company is excluded from the small company definition (section 2(85)). |
| Foreign direct investment | Governed by the Foreign Exchange Management (Non-debt Instruments) Rules 2019. Sector caps, government approval routes and reporting forms and deadlines are not covered here; refer (see the refer list). |
| Payments to and from the foreign parent | Transfer pricing rules apply; see `india-transfer-pricing`. |

## Two worked examples that recompute

### Example 1: Private company incorporated on 10 January 2027, with three directors

Day 10 of 2027 is the incorporation date. The registered office must be in place and verified, and the Board must appoint the first auditor, within thirty days: by day 40, 9 February 2027. The INC-20A declaration is due within 180 days: by day 190, 9 July 2027 (2027 is not a leap year); no business or borrowing before it. The financial year may run to 31 March 2028 because the company was incorporated on or after 1 January. Director KYC: one director held a DIN on 31 March and missed the rule 12A(1) filing, so pays 5,000 rupees; another changed his mobile number and files again within thirty days for 500 rupees; the third files on time for nil.

```oa-check
name: Post-incorporation deadlines from day 10 of 2027 and DIR-3 KYC fees for three directors
inputs:
  incorporation_day: 10
  late_kyc: 5000
  change_kyc: 500
  on_time_kyc: 0
steps:
  - office_and_auditor_day: incorporation_day + 30
  - inc20a_day: incorporation_day + 180
  - kyc_fees: late_kyc + change_kyc + on_time_kyc
expected:
  office_and_auditor_day: 40
  inc20a_day: 190
  kyc_fees: 5500
```

### Example 2: Late annual return, company and one officer

A company holds its AGM on 30 September 2027 and files MGT-7 on 29 January 2028, 61 days after the sixty-day period ended on 29 November 2027. Section 92(5): 10,000 rupees plus 100 rupees a day while the failure continues, capped at 2,00,000 rupees for the company and 50,000 rupees for an officer in default. The company owes 10,000 + 61 x 100 = 16,100; the officer the same 16,100 (under the 50,000 cap). If it is a small company or OPC, section 446B may halve these: check it before quoting.

```oa-check
name: Section 92(5) penalty, 61 days late, company and officer
inputs:
  days_late: 61
steps:
  - company_penalty: min(10000 + days_late * 100, 200000)
  - officer_penalty: min(10000 + days_late * 100, 50000)
expected:
  company_penalty: 16100
  officer_penalty: 16100
```

## Ask the client first

- Who are the founders, what are their citizenships, and how many days has each spent in India in the current and the preceding financial year? (OPC eligibility, LLP designated partner, company resident director.)
- Will a foreign company or a foreign individual hold shares, and in which sector will the business operate? (FDI route, small company exclusion for subsidiaries, transfer pricing.)
- Does the business need equity investors, or is it a professional practice? (Company or LLP.)
- Will the company manufacture, and when will production start? (Section 200 and the closed section 201 regime.)
- In which state will the registered office be, and is it ready? (Registrar jurisdiction, stamp duty, the thirty-day office rule.)
- Does the business need a licence or approval from a sector regulator such as the Reserve Bank of India or SEBI? (A precondition for some businesses; refer.)

### The method, step by step

1. **Choose the form** (Who this applies to): check the founders against rule 3 for an OPC (check on the MCA portal) and section 7(1) for an LLP (ICAI chapter 12: https://resource.cdn.icai.org/74743bos60488-m3-cp12.pdf).
2. **Fix the board or designated partners**: confirm the section 149 director rules on the MCA portal, and that each first director has a DIN and a digital signature (check section 7 on the MCA portal).
3. **Reserve the name** through RUN or SPICe+ Part A; the reservation lasts twenty days from approval (section 4(5), ICAI chapter 2: https://resource.cdn.icai.org/74730bos60488-m1-cp2.pdf).
4. **Prepare and file SPICe+ (INC-32)** with e-MoA (INC-33) and e-AoA (INC-34), the fee under the Companies (Registration Offices and Fees) Rules 2014 and state stamp duty; for foreign subscribers, follow rule 13 (check on the MCA portal).
5. **After incorporation**, diarise: registered office and its verification within thirty days (section 12); section 10A and Form INC-20A (within 180 days).
6. **Test small company status** against the limits in force from 1 December 2025 and the section 2(85) exclusions (https://egazette.gov.in/WriteReadData/2025/268124.pdf and ICAI chapter 1: https://resource.cdn.icai.org/74729bos60488-m1-cp1.pdf).
7. **Set the annual calendar**: annual general meeting under section 96 (six months from the year end), annual return within sixty days and AOC-4 within thirty days of the meeting (ICAI chapter 7: https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf and ICAI chapter 9: https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf), director KYC under rule 12A (https://egazette.gov.in/WriteReadData/2025/268970.pdf).
8. **Decide the income tax regime** for tax year 2026-27: section 200 option or ordinary rates, and the return due date (Finance Act 2026: https://egazette.gov.in/WriteReadData/2026/271439.pdf and Income-tax Act 2025: https://egazette.gov.in/WriteReadData/2025/265620.pdf).
9. **Hand off** GST, payroll, TDS, financial statements and transfer pricing to the skills named under Tax registrations and returns.

### When to refuse or refer

- Foreign direct investment in a sector with a cap or a government approval route, or any investor from a country that shares a land border with India: refer to a practitioner who handles FEMA filings.
- Any company that will carry on non-banking financial, insurance, banking or securities business: refer; sector approval is a precondition.
- Section 8 (not-for-profit) companies, producer companies, IFSC companies and public companies that will list: out of scope; refer.
- Conversion of a firm, a private company or an unlisted public company into an LLP, or an OPC into another form: refer.
- Choosing between the section 200 option and ordinary rates where minimum alternate tax credit or losses exist, or where the tax year 2024-25 turnover test is unclear: refer to the company's accountant.
- A request to form a company with no genuine business, to hold assets for an undisclosed owner, or to avoid the resident director rule with a nominee who will not act: refuse.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Income-tax Act 2025 sections 1(3), 200, 201 and 536(1) (Gazette, Act 30 of 2025) | https://egazette.gov.in/WriteReadData/2025/265620.pdf | 2026-11-14 |
| Read for Finance Act 2026 section 3, First Schedule Part I-B Paragraph E, and the substituted section 263(1)(c) due dates | https://egazette.gov.in/WriteReadData/2026/271439.pdf | 2026-11-14 |
| Read for G.S.R. 880(E), small company limits from 1 December 2025 | https://egazette.gov.in/WriteReadData/2025/268124.pdf | 2026-11-14 |
| Read for G.S.R. 943(E), rule 12A director KYC from 31 March 2026 | https://egazette.gov.in/WriteReadData/2025/268970.pdf | 2026-11-14 |
| Read for G.S.R. 300(E) of 21 April 2026, DIR-3 KYC fees of nil, 5,000 and 500 | https://egazette.gov.in/WriteReadData/2026/271973.pdf | 2026-11-14 |
| Read for the Foreign Exchange Management (Non-debt Instruments) (Third Amendment) Rules 2026 of 12 June 2026 | https://egazette.gov.in/WriteReadData/2026/273406.pdf | 2026-11-14 |
| Read for the Corporate Laws (Amendment) Bill 2026 (pending): section 2(85), 403 and 446B wording | https://egazette.gov.in/WriteReadData/2026/271201.pdf | 2026-11-14 |
| Read for ICAI study material chapter 1: sections 2(40), 2(62), 2(68), 2(85) | https://resource.cdn.icai.org/74729bos60488-m1-cp1.pdf | 2026-11-14 |
| Read for ICAI study material chapter 2: sections 4(5), 10A (INC-20A within 180 days) and 12 | https://resource.cdn.icai.org/74730bos60488-m1-cp2.pdf | 2026-11-14 |
| Read for ICAI study material chapter 7: sections 92(4), 92(5) and 96(1) | https://resource.cdn.icai.org/74735bos60488-m2-cp7.pdf | 2026-11-14 |
| Read for ICAI study material chapter 9: section 137(1) including the OPC proviso, and 137(3) | https://resource.cdn.icai.org/74737bos60488-m2-cp9.pdf | 2026-11-14 |
| Read for ICAI study material chapter 10: section 139(1) and 139(6) | https://resource.cdn.icai.org/74738bos60488-m2-cp10.pdf | 2026-11-14 |
| Read for ICAI study material chapter 12: LLP Act sections 6, 7 and 34 | https://resource.cdn.icai.org/74743bos60488-m3-cp12.pdf | 2026-11-14 |
| Read for the ICAI Guidance Note on CARO 2020, paragraph 1(2) exclusions | https://resource.cdn.icai.org/60117aasb48979-a.pdf | 2026-11-14 |

Not yet confirmed: incorporation, RUN and INC-20A fees and state stamp duty; the prescribed minimum paid-up capital (if any); section 3(1) minimum members; rule 3 OPC eligibility; rule 13 foreign subscriber documents; section 149 director numbers and the section 149(3) resident director test; section 56(4) share certificate period; section 173 board meeting rules; the section 137(3) caps; the LLP audit thresholds (rule 24); which rate a new company with no 2024-25 turnover falls under; the list of registrations bundled into SPICe+.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `india-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/india-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
