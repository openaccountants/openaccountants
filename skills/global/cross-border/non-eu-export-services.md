---
name: non-eu-export-services
description: Use this skill for the 2026 VAT/GST treatment of services sold to overseas clients by EU, UK, Australian, Indian and Singaporean freelancers or businesses. It distinguishes outside-scope supplies, GST-free or zero-rated exports, and domestic exceptions; tests customer status, establishments, service type, beneficiaries and payment evidence; and identifies invoice, return and input-credit conditions. Triggers include "export of services", "overseas client", "services to a US client", "no VAT", "Division 38", "LUT", "Fifth Schedule" or "international services". The former Singapore Fifth Schedule shortcut is corrected to section 21(3). Destination-country liability and unconfirmed national return fields require their own supported country guidance.
jurisdiction: GLOBAL
category: cross-border
tax_year: 2026
version: 1.1
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: cross-country-method
---

# Non EU Export Services v1.1

## Scope

Determine the seller-side indirect-tax treatment of services supplied across borders by an EU, UK, Australian, Indian or Singaporean business. A foreign customer or foreign consumption alone does not establish export relief. Establish the place of supply, any specific relief, who owes the tax, input-credit entitlement and the applicable reporting obligation separately. Goods exports, destination-country registration computations and permanent-establishment income tax are separate jobs.

| Metadata | Current scope |
|---|---|
| Jurisdiction | EU, UK, Australia, India, Singapore; other countries need their own law |
| Contributor | OpenAccountants |
| Currency | 2026 rules checked on 15 November 2026; older retrieved official copies and filing-cycle limits identified in Sources |
| Skill version | 1.1 |
| Primary legislation | EU Directive Articles 43-59a and 169; UK VATA section 7A and Schedule 4A; Australian GST Act section 38-190; Indian IGST sections 2(6), 13 and 16 with the enacted 2026 amendment; Singapore GST Act section 21(3), as explained by IRAS |
| Related guidance | `eu-reverse-charge.md`, `eu-oss-digital.md`, `vat-place-of-supply-master.md`, `permanent-establishment-risk.md` and the actual seller/destination country VAT/GST return Guide |

**Confidence labels:** the original [T1] standard B2B scenarios are straightforward only after their legal conditions and evidence are established; [T2] land, events, transport and mixed supplies require classification and review; [T3] unclear consumption, establishments or complex multi-party arrangements require referral. These are internal task labels, not approval tiers or permission to skip professional review. This revision remains tier 2, without accountant attestation.

### Quick reference

| Seller / situation | Starting treatment, subject to exceptions | Primary source |
|---|---|---|
| EU ordinary business-use service to a non-EU business | Article 44 customer-establishment rule; outside seller VAT only if the relevant customer establishment is outside the EU | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| EU service to non-EU consumer | Article 45 supplier rule unless a specific rule, including Articles 47, 54, 58 or 59, changes it | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| UK ordinary B2B service to non-UK business | Section 7A recipient-belonging rule, subject to Schedule 4A | https://www.legislation.gov.uk/ukpga/1994/23/section/7A/data.xml |
| Australian service to overseas customer | Prove a particular section 38-190 item and all applicable exclusions; item 2 and item 3 are distinct routes | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |
| Indian service export | All 5 section 2(6) conditions (derived count), current place rule and compliant bond/LUT or eligible notified tax-paid route | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf |
| Singapore international service | Qualifying section 21(3) provision; overseas contract alone is insufficient | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services |

## Ask the client first

Read contracts, invoices, prior returns and existing case material first. Ask only unresolved facts, together:

1. Where is the seller established and registered, under which VAT/GST scheme, and for what supply/return period?
2. Who contracts and pays, where do the customer and relevant establishments belong, and is the service for business or private use?
3. What exactly is supplied, including bundled goods, rights, land, event admission, training, transport or intermediary elements?
4. Where is the service performed, where are relevant land/goods, and who actually receives or directly benefits from it? Identify any Australian or Singapore beneficiary.
5. What supports the customer's status/location and the intended use, including tax identifiers, commercial checks and establishment facts?
6. For India, what are the permitted currency, actual receipt date, RBI/FEMA evidence, separate-person facts and current-year LUT/bond or notified paid-route eligibility? For all sellers, what supports input deduction and the actual return field?

Stop an unsupported classification or final invoice if the seller, recipient/status or relevant establishment is unknown; also stop when service type or another decisive fact is missing. A foreign postal address is not enough. EU customer-status/private-use/establishment tests: Regulation 282/2011 Articles 18-22, https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; UK evidence and belonging: Notice 741A sections 2-4 and 6, https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a.

## The method, step by step

### Step 1: Separate outside scope, zero-rated and exempt

An outside-scope service is located outside the seller's taxing jurisdiction. A zero-rated/GST-free service qualifies for a specific domestic relief. An exempt/input-taxed supply is a different category and can restrict credits. Even if the customer pays no seller tax in both cases, the legal basis, invoice wording, deduction and reporting can differ. There is no worldwide rule that all B2B services are taxed only in the customer's country: use the relevant country rule and exceptions. UK Notice 741A sections 1-2 and 6: https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a; EU Articles 44-59a and 168-178: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

Do not promise FULL input recovery merely because a service is exported. For EU outside-territory transactions, Article 169(a) requires that deduction would be available if the transaction occurred domestically, and excludes Article 284-exempt transactions; Article 169(c) separately addresses specified exempt financial/insurance transactions with non-EU customers. Mixed use, non-business expenditure, national exclusions and invoice evidence still matter under Articles 173, 176 and 178. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1. The country rules below impose their own conditions.

### Rates used in the conditional cases

| Item | Rate / conditions | Primary source |
|---|---|---|
| Malta ordinary taxable event/training | 18% standard rate (in words on the page); only after excluding an exemption or Eighth Schedule reduced treatment | https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 |
| UK ordinary taxable land survey | 20% standard rate; not an exempt/reduced/zero-rated supply | https://www.gov.uk/vat-rates |
| Metropolitan France ordinary taxable service | 20% standard rate; the yoga example still requires its actual exemption/franchise and classification checks | https://www.douane.gouv.fr/fiche/les-taux-de-tva |

### Step 2: EU seller to a non-EU customer

#### B2B general rule and evidence

