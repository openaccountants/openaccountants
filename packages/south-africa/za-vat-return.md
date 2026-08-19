---
name: za-vat-return
description: Use this skill whenever asked about South African VAT returns for self-employed individuals or small businesses. Trigger on phrases like "South Africa VAT", "VAT201", "SARS VAT", "15% VAT", "eFiling VAT", "zero-rated SA", "VAT vendor", or any question about VAT filing, computation, or registration for vendors in South Africa. Covers the 15% standard rate, zero-rated and exempt supplies, R2.3M registration threshold, VAT201 return, and bimonthly filing via SARS eFiling. ALWAYS read this skill before touching any South African VAT work.
version: 2.1
jurisdiction: ZA
tax_year: 2026
last_updated: 2026-07-13
reviewed_by: Werner Britz
review_status: current
depends_on:
  - vat-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ZA VAT Return

## South Africa VAT Return (VAT201) -- Self-Employed Skill v2.1

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by Werner Britz on 2026-06-12. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified `skill_facts` — edit the facts, not the prose.

### VAT (za-vat-return)

- **Country** — South Africa
- **Tax** — Value-Added Tax (VAT) at 15%  _(VAT Act s 7(1)(a); SARS media release 25 April 2025)_
- **Currency** — ZAR only  _(VAT Act s 20(4); SARS VAT 404 Guide)_
- **Primary legislation** — Value-Added Tax Act 89 of 1991 (VAT Act)
- **Supporting legislation** — Tax Administration Act 28 of 2011 (TAA); SARS interpretation notes
- **Tax authority** — South African Revenue Service (SARS)
- **Filing portal** — SARS eFiling (efiling.sars.gov.za)
- **Default filing frequency** — Bimonthly (Category A)  _(VAT Act s 27(2))_
- **Filing deadline** — Last business day of month following period end (eFiling)  _(VAT Act s 28; SARS VAT 404 Guide)_

Editorial only. After this validation review the "Pending" status should be updated.

