---
name: bahrain-vat
description: Prepare and review Bahrain VAT classification working papers, including bank-statement triage, input recovery, imports, reverse charge, return reconciliation and specialist referrals. Includes dated official form guidance and explicit holds on unconfirmed current portal details.
version: 2.1
jurisdiction: BH
category: international
domain: tax
type: situation-rules
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Bahrain VAT (2026, version 2.1)

## Scope

Use this Guide for Bahrain VAT registration screening, transaction classification and return working papers. It covers resident taxable persons and non-residents liable for Bahrain VAT, domestic sales and purchases, exports, imports, reverse charge, exemptions and input recovery. It produces a documented computation for professional review. It does not authorize portal submission or handle VAT-group consolidation or specialist upstream oil and gas returns. VAT applies to taxable Bahrain supplies, relevant reverse-charge receipts and imports: [VAT Law, arts. 2 and 4](https://lloc.gov.bh/Legislation/HTM/L4818).

The law and Executive Regulations below were read on 16 November 2026, including the enacted rate amendment and its commencement. The accessible NBR General Guide is version 1.14, updated 11 March 2026; the accessible return manual is version 1.2, updated 27 February 2025. Those dated documents do not establish that the current portal is unchanged. See the precise non-usable holds under Sources.

| Quick reference | Rate, amount or condition | Official source |
|---|---|---|
| Standard rate | 10% from 1 January 2022, unless zero-rated or exempt; no general reduced rate in these provisions | [Law 33/2021, arts. 3–5, replacing VAT Law art. 3](https://lloc.gov.bh/Legislation/HTM/K3321) |
| Zero rate | Qualifying supplies under VAT Law art. 53; zero-rated sales retain input recovery subject to ordinary conditions | [VAT Law arts. 42 and 53](https://lloc.gov.bh/Legislation/HTM/L4818) |
| Exemption | Qualifying financial services and real-estate sales/rentals; directly attributable input is generally not recoverable | [VAT Law arts. 42, 54–55](https://lloc.gov.bh/Legislation/HTM/L4818) |
| Mandatory resident registration | Taxable supplies exceed BHD 37,500 in the preceding or expected following 12 months; include the prescribed registration components, not just bank receipts | [VAT Law art. 29](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations arts. 33–34](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218); [dated NBR §3.2.2, numeric threshold](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/TjifwIUNJsy20MvW1ueSYqyColOmV9V8vqxUZIK9.pdf) |
| Non-resident registration | No turnover threshold where the non-resident is liable to pay Bahrain VAT; distinguish customer reverse-charge liability | [VAT Law arts. 4 and 29(c)](https://lloc.gov.bh/Legislation/HTM/L4818) |
| Voluntary registration | BHD 18,750: qualifying supplies or expenses in the previous 12 months reach the threshold, or are expected to exceed it in the next 12 months | [VAT Law art. 33](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 44](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218); [dated NBR §3.2.3, numeric amount](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/TjifwIUNJsy20MvW1ueSYqyColOmV9V8vqxUZIK9.pdf) |
| Ordinary filing frequency | Monthly where declared annual supplies exceed BHD 3,000,000; quarterly otherwise, subject to NBR-assigned or approved different periods | [Regulations art. 48](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218); [dated NBR §13.2, numeric threshold](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/TjifwIUNJsy20MvW1ueSYqyColOmV9V8vqxUZIK9.pdf) |
| Return and payment | Last day of the month following the VAT period; if that day is an official holiday, the deadline extends to the next working day; nil returns remain required | [VAT Law art. 36](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations arts. 49, 63 and 106(c)](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Administration | National Bureau for Revenue (NBR); BHD; electronic return through the [NBR portal](https://www.nbr.gov.bh/) | [Regulations arts. 49–50 and 64](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |

Contributor | Open Accounting Skills Registry

## Ask the client first

Obtain the entity's VAT registration certificate, effective registration date, VAT-group status, assigned return type and period, business activities, actual and forecast taxable supplies, full-period bank statements and transaction register. A statement in CSV, PDF or pasted text from NBB, BBK, Ahli United, BisB, SICO, Al Baraka, Ithmaar or any Bahraini or international bank remains acceptable for initial triage. Obtain sales/purchase invoices, credit notes, contracts, export/customs evidence, prior returns and the reconciled credit carried forward before finalizing the working paper.

For each transaction establish the actual supplier/customer and billing establishment, residency, VAT registration, place and date of supply, goods versus services, invoice currency, whether the amount includes VAT, business use, exempt use and evidence of the claimed relief. Supplier names are investigation leads, not legal classifications. An unexplained bank receipt is not automatically a VAT-exclusive sale. [VAT Law arts. 12–20, 40 and 43](https://lloc.gov.bh/Legislation/HTM/L4818).

**Document policy:** no bank statement or equivalent complete transaction record means stop this bank-led workflow. A bank-only file may produce a provisional list of questions and classifications; it cannot support an unqualified filing-ready return. Retain the warning: “This return was produced from bank statement alone. Reviewer must verify input VAT claims are supported by compliant tax invoices.” Also reconcile invoices and unpaid supplies because the tax point is not simply cash movement. There is no general BHD 50 invoice-evidence exemption. Recovery needs the prescribed evidence regardless of amount; a bank's own statement can qualify for its supplies only if it contains the required bank identity, registration, customer, date, per-supply rate and VAT information. [VAT Law arts. 12–13 and 43](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations arts. 52(i), 53 and 57](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).

Replace the old “conservative defaults” with explicit unresolved fields. Unknown sale rate, purchase VAT status, counterparty country, GCC B2B/B2C status, business-use proportion or blocked-input status means hold the affected classification/recovery and ask for the missing fact. Do not invent domestic status, standard-rated liability or an entitlement to deduct. Record unresolved input VAT separately; a provisional zero recovery is a workflow hold, not a finding that tax is legally blocked.

## The method, step by step

### Registration and tax points [VAT Law arts. 12–13, 29 and 33](https://lloc.gov.bh/Legislation/HTM/L4818)

For mandatory registration include taxable supplies other than capital-asset disposals, deemed supplies, relevant intra-GCC supplies, prescribed related-party aggregation and receipts on which the recipient is liable. Apply the rolling actual/forecast tests. Apply within 30 days after the end of the month in which the actual threshold is exceeded, or 30 days before the month in which it is expected to be exceeded. A liable non-resident applies within 30 days of the first liable supply. [Regulations arts. 33–34 and 36](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).

Ordinarily VAT is due on the earliest of supply, invoice or receipt of consideration, to the extent received. Continuous/periodic contracts have special invoice, due-date and payment rules. Capture advances and unpaid invoices, not only bank statement totals. Invoice issuance is generally due within 15 days after the end of the supply month. Convert foreign currency using the Central Bank of Bahrain approved rate at the tax point; do not treat an unexplained bank conversion as proof of that rate. [VAT Law arts. 12–13, 39–40](https://lloc.gov.bh/Legislation/HTM/L4818).

### Classify the actual supply [VAT Law arts. 3, 53–56](https://lloc.gov.bh/Legislation/HTM/L4818)

| Supply | Treatment and conditions | Official source |
|---|---|---|
| Ordinary Bahrain goods/services | Standard rate unless a specific relief applies; prices, net consideration and VAT must reconcile | [Amended art. 3](https://lloc.gov.bh/Legislation/HTM/K3321); [VAT Law art. 20](https://lloc.gov.bh/Legislation/HTM/L4818) |
| Goods exports and customs-suspension supplies | Zero-rated if actually exported outside Implementing States or supplied to/within a qualifying customs suspension within 90 days, by/on behalf of supplier or customer, without disqualifying intervening use/supply, with commercial, transport and official evidence. A “free zone” address alone is insufficient | [VAT Law art. 53(1)–(2)](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 67](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Exported services | Test non-resident recipient, presence, actual benefit/use and any connection to Bahrain goods, land or special place-of-supply rule. A foreign address alone is insufficient; hold doubtful exported-service relief for specialist review | [VAT Law arts. 17–18 and 53(7)](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 73](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| International transport | Qualifying passenger/goods transport and directly associated supplies, subject to the qualifying means-of-transport and related-service rules | [VAT Law art. 53(3)](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 68](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Local passenger/goods transport | Zero-rated where licensed and qualifying; excludes self-drive hire, sightseeing/recreation, food delivery by the food supplier and specified ancillary transport. It is not generally exempt | [VAT Law art. 53(13)](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 78](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Healthcare, medicines and equipment | Qualifying basic/preventive medical services by qualified licensed providers, and approved medicines/equipment; cosmetic treatment is excluded unless part of prescribed medical treatment | [VAT Law art. 53(4)–(5)](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations arts. 69–71](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Education | Qualifying licensed nursery through higher education and prescribed connected supplies; professional training is not generally included, and uniforms, meals, stationery and recreational trips are not automatically zero-rated | [VAT Law art. 53(12)](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 77](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Specified basic food | Only the specified list and conditions; restaurant, café and catering supplies are excluded from this food relief | [VAT Law art. 53(15)](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 80](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| New buildings | Qualifying construction services and incorporated goods can be zero-rated, including commercial/industrial construction. Demolition, architect/interior-design fees, refurbishment and removable furnishings do not qualify merely because linked to a new building | [VAT Law art. 53(11)](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 76](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Oil and gas | Specific sector supplies can be zero-rated; downstream products such as plastics/fertilizers are excluded. Refer upstream operations under R-BH-2 | [VAT Law art. 53(14)](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 79](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Financial services | Margin/interest remuneration is generally exempt; explicit service fees/commissions are generally taxable. Securities transfers and life insurance have specific exemptions regardless of consideration form. Do not exempt ordinary financial-advisory fees | [VAT Law art. 54](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 81](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Real estate | Bare land/building sales and rentals are generally exempt, including residential and commercial property. Hotels, short parking, non-exclusive serviced offices, function halls and separately charged services have exceptions | [VAT Law art. 55](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 82](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Exempt imports | Check the statutory exemption, including goods whose domestic supply would qualify for exemption/zero rate and specified diplomatic, military, returned goods and personal imports. Customs-duty exemption alone is insufficient | [VAT Law art. 56](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 83](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |

### Supplier pattern library: investigation, then evidence [VAT Law arts. 2, 4, 9 and 54](https://lloc.gov.bh/Legislation/HTM/L4818)

Match case-insensitive substrings to request the underlying document. If none match, apply the supply rules above. Do not assign a rate or exclusion from the name alone.

| Patterns retained | Required investigation and resulting classification | Official source |
|---|---|---|
| NBB; NATIONAL BANK OF BAHRAIN; BBK; BANK OF BAHRAIN AND KUWAIT; AHLI UNITED; AUB; BISB; AL SALAM BANK; AL BARAKA; ITHMAAR | Separate explicit bank service charges from exempt interest/margin. An explicit taxable fee can carry recoverable VAT where used for taxable business; do not exclude every charge | [VAT Law art. 54](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations arts. 52(i) and 81](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| INTEREST; LOAN; REPAYMENT | Split principal/capital movements, exempt financing consideration and any taxable fee. “Financial” does not make every component outside scope | [VAT Law arts. 2 and 54](https://lloc.gov.bh/Legislation/HTM/L4818) |
| NBR; NATIONAL BUREAU FOR REVENUE; LMRA; LABOUR MARKET; SIO; SOCIAL INSURANCE; MOIC; MINISTRY OF INDUSTRY; TAMKEEN | Identify genuine tax, levy, contribution or grant versus payment for a supply. Government economic activity can be taxable; a public-sector counterparty is not a blanket exemption | [VAT Law arts. 2 and 9](https://lloc.gov.bh/Legislation/HTM/L4818) |
| CUSTOMS; BAHRAIN CUSTOMS | Separate customs duty and import VAT; claim only evidenced eligible VAT in the client's capacity as importer | [VAT Law arts. 21 and 43](https://lloc.gov.bh/Legislation/HTM/L4818) |
| EWA; ELECTRICITY AND WATER; BATELCO; STC BAHRAIN; ZAIN BAHRAIN | Ordinary domestic utilities/telecom are standard-rated where supplied in Bahrain. Inspect actual invoice, supply and recipient, including separately charged property utilities | [VAT Law arts. 15 and 18](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 82](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| GOOGLE; MICROSOFT; ADOBE; META; AWS; AMAZON WEB SERVICES; ZOOM; SLACK; NOTION; ANTHROPIC; OPENAI | Check actual billing establishment and Bahrain place of supply. A non-resident taxable supply to a liable Bahrain recipient can require reverse charge; brand or USD billing does not establish residency | [VAT Law arts. 4(2), 17–18](https://lloc.gov.bh/Legislation/HTM/L4818) |
| SOLIDARITY; AXA BAHRAIN; GIG BAHRAIN | Life insurance/reinsurance is exempt; ordinary general insurance is generally standard-rated. Read the policy and fees | [Regulations art. 81](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218); [NBR General Guide §6.4.3](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/TjifwIUNJsy20MvW1ueSYqyColOmV9V8vqxUZIK9.pdf) |
| SALARY; WAGES; PAYROLL; GOSI; SOCIAL INSURANCE ORGANIZATION; OWN TRANSFER; INTERNAL; DIVIDEND | Reconcile genuine employee remuneration, statutory contributions, own-account transfers and investment distributions separately from consideration for a business supply. Agency/payroll service charges and recharges require their own analysis | [VAT Law arts. 2 and 8](https://lloc.gov.bh/Legislation/HTM/L4818) |

### Reverse charge and goods imports [VAT Law arts. 4, 17–21 and 42–43](https://lloc.gov.bh/Legislation/HTM/L4818)

For a taxable service supplied in Bahrain by a non-resident to a liable Bahrain taxable recipient, self-account for output VAT at the applicable rate and separately determine input recovery. Digital services are tested by Bahrain use/enjoyment. No VAT shown on a foreign invoice is not an exemption. A fully taxable business with compliant evidence may have equal output/input, while an exempt or partly exempt recipient can owe net VAT. Keep both entries even where they net to zero. Record the BHD VAT on the foreign supplier invoice as required by [Regulations art. 52(c)](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).

Goods imports are ordinarily taxed through Customs. The base is customs value plus excise, customs duty and other charges, excluding VAT, rather than merely the bank payment. Check exemption and customs-suspension conditions. Approved import deferral is reported as due and potentially deductible in the relevant return; do not confuse it with ordinary imported-service reverse charge. [VAT Law arts. 21, 51–52 and 56](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations arts. 22 and 65](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).

**GCC transition:** NBR General Guide 1.14 expressly says Bahrain recognizes no other GCC state as an Implementing State until further notice. Thus its dated instruction covers Saudi Arabia, UAE, Oman, Kuwait and Qatar alike; another country's introduction of VAT does not by itself activate Bahrain intra-GCC treatment. Under that confirmed position, goods moving from Bahrain to Oman or Qatar are tested as exports and incoming GCC goods as ordinary imports, with relief/documentation conditions. Services still follow their own place-of-supply/export rules. Confirmation of any subsequent NBR recognition announcement is held, so do not use this dated status as an unqualified current filing instruction. [NBR General Guide introduction and §20.4](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/TjifwIUNJsy20MvW1ueSYqyColOmV9V8vqxUZIK9.pdf).

### Input recovery, blocked costs and partial exemption [VAT Law arts. 42–46](https://lloc.gov.bh/Legislation/HTM/L4818)

Recover only VAT attributable to taxable business supplies, including qualifying zero-rated supplies, and qualifying overseas supplies that would confer recovery if made in Bahrain. Directly exempt, private/nonbusiness and prohibited-use inputs do not qualify. Keep compliant original invoices or customs/importer evidence and reconcile the actual recipient. Full invoices require supplier registration, parties, dates, sequential number, supply, net BHD values, rate/VAT and gross total. Simplified invoices are permitted for an unregistered customer or consideration not exceeding BHD 500, with the prescribed minimum fields; this is not an input-recovery exemption from documentation. [Regulations arts. 52–53 and 57](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).

| Cost | Recovery decision | Official source |
|---|---|---|
| Client entertainment, hospitality, accommodation, meals/drinks outside ordinary business provision; entertainment events/trips | Block the input VAT covered by these rules. A hotel name alone does not prove entertainment | [Regulations art. 58(a)](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Personal-use goods/services, including free employee benefits | Generally blocked, subject to statutory requirements for the benefit and the precise rule | [Regulations art. 58(a)(3)](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Employee/director vehicle and related repairs, insurance or maintenance | Recover only established business-use portion under applicable conditions; private use is blocked. Rental, emergency, licensed taxi/bus and inherently business vehicles have specified exceptions | [Regulations art. 58(b)–(c)](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Recreational club membership | Assess personal/recreational use under the entertainment/nonbusiness rules; no automatic deduction | [VAT Law art. 42(c)](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 58](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| Missing compliant evidence | Hold recovery pending evidence; distinguish missing proof from a permanently blocked cost | [VAT Law art. 43](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 57](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |

First directly attribute inputs to supplies that do or do not confer recovery. Apply the standard proportion only to genuinely common residual VAT: value of supplies conferring recovery divided by the value of all relevant supplies, multiplied by residual input VAT. Exclude capital-asset supplies, incidental supplies outside the main activity, supplies through an overseas establishment and outside-scope transactions from the ratio as prescribed. Round the percentage to the nearest one decimal place. Recalculate annually and adjust in the last period of that year or first period of the next. NBR approval is needed for an alternative method, not for using the ordinary statutory method. Refer if attribution, exclusions or method are unresolved. [Regulations art. 59](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).

Credit notes require the supplier's output and recipient's previously deducted input to be adjusted with correcting evidence. Distinguish a later change to the transaction, such as returned goods, from discovery of incorrect invoicing: Regulations art. 32 uses the period of the adjustment event, while art. 54 addresses the period in which an overcharge or undercharge is discovered. Do not automatically use a delayed credit-note issue date. [VAT Law arts. 28, 41, 46 and 48](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations arts. 32 and 54](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).

### Return reconciliation and dated form routing [Regulations arts. 49–50](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218)

Build a working paper with taxable values, output VAT, credit/debit adjustments, imports paid at Customs, deferred imports, imported-service reverse charge, local purchases, blocked/apportioned input, prior corrections and credit brought forward. Calculate output liability less allowable input, then apply permitted corrections/credits. Reconcile the portal calculation to this schedule and retain receipt and payment evidence. Never overwrite a disagreement to force agreement.

The following is a **dated form reference**, not confirmation of the 2026 live form. The actual image on printed page 21 of [NBR return manual 1.2, updated 27 February 2025](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf) shows these fields. Its prose on page 14 still calls net VAT line 17, contradicting the image. Confirm the assigned form's labels before mapping; the simplified return is a separate form and this numbering must not be imposed on it.

| Dated image line | Field and working-paper destination | Official source |
|---|---|---|
| 1(a) | Standard-rated domestic sales; historical-rate subfields appear only where applicable | [Manual §8.1, p. 21 image](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf#page=23) |
| 2 | Sales to registered VAT payers in other GCC states; do not activate solely because foreign registration exists | [Manual p. 21 image](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf#page=23) |
| 3 | Sales subject to domestic reverse charge; verify actual approval and scope | [Manual p. 21 image](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf#page=23) |
| 4–7 | Zero-rated domestic sales; exports; exempt sales; total sales, respectively | [Manual p. 21 image](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf#page=23) |
| 8(a)–10 | Domestic standard purchases; imports with VAT paid at Customs; imports with Customs deferral, respectively | [Manual p. 21 image](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf#page=23) |
| 11(a)–12 | Imports accounted for under reverse charge; domestic reverse-charge purchases, respectively. Record output liability and eligible input separately in the schedule | [Manual p. 21 image](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf#page=23) |
| 13–15 | Non-registered/zero-rated/exempt purchases; total purchases; total VAT due for current period, respectively | [Manual p. 21 image](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf#page=23) |
| 16–19 | Previous-period corrections; credit carried forward; net VAT due/reclaimed; late-payment penalty, respectively. Do not treat a correction field as unrestricted permission to move prior errors | [Manual p. 21 image](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf#page=23) |

Do not use the predecessor's invented separate output-VAT box formulas. Adjustments/apportionment are columns against relevant supplies in the actual image, not the predecessor's standalone boxes. The full predecessor mapping remains explicitly non-usable under Sources for traceability. Domestic reverse-charge approval is a separate regime under [Regulations art. 66](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218), not a blanket treatment of all domestic purchases.

## Boundary and exception table

| Situation | Resolution and boundary | Official source |
|---|---|---|
| EC1: AWS from a US provider, no VAT invoice charge | Verify non-resident supplier and taxable Bahrain receipt; account for reverse charge and eligible input. Net nil only with full recovery | [VAT Law arts. 4, 18 and 42–43](https://lloc.gov.bh/Legislation/HTM/L4818) |
| EC2: manufacturer exports goods to Oman | Under the dated confirmed GCC position, export relief needs actual movement and documentation; recovery follows taxable use, not destination alone | [Regulations art. 67](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218); [NBR §1.2.3](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/TjifwIUNJsy20MvW1ueSYqyColOmV9V8vqxUZIK9.pdf) |
| EC3: sedan for director | Private-use VAT blocked; establish any qualifying business portion and applicable vehicle conditions | [Regulations art. 58(b)–(c)](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| EC4: goods sold to Qatar | Same export evidence and current recognition check; no blanket relief from a Qatar customer name | [Regulations art. 67](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218); [NBR §1.2.3](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/TjifwIUNJsy20MvW1ueSYqyColOmV9V8vqxUZIK9.pdf) |
| EC5: developer sells new apartment within 3 years | The original 3-year/first-sale zero rate is rejected. Sale is generally exempt, while qualifying construction is a different zero-rated supply; related exempt-sale input is not automatically recoverable | [VAT Law arts. 42, 53(11), 55](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations arts. 76 and 82](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| EC6: bank interest | Generally exempt financing income; directly related input is not recoverable | [VAT Law arts. 42 and 54](https://lloc.gov.bh/Legislation/HTM/L4818) |
| EC7: consulting plus “financial advisory” | Advisory fees are not exempt merely because financial. Partial exemption arises only if the actual other supplies are exempt; then attribute/apportion | [VAT Law art. 54](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations arts. 59 and 81](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |
| EC8: credit note for returned goods | Supplier adjusts output and buyer previously recovered input, using legal event/period and correcting evidence | [VAT Law arts. 28, 41, 46, 48](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 32](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) |

## Worked cases

These are conditional computations in BHD, not assertions that bank narratives establish the facts. Round VAT to the nearest fils where needed under [Regulations art. 55](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218), corroborated by [NBR General Guide §10.9.2](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/TjifwIUNJsy20MvW1ueSYqyColOmV9V8vqxUZIK9.pdf). The applicable standard rate is set by [Law 33/2021 art. 3](https://lloc.gov.bh/Legislation/HTM/K3321); value/recovery rules are [VAT Law arts. 20 and 42–43](https://lloc.gov.bh/Legislation/HTM/L4818).

### Original example 1: non-resident SaaS

Input unchanged: `05.01.2026 ; NOTION LABS INC ; DEBIT ; Monthly plan ; USD 16.00 ; BHD 6.03`.

Assume the invoice establishes a non-resident supplier, no Bahrain VAT charged, Bahrain taxable recipient/use, and a VAT-exclusive BHD tax-point value of 6.030 supported by the required exchange-rate evidence. Do not infer these from the brand. Output reverse-charge VAT is 0.603; allowable input is 0.603 only for fully taxable business use with evidence, giving net nil. The predecessor's 0.60 was a two-decimal display, not the complete fils amount. Route to imported reverse-charge purchases on the assigned form, with both tax legs reconciled; dated image line 11(a), not old separate boxes 10 and 14. [VAT Law arts. 4, 18, 40, 42–43](https://lloc.gov.bh/Legislation/HTM/L4818); [dated manual image](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf#page=23).

```oa-check
name: Original Notion USD16, supported BHD6.03 value
inputs:
  usd_invoice: 16
  bhd_base: 6.03
  rate: 0.10
  recoverable_fraction: 1
steps:
  output_vat: round(bhd_base * rate, 3)
  input_vat: output_vat * recoverable_fraction
  net_vat: output_vat - input_vat
expected:
  output_vat: 0.603
  input_vat: 0.603
  net_vat: 0
tolerance: 0.0001
```

### Original example 2: domestic sale

Input unchanged: `10.01.2026 ; AL JAZEERA TRADING ; CREDIT ; Invoice 2026-001 ; +5,000.00 ; BHD`.

The original result assumes an invoice **net** price of 5,000, giving output VAT 500 and gross consideration 5,500. Reconcile why only 5,000 was received. If instead 5,000 is the complete VAT-inclusive price, output VAT is 454.545 and net 4,545.455. Hold the choice until the invoice/payment allocation resolves it. Route qualifying standard sales to the corresponding field, dated image line 1(a). [VAT Law art. 20](https://lloc.gov.bh/Legislation/HTM/L4818); [dated manual image](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf#page=23).

```oa-check
name: Original Al Jazeera BHD5000 net versus inclusive
inputs:
  stated_amount: 5000
  rate: 0.10
steps:
  vat_if_net: stated_amount * rate
  gross_if_net: stated_amount + vat_if_net
  vat_if_inclusive: round(stated_amount * rate / (1 + rate), 3)
  net_if_inclusive: stated_amount - vat_if_inclusive
expected:
  vat_if_net: 500
  gross_if_net: 5500
  vat_if_inclusive: 454.545
  net_if_inclusive: 4545.455
tolerance: 0.0001
```

### Original example 3: client entertainment

Input unchanged: `15.01.2026 ; GULF HOTEL BAHRAIN ; DEBIT ; Client dinner ; -250.00 ; BHD`.

Assume the whole 250 gross is standard-rated client entertainment supported by an invoice. Embedded VAT is 22.727, net invoice value 227.273 and VAT recovery nil. The expense remains 250 including irrecoverable VAT; the predecessor's “net 250” described that cost, not a VAT-exclusive invoice base. Other levies or mixed charges would require invoice-level separation. The correct block is [Regulations art. 58(a)](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218), not the unsupported predecessor reference to Order 14/2019.

```oa-check
name: Original Gulf Hotel BHD250 gross dinner
inputs:
  gross: 250
  rate: 0.10
  recovery_fraction: 0
steps:
  embedded_vat: round(gross * rate / (1 + rate), 3)
  invoice_net: gross - embedded_vat
  input_recovery: embedded_vat * recovery_fraction
  expense: invoice_net + embedded_vat - input_recovery
expected:
  embedded_vat: 22.727
  invoice_net: 227.273
  input_recovery: 0
  expense: 250
tolerance: 0.0001
```

### All original test-suite inputs

The six original cases are a domestic goods sale, a local supplies purchase, IT services from a UK firm with no VAT charged, a goods export, a client dinner, and bank interest income. The following preserve their original inputs. Assume registration and valid evidence; purchases serve wholly taxable business unless expressly blocked/exempt. Export relief needs the conditions above. These assumptions are necessary for the original expected results. [VAT Law arts. 3, 4, 42–43, 53–54](https://lloc.gov.bh/Legislation/HTM/L4818), with [rate amendment](https://lloc.gov.bh/Legislation/HTM/K3321) and [Regulations arts. 58 and 67](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).

```oa-check
name: Original six Bahrain VAT tests
inputs:
  standard_sale_net: 10000
  purchase_net: 5000
  invoiced_purchase_vat: 500
  uk_it_services: 2000
  export_goods: 50000
  dinner_net: 300
  dinner_vat: 30
  bank_interest: 100000
  standard_rate: 0.10
  export_rate: 0
  blocked_recovery: 0
steps:
  test1_output: standard_sale_net * standard_rate
  test2_input: min(invoiced_purchase_vat, purchase_net * standard_rate)
  test3_output: uk_it_services * standard_rate
  test3_input: test3_output
  test3_net: test3_output - test3_input
  test4_output: export_goods * export_rate
  test5_input: dinner_vat * blocked_recovery
  test5_gross: dinner_net + dinner_vat
  test6_output: bank_interest * 0
  test6_direct_input_fraction: 0 * bank_interest
expected:
  test1_output: 1000
  test2_input: 500
  test3_output: 200
  test3_input: 200
  test3_net: 0
  test4_output: 0
  test5_input: 0
  test5_gross: 330
  test6_output: 0
  test6_direct_input_fraction: 0
```

The exempt-interest test computes no output VAT; its zero multiplier represents exemption, not a zero-rated taxable sale. Related input remains non-deductible. Imported-service output must still be declared where recovery is unavailable.

## When to refuse or refer

- **R-BH-1, VAT group:** stop single-entity consolidation if the client is a group member. Transactions between members of the same registered group are not supplies for VAT; obtain the group certificate and refer group consolidation to the licensed adviser. [VAT Law art. 30](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations art. 38](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).
- **R-BH-2, upstream oil and gas:** refer sector treatment to a specialist. The relevant zero-rate provision is VAT Law art. 53(14), with detailed scope/exclusions in Regulations art. 79, not the predecessor's art. 68. [Law](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).
- **R-BH-3, unresolved partial exemption:** refer where attribution, residual allocation or an alternative method cannot be established. Ordinary statutory apportionment does not itself require an NBR-agreed method; alternative methods do require approval. [Regulations art. 59](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).
- Stop a claimed exemption, export relief, recovery or form mapping dependent on a genuinely missing fact/source. Present the transaction, issue, evidence, alternative treatments, recommended resolution and required professional action. Preserve the **REVIEWER FLAG / Tier: T2** workflow for ambiguity and **ESCALATION REQUIRED / Tier: T3 / Do not classify. Refer to licensed tax advisor** for matters outside scope. These are workflow flags, not professional approval labels.

Direct tax, payroll/social insurance and excise are outside this VAT job. Route corporate-tax questions to [bh-corporate-income-tax](bh-corporate-income-tax.md), personal tax to [bh-income-tax](bh-income-tax.md), social insurance/payroll to [bh-payroll-social](bh-payroll-social.md), and excise to an appropriate current specialist source. Do not use the predecessor's unsupported rates reproduced as non-usable history under Sources.

## Filing and payment

Use the taxpayer's assigned period rather than presuming every small business is quarterly. NBR may modify periods and a taxpayer may obtain monthly filing approval. Reconcile all transactions and prior credit before the end-of-next-month deadline. If the last day is an official holiday, Regulations art. 106(c) extends the deadline to the next working day. File nil returns when registered even without activity. [VAT Law art. 36](https://lloc.gov.bh/Legislation/HTM/L4818); [Regulations arts. 48–50, 63 and 106(c)](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218).

For an error in a filed return, the statutory amended-return deadline is 30 days from awareness, before NBR inspection/audit. Regulations art. 51 permits an error producing net VAT due below BHD 5,000 to be corrected through the period following the original return; it does not permit any later-period adjustment merely because the error is small. Distinguish a commercial credit-note adjustment from a taxpayer error. [Regulations art. 51](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218); [NBR General Guide §13.3.4](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/TjifwIUNJsy20MvW1ueSYqyColOmV9V8vqxUZIK9.pdf).

The dated [NBR manual §§3–7 and FAQ9.4](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf) describes login, VAT, VAT Returns, the unfiled obligation, taxpayer/period review, draft, supporting information, declaration and submission receipt. Only the taxpayer or duly authorized representative submits. Preserve the electronic receipt and reconcile the bill/payment, credit offset and any refund request. General portal operations and available payment channels require current confirmation because the live site could not be read. Excess refundable VAT can be carried forward on request and NBR may offset tax/fines: [VAT Law arts. 57–58](https://lloc.gov.bh/Legislation/HTM/L4818).

### Penalties and interest [VAT Law arts. 60, 63–64](https://lloc.gov.bh/Legislation/HTM/L4818)

These are the statutory provisions read, not a computation of a particular assessment. Obtain the notice, dates and legal basis; refer possible evasion to a Bahrain professional.

| Breach | Statutory consequence and boundary | Official source |
|---|---|---|
| Late filing or payment, delay not exceeding 60 days | Administrative fine 5%–25% of VAT that should have been declared/paid; not a fixed monthly charge or BHD minimum | [VAT Law art. 60(a)(1)](https://lloc.gov.bh/Legislation/HTM/L4818) |
| Registration failure within the statutory 60-day period described in the provision | Fine up to BHD 10,000; the law does not impose the predecessor's BHD 5,000 minimum | [VAT Law art. 60(a)(2)](https://lloc.gov.bh/Legislation/HTM/L4818) |
| Incorrect import/supply data understating value | Fine 2.5%–5% of unpaid VAT per month or part of a month unpaid | [VAT Law art. 60(a)(3)](https://lloc.gov.bh/Legislation/HTM/L4818) |
| Listed procedural breaches | Up to BHD 5,000; includes information, inspection and invoicing failures; VAT itself remains collectible | [VAT Law art. 60(b)–(c)](https://lloc.gov.bh/Legislation/HTM/L4818) |
| Tax evasion as defined by the law | Imprisonment 3–5 years and fine 1–3 times VAT; repeat-offence and legal-person rules differ. Delay categories refer to further periods after those in art. 60, not every late return automatically | [VAT Law arts. 63–64](https://lloc.gov.bh/Legislation/HTM/L4818) |

## Completion checklist

Confirm registration, period and form; reconcile banks to invoices, advances and unpaid supplies; substantiate zero rates/exemptions; review every foreign service and goods import; separate explicit bank fees from financing; document business use and blocked input; compute standard/special apportionment correctly; reconcile credit notes, prior corrections and credits; recompute the working paper independently of portal totals; preserve professional flags, receipts and supporting evidence. Never invent a rate from a counterparty name, ignore reverse charge because its net is nil, or claim blocked VAT. Historical adjustments may relate to an earlier rate, so the old prohibition on any rate other than the current standard/zero is unsafe. Use the calculation engine with reviewed inputs, and reconcile its output; do not prohibit the arithmetic needed to validate the return. [VAT Law arts. 4, 12, 36, 41–46](https://lloc.gov.bh/Legislation/HTM/L4818); [Law 33/2021 arts. 4–5](https://lloc.gov.bh/Legislation/HTM/K3321).

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions or outcomes arising from its use. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

**General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Sources

| Official source | Actual read date and scope |
|---|---|
| [Decree-Law 48/2018 issuing the VAT Law](https://lloc.gov.bh/Legislation/HTM/L4818) | 2026-11-16. Read for this guide: issuing commencement; definitions and arts. 2–4, 8–9, 12–24, 28–30, 33, 35–46, 48, 51–60, 63–64, 75–76 and neighboring clauses relevant to these rules. Original art. 3 is superseded by the amendment below; do not read the old rate alone as current |
| [Law 33/2021](https://lloc.gov.bh/Legislation/HTM/K3321) | 2026-11-16. Read for this guide: entire enacted amendment, arts. 1–6, including replacement standard rate, contract transition and January commencement |
| [Executive Regulations, Resolution 12/2018](https://www.lloc.gov.bh/Legislation/HTM/RFNE1218) | 2026-11-16. Read for this guide: relevant definitions and arts. 2, 7–9, 22–28, 32–39, 44, 48–59, 63–69, 71–73, 76–83, 104–106 and neighboring conditions. References here are to the cached Arabic operative provisions, not a statement that every article was reviewed |
| [NBR General Guide 1.14, updated 11 March 2026](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/TjifwIUNJsy20MvW1ueSYqyColOmV9V8vqxUZIK9.pdf) | 2026-11-16. Read for this guide: cover, introduction/GCC transitional recognition, §§3.2.2–3.2.3 registration thresholds and conditions, §§6.3–6.4 categories, 10.4 and 10.9–10.10 invoices/rounding, 11.5–11.6 recovery/apportionment, 13.2–13.3 periods/returns/amendments and 20.4 Implementing States. This is the actual accessible edition, not a claim that it is the latest edition |
| [NBR return filing/payments/refunds manual 1.2, updated 27 February 2025](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/SM6HsC9Nlqk6YnJqk3OJq5nT5FRorlhSbAzAEDa8.pdf) | 2026-11-16. Read for this guide: cover; §§1–7 procedure/payment/credit, §8.1 actual form images on printed p. 21, FAQs9.1–9.8. Image read visually, not inferred from missing PDF text. Prose line17 conflicts with image line18 for net VAT |
| [NBR simplified return manual, January 2022, version 1.0](https://nbrproduserdata-ir.s3.eu-west-1.amazonaws.com/media/F41AhMDZ30ln3TMHSGja3jbMZCjYsYLVhL0ibyef.pdf) | 2026-11-16. Read for this guide: cover and §§1–2 identifying a separate simplified return and tax-rate questions; no assertion of current eligibility or complete field mapping |

**Not yet confirmed:** current NBR website/portal screens, tooltips, simplified-return eligibility/numbering, payment-channel availability and any later GCC recognition notice. The official website returned 403 through direct access and an ordinary browser. Later General Guide version content was not obtained; no later-edition claim is based on a search snippet. The live form must resolve the dated manual's prose/image inconsistency. The predecessor's driving-instruction and dealer-stock vehicle exceptions also lack confirmation as standalone exceptions in the provisions read; establish ordinary taxable-business recovery and the actual vehicle conditions, or refer. These items are non-usable for final field selection or an unqualified current filing instruction until confirmed from accessible official authority. Underlying law-supported working papers can still be prepared.

**Non-usable predecessor form history:** old boxes 1 standard sales; 2 GCC sales; 3 domestic zero; 4 exports; 5 exempt; 6 total sales; 7 output VAT computed from old1+2; 8 output adjustment; 9 goods import VAT; 10 services output; 11 total output as old7+8+9+10; 12 local purchases; 13 goods imports; 14 services input; 15 total input; 16 blocked/input adjustment; 17 allowable input as old15−16; 18 net as old11−17; 19 carried credit; 20 payable/refundable as old18−19. This entire old mapping is rejected as a filing instruction and retained only to make the correction traceable. Use the dated image and current-form confirmation above, never these old numbers/formulas.

**Non-usable predecessor claims:** the old BHD 50 invoice cutoff, new-residential-property first-sale relief within 3 years, blanket GCC implementation assumptions, all-bank-fees exemption, universal NBR-approved partial-exemption requirement and old penalties have been corrected in their corresponding sections. Old out-of-scope direct-tax claims “CIT 0%/no CIT”, “PIT none”, social insurance employer/employee 12%/7% for Bahraini and 3%/1% for non-Bahraini, and excise tobacco/energy/carbonated-drinks 100%/100%/50% are unverified for this VAT assignment and must not be used. Their destination is the relevant owner/specialist, not a VAT conclusion. No accountant approval or named-author credit is added or removed by this update.