For a taxable customer acting as such, Article 44 locates an ordinary service at the customer's business establishment, or the fixed establishment receiving it, or the fallback permanent address/usual residence. Thus remote business consulting, software development or design supplied to the evidenced US/Japanese establishment is normally outside the seller's EU VAT, subject to the particular rules below and any implemented Article 59a use/enjoyment override. Do not treat a non-EU head-office address as decisive if an EU establishment actually receives the service. Sources: Articles 43-45 and 59a, https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; Regulation Articles 18(3), 19 and 20-22, https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

For a non-EU customer, obtain the relevant tax-authority business certificate, or the business tax/similar identifier or other proof plus reasonable commercial verification, unless contrary information exists. Exclusively private-use services follow B2C rules even if bought by a business. The EU rules also deem specified non-taxable legal persons identified for VAT to be taxable for place-of-supply purposes; do not equate business status solely with possession of an EU VAT number. Sources: Article 43, https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; Regulation Articles 18-19, https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

Do not describe an Article 44 supply outside the EU as an EU statutory 0% rate. A descriptive invoice note such as "Outside the scope of VAT - place of supply outside the EU" records the conclusion; it is not a universally prescribed wording. Check the seller's invoice rules, and any destination-country reverse charge. Article 219a determines the applicable invoicing framework and Article 226 includes the required "Reverse charge" wording where the customer is liable. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

There is no EU recapitulative-statement entry for an ordinary service actually located outside the EU merely because the seller is EU-established. Article 262 concerns the specified intra-EU transactions, including qualifying Article 196 services. Intrastat concerns goods movements, not these pure service supplies; separate national services-statistics duties may exist. Sources: Article 262, https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; the goods-movement distinction in the official 2026 ELSTER instructions, https://www.elster.de/eportal/helpGlobal?themaGlobal=help_ustva_2026.

#### B2C general rule, listed services and special places

| Service to a non-EU private consumer | Place rule and condition | Primary source |
|---|---|---|
| Consulting, legal, accounting, engineering, advertising, data processing/information; IT only if its actual nature fits a listed category | Article 59 shifts the listed service to the customer's established/permanent/usual location outside the EU; an IT label alone is not enough | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Telecommunications, broadcasting or electronically supplied service | Article 58 customer location; email communication alone does not make a human-delivered service electronic; destination-country tax may arise | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Property/land-related service | Article 47 property location; establish a sufficiently direct connection, not merely a customer's property interest | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 ; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| In-person cultural, sporting, educational or similar activity/admission | Article 54 for B2C, where the activity takes place; Article 53 is the B2B admission provision | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Streamed or otherwise virtually available B2C activity | Article 54 customer location; virtual B2B admission is excluded from Article 53 and requires the applicable rule, normally Article 44 | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Restaurant/catering | Article 55 physical performance, subject to the specific Article 57 rule for qualifying onboard EU passenger-transport services | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Passenger transport | Article 48 transport location, proportionate to distances; national exemptions/rates still require checking | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Other service with no applicable special rule | Article 45 supplier establishment/fixed-establishment rule; a foreign consumer does not by itself remove domestic VAT | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

Article 59 also includes specified rights/licences, obligations to refrain, financial/insurance services, staff, movable-property hire except transport, and energy-network services. Identify the actual category and relevant exclusion; do not limit the article to the professional examples above or treat every service as listed. Member-State Article 59a implementation can change the result where effective use/enjoyment differs. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### EU return mappings: original claims checked separately

| Seller | Treatment of the former field assertion | Source / current limit |
|---|---|---|
| Malta | Former "Box 2 = non-EU supplies" is not confirmed for the current return and registration regime. Do not populate it from this Guide | Not yet confirmed: actual applicable MTCA form/portal field |
| Germany | Ordinary foreign-place services taxable if supplied domestically: 2026 UStVA row 36, KZ 45, excluding items belonging in rows 33-35 and stated domestic exceptions. Do not confuse it with qualifying intra-EU services in row 35/KZ 21 | 2026 official form/instructions https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=7 ; https://www.elster.de/eportal/helpGlobal?themaGlobal=help_ustva_2026 |
| France | Ordinary non-taxable foreign-place services belong in CA3 E2, not the old E1 export-goods shortcut; the notice includes services to a foreign-established customer even if taxed there | 2026 CA3 notice E1/E2, https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf |
| Italy | Former "VE30 field 4 / Esterometro" is not a usable current service-export mapping. Annual IVA 2026 is for tax period 2025: its VE34 covers qualifying outside-territory invoiced transactions. That is 2025-2026 filing-cycle evidence, not the annual form for 2026 transactions | IVA 2026 cover/VE34 instructions, https://www.agenziaentrate.gov.it/portale/documents/20143/9602686/IVA_ANNUALE_2026_istr.pdf/2a42fb92-1b76-229a-d0f5-06069d79b514?t=1768504755711 ; current 2026-transaction annual/e-invoicing fields not yet confirmed |
| Slovakia | Do not use old row 15 for an ordinary service whose place is outside Slovakia: the authority says foreign-place transactions are omitted from the domestic VAT return. Other records/reporting must be assessed separately | Current PFS return instructions, https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/danove-priznanie |

### Step 3: UK seller to a non-UK customer

For services, Northern Ireland uses UK place rules and the Isle of Man is treated as part of the UK VAT territory; establish the actual VAT jurisdiction rather than postal geography. Source: Notice 741A section 2.5, https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a.

The B2B general rule is VATA section 7A(2)(a), **not the former section 7(10) citation**. It places the service where the relevant business recipient belongs, subject to Schedule 4A exceptions. For an ordinary business-use service received by the Australian establishment, do not charge UK VAT; preserve business/location evidence and explain "Outside the scope of UK VAT" as descriptive wording. Sources: https://www.legislation.gov.uk/ukpga/1994/23/section/7A/data.xml; Notice 741A sections 2-4 and 6, https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a.

UK input tax on supplies outside the UK is recoverable subject to the normal rules where the service would be taxable if made in the UK; certain specified exempt supplies have separate relief. Do not promise full recovery of all costs. Source: Notice 741A section 2.7, https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a.