- **15% Standard rate** — 15% - Standard rate (effective 1 April 2018)  _(VAT Act s 7(1)(a))_
- **0% Zero-rated list** — List is correct as far as it goes but incomplete. Other zero-rated items under s 11: supply of an enterprise as a going concern; certain services to non-residents; gold supplied to the SARB or a bank; illuminating paraffin; certain government grants; certain agricultural inputs (fertiliser, seeds, dipping etc); deemed supplies of certain second-hand goods exported.  _(VAT Act s 11; Schedule 2)_
- **Exempt list** — Broadly correct. Tighten: "financial services" is narrow (interest, dividends, life insurance, currency exchange MARGIN, dealing in securities - all fee-based items are standard-rated under the proviso to s 2(1)). Add: donated goods/services supplied by associations not for gain; supply of accommodation in a "dwelling" (long-term); the implicit margin in currency exchange.  _(VAT Act s 12 and s 2(1) with proviso)_
- **Tax fraction** — For VAT-inclusive amounts at 15%: 15/115  _(VAT Act s 1, definition of "tax fraction")_
- **Compulsory registration** — From 1 April 2026, R2,300,000 in any consecutive 12-month period. Announced Budget Speech 25 February 2026. Unchanged for 17 years before this. Application within 21 business days of exceeding or reasonably expecting to exceed.  _(VAT Act s 23; SARS Register for VAT page; SARS Budget 2026 FAQ; CDH alert 19 March 2026)_
- **Voluntary registration** — From 1 April 2026, R120,000.  _(VAT Act s 23(3); SARS Register for VAT page; SARS Budget 2026 FAQ)_
- **Payments basis eligibility** — R2.5m threshold applies only to NATURAL PERSONS. Full s 15(2) list: public authorities; water boards; municipal entities; municipalities; associations not for gain; foreign suppliers of electronic services; SABC Ltd; natural persons under R2.5m. Companies, CCs, and trusts outside the listed categories cannot use payments basis at any turnover level.  _(VAT Act s 15(2); SARS VAT Connect Issue 10 (March 2020))_
- **Full tax invoice threshold** — R5,000  _(VAT Act s 20(4) and (5); SARS Tax Invoices page)_
- **No invoice required** — "R50 or less" rather than "under R50". A till slip or sales docket is still required to support an input tax claim. For supplies between R50 and R5,000, an abridged invoice is acceptable.  _(VAT Act s 20(6))_
- **Registration status unknown** — STOP - do not compute  _(VAT Act s 7 and s 23)_
- **Accounting basis unknown** — Invoice basis (default)  _(VAT Act s 15(1))_
- **Supply classification unknown** — Standard-rated at 15%
- **Private use proportion unknown** — 0% recovery  _(VAT Act s 17(1))_
- **Second-hand goods claim** — Not claimable until documentation confirmed  _(VAT Act s 16(3)(a)(ii); SARS VAT264 form (modernised 2023))_
- **Minimum viable** — Bank statement for the VAT period in CSV, PDF, or pasted text, plus confirmation of VAT registration status and vendor number
- **Recommended** — Sales invoices, purchase invoices with VAT shown, prior period VAT201  _(VAT Act s 16(2) and s 20)_
- **Ideal** — Complete invoice register, filing category confirmation, prior year VAT reconciliation
- **R-ZA-1: Below threshold** — Threshold should be R2,300,000 from 1 April 2026. Also update the voluntary registration test to R120,000.  _(VAT Act s 23)_
- **R-ZA-2: Cross-border services** — Complex cross-border service transactions and customs VAT require specialist review. Escalate.
- **R-ZA-3: VAT grouping** — SA does not have a true "VAT group" registration in the UK sense. The closest equivalent is the branch registration under s 50 (separate enterprises of one vendor) and s 23(2A) single branch registration for foreign groups. Reword as "branch and divisional registrations outside scope".  _(VAT Act s 50 and s 23(2A))_
- **R-ZA-4: Large complex transactions** — Transactions involving property, construction, or financial instruments require specialist review. Escalate.
- **EFT FROM [client] / EFT CREDIT** — Taxable supply / Output VAT at 15% / Standard electronic transfer
- **INSTANT MONEY / CASH DEPOSIT** — Taxable supply / Revenue / Cash receipt
- **PAYFAST PAYOUT / PAYFAST SETTLEMENT** — Taxable supply / Revenue / PayFast payment gateway  _(VAT Act s 7(1)(a) and s 2(1) with proviso)_
- **YOCO SETTLEMENT / YOCO PAYOUT** — Taxable supply / Revenue
- **SNAPSCAN PAYOUT** — Taxable supply / Revenue
- **ZAPPER SETTLEMENT** — Taxable supply / Revenue
- **CAPITEC / FNB / ABSA / NEDBANK / STD BANK CREDIT** — CORRECT in principle, but bank credit alone is not a VAT classifier. The CHARACTER of the receipt matters: same bank credit could be a taxable supply (revenue), an exempt supply (rent of dwelling), a loan drawdown (out of scope), or a refund (no VAT). Treat as "potential taxable supply, investigate".
- **INTEREST / INT EARNED** — Exempt / NOT taxable / Bank interest - financial service  _(VAT Act s 12(a) and s 2(1)(f))_
- **SARS REFUND** — EXCLUDE / Not income / Tax refund
- **LOAN DRAWDOWN** — EXCLUDE / Not income / Loan proceeds
- **MISSING: Exports for foreign currency** — Add pattern: foreign currency credit (SWIFT/EFT) where services exported or goods exported. Zero-rated under s 11(1)(a) for goods (subject to documentary requirements per Export Regulation) or s 11(2)(l) for services to a non-resident not physically present in SA at the time. Most common gap for SA service businesses with foreign clients.  _(VAT Act s 11; Export Regulation GN R316)_
- **MISSING: Insurance proceeds** — Insurance indemnity payments are deemed taxable supplies under s 8(8) where the underlying insured asset/expense was used in making taxable supplies. Common reviewer trap.  _(VAT Act s 8(8))_
- **MISSING: Fringe benefits (output VAT)** — Where the vendor employs staff and grants any Seventh Schedule fringe benefit (private use of company car, low-interest loans, free or cheap services, assets given at less than market value, residential accommodation, etc), s 18(3) deems a taxable supply by the employer. Output VAT is payable on the cash equivalent of the benefit per the Seventh Schedule (s 10(13)) in the month the benefit accrues (s 9(7)). Exclusions: exempt supplies, zero-rated supplies, entertainment, and benefits granted in the course of an exempt activity.  _(VAT Act s 18(3) read with s 9(7) and s 10(13); Income Tax Act Seventh Schedule; KPMG TNF September 2019)_
- **OFFICE RENT / COMMERCIAL LEASE** — Only claimable where the landlord is VAT-registered AND issues a VAT tax invoice. Common pitfall: smaller landlords (especially individual landlords) are below the VAT threshold and do not charge VAT, in which case the rent is OUT OF SCOPE and no input is claimable. Residential letting is exempt regardless. Skill should say "claimable IF landlord issues VAT invoice".  _(VAT Act s 16(2) and s 20)_
- **ESKOM / CITY POWER / CITY OF CAPE TOWN** — Utilities / Input VAT claimable / Electricity  _(VAT Act s 7)_
- **TELKOM / VODACOM / MTN / CELL C / RAIN** — Communications / Business portion claimable / Mixed use: apportion
- **ENGEN / SHELL / CALTEX / SASOL** — Fuel (petrol and diesel) is ZERO-RATED in SA under s 11(1)(h) read with Schedule 2 Part A. There is NO VAT on the fuel component itself. What IS standard-rated and where input may be claimed: lubricants, oils, car-wash, shop purchases at a fuel station, vehicle accessories. The pump price includes the fuel levy and RAF levy but no VAT. Telling clients to claim "input VAT on fuel" is a common error that triggers a SARS query.  _(VAT Act s 11(1)(h); Schedule 2 Part A)_
- **TAKEALOT / MAKRO / GAME** — Office supplies / Input VAT claimable / Business purchases
- **GOOGLE ADS / META / LINKEDIN** — Treatment depends on the contracting entity. Google Ads SA, Meta SA, LinkedIn SA bill SA VAT and input is claimable normally. Where billed from a foreign entity (e.g. Google Ireland), this is an imported service under s 7(1)(c): the SA vendor must self-assess output VAT and may claim corresponding input where used for taxable supplies (net zero for fully taxable). Most SA businesses are now billed by the local SA entity since the electronic services regulations.  _(VAT Act s 7(1)(c) and s 14; Foreign Suppliers of Electronic Services Regulations)_
- **UBER SA / BOLT SA / TAXI** — Uber/Bolt operate on an AGENCY model: the platform invoices the rider in the name of the driver as the driver's agent for the fare. The driver is the actual supplier of the road transport service. Under s 12(g) of the VAT Act, "the supply by any person of a service comprising the transport in a vehicle operated by him of fare-paying passengers and their personal effects by road" is EXEMPT. So even a VAT-registered Uber driver could not charge VAT on the fare. Uber's own SA tax page for drivers confirms: "the transportation services provided by you to riders is exempt from VAT in South Africa". Three separate supplies in the chain: (1) Driver -> Rider for the fare: EXEMPT (s 12(g)). No VAT, no input claim for a business rider. (2) Uber/Bolt -> Driver for service fee and commission: STANDARD-RATED at 15%. Driver may claim input if registered (most are not). (3) Uber -> Rider for booking fee (small separate line): STANDARD-RATED at 15%. A VAT-registered business rider can claim input on this fragment with a valid Uber tax invoice. Note: Uber registered as a SA VAT vendor from May 2019; Bolt similarly. TAXI (metered cab): generally not VAT-registered, and the same s 12(g) exemption applies to the fare itself. Practical: for a business client using Uber/Bolt, the FARE is not claimable as input VAT. Only the booking fee fragment (if separately shown on the Uber tax invoice) may be claimed. Most invoices do not separate this cleanly, so the practical answer is "no input on Uber/Bolt in most cases".  _(VAT Act s 12(g) and s 54 (agent and principal); Uber South Africa "Tax Information for Driver-Partners" page; SARS BGR 16 (Issue 4) on apportionment; SARS VAT Quick Reference Guide. The agency point is anchored in s 54 of the VAT Act: where a person acts as agent, the supply is deemed made by the principal.)_
- **SARS INCOME TAX / SARS PAYE** — EXCLUDE / Tax payment / Not deductible
- **SARS VAT PAYMENT** — EXCLUDE / VAT payment / Not input tax
- **BANK CHARGES / FNB FEE / ABSA FEE** — Bank service fees are STANDARD-RATED at 15% and INPUT IS CLAIMABLE for vendors. Proviso to s 2(1) deems fee-based activities NOT to be financial services. SA banks issue monthly VAT tax invoices (downloadable from online banking). Exempt items are interest charged/earned and the implicit currency exchange margin. See critical finding #3.  _(VAT Act s 2(1) proviso; SARS VAT News 7 (August 1996); PwC SA Tax Summary)_
- **OWN TRANSFER / PERSONAL** — Correct for sole proprietors and partnerships. For companies and CCs, transfers to shareholders or directors require investigation: may be salary, dividend, loan, or fringe benefit (s 18(3)). Treat as "investigate" for non-individual vendors.
- **MISSING: Motor cars and rentals** — Critical omission. Input tax on the supply of a "motor car" is BLOCKED under s 17(2)(c). "Motor car" is defined in s 1: includes motor car, station wagon, minibus, double cab light delivery vehicle, and any other vehicle on public roads, 3+ wheels, constructed or converted wholly or mainly for the carriage of passengers. Excludes: vehicles carrying only 1 person or more than 16 persons; vehicles over 3,500kg unladen mass; caravans, ambulances, hearses (with conditions), game-viewing vehicles. Test is OBJECTIVE (passenger area vs loading area) per IN 82. Input BLOCKED on: purchase, finance lease (instalment credit), operating lease, and CAR RENTAL (e.g. Avis, Europcar, Hertz, Bidvest Car Rental) of motor cars. Input CLAIMABLE on: running costs (fuel, insurance, repairs, maintenance) for business use, even on a blocked motor car, because these are not "supply of a motor car". Exceptions where input on the motor car itself is claimable: vendor regularly sells or rents motor cars in the ordinary course of business (motor dealer, car rental company); vehicle is a stock-in-trade demonstrator. Bakkies (single cab) used exclusively for goods transport are not "motor cars".  _(VAT Act s 1 (definition) and s 17(2)(c); SARS Interpretation Note 82; RTCC v CSARS Tax Court VAT 1345 (2016))_
- **MISSING: Entertainment** — Input tax on entertainment, accommodation, food, and beverages is BLOCKED under s 17(2)(a). "Entertainment" includes meals, beverages, social functions, prizes, hampers, recreation, corporate gifts, golf days, year-end functions, etc. Exceptions (input claimable): (i) where the vendor is in the business of supplying entertainment (restaurants, hotels, conference venues); (ii) where entertainment is supplied to an employee or office holder who is away from usual place of work on business (employee subsistence); (iii) employee canteen supplies for charge; (iv) bona fide promotional gifts to customers (subject to conditions). The VAT block applies even where income tax allows the deduction.  _(VAT Act s 17(2)(a); SARS BGR 16 and IN 70)_
- **MISSING: Insurance premiums** — Short-term insurance premiums (asset cover, business interruption, public liability, fleet) are STANDARD-RATED and input is claimable where the underlying asset/activity is used for taxable supplies. Insurer issues VAT tax invoice. Long-term life insurance is exempt under s 2(1)(i). Pay-outs are deemed taxable supplies under s 8(8) where the underlying was used for taxable supplies.  _(VAT Act s 7, s 8(8), s 12(a) read with s 2(1)(i))_
- **EXPORT / INTERNATIONAL SHIPMENT** — Correct in principle, but zero-rating of exports requires strict documentary evidence under the Export Regulation (GN R316, 2 May 2014). For direct exports (vendor responsible for delivery overseas) the documents are different to indirect exports (foreign purchaser collects in SA). Without the prescribed documents, the supply must be standard-rated. Skill should flag this.  _(VAT Act s 11(1)(a); Export Regulation GN R316)_
- **BROWN BREAD / MAIZE MEAL / RICE / EGGS / MILK** — Zero-rated / Basic foodstuffs  _(VAT Act s 11(1)(j); Schedule 2 Part B)_
- **FUEL LEVY / PETROL / DIESEL** — Zero-rated / Fuel levy applies instead  _(VAT Act s 11(1)(h); Schedule 2 Part A)_
- **MISSING: Going concern** — Important zero-rating: sale of an enterprise (or part) as a going concern to another vendor is zero-rated under s 11(1)(e), provided: both parties are vendors; the parties agree in writing that the supply is of a going concern; the enterprise is an income-earning activity at the effective date; the assets needed to carry on are supplied; and the parties agree it is zero-rated. Significant trap if not handled correctly: SARS will recharacterise as standard-rated.  _(VAT Act s 11(1)(e))_
- **Example 1: Standard Bimonthly Return** — The arithmetic assumes the R500,000 and R200,000 figures are VAT-EXCLUSIVE. Bank statements show VAT-INCLUSIVE amounts. The example should be explicit on this and ideally show both. If R500,000 was the VAT-inclusive sales receipt, output VAT = R500,000 x 15/115 = R65,217.
- **Example 2: Exporter in Refund Position** — Correct arithmetically. Add: a refund position invariably triggers a SARS VAT verification or audit and the vendor must hold the prescribed export documents per the Export Regulation. SARS will withhold the refund until verified. Flag for reviewer.  _(VAT Act s 11; Export Regulation GN R316; TAA s 190)_
- **Example 3: Second-Hand Goods Purchase** — Calculation correct. Add: claimable in the period the goods are acquired AND paid for; capped at lesser of consideration paid or open market value; requires VAT264 declaration (modernised 2023) plus proof of identity of seller and proof of payment. For acquisitions of "fixed property" the rules differ - notional input is limited to transfer duty actually paid.  _(VAT Act s 16(3)(a)(ii) and s 16(3)(b); SARS VAT264)_
- **Example 4: Bad Debt Relief** — Invoice for R23,000 (incl. VAT) written off after 14 months. Relief: R23,000 x 15/115 = R3,000.  _(VAT Act s 22(1) and s 22(2))_
- **Field 1 / 1A** — On the actual VAT201: Field 1 is standard-rated supplies excluding capital goods. Field 1A is standard-rated supplies of capital goods. The VAT amounts are NOT in Fields 1 and 1A; they are in Fields 4 and 4A (computed as Field 1 x 15/115 and Field 1A x 15/115 respectively).  _(SARS, "Guide to Completing the Value-Added Tax (VAT201) Return")_
- **Field 2** — Split required: Field 2 (zero-rated supplies excluding exports) and Field 2A (zero rate, only exported goods).  _(SARS VAT201 completion guide)_
- **Field 3** — Exempt supplies  _(SARS VAT201 completion guide)_
- **Field 4** — Field 4 is output VAT on Field 1 (Field 1 x 15/115), not total supplies. There is no aggregate-supplies line on the form.  _(SARS VAT201 completion guide)_
- **Field 5 / 5A** — Field 5 is the VAT-exclusive value of commercial accommodation supplied for more than 28 days. Capital goods purchased (input) is Field 14, with imported capital goods at Field 14A.  _(SARS VAT201 completion guide)_
- **Field 6 / 6A** — Field 6 = Field 5 x 60% (deemed taxable portion of long-stay commercial accommodation). Other purchases (input) is Field 15, with imported other goods at Field 15A.  _(SARS VAT201 completion guide)_
- **Field 7** — Field 7 (with Field 8 as the aggregate of Fields 6 and 7) handles commercial accommodation. Total input tax is Field 19 (sum of Fields 14+14A+15+15A+16+17+18).  _(SARS VAT201 completion guide)_
- **Field 8** — Field 8 is the sum of Fields 6 and 7 (commercial accommodation). Total output tax is Field 13 (sum of 4+4A+9+11+12). Net VAT payable/refundable is Field 20.  _(SARS VAT201 completion guide)_
- **Field 9** — Field 9 is output VAT on commercial accommodation (Field 8 x 15%). Net VAT payable/refundable is Field 20.  _(SARS VAT201 completion guide)_
- **MISSING: Output adjustments fields (10, 11, 12)** — Field 10 (VAT-incl value) and Field 11 (Field 10 x 15/115): change in use and export of second-hand goods previously notional-input. Field 12: other and imported services - this is where output VAT on imported services under s 7(1)(c) is declared.  _(SARS VAT201 completion guide)_
- **MISSING: Input fields (14-19)** — Field 14: capital goods purchased (VAT amount). Field 14A: imported capital goods (VAT amount). Field 15: other goods/services purchased (VAT amount). Field 15A: imported other goods/services (VAT amount). Field 16: change in use (adjustment). Field 17: bad debts (s 22 relief). Field 18: other. Field 19: total input (sum of 14+14A+15+15A+16+17+18).  _(SARS VAT201 completion guide)_
- **MISSING: Diesel refund (fields 21-38)** — For qualifying vendors (mining, farming, electricity generation, rail, foreign-going ships, offshore) the VAT201 includes a diesel refund schedule. Out of scope for a generic skill but worth noting as a "see specialist" item.  _(Customs and Excise Act Sch 6 Part 3; VAT Act s 75)_
- **Category A: Bimonthly** — Default for most vendors  _(VAT Act s 27(2))_
- **Category B: Monthly** — Taxable supplies > R30M/year  _(VAT Act s 27(3))_
- **Category C: Six-monthly** — Farming enterprises (by approval)  _(VAT Act s 27(4))_
- **Category D: Annual** — Category D is for connected-party-only farming or rental enterprises (annual). Sub-categories E (annual, certain connected-party rental) and F (four-monthly, micro businesses on turnover tax) exist but are not mentioned.  _(VAT Act s 27(4A) to (5))_
- **eFiling deadline** — Last business day of month following period end  _(VAT Act s 28; SARS VAT 404 Guide)_
- **Manual (branch) deadline** — 25th of month following period end  _(VAT Act s 28)_
- **Payments basis criteria** — R2.5m applies to natural persons only. Other eligible categories: public authorities, water boards, municipalities and municipal entities, associations not for gain, SABC, foreign electronic services suppliers. Application via VAT-Reg-02 process; SARS issues a directive on approval (not a Binding Private Ruling).  _(VAT Act s 15(2); SARS VAT Connect Issue 10)_
- **Late filing** — For VAT, the main penalty for late submission is the percentage-based penalty under s 213 TAA (10% of the tax due). Fixed-amount administrative penalties under s 210 also apply but the escalating-scale fixed amounts that the skill describes (R250-R16,000) are more characteristic of personal income tax administrative penalties. SARS does also impose understatement penalties under s 222-224 for understatements.  _(TAA s 210, s 213, s 222-224)_
- **Late payment** — 10% of amount outstanding  _(TAA s 213)_
- **Interest** — Current rate is 10.25% p.a. from 2 March 2026 on late or underpayment of VAT. Interest compounds monthly. Reference the SARS interest rate page rather than hardcoding.  _(TAA s 187; SARS Interest Rates page; SARS Budget 2026 Tax Guide)_
- **Understatement** — 10-200% depending on behaviour  _(TAA s 222 to s 224; Schedule to TAA Chapter 16)_
- **6.1 Mixed Supplies Apportionment** — The "revenue-based ratio" is the SARS standard turnover-based method (STM) per BGR 16. Alternative methods (transaction-count, headcount, floor area) require a ruling application under s 41B. The STM is computed as taxable supplies / total supplies, excluding certain items (directors fees, fixed property sales over R100k, capital items, etc). 5% de minimis rule under s 17(1) proviso: if exempt is under 5% of total, claim 100%.  _(VAT Act s 17(1); BGR 16; CSARS v African Bank Ltd [2025] ZASCA 101)_
- **6.2 Imported Services (Reverse Charge, s 7(1)(c))** — Substantively correct but the trigger needs tightening: imported service is a service supplied by a non-resident, OR by a resident from outside SA, to a recipient who is a resident, for utilisation otherwise than for making taxable supplies. The "self-assess" works for FULLY taxable recipients (output = input, net zero). For partially exempt recipients, the output is fully payable but input is apportioned - so there IS a real cost. For non-vendors (e.g. an individual buying foreign digital subscriptions in personal capacity), output is payable via VAT215 within 30 days. The latter is widely ignored in practice but technically required.  _(VAT Act s 7(1)(c) and s 14; SARS Form VAT215)_
- **6.3 Second-Hand Goods Input Tax** — Notional input tax: tax fraction (15/115) of consideration paid. Requires declaration from seller and proof of payment. Cannot exceed lesser of consideration paid or open market value. Flag for reviewer.  _(VAT Act s 16(3)(a)(ii) and s 16(3)(b); SARS VAT264 form)_
- **6.4 Change from Payments to Invoice Basis** — When turnover exceeds R2,500,000. Transitional adjustments required. Flag for tax practitioner.  _(VAT Act s 15(4) and (5))_
- **MISSING: Motor cars and motor expenses** — See expense pattern row above and critical finding #4. Section should address: (a) is the vehicle a "motor car" as defined (objective test - passenger area vs loading area); (b) is the supply within an exception (vendor sells/rents motor cars, demonstration vehicle, etc); (c) running costs ARE claimable even on blocked motor cars; (d) acquisition via rental, finance lease, or operating lease - all blocked; (e) accessories invoiced separately may be claimable.  _(VAT Act s 1, s 17(2)(c); SARS IN 82)_
- **MISSING: Entertainment (2)** — See expense pattern above. Tier 2 question: is the vendor in the business of providing entertainment? Default: blocked. Sub-cases: subsistence for employees away from usual place of work (claimable); employee canteen for charge (claimable subject to cap); promotional gifts subject to BGR conditions.  _(VAT Act s 17(2)(a); BGR 16)_
- **MISSING: Fringe benefits (deemed output VAT)** — Section 18(3) deems Seventh Schedule fringe benefits granted by VAT-registered employers as taxable supplies. Output VAT payable on cash equivalent. Common items: company car (3.5% of determined value / 3.25% if maintenance plan); right of use of an asset; subsidies; low- or no-interest loans; assets given for less than market value; free or cheap services.  _(VAT Act s 18(3), s 9(7), s 10(13); Income Tax Act Seventh Schedule)_
- **MISSING: Tax invoice compliance detail** — Single most common reason SARS disallows input. FULL TAX INVOICE (supplies > R5,000 incl VAT) under s 20(4) requires: (a) words "Tax Invoice", "VAT Invoice", or "Invoice"; (b) supplier name, address, VAT number; (c) recipient name, address, AND recipient VAT number where recipient is a vendor; (d) serial number and date of issue; (e) description of goods/services (mention "second-hand goods" if applicable); (f) quantity or volume of goods/services; (g) value of supply, amount of VAT, and consideration (or consideration plus statement that VAT is included). ABRIDGED TAX INVOICE (R50-R5,000 incl VAT) under s 20(5) requires items (a), (b), (d), (e), and (g); does NOT require recipient details (item c) or quantity (item f). Must be issued within 21 days of the supply.  _(VAT Act s 20(4) and (5); SARS Tax Invoices page)_
- **Template structure** — Conceptually sound but field references in Section A and B do not match the VAT201. Rebuild with the correct field numbers (see Section 5.1 above). Add: prior period credit carry-forward, output adjustments (change in use, exports of second-hand goods), input adjustments (bad debts, change in use), imported services line.  _(SARS VAT201 completion guide)_
- **Bank formats table** — FNB, ABSA, Standard Bank, Nedbank, Capitec, Investec column structures
- **EFT CREDIT / INWARD PAYMENT** — Bank transfer in / Potential income
- **DEBIT ORDER / DEBICHECK** — Direct debit / Regular expense
- **POS / CARD PURCHASE** — Point of sale / Expense
- **CASH DEPOSIT** — Cash received / Income
- **SARS / RECEIVER OF REVENUE** — Tax payment or refund / Exclude
- **BANK CHARGES / SERVICE FEE** — Bank service fees are STANDARD-RATED at 15% in SA. See critical finding #3. Input is claimable with the monthly VAT tax invoice from the bank.  _(VAT Act s 2(1) proviso; SARS VAT News 7 (1996))_
- **Question 1 (VAT registration)** — Are you registered as a VAT vendor? What is your VAT number?
- **Question 2 (Filing category)** — Add E and F to the list (see Section 5.2 above).  _(VAT Act s 27)_
- **Question 3 (Accounting basis)** — Are you on invoice basis or payments basis?
- **Question 4 (Supply types)** — What types of goods or services do you sell?
- **Question 5 (Zero-rated supplies)** — Do you make any zero-rated supplies (exports, basic foodstuffs)?
- **Question 6 (Exempt supplies)** — Important question but should add: "Do you have any mixed-use input (used for both taxable and exempt)?" This is the trigger for s 17(1) apportionment.  _(VAT Act s 17(1))_
- **Question 7 (Second-hand goods)** — Do you purchase second-hand goods from non-vendors?
- **Question 8 (Imported services)** — Do you import services from non-resident suppliers?
- **MISSING: Motor vehicle question** — Add: "Do you have any motor cars (including double cabs, station wagons, SUVs, minibuses) used in the business? Have you claimed input tax on the purchase, lease, or rental of any vehicle?" This would catch the s 17(2)(c) block.  _(VAT Act s 17(2)(c))_
- **MISSING: Fringe benefits question** — Add: "Do you employ staff and grant any fringe benefits (company car, low-interest loans, assets at less than market value, free or cheap services, accommodation)?" This triggers s 18(3) output VAT.  _(VAT Act s 18(3))_
- **MISSING: Entertainment question** — Add: "Do you incur entertainment, meals, accommodation, or social functions for clients or staff?" Triggers s 17(2)(a) block analysis.  _(VAT Act s 17(2)(a))_
- **Key legislation list** — VAT Act sections 7, 11, 12, 23, 15, 16, 20, 22, 27, 28  _(VAT Act)_
- **Known gaps / out of scope** — Cross-border services; customs VAT on imports; VAT grouping; large-value property transactions  _(VAT Act)_

