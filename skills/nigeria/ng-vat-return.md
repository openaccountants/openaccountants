---
name: ng-vat-return
description: >
  Use this Nigeria VAT return reference whenever asked about Nigerian VAT
  returns for self-employed individuals or small businesses. Trigger on phrases
  like Nigeria VAT return, VAT Form 002, VAT 002, NRS VAT, 7.5% VAT, Rev360,
  input VAT, small business VAT, VAT withheld, nil return, or Nigerian VAT
  registration, classification, input deductions, imported services, monthly
  returns or payment deadlines. Covers VAT months from January 2026 under the
  Nigeria Tax Act and Nigeria Tax Administration Act 2025, with
  bank-narration patterns and the VAT 002 lines. Supplies under the repealed
  VAT Act are refused. Two printed texts of the Nigeria Tax Act differ, and this
  file names its working text. This Tier 2 draft supports source checking and
  reviewer questions; it does not authorise filing, payment or a tax position.
version: 2.3
jurisdiction: NG
tax_year: 2026
tax_year_notes: "VAT months from January 2026, read at 5 November 2026. VAT has no year of assessment: the Nigeria Tax Act 2025 commenced on 1 January 2026 and returns are monthly. 7.5% enacted. The NGN 100 million small business turnover test is in the Nigeria Tax Administration Act and the working text of the Nigeria Tax Act; a scanned copy on the NRS website with the same Gazette reference prints NGN 50 million for a small company. Supplies under the repealed VAT Act are outside this file."
last_updated: 2026-11-05
depends_on:
  - vat-workflow-base
  - ng-vat
job: vat-return
category: international
tier: 1
reviewed_by: "Omolola Fasasi"
reviewed_on: 2026-11-03
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: vat-gst
---

# NG VAT Return v2.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Self-employed individuals and small businesses that are taxable persons under the Nigeria Tax Act 2025 (NTA) and the Nigeria Tax Administration Act 2025 (NTAA), and the reviewers working with them. The tax is administered by the Nigeria Revenue Service (NRS). The return is Form VAT 002, uploaded on the NRS Rev360 portal (https://selfservice.nrs.gov.ng/). Amounts are in naira (NGN) unless the transaction is in another currency: tax is assessed in the currency of the transaction (NTAA s 39).

Figures apply to VAT months from January 2026, read at 5 November 2026. VAT has no year of assessment. The NTA commenced on 1 January 2026 and returns are monthly.

### What this file is

This is the return workflow file for Nigeria (`job: vat-return`), a country slot file for `vat-workflow-base`. The base owns the workflow, output specification, question form and self-checks. Its status is Tier 2, pending review. It was contributed by the Open Accountants Community. No statement here has been approved by an accountant.

The sibling guide `ng-vat` holds the wider reference. The split is provisional: one job in one country has one skill, so the owner may retire one file with an alias. The older `nigeria-vat` file is archived.

**Operational hold.** `vat-workflow-base` Step 1 requires a regional or directive layer as well as this file. None for Nigeria was found in this repository at 5 November 2026, so Step 1 stops the workflow. Use this file as a reference only. Stop before producing a workbook, return or filing instruction until a regional layer or an approved non-EU exception exists.

Every classification is a working paper for reviewer checking. Treat all input VAT as provisional until the document behind it is checked.

### How to read the amounts

The words below carry a fixed meaning in this file.

- **Enacted:** printed in the working text of the Act named.
- **Guideline:** stated in the General Transition Guidelines of the Minister of Finance, which say they are made under NTAA s 144 and NTA s 200.
- **Administered:** what NRS says in the circular, notice, page or template named. NRS practice is not enacted law.
- **Held:** not settled on the sources read. Do not state a result as settled.

**Working text of the NTA.** 2 texts carry the same Gazette reference (No. 117, Vol. 112, 26 June 2025, Act No. 7), and they differ:

| Point | Working text | Scanned copy |
| --- | --- | --- |
| Where read | The PDF on the National Assembly site, byte-identical to the PDF that press reports say the House of Representatives released as a certified true copy in January 2026 | A 215-page scanned PDF on the NRS website, imprint FGP 29/72025/500 |
| VAT sections | ss 143 to 157, 185 to 188, definitions in s 201 | ss 144 to 158, 186 to 189, definitions in s 202 |
| Small company | Gross turnover NGN 100,000,000 or less a year, fixed assets not above NGN 250,000,000 | Gross turnover NGN 50,000,000 or less a year, same asset limit, professional services excluded |
| Zero rate | s 186(a) to (q) | Adds (r) electric vehicles and (s) parts and semi-knock-down units for assembling them |
| Zero-rated supplier | Credit and refund under s 155(1) and (2) | Adds s 156(4): pays VAT on inputs and may request a refund |
| Input rule | s 155(4) and (5) | s 156(5) and (6) |
| Humanitarian exemption | s 185(1)(c) ends 'provided that the humanitarian donor shall first pay the VAT and request a refund from the Service' | s 186(1)(c) has no such words |
| Money exemption | s 185(1)(m) 'money, stakes or securities including interest in money or securities'; s 188 defines 'Stake' as an amount waged on a game | s 186(1)(m) 'money or securities including interest in money or securities'; no 'Stake' definition found |
| Seed definition | None in s 188 | s 189 defines agricultural seeds and seedlings |
| VAT invoice | 7 limbs, (a) to (g) | 8 limbs, (a) to (h), with the invoice number on its own |
| Cross-references | s 147 'Part IX of this Chapter'; s 153 names s 146; s 156 names s 191 | s 148 'Part IV of Chapter Eight of this Act'; s 154 names s 148; s 157 names s 190 |

This file follows the working text, and neither text is proved to be the law. 3 official documents lean to the working text. The NRS circular and guidelines of 29 June 2026 use its section numbers. Paragraph 20 of the Transition Guidelines gives the new small company test as NGN 100 million and NGN 250 million. The zero-rated list in the NRS VAT 002 template has no electric vehicles, though that is weak evidence: the same list leaves out s 186(h), and the template's exempt list leaves out s 185(1)(d) and (o).

Other evidence points to the scanned copy. NRS hosts it on its own site. The template's exempt list words the humanitarian and money limbs as the scan does, though it shortens other limbs. The Withholding Guidelines cite the input rule as s 155(5): the section number fits the working text and the subsection fits the scan. The cross-references in the scan's ss 148, 154 and 157 fit its own numbering, whilst those in the working text's ss 147, 153 and 156 do not.

No re-gazetted text and no court ruling on the point was read. Section numbers here follow the working text; in the scanned copy most VAT sections are one higher. Where a result turns on a difference, it is Needs Input. The table above is not a complete comparison: the scan extracts too poorly for a line-by-line check of its VAT sections and definitions. The exemption, invoice and cross-reference rows were read on the page image; the other scan rows rest on the extracted text.

The NTAA was read in the Tax Appeal Tribunal copy and compared clause by clause with the copy reported as released by the House. No difference was found in the clauses used here, and the 88 hunks left by the comparison were not all read by eye; see Sources.

### Refusals and boundaries

These are the country refusals for `vat-workflow-base`. If a trigger fires, stop, output the message verbatim and end, as Step 5 of the base requires. There is no partial classification.

- **R-NG-1, small business.** Trigger: for a VAT month from January 2026, the facts confirm all of these: gross turnover of NGN 100,000,000 or less a year, counting the NTAA s 22(7) exclusions only for a company; total fixed assets of not more than NGN 250,000,000; the business does not provide professional services; and no written opt-out notice under s 22(5) has been given. A business providing professional services is never within this refusal, whatever its turnover. If any limb is unknown, or a person that is not a company meets the turnover limb only through those exclusions, this is Needs Input, not a stop. Message: 'On the facts given this is a small business under the Nigeria Tax Administration Act, so section 22(1) does not require this VAT return. This workflow stops here. Have the position reviewed, because a business that ceases to be a small business must file monthly.'
- **R-NG-2, international VAT recovery and transfer pricing.** Trigger: the client wants to recover VAT charged by another country, or the period raises a transfer pricing question. Message: 'International VAT recovery and transfer pricing are outside this workflow. This workflow cannot complete the return. Refer it to an ICAN or ANAN member or a CITN-registered tax practitioner.'
- **R-NG-3, corporate tax.** Trigger: the request is for Companies Income Tax or another income tax computation. Message: 'Companies Income Tax is a separate obligation outside this workflow. This workflow cannot complete that request.'
- **R-NG-4, repealed law.** Trigger: the VAT month is before January 2026, or the month includes an amount the Transition Guidelines leave under the repealed law: goods delivered or services rendered up to 31 December 2025 whenever paid; payment made in advance before commencement for a later supply; or the part of a spanning contract executed or received before commencement (paragraphs 10.2.1 and 10.2.2). Message: 'This return includes a period or amount under the repealed Value Added Tax Act. This file does not verify that law. This workflow cannot complete the return. Refer it to an ICAN or ANAN member or a CITN-registered tax practitioner.'
- **R-NG-5, restructuring and business transfers.** Trigger: the month includes a business restructuring under NTA s 189(6), or a transfer of a business or part of one as a going concern under s 189(7). Message: 'This restructuring or business transfer needs specialist review. This workflow cannot complete the return. Refer it to an ICAN or ANAN member or a CITN-registered tax practitioner.'
- **R-NG-6, petroleum operations.** Trigger: the client is a company engaged in petroleum operations as the NTA defines them, or the month includes oil and gas exports or crude petroleum oil or feed gas (NTA s 185(1)(a) and (b)). Message: 'Petroleum operations and oil and gas supplies need specialist review. This workflow cannot complete the return. Refer it to an ICAN or ANAN member or a CITN-registered tax practitioner.'
- **R-NG-7, withholding agent's return.** Trigger: the client is a government body or an appointed agent and asks for its own return of VAT withheld from suppliers. Message: 'The return of VAT withheld is a separate return outside this workflow. This workflow cannot complete that return. Refer it to an ICAN or ANAN member or a CITN-registered tax practitioner.'