For B2C, apply section 7A(2)(b) unless Schedule 4A changes it. Listed professional/intangible services to a customer belonging outside the UK shift to that customer under Schedule 4A paragraph 16; ordinary unlisted services remain under the supplier rule, subject to the particular performance/property rules. Classify actual IT/consulting rather than the supplier's qualification. Digital/telecoms/broadcasting customer-location rules and the specified use/enjoyment categories need separate checks. The UK use/enjoyment rule is not a universal anti-avoidance test for every service. Sources: https://www.legislation.gov.uk/ukpga/1994/23/schedule/4A/data.xml; Notice 741A sections 6-14, https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a.

For an ordinary outside-UK service by a UK VAT-registered business under standard accounting, include its net value in Box 6 and no output VAT from that supply in Box 1. Confirm any special scheme separately. Source: Notice 700/12 sections 3.2 and 3.7, https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012.

**Post-Brexit correction:** services are outside the Northern Ireland goods arrangement. A UK supplier can still supply Article 44 services for which an EU customer owes VAT under **Article 196**: it applies to a supplier not established in the customer's Member State, including a UK supplier, subject to the establishment/liability conditions. French implementation does not replace or disapply that EU mechanism merely because the supplier is non-EU. The UK seller charges no UK VAT on an ordinary qualifying France-place service; check French recipient liability and invoicing. Sources: Articles 44, 192a and 196, https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; UK Notice 741A section 2.5, https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a.

### Step 4: Australian seller to an overseas customer

Use GST Act section 38-190 for things other than goods or real property; a service performed by the supplier in Australia can qualify. Identify the precise item, the non-resident/recipient, its relevant presence and the actual recipient/beneficiary. An overseas registered address alone does not establish all conditions. Source: https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html.

| Route | Operative test, keeping alternatives distinct | Primary source |
|---|---|---|
| Item 1 | Supply directly connected with goods or real property situated outside the indirect tax zone | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |
| Item 2(a) | Non-resident not in the indirect tax zone when the thing is done; supply is neither work physically performed on goods there nor directly connected with real property there | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |
| Item 2(b), an alternative to item 2(a) | Same non-resident/absence condition; recipient acquires in carrying on its enterprise and is neither GST-registered nor required to be registered | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |
| Item 3 | Recipient not in the indirect tax zone when the thing is done; effective use/enjoyment outside; excludes local goods-work and local real-property connection | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |
| Rights/options, subsection (2) | Relief is excluded for a right/option to acquire something whose supply would be connected with the indirect tax zone and would not be GST-free | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |
| Input-taxed real-property connection, subsection (2A) | Items 2-4 do not relieve an acquisition relating directly/indirectly, wholly/partly, to a supply of local real property input-taxed under the specified residential-property subdivisions | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |
| Local third-party provision, subsection (3) | Item 2 can be denied where the non-resident agreement provides the service to another entity in Australia; apply all statutory exceptions, including the Australian-based business-recipient and specified employee/officer cases | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |
| Item 3 extension, subsections (4)-(5) | Certain agreements with an Australian resident for provision to another entity outside Australia can satisfy the absence limb; listed local international-transport-related services are excluded from this extension | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |

Do not combine items 2 and 3 into one cumulative test. Effective use/enjoyment outside Australia is an item 3 condition, not a universal added condition to every item 2 supply. Conversely, do not disregard subsections (2), (2A) and (3) just because the contract is with a non-resident. Complex presence, third-party provision, rights and mixed supplies require the applicable detailed ruling/country guidance before a final result. Source: https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html.

Input tax credits require a creditable acquisition: business/creditable purpose, a taxable acquisition for consideration, registration/required registration and applicable evidence/limitations. Private/input-taxed use and partly creditable acquisitions can reduce entitlement. GST-free output does not establish full credit for every purchase. Sources: GST Act sections 11-5, 11-15 and 11-20 to 11-30, https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html.

**Reporting correction:** ordinary GST-free remote development/design/consulting is included in G1; under full reporting, it is normally other GST-free sales in G3. G2 excludes GST-free services except the specified repair/renovation/modification/treatment of overseas goods destined outside Australia. Do not put every exported service in G2. Simpler BAS uses the applicable simplified labels rather than requiring G2/G3. Sources: ATO BAS G1-G3 instructions, https://www.ato.gov.au/api/public/content/0-98e0ef06-57b7-4811-a119-5236f1676a3c; reporting-method guidance, https://www.ato.gov.au/api/public/content/0-9fc804ad-a043-4a35-b540-16b71d9ca9bf.

**Original common scenario:** an Australian developer works from Australia for a US company, with the software used in the US. Subject to proving the non-resident/absence facts, no excluded local goods/property connection, and the third-party/exclusion checks above, item 2(a) can give GST-free treatment. Invoice the agreed AUD amount without GST. The supplier's Australian workplace is not itself a failure of the item. Source: https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html.

### Step 5: Indian seller to a non-Indian customer

All 5 IGST section 2(6) conditions (derived count of its enumerated requirements) must hold, not just a foreign customer and an LUT:

| Condition | Required evidence | Primary source |
|---|---|---|
| Supplier | Located in India | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf |
| Recipient | Located outside India, based on the relevant establishment | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf |
| Place of supply | Outside India under section 13 and the applicable current exception | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf ; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Payment | Received in convertible foreign exchange or INR wherever permitted by RBI; monitor the applicable receipt period | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf ; https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf |
| Distinct establishments | Supplier and recipient are not merely establishments of a distinct person under section 8 Explanation 1; a separately incorporated foreign customer is not automatically the same person's establishment | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf ; https://cbic-gst.gov.in/pdf/Circular-No-161-14-2021-GST.pdf |

Section 13(2) normally uses recipient location, with a supplier-location fallback if recipient location is unavailable in the ordinary course. Goods-work/physical-presence services, immovable property, events and the remaining special rules can change the place. The former intermediary-services clause in section 13(8)(b) was **omitted by Finance Act 2026 section 157, from 30 March 2026**; do not apply an older consolidated scan's intermediary supplier-location rule to a current transaction without that overlay. The date follows presidential assent: section 157 has no separate delayed commencement under Finance Act section 1, so General Clauses Act section 5 supplies the assent-date default. Other section 13 conditions still apply; omission alone does not prove every export condition. Sources: https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf; Finance Act commencement/section 157, https://egazette.gov.in/WriteReadData/2026/271439.pdf; General Clauses Act section 5, https://www.indiacode.nic.in/bitstream/123456789/15374/1/the_general_clauses_act%2C_1897.pdf.

