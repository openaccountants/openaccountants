---
name: za-vat-return
description: Use this skill whenever asked about South African VAT returns for self-employed individuals or small businesses. Trigger on phrases like "South Africa VAT", "VAT201", "SARS VAT", "15% VAT", "eFiling VAT", "zero-rated SA", "VAT vendor", or any question about VAT filing, computation, or registration for vendors in South Africa. Covers the 15% standard rate, zero-rated and exempt supplies, R2.3M registration threshold, VAT201 return, and bimonthly filing via SARS eFiling. ALWAYS read this skill before touching any South African VAT work.
version: 2.2
jurisdiction: ZA
tax_year: 2026
last_updated: 2026-11-01
authored_by: Werner Britz, CA(SA)
reviewed_by: Werner Britz
review_status: current
source_checked: 2026-10-17
trust_label: Checked by Werner Britz
depends_on:
  - vat-workflow-base
category: international
tier: 2
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

## Detail folded from south-africa-vat

Everything below comes from the retired `south-africa-vat` skill, v2.1, validated by Werner Britz CA(SA), and is kept in full so nothing is lost. Where it restates a point above, the two were written for the same VAT Act. Werner Britz is to confirm this merged file.

### Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Werner Britz** on 2026-06-12.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

#### VAT (south-africa-vat)