R-NG-4 replaces the part of the legacy R-NG-1 that stopped a business at NGN 25,000,000 for periods before 2026.

### Working limits

Kept from the prior version with their corrections.

- Never charge VAT on an exempt supply. The legacy examples were wrong in part: basic food, medical items and services, educational books and tuition are zero-rated from 2026, not exempt.
- Never claim input VAT without the document the claim rests on: see Input VAT documents. The Act names no document for this; the NRS VAT page asks for valid VAT invoices.
- Never treat a business below NGN 25,000,000 as outside VAT for a month from January 2026. That amount is not the test: use R-NG-1. A business providing professional services is never a small business.
- Never apply a rate other than 7.5% or 0%. The prior wording named 7.5% only and left out the zero rate. The 5% in the 2012 text of the old Act is not a rate for any month here.
- Never miss the 21st. Nil returns are still required, except from a small business (NTAA s 22(4)).
- Never claim input VAT on purchases used for exempt supplies.
- Never ignore VAT due on a supply from a non-resident: see Cross-border points.
- Never present calculations as definitive. Label them as estimated and direct the client to an ICAN or ANAN member or a CITN-registered tax practitioner.

### Required inputs

| Level | Items | Policy |
| --- | --- | --- |
| Minimum viable | Bank statement for the month in CSV, PDF or pasted text, confirmation of registration, and the Tax ID | HARD STOP without the statement, the registration fact or the Tax ID |
| Recommended | Sales invoices, purchase invoices showing VAT, prior period returns | SOFT WARN |
| Ideal | Complete invoice register, the Tax ID evidence, evidence of VAT withheld on government or agent supplies, import documents, asset register | SOFT WARN |

Say: 'Input VAT needs the document behind it. All input VAT is provisional until that document is checked.'

Every taxable person registers and obtains a Tax ID (NTAA s 4). The Acts read use the Tax ID, not a separate VAT number; the legacy 'TIN' is that number's older name.

## Rates, bands and thresholds

Each row leads with the official source. Enacted rows are read in the working text.