| Export route | Conditions / cash-flow consequence | Primary source |
|---|---|---|
| Without payment under bond/LUT | Section 16(3) and rule 96A require the compliant route; use FORM GST RFD-11 before export, subject to permitted condonation. LUT is for its financial year; otherwise an eligible bond route may be required | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf ; https://cbic-gst.gov.in/pdf/Final_Master_circular_LUT_Bond_04102017.pdf ; https://cbic-gst.gov.in/pdf/circularno-40-cgst.pdf |
| With payment and refund | Not a universal alternative available to everyone: section 16(4) requires the currently notified class/conditions and refund procedure. Establish eligibility before paying tax expecting a refund; current notification applicability is not cleared here | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf |
| Input credit / refund | Section 16(2) preserves eligible credit subject to CGST section 17(5); unutilised credit/refunds remain subject to section 54 and applicable rules/evidence. Do not promise FULL refund or adjustment of every domestic cost | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf |

For an eligible exporter with qualifying zero-rated services, the original financial-year LUT recommendation is retained: use a valid LUT for the relevant financial year where its conditions are met, rather than advancing IGST under an eligible tax-paid route and awaiting its refund. This avoids that upfront tax/refund cash-flow cycle; it does not guarantee or accelerate a separate unutilised-input-credit refund. Eligibility, receipt and refund conditions still control. Sources: https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf; https://cbic-gst.gov.in/pdf/Final_Master_circular_LUT_Bond_04102017.pdf; https://cbic-gst.gov.in/pdf/circularno-40-cgst.pdf.

LUT eligibility is subject to Notification 37/2017: the prosecution exclusion involves tax evaded exceeding INR 250 lakh (in words on the page); use the actual facts rather than assume every freelancer qualifies. Circular 8/8/2017 paragraph 2(b) states validity for the financial year; Circular 40/14/2018 updates online RFD-11/ARN acceptance. Current portal guidance selects that financial year. Sources: https://gstcouncil.gov.in/sites/default/files/2024-04/notfctn-37-central-tax-english.pdf; https://cbic-gst.gov.in/pdf/Final_Master_circular_LUT_Bond_04102017.pdf; https://cbic-gst.gov.in/pdf/circularno-40-cgst.pdf; https://tutorial.gst.gov.in/userguide/refund/Furnishing_of_Letter_of_Undertaking.htm.

For services under rule 96A(1)(b), the payment/interest consequence is **15 days after expiry of the later of 1 year from invoice or the FEMA-permitted period including RBI extension**, subject to any further period the Commissioner allows, if permitted-currency payment is not received. These periods are stated in words in the operative amendment (in words on the page). Do not use an unqualified fixed 1-year deadline. Missing/late LUT is not an instruction to assume automatic tax-paid refund: Circular 37/11/2018 paragraph 4 permits case-specific ex post facto condonation. Sources: 12/2024-Central Tax rule 20, https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf; https://cbic-gst.gov.in/pdf/circularno-37-cgst.pdf.

For a registered exporter, reconcile GSTR-1 Table 6A export invoices with GSTR-3B Table 3.1(b) zero-rated outward supplies, including applicable amendments; preserve payment, LUT and refund evidence. Use the period's required INR valuation rather than insert the USD invoice as though it were INR. Current official return FAQ maps these tables: https://tutorial.gst.gov.in/userguide/returns/GSTR3B.htm; the service-valuation rule is CGST Rule 34(2), applied through IGST section 20: https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter4/rule34_v1.00.html; https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf (CGST section 13 concerns time of supply; the IGST section 13 place-of-supply test is separate). No return/payment or refund filing deadline beyond the sourced receipt rule is determined by this Guide.

**Original common scenario:** an Indian developer supplies software development to a US company, paid in USD with LUT filed. It can be a zero-rated export without IGST only after the location/place, separate-establishment and timely permitted-payment conditions are proved and the LUT is valid. Eligible ITC follows its own conditions; payment in USD and LUT alone do not prove all 5 conditions. Sources: https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf; https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf.

### Step 6: Singaporean seller to an overseas customer

The governing route is GST Act **section 21(3) international services**, not a general "Fifth Schedule" catch-all. IRAS explicitly says not every overseas-customer service is zero-rated. The Fifth Schedule of the International Services Order concerns specified telecommunications under section 21(3)(q); it is not the old professional-service Para 1/2/3/10 table. Source: current IRAS international-services table and belonging guidance, https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services.

| Route / original topic | Conditions and corrected reference | Primary source |
|---|---|---|
| General overseas contract, formerly "Para 1" | Section 21(3)(j): contractually supplied to an overseas person outside Singapore when performed; directly benefits an overseas person outside Singapore or a GST-registered person belonging in Singapore; no prohibited Singapore land/goods connection, subject to the section 21(3)(g) goods exception and relevant media-sales provisions | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services |
| Prescribed professional/data services | Section 21(3)(k) and Second Schedule of the International Services Order: overseas contractual person wholly in business capacity; direct beneficiary overseas in business capacity or GST-registered in Singapore; Singapore land-related services are excluded. The exact Singapore-goods/ships limb for professional services versus data services is not cleared by this Guide: see the specific reservation in Sources; do not decide relief for that branch from the combined summary. Unlike (j), the overseas customer can be in Singapore for these qualifying services | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services |
| Goods for export, formerly "Para 2" | The specific section 21(3)(g)/(h) and prescribed conditions/evidence, not every service touching goods. Services directly connected with overseas goods have the separate (f) route | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services |
| International transport, formerly "Para 3" | Apply the relevant section 21(3)(a) transport category/conditions; no generic relief for every transport service | https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services |
| Intellectual-property rights, formerly "Para 10" | Preserve the licensing/IP topic, but do not use that unsupported paragraph mapping. Identify the actual supply/right and applicable current international-services provision before zero-rating; the old category attribution is unconfirmed | Not yet confirmed: exact former Para 10 mapping; no relief cleared merely by this label |

Determine the contractual customer's belonging status, not just its incorporation address. A Singapore business/fixed establishment most directly using the contracted service can change that status. Separately identify direct beneficiaries and their GST registration. A Singapore branch or beneficiary does **not** automatically deny relief: the local GST-registered beneficiary limb can apply if the overseas-contract and other conditions are met. Unregistered local benefit, or a contractual customer actually belonging in Singapore, can produce a different outcome. Source: https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services.