After this validation, version 2.1 changelog should record: corrected R2.3m registration threshold; corrected bank charges and payment processor fees to standard-rated; corrected VAT201 field structure; added motor car block; added s 18(3) fringe benefits; added tax invoice compliance requirements.

- **Never claim input on exempt supplies** — Only taxable (including zero-rated) supplies qualify  _(VAT Act s 17(1))_
- **Never charge VAT if not registered** — CORRECT  _(VAT Act s 7 and s 23)_
- **Never use a rate other than 15%** — For standard-rated supplies  _(VAT Act s 7(1)(a))_
- **Never confuse zero-rated with exempt** — Input tax claimable on zero-rated; not on exempt  _(VAT Act s 11 vs s 12)_
- **Never claim input without a valid tax invoice** — For supplies over R50  _(VAT Act s 16(2) and s 20)_
- **Never ignore the bimonthly filing deadline** — Penalties apply from first day late  _(VAT Act s 28; TAA s 213)_
- **Never apply payments basis without SARS approval** —   _(VAT Act s 15(2))_
- **Never claim notional input on second-hand goods without documentation** —   _(VAT Act s 16(3)(a)(ii); VAT264)_

Always label as estimated; direct to SARS-registered tax practitioner

- **MISSING prohibition: motor cars** — Add: "Never claim input on the supply (purchase, lease, rental) of a motor car as defined, unless within an exception under s 17(2)(c)."  _(VAT Act s 17(2)(c))_
- **MISSING prohibition: entertainment** — Add: "Never claim input on entertainment, accommodation, or food and beverages, unless the vendor is in the business of providing entertainment or the supply is to an employee away from usual place of work."  _(VAT Act s 17(2)(a))_
- **MISSING prohibition: fringe benefits** — Add: "Never omit output VAT on Seventh Schedule fringe benefits granted to employees under s 18(3)."  _(VAT Act s 18(3))_

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | South Africa |
| Tax | Value-Added Tax (VAT) at 15% |
| Currency | ZAR only |
| Primary legislation | Value-Added Tax Act 89 of 1991 (VAT Act) |
| Supporting legislation | Tax Administration Act 28 of 2011 (TAA); SARS interpretation notes |
| Tax authority | South African Revenue Service (SARS) |
| Filing portal | SARS eFiling (efiling.sars.gov.za) |
| Default filing frequency | Bimonthly (Category A) |
| Filing deadline | Last business day of month following period end (eFiling) |
| Contributor | Open Accountants Community |
| Validated by | Werner Britz CA(SA), Spurwing CFO |
| Validation date | May 2026 |
| Skill version | 2.1 |