- **Country** — South Africa (Republic of South Africa)
- **Tax** — VAT (Value-Added Tax)
- **Currency** — ZAR (South African Rand / R)
- **Tax year** — VAT has tax periods, not tax years, and there is no QUARTERLY category in SA. Categories under s 27: A (bimonthly, periods ending January, March, May, July, September, November), B (bimonthly, periods ending February, April, June, August, October, December), C (monthly, >R30m), D (six-monthly: farming below R1.5m, or micro businesses registered for turnover tax on application), E (annual: companies/trusts letting property, renting goods or managing companies for connected persons).  _([VAT Act s 27](https://www.sars.gov.za/types-of-tax/value-added-tax/tax-periods-for-vat-vendors/))_
- **Standard rate** — 15%  _(VAT Act s 7(1)(a); SARS media release 25 April 2025)_
- **Zero rate list** — Two problems: (1) "Residential accommodation on long-term letting by developers" is EXEMPT under s 12(c), not zero-rated. (2) "Certain financial instruments" is misleading - financial instruments are generally exempt under s 2/s 12; the only zero-rated financial supply is gold supplied to the SARB or a bank under s 11(1)(k). Add: supply of an enterprise as a going concern (s 11(1)(e)); illuminating paraffin (s 11(1)(h)); certain government grants; agricultural inputs; deemed exports of second-hand goods.  _(VAT Act s 11 and s 12(c))_
- **Exempt list** — "Lending" alone is too narrow - the s 2 definition covers exchange of currency, dealing in securities, life insurance/reinsurance, retirement annuity contributions, etc. SHORT-TERM insurance is standard-rated (not exempt). Add to list: educational services by recognised institutions; childcare and creche; donated goods/services by associations not for gain.  _(VAT Act s 12 and s 2)_
- **Registration threshold** — R2,300,000 from 1 April 2026 (compulsory). R120,000 (voluntary).  _(VAT Act s 23; SARS Register for VAT page)_
- **Tax authority** — SARS (South African Revenue Service)
- **Return form** — VAT201 (eFiling)
- **Filing portal** — SARS eFiling (https://efiling.sars.gov.za)
- **Filing frequencies** — No quarterly category exists. See "Tax year" row above for the full list.  _(VAT Act s 27)_
- **Filing deadline** — Last business day of month following tax period (eFiling); 25th for paper (not recommended)  _(VAT Act s 28)_
- **Tax invoice** — Add the required content (see Section 5.4 below): full invoice over R5,000 incl VAT, abridged R50-R5,000, no invoice required for R50 or less but a till slip is needed.  _(VAT Act s 16(2) and s 20)_
- **VAT number** — Format: 4xxxxxxxx (10 digits starting with 4)  _(SARS Register for VAT page)_

After validation, update "Validated by" status with reviewer name and date.

- **Field 1** — Add: "excluding capital goods" - capital goods go to Field 1A.  _(SARS VAT201 completion guide)_
- **Field 1A** — Field 1A is the VAT-INCLUSIVE VALUE of standard-rated CAPITAL goods supplied. Output VAT on Field 1 is Field 4. Output VAT on Field 1A is Field 4A.  _(SARS VAT201 completion guide)_
- **Field 2** — Split: Field 2 (zero-rated excl exports), Field 2A (exported goods).  _(SARS VAT201 completion guide)_
- **Field 3** — Exempt supplies  _(SARS VAT201 completion guide)_
- **Field 4** — Field 4 is output VAT on Field 1 (Field 1 x 15/115). Not a total of supplies.  _(SARS VAT201 completion guide)_
- **Field 5** — Field 5 is value of commercial accommodation supplied for more than 28 days. Total output is Field 13.  _(SARS VAT201 completion guide)_
- **Field 10** — Field 10 is consideration on which a notional input was previously deducted, where goods are subsequently exported or applied for non-taxable use - this is an OUTPUT adjustment.  _(SARS VAT201 completion guide)_
- **Field 11** — Field 11 = Field 10 x 15/115. Field 12 is other and imported services (output).  _(SARS VAT201 completion guide)_
- **Field 12** — Field 12 is other and imported services (output side, e.g. imported services self-assessed output). Total input is Field 19.  _(SARS VAT201 completion guide)_
- **Field 13** — Field 13 is TOTAL OUTPUT TAX (sum of Fields 4 + 4A + 9 + 11 + 12). Net VAT is Field 20.  _(SARS VAT201 completion guide)_
- **Field 14** — Field 14 is input VAT on CAPITAL goods (with Field 14A for imported capital). Refund/payable is Field 20.  _(SARS VAT201 completion guide)_
- **Field 15** — Field 15 is input VAT on OTHER goods/services (with Field 15A for imported). Refund/payable is Field 20.  _(SARS VAT201 completion guide)_
- **MISSING: Fields 16, 17, 18, 19, 20** — Field 16 (change in use, input adjustment); Field 17 (bad debts s 22 relief); Field 18 (other inputs); Field 19 (total input tax = sum of 14+14A+15+15A+16+17+18); Field 20 (net VAT payable/refundable).  _(SARS VAT201 completion guide)_
- **Unknown rate on a sale** — 15% standard
- **Unknown counterparty country** — Domestic South Africa
- **Unknown export qualification** — 15% until export evidence confirmed  _(Export Regulation GN R316)_
- **Unknown business-use % (vehicle, entertainment)** — For VEHICLES that are "motor cars" the input is FULLY BLOCKED regardless of business use (s 17(2)(c)). For non-motor-car vehicles and other mixed-use items, the default of 0% is conservative. Reword to flag motor car block.  _(VAT Act s 17(2)(c))_
- **Unknown whether tax invoice compliant** — No input tax  _(VAT Act s 16(2))_
- **Unknown whether zero-rated or exempt** — Treat as taxable 15%
- **Unknown B2B vs B2C for cross-border** — 15% if consumed in South Africa

Reasonable threshold for a high-value review flag.

Reasonable.

Reasonable.

Reasonable.

Reasonable.

- **Minimum viable** — Bank statement for the tax period in CSV, PDF, or pasted text. VAT registration number (starting with 4)
- **Recommended** — Tax invoices are required for input claims above R50, not just above R5,000. Above R5,000 a FULL tax invoice is required; between R50 and R5,000 an abridged invoice is acceptable. Reference to "Field 14" for prior period excess credit is wrong - prior period credit is not a VAT201 field; it carries forward via SARS's vendor statement.  _(VAT Act s 16(2) and s 20)_
- **Ideal** — Complete creditors/debtors ledger, import VAT certificates (SAD500), asset register, prior VAT201 return
- **R-ZA-1: Non-VAT-registered vendor** — Only registered vendors can charge VAT and claim input tax  _(VAT Act s 7 and s 23)_
- **R-ZA-2: Partial exemption / apportionment** — Concept correct. Note: standard turnover-based method (STM) per BGR 16 is the default; alternative methods need a ruling. De minimis rule under proviso to s 17(1): if exempt is less than 5% of total, claim full input. Most small businesses can avoid apportionment with planning.  _(VAT Act s 17(1); BGR 16)_
- **R-ZA-3: Capital goods scheme (Section 18A)** — Section 18A in the skill seems to refer to the change-in-use adjustment under s 18 generally. There is no "capital goods scheme" of the EU type in SA. The s 18(1) adjustment applies on change of use to non-taxable. s 18(4) applies to a change from non-taxable to taxable. s 16(3)(h) gives a deemed input claim on a change of use. The skill should reference s 18 and s 16(3)(h) rather than "s 18A".  _(VAT Act s 18)_
- **R-ZA-4: Financial services (Section 2)** — Financial services have complex VAT treatment. Banks, insurers, and financial institutions require specialist handling.  _(VAT Act s 2 and s 12(a))_
- **R-ZA-5: Property transactions** — Correct as a refusal but note: SA does not have an "option to tax" election for commercial property in the UK sense. Sale of commercial property by a vendor is standard-rated by default; going-concern zero-rating may apply (s 11(1)(e)). Transfer duty interaction is critical.  _(VAT Act s 11(1)(e); Transfer Duty Act)_
- **ABSA BANK, ABSA GROUP** — Bank service fees are STANDARD-RATED at 15%, input claimable. See summary critical finding #3. ABSA issues a monthly VAT tax invoice downloadable from online banking.  _(VAT Act s 2(1) proviso; SARS VAT News 7)_
- **STANDARD BANK, STANBIC** — Standard-rated, input claimable. Same correction.
- **FIRSTRAND, FNB, FIRST NATIONAL BANK** — Standard-rated, input claimable. FNB issues a monthly tax invoice via online banking.
- **NEDBANK** — Standard-rated, input claimable.
- **CAPITEC BANK** — Standard-rated, input claimable.
- **INVESTEC** — Standard-rated, input claimable.
- **AFRICAN BANK** — Standard-rated, input claimable. African Bank's mix of taxable fees and exempt credit provision was the subject of the 2025 SCA judgment on apportionment.  _(CSARS v African Bank Ltd [2025] ZASCA 101)_
- **BANK CHARGES, SERVICE FEE, INTEREST** — Bank charges and service fees: STANDARD-RATED. Interest: exempt. The two should be separated.  _(VAT Act s 2(1) proviso)_
- **SARS, SOUTH AFRICAN REVENUE SERVICE** — EXCLUDE - Tax payment
- **UIF, UNEMPLOYMENT INSURANCE FUND** — EXCLUDE - Statutory contribution
- **WORKMEN'S COMP, COIDA** — EXCLUDE - Compensation fund
- **MUNICIPALITY, LOCAL AUTHORITY (rates)** — Property RATES are out of scope. But same municipality's ELECTRICITY, WATER, REFUSE REMOVAL charges ARE standard-rated and input claimable on the same bill. Most municipal accounts mix rates (no VAT) with electricity/water (15% VAT) - must split on the line item, not exclude the whole supplier.  _(VAT Act s 7)_
- **ROAD ACCIDENT FUND, RAF** — EXCLUDE - Statutory levy
- **ESKOM** — Input 15%
- **CITY POWER (Johannesburg)** — Input 15%
- **CAPE TOWN ELECTRICITY** — Input 15%
- **RAND WATER, RAND WATER BOARD** — Input 15%
- **CITY OF CAPE TOWN WATER** — Input 15%
- **VODACOM** — Input 15%
- **MTN SOUTH AFRICA** — Input 15%
- **CELL C** — Input 15%
- **TELKOM SA** — Input 15%
- **RAIN NETWORK** — Input 15%
- **AFRIHOST** — Input 15%
- **SOUTH AFRICAN AIRWAYS, SAA** — Route distinction (international 0% / domestic 15%) is correct as a high-level summary, but ticket components are NOT uniformly 15% (domestic) or 0% (international). Split required: Airline ticket must be SPLIT - not all components are VATable. Typical breakdown on a domestic SA ticket: (a) Base air fare: 15% VAT (claimable). (b) Fuel surcharge: 15% VAT (claimable, airline cost). (c) ACSA Passenger Service Charge (PSC): 15% VAT INCLUSIVE (per ACSA published tariffs from 1 April 2019; claimable). (d) SACAA Passenger Safety Charge: NOT VATable (statutory levy, pass-through). (e) ATNS Air Traffic and Navigation Services charge: NOT VATable to the passenger (regulated pass-through). (f) Insurance surcharge (if charged by airline): 15% VAT (claimable). (g) Air Passenger Tax (only on flights to international destinations - R100 SACU / R190 other): NOT VATable (tax under s 47B Customs and Excise Act, imposed on the passenger, recovered by the airline). For INTERNATIONAL flights ex-SA: the airfare itself is ZERO-RATED under s 11(2)(a). Airport taxes and APT remain not-VATable. Practical: the airline e-ticket usually shows these as separate lines. Claim input only on the VAT-inclusive components (lines (a), (b), (c), and (f) for domestic; line (c) only for international, since (a) is zero-rated). The full "15% of ticket total" approach overclaims input by approximately the value of items (d), (e), and (g). Note: SAA emerged from business rescue in 2021. Mango (subsidiary) ceased operating in 2021.  _(VAT Act s 11(2)(a) and s 12; Customs and Excise Act s 47B (Air Passenger Tax); ACSA Airport Tariffs schedule (effective 1 April 2019 and as amended); SACAA passenger safety charge regulations; Tax Faculty FAQ on travel agent VAT; Accounting Weekly "International Airfare and VAT Claims")_
- **FLYSAFAIR** — Cannot apply "15% on ticket total" - need to split by component. Airline ticket must be SPLIT - not all components are VATable. Typical breakdown on a domestic SA ticket: (a) Base air fare: 15% VAT (claimable). (b) Fuel surcharge: 15% VAT (claimable, airline cost). (c) ACSA Passenger Service Charge (PSC): 15% VAT INCLUSIVE (per ACSA published tariffs from 1 April 2019; claimable). (d) SACAA Passenger Safety Charge: NOT VATable (statutory levy, pass-through). (e) ATNS Air Traffic and Navigation Services charge: NOT VATable to the passenger (regulated pass-through). (f) Insurance surcharge (if charged by airline): 15% VAT (claimable). (g) Air Passenger Tax (only on flights to international destinations - R100 SACU / R190 other): NOT VATable (tax under s 47B Customs and Excise Act, imposed on the passenger, recovered by the airline). For INTERNATIONAL flights ex-SA: the airfare itself is ZERO-RATED under s 11(2)(a). Airport taxes and APT remain not-VATable. Practical: the airline e-ticket usually shows these as separate lines. Claim input only on the VAT-inclusive components (lines (a), (b), (c), and (f) for domestic; line (c) only for international, since (a) is zero-rated). The full "15% of ticket total" approach overclaims input by approximately the value of items (d), (e), and (g).  _(VAT Act s 11(2)(a) and s 12; Customs and Excise Act s 47B (Air Passenger Tax); ACSA Airport Tariffs schedule (effective 1 April 2019 and as amended); SACAA passenger safety charge regulations; Tax Faculty FAQ on travel agent VAT; Accounting Weekly "International Airfare and VAT Claims")_
- **AIRLINK** — Route framing correct but not all components on a domestic ticket are 15%. Split required: same breakdown as SAA/FlySafair entries above.  _(VAT Act s 11(2)(a) and s 12; Customs and Excise Act s 47B (Air Passenger Tax); ACSA Airport Tariffs schedule (effective 1 April 2019 and as amended); SACAA passenger safety charge regulations; Tax Faculty FAQ on travel agent VAT; Accounting Weekly "International Airfare and VAT Claims")_
- **KULULA.COM** — Kulula ceased operations on 5 July 2022 along with its parent Comair under business rescue. Remove from supplier list. Where the row is being used as a template for similar low-cost domestic carriers (Lift, FlySafair, Cemair): same split-by-component issue applies (same breakdown as SAA/FlySafair entries above).  _(VAT Act s 11(2)(a) and s 12; Customs and Excise Act s 47B (Air Passenger Tax); ACSA Airport Tariffs schedule (effective 1 April 2019 and as amended); SACAA passenger safety charge regulations; Tax Faculty FAQ on travel agent VAT; Accounting Weekly "International Airfare and VAT Claims")_
- **UBER SOUTH AFRICA** — Uber/Bolt operate on an AGENCY model: the platform invoices the rider in the name of the driver as the driver's agent for the fare. The driver is the actual supplier of the road transport service. Under s 12(g), the fare is EXEMPT. Three separate supplies: (1) Driver->Rider fare: EXEMPT (s 12(g)); (2) Uber/Bolt->Driver service fee: STANDARD-RATED 15%, driver may claim input if registered; (3) Uber->Rider booking fee: STANDARD-RATED 15%, business rider may claim input with valid tax invoice. Uber registered as SA VAT vendor from May 2019; Bolt similarly. TAXI: generally not VAT-registered, same s 12(g) exemption applies. Practical: fare not claimable, only booking fee fragment (if separately shown) may be claimed.  _(VAT Act s 12(g) and s 54 (agent and principal); Uber South Africa "Tax Information for Driver-Partners" page; SARS BGR 16 (Issue 4) on apportionment; SARS VAT Quick Reference Guide)_
- **BOLT SOUTH AFRICA** — Same agency model as Uber: platform invoices rider as driver's agent for the fare; fare EXEMPT under s 12(g); service fee/commission STANDARD-RATED 15%; booking fee STANDARD-RATED 15% and claimable with valid tax invoice.  _(VAT Act s 12(g) and s 54; Uber South Africa "Tax Information for Driver-Partners" page; SARS BGR 16 (Issue 4); SARS VAT Quick Reference Guide)_
- **DHL SOUTH AFRICA** — Input 15%  _(VAT Act s 11(2)(a))_
- **FEDEX SOUTH AFRICA** — Input 15%
- **DAWN WING** — Input 15%
- **THE COURIER GUY, TCG** — Input 15%
- **ARAMEX SOUTH AFRICA** — Input 15%
- **CHECKERS, SHOPRITE** — CRITICAL ENTERTAINMENT BLOCK: input tax on food and beverages purchased from a supermarket is usually BLOCKED under s 17(2)(a) regardless of underlying rate, because the supply to employees, clients, or in the office is "entertainment" as defined in s 1. Default for office groceries (tea, coffee, milk, sugar, biscuits, refreshments, staff fridge, year-end party food): NO INPUT TAX regardless of rate. Exceptions where input CAN be claimed: (1) vendor is in the business of providing entertainment (restaurant, hotel, conference venue, caterer, B&B - resale stock); (2) employee subsistence away from usual place of work; (3) employee canteen charged at/above cost (s 17(2)(a)(ii)); (4) bona fide promotional gifts subject to BGR conditions; (5) long-distance road transport operators meals for drivers. Line-item split relevant only where items are genuinely for resale.  _(VAT Act s 1 ("entertainment" definition); s 17(2)(a) (input tax block); SARS BGR 16 (Issue 4); SARS IN 70 (supplies for no consideration); SARS VAT 411 Guide for Entertainment, Accommodation and Catering)_
- **PICK N PAY, PNP** — CRITICAL ENTERTAINMENT BLOCK (same as Checkers/Shoprite entry): input on office groceries blocked under s 17(2)(a); exceptions for hospitality trade, subsistence, canteen-with-charge, promotional gifts, transport operator driver meals.  _(VAT Act s 1 ("entertainment" definition); s 17(2)(a) (input tax block); SARS BGR 16 (Issue 4); SARS IN 70 (supplies for no consideration); SARS VAT 411 Guide for Entertainment, Accommodation and Catering)_
- **WOOLWORTHS FOOD** — CRITICAL ENTERTAINMENT BLOCK (same as above entries): input on office groceries blocked under s 17(2)(a); same exceptions apply.  _(VAT Act s 1 ("entertainment" definition); s 17(2)(a) (input tax block); SARS BGR 16 (Issue 4); SARS IN 70 (supplies for no consideration); SARS VAT 411 Guide for Entertainment, Accommodation and Catering)_
- **SPAR** — CRITICAL ENTERTAINMENT BLOCK (same as above entries): input on office groceries blocked under s 17(2)(a); same exceptions apply.  _(VAT Act s 1 ("entertainment" definition); s 17(2)(a) (input tax block); SARS BGR 16 (Issue 4); SARS IN 70 (supplies for no consideration); SARS VAT 411 Guide for Entertainment, Accommodation and Catering)_
- **FOOD LOVERS MARKET** — CRITICAL ENTERTAINMENT BLOCK (same as above entries): input on office groceries blocked under s 17(2)(a); same exceptions apply.  _(VAT Act s 1 ("entertainment" definition); s 17(2)(a) (input tax block); SARS BGR 16 (Issue 4); SARS IN 70 (supplies for no consideration); SARS VAT 411 Guide for Entertainment, Accommodation and Catering)_
- **CLICKS** — CLAIMABLE at 15% (business use): office cleaning supplies, toiletries, stationery, first aid supplies (mandatory under OHS Act), batteries, other general office consumables. BLOCKED under s 17(2)(a) entertainment: food/beverages for office consumption, catering for client meetings, alcohol for staff functions. NOT FOR BUSINESS (no input claim, not income tax deductible either): personal cosmetics, vitamins for personal use, hair care for personal use; if provided to staff as benefit may be fringe benefit under s 18(3). STANDARD-RATED at 15% but check business purpose: prescription medicines (NOT exempt); OTC medicines - business purchases uncommon (typically only first aid kit stock).  _(VAT Act s 1 ("entertainment" definition - "food, beverages, accommodation, entertainment, amusement, recreation or hospitality"); s 17(2)(a) (entertainment input tax block); SARS BGR 16; Occupational Health and Safety Act 85 of 1993 (first aid kit requirement))_
- **DIS-CHEM** — Skill's line is wrong on two counts. (1) Prescription medicines are STANDARD-RATED at 15%, not exempt or zero-rated. (2) Single-rate "Input 15% (OTC)" too narrow. CLAIMABLE at 15%: office cleaning supplies, toiletries for office, hand sanitiser and tissues, first aid supplies, stationery, batteries. BLOCKED under s 17(2)(a): food/beverages for office consumption, catering items for client meetings. NOT FOR BUSINESS: personal cosmetics, vitamins, baby products, fragrance and beauty products. STANDARD-RATED at 15% input: prescription medicines (corrected from skill's "0% prescription exemption"). All medicines standard-rated. Correct entry: "Input 15% on medicines (prescription and OTC); input 15% on office consumables, cleaning, hygiene, and first aid; entertainment block applies to food and beverage lines; personal cosmetics not business expense."  _(VAT Act s 1 ("entertainment" definition - "food, beverages, accommodation, entertainment, amusement, recreation or hospitality"); s 17(2)(a) (entertainment input tax block); SARS BGR 16; Occupational Health and Safety Act 85 of 1993 (first aid kit requirement); Schedule 2 of VAT Act (excludes prescription medicines))_
- **MCDONALD'S SA, STEERS, NANDO'S** — Standard-rated AS SUPPLIES from the restaurant's side. From the buying business's side, input tax BLOCKED under s 17(2)(a) as entertainment, UNLESS the buying vendor is in the business of providing entertainment (rare), or qualifies as employee subsistence away from usual place of work, or canteen-with-charge, or promotional. Default for a client business: no input claim. CRITICAL ENTERTAINMENT BLOCK applies as with supermarket entries above (office groceries etc.); same five exceptions apply.  _(VAT Act s 1 ("entertainment" definition); s 17(2)(a) (input tax block); SARS BGR 16 (Issue 4); SARS IN 70 (supplies for no consideration); SARS VAT 411 Guide for Entertainment, Accommodation and Catering)_
- **Skill text** — Tighten the trigger: imported service is a service supplied by a non-resident OR by a resident from outside SA, to a recipient who is a resident, for utilisation otherwise than in making taxable supplies. The "net zero" works for fully taxable; partially exempt have a real cost (input apportioned). Critical detail: SA-registered electronic services suppliers (Google SA, Microsoft SA, Meta SA, Amazon SA, etc.) issue SA VAT tax invoices DIRECTLY and this is not an imported service - input is claimed normally. The s 7(1)(c) self-assessment only arises where the foreign entity bills you directly without SA VAT.  _(VAT Act s 7(1)(c) and s 14; Foreign Suppliers of Electronic Services Regulations (2014, expanded 2019))_
- **GOOGLE (Workspace, Ads, Cloud)** — Google Cloud SA, Workspace, and Ads are typically billed by Google SA or Google Ireland with SA VAT charged (Google is a registered foreign electronic services supplier). If billed with SA VAT, treat as standard input. Only self-assess if invoice shows no SA VAT.  _(Foreign Suppliers of Electronic Services Regulations)_
- **MICROSOFT (365, Azure)** — Microsoft is a registered foreign electronic services supplier - bills SA VAT directly. Treat as standard input on a SA VAT tax invoice. Self-assessment only for invoices without SA VAT.
- **META, FACEBOOK ADS** — Meta SA Pty Ltd or Meta Platforms Ireland bills SA VAT. Standard input.
- **ZOOM, SLACK** — Zoom and Slack registered for SA VAT - bill SA VAT directly.
- **NOTION, OPENAI, ANTHROPIC** — Check the actual invoice. Some are now SA VAT-registered (Notion, OpenAI); some bill from US/foreign entity without SA VAT (Anthropic API direct billing as at review date). For those without SA VAT, self-assessment under s 7(1)(c) applies.
- **AWS** — AWS South Africa region bills SA VAT for SA-resident accounts. Treat as standard input.
- **XERO (if billed from NZ)** — Xero now bills SA customers with SA VAT (Xero South Africa). Treat as standard input.
- **XERO (South Africa entity)** — Input 15%
- **SAGE SOUTH AFRICA** — Input 15%
- **PASTEL, SAGE PASTEL** — Input 15%
- **PAYFAST (transaction fees)** — PayFast transaction fees are STANDARD-RATED at 15% and input is claimable. Same logic as bank fees: fee-based payment processing is not a "financial service" under the proviso to s 2(1). PayFast issues a monthly VAT tax invoice. See summary critical finding #15.  _(VAT Act s 2(1) proviso)_
- **YOCO (transaction fees)** — Standard-rated, input claimable. Yoco issues a tax invoice in the merchant dashboard.
- **PEACH PAYMENTS (fees)** — Standard-rated, input claimable.
- **OWN ACCOUNT TRANSFER, INTER-ACCOUNT** — EXCLUDE - Internal movement
- **LOAN, BOND REPAYMENT** — EXCLUDE - Loan principal
- **SALARY, WAGES, PAYROLL** — EXCLUDE - Outside VAT scope
- **DIVIDEND** — EXCLUDE - Out of scope  _(VAT Act s 12(a) and s 2(1)(g))_
- **MUNICIPAL RATES, PROPERTY RATES** — EXCLUDE - Local government levy - not a supply
- **Example 1: Domestic B2B revenue (15%)** — Arithmetic correct. Report on Field 1 (VAT-inclusive R115,000) with output VAT computed at Field 4 (R115,000 x 15/115 = R15,000). The skill describes net R100,000 going to Field 1 but Field 1 takes the VAT-inclusive value.  _(SARS VAT201 completion guide)_
- **Example 2: Export service (zero-rated)** — Correct treatment. Note: services exported are zero-rated under s 11(2)(l), not Schedule 1 (Schedule 1 is the list of standard-rated goods historically; Schedule 2 covers zero-rated). Critical condition: the non-resident recipient must not be in the Republic at the time the services are rendered. If they are in SA, the services are standard-rated. Documentary evidence (contract, proof of payment in foreign currency, evidence of non-residence) is required.  _(VAT Act s 11(2)(l))_
- **Example 3: Electricity (15%, input credit)** — Input tax on other goods/services purchased goes to Field 15 (with Field 15A for imported goods), not Field 10. Field 10 is the OUTPUT adjustment for change in use / second-hand goods exported.  _(SARS VAT201 completion guide)_
- **Example 4: Zero-rated food** — Correct caution. Add: even on the conservative basis, must hold a tax invoice/till slip showing VAT to claim. Without one, no input regardless of treatment.  _(VAT Act s 16(2))_
- **Example 5: Imported service (Google Ads)** — Multiple issues: (1) Google Ads is typically billed by Google SA with SA VAT directly (since electronic services regulations) - no self-assessment if invoice shows SA VAT. (2) Output for imported services goes to Field 12 (other and imported services), not Field 5. (3) Input claimed in Field 15 (other inputs), not Field 10/11.  _(VAT Act s 7(1)(c); SARS VAT201 completion guide)_
- **5.1 Standard rate 15%** — Default rate for all taxable supplies. Section 7(1)(a).  _(VAT Act s 7(1)(a))_
- **5.2 Zero rate 0%** — Multiple errors: (1) PRESCRIPTION MEDICINES are NOT zero-rated - they are standard-rated at 15%. (2) "Qualifying accommodation" is vague - commercial accommodation for more than 28 days has a 60% deemed taxable value (s 10(10)), it is not zero-rated. (3) Add the missing going-concern zero-rating (s 11(1)(e)).  _(VAT Act s 11; Schedule 2)_
- **5.3 Exempt supplies** — Add: educational services by recognised institutions; childcare and creche; donated goods sold by associations not for gain. Confirm "financial services" means narrow s 2 definition.  _(VAT Act s 12)_
- **5.4 Tax invoice requirements (Section 20)** — Threshold mixed up. The position is: (a) supplies R50 or less: NO invoice required (till slip sufficient); (b) supplies between R50 and R5,000: ABRIDGED tax invoice acceptable (omits recipient details and quantity/volume); (c) supplies above R5,000: FULL tax invoice required (seven items including recipient details and quantity). The skill swaps full and abridged. Must be issued within 21 days of the supply.  _(VAT Act s 20(4), (5) and (6); SARS Tax Invoices page)_
- **5.5 Imported services** — Definition tighter: imported service is a service supplied by a person not resident or carrying on business in SA, to a SA-resident recipient, used otherwise than for making taxable supplies. Non-vendor individuals are technically required to remit on VAT215 within 30 days - widely ignored in practice but enforceable.  _(VAT Act s 7(1)(c) and s 14; SARS Form VAT215)_
- **5.6 Anti-avoidance - entertainment** — Largely correct. Add the other exceptions: employee subsistence away from usual place of work; employee canteen for charge; bona fide promotional gifts subject to BGR conditions; long-distance road transport operators meals for drivers.  _(VAT Act s 17(2)(a); BGR 16; SARS IN 70)_
- **5.7 Motor vehicles** — Mostly correct but tightening needed: the "motor car" definition is wider than "passenger vehicle" colloquially - it includes station wagons, double-cab LDVs (bakkies), minibuses up to 16 seats, and SUVs. The test is OBJECTIVE per IN 82 (passenger area vs loading area). Single-cab bakkies are not motor cars. The "transport services" exception is not in the Act - the actual exception under s 17(2)(c) is for vendors who CONTINUOUSLY OR REGULARLY SUPPLY MOTOR CARS in the ordinary course of business (dealers, rental companies). A passenger transport operator (taxi, ride-hailing) is also caught and CAN claim. The skill conflates these.  _(VAT Act s 1 (motor car) and s 17(2)(c); SARS IN 82; RTCC v CSARS VAT 1345)_
- **5.8 Filing deadlines table** — No quarterly category. See Section 1 note above. Five categories under s 27: A, B, C, D, E.  _([VAT Act s 27](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-VAT404-VAT-404-Guide-for-Vendors.pdf))_
- **6.1 Entertainment - is vendor in the hospitality trade?** — Add the other exceptions to the block (see 5.6 above): employee subsistence; employee canteen for charge; promotional gifts subject to BGR conditions.  _(VAT Act s 17(2)(a); BGR 16)_
- **6.2 Motor car - definition** — Reasonable Tier 2 question but should explicitly state the OBJECTIVE test (passenger area vs loading area per IN 82) and include the double-cab bakkie note (caught as motor car) and SUVs (caught). Also add the rental-company / dealer exception under s 17(2)(c).  _(VAT Act s 1 and s 17(2)(c); SARS IN 82)_
- **6.3 Rent - landlord opted to charge VAT?** — "Opt to charge VAT" is a UK concept. In SA, commercial landlords charge VAT if they are registered (compulsory or voluntary); residential letting is exempt regardless. Better framing: "Is this commercial or residential property? Is the landlord VAT-registered (check VAT number on invoice)?"  _(VAT Act s 7 and s 12(c))_
- **6.4 Zero-rated basic food vs standard-rated food** — Itemised receipt question.  _(Schedule 2 Part B)_
- **6.5 Imported services - partial exemption interaction** — Vendor with exempt income may have limited recovery.  _(VAT Act s 17(1))_
- **MISSING: Fringe benefits as deemed supplies** — See summary critical finding #5. Section 18(3) deems Seventh Schedule fringe benefits as taxable supplies by the employer. Output VAT payable on cash equivalent in the month of accrual. Common items: company car, low-interest loans, free or cheap services, assets at less than market value, residential accommodation, awards over R5,000. Exclusions: exempt supplies, zero-rated supplies, entertainment supplied as a fringe benefit.  _(VAT Act s 18(3), s 9(7), s 10(13))_
- **MISSING: Adjustments under s 18** — Section 18 adjustments: (a) s 18(1) when goods/services acquired for taxable use are applied for non-taxable use - output VAT payable on lesser of cost or open market value; (b) s 18(4) when previously non-claimed goods/services are applied for taxable use - input VAT claim available; (c) s 18(3) fringe benefits (above); (d) s 18(7) supplies to relatives and connected persons at non-arm's length.  _(VAT Act s 18)_
- **MISSING: Bad debts and bad debts recovered** — Section 22(1) bad debt relief: vendor on invoice basis may claim input deduction equal to 15/115 of the bad debt amount, where (a) the original supply was taxable, (b) the vendor has already accounted for the supply in a VAT return, (c) the debt has been written off as irrecoverable. s 22(2) recoupment if subsequently recovered. Common practitioner trap.  _([VAT Act s 22](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-VAT404-VAT-404-Guide-for-Vendors.pdf))_
- **A. Output tax structure** — Logic sound. Map to actual VAT201 fields: A1->Field 1, A2->Field 4, A3->Field 2/2A, A4->Field 3, A5->Field 12 (other and imported services), A6->Field 13. Also add capital goods (Field 1A/4A) and commercial accommodation if applicable.  _(SARS VAT201 completion guide)_
- **B. Input tax structure** — Logic sound. Map to actual VAT201: B1/B2 -> Field 15 (or Field 14 for capital), B3 -> Field 15A or 14A, B4 -> Field 15 (imported services input), B5 (blocked) -> not a Field; just excluded from claim, B6 -> Field 19.  _(SARS VAT201 completion guide)_

FNB, Standard Bank, ABSA, Nedbank, Capitec column structures

- **CREDIT** — Incoming funds / Potential revenue
- **DEBIT** — Outgoing payment / Potential expense
- **ATM WITHDRAWAL** — Cash withdrawal / Tier 2 - ask
- **BANK CHARGES** — Bank charges are STANDARD-RATED at 15%, input claimable. See critical finding #3.  _(VAT Act s 2(1) proviso)_
- **INTEREST EARNED** — Interest received / Exempt  _(VAT Act s 12(a) read with s 2(1)(f))_
- **BALANCE** — Running balance / Ignore
- **SALARY / WAGES** — Payroll / Out of VAT scope
- **Q1: VAT number** — VAT registration number (10 digits starting with 4)
- **Q2: Tax period** — Tax period covered by this bank statement
- **Q3: Filing frequency** — Add specifically: Category A/B/C/D/E.  _([VAT Act s 27](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-VAT404-VAT-404-Guide-for-Vendors.pdf))_
- **Q4: Exports** — Do you have any exports? Evidence held?  _(Export Regulation GN R316)_
- **Q5: Exempt income** — Financial services, residential rent  _(VAT Act s 17(1))_
- **Q6: Entertainment vendor** — Determines whether entertainment input is blocked  _(VAT Act s 17(2)(a))_
- **Q7: Vehicles for goods** — Better question: "Do you own/lease/rent any motor vehicles? What type (sedan, SUV, single-cab bakkie, double-cab bakkie, panel van, truck)? What use?" The "motor car" definition turns on construction, not use.  _(VAT Act s 1 and s 17(2)(c))_
- **Q8: Imported services** — Refine: which suppliers bill SA VAT vs which bill without (the latter trigger self-assessment).
- **Q9: Prior period credit** — Amount to carry forward
- **MISSING: Q10 Employee fringe benefits** — Add: "Do you employ staff and grant any Seventh Schedule fringe benefits?" Triggers s 18(3) output VAT analysis.  _(VAT Act s 18(3))_
- **MISSING: Q11 Tax invoice compliance** — Add: "Do all your supplier tax invoices meet the s 20 requirements (or abridged for R50-R5,000)? Have any been queried by SARS?"  _(VAT Act s 20)_
- **Key legislation table** — Add: s 1 (definitions); s 8 (deemed supplies); s 9 (time of supply); s 10 (value of supply); s 14 (imported services calculation); s 15 (accounting basis); s 18 (adjustments); s 22 (bad debts); s 23 (registration); s 27 (tax periods); s 28 (returns); s 41B (rulings); s 50 (branch registration); s 72 (Commissioner's decisions).  _(VAT Act)_
- **Known gaps** — No "option to tax" in SA (UK concept). Add to gaps: gold and valuable metals (DRC regulations); electronic services foreign supply; mining; long-term insurance; share blocks; instalment credit agreements; connected-person supplies.
- **Self-check list** — Add: motor car block; fringe benefits (s 18(3)); change-in-use adjustments; bad debts.
- **NEVER allow input on entertainment unless hospitality** — CORRECT  _(VAT Act s 17(2)(a))_
- **NEVER allow input on motor cars (passenger) for mixed purposes** — Block applies regardless of business use percentage - not just "mixed purposes". Even 100% business use of a motor car is blocked (unless within s 17(2)(c) exceptions).  _(VAT Act s 17(2)(c))_
- **NEVER zero-rate exports without evidence** — CORRECT  _(Export Regulation GN R316)_
- **NEVER allow input from a non-VAT-registered supplier** — CORRECT  _(VAT Act s 16(2) and s 16(3)(a)(ii))_
- **NEVER self-assess imported services without recording both output and input** — CORRECT  _(VAT Act s 7(1)(c))_
- **NEVER present calculations as definitive** — NEVER present calculations as definitive
- **MISSING prohibition: bank fees** — Add: "Never exclude bank service fees as exempt - they are standard-rated and input claimable."  _(VAT Act s 2(1) proviso)_
- **MISSING prohibition: fringe benefits** — Add: "Never omit s 18(3) output VAT on employee fringe benefits."  _(VAT Act s 18(3))_

Note: skill has the disclaimer duplicated at end of file (sections 514-516 and 521-525). One copy is enough.

### Section 1 — Quick reference

**Section 1 — Quick reference**  _(https://www.sars.gov.za/types-of-tax/value-added-tax/tax-periods-for-vat-vendors/)_

| Field | Value |
| --- | --- |
| Country | South Africa (Republic of South Africa) |
| Tax | VAT (Value-Added Tax) |
| Currency | ZAR (South African Rand / R) |
| Tax year | Tax periods under s 27: Category A bimonthly (odd months) or B bimonthly (even months) (default, allocated by SARS); C monthly (>R30m); D six-monthly (farming <R1.5m, or micro businesses on turnover tax on application); E annual (companies/trusts supplying connected persons). No quarterly category exists. |
| Standard rate | 15% |
| Zero rate | 0% (exports; basic foodstuffs (Schedule 2); international transport; certain farming inputs; petrol/diesel; illuminating paraffin; supply of enterprise as going concern (s 11(1)(e)); gold to SARB/bank) |
| Exempt | Financial services (narrow s 2 definition -- interest, exchange margins, life insurance, dealing in securities; fee-based services are STANDARD-RATED per s 2(1) proviso), residential rental, public road and rail transport (s 12(g)), educational services by recognised institutions, childcare, donated goods/services by associations not for gain. Short-term insurance is STANDARD-RATED, not exempt. |
| Registration threshold | ZAR 2,300,000 in any consecutive 12-month period (from 1 April 2026). Voluntary registration: ZAR 120,000. |
| Tax authority | SARS (South African Revenue Service) |
| Return form | VAT201 (eFiling) |
| Filing portal | SARS eFiling (https://efiling.sars.gov.za) |
| Filing frequencies | Category A bimonthly (odd months) and Category B bimonthly (even months) (default); Category C monthly (>R30m); Category D six-monthly (farming <R1.5m, or micro businesses on turnover tax); Category E annual (companies/trusts supplying connected persons) |
| Filing deadline | Last business day of month following tax period (eFiling); 25th for paper (not recommended) |
| Tax invoice | VAT-compliant invoice — required for input tax |
| VAT number | Format: 4xxxxxxxx (10 digits starting with 4) |
| Contributor | Open Accountants Community |
| Validated by | Werner Britz CA(SA), Spurwing CFO |
| Validation date | May 2026 |
| Skill version | 2.1 |

#### Key VAT201 fields

**Key VAT201 fields**  _(https://www.sars.gov.za/wp-content/uploads/Ops/Guides/GEN-ELEC-04-G01-Guide-for-completing-the-Value-Added-Tax-VAT201-Declaration-External-Guide.pdf)_

| Field | Meaning |
| --- | --- |
| 1 | Standard-rated supplies (VAT-inclusive, excluding capital goods and accommodation) |
| 1A | Standard-rated capital goods supplied (VAT-inclusive) |
| 2 | Zero-rated supplies (excluding exports) |
| 2A | Zero-rated exported goods |
| 3 | Exempt and non-supplies |
| 4 | Output VAT on Field 1 (Field 1 x 15/115) |
| 4A | Output VAT on Field 1A |
| 5 | Commercial accommodation supplied for more than 28 days (VAT-exclusive; 60% taxed via Field 6) |
| 9 | Output VAT on commercial accommodation |
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

#### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 15% standard |
| Unknown counterparty country | Domestic South Africa |
| Unknown export qualification | 15% until export evidence confirmed |
| Unknown business-use % (vehicle, entertainment) | 0% input tax. Note: for motor cars as defined, input is FULLY BLOCKED under s 17(2)(c) regardless of business use percentage. |
| Unknown whether tax invoice compliant | No input tax |
| Unknown whether zero-rated or exempt | Treat as taxable 15% |
| Unknown B2B vs B2C for cross-border | 15% if consumed in South Africa |

#### Red flag thresholds

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single transaction | ZAR 50,000 |
| HIGH tax delta on single default | ZAR 7,500 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net VAT position | ZAR 30,000 |

#### Required inputs

Minimum viable — bank statement for the tax period in CSV, PDF, or pasted text. VAT registration number (starting with 4).

Recommended — tax invoices for all input tax claims above ZAR 50 (full tax invoice above ZAR 5,000), sales invoices for all output, prior period excess credit.

Ideal — complete creditors/debtors ledger, import VAT certificates (SAD500), asset register, prior VAT201 return.

Refusal if minimum missing — SOFT WARN. No bank statement = hard stop. "Input tax credits require a valid VAT tax invoice per Section 20 of the VAT Act. All credits are provisional pending invoice verification."

#### Refusal catalogue

- **R-ZA-1 — Non-VAT-registered vendor** — "Only registered vendors can charge VAT and claim input tax. Confirm VAT registration before proceeding."  _(R-ZA-1)_
- **R-ZA-2 — Partial exemption / apportionment** — "If the vendor makes both taxable and exempt supplies, input tax must be apportioned under Section 17(1) of the VAT Act. The apportionment ratio changes annually — out of scope without full-year data. Escalate to a CA(SA)."  _(R-ZA-2, Section 17(1) VAT Act)_
- **R-ZA-3 — Capital goods scheme (Section 18A)** — "Adjustments to input tax on capital goods where use changes between taxable and non-taxable purposes require specialist computation. Out of scope."  _(R-ZA-3, Section 18A)_
- **R-ZA-4 — Financial services (Section 2)** — "Financial services have complex VAT treatment. Banks, insurers, and financial institutions require specialist handling. Out of scope."  _(R-ZA-4, Section 2)_
- **R-ZA-5 — Property transactions** — "Property development, sale of commercial property, and going-concern zero-rating elections are highly fact-sensitive. Escalate to specialist."  _(R-ZA-5)_

#### 3.1 South African banks — fees (standard-rated per s 2(1) proviso)

**South African banks — fees (standard-rated per s 2(1) proviso)**  _(s 2(1) proviso; s 12(a); s 2(1)(f))_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ABSA BANK, ABSA GROUP | Input 15% | Bank service fees are standard-rated per s 2(1) proviso; banks issue monthly VAT tax invoices. Interest remains exempt. |
| STANDARD BANK, STANBIC | Input 15% | Standard-rated per s 2(1) proviso |
| FIRSTRAND, FNB, FIRST NATIONAL BANK | Input 15% | Standard-rated per s 2(1) proviso |
| NEDBANK | Input 15% | Standard-rated per s 2(1) proviso |
| CAPITEC BANK | Input 15% | Standard-rated per s 2(1) proviso |
| INVESTEC | Input 15% | Standard-rated per s 2(1) proviso |
| AFRICAN BANK | Input 15% | Standard-rated per s 2(1) proviso |
| BANK CHARGES, SERVICE FEE | Input 15% | Standard-rated per s 2(1) proviso |
| INTEREST | EXCLUDE | Exempt under s 12(a) / s 2(1)(f) |

#### 3.2 South African government and statutory (exclude)

**South African government and statutory (exclude)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SARS, SOUTH AFRICAN REVENUE SERVICE | EXCLUDE | Tax payment |
| UIF, UNEMPLOYMENT INSURANCE FUND | EXCLUDE | Statutory contribution |
| WORKMEN'S COMP, COIDA | EXCLUDE | Compensation fund |
| MUNICIPALITY, LOCAL AUTHORITY (rates) | EXCLUDE | Rates and taxes — outside VAT scope |
| ROAD ACCIDENT FUND, RAF | EXCLUDE | Statutory levy |

#### 3.3 South African utilities (taxable at 15%)

**South African utilities (taxable at 15%)**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| ESKOM | Input 15% | 15% | National electricity — taxable |
| CITY POWER (Johannesburg) | Input 15% | 15% | Municipal electricity — taxable |
| CAPE TOWN ELECTRICITY | Input 15% | 15% | Municipal electricity — taxable |
| RAND WATER, RAND WATER BOARD | Input 15% | 15% | Water — taxable |
| CITY OF CAPE TOWN WATER | Input 15% | 15% | Water — taxable |
| VODACOM | Input 15% | 15% | Mobile/internet — taxable |
| MTN SOUTH AFRICA | Input 15% | 15% | Mobile — taxable |
| CELL C | Input 15% | 15% | Mobile — taxable |
| TELKOM SA | Input 15% | 15% | Fixed-line/internet — taxable |
| RAIN NETWORK | Input 15% | 15% | Internet — taxable |
| AFRIHOST | Input 15% | 15% | Internet — taxable |

#### 3.4 Transport and logistics

**Transport and logistics**  _(s 12(g))_

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| SOUTH AFRICAN AIRWAYS, SAA | Check route | 0%/15% | International 0%; domestic 15% |
| FLYSAFAIR | Input 15% | 15% | Domestic airline — 15% |
| AIRLINK | Check route | 0%/15% | International 0%; domestic 15% |
| KULULA.COM | Input 15% | 15% | Domestic — 15% |
| UBER SOUTH AFRICA / BOLT SOUTH AFRICA | EXEMPT (s 12(g)) | — | Fare is exempt -- road transport of fare-paying passengers. No input VAT claimable on the fare. Only the booking fee (if separately shown on Uber tax invoice) may carry input VAT. |
| DHL SOUTH AFRICA | Input 15% | 15% | Courier — taxable |
| FEDEX SOUTH AFRICA | Input 15% | 15% | Courier — taxable |
| DAWN WING | Input 15% | 15% | Courier — taxable |
| THE COURIER GUY, TCG | Input 15% | 15% | Courier — taxable |
| ARAMEX SOUTH AFRICA | Input 15% | 15% | Courier — taxable |

#### 3.5 Food and retail

**Food and retail**  _(s 17(2)(a))_

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| CHECKERS, SHOPRITE | Input 15%/0% | Mixed | Basic zero-rated food items; non-food 15%. For office consumption (tea, coffee, staff fridge, year-end function), input tax is BLOCKED under s 17(2)(a) entertainment regardless of zero-rate/standard-rate split. Only claimable where items are for resale by a vendor in the entertainment trade. |
| PICK N PAY, PNP | Input 15%/0% | Mixed | Same — zero-rate basic foodstuffs. For office consumption (tea, coffee, staff fridge, year-end function), input tax is BLOCKED under s 17(2)(a) entertainment regardless of zero-rate/standard-rate split. Only claimable where items are for resale by a vendor in the entertainment trade. |
| WOOLWORTHS FOOD | Input 15%/0% | Mixed | Food hall: basic items 0%; prepared/luxury food 15%. For office consumption (tea, coffee, staff fridge, year-end function), input tax is BLOCKED under s 17(2)(a) entertainment regardless of zero-rate/standard-rate split. Only claimable where items are for resale by a vendor in the entertainment trade. |
| SPAR | Input 15%/0% | Mixed | Same. For office consumption (tea, coffee, staff fridge, year-end function), input tax is BLOCKED under s 17(2)(a) entertainment regardless of zero-rate/standard-rate split. Only claimable where items are for resale by a vendor in the entertainment trade. |
| FOOD LOVERS MARKET | Input 15%/0% | Mixed | Same. For office consumption (tea, coffee, staff fridge, year-end function), input tax is BLOCKED under s 17(2)(a) entertainment regardless of zero-rate/standard-rate split. Only claimable where items are for resale by a vendor in the entertainment trade. |
| CLICKS | Input 15% | 15% | Health/beauty retail — 15% |
| DIS-CHEM | Input 15% | 15% | Prescription medicines are standard-rated at 15%; all pharmacy items 15% |
| MCDONALD'S SA, STEERS, NANDO'S | BLOCKED under s 17(2)(a) | 15% | BLOCKED under s 17(2)(a) for the buying business. Only the restaurant itself (being in the entertainment trade) can claim its own inputs. |

- **Zero-rated basic foodstuffs** — Brown bread, maize meal, mielie rice, dried mealies, dried beans, lentils, pilchards/sardines in tins, milk, eggs, fruits and vegetables, vegetable oil, edible legumes. These are zero-rated under Schedule 2 of the VAT Act.  _(Schedule 2 of the VAT Act)_

#### 3.6 SaaS — international suppliers (reverse charge / imported services)

- **Imported services rule** — Under VAT Act Section 7(1)(c), imported services from abroad are subject to VAT if the recipient is a non-vendor or partially exempt vendor. Services used wholly to make taxable supplies are not "imported services" as defined, so a fully taxable vendor declares nothing. Where the foreign supplier is registered as an SA vendor (e.g. electronic services), SA VAT is on the invoice and is claimed as normal input tax.  _([VAT Act Section 7(1)(c)](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-VAT404-VAT-404-Guide-for-Vendors.pdf))_

**SaaS — international suppliers (reverse charge / imported services)**  _([VAT Act Section 7(1)(c)](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-VAT404-VAT-404-Guide-for-Vendors.pdf))_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE (Workspace, Ads, Cloud) | Input 15% if invoice shows SA VAT; otherwise imported services only on the non-taxable portion | Registered foreign electronic-services suppliers charge SA VAT; no VAT is declared on services used wholly for taxable supplies |
| MICROSOFT (365, Azure) | Imported services — self-assess 15% | Same |
| META, FACEBOOK ADS | Imported services — self-assess 15% | Same |
| ZOOM, SLACK | Imported services — self-assess 15% | Same |
| NOTION, OPENAI, ANTHROPIC | Imported services — self-assess 15% | Same |
| AWS | Imported services — self-assess 15% | Same |
| XERO (if billed from NZ) | Imported services — self-assess 15% | Same |
| SAGE (if billed from UK) | Imported services — self-assess 15% | Same |

#### 3.7 Local SaaS and professional tools (15%)

**Local SaaS and professional tools (15%)**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| XERO (South Africa entity) | Input 15% | 15% | Accounting software |
| SAGE SOUTH AFRICA | Input 15% | 15% | Accounting/payroll |
| PASTEL, SAGE PASTEL | Input 15% | 15% | South African accounting |
| QUICKBOOKS SOUTH AFRICA | Input 15% | 15% | Accounting SaaS |

#### 3.8 Payment processors (standard-rated per s 2(1) proviso)

**Payment processors (standard-rated per s 2(1) proviso)**  _(s 2(1) proviso)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PAYFAST (transaction fees) | Input 15% | Standard-rated -- fee-based payment processing is not a financial service per s 2(1) proviso |
| YOCO (transaction fees) | Input 15% | Standard-rated -- fee-based payment processing is not a financial service per s 2(1) proviso |
| PEACH PAYMENTS (fees) | Input 15% | Standard-rated -- fee-based payment processing is not a financial service per s 2(1) proviso |
| STRIPE (fees) | Input 15% | Standard-rated -- fee-based payment processing is not a financial service per s 2(1) proviso |

#### 3.9 Internal transfers and exclusions

**Internal transfers and exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OWN ACCOUNT TRANSFER, INTER-ACCOUNT | EXCLUDE | Internal movement |
| LOAN, BOND REPAYMENT | EXCLUDE | Loan principal |
| SALARY, WAGES, PAYROLL | EXCLUDE | Outside VAT scope |
| DIVIDEND | EXCLUDE | Out of scope |
| MUNICIPAL RATES, PROPERTY RATES | EXCLUDE | Local government levy — not a supply |
| ATM, CASH WITHDRAWAL | Tier 2 — ask | Default exclude |

### Section 4 — Worked examples

Six classifications from a hypothetical Johannesburg-based IT consultant. Format: FNB (First National Bank) account statement.

#### Example 1 — Domestic B2B revenue (15%)

**Input line:**
`15 Apr 2025  CREDIT  ABC TECHNOLOGY (PTY) LTD  INV-2025-041  R 115,000.00  R 500,000.00`

**Reasoning:**
Incoming R 115,000 (VAT-inclusive) from a SA company for IT consulting. Standard 15% VAT. Gross R 115,000 includes VAT. Net = R 100,000 (taxable supply) + R 15,000 output tax (R 115,000 × 15/115). A VAT-compliant tax invoice must be issued per Section 20 of the VAT Act. Report R 115,000 VAT-inclusive on VAT201 Field 1. Output VAT R 15,000 goes to Field 4.

**Classification:** Output tax 15% — R 15,000. Net supply: R 100,000. VAT-inclusive: R 115,000.

#### Example 2 — Export service (zero-rated)

**Input line:**
`22 Apr 2025  CREDIT  ACME CORP USA  USD 5,000 (R 92,500)  R 592,500.00`

**Reasoning:**
USD receipt from a US company for IT consulting services exported from South Africa. Zero-rated under section 11(2)(l) of the VAT Act if the services are supplied to a non-resident who is not present in SA when the services are rendered (and no exclusion applies). Evidence: contract showing foreign client, payment in foreign currency. Report R 92,500 on Field 2 (zero-rated). Output tax: R 0.

**Classification:** Zero-rated export — R 92,500. Output tax: R 0.

#### Example 3 — Electricity (15%, input credit)

**Input line:**
`10 Apr 2025  DEBIT  ESKOM HOLDINGS SOC  April electricity  -R 11,500.00  R 388,500.00`

**Reasoning:**
Eskom electricity bill. Taxable at 15%. Gross R 11,500. Net = R 10,000 + R 1,500 input tax (R 11,500 × 15/115). Eskom issues VAT-compliant tax invoices — input credit of R 1,500 claimable. Report on Field 15 (input VAT on other goods/services).

**Classification:** Input tax 15% — R 1,500. Net expense: R 10,000.

#### Example 4 — Zero-rated food (basic foodstuffs)

**Input line:**
`12 Apr 2025  DEBIT  PICK N PAY  Groceries (business kitchen)  -R 800.00  R 387,700.00`

**Reasoning:**
Grocery purchase. If itemised receipt shows basic foodstuffs only (brown bread, eggs, fresh vegetables, etc.) — zero-rated under Schedule 2 of the VAT Act. No input tax on zero-rated items (the input tax rate is 0%). If mixed grocery (some 15% non-food items), split the purchase. Without itemised receipt: conservative default is 15% on full amount.

**Classification:** Zero-rated (if basic foodstuffs only) — R 0 input tax. Conservative default: 15% on R 800 = R 104 input tax / (R 695.65 net + R 104 VAT = R 800 gross). Flag: obtain itemised receipt.

#### Example 5 — Imported service — self-assess (Google Ads)

**Input line:**
`08 Apr 2025  DEBIT  GOOGLE IRELAND LIMITED  Google Ads April  -R 10,000.00  R 377,700.00`

**Reasoning:**
Google Ads billed from Ireland. Note: Google typically bills SA VAT directly now via its local entity; check the invoice. If billed by a non-resident entity, this is an "imported service" under Section 7(1)(c) of the VAT Act. The South African VAT-registered vendor must self-assess 15% VAT. Self-assessed output: R 10,000 × 15% = R 1,500 (add to Field 12 — other output adjustments and imported services). For a fully taxable vendor, simultaneously claim same as input tax R 1,500 (Field 15 — input VAT on other goods/services). Net effect: zero. Must be disclosed in the VAT201.

**Classification:** For a vendor using the service wholly to make taxable supplies, this is not an "imported service" as defined — no VAT is declared (nothing in Field 12 or Field 15). VAT is declared in Field 12 only to the extent the service is used for non-taxable purposes.

#### Example 6 — Residential rent (exempt, no input tax)

**Input line:**
`01 Apr 2025  DEBIT  CITY PROP MANAGEMENT  April office rent  -R 23,000.00  R 354,700.00`

**Reasoning:**
Monthly rent. If this is for a commercial office space where the landlord has opted to charge VAT and issues a VAT invoice showing 15%, then input tax of R 3,000 is claimable (gross R 23,000 / 1.15 × 15%). If the landlord has NOT opted to charge VAT (which is common for smaller landlords), then the rent is exempt and no input tax is available. Default: ask for the landlord's VAT invoice.

**Classification:** Tier 2 — ask. If VAT invoice received from landlord: Input 15% — R 3,000. If no VAT invoice: EXEMPT — no input tax.

#### 5.1 Standard rate 15%

- **Standard rate** — 15% (Default rate for all taxable supplies)  _(VAT Act No. 89 of 1991, Section 7(1)(a))_

#### 5.2 Zero rate 0%

- **Zero rate 0% supplies** — Exports of goods and qualifying services; basic foodstuffs (Schedule 2); illuminating paraffin; petrol and diesel (specific provisions); certain agricultural inputs; supply of enterprise as going concern (s 11(1)(e)); gold to SARB/bank. Evidence required for export zero-rating. Prescription medicines are STANDARD-RATED at 15%.  _(VAT Act Section 11; Schedule 2)_

#### 5.3 Exempt supplies

- **Exempt supplies** — Financial services (Section 2); residential rental; public road and rail transport. No output tax charged; no input tax claimable on costs.  _(VAT Act Section 12)_

#### 5.4 Tax invoice requirements (Section 20)

- **Supplies R50 or less** — NO invoice required (till slip sufficient)  _(Section 20)_
- **Supplies R50 to R5,000** — ABRIDGED tax invoice (omits recipient details), except zero-rated supplies, which always need a FULL tax invoice  _([Section 20](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-VAT404-VAT-404-Guide-for-Vendors.pdf))_
- **Supplies above R5,000** — FULL tax invoice required with supplier name/address/VAT number, invoice number, date, buyer name/address/VAT number (if VAT-registered), description, net amount, VAT rate, VAT amount, total  _(Section 20)_
- **Tax invoice issuance timeframe** — Must be issued within 21 days.  _(Section 20)_

#### 5.5 Imported services

- **Imported services treatment** — Services supplied by a non-resident to a South African recipient are subject to VAT under Section 7(1)(c). Services used wholly to make taxable supplies are not imported services and no VAT is declared; vendors declare VAT in Field 12 only on the non-taxable portion. Partially exempt or non-vendor recipients cannot recover and face a cost.  _([VAT Act Section 7(1)(c)](https://www.sars.gov.za/wp-content/uploads/Ops/Guides/Legal-Pub-Guide-VAT404-VAT-404-Guide-for-Vendors.pdf))_

#### 5.6 Anti-avoidance — entertainment

- **Entertainment input tax block** — Input tax on entertainment, accommodation, and food/beverages is BLOCKED under Section 17(2)(a) UNLESS the vendor is in the business of providing entertainment (hotels, restaurants, conference venues). "Entertainment" includes meals, beverages, social functions.  _(Section 17(2)(a))_

#### 5.7 Motor vehicles

- **Motor vehicle input tax block** — Input tax on motor cars (as defined — passenger vehicles) is BLOCKED under Section 17(2)(c). Exception: if the vendor trades in motor cars or provides transport services as their primary business. Bakkies (utes/pickups) used exclusively for business: may qualify.  _(Section 17(2)(c))_

#### 5.8 Filing deadlines

**Filing deadlines**  _(https://www.sars.gov.za/types-of-tax/value-added-tax/tax-periods-for-vat-vendors/)_

| Category | Period | Due date |
| --- | --- | --- |
| Category C (>R30m) | Monthly | Last business day of following month |
| Category A / B (default) | Bimonthly | Last business day of following month |
| Category D (farming <R1.5m; micro businesses) | Six-monthly | Last business day of following month |
| Category E (company/trust supplying connected persons) | Annual | Last business day of following month |

#### 5.9 Penalties

**Penalties**  _(https://www.sars.gov.za/individuals/what-if-i-do-not-agree/admin-penalty/)_

| Offence | Penalty |
| --- | --- |
| Late return | ZAR 250–ZAR 16,000 per month late |
| Late payment | 10% of tax due + interest at prescribed rate |
| Understatement | 10%–200% of shortfall depending on intent |
| Fraud | Criminal prosecution |

#### 6.1 Entertainment — is vendor in the hospitality trade?

**What it shows:** Restaurant, entertainment, or accommodation expense.
**What's missing:** Whether the vendor's primary business is hospitality/entertainment (unblocks the input).
**Conservative default:** BLOCKED — no input tax.
**Question to ask:** "Is this entertainment expense directly related to the provision of entertainment to customers (e.g., you are a restaurant, hotel, or conference venue)? If not, the input tax is blocked."

#### 6.2 Motor vehicle — is it a "motor car" as defined?

**What it shows:** Vehicle purchase, lease, or maintenance.
**What's missing:** Whether the vehicle is a "motor car" (blocked) or a qualifying vehicle.
**Conservative default:** BLOCKED — no input tax.
**Question to ask:** "Is this a passenger vehicle (sedan, SUV, hatchback) used for business? If yes: blocked. Is it a bakkie/van used exclusively for business goods transport? If exclusively business use: may be unblocked."

#### 6.3 Rent — has landlord opted to charge VAT?

**What it shows:** Monthly rent payment.
**What's missing:** Whether the landlord is VAT-registered and has charged VAT on the invoice.
**Conservative default:** No input tax (treat as exempt until VAT invoice confirmed).
**Question to ask:** "Does your landlord issue a VAT tax invoice for the rent showing their VAT number and 15% VAT? If not, no input credit is available."

#### 6.4 Zero-rated basic food vs. standard-rated food

**What it shows:** Supermarket purchase.
**What's missing:** Itemised receipt showing which items are basic (zero-rated) vs. standard (15%).
**Conservative default:** 15% on full amount.
**Question to ask:** "Do you have an itemised till slip? Items like brown bread, eggs, fresh vegetables, milk are zero-rated; packaged snacks, prepared food, non-food items are 15%."

#### 6.5 Imported services — partial exemption interaction

**What it shows:** Payment for foreign digital services.
**What's missing:** Whether the vendor has any exempt income that blocks full input tax recovery on imported services.
**Conservative default:** Self-assess output and input at 15% (net zero for fully taxable).
**Question to ask:** "Does the business have any exempt income (residential rent, financial services)? If yes, the imported services input tax recovery may be limited."

#### 6.6 Motor vehicle — is it a "motor car" as defined?

- **Motor car definition and blocked input** — Input tax on the supply of a "motor car" is BLOCKED under s 17(2)(c). "Motor car" definition includes sedans, SUVs, double-cab bakkies, minibuses up to 16 seats. Objective test per IN 82 (passenger area vs loading area). Single-cab bakkies are NOT motor cars. Running costs (fuel, repairs, insurance) ARE claimable even on blocked motor cars. Exception: vendor who continuously supplies motor cars in ordinary course (dealers, rental companies).  _(s 17(2)(c); IN 82)_

### Section 7 — Excel working paper template

```
SOUTH AFRICA VAT201 WORKING PAPER
Tax Period: ____________  VAT Registration No.: ____________

A. OUTPUT TAX
  A1. Standard-rated supplies at 15% (net)     ___________
  A2. Output tax 15% (A1 × 15/115 of gross OR A1 × 15%)  ___
  A3. Zero-rated supplies (net)                ___________
  A4. Exempt supplies (net)                    ___________
  A5. Imported services self-assessed output   ___________
  A6. Total output tax (A2 + A5)               ___________

B. INPUT TAX
  B1. Standard-rated purchases (net)           ___________
  B2. Input tax at 15% (B1 × 15/115)           ___________
  B3. Import VAT (SAD500)                      ___________
  B4. Imported services input (self-assessed)  ___________
  B5. Blocked input (entertainment, motor cars) ___________
  B6. Net input tax (B2+B3+B4 − B5)            ___________

C. NET VAT
  C1. Net VAT (A6 − B6)                         ___________
  C2. Prior period credit                       ___________
  C3. Net payable / (refund) (C1 − C2)          ___________

REVIEWER FLAGS:
  [ ] Tax invoices (Section 20) confirmed for all input claims?
  [ ] Entertainment and motor car inputs correctly blocked?
  [ ] Export evidence held for zero-rated supplies?
  [ ] Imported services self-assessed (output = input)?
  [ ] Basic foodstuffs correctly zero-rated?
  [ ] Rent — landlord VAT invoice confirmed?
```

#### Common South African bank statement formats

**Common South African bank statement formats**

| Bank | Key columns | Date format | Amount |
| --- | --- | --- | --- |
| FNB | Date, Description, Debit, Credit, Balance | DD Mon YYYY | ZAR with 2 decimals |
| Standard Bank | Date, Narrative, Debit, Credit, Balance | DD MMM YYYY | ZAR |
| ABSA | Date, Description, Amount, Balance | DD/MM/YYYY | ZAR |
| Nedbank | Date, Details, Debit, Credit, Balance | DD/MM/YYYY | ZAR |
| Capitec | Date, Description, Debit, Credit, Balance | YYYY-MM-DD | ZAR |

#### Key South African banking terms

**Key South African banking terms**

| Term | Meaning | Classification hint |
| --- | --- | --- |
| CREDIT | Incoming funds | Potential revenue |
| DEBIT | Outgoing payment | Potential expense |
| ATM WITHDRAWAL | Cash withdrawal | Tier 2 — ask |
| BANK CHARGES | Bank fee | Standard-rated (s 2(1) proviso) — claim input VAT |
| INTEREST EARNED | Interest received | Exempt |
| BALANCE | Running balance | Ignore |
| SALARY / WAGES | Payroll | Out of VAT scope |
| EFT / EFT DEBIT | Electronic fund transfer | Check direction |

### Section 9 — Onboarding fallback

```
SOUTH AFRICA VAT ONBOARDING — MINIMUM QUESTIONS
1. VAT registration number (10 digits starting with 4)?
2. Tax period covered by this bank statement?
3. Filing frequency: Category A or B bimonthly, C monthly, D six-monthly, E annual?
4. Do you have any exports (zero-rated)? Evidence held?
5. Do you have exempt income (financial services, residential rent)?
6. Does the business provide entertainment as its primary service?
   (Determines whether entertainment input tax is blocked)
7. Are any vehicles used exclusively for business goods transport?
8. Imported services (Google, Microsoft, etc.) — confirm for self-assessment
9. Prior period credit/refund amount to carry forward?
```

#### Key legislation

**Key legislation**

| Topic | Reference |
| --- | --- |
| VAT Act | Value-Added Tax Act No. 89 of 1991 |
| Standard rate | Section 7(1)(a) |
| Zero rate | Section 11; Schedule 2 |
| Exemptions | Section 12 |
| Input tax | Section 16 |
| Blocked input — entertainment | Section 17(2)(a) |
| Blocked input — motor cars | Section 17(2)(c) |
| Tax invoice | Section 20 |
| Imported services | Section 7(1)(c) |
| Penalties | Tax Administration Act No. 28 of 2011 |

#### Known gaps

- Partial exemption (Section 17(1)) apportionment — escalate
- Property going-concern zero-rating — escalate
- Financial services VAT — escalate
- Capital goods adjustments (Section 18A) — escalate

#### Self-check

- [ ] All tax invoices Section 20 compliant
- [ ] Entertainment and motor car inputs blocked
- [ ] Export zero-rating supported by evidence
- [ ] Imported services self-assessed
- [ ] Basic foodstuffs correctly split from 15% items
- [ ] Prior period credit carried forward

#### Changelog

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2024 | Initial |
| 2.0 | April 2026 | v2.0 rewrite: pattern library, worked examples, no inline tier tags |
| 2.1 | May 2026 | Validated by Werner Britz CA(SA); corrected registration threshold to R2.3m; corrected bank fees and payment processors to standard-rated; corrected VAT201 field structure; corrected Uber/Bolt to exempt; added motor car and entertainment blocks; fixed tax invoice thresholds; removed prescription medicines from zero-rated; fixed filing categories |

### Prohibitions

- NEVER allow input tax on entertainment expenses unless vendor's primary business is hospitality
- NEVER allow input tax on motor cars (passenger vehicles) used for mixed purposes
- NEVER zero-rate exports without evidence (customs documents, foreign payment records)
- NEVER allow input tax from a non-VAT-registered supplier
- NEVER self-assess imported services without recording both output and input in the same period
- NEVER present calculations as definitive — direct to a CA(SA) or registered tax practitioner
- NEVER claim input on the supply of a motor car as defined, unless within s 17(2)(c) exception
- NEVER claim input on entertainment unless vendor is in the entertainment trade or supply is employee subsistence
- NEVER exclude bank service fees as exempt -- they are standard-rated (s 2(1) proviso)
- NEVER omit output VAT on Seventh Schedule fringe benefits under s 18(3)


## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, chartered accountant (CA(SA)), or equivalent licensed practitioner in South Africa) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