Report qualifying zero-rated international services in **GST return Box 2**. Input GST is deductible only if all applicable conditions hold, including GST registration, business/taxable use, proper invoices/import evidence, attribution, disallowance and fraud checks; mixed exempt/non-business use can restrict recovery. Sources: https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns; https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax.

**Original common scenario:** a Singapore UI/UX designer supplies a UK company. With evidenced overseas contractual/beneficiary status and the relevant section 21(3) conditions, GST can be zero-rated; a foreign invoice address alone does not establish this. Input credit remains conditional and Box 2 applies only to the qualifying supply. Sources: https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services; https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax; https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns.

## Boundary and exception table

| Original exception | Apply this boundary instead of blanket export relief | Source |
|---|---|---|
| Land/immovable property in EU or UK | Property location governs the sufficiently connected service; taxable liability/exemption/rate is a separate step | Article 47 https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 ; Schedule 4A paragraph 1 https://www.legislation.gov.uk/ukpga/1994/23/schedule/4A/data.xml |
| Land/property in AU, India or Singapore | Use the specific country tests: AU item 2 alternatives/exclusions, India section 13(4), SG relevant section 21(3) land exclusion/overseas-land relief. Do not transplant the EU test or assert every domestic land service has the same rate | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html ; https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf ; https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services |
| Event admission/attendance | EU in-person B2B admission Article 53; B2C activities Article 54; distinguish virtual attendance. UK performance/admission rules must be checked separately | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 ; https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a |
| Restaurant/catering | EU Article 55, subject to onboard Article 57; UK physical-performance rule. Overseas customer does not itself confer relief | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 ; https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a |
| Passenger transport | EU distance rule Article 48; UK has specific transport rules; Australian international/domestic transport relief is a separate country-law inquiry, not automatically section 38-190 | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 ; https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a ; https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |
| Goods physically in AU or SG | AU item-specific goods-work exclusions and alternative routes matter; SG local-goods restrictions have specified goods-for-export exceptions. Do not say all local work necessarily fails every relief | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html ; https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services |
| Effective use/enjoyment or local benefit | AU item 3 is not all item 2; UK applies specified categories; EU depends on actual Article 59a implementation; SG uses its particular direct-benefit/belonging tests | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html ; https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a ; https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 ; https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services |
| Other B2C service | EU supplier rule Article 45 applies only after all specific rules are excluded, not solely because the service is absent from Article 59 | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

## Worked cases

The original amounts, countries and scenarios are retained. Each assumes the seller's ordinary registration and no relevant exemption/special scheme unless stated. Establish the additional decisive facts below before using a result; figures are example inputs or derived results, not new thresholds.

### Example 1: Malta IT freelancer to US client, B2B

Remote software development, EUR 5,000 monthly. Assuming the actual US business establishment receives it for business use and no particular-place/use-enjoyment override applies, Article 44 places it in the US. Malta output VAT from this invoice is EUR 0; customer total EUR 5,000. Describe outside scope, not a statutory 0% Malta rate. Deduct qualifying Malta inputs under the conditions above; do not promise full recovery of every cost. The former Malta Box 2 instruction remains unconfirmed and must not be filed from this example. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

### Example 2: German designer to Japanese client, B2B

Branding invoice EUR 3,000, received by the Japanese business establishment. On ordinary Article 44 facts, German output VAT is EUR 0 and invoice total EUR 3,000; 2026 UStVA row 36/KZ 45 applies if the stated non-taxable foreign-place reporting conditions hold. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=7; https://www.elster.de/eportal/helpGlobal?themaGlobal=help_ustva_2026.

### Example 3: UK accountant to Australian client, B2B

Tax advisory invoice GBP 10,000 to the Australian business establishment, with no special rule. Section 7A places it outside the UK; output VAT GBP 0 and total GBP 10,000. Under ordinary VAT accounting put GBP 10,000 in Box 6 and no output tax for this supply in Box 1. Input recovery is conditional. Sources: https://www.legislation.gov.uk/ukpga/1994/23/section/7A/data.xml; https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012; Notice 741A section 2.7, https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a.

### Example 4: Australian developer to Canadian client, B2B

App-development invoice AUD 20,000. Assume the Canadian company is a non-resident outside Australia when the service is done, no local goods-work/property link, and no subsection (2)/(2A)/(3) exclusion. Item 2(a) gives GST-free output, GST AUD 0 and total AUD 20,000. Ordinary service proceeds go in G1 and, for full reporting, G3, not old G2. Sources: https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html; https://www.ato.gov.au/api/public/content/0-98e0ef06-57b7-4811-a119-5236f1676a3c.

### Example 5: Indian developer to UK client, B2B

Development invoice USD 10,000, with LUT filed. Confirm all 5 export conditions, including actual permitted-currency receipt and section 13 place, plus a valid financial-year LUT. On those additional proved facts no IGST is payable under the LUT route; receipt remains USD 10,000 before other contractual deductions. Convert/report the appropriate INR values in the export/zero-rated tables. Eligible ITC/refund is conditional, not FULL by default. Sources: https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf; https://cbic-gst.gov.in/pdf/Final_Master_circular_LUT_Bond_04102017.pdf; https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf; https://tutorial.gst.gov.in/userguide/returns/GSTR3B.htm; https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter4/rule34_v1.00.html.

### Example 6: Singapore consultant to German client, B2B

Management-advisory invoice SGD 15,000. On proved section 21(3)(j) or applicable (k) facts, zero-rated GST is SGD 0 and total SGD 15,000; Box 2 includes SGD 15,000. Do not cite the former "Fifth Schedule Para 1". Sources: https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services; https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns.

### Example 7: French architect, Swiss property

EUR 20,000 design fee for a building to be constructed in Switzerland. A sufficiently connected architectural service falls under Article 47 at the Swiss property, outside French VAT. French output VAT EUR 0; invoice total EUR 20,000 before any Swiss tax. Swiss registration, acquisition tax, exemptions and liability need the Swiss Guide/current law; none is computed here. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

### Example 8: Maltese trainer, 3-day in-person Malta event for a US company