### Rate Table

**Rate Table**

| Rate | Application |
| --- | --- |
| 15% | Standard rate (effective 1 April 2018) |
| 0% | Exports, basic foodstuffs, petrol/diesel, international transport, agricultural inputs, going concern (s 11(1)(e)), gold to SARB/bank, illuminating paraffin |
| Exempt | Financial services, residential rental, public transport, educational services, childcare |

### Tax Fraction

- **Tax fraction** — For VAT-inclusive amounts at 15%: 15/115.

### Key Thresholds

**Key Thresholds table**

| Item | Amount (ZAR) |
| --- | --- |
| Compulsory registration | R2,300,000 taxable supplies in any 12-month period (from 1 April 2026) |
| Voluntary registration | R120,000 taxable supplies in any 12-month period (from 1 April 2026) |
| Payments basis eligibility | R2,500,000 threshold applies to natural persons only. Full s 15(2) list includes public authorities, water boards, municipal entities, municipalities, associations not for gain, foreign suppliers of electronic services, SABC Ltd, and natural persons under R2,500,000 |
| Full tax invoice threshold | R5,000 |
| No invoice required | Supplies under R50 |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Registration status unknown | STOP -- do not compute |
| Accounting basis unknown | Invoice basis (default) |
| Supply classification unknown | Standard-rated at 15% |
| Private use proportion unknown | 0% recovery |
| Second-hand goods claim | Not claimable until documentation confirmed |