| Item | Amount or rule | Position at 5 November 2026 | Source and limit |
| --- | --- | --- | --- |
| Standard rate | 7.5% (NTA s 147) | Enacted. Section 147 opens 'Subject to the provisions of Part IX of this Chapter', and Chapter Six has no Part IX; the scanned copy's s 148 opens with Part IV of Chapter Eight. | [NTA 2025](https://nass.gov.ng/documents/download/11249) |
| Zero rate | 0% on the s 186 list | Enacted | same |
| Exempt | The s 185(1) list. No VAT, no input. An order under s 187 or NTAA s 144(3)(c) can add to it. | Enacted. Limbs (c) and (m) differ between the 2 texts. No such order was read. | same |
| Suspended items | Petroleum products, renewable energy equipment, CNG, LPG and other gaseous hydrocarbons: charged from the date the Minister indicates by Gazette order, or suspended by such an order (s 185(2), Eleventh Schedule para 1) | Enacted. No order was read: Needs Input. | same |
| Tax fraction | 7.5/107.5, from s 148(1)(a): the value is the amount which with the VAT equals the consideration | Enacted | same |
| Small business turnover | Gross turnover NGN 100,000,000 or less a year (NTAA definition) | Enacted | [NTAA 2025](https://tat.gov.ng/Nigeria-Tax-Act-2025.pdf) |
| Small business assets | Total fixed assets not more than NGN 250,000,000 (NTAA definition) | Enacted | same |
| Professional services | A business providing them is not a small business (NTAA definition). The term is not defined in either Act on a text search. | Enacted, meaning held | same |
| Small company in the scanned copy | unverified: NGN 50,000,000 | Held. Not used here. Paragraph 20 of the Transition Guidelines and the NTAA point to NGN 100,000,000. | [Scanned NTA on the NRS site](https://www.nrs.gov.ng/uploads/NIGERIA_TAX_ACT_2025_ef6bb812a5.pdf); see Working text |
| Monthly return | By the 21st of the following month (NTAA s 22(1)) | Enacted | [NTAA 2025](https://tat.gov.ng/Nigeria-Tax-Act-2025.pdf) |
| Remittance of VAT withheld or self-accounted | By the 14th of the following month, or as NRS prescribes (NTA s 154(4)) | Enacted; conflict with NTAA s 107 under Deadlines and filing | [NTA 2025](https://nass.gov.ng/documents/download/11249) |
| Input VAT claim period | Within 5 years after the end of the tax period in which it was incurred (NTA s 155(4), proviso (b)) | Enacted | same |
| VAT refund request | Within 12 months after the transaction, or it lapses (NTAA s 56). Decision within 30 days of a valid request. | Enacted | [NTAA 2025](https://tat.gov.ng/Nigeria-Tax-Act-2025.pdf) |
| Records | Not less than 6 years after the year of assessment (NTAA s 31(5)). The legacy '5 years minimum' is corrected. | Enacted | same |
| Electronic invoice direction | At least 30 days' notice (NTA s 152(4)) | Enacted | [NTA 2025](https://nass.gov.ng/documents/download/11249) |

**The small business test, exactly.** The test looks at one 'business' and 2 amounts. Neither Act read says whether a person's separate businesses, or connected persons' businesses, are added together, so an answer that turns on that is Needs Input. 'Per annum' is not tied to a calendar year, an accounting year or a rolling 12 months, and 'total fixed assets' is not tied to cost or written-down value: the same applies. The NTAA does not define gross turnover. NTA s 201 does, and it counts the gross inflow from operating activities, including sales of goods, supply of services, interest, rents, royalties and dividends, and leaves out contributions from equity participants. In determining whether 'a person' meets 'the threshold of being a small company', NTAA s 22(7) then excludes the supply of a capital asset, and a supply made solely because the person sells all or part of the business or permanently ceases business. Section 22(4) and the definition say 'small business'; the NRS VAT page says 'small companies'. This file applies the NTAA definition to the test, because s 22(4) uses it, and applies the s 22(7) exclusions to a company. Whether they reach a person that is not a company is held: the NTAA defines 'Person' to include individuals, but the threshold s 22(7) names is a company's. If the result for such a person turns on them, it is Needs Input.

**What the exemption covers.** NTAA s 22(4) lifts the return. Section 22(5) describes the exemption as including registration, charging of tax on taxable supplies and filing of returns, and lets a small business opt out by written notice. Section 22(8), as printed, exempts a person 'granted exemption in subsection (5)' from NTAA ss 100 and 102 and NTA s 151. Section 22(9) disapplies s 22(5) for companies in petroleum operations; R-NG-6 applies. Section 22(6) requires monthly returns once a business ceases to be small. Section 22(4) lifts s 22(1) only; a small business that has opted out files. How the s 22(8) reference to NTA s 151 affects VAT a small business pays on purchases, and whether it can recover any input VAT without opting out, is held.

**Exempt, NTA s 185(1).** All limbs: (a) oil and gas exports; (b) crude petroleum oil and feed gas for all processed gas; (c) goods purchased for use in humanitarian donor funded projects, provided that the humanitarian donor shall first pay the VAT and request a refund from the Service; (d) baby products; (e) locally manufactured sanitary towels, pads or tampons; (f) military hardware, arms, ammunitions and locally manufactured uniforms supplied to armed forces, para-military and other security agencies of a Nigerian government; (g) shared passenger road-transport service; (h) purchase, hire, rental or lease of tractors, ploughs and other equipment used for agricultural purposes; (i) supplies consumed by an approved entity in an export processing or free trade zone on its approved activity; (j) goods or services supplied to a diplomatic mission, diplomat or person recognised under the Diplomatic Immunities and Privileges Act whose activity is in the public interest and not for profit; (k) plays and performances conducted by educational institutions as part of learning; (l) land or building including interest in land or building; (m) money, stakes or securities including interest in money or securities; (n) Government licences; and (o) assistive devices and disability-related products including hearing aids, wheelchairs and braille materials.

Limbs (c) and (m) are as the working text prints them. The scanned copy has no donor proviso in (c) and no 'stakes' in (m), so a result that turns on whether the donor must pay first, or on whether a stake is exempt, is Needs Input.

Section 187 lets the President, by an order published in the Official Gazette, give effect to an exemption in an agreement with another government or a donor agency for development financing of a project in Nigeria. NTAA s 144(3)(c) lets the Minister amend, vary or modify the Part IV list by regulation. No order under either was read.

The legacy table put diplomatic and humanitarian items at 0%. Both are exempt from 2026.

**Zero rate, NTA s 186.** All limbs: (a) basic food items; (b) all medical and pharmaceutical products including medicinal herbal products; (c) educational books and materials; (d) fertilisers; (e) locally produced agricultural chemicals; (f) locally produced veterinary medicine; (g) locally produced animal feeds; (h) live cattle, goats, sheep and poultry; (i) agricultural seeds and seedlings; (j) electricity generated by generation companies and supplied to the National Grid or Nigeria Bulk Electricity Trading Company; (k) electricity transmitted by Transmission Company of Nigeria to electricity distribution companies; (l) medical services; (m) tuition relating to nursery, primary, secondary or tertiary education; (n) exported goods excluding oil and gas; (o) exported services; (p) exported incorporeal property; and (q) medical equipment.

Section 186 opens 'Subject to paragraph 2 of the Tenth Schedule'. The items that paragraph appears to mean, CNG and LPG conversion equipment and services, sit in paragraph 2 of the Eleventh Schedule, which lets the Minister classify them as exempt or zero-rated by order. No order was read.

Read the s 188 definitions before relying on a limb. They are not repeated here. They include Basic Food Items, Medical Services (by a qualified health practitioner, excluding cosmetology, spa, gymnasium or similar services), Shared Passenger Road-Transport Service (excluding leased, hired or rented vehicles, transport apparatus for business or private use, and car or ride hailing services), Exported Goods, Educational Books and Materials, Baby Products, Medical Equipment and Medical and Pharmaceutical Products.

Zero-rated supplies are taxable supplies charged at zero percent (s 186), so input VAT on them can be deducted under s 155(4). Input VAT on exempt items cannot be claimed and is expensed (Refund Guidelines para 11.4).

**Earlier periods.** The legacy figures for periods before 2026 are not used here (R-NG-4). The Finance Act 2020, Act No. 1 of 2021, s 42 sets 7.5% 'with effect from' February 2020; no day appears in the extracted text, and the legacy '1 February' is held. The Finance Act 2019, the source the legacy file's NGN 25,000,000 traces to, was not read. Paragraph 20 of the Transition Guidelines describes a small company under the repealed laws as having annual turnover not exceeding NGN 25 million.

## The base

VAT is payable on all taxable supplies in Nigeria, subject to the exemptions in Part IV of Chapter Eight (NTA s 144), which holds ss 185 to 188. A taxable supply is any transaction for the sale of goods or the performance of a service for a consideration (s 201).

**Place of supply, s 145.** A supply is in Nigeria where:

- for goods: (i) they are physically present, imported into, assembled or installed in Nigeria at the time of supply, or (ii) the beneficial owner of the rights in or over them is a taxable person in Nigeria and the goods or right are situated, registered or exercisable in Nigeria;
- for a service: (i) it is provided to and consumed by a person in Nigeria, wherever rendered and wherever the obligation to render it rests, or (ii) it is connected with existing immovable property located in Nigeria, including the services of agents, experts, engineers, architects and valuers;
- for an incorporeal: (i) the right is exploited by a person in Nigeria or whose usual residence is in Nigeria, (ii) it is registered in Nigeria or assigned to or acquired by a person in Nigeria, wherever payment is made, or (iii) it is connected with a tangible or immovable asset in Nigeria.

The NRS circular says a service 'rendered to or consumed by' a person in Nigeria. The Act says 'provided to and consumed by'. Apply the Act and flag the difference.

**Time of supply, s 146.** The earliest of: an invoice or receipt being issued; goods being delivered or made available; or payment being due or received. For connected persons without invoices, the time is removal, availability, commencement of the service, or availability of the incorporeal. For rental and periodic supplies, each supply occurs when payment is due or received, whichever is earlier. For progressive or construction supplies, each occurs when payment is due or received or an invoice for that payment is issued, whichever is first. For instalment credit, it is delivery or any payment received, whichever is first.

There is no deposit carve-out in s 146. A part payment or mobilisation payment fixes the time of supply for that amount: the NRS circular's Illustration 2 treats a mobilisation payment that way. No provision on a supply subject to a suspensive condition was read: held.

**Value, ss 148 and 149.** For a money consideration, the value is the amount which with the VAT equals the consideration. For a non-money consideration, it is market value. Where a consideration relates partly to a taxable supply, only the attributable part counts. Connected persons, or a supply not for money, use the arm's length amount. Imported value is the price plus taxes, duties and charges other than VAT, plus commission, 'parking' (as printed), transport and insurance up to the port or point of entry.

**Input VAT, s 155(4) and (5).** A registered person may deduct input tax on any taxable supply, including services and fixed assets, at the end of the tax period of the supply, only to the extent it was incurred for consumption, use or supply in the course of making taxable supplies. Provisos: (a) where input tax relates to both taxable and non-taxable supplies, only the taxable proportion is deductible; (b) the claim must be made within 5 years after the end of the tax period in which it was incurred. Section 155(5) limits the deduction to taxable supplies made from commencement. The old Act's limit on services and fixed assets no longer applies. The NRS page calls this 'fully recoverable'; the Act's conditions still apply.

Sections 151 to 155 contain no block on entertainment or motor cars as read. The test is the purpose test above, and private use fails it.

**Apportionment.** Section 155(4)(a) gives no method. NTA s 193(2) requires any method to be just and equitable and consistently applied under similar circumstances. Attribute directly first. The legacy revenue ratio is one possible method, not a statutory one, and the NRS circular's Illustration 4 apportions by use of a building. Input VAT on exempt items is expensed (Refund Guidelines para 11.4). A share the client states is not itself a method, so it goes to the reviewer.

**Withheld VAT.** Federal, State and Local Government bodies and their ministries, departments and agencies, and any person NRS appoints, collect or withhold VAT on taxable supplies made to them (NTA s 154(1)). The appointed agent withholds the VAT stated on the invoice and does not pay it to the supplier (Withholding Guidelines para 4). The supplier then reports as follows (para 8): disclose total output VAT; deduct the output VAT withheld to reach net output VAT; deduct input VAT on all supplies; and offset any excess against later VAT or request a refund. The legacy term 'WHT-VAT' means this. Income tax withholding is a different tax.

NRS may also direct a taxable person, to whom taxable supplies are made in Nigeria on an invoice that does not include VAT, to self-account for the VAT payable and remit it (s 154(2)). All 3 conditions must be met: a direction, a taxable supply made in Nigeria and an invoice without VAT. A remittance under s 154(1) or (2) goes with a schedule showing the contractor's or supplier's name, Tax ID and address, the invoice number, the gross amount, the VAT and the month (s 154(3)).

### Conservative defaults

These apply the Tier 2 rule and the permitted factual defaults rule in `vat-workflow-base`. A default stands only where the law read fixes the result of the missing fact. Unknown rates, legal scope, counterparty jurisdiction or evidence conditions are otherwise Needs Input.

| Ambiguity | Default |
| --- | --- |
| Registration or Tax ID unknown | HARD STOP under Required inputs |
| Small business limb unknown | Needs Input. Do not stop under R-NG-1, and do not compute. |
| Supply classification unknown | Needs Input. The legacy 'standard-rated at 7.5%' default is replaced, because a receipt can be zero-rated, exempt or no supply at all. |
| Whether an amount relates to a date before 1 January 2026 | Needs Input until known; then R-NG-4 if it does |
| VAT-inclusive or exclusive basis unknown | Needs Input |
| Input VAT with no document held | Needs Input. Nothing is entered until a document under Input VAT documents is held. The legacy 'not claimable' is kept in effect. |
| Mixed use share or method unknown | Needs Input. Section 155(4)(a) allows the taxable proportion, so the law read does not fix nil. The legacy 'no input credit on disputed portion' is replaced. |
| Non-resident supplier, no VAT on the invoice | Needs Input until place of supply, the supplier's appointment and the use are known. Then s 150(2) applies at 7.5%: see Cross-border points. The legacy 'self-account at 7.5%' stands only on those facts. |
| Export shown, evidence or customer location unknown | Needs Input. 7.5% applies only where the supply is verified as a taxable supply in Nigeria under s 145 and is outside ss 185 and 186. Disclose the zero-rated alternative and the output VAT. |
| Foreign currency, exchange rate unknown | Needs Input. See Foreign currency. |
| Credit brought forward from before 2026 | Needs Input. The Transition Guidelines do not address it. |

### Red flag thresholds

Working review settings for the reviewer brief, not legal amounts. They match the archived `nigeria-vat` file.

| Flag | Value |
| --- | --- |
| HIGH single transaction | NGN 10,000,000 |
| HIGH tax delta on a single default | NGN 750,000 |
| MEDIUM counterparty concentration | More than 40% of output or input |
| MEDIUM conservative default count | More than 4 a return |
| LOW absolute net VAT position | NGN 5,000,000 |
| Tier 2 question threshold | NGN 0: no row is filtered on amount, as no Nigerian floor was set |

### VAT 002 lines

The source is the NRS template VAT.XLSX, read at 5 November 2026. Only Schedules A to F are completed; the form fills from them. Valid codes for the working paper's box column are the line numbers below.

| Line | Meaning | Schedule or formula |
| --- | --- | --- |
| 10 | Total sales or income exclusive of VAT | A |
| 15 | Less exempt goods and services in line 10 | A1, category 1 |
| 20 | Less zero-rated goods and services in line 10 | A2, category 2 |
| 22 | Less sales adjustments | B: 'sales returns, credit notes issued, bad debts written off, overstated sales in previous returns, and similar corrections', in the template's words |
| 25 | Sales or income subject to VAT | 10 - 15 - 20 - 22 |
| 35 | Total output VAT at 7.5% | 25 x 7.5% |
| 40 | Standard-rated domestic purchases used for sales | C, from the purchase lists in C_2 for goods, services and fixed assets |
| 45 | Inventory adjustments | C1 |
| 55 | VAT suffered on VATable domestic supplies | (40 + 45) x 7.5% |
| 85 | Imported purchases | D |
| 90 | VAT suffered on imported purchases | D |
| 95 | Total input VAT | 55 + 90 |
| 100 | VAT balance for the current period | 35 - 95 |
| 105 | Input tax on VAT self-charge | E x 7.5% |
| 110 | VAT withheld by MDAs and appointed agents | F |
| 115 | Net VAT balance for the current period | 100 - (105 + 110) |
| 116 | VAT credit from previous period | No formula in the file read |
| 125 | Net VAT due for the current period | No formula in the file read |
| 130 | VAT credit for the current period | No formula in the file read |
| 135 | Total VAT credit | No formula in the file read |
| 140 | Relieved VAT credit | No formula in the file read; meaning held |
| 150 | VAT payable | No formula in the file read |

The template fixes 7.5% and computes VAT from the purchase value, so it can differ from the VAT on a document: a 0% or non-VAT purchase must not go in line 40. Schedule C takes its totals from the C_2 purchase list, which its instructions say populates from the VAT-Track and E-Invoice platforms. A mismatch with the client's records goes in the reconciliation (variance) column, and once the figures are reconciled a detailed schedule of all purchases is uploaded. Schedule C also asks for the amount relating to zero-rated sales, but no form formula reads that column: line 40 reads the total after the variance. The bad debt row of Schedule B is administered only: no bad debt section was found in ss 143 to 157. Schedule A asks for the customer's name and Tax ID, product, category (0 VATable, 1 exempt, 2 zero-rated), and place of consumption by State and Local Government, which serves NTAA s 22(11) attribution. Schedule D asks for the HS code, vessel, country of origin, Form M number, bill of lading number, currency, invoiced value, exchange rate to NGN and other charges. Schedule F asks for the agent's name, address and Tax ID, nature and date of transaction, invoice reference, currency, value and exchange rate.

Line 105 is held. The template subtracts Schedule E, and its status column reads 'Self Charge or Input VAT on Purchases'. It does not say how this line fits the separate remittance under ss 150(2) and 154. Confirm before filing.

### VAT invoice, s 152

The legacy heading cited 'VATA s 10', which in the old Act is the non-resident section; the old invoice section is s 13A. From 2026 the supplier keeps sequential numbering and gives the purchaser a VAT invoice showing: (a) the supplier's Tax ID; (b) the supplier's name and address and the sequential invoice number; (c) incorporation or business registration number as applicable; (d) date of supply; (e) purchaser's name; (f) gross amount; and (g) VAT charged and the rate. It issues on supply whether or not payment is made. A person NRS appoints may issue it. The legacy list of description, quantity and price is not in s 152; keep those details where the document shows them, as they help prove the supply.

### Input VAT documents

The Act names no document for s 155(4). Use these, and name the one held:

- a VAT invoice with the s 152 particulars, for a domestic purchase;
- proof of VAT paid before clearing, with the Schedule D details, for imported goods (s 155(3));
- for VAT withheld or self-accounted, the invoice and proof of remittance; and
- a document NRS accepts in writing for the case.

The last 3 are this file's working list, not a statutory one. Withholding Guidelines para 3 also accepts a bill, debit note or similar document as the place where the supplier states the gross amount, rate and VAT.

### E-invoicing and fiscalisation

A taxable person making a taxable supply implements the fiscalisation system NRS deploys (NTA s 157). Where NRS deploys an Electronic Fiscal System, anyone making a taxable supply uses it for recording and reporting all supplies, and NRS specifies the system and transition (NTAA s 23). Its notice of 20 July 2026 reminds large taxpayers of a Public Notice of 17 February 2026, says compliance monitoring has begun, and requires full compliance by 31 July 2026: onboarding on the Merchant Buyer Solution, integration through approved providers, completion of all required validation and testing, active transmission to the platform, and receipt only of compliant e-invoices with a valid Invoice Reference Number. The NRS e-invoice page links the portal at both https://einvoice.nrs.gov.ng/ and https://einvoice.firs.gov.ng/.

That notice of 17 February 2026 was not read. Who counts as a large taxpayer, and any date for medium or emerging taxpayers, is held: the turnover bands and dates seen came from press reports only. Ask the client whether NRS has told it to onboard.

### Supplier discovery library

The patterns are matching aids. Naming a business does not establish its VAT status, its billing entity or what any invoice shows. No supplier's status was read for this conversion. Always apply the condition. 'Input 7.5%' below means: claim only with a document under Input VAT documents, showing VAT, for taxable use.

**Receipts.** A bank credit is not a VAT classifier.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| TRANSFER FROM [client], INWARD TRF | Candidate taxable supply | Trace to the invoice or agreement. Line 10 only once classified. |
| NIP, NIBSS | Candidate taxable supply | Could be a sale, loan, refund or own transfer: trace it |
| POS SETTLEMENT, POS CREDIT | Candidate taxable supply | Terminal settlement, which may be net of fees. Reconcile it to the processor's statement or sales records: line 10 takes the sale, not the net credit, with fees treated below. If the gross cannot be shown, Needs Input. |
| PAYSTACK PAYOUT, PAYSTACK SETTLEMENT | Candidate taxable supply | same |
| FLUTTERWAVE PAYOUT, RAVE SETTLEMENT | Candidate taxable supply | same |
| OPAY SETTLEMENT, OPAY PAYOUT | Candidate taxable supply | same |
| MONNIFY PAYOUT | Candidate taxable supply | same |
| INTERSWITCH, QUICKTELLER | Candidate taxable supply | same |
| USSD, MOBILE BANKING | Classify by the receipt | Income or expense |
| FGN, STATE GOVT, LGA PAYMENT, MDAs | Candidate taxable supply | Check whether the payer withheld VAT; Schedule F |
| SWIFT, FOREIGN CURRENCY CREDIT | Candidate zero rate | Export test under Cross-border points; otherwise Needs Input |
| RICE, BEANS, GARRI, YAMS, VEGETABLES (sold) | Candidate zero rate | Basic food under s 186(a) and the s 188 list. Legacy 'exempt' corrected. |
| PHARMACY, HOSPITAL, CLINIC (sold) | Candidate zero rate | Products under s 186(b), equipment under (q), services by a qualified health practitioner under (l). Cosmetology, spa and gym services are outside. |
| SCHOOL FEES, UNIVERSITY, COLLEGE (received) | Candidate zero rate | Tuition under s 186(m). Other charges need their own classification. |
| RESIDENTIAL RENT, HOUSE RENT (received) | Candidate exempt | Land or building including an interest in it, s 185(1)(l). The Act does not define 'interest', so confirm a lease is within it; held. |
| INTEREST EARNED, INT CREDIT | Candidate exempt | s 185(1)(m). Include in line 10 and line 15 only as the reviewer directs. |
| LOAN DISBURSEMENT | Exclude | Loan proceeds |
| NRS REFUND, FIRS REFUND | Exclude | Tax refund |

**Banks and payment processors.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| SMS ALERT, BANK CHARGES, COMMISSION, ACCOUNT MAINTENANCE | Check document | The legacy 'exempt (financial service)' is not supported: s 185(1)(m) names money, stakes, securities and interest, not fees. Input only on VAT a document shows. |
| PAYSTACK FEE, FLUTTERWAVE FEE | Check document | same |
| STAMP DUTY | Exclude | Stamp duty |

**Rent, utilities and communications.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| OFFICE RENT, COMMERCIAL LEASE | Candidate exempt: Needs Input | s 185(1)(l) covers land or building including an interest in it, with no commercial carve-out, but the Act does not define 'interest', so whether a lease is within it is held. The legacy 'input 7.5%' is neither kept nor reversed. If a landlord's invoice shows VAT, Needs Input. Separately charged services need their own classification. |
| IKEJA ELECTRIC, EKEDC, AEDC, BEDC | Input 7.5% | Retail supply by a distribution company is not in s 186(j) or (k). Claim only the VAT the bill shows, for taxable use. |
| MTN, GLO, AIRTEL, 9MOBILE | Input 7.5%, by use | Mixed use: Needs Input until the share and method are known |

**Fuel, motor and travel.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| UBER, BOLT | Input 7.5% | Car or ride hailing is outside the s 188 shared transport definition, so it is not exempt on that limb. Claim only the VAT a document shows. |
| TAXI, BUS FARE, DANFO | Check document | Shared passenger road transport is exempt (s 185(1)(g)): no input. A hired vehicle is outside that exemption. |
| FUEL, DIESEL, PMS | Needs Input | Petroleum products are suspended items: s 185(2). No order was read. |
| FLIGHT, AIRLINE | Check invoice | Claim only the VAT the document shows. No air transport item is in ss 185 or 186. |

**Office, software and other costs.** Generic rows state conditions only.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| GOOGLE ADS, META, LINKEDIN | Check invoice | Legacy 'input VAT claimable' is conditioned. VAT shown on a compliant invoice is an ordinary input. No VAT shown: see Cross-border points. No supplier's appointment was read. |
| MICROSOFT, ADOBE, AWS, APPLE, ZOOM | Check invoice | same |
| ANTHROPIC, OPENAI | Check invoice | same |
| OFFICE SUPPLIES, STATIONERY | Input 7.5% | Business purchases |
| COURIER, POSTAGE | Check invoice | Input 7.5% where shown |
| INSURANCE PREMIUM | Check invoice | No insurance limb in ss 185 or 186. Claim only the VAT the document shows. |
| LICENCE FEE, PERMIT, GOVERNMENT FEE | No input on a Government licence | s 185(1)(n). Other fees: check document. |

**Exclusions.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| NRS TAX PAYMENT, FIRS TAX PAYMENT, FIRS VAT, VAT PAYMENT | Exclude | Tax payment, not input VAT |
| SALARY, PAYROLL | Exclude | Employment cost; 'services' under the old Act excluded employment, and the point is held for the NTA |
| PERSONAL WITHDRAWAL, SELF TRANSFER | Exclude | Drawings |
| LOAN REPAYMENT | Exclude | Principal only |
| ATM, CASH WITHDRAWAL | Tier 2, ask | Needs Input: see Transaction questions and defaults |

### Bank exports and narrations

Column layouts are from the prior version and were not checked against any bank's documents. Confirm against the file supplied.

| Bank | Format | Key fields |
| --- | --- | --- |
| GTBank | CSV, PDF | Date, Description, Debit, Credit, Balance |
| First Bank | CSV | Transaction Date, Narration, Debit, Credit, Balance |
| Access Bank | CSV | Date, Description, Debit Amount, Credit Amount, Balance |
| UBA | CSV | Date, Narration, Debit, Credit, Balance |
| Zenith Bank | CSV | Date, Description, Debit, Credit, Balance |
| Fidelity Bank | CSV | Trans Date, Narration, Debit, Credit, Balance |

| Narration | Meaning | Hint |
| --- | --- | --- |
| NIP, NIBSS, INWARD TRF | Interbank transfer in | Potential income |
| POS, SETTLEMENT | POS terminal | Income or expense |
| USSD, MOBILE BANKING | Mobile transfer | Income or expense |
| FGN, MDAs | Government payment | Income; check VAT withheld |
| STAMP DUTY | Stamp duty charge | Exclude |
| VAT, FIRS, NRS | Tax payment | Exclude |
| SMS ALERT | Bank charge | Check document |

### Transaction questions and defaults

Tier 2 catalogue for the structured form in `vat-workflow-base`.

| Item | What is missing | Default | Question |
| --- | --- | --- | --- |
| Small business | A limb of the test | Needs Input | 'Are you a company, or do you trade in another form? What was gross turnover for the year, and how much of it came from capital asset sales or sales made solely on selling or ceasing the business? What are total fixed assets? Do you provide professional services? Have you given NRS a written opt-out notice?' |
| Mixed taxable and exempt supplies | Attribution and method | Needs Input. Directly attributable input follows its supply. Once the reviewer accepts a just and equitable method, apply the proportion. | 'Which purchases relate only to taxable sales, which only to exempt sales, and which to both? What method have you used before?' |
| Mixed private use | Business share | Needs Input | 'What share of this item is used for your taxable sales, and what is that based on?' |
| Non-resident services | Place, appointment, use | Needs Input. Flag for reviewer. | 'Where is the supplier resident? Did the invoice show VAT? Has NRS appointed the supplier or a platform to collect VAT? Has NRS directed you to self-account? Was the service consumed in Nigeria?' |
| Foreign currency invoicing | Currency and rate | Needs Input. Flag the rate source and date. | 'In what currency was the sale invoiced and paid? What rate did you use, from what source, on what date?' |
| VAT withheld | Evidence | Needs Input until the evidence is held | 'Did this customer withhold VAT? Do you hold the evidence, and does the amount match the invoice?' |
| Exported service | Customer and location | Needs Input | 'Is the customer non-resident and outside Nigeria? Is the service for its Nigerian permanent establishment?' |
| Input documents | Whether the document meets s 152 | Needs Input | 'Do you hold a VAT invoice for this purchase showing the supplier's Tax ID, invoice number and VAT?' |
| Cash withdrawal | What the cash paid for | Needs Input. Nothing is entered until the purchase and a document are shown. | 'What did this cash pay for, and do you hold a document for it?' |
| Processor settlement | Gross sales, fees and refunds behind the credit | Needs Input until reconciled | 'Do you hold the processor's statement for this settlement, showing gross sales, fees and refunds?' |
| Rent | The lease terms and what the invoice shows | Needs Input. Enter no input VAT on the rent until the reviewer decides. | 'Do you hold a lease or a licence? Does the landlord's invoice show VAT? Are services charged separately?' |
| Transition | Delivery and payment dates | Needs Input | 'Was any of this delivered, performed or paid for before 1 January 2026?' |

### Onboarding fallback

If the client provides a bank statement but cannot answer the questions at once, the work stays at intake. List credits as candidates only and enter nothing on unknown items. The legacy fallback of applying 7.5% to all unclassified business income is replaced by the defaults above. Note input only where the document is held. Flag all government payments for VAT withheld review. Registration and the Tax ID still have to be confirmed. Ask the groups under Ask the client first, then the Step 6.5 questions. The legacy working paper with PENDING flags is replaced: base Step 6 builds the workbook only after the evidence conditions and answers are resolved, so build nothing and compute no line before then. What stays unanswered is Needs Input, and any result that depends on it is withheld.

### Foreign currency

The legacy rule, 'VAT must be computed in NGN', with the CBN rate on the date of supply, is corrected. Tax is assessed in the currency of the transaction, and tax so assessed in another currency is paid in that currency (NTAA s 39). The VAT 002 template offers NGN, GBP, Euro and USD. Its Schedules D and F have an exchange rate column, but no rate source was read for VAT: Needs Input, and flag for reviewer.

### Excel working paper

Working paper only. Layout for Sheet 'Box Summary' under `vat-workflow-base`.

```
NIGERIA VAT WORKING PAPER (VAT 002)
Taxpayer: _______________  Tax ID: ___________
Month: ___________  Currency: NGN / GBP / Euro / USD

A. OUTPUT (SALES)
  A1. Total sales or income, exclusive of VAT -> Line 10                 ___________
  A2. Exempt supplies included in A1 -> Line 15                          ___________
  A3. Zero-rated supplies included in A1 -> Line 20                      ___________
  A4. Sales adjustments -> Line 22                                       ___________
  A5. Sales subject to VAT (A1 - A2 - A3 - A4) -> Line 25                ___________
  A6. Output VAT (A5 x 7.5%) -> Line 35                                  ___________

B. INPUT (PURCHASES)
  B1. Standard-rated domestic purchases for taxable use -> Line 40       ___________
  B2. Inventory adjustments -> Line 45                                   ___________
  B3. VAT on B1 + B2 -> Line 55                                          ___________
  B4. VAT on imported purchases -> Line 90                               ___________
  B5. Total input VAT (B3 + B4) -> Line 95                               ___________
  B6. Not deductible (exempt or private use): excluded, no line          ___________

C. NET VAT
  C1. Balance (A6 - B5) -> Line 100                                      ___________
  C2. Input tax on VAT self-charge -> Line 105 (held)                    ___________
  C3. VAT withheld by MDAs and appointed agents -> Line 110              ___________
  C4. Net balance (C1 - (C2 + C3)) -> Line 115                           ___________
  C5. Credit from previous period -> Line 116                            ___________
  C6. VAT payable or credit carried -> Lines 125 to 150                  ___________

REVIEWER FLAGS:
  [ ] Registration and Tax ID confirmed?
  [ ] Small business test applied, with each limb evidenced?
  [ ] All input claims supported by a document under Input VAT documents?
  [ ] Mixed supply apportionment just and equitable and consistently applied?
  [ ] Zero-rated and exempt correctly distinguished?
  [ ] Nil return filed if no activity and not a small business?
  [ ] VAT withheld from government and agent contracts accounted for?
  [ ] VAT on non-resident supplies accounted for?
  [ ] Nothing here relates to the repealed law (R-NG-4)?
```

### Key legislation

| Topic | Reference |
| --- | --- |
| VAT imposition and charge | NTA ss 143 and 144 |
| Place, time, rate and value | NTA ss 145 to 149 |
| Non-residents | NTA s 150; NTAA s 6 |
| VAT invoice | NTA s 152 |
| Collection and withholding | NTA ss 153 and 154 |
| Credit, input tax and remission | NTA s 155 |
| Fiscalisation | NTA s 157; NTAA s 23 |
| Exempt and zero-rated supplies | NTA ss 185 to 188; Eleventh Schedule; NTAA s 144(3)(c) |
| Registration | NTAA ss 4 to 8 |
| Small business and returns | NTAA s 22 and the 'Small Business' definition |
| VAT refund | NTAA s 56 |
| Penalties | NTAA ss 65, 100 to 107, 122 and 127 |
| Repeal and savings | NTA ss 195(j), 197 and 198 |

The legacy table's VATA references were to the repealed law, and several were wrong for it: on the 2012 text the old Act's s 10 was non-residents, invoices were s 13A, and there was no s 10A. The 'VATA s 16-18' penalty reference is corrected: on that text s 16 was remittance and s 17 input tax, and penalties were in s 19 and Part V, ss 25 to 37. Later amendments to those sections were read only in part.

### Known gaps

- International VAT recovery: R-NG-2.
- Transfer pricing: R-NG-2.
- Companies Income Tax: R-NG-3.
- Withholding tax on contracts, separate from VAT.
- The agent's own return of VAT withheld: R-NG-7.
- Refund applications, beyond identifying the credit.

## Deadlines and filing

**Which law applies.** The NTA repeals the VAT Act (s 195(j)). Under the Transition Guidelines (paras 10.2.1 and 10.2.2):

- goods delivered or services rendered up to 31 December 2025 stay under the repealed law, whenever paid;
- transactions from 1 January 2026 fall under the new Acts, except where payment was made in advance before commencement;
- for a contract made before and executed after commencement, the new Acts apply only to the part executed after commencement;
- sums received before commencement are taxed under the repealed law and sums received after under the new Acts.

Para 10.2.2(2) can be read against para 10.2.1, which turns on delivery 'irrespective of when payment is made'. Para 5(2) says no filing obligation under the Acts applies to a period before commencement; para 6(2) says returns due from commencement use forms under the Acts; para 6(3) keeps existing forms valid pending new ones. So the December 2025 return is held on its form. R-NG-4 applies. Whether the Guidelines were published in the Gazette is held; NTAA s 144(3) and NTA s 200(2)(c) both provide for publication in the Federal Government Gazette.

| Item | Rule | Source |
| --- | --- | --- |
| Filing frequency | Monthly | NTAA s 22(1) |
| Return due | On or before the 21st of the following month, with or without a notice | NTAA s 22(1) |
| Payment due | Not later than the due date for the return | NTA s 155(1); VAT 002 notes |
| Filing extension | Does not extend the time to pay | NTAA s 22(2) |
| Nil returns | Required 'whether or not an economic activity has taken place', except from a small business | NTAA s 22(1) and (4) |
| Filing route | Complete the template and upload it on Rev360 | NRS Tax Returns Forms page |
| VAT withheld or self-accounted | Remit by the 14th of the following month, or as NRS prescribes | NTA s 154(4) |
| Real-time returns | Where NRS deploys the technology, at the time it prescribes | NTAA s 22(10) |

**Conflict on the 14th.** NTA s 154(4) and the Withholding Guidelines (paras 4 and 7.1) say the 14th. The NTAA s 107 penalty is triggered by the 21st. NRS's circular gives 14 days for VAT withheld and 21 for output VAT. Transition Guidelines para 14(2) says that where 2 provisions of the new Acts appear inconsistent, the interpretation that best reflects legislative intent, economic neutrality and administrative simplicity prevails, and para 14(3) resolves a clear inconsistency in favour of the taxpayer. Whether this is such a conflict, and what force the Guidelines have against an Act, is held. Use the 14th as the cautious date, and do not treat the 21st as a safe date.

No rule moving a due date that falls on a weekend or public holiday was found in the sections read: held. June 2026's 21st was a Sunday.

### Filing on Rev360

The legacy portal, TaxPro Max (taxpromax.firs.gov.ng), is corrected for filing guidance. The NRS forms page says to complete VAT.XLSX and upload it on Rev360. The NRS self-service page links to https://selfservice.nrs.gov.ng/, and the NRS home page names that portal 'Rev360 for Taxpayers'. Whether any taxpayer class stays on TaxPro Max for a period is held: that claim was seen only in a secondary report. The NRS Rev360 manual sits behind a sign-in and was not read, so the screen steps are not given here. This workflow does not file or pay.

1. Download VAT.XLSX from the NRS forms page.
2. Complete Schedules A to F as applicable, checking any purchases already populated in Schedules C and C_2. The form fills from them; do not type into lines 10 to 150.
3. Review the form, and complete and sign the declaration.
4. Upload on Rev360 by the 21st, and pay by the same date.

WVAT.XLSX is the separate schedule for VAT withheld: R-NG-7.

### Credits and refunds

Excess input VAT is a credit against later months (NTA s 155(1)(b)). Excess not used is refundable on request with the information NRS requires (s 155(2)). The request is in the prescribed form, within 12 months after the transaction, or it lapses (NTAA s 56). Within 30 days of a valid request NRS refunds or sets off (s 56; Refund Guidelines para 12). The application goes through the NRS tax administration solution or the relevant Executive Director, and all due returns must be filed (paras 5 and 10.1). A request is valid only when all prescribed information and documents are supplied. Do not record an unapproved refund as cash received.

## Penalties and interest

The legacy column of pre-2026 VATA penalties is not carried: R-NG-4 applies, and those amounts were not proved from a primary text. The NTAA column is kept and checked. From commencement:

| Default | Rule | Source |
| --- | --- | --- |
| Failure to register | NGN 50,000 in the first month; NGN 25,000 each subsequent month | NTAA s 100(1) |
| Contract awarded to an unregistered person | NGN 5,000,000, on a statutory body or company | NTAA s 100(2) |
| Failure to file, or knowingly incomplete or inaccurate return | NGN 100,000 in the first month; NGN 50,000 each subsequent month | NTAA s 101 |
| Late payment | Subject to s 67: 10% of the tax payable, plus interest: naira, CBN monetary policy rate plus a spread set by the Minister; foreign currency, SOFR or successor plus such a spread. NRS may remit for good cause (s 66). | NTAA s 65(1) |
| Books and records | NGN 10,000 for a person other than a company; NGN 50,000 for a company | NTAA s 102 |
| Refusing access to deploy technology, 30 days after the notice | NGN 1,000,000 for the first day of default; NGN 10,000 each subsequent day | NTAA s 103 |
| Failure to use the fiscalisation system | NGN 200,000 plus 100% of the tax due plus interest at the CBN monetary policy rate a year | NTAA s 104 |
| Failure to collect, deduct or withhold | 40% of the amount not deducted | NTAA s 105 |
| Failure to make attribution | NGN 1,000,000 | NTAA s 106 |
| Failure to remit tax deducted, collected or withheld by the 21st | The amount, plus 10% a year, plus interest at the CBN monetary policy rate | NTAA s 107(1) |
| Failure to self-account in time | The tax, plus 10% a year, plus interest at that rate | NTAA s 107(2) |
| False or fictitious VAT refund claim | The amount received, plus 100% of it, plus interest at that rate | NTAA s 122 |
| Failure to issue a VAT invoice | No specific penalty found on a text search of the NTAA or the NTA. NTAA s 127 penalises a contravention of 'this Act', which is the NTAA, and the invoice duty is in NTA s 152, so whether s 127 reaches this breach is held and no amount is stated. Section 104 covers only a failure to process a taxable supply through the fiscalisation system. | NTA s 152; NTAA ss 104 and 127 |

Section 67 makes tax due a debt, lets NRS issue a demand notice for the tax, penalty and interest where tax is unpaid after 30 days, and provides for recovery. As read it sets no different amount, and no example here computes a s 65 penalty. The legacy 'failure to collect VAT' row is corrected to the words of s 105. The NRS VAT page applies NGN 100,000 and NGN 50,000 to 'late registration or filing'; s 100 sets lower amounts for registration, so s 100 is used. The Minister's spread and the current monetary policy rate were not read, so interest is not computed here. Section 22(8) as printed lifts ss 100 and 102 for an exempted person.

## Cross-border points

**Exports.** Exported goods, excluding oil and gas, are goods produced or procured for commercial purposes by a person in Nigeria and supplied to a person outside Nigeria (ss 186(n), 188). An exported service is rendered to a non-resident person outside Nigeria by a taxable person, wherever rendered; a service to the Nigerian permanent establishment of a non-resident does not qualify (s 201). No list of export proof appears in the sections read. Keep the contract, invoice, shipping or delivery evidence and payment records, and note that this list is a working one.

**Non-resident suppliers.** A non-resident making taxable supplies to Nigeria registers and includes VAT on its invoice (s 150(1); NTAA s 6). Where it supplies from outside Nigeria to persons in Nigeria, the taxable person receiving the supply withholds and remits (s 150(2)). NRS may appoint any person, including a non-resident supplier, to collect (s 150(3)); then the customer does not withhold unless the appointee failed to collect (s 150(4)). Legacy 'VATA s 10A' and its digital-only wording are corrected: s 150 covers all taxable supplies, and no s 10A was found in the old Act's 2012 text. Legacy wording said the recipient 'may' self-account; s 150(2) says 'shall withhold'.

Input on that VAT follows s 155(4). Do not describe it as nil cash: the withheld amount is remitted first. A person not registered or not a taxable person is held. Whether s 154(4)'s 14th applies to s 150(2) withholding by a person who is not an appointed agent is also held, though Withholding Guidelines para 4.1 brings that case 'in line with these Guidelines'.

**Imported goods.** An importer pays the VAT to NRS before clearing (s 155(3)). Goods bought through a non-resident online platform whose VAT was collected are not charged again on proof of payment (s 150(8)). Report imports in Schedule D.

## Two worked examples that recompute

All examples are hypothetical, apply 7.5%, assume a registered taxable person that is not a small business unless stated, and treat amounts as VAT exclusive unless stated. Each is checked by CI. Dates assume the VAT month of June 2026, with the operational hold lifted.

### Example 1: standard monthly return

**Input.** Taxable supplies NGN 5,000,000. Input VAT from purchases NGN 150,000, VAT invoices held, wholly for taxable use.

```oa-check
name: NG VAT 002 standard return on VAT exclusive and VAT inclusive facts
inputs:
  sales_excl: 5000000
  input_vat: 150000
  rate: 7.5
steps:
  - line_35: pct(sales_excl, rate)
  - payable: line_35 - input_vat
  - alt_output: round(sales_excl * rate / (100 + rate), 2)
  - alt_payable: alt_output - input_vat
expected:
  line_35: 375000
  payable: 225000
  alt_output: 348837.21
  alt_payable: 198837.21
```

**Result.** VAT payable NGN 225,000, on the VAT exclusive facts. Bank statements show VAT inclusive amounts, so state the basis: had NGN 5,000,000 been a VAT inclusive total, payable would be NGN 198,837.21. Return and payment are due by Tuesday 21 July 2026.

### Example 2: exporter in a credit position

**Input.** Exports of services NGN 10,000,000. Input VAT NGN 300,000, documents held. In the second case, NGN 2,000,000 of those services went to the Nigerian permanent establishment of the non-resident customer, and the supply is verified as taxable in Nigeria and outside ss 185 and 186.

```oa-check
name: NG exporter credit with and without the exported service test met
inputs:
  exports: 10000000
  to_pe: 2000000
  input_vat: 300000
  rate: 7.5
steps:
  - case1_output: 0
  - case1_credit: input_vat - case1_output
  - case2_output: pct(to_pe, rate)
  - case2_credit: input_vat - case2_output
expected:
  case1_output: 0
  case1_credit: 300000
  case2_output: 150000
  case2_credit: 150000
```

**Result.** First case: output VAT nil and a credit of NGN 300,000. Second case: the NGN 2,000,000 is not an exported service, so output VAT is NGN 150,000 and the credit is NGN 150,000. Either credit goes against later months or, if unused, may be the subject of a refund request within 12 months. The legacy example's 'refund from FIRS' is corrected to NRS.

### Example 3: mixed taxable and exempt supplies

**Input.** Taxable supplies NGN 3,000,000, exempt supplies NGN 2,000,000. Total input VAT NGN 200,000, none directly attributable. Case 1: the reviewer accepts a revenue ratio. Case 2: the reviewer accepts a floor area share of 50%.

```oa-check
name: NG input VAT apportionment under two accepted methods
inputs:
  taxable: 3000000
  exempt: 2000000
  input_vat: 200000
  area_share: 50
  rate: 7.5
steps:
  - output: pct(taxable, rate)
  - ratio_pct: round(taxable / (taxable + exempt) * 100, 2)
  - case1_input: pct(input_vat, ratio_pct)
  - case1_payable: output - case1_input
  - case1_expensed: input_vat - case1_input
  - case2_input: pct(input_vat, area_share)
  - case2_payable: output - case2_input
expected:
  output: 225000
  ratio_pct: 60
  case1_input: 120000
  case1_payable: 105000
  case1_expensed: 80000
  case2_input: 100000
  case2_payable: 125000
```

**Result.** VAT payable is NGN 105,000 on the revenue ratio, with NGN 80,000 expensed, or NGN 125,000 on the floor area share. Neither is the statutory method: s 155(4)(a) gives none, and s 193(2) requires a just and equitable method consistently applied. Flag for reviewer.

### Example 4: nil return, or no return at all

**Input.** A month with no supplies or purchases. Case 1: a consultant in professional services with annual turnover of NGN 40,000,000. It misses the return and it stays outstanding for 3 months. Case 2: a trading company with annual gross turnover of NGN 115,000,000, of which NGN 30,000,000 is the sale of a capital asset, fixed assets of NGN 200,000,000, no professional services and no opt-out.

```oa-check
name: NG nil return penalty and small business test
inputs:
  months_late: 3
  first_month: 100000
  later_month: 50000
  gross: 115000000
  capital_sale: 30000000
  assets: 200000000
  turnover_limit: 100000000
  asset_limit: 250000000
steps:
  - vat_due: 0
  - penalty: first_month + later_month * max(months_late - 1, 0)
  - counted: gross - capital_sale
  - turnover_margin: turnover_limit - counted
  - asset_margin: asset_limit - assets
  - margin_without_exclusion: turnover_limit - gross
expected:
  vat_due: 0
  penalty: 200000
  counted: 85000000
  turnover_margin: 15000000
  asset_margin: 50000000
  margin_without_exclusion: -15000000
```

**Result.** Case 1 must file a nil return by the 21st, because a business providing professional services is never a small business, at any turnover. VAT is nil, and the s 101 penalty on the facts given is NGN 200,000. Case 2 counts NGN 85,000,000 under s 22(7)(a), and both margins are at or above zero, so all limbs of R-NG-1 are met and the workflow stops. Without that exclusion, the NGN 115,000,000 would be NGN 15,000,000 above the limit. So for an individual trader on the same figures, the result turns on whether s 22(7) reaches that person: it is Needs Input, neither the stop nor a computed return.

### Example 5: supplier to a government agency

**Input.** Sales to a ministry NGN 8,000,000, on which it withheld all the VAT of NGN 600,000, with evidence held. Other sales NGN 2,000,000. Input VAT NGN 900,000 on all supplies, documents held, wholly for taxable use.

```oa-check
name: NG VAT withheld by a government customer
inputs:
  to_mda: 8000000
  other: 2000000
  input_vat: 900000
  rate: 7.5
steps:
  - withheld: pct(to_mda, rate)
  - line_35: pct(to_mda + other, rate)
  - line_100: line_35 - input_vat
  - line_115: line_100 - withheld
  - net_output: line_35 - withheld
  - excess: input_vat - net_output
  - after_withheld: input_vat - withheld
  - refund_illustration: after_withheld - pct(other, rate)
expected:
  withheld: 600000
  line_35: 750000
  line_100: -150000
  line_115: -750000
  net_output: 150000
  excess: 750000
  after_withheld: 300000
  refund_illustration: 150000
```

**Result.** Output VAT NGN 750,000 in line 35. Line 110 is NGN 600,000 and line 115 is NGN 750,000 negative, which matches Withholding Guidelines para 8: net output NGN 150,000, input NGN 900,000, excess NGN 750,000. Nothing is payable for the month. Refund Guidelines para 11.2 points the other way: its illustration nets the withheld VAT against input, which here leaves NGN 300,000, and its Note lets input be claimed against output VAT from other supplies, which here would leave NGN 150,000. Reading the 2 passages together that way is an inference. The difference is unresolved, so do not state a refund amount. Show the line 115 result and flag it for the reviewer.

### Example 6: service from a non-resident

**Input.** A registered business buys software from a non-resident supplier, for NGN 1,000,000 with no VAT on the invoice. NRS has not appointed the supplier. The service is provided to and consumed by the business in Nigeria. Use is 60% taxable supplies and 40% private, on a basis the reviewer accepts.

```oa-check
name: NG VAT withheld on a non-resident supply with part private use
inputs:
  invoice: 1000000
  taxable_share: 60
  rate: 7.5
steps:
  - vat_withheld: pct(invoice, rate)
  - input_allowed: pct(vat_withheld, taxable_share)
  - cost_after_input: vat_withheld - input_allowed
expected:
  vat_withheld: 75000
  input_allowed: 45000
  cost_after_input: 30000
```

**Result.** NGN 75,000 is withheld and remitted under s 150(2). NGN 45,000 may be deducted under s 155(4). The other NGN 30,000 is a cost. Use 14 July 2026, Tuesday, for the remittance, given the conflict under Deadlines and filing. Line 105 is held.

### Example 7: processor settlement net of fees

**Input.** A bank credit 'PAYSTACK SETTLEMENT NGN 980,000'. The processor's statement shows VAT inclusive sales of NGN 1,000,000 and a fee of NGN 20,000 kept from the payout. All the sales are standard-rated.

```oa-check
name: NG processor settlement reconciled to gross sales
inputs:
  settled: 980000
  fee: 20000
  rate: 7.5
steps:
  - gross_sales: settled + fee
  - output_vat: round(gross_sales * rate / (100 + rate), 2)
  - line_10: gross_sales - output_vat
  - on_net_credit: round(settled * rate / (100 + rate), 2)
  - understated: output_vat - on_net_credit
expected:
  gross_sales: 1000000
  output_vat: 69767.44
  line_10: 930232.56
  on_net_credit: 68372.09
  understated: 1395.35
```

**Result.** Line 10 is NGN 930,232.56 and output VAT NGN 69,767.44. Treating the net credit as the sale would understate output VAT by NGN 1,395.35. That the fee does not reduce the value is this file's reading of s 148(1)(a), the consideration being what the customer pays. The fee is a separate cost, with input only on VAT a document shows. Without the statement, this is Needs Input, not a computed figure.

### Transaction patterns

| Input | Treatment |
| --- | --- |
| Credit 'PAYSTACK SETTLEMENT NGN 980,000' | Candidate taxable supply, possibly net of fees. Needs Input until reconciled to gross sales; treat the fee separately. See Example 7. |
| Debit 'OFFICE RENT NGN 500,000' | Candidate exempt under s 185(1)(l): Needs Input, because whether a lease is an 'interest' is held. |
| Debit 'GOOGLE ADS NGN 200,000', no VAT on the invoice | Needs Input; see Cross-border points. |
| Credit 'FGN PAYMENT NGN 930,000' | Candidate taxable supply; check VAT withheld. |
| Debit 'SMS ALERT NGN 40' | Check document. Not exempt on the sources read. |

## Ask the client first

Use these 6 groups in the workflow base's order. Infer what the statement shows first (Step 3), and at the Step 4 confirmation ask only the items below that the data could not show. Groups 1, 2 and 6 feed the refusal checks at Step 5. Points in groups 3 to 5 that turn on a transaction go to Step 6.5, through Transaction questions and defaults. Build nothing before Step 7. An unanswered item stays Needs Input.

1. **Registration.** Are you registered with NRS, and what is your Tax ID? What month does this statement cover? Are you on Rev360, and has NRS told you to onboard for e-invoicing?
2. **Small business.** Are you a company, or do you trade in another form? What is your annual gross turnover, and how much of it came from capital asset sales or sales made solely on selling or ceasing the business? What are your total fixed assets? Do you provide professional services? Have you given a written opt-out notice?
3. **Sales.** What goods or services do you sell, and where are they consumed? Any zero-rated supplies (basic food, medical, tuition, exports) or exempt supplies (land or buildings, money or securities, shared road transport)? Do you sell in foreign currency?
4. **Customers.** Do you sell to government bodies or appointed agents, and did they withhold VAT? Do you hold the evidence?
5. **Purchases.** Do you hold valid VAT invoices for all input claims? Do you import goods or services, or buy from non-residents? Is anything used partly for exempt supplies or privately?
6. **Balances and transition.** What excess credit is carried from the prior month, and where does it come from? Was anything delivered, performed or paid for before 1 January 2026?

### Completion checks

- Registration and Tax ID confirmed.
- Small business test applied, with each limb evidenced. Turnover and fixed assets tested for 2026; professional services excluded at any turnover; NGN 25,000,000 not used.
- All input claims supported by a document under Input VAT documents.
- Exempt supplies identified and excluded from output VAT; zero-rated supplies not treated as exempt.
- Withheld and self-accounted VAT shown, with the 14th noted.
- Nil return filed if no activity and not a small business.
- Return and payment by the 21st of the following month.
- Any result that turns on the 2 texts of the NTA is flagged.

## Sources

Read on means the date read for this conversion. Limits follow each source. Citations to the NTA are to the working text.

| Source | URL | Read on |
| --- | --- | --- |
| Nigeria Tax Act 2025, Act No. 7, working text, National Assembly PDF, read in part: ss 143 to 157, 185 to 189, 193, 195, 197, 198, 200, 201 definitions and the Eleventh Schedule | https://nass.gov.ng/documents/download/11249 | 2026-11-05 |
| Same file as reported released by the House of Representatives, third-party media host, SHA-256 identical to the National Assembly PDF; not separately read | https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf | 2026-11-05 |
| Nigeria Tax Act 2025, scanned copy on the NRS site, fetched by the Nigerian income tax conversion, read in part: ss 144 to 158, 186 to 189, s 202 'small company'; poor text extraction, so no line-by-line comparison; ss 148, 153 to 155, 157 and 186 read on the page image | https://www.nrs.gov.ng/uploads/NIGERIA_TAX_ACT_2025_ef6bb812a5.pdf | 2026-11-05 |
| Nigeria Tax Administration Act 2025, Act No. 5, Tax Appeal Tribunal PDF (the file name says Tax Act), read in part: ss 3 to 8, 22, 23, 31, 39, 56, 65, 66, 100 to 107, 121, 122, 127, 144 and definitions | https://tat.gov.ng/Nigeria-Tax-Act-2025.pdf | 2026-11-05 |
| Nigeria Tax Administration Act 2025 as reported released by the House of Representatives, third-party media host, compared by clause with the Tribunal PDF after removing spaces; poor text extraction in places; 13 of 88 hunks were filtered for reading and read, and the others passed a filter on numbers and letter counts | https://media.premiumtimesng.com/wp-content/files/2026/01/Approved-Copy-to-Print-NIGERIA-TAX-ADMINISTRATION-ACT-2025.pdf.pdf | 2026-11-05 |
| General Transition Guidelines for the Tax Acts 2025, read in full, in a PDF the Nigerian income tax conversion fetched from a private consultant's website, as no official copy was found; the Ministry statement at the URL confirms the issue of the Guidelines, not that text | https://fmino.gov.ng/federal-government-issues-transition-guidelines-for-tax-acts-2025/ | 2026-11-05 |
| NRS information circular on changes in the administration of VAT, Circular 2026/05, read in full | https://www.nrs.gov.ng/uploads/INFORMATION_CIRCULAR_ON_CLARIFICATION_ON_THE_CHANGES_IN_THE_ADMINISTRATION_OF_THE_VALUE_ADDED_TAX_23_3_26_4adf581b75.pdf | 2026-11-05 |
| NRS Guidelines on the Withholding of VAT, Circular 2026/18, read in part: paras 2 to 9 | https://www.nrs.gov.ng/uploads/GUIDELINES_ON_THE_WITHHOLDING_OF_VAT_30_05_26_4601d747cf.pdf | 2026-11-05 |
| NRS Guidelines on Tax Refund, Circular 2026/17, read in part: paras 5 and 10 to 16 | https://www.nrs.gov.ng/uploads/GUIDELINES_ON_TAX_REFUND_30_05_2026_85b67c6137.pdf | 2026-11-05 |
| NRS VAT 002 template, VAT.XLSX, read in full for labels, lists and formulas, values in other sheets by sample | https://www.nrs.gov.ng/uploads/VAT_7cd6cf6a80.xlsx | 2026-11-05 |
| NRS VAT withheld schedule, WVAT.XLSX, read in part: headings | https://www.nrs.gov.ng/uploads/WVAT_b0097007f9.xlsx | 2026-11-05 |
| NRS Value Added Tax page, read in full | https://www.nrs.gov.ng/tax-information/value-added-tax | 2026-11-05 |
| NRS Tax Returns Forms page, read in part: VAT rows | https://www.nrs.gov.ng/compliance/tax-returns-forms | 2026-11-05 |
| NRS filing and payment deadlines page, read in part: VAT row | https://www.nrs.gov.ng/compliance/filing-and-payment-deadlines | 2026-11-05 |
| NRS home page, read in part: Rev360 link | https://www.nrs.gov.ng/ | 2026-11-05 |
| NRS self-service portal page, read in part | https://www.nrs.gov.ng/taxpayer-services/self-service-portal | 2026-11-05 |
| NRS notice of 20 July 2026, e-invoicing compliance monitoring, read in full; the site's list also shows it at news-release-4 and news/162, so this address may not be stable | https://www.nrs.gov.ng/news/news/news-release-2 | 2026-11-05 |
| NRS e-invoice page, read in part: portal link | https://www.nrs.gov.ng/taxpayer-services/e-invoice | 2026-11-05 |
| FIRS Tax Law Compendium, July 2012, VAT Act text, read in part: ss 4, 8, 10, 13, 13A, 15 to 17, 19, 29 to 35, 40, 46, the Part V contents and the First Schedule; before the Finance Act amendments | https://www.nrs.gov.ng/uploads/FIRS_Tax_Law_Compendium_a00a142660.pdf | 2026-11-05 |
| Finance Act 2020, Act No. 1 of 2021, Gazette No. 4, Vol. 108, read in part: ss 40 to 45; poor text extraction, in the PDF retained by the Nigerian income tax conversion | https://archive.gazettes.africa/archive/ng/2021/ng-government-gazette-dated-2021-01-04-no-4.pdf | 2026-11-05 |
| Finance Act 2021, read in part: ss 30 to 32, in the PDF retained by the Nigerian income tax conversion | https://budgetoffice.gov.ng/index.php/resources/internal-resources/budget-documents/finance-act-2021/download | 2026-11-05 |

Not yet confirmed: which text of the NTA is law, and whether any re-gazetted text exists; the small company amount if the scanned copy governs; whether electric vehicles are zero-rated; the meaning of 'Part IX' in s 147, 'Tenth Schedule' in s 186, 's 146' in s 153 and 's 191' in s 156; any Minister's order under the Eleventh Schedule; any order under s 187 or NTAA s 144(3)(c); whether a donor must pay first under s 185(1)(c) and whether stakes are exempt under s 185(1)(m); aggregation, period and asset basis for the small business test; whether NTAA s 22(7) reaches a person that is not a company; the meaning of professional services; whether the Transition Guidelines were gazetted, and how paras 5(2), 6(2), 6(3), 10.2.1 and 10.2.2 fit together; credit brought forward from before 2026; line 105, line 140 and the formulas after line 115; the amount claimable where output VAT is withheld; the effect of s 22(8) on purchases by a small business; the 14th against the 21st, and the force of Transition Guidelines para 14; whether the 14th applies to s 150(2) withholding; whether a person not registered or not a taxable person withholds under s 150(2); the exchange rate source for VAT; the penalty for failing to issue a VAT invoice, including whether NTAA s 127 reaches a breach of the NTA; whether a processor's fee affects the value of a supply; whether employment is outside 'services' under the NTA; the Nigeria Revenue Service (Establishment) Act 2025, which was not read; due dates on non-working days; the Minister's spread and current monetary policy rate; export evidence; the scope of the 17 February 2026 e-invoicing notice; Rev360 screen steps and any class remaining on TaxPro Max; bad debt relief; suspensive conditions; rent as an interest in land; and all law before 2026.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.3 | 2026-11-05 | Converted to the upstream template as the return workflow file. Rebuilt on the NTA and NTAA from 1 January 2026, named the working text, moved earlier periods to R-NG-4, and corrected zero-rated and exempt lists, input VAT, invoice, record, portal, currency, withholding and penalty statements. Added the operational hold and the workflow slots. |
| 2.2 | November 2026 | Legacy: penalties shown under the NTAA from 1 January 2026. |
| 2.0 | April 2026 | Legacy: full rewrite to the v2.0 structure, Nigerian bank formats, local payment patterns and worked examples. |
| 1.0 | 2025 | Initial. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a chartered accountant (FCA/ACA) or accredited tax practitioner in Nigeria) before filing or acting upon.