Fee EUR 10,000. If it buys admission to a qualifying educational event in Malta, Article 53 locates the service there. Assuming ordinary taxable training, no exemption/reduced rate and ordinary registration, standard Malta VAT is 18% (in words on the page): derived VAT EUR 1,800 and total EUR 11,800. If the evidenced transaction instead is an ordinary bespoke B2B training service outside the admission rule, Article 44 can place it at the US establishment: output VAT EUR 0, total EUR 10,000. The classification is a legal/factual decision, not a choice of the cheaper answer. Closed attendance, advance registration/payment or the word "bespoke" alone does not resolve it: C-647/17 held a limited multi-day professional course could be admission. Sources: Articles 44/53 https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; Regulation Article 32 https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; judgment https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=ecli%3AECLI%3AEU%3AC%3A2019%3A195; Malta Article 19 https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4.

```oa-check
name: Malta training - admission versus ordinary B2B service, conditional classification
inputs:
  fee: 10000
  malta_standard_rate: 0.18
steps:
  - admission_vat: fee * malta_standard_rate
  - admission_total: fee + admission_vat
  - ordinary_b2b_vat: fee * 0
  - ordinary_b2b_total: fee + ordinary_b2b_vat
  - tax_difference: admission_vat - ordinary_b2b_vat
expected:
  admission_vat: 1800
  admission_total: 11800
  ordinary_b2b_vat: 0
  ordinary_b2b_total: 10000
  tax_difference: 1800
```

### Edge cases: all original situations retained

**EC1: Australian work split across Singapore and Australia.** The consultant spends 2 weeks in Singapore and 4 in Australia for a Singapore company. Duration/location of the supplier's work alone does not decide export relief. Test the actual item 2 non-resident/absence/connection conditions and exclusions; if relying on item 3, test effective use/enjoyment. Local third-party provision needs subsection (3), not an invented universal use test. No IRAS challenge or relief for this Australian supply is inferred merely from the travel. Source: https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html.

**EC2: French yoga instructor and US tourist in Paris.** This is not automatically an Article 59 export. Establish whether the in-person sporting/educational-activity rule in Article 54 or the residual Article 45 applies; both lead to France on the stated French-supplier/Paris facts. If the service is an ordinary taxable, non-exempt standard-rated supply, metropolitan France's standard rate is 20%; franchise/teaching/sports exemptions and any specific relief require the French Guide. The old unconditional "Article 45 and 20%" conclusion is not enough. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; CGI Article 278 rate summary https://www.douane.gouv.fr/fiche/les-taux-de-tva.

**EC3: Indian developer, Dubai client, payment in INR.** INR meets section 2(6)(iv) only where RBI permits it. Obtain the actual transaction's permission/payment evidence; if it is not permitted, export qualification fails. Then determine the applicable tax/place/rate rather than inventing an IGST amount or assuming relief. Observe current rule 96A where exporting without payment. Sources: https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf; https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf.

**EC4: UK web developer to French company post-Brexit.** On ordinary B2B business-use/establishment facts, no UK VAT; French customer liability can arise under Article 196 as implemented in France, even though the supplier is outside the EU. Article 196 is not limited to EU-established suppliers. Sources: https://www.legislation.gov.uk/ukpga/1994/23/section/7A/data.xml; https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

**EC5: Singapore advertising agency, overseas parent with Singapore branch.** Establish which establishment uses the contracted service, the actual overseas contractual person's belonging, direct beneficiary and GST registration, plus the exact advertising category. A branch alone is not automatic denial, and local GST-registered direct benefit can qualify; Singapore-belonging contractual use or an unregistered local direct beneficiary may fail the relevant relief. No "Fifth Schedule" shortcut. Source: IRAS advertising/belonging/(j)/(k) table, https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services.

### Original test suite, corrected expected results

| Test and original input | Expected result and required condition | Source |
|---|---|---|
| Test 1: Malta sole trader, IT consulting to US company, EUR 3,000 | Ordinary Article 44 facts: output VAT EUR 0, total EUR 3,000. Conditional input deduction; former Box 2 = EUR 3,000 is unconfirmed and not a filing instruction | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 ; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| Test 2: French remote data processing to US individual, EUR 1,000 | Article 59 listed service, proved non-EU consumer location/no override: French output VAT EUR 0, total EUR 1,000 | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Test 3: Indian developer to US client, USD 5,000, LUT and USD payment | No IGST only once all export/receipt/LUT conditions are established; eligible ITC conditional; report INR equivalents in GSTR-1 6A / GSTR-3B 3.1(b) | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf ; https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf ; https://tutorial.gst.gov.in/userguide/returns/GSTR3B.htm ; https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter4/rule34_v1.00.html |
| Test 4: Australian designer to UK company, AUD 8,000, client outside Australia | Add the non-resident, goods/property and exclusion evidence: item 2(a) GST-free, output GST AUD 0; G1 and full-reporting G3, not automatic G2 | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html ; https://www.ato.gov.au/api/public/content/0-98e0ef06-57b7-4811-a119-5236f1676a3c |
| Test 5: UK surveyor, UK building, Singapore buyer, GBP 5,000 net | Sufficiently land-related service in UK; assume ordinary taxable standard-rate service: 20% VAT, derived GBP 1,000 tax and GBP 6,000 total, despite foreign buyer | https://www.legislation.gov.uk/ukpga/1994/23/schedule/4A/data.xml ; https://www.gov.uk/vat-rates |

Test 5 recomputes the UK property's location-driven result; it is not a foreign-customer zero-rating case. A general B2B advisory service with a different actual nature would need a separate scope decision, rather than reuse the survey result.

```oa-check
name: UK survey of UK building for Singapore buyer
inputs:
  net_fee: 5000
  standard_vat_rate: 0.20
steps:
  - output_vat: net_fee * standard_vat_rate
  - invoice_total: net_fee + output_vat
expected:
  output_vat: 1000
  invoice_total: 6000
```

## When to refuse or refer