### Required Inputs

**Minimum viable:** Bank statement for the VAT period in CSV, PDF, or pasted text, plus confirmation of VAT registration status and vendor number.

**Recommended:** Sales invoices, purchase invoices with VAT shown, prior period VAT201.

**Ideal:** Complete invoice register, filing category confirmation, prior year VAT reconciliation.

### Refusal Catalogue

- **R-ZA-1 -- Below threshold** — If taxable supplies have not exceeded R2,300,000 in any 12-month period (from 1 April 2026) and client is not voluntarily registered, no VAT obligations. Stop.
- **R-ZA-2: Cross-border services** — Complex cross-border service transactions and customs VAT require specialist review. Escalate.
- **R-ZA-3 -- VAT grouping** — VAT group registrations are outside this skill scope. Escalate.
- **R-ZA-4: Large complex transactions** — Transactions involving property, construction, or financial instruments require specialist review. Escalate.

### 3.1 Income Patterns (Credits)

**Income Patterns table**

| Pattern | Tax Line | Treatment | Notes |
| --- | --- | --- | --- |
| EFT FROM [client] / EFT CREDIT | Taxable supply | Output VAT at 15% | Standard electronic transfer |
| INSTANT MONEY / CASH DEPOSIT | Taxable supply | Revenue | Cash receipt |
| PAYFAST PAYOUT / PAYFAST SETTLEMENT | Taxable supply | Revenue | PayFast payment gateway |
| YOCO SETTLEMENT / YOCO PAYOUT | Taxable supply | Revenue | Yoco card machine settlement |
| SNAPSCAN PAYOUT | Taxable supply | Revenue | SnapScan mobile payment |
| ZAPPER SETTLEMENT | Taxable supply | Revenue | Zapper payment |
| CAPITEC / FNB / ABSA / NEDBANK / STD BANK CREDIT | Taxable supply | Revenue | Bank transfer income |
| INTEREST / INT EARNED | Exempt | NOT taxable | Bank interest -- financial service |
| SARS REFUND | EXCLUDE | Not income | Tax refund |
| LOAN DRAWDOWN | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