1. **Check place before charging:** never infer domestic tax or export relief from customer geography alone. Use country-specific general and particular rules, not a universal B2B default.
2. **Keep categories and credits separate:** never equate zero-rated, outside scope and exempt, or promise full input recovery automatically. Apply actual credit restrictions and any specific exceptions.
3. **Determine actual reporting:** never omit required returns just because output tax is nil, or invent a box. Slovakia's foreign-place omission and Australia's service/G2 distinction show why reporting is country-specific.
4. **Check all B2C rules:** never assume every foreign consumer receives an outside-scope service, or that Article 59 is the only exception to Article 45.
5. **Check property and relief together:** never zero-rate merely because the buyer is abroad; land location, actual country relief/exemption and rate need checking. The old worldwide absolute prohibition is not a substitute for Australian/other particular statutory routes.
6. **India route and evidence:** never tell an exporter to skip a required LUT/bond, but do not say missing LUT inevitably requires tax payment followed by a guaranteed refund. Check eligibility, permitted late condonation, payment timing and notified paid-route conditions.
7. **Australian item-specific use test:** never impose or disregard effective use/enjoyment without identifying the relevant item, local-beneficiary provision and exclusions. The former blanket no-Australian-use rule is corrected above.

Refer an unknown establishment, classification, local scheme/box, mixed supply, local-beneficiary chain, unproved Indian payment permission, foreign registration or tax-paid refund eligibility. Preserve a clearly supported portion with open items, without presenting a complete cleared export conclusion. The [T1]/[T2]/[T3] labels never override missing evidence.

## Filing and payment

Use the actual registration scheme, period and country return instructions. Keep the legal place/relief decision, contract, location/status/beneficiary evidence, input-tax support, invoice wording and return reconciliation together. No universal export-services filing deadline or late-penalty rate is supplied here; country Guides must supply the actual filing/payment/penalty computation.

Confirmed reporting pointers are the conditional German/French/Slovak directions above, ordinary UK Box 6/no output in Box 1, the Australian reporting-method distinction, Indian export/zero-rated tables, and Singapore Box 2. The Italian evidence is explicitly the 2025-2026 filing cycle; Malta's former field remains unconfirmed. None of these pointers alone clears destination-country registration, reverse charge, income-tax withholding or permanent-establishment risk.

## Completion checklist

- [ ] Actual seller scheme, recipient/status, relevant establishments and service classification established.
- [ ] Country-specific particular rules and actual local use/beneficiary exceptions checked before general relief.
- [ ] Outside scope, zero-rating/GST-free and exempt treatment distinguished; no fictitious 0% rate for an outside-scope EU invoice.
- [ ] Each input-credit claim separately supported; private, exempt and blocked expenditure considered.
- [ ] India currency/receipt and LUT/bond/paid-route eligibility evidenced for the correct financial year.
- [ ] Actual form/period/return values reconciled; all unconfirmed fields and foreign-tax questions held open.
- [ ] Every original scenario/edge/test retained with its necessary corrected conditions; arithmetic checked without changing the legal classification.
- [ ] Draft reviewed for the actual engagement by a qualified professional; source research is not accountant attestation.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

Actual operative reads: 15 November 2026; focused historical-schedule conflict read on 16 November 2026. Read scopes below identify the provisions used, not a claim that every paragraph of a long Act or all destination-country rules was reviewed. Several official copies previously retrieved in this lane were personally read for this rewrite; an unsuccessful fresh request is not described as successful retrieval.