**Expense Patterns table**

| Pattern | Expense Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT / COMMERCIAL LEASE | Rent | Input VAT claimable | Business premises |
| ESKOM / CITY POWER / CITY OF CAPE TOWN | Utilities | Input VAT claimable | Electricity |
| TELKOM / VODACOM / MTN / CELL C / RAIN | Communications | Business portion claimable | Mixed use: apportion |
| ENGEN / SHELL / CALTEX / SASOL | Fuel | ZERO-RATED (s 11(1)(h)) -- no VAT on fuel | Lubricants, car-wash, shop purchases at fuel stations are 15% |
| TAKEALOT / MAKRO / GAME | Office supplies | Input VAT claimable | Business purchases |
| GOOGLE ADS / META / LINKEDIN | Advertising | Input VAT claimable | Digital advertising |
| UBER SA / BOLT SA / TAXI | Travel | EXEMPT (s 12(g)) -- fare is exempt; no input VAT claimable | Only the small booking fee (if separately shown) may carry input VAT |
| SARS INCOME TAX / SARS PAYE | EXCLUDE | Tax payment | Not deductible |
| SARS VAT PAYMENT | EXCLUDE | VAT payment | Not input tax |
| BANK CHARGES / FNB FEE / ABSA FEE | Input 15% | Input VAT claimable | Fee-based services are standard-rated per s 2(1) proviso; banks issue monthly VAT tax invoices |
| MOTOR CAR PURCHASE / LEASE / RENTAL (AVIS, EUROPCAR, HERTZ, BIDVEST) | BLOCKED | Input tax blocked under s 17(2)(c) | "Motor car" includes sedans, SUVs, double-cab bakkies, minibuses. Running costs (fuel, repairs) ARE claimable |
| CLIENT LUNCHES / ENTERTAINMENT / CORPORATE GIFTS | BLOCKED | Input tax blocked under s 17(2)(a) | Unless vendor is in the business of providing entertainment |
| CHECKERS / SHOPRITE / PICK N PAY / WOOLWORTHS / SPAR | Office supplies | Input VAT claimable if for resale | For office consumption (tea, coffee, staff fridge), input tax is BLOCKED under s 17(2)(a) entertainment block regardless of whether items are zero-rated or standard-rated. Only claimable where items are for resale |
| OWN TRANSFER / PERSONAL | EXCLUDE | Drawings | Not business |

### 3.3 Zero-Rated Supply Indicators

**Zero-Rated Supply Indicators table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EXPORT / INTERNATIONAL SHIPMENT | Zero-rated output | Goods exported from SA |
| BROWN BREAD / MAIZE MEAL / RICE / EGGS / MILK | Zero-rated | Basic foodstuffs |
| FUEL LEVY / PETROL / DIESEL | Zero-rated | Fuel levy applies instead |

### 3.4 Transport Patterns

**Transport Patterns table**

| Pattern | Expense Category | Treatment | Notes |
| --- | --- | --- | --- |
| FLYSAFAIR / LIFT / CEMAIR | Domestic flights | Input VAT claimable | Domestic air travel is standard-rated at 15% |
| SA AIRLINK | Domestic flights | Input VAT claimable | Standard-rated |
| UBER SA / BOLT SA / TAXI | Local transport | EXEMPT (s 12(g)) | Fare is exempt; no input VAT. Only the booking fee (if separately shown) may carry input VAT |
| GREYHOUND / INTERCAPE | Long-distance bus | EXEMPT (s 12(g)) | Public road transport of fare-paying passengers |

### 3.5 Payment Processor Fees

**Payment Processor Fees table**