| Official source | Read for actual operative scope and limits | Read on |
|---|---|---|
| https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 | Read for Articles 43-59a, 168-169, 173, 176, 178, 192a, 196, 219a, 226 and 262; current consolidated official XHTML retrieved directly; general/special places, credit and reporting conditions | 2026-11-15 |
| https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 | Read for Articles 18-22, 31a and 32-33a; non-EU status/private use/establishments, sufficient property connection and admission. Ordinary official XHTML retrieval | 2026-11-15 |
| https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=ecli%3AECLI%3AEU%3AC%3A2019%3A195 | Read for paragraphs 18-36 and operative conclusion in the previously saved authentic official parsed judgment; advance registration/payment does not exclude admission. No new successful judgment download claimed | 2026-11-15 |
| https://www.legislation.gov.uk/ukpga/1994/23/section/7A/data.xml | Read for section 7A in official XML, including business/private capacity and Schedule 4A qualification; corrects old section 7(10) reference | 2026-11-15 |
| https://www.legislation.gov.uk/ukpga/1994/23/schedule/4A/data.xml | Read for Schedule 4A land paragraph 1, relevant performance/admission and outside-UK B2C paragraph 16 provisions/conditions; detailed tax liability separate | 2026-11-15 |
| https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | Read for sections 1-4, 6-7, 9-10 and 12-14: evidence/belonging, input recovery, special places and specified use/enjoyment; not every transport relief approved | 2026-11-15 |
| https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012 | Read for sections 3.2/3.7 and normal input conditions; Box 1 output and Box 6 foreign-place services, ordinary accounting | 2026-11-15 |
| https://www.gov.uk/vat-rates | Read for standard 20% rate and distinction from exempt/reduced/zero-rated supplies | 2026-11-15 |
| https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html | Read for section 38-190 table items 1-5 and all subsections (2)-(5); sections 11-5/11-15/11-20 to 11-30 credit conditions; official 2026 compilation and saved copy | 2026-11-15 |
| https://www.ato.gov.au/api/public/content/0-98e0ef06-57b7-4811-a119-5236f1676a3c | Read for G1-G3 operative reporting, G2 exclusion for ordinary GST-free services and specified goods-work exception. Successful official web PDF response; ordinary shell fetch 403 not counted | 2026-11-15 |
| https://www.ato.gov.au/api/public/content/0-9fc804ad-a043-4a35-b540-16b71d9ca9bf | Read for Simpler/full reporting labels and GST-free reporting/input conditions; no turnover threshold introduced here | 2026-11-15 |
| https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf | Read the official-hosted Act scan visually/OCR at sections 2(6), 8 Explanation 1, 13 and 16 including 2023/2024 notes. Older consolidated scan overlaid with enacted 2026 law, not presumed current alone | 2026-11-15 |
| https://egazette.gov.in/WriteReadData/2026/271439.pdf | Read saved authentic Gazette Act, commencement section 1 and operative section 157/neighboring context. Fresh web request timed out and shell certificate validation failed; no bypass, source was the earlier successfully retrieved official PDF | 2026-11-15 |
| https://www.indiacode.nic.in/bitstream/123456789/15374/1/the_general_clauses_act%2C_1897.pdf | Read section 5(1)/(3) and neighboring sections 4-6 in actual official India Code PDF response; default assent-date commencement where no particular date is expressed | 2026-11-15 |
| https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf | Read Notification 12/2024 preamble/commencement and rule 20 at PDF pages 6-7: substituted rule 96A(1)(b) later-period condition; does not rely on withdrawn non-official CGGST copy | 2026-11-15 |
| https://gstcouncil.gov.in/sites/default/files/2024-04/notfctn-37-central-tax-english.pdf | Read whole Notification 37/2017 conditions, prosecution exclusion and financial-year/RFD-11 context | 2026-11-15 |
| https://cbic-gst.gov.in/pdf/Final_Master_circular_LUT_Bond_04102017.pdf | Read Circular 8/8/2017 paragraph 2(a)-(g) and context; financial-year validity; later online modifications applied rather than obsolete paper procedure | 2026-11-15 |
| https://cbic-gst.gov.in/pdf/Circular-No-161-14-2021-GST.pdf | Read Circular 161/17/2021 sections 3-5, separate companies versus branches/establishments; its historical currency extract does not replace current section 2(6) | 2026-11-15 |
| https://cbic-gst.gov.in/pdf/circularno-40-cgst.pdf | Read whole Circular 40/14/2018, online RFD-11/ARN and conditions, replacing specified older circular paragraphs | 2026-11-15 |
| https://tutorial.gst.gov.in/userguide/refund/Furnishing_of_Letter_of_Undertaking.htm | Read actual LUT manual: financial-year selection and RFD-11 submission; no client account or filing performed | 2026-11-15 |
| https://cbic-gst.gov.in/pdf/circularno-37-cgst.pdf | Read paragraphs 4-5/7: case-specific late-LUT condonation and eligibility; old fixed receipt language is superseded by the 2024 rule amendment | 2026-11-15 |
| https://tutorial.gst.gov.in/userguide/returns/GSTR3B.htm | Read current FAQ mappings, system-generated tables 3.1(b) to GSTR-1/1A 6A, nil-return distinction and reconciliation context; no taxpayer return accessed | 2026-11-15 |
| https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter4/rule34_v1.00.html | Actual live active Rule 34(1)–(2) and substitution note read with Rules 33/35 neighbours; services use GAAP exchange rate at CGST section 13 time of supply, incorporated subject to IGST section 20; no actual exchange rate or converted INR value determined | 2026-11-15 |
| https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/charging-gst-%28output-tax%29/when-to-charge-0-gst-%28zero-rate%29/providing-international-services | Read international-services table, including (j)/(k), goods/land/transport/telecom categories, advertising and belonging; primary IRAS guidance. Direct consolidated SSO Act route returned 403; ordinary browser unavailable, so no full SSO read claimed | 2026-11-15 |
| https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/claiming-gst-%28input-tax%29/conditions-for-claiming-input-tax | Read all input conditions, attribution, blocked/non-business expenses and partial-exemption limits; no blanket full credit | 2026-11-15 |
| https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/filing-gst/completing-gst-returns | Read Box 2 and associated qualifying-zero-rated/input/currency context | 2026-11-15 |
| https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/2025-12-29-vordruckmuster-USt-voranmeldung-2026.pdf?__blob=publicationFile&v=7 | Read saved genuine 2026 UStVA form row 36/KZ 45 and instructions, with rows 33-35 exclusions. Fresh web request 503; prior retrieved copy personally read | 2026-11-15 |
| https://www.elster.de/eportal/helpGlobal?themaGlobal=help_ustva_2026 | Read 2026 other non-taxable foreign-place section, exceptions, intra-EU reporting and goods-movement distinction | 2026-11-15 |
| https://www.impots.gouv.fr/sites/default/files/formulaires/3310-ca3-sd/2026/3310-ca3-sd_5426.pdf | Read 2026 CA3 notice E1/E2 and foreign-customer service scope, with filing context | 2026-11-15 |
| https://www.douane.gouv.fr/fiche/les-taux-de-tva | Read metropolitan standard 20% and CGI Article 278 reference; yoga-specific exemption not cleared | 2026-11-15 |
| https://www.agenziaentrate.gov.it/portale/documents/20143/9602686/IVA_ANNUALE_2026_istr.pdf/2a42fb92-1b76-229a-d0f5-06069d79b514?t=1768504755711 | Read saved official annual IVA 2026 cover/tax period 2025 and VE34 with deduction qualifications; 2025-2026 filing cycle only | 2026-11-15 |
| https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/danove-priznanie | Read domestic-return scope and explicit exclusion of transactions with foreign place, neighboring filing/correction context | 2026-11-15 |
| https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 | Read current Cap 406 Article 19 and Eighth Schedule exception, neighboring liability; standard 18% stated in words | 2026-11-15 |
| https://www.iras.gov.sg/media/docs/default-source/uploadedfiles/pdf/list-of-international-services-extract.pdf?sfvrsn=d4781b9c_24 | Historical official excerpt effective 1 January 2020, updated 17 February 2020: Second Schedule paragraphs 1(a)-(b), 2(a)-(b), and neighboring exclusions personally read. Professional paragraph 1(b) includes export goods and ships; data paragraph 2(b) includes export goods only. This is not proof of the current consolidated Order | 2026-11-16 |

Not yet confirmed: Singapore professional-versus-data Singapore-goods/ships conditions under the current Second Schedule: the retained 2020 official reproduction distinguishes professional services (export goods and ships) from data services (export goods only), while the current IRAS table combines the categories. The former combined proposition "professional/data services must not directly relate to Singapore land/goods other than goods for export" is individually unusable for this branch until the current regulatory text/version is reconciled; no ships relief or blanket ships exclusion is cleared here. Malta's former Box 2 mapping for the actual current scheme/return; Italian annual fields for 2026 transactions and the former VE30 field 4/Esterometro instruction; Singapore's former IP "Para 10" mapping; the current notified eligibility/conditions for an Indian tax-paid export refund in an actual case; entity-specific FEMA/RBI permissions/periods; country-specific use/enjoyment implementation, exemptions and registration where not opened here; Swiss or other destination tax/registration amounts; any unlisted foreign filing/payment/penalty deadlines. Former France E1, Slovakia row 15 and blanket Australian G2 instructions are corrected above, not usable alternative boxes. Former unconditional full input recovery, Australian universal-use test and post-Brexit Article 196 exclusion must not be reused.

If you would like a licensed accountant to review your export VAT position, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