| Pattern | Expense Category | Treatment | Notes |
| --- | --- | --- | --- |
| PAYFAST FEE / PAYFAST CHARGE | Payment processing | Input 15% | Standard-rated -- fee-based processing is not a financial service per s 2(1) proviso |
| YOCO FEE / YOCO CHARGE | Payment processing | Input 15% | Standard-rated -- fee-based processing is not a financial service per s 2(1) proviso |
| PEACH PAYMENTS FEE | Payment processing | Input 15% | Standard-rated -- fee-based processing is not a financial service per s 2(1) proviso |

### Example 1 -- Standard Bimonthly Return

**Input:** Standard-rated supplies R500,000 (VAT-exclusive). Purchases R200,000 (VAT-exclusive, all standard-rated, valid invoices).

**Reasoning:**
Output VAT: R500,000 x 15% = R75,000. Input VAT: R200,000 x 15% = R30,000. VAT payable: R75,000 - R30,000 = R45,000. VAT-inclusive supply total: R575,000 (Field 1). VAT-inclusive purchase total: R230,000.

**Classification:** VAT payable R45,000 (Field 20).

### Example 2 -- Exporter in Refund Position

**Input:** Zero-rated exports R800,000. Purchases R300,000 (standard-rated).

**Reasoning:**
Output VAT: R0. Input VAT: R300,000 x 15% = R45,000. Refund: R45,000.

**Classification:** VAT refund R45,000.

### Example 3 -- Second-Hand Goods Purchase

**Input:** Vendor buys used equipment from non-vendor for R50,000 (no VAT charged).

**Reasoning:**
Notional input tax: R50,000 x 15/115 = R6,521.74. Claimable if documentation requirements are met (declaration from seller, proof of payment). Reported in Field 15 (input VAT on other goods/services).

**Classification:** Input tax R6,521.74 (Field 15). Flag for reviewer on documentation.

### Example 4 -- Bad Debt Relief

**Input:** Invoice for R23,000 (incl. VAT) written off after 14 months.

**Reasoning:**
Bad debt relief under s 22(1): debt outstanding over 12 months and written off. Relief: R23,000 x 15/115 = R3,000.

**Classification:** Input tax deduction R3,000.

### Example 5 -- Google Ads (Imported Services)

**Input:** Google Ads spend R50,000 for the period. Google now bills via SA-registered entity with SA VAT number and issues VAT tax invoices.

**Reasoning:**
Where Google bills via a South African entity registered for VAT and issues a valid tax invoice showing 15% VAT, the vendor claims input tax directly. VAT amount: R50,000 x 15/115 = R6,521.74. Reported in Field 15 (input VAT on other goods/services). If billed by a non-resident entity without SA VAT registration, the vendor must self-account for output VAT under s 7(1)(c) in Field 12 (imported services) and claim corresponding input in Field 15 if the service is for making taxable supplies.

**Classification:** Input tax R6,521.74 (Field 15) where billed by SA entity. If imported service: output in Field 12, input in Field 15.

### 5.1 VAT201 Return Fields

**VAT201 Return Fields table**

| Field | Description |
| --- | --- |
| 1 | Standard-rated supplies (VAT-inclusive, excluding capital goods) |
| 1A | Standard-rated capital goods supplied (VAT-inclusive) |
| 2 | Zero-rated supplies (excluding exports) |
| 2A | Zero-rated exported goods |
| 3 | Exempt and non-supplies |
| 4 | Output VAT on Field 1 (Field 1 x 15/115) |
| 4A | Output VAT on Field 1A (Field 1A x 15/115) |
| 5 | Commercial accommodation supplied for 28+ days (value) |
| 6 | Field 5 x 60% (deemed taxable portion) |
| 7 | Field 6 x 15/115 (VAT on deemed portion) |
| 8 | Sum of Fields 6 and 7 |
| 9 | Output VAT on commercial accommodation (Field 8 x 15%) |
| 10 | Change-in-use / second-hand goods exported (consideration) |
| 11 | Field 10 x 15/115 |
| 12 | Other output adjustments and imported services |
| 13 | Total output tax (4 + 4A + 9 + 11 + 12) |
| 14 | Input VAT on capital goods |
| 14A | Input VAT on imported capital goods |
| 15 | Input VAT on other goods/services |
| 15A | Input VAT on imported other goods/services |
| 16 | Change-in-use input adjustment |
| 17 | Bad debts (s 22 relief) |
| 18 | Other input adjustments |
| 19 | Total input tax (14 + 14A + 15 + 15A + 16 + 17 + 18) |
| 20 | Net VAT payable / refundable (13 - 19) |

### 5.2 Filing Categories

**Filing Categories table**

| Category | Frequency | Who |
| --- | --- | --- |
| A | Bimonthly | Default for most vendors |
| B | Monthly | Taxable supplies > R30M/year |
| C | Six-monthly | Farming enterprises (by approval) |
| D | Annual | Small vendors (by approval) |
| E | Annual | Connected-party rental enterprises (by approval) |
| F | Four-monthly | Micro businesses on turnover tax |

### 5.3 Filing Deadlines

**Filing Deadlines table**

| Method | Deadline |
| --- | --- |
| eFiling | Last business day of month following period end |
| Manual (branch) | 25th of month following period end |

### 5.4 Payments Basis (s 15)

- **Payments basis (s 15)** — R2,500,000 threshold applies to natural persons only. Full s 15(2) list includes public authorities, water boards, municipal entities, municipalities, associations not for gain, foreign suppliers of electronic services, SABC Ltd, and natural persons under R2,500,000. Account for VAT when payment is made or received. Must apply to SARS.  _(VAT Act s 15)_

### 5.5 Penalties (TAA Chapter 15)

**Penalties table**

| Offence | Penalty |
| --- | --- |
| Late filing | Fixed amount penalty (escalating scale) |
| Late payment | 10% of amount outstanding |
| Interest | Prescribed rate compounding monthly |
| Understatement | 10-200% depending on behaviour |

### 6.1 Mixed Supplies Apportionment

- **Mixed Supplies Apportionment** — Input tax must be apportioned when making both taxable and exempt supplies. Directly attributable input follows its supply. Residual input apportioned using revenue-based ratio. Flag for reviewer.

### 6.2 Imported Services (Reverse Charge, s 7(1)(c))

- **Imported Services** — If foreign supplier is not VAT-registered in SA and service is consumed in SA, recipient must account for VAT. May claim corresponding input tax if for taxable supplies.

### 6.3 Second-Hand Goods Input Tax (s 16(3)(a)(ii))

- **Second-Hand Goods Input Tax** — Notional input tax: tax fraction (15/115) of consideration paid. Requires declaration from seller and proof of payment. Cannot exceed lesser of consideration paid or open market value. Flag for reviewer.

### 6.4 Change from Payments to Invoice Basis

- **Change from Payments to Invoice Basis** — When turnover exceeds R2,500,000. Transitional adjustments required. Flag for tax practitioner.

### 6.5 Motor vehicle -- is it a "motor car" as defined?

- **Motor vehicle test** — What it shows: Vehicle purchase, lease, rental, or maintenance payment. What's missing: Whether the vehicle is a "motor car" as defined in s 1 (objective test per IN 82 -- passenger area vs loading area). Conservative default: BLOCKED -- no input tax on supply of motor car. Question: "Is this a passenger vehicle (sedan, SUV, hatchback, double-cab bakkie, minibus)? If yes: input on purchase/lease/rental is blocked under s 17(2)(c). Running costs (fuel, repairs, insurance) are claimable for business use." Exception: vendor who continuously supplies motor cars in ordinary course (dealers, rental companies).

## Section 7 -- Working Paper Template

```
SOUTH AFRICA VAT WORKING PAPER (VAT201)
Vendor: _______________  VAT Number: ___________
Period: ___________  Category: A / B / C / D / E / F
Basis: Invoice / Payments

A. OUTPUT (SALES)
  A1. Standard-rated supplies (excl. VAT)        ___________
  A2. Output VAT (A1 x 15%)                     ___________
  A3. Zero-rated supplies                        ___________
  A4. Exempt supplies                            ___________

B. INPUT (PURCHASES)
  B1. Capital goods VAT                          ___________
  B2. Other purchases VAT                        ___________
  B3. Adjustments                                ___________
  B4. Total input VAT                            ___________

C. NET VAT
  C1. Output less input (A2 - B4)                ___________
  C2. VAT payable / refundable                   ___________

REVIEWER FLAGS:
  [ ] Registration and vendor number confirmed?
  [ ] Filing category confirmed?
  [ ] Accounting basis confirmed?
  [ ] Tax invoices held for all input claims?
  [ ] Second-hand goods documentation complete?
  [ ] Zero-rated vs exempt correctly distinguished?
```

### South African Bank Statement Formats

**Bank Statement Formats table**

| Bank | Format | Key Fields |
| --- | --- | --- |
| FNB | CSV / PDF | Date, Description, Amount, Balance |
| ABSA | CSV | Date, Description, Debit, Credit, Balance |
| Standard Bank | CSV | Date, Description, Debit, Credit, Balance |
| Nedbank | CSV | Date, Description, Debit, Credit, Balance |
| Capitec | CSV | Date, Description, Debit, Credit, Balance |
| Investec | CSV | Date, Description, Debit, Credit, Balance |

### Key SA Banking Narrations

**Key SA Banking Narrations table**

| Narration | Meaning | Classification Hint |
| --- | --- | --- |
| EFT CREDIT / INWARD PAYMENT | Bank transfer in | Potential income |
| DEBIT ORDER / DEBI CHECK | Direct debit | Regular expense |
| POS / CARD PURCHASE | Point of sale | Expense |
| CASH DEPOSIT | Cash received | Income |
| SARS / RECEIVER OF REVENUE | Tax payment or refund | Exclude |
| BANK CHARGES / SERVICE FEE | Bank fee | Standard-rated 15% -- input claimable (s 2(1) proviso) |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all EFT credits from business sources as potential taxable supplies
2. Apply conservative defaults: invoice basis, standard-rated, 0% private recovery
3. Only claim input VAT where VAT is clearly evident
4. Flag all large purchases for capital goods review

Present these questions:

```
ONBOARDING QUESTIONS -- SOUTH AFRICA VAT
1. Are you registered as a VAT vendor? What is your VAT number?
2. What filing category are you (A bimonthly, B monthly, C six-monthly, D annual)?
3. Are you on invoice basis or payments basis?
4. What types of goods or services do you sell?
5. Do you make any zero-rated supplies (exports, basic foodstuffs)?
6. Do you make any exempt supplies (financial, residential rent, education)?
7. Do you purchase second-hand goods from non-vendors?
8. Do you import services from non-resident suppliers?
```

### Key Legislation

**Key Legislation table**

| Topic | Section |
| --- | --- |
| Imposition of VAT | VAT Act s 7 |
| Zero-rated supplies | VAT Act s 11 |
| Exempt supplies | VAT Act s 12 |
| Registration | VAT Act s 23 |
| Payments basis | VAT Act s 15 |
| Input tax | VAT Act s 16 |
| Tax invoices | VAT Act s 20 |
| Bad debts | VAT Act s 22 |
| Filing | VAT Act s 27, 28 |

### Known Gaps / Out of Scope

- Cross-border services (complex)
- Customs VAT on imports
- VAT grouping
- Large-value property transactions

### Changelog

**Changelog table**

| Version | Date | Change |
| --- | --- | --- |
| 2.1 | May 2026 | Validated by Werner Britz CA(SA); corrected R2.3m registration threshold; corrected bank charges and payment processor fees to standard-rated; corrected VAT201 field structure; added motor car block; corrected Uber/Bolt to exempt; corrected fuel to zero-rated; added entertainment block; removed Kulula (ceased 2022) |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; SA bank formats; local payment patterns (PayFast, Yoco, SnapScan); worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Registration and vendor number confirmed?
- [ ] Filing category and accounting basis confirmed?
- [ ] Tax fraction 15/115 used consistently?
- [ ] Zero-rated vs exempt correctly distinguished?
- [ ] Second-hand goods claims properly documented?
- [ ] Bad debt relief only after 12 months?

## PROHIBITIONS

- **NEVER claim input tax on exempt supplies** — only taxable (including zero-rated) supplies qualify
- **NEVER charge VAT if not registered as a vendor** — 
- **NEVER use a rate other than 15% for standard-rated supplies** — 
- **NEVER confuse zero-rated (input tax claimable) with exempt (input tax NOT claimable)** — 
- **NEVER claim input tax without a valid tax invoice (for supplies over R50)** — 
- **NEVER ignore the bimonthly filing deadline -- penalties apply from the first day late** — 
- **NEVER apply payments basis without SARS approval** — 
- **NEVER claim notional input on second-hand goods without proper documentation and declarations** — 
- **NEVER claim input on the supply (purchase, lease, rental) of a motor car as defined, unless within an exception under s 17(2)(c)** — 
- **NEVER claim input on entertainment, accommodation, or food and beverages unless the vendor is in the business of providing entertainment or the supply is to an employee away from usual place of work** — 
- **NEVER exclude bank service fees as exempt -- they are standard-rated and input claimable (s 2(1) proviso)** — 
- **NEVER omit output VAT on Seventh Schedule fringe benefits granted to employees under s 18(3)** — 
- **NEVER present calculations as definitive -- always label as estimated and direct client to a SARS-registered tax practitioner** — 

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, chartered accountant (CA(SA)), or equivalent licensed practitioner in South Africa) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
