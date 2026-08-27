---
name: us-pl-86-272-income-tax-nexus
description: Tier 2 US federal content skill for Public Law 86-272 (15 USC §§381-384) — the federal statute that prevents states from imposing income tax on out-of-state sellers whose only activity is solicitation of tangible personal property orders shipped from out of state. Covers the 2021/2024 MTC revised statement that erodes P.L. 86-272 protection for nearly all internet-era activities (customer accounts, live chat, online reviews, post-sale service), California's FTB Legal Rulings 2022-01/02, New York's 2023 adoption, the Wisconsin v. Wrigley solicitation safe harbor, the factor-presence economic nexus model ($50k payroll, $500k receipts), and voluntary disclosure agreement processes. Tax year 2025.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Pl 86 272 Income Tax Nexus

## US Public Law 86-272 — State Income Tax Nexus Protection for Out-of-State Sellers of Tangible Personal Property

## 0. Scope and Limits

- **Public Law 86-272** — Federal statute (the "Interstate Income Act of 1959"), codified at 15 U.S.C. §§381–384, which limits a state's power to impose a net income tax on a person whose only business activity within the state is the solicitation of orders for sales of tangible personal property that are sent outside the state for approval and shipped or delivered from a point outside the state.  _(15 U.S.C. §§381-384)_

This is a federal nexus skill, not a state-tax-computation skill. It is read by accountants advising clients on:

- whether to register for and file a state income tax return in a particular state,
- whether a planned in-state activity (sales rep visit, trade show, FBA inventory, website chat) destroys P.L. 86-272 protection,
- whether the 2021/2024 Multistate Tax Commission ("MTC") revised statement on P.L. 86-272 has eroded protection for an e-commerce or hybrid client,
- whether an economic-nexus filing obligation exists independent of P.L. 86-272,
- whether to enter a voluntary disclosure agreement (VDA) to limit lookback exposure,
- and how to document the requirements for protection (approval outside the state, shipment from outside the state) in the working-paper file.

- **Scope inclusions - four statutory requirements** — The four statutory requirements (TPP, solicitation, out-of-state approval, out-of-state shipment).  _(15 U.S.C. §§381-384)_
- **Solicitation safe harbor per Wrigley** — The solicitation safe harbor as construed by Wisconsin Dep't of Revenue v. William Wrigley Jr. Co., 505 U.S. 214 (1992) — "solicitation of orders" + activities "entirely ancillary" to solicitation.  _(Wisconsin Dep't of Revenue v. William Wrigley Jr. Co., 505 U.S. 214 (1992))_
- **MTC Statement of Information** — The MTC Statement of Information ("Statement Concerning Practices of Multistate Tax Commission and Signatory States Under Public Law 86-272"), originally issued 1986, revised August 2021 and clarified through 2024, treats most internet-based activities as exceeding solicitation.  _(MTC Statement of Information, revised August 2021, clarified 2024)_
- **State adoption of MTC interpretation** — California (FTB Legal Ruling 2022-01 and FTB Legal Ruling 2022-02), New York (TSB-M-23 and Department guidance issued 2023), New Jersey (TB-108), Oregon, Minnesota, and the growing list of states incorporating MTC language into administrative guidance.  _(FTB Legal Ruling 2022-01, FTB Legal Ruling 2022-02, TSB-M-23, TB-108)_
- **Pending challenges to MTC interpretation** — The pending challenges: American Catalog Mailers Association v. Franchise Tax Board (California Superior Court, San Francisco County, Case No. CGC-22-601363 and successor matters) and parallel constitutional Commerce Clause arguments.  _(American Catalog Mailers Association v. Franchise Tax Board, Case No. CGC-22-601363)_
- **MTC Factor-presence economic nexus model** — $50,000 of property, $50,000 of payroll, $500,000 of receipts, or 25% of total property/payroll/receipts in the state USD  _(MTC Factor Presence Nexus Standard)_
- **Gross receipts taxes not protected by P.L. 86-272** — The interaction with state gross receipts taxes (Ohio CAT, Washington B&O, Oregon CAT, Nevada Commerce Tax, Texas Franchise Tax margin) — NOT protected by P.L. 86-272.  _(15 U.S.C. §381)_
- **Sales tax economic nexus separate regime** — The interaction with sales tax economic nexus under South Dakota v. Wayfair, 138 S. Ct. 2080 (2018) — entirely separate regime.  _(South Dakota v. Wayfair, 138 S. Ct. 2080 (2018))_

Combined / unitary reporting consequences once income tax nexus is established.

Voluntary disclosure agreement (VDA) mechanics: typical 3–4 year lookback, penalty waiver, anonymous front-loaded negotiation.

- **Scope exclusions (refusal catalogue)** — State sales tax registration, collection, remittance — see the relevant state sales tax skill (e.g., texas-sales-tax, california-sales-use-tax). Federal income tax computation under Subchapter C or Subchapter S — see us-form-1120-c-corp, the partnership skill, or the sole-prop skills. State-specific income tax return preparation — see ca-540-individual-return, ca-smllc-form-568, and other state skills. Foreign (non-U.S.) income tax nexus, permanent establishment, treaty-based positions — see treaty / PE skills. Property tax, payroll/withholding tax, unemployment insurance, occupational license — not covered. Local (city / county) income tax (e.g., Portland Multnomah BIT, New York City UBT, Philadelphia BIRT) — P.L. 86-272 does NOT apply to local income taxes, only state income taxes. If the client has Philadelphia or NYC exposure, refer the question out. Banks, insurance companies, common carriers — P.L. 86-272 explicitly excludes these from the protection it provides (15 U.S.C. §381(c)). Tax planning that crosses into a recommended-tax-shelter analysis under Circular 230 §10.35.  _(15 U.S.C. §381(c); Circular 230 §10.35)_

Assumed reviewer: A Circular 230 practitioner (EA, CPA, or attorney) admitted in at least one U.S. jurisdiction, who reviews and signs off on every output before it reaches the client or any state revenue department. This skill produces working-paper memoranda — not advice that goes directly to a taxpayer.

Tax year: 2025 (filings due in calendar year 2026 for calendar-year taxpayers). The MTC revised statement is treated as the current administrative interpretation; the pending ACMA litigation is treated as not-yet-resolved as of the last_updated date.

## 1. Background: The 1959 Statute and What It Was For

### 1.1 The Northwestern States Portland Cement crisis

- **Northwestern States Portland Cement Co. v. Minnesota** — The U.S. Supreme Court held that a state could constitutionally impose a properly apportioned net income tax on a foreign corporation whose only in-state activity was the regular solicitation of orders by employees, where the orders were sent out of state for approval and the goods shipped from out of state.  _(Northwestern States Portland Cement Co. v. Minnesota, 358 U.S. 450 (1959))_

The reasoning was that net income tax — unlike a sales tax, which falls on the transaction — was a tax on the privilege of earning income from in-state customers, and that the Commerce Clause did not forbid such a tax when properly apportioned.

The decision triggered a wave of taxpayer alarm. Companies that had previously believed themselves immune from state income tax discovered that any state in which a single sales rep regularly visited customers could impose tax. Industry associations lobbied Congress.

### 1.2 Congressional response

- **Enactment of P.L. 86-272** — Congress responded within months by enacting Public Law 86-272, the Interstate Income Act of 1959, signed September 14, 1959. The statute is short — three operative sections plus definitions — and is now codified at 15 U.S.C. §§381–384.  _(15 U.S.C. §§381-384)_

It is, by its terms, a temporary statute: §381 begins "No State, or political subdivision thereof, shall have power to impose, for any taxable year ending after the date of the enactment of this Act, a net income tax…" The statute was always understood as a stopgap pending congressional revision of the broader question of state taxation of interstate commerce. No comprehensive revision has occurred in the 66 years since enactment. The Willis Commission (1965) recommended sweeping reform; Congress did not act.

The statute therefore continues to govern, but the world it was drafted for — traveling salesmen taking paper orders for shipment of physical goods — has been largely supplanted by internet-mediated transactions in services, software, and digital products that lie entirely outside the statute's text.

### 1.3 What the statute actually says

- **15 U.S.C. §381(a) operative text** — No State, or political subdivision thereof, shall have power to impose, for any taxable year ending after September 14, 1959, a net income tax on the income derived within such State by any person from interstate commerce if the only business activities within such State by or on behalf of such person during such taxable year are either, or both, of the following: (1) the solicitation of orders by such person, or his representative, in such State for sales of tangible personal property, which orders are sent outside the State for approval or rejection, and, if approved, are filled by shipment or delivery from a point outside the State; and (2) the solicitation of orders by such person, or his representative, in such State in the name of or for the benefit of a prospective customer of such person, if orders by such customer to such person to enable such customer to fill orders resulting from such solicitation are orders described in paragraph (1).  _(15 U.S.C. §381(a))_
- **15 U.S.C. §381(c) exclusions** — (c) The provisions of subsections (a) and (b) shall not apply to the imposition of a net income tax by any State, or political subdivision thereof, with respect to — (1) any corporation which is incorporated under the laws of such State; or (2) any individual who, under the laws of such State, is domiciled in, or a resident of, such State.  _(15 U.S.C. §381(c))_
- **Net income tax definition** — Section 383 defines "net income tax" as "any tax imposed on, or measured by, net income."  _(15 U.S.C. §383)_
- **Four things that follow from the text** — 1. The protection covers net income tax only, and only when imposed by a state or political subdivision. 2. The protected activity is solicitation of orders — not sales themselves, not delivery, not service, not collection. 3. The orders must be for tangible personal property ("TPP") — not services, not intangibles, not real estate. 4. The orders must be approved out of state and shipped from out of state. The statute does not define "solicitation," does not define "tangible personal property," and does not address what happens when in-state activity exceeds mere solicitation.  _(15 U.S.C. §§381-384)_

## 2. The Four Requirements for P.L. 86-272 Protection

A taxpayer wishing to assert P.L. 86-272 protection against a state's income tax must establish all four of the following. The burden is on the taxpayer.

### 2.1 Requirement 1 — Sales of Tangible Personal Property Only

- **Tangible personal property (TPP)** — Property that has physical existence and can be touched or moved: widgets, books, machinery, parts, packaged consumer goods, chemicals, raw materials.  _(15 U.S.C. §381(a))_
- **Items NOT considered TPP** — Services (consulting, advertising, financial services, transportation services). Real estate transactions, rentals, leases of real property. Intangibles: software licenses (depending on state treatment — many states treat software as TPP, but many do not), patents, trademarks, royalties. Software-as-a-service (SaaS): almost universally treated as a service, not TPP. SaaS income is not within the P.L. 86-272 shelter. Cloud subscriptions, streaming media, digital downloads — treatment varies; many states treat as services or as a separate "digital products" category. Hybrid sales: if a single contract bundles TPP and a service, courts and state administrators generally apply a dominant-purpose or true-object test. If the service is dominant, the entire transaction is unprotected. If the TPP is dominant and the service is incidental, the TPP portion remains protected; the service portion does not.  _(15 U.S.C. §381(a))_

AUDIT FLASH POINT: A "software company" that sells both shrink-wrap CDs (TPP under most state law) and a SaaS subscription (service) cannot claim P.L. 86-272 over the SaaS line of business. If the company has any in-state activity supporting SaaS customers, the protection is lost as to that activity, and the state may assert that the company's entire in-state presence falls outside the shelter.

### 2.2 Requirement 2 — Solicitation of Orders In-State

- **Solicitation (Wrigley construction)** — "Speech or conduct that explicitly or implicitly proposes a sale" plus activities that are "entirely ancillary" to solicitation — meaning activities that serve no purpose apart from facilitating the solicitation.  _(Wisconsin Dep't of Revenue v. William Wrigley Jr. Co., 505 U.S. 214 (1992))_
- **Activities that are solicitation or ancillary (safe)** — Sales representatives' visits to existing or prospective customers to take orders. Displaying samples, demonstrating products. Distributing promotional materials, brochures, catalogs. Carrying free samples and giving them to customers (de minimis quantities consistent with sample-distribution purpose). Maintaining an in-state sample room used only for solicitation. Recruiting, training, and evaluating sales personnel whose function is solicitation. Maintaining records relating to in-state sales activity. Coordinating with out-of-state offices on customer orders. Carrying business cards, using company-branded vehicles for travel between customer visits.  _(Wisconsin Dep't of Revenue v. William Wrigley Jr. Co., 505 U.S. 214 (1992))_

### 2.3 Requirement 3 — Orders Approved Outside the State

- **Out-of-state approval requirement** — The orders solicited in-state must be transmitted out of state for approval or rejection. The in-state sales representative cannot have authority to bind the company contractually. A sales rep who can approve orders on the spot (signs the contract, sets pricing, finalizes terms) is conducting business beyond solicitation — and the protection is lost.  _(15 U.S.C. §381(a))_

Written sales-rep agreements should specify that the rep has no authority to accept orders. Order acknowledgments should be issued by the out-of-state home office. The order workflow should show transmission from rep → home office → acceptance. Pricing authority must rest at the home office for the protection to hold.

AUDIT FLASH POINT: State auditors routinely ask for the written sales-rep agreement, sample order forms, and the order-approval workflow. If the workflow shows in-state approval — even one example — the auditor will assert the protection is lost for the entire year.

### 2.4 Requirement 4 — Goods Shipped from Outside the State

- **Out-of-state shipment requirement and in-state inventory** — The goods must be shipped or delivered from a point outside the state. In-state inventory destroys protection. Inventory in a third-party logistics warehouse (3PL) located in the state: destroys protection. Inventory held on consignment with an in-state distributor: destroys protection. Fulfillment-by-Amazon (FBA) inventory stored in an Amazon facility located in the state: destroys protection in that state. Because Amazon moves FBA inventory between fulfillment centers without seller direction, an FBA seller can have inventory in 10–20 states without knowing it. FBA inventory locations are accessible from the seller's Amazon account. Drop-shipping from an out-of-state vendor: typically preserves protection (no in-state inventory ownership), but state-by-state analysis required. Demonstrator stock and samples held by sales reps: small quantities of samples consistent with the rep's solicitation function are generally permissible under the Wrigley "entirely ancillary" doctrine; quantities consistent with carrying salable inventory are not.  _(15 U.S.C. §381(a); Wisconsin Dep't of Revenue v. William Wrigley Jr. Co., 505 U.S. 214 (1992))_

AUDIT FLASH POINT: FBA sellers nearly always have lost P.L. 86-272 protection in every state where Amazon has stored their inventory. The seller's monthly Amazon inventory location report is discoverable and is now routinely requested by state revenue departments in income-tax nexus questionnaires.

## 3. The Wrigley Decision (1992) — the Bright Line

- **Wrigley holdings** — 1. "Solicitation of orders" covers only those activities that "explicitly or implicitly propose a sale." 2. The protection extends beyond literal solicitation to activities "entirely ancillary to requests for purchases" — meaning activities "that serve no independent business function apart from their connection to the soliciting of orders." 3. Activities that the company would engage in "anyway" — independent of solicitation — are not ancillary and fall outside the safe harbor, even if they also incidentally support solicitation. 4. A de minimis activity that does not establish a "nontrivial additional connection" with the state does not destroy the protection. The de minimis exception is narrow.  _(Wisconsin Dep't of Revenue v. William Wrigley Jr. Co., 505 U.S. 214 (1992))_
- **Activities Wrigley lost protection over** — Replacing stale gum at retail outlets from a stock of "agency stock" kept in cars. Supplying retailers with display racks from in-state storage. Storing the agency stock and display racks at the rep's home or rented in-state space. Each of these went beyond solicitation: they were activities the company would have to perform somewhere even if it had no salespeople — they served an independent business function (product distribution and merchandising) — and so they could not be characterized as "entirely ancillary" to solicitation.  _(Wisconsin Dep't of Revenue v. William Wrigley Jr. Co., 505 U.S. 214 (1992))_
- **Wrigley test as commonly applied** — An in-state activity preserves P.L. 86-272 protection if and only if it is either (a) literal solicitation of orders, or (b) an activity that serves no purpose apart from facilitating that solicitation. Any activity that the taxpayer would conduct independently of solicitation — even if it also helps solicitation along — defeats the protection.  _(Wisconsin Dep't of Revenue v. William Wrigley Jr. Co., 505 U.S. 214 (1992))_

This test is the dividing line between "solicitation safe harbor" activities and "beyond solicitation" activities, and it is the test the MTC revised statement applies (controversially) to internet activities.

## 4. Pre-Internet "Beyond Solicitation" Activities — Settled Law

- **Settled beyond-solicitation activities as of 2025** — Performing repairs or warranty service in-state by the sales rep or any agent. Approving or rejecting credit in-state (must be done at the out-of-state home office). Maintaining a stock of goods in-state — owned, consigned, or stored on the company's behalf. Collecting delinquent accounts in-state. Investigating credit-worthiness in-state. Conducting training classes for customers beyond product instruction incident to a sale. Repossessing property in-state. Hiring, training, or supervising personnel other than the sales force. Operating an in-state office open to the public — even a small office, even rented part-time, even a "home office" of the sales rep that has signage, a separate phone line, or business address. Maintaining a company-owned vehicle stocked with non-sample inventory. Picking up or replacing damaged or returned goods. Approving exchanges, returns, or replacements in-state. Use of independent contractors who function as employees — i.e., who solicit on the taxpayer's behalf and would be statutory agents under common-law tests. (Note: §381(d) provides a separate safe harbor for independent contractors doing business in their own name, but only as to solicitation; independent contractors doing more than solicit destroy the protection just as employees would.)  _(MTC 1986/2001 Statement; 15 U.S.C. §381(d))_
- **Activities that preserve protection (pre-internet doctrine)** — Carrying samples for display. Distributing literature. Soliciting orders (including by phone and mail from out of state, which by definition has no in-state connection). Coordinating shipping logistics in routine ways (e.g., providing a tracking number). Owning/using a personal vehicle, mobile phone, and laptop incident to solicitation. The sales rep's home — if no in-state office is held out to the public.  _(MTC 1986/2001 Statement)_

## 5. The 2021/2024 MTC Revised Statement — the Internet Erosion

### 5.1 What the MTC did

- **MTC history and 2021 revision** — The Multistate Tax Commission is an interstate compact organization. Its "Statement of Information Concerning Practices of Multistate Tax Commission and Signatory States Under Public Law 86-272" is non-binding model administrative guidance. The MTC originally issued the Statement in 1986, revised it in 1993 and 2001, and then issued a substantially revised version on August 4, 2021, with technical clarifications and updates carried into the 2024 edition. The 2021 revision did not change the four statutory requirements. It changed the MTC's view of how the Wrigley "entirely ancillary" test applies to internet activities. The MTC took the position that most things a business does on or through its website constitute in-state business activity in every state where customers access the website — because the customer's interaction with the website occurs in the customer's state — and that most such activities are not ancillary to solicitation of TPP orders.  _(MTC Statement of Information, revised August 4, 2021, clarified 2024)_

### 5.2 The new "in-state internet activities that exceed solicitation"

- **Internet activities classified as exceeding solicitation** — 1. Post-sale customer assistance via electronic chat or email initiated by clicking a website-based icon — including chat answering product-use questions, return/exchange questions, billing/payment questions. 2. Solicitation of branded credit cards for use across the entire enterprise (versus credit applications limited to the immediate sale of TPP). 3. Inviting and receiving applications for non-sales employment positions through the website (e.g., engineering, IT, customer service roles unconnected to the in-state sales force). 4. Placing internet "cookies" or similar technology onto the customer's computer or device that gather customer information used to adjust production schedules, develop new products, track inventory for which the cookie was not strictly related to soliciting that customer's order — i.e., cookies used for any purpose beyond optimizing the immediate sales transaction. 5. Remotely fixing or upgrading products previously sold by transmitting software updates or repairs over the internet to in-state customers. 6. Streaming videos or providing music or other content to in-state customers as part of a sale, where the content delivery is itself an activity the seller would conduct independently. 7. Offering an extended product warranty via the website to in-state customers. 8. Contracting with a marketplace facilitator (such as Amazon, eBay, Etsy) to facilitate sales of TPP to in-state customers, where the facilitator maintains inventory in-state on the seller's behalf. 9. Contracting with in-state customers to stream videos or music to electronic devices for a charge — i.e., a service offering bundled with TPP. 10. Maintaining a website that allows customers to upload product reviews, ratings, photographs, or videos, where the seller moderates that user-generated content. (Moderation is treated as an independent business activity.) 11. Customer log-in to manage a subscription, view order history, manage shipping addresses, store payment methods — anything that goes beyond placing the immediate order. 12. Online live chat with a sales representative that does not lead to an immediate order (where chat is used for general customer service).  _(MTC Statement of Information, revised August 4, 2021, clarified 2024)_
- **Internet activities classified as NOT exceeding solicitation** — A static website that presents catalog information and allows the customer to place orders. A website that allows customers to apply for credit limited to the purchase of TPP being solicited, where the application is approved out of state. Cookies that are strictly limited to remembering the customer's items in a shopping cart, language preferences, or storing the customer's order in progress. Telephone numbers and email addresses for the customer to place orders or ask questions about products being sold.  _(MTC Statement of Information, revised August 4, 2021, clarified 2024)_

### 5.3 The legal theory and the controversy

The MTC's theory is straightforward: under Wrigley, an in-state activity is protected only if it is "entirely ancillary" to solicitation. Customer service after a sale is by definition not ancillary to solicitation — it relates to a sale that already occurred. Therefore post-sale online customer service in a state is in-state business activity that exceeds solicitation, and the protection is lost.

The controversy is whether the customer's interaction with a website constitutes the seller's activity in the customer's state at all. Under longstanding nexus doctrine, a seller's activity must be physical or attributable to an agent in the state. A passive website hosted on out-of-state servers, accessed by an in-state customer, was historically not seller activity in the customer's state. The MTC's revised position effectively imputes the customer's interaction back to the seller, on the theory that the seller "purposefully avails itself" of the in-state market through interactive web functionality.

This theory has not been tested in the U.S. Supreme Court. Whether it survives constitutional review under the Commerce Clause and Due Process Clause is open.

### 5.4 Effective date and retroactivity

- **California adoption and retroactivity position** — California (FTB Legal Ruling 2022-01, issued February 14, 2022, and FTB Legal Ruling 2022-02, issued July 14, 2022): California has taken the position that its adoption of the MTC framework is clarifying rather than new law, and therefore applies to open tax years — California's statute of limitations is generally 4 years. California's FTB has been the most aggressive enforcer.  _(FTB Legal Ruling 2022-01 (Feb 14, 2022); FTB Legal Ruling 2022-02 (Jul 14, 2022))_
- **New York adoption** — New York (Department of Taxation and Finance, 2023 guidance): New York adopted the MTC framework prospectively from a 2023 administrative pronouncement; some auditors have asserted retroactive application.  _(New York Department of Taxation and Finance, 2023 guidance)_
- **New Jersey adoption** — New Jersey (TB-108, issued September 13, 2022): prospective adoption.  _(TB-108, issued September 13, 2022)_
- **Oregon, Minnesota, and others** — Oregon, Minnesota, and others: various positions, some prospective, some quasi-retroactive.

AUDIT FLASH POINT — California: The FTB has been opening audits going back to tax years 2018–2021, asserting that the MTC-style interpretation has always been the law. Taxpayers with California-customer-facing websites (customer accounts, live chat, online support) who have not filed California income tax returns should expect lookback exposure of 3–4 years plus interest, on the theory that they should have been filing all along. Voluntary disclosure becomes critical here — see Section 11.

AUDIT FLASH POINT — New York: NY's Department of Taxation and Finance has been issuing nexus questionnaires to out-of-state businesses identified through 1099-K reporting, marketplace facilitator reporting, and shipping/delivery records. The questionnaires routinely ask whether the business has live chat, customer accounts, online reviews, or app-based interactions — all "beyond solicitation" trigger answers under the MTC framework.

### 5.5 The ACMA challenge

- **ACMA v. FTB litigation status** — The American Catalog Mailers Association, joined by the National Federation of Independent Business and other trade groups, filed suit against California's FTB challenging the FTB's interpretation. The case was filed in California Superior Court (San Francisco County) and as of the last_updated date is pending through trial-court and intermediate-appellate stages, with no final decision binding the FTB. Parallel litigation has been filed or threatened in other states.  _(American Catalog Mailers Association v. Franchise Tax Board, Case No. CGC-22-601363)_
- **Substantive constitutional arguments** — The substantive constitutional argument is that the MTC interpretation: 1. Exceeds the statutory text of P.L. 86-272 by imputing the customer's actions to the seller; 2. Violates the Internet Tax Freedom Act (47 U.S.C. §151 note) by imposing a "discriminatory tax on electronic commerce" (treating internet activity differently from comparable non-internet activity that would still be solicitation); 3. Violates the Commerce Clause by lacking substantial nexus between the taxing state and the taxpayer's in-state activity.  _(47 U.S.C. §151 note (Internet Tax Freedom Act))_

Until the ACMA litigation reaches a final decision, accountants should treat the MTC interpretation as the operative administrative law in adopting states, while preserving the constitutional defenses as audit-defense positions and protective claims.

## 6. SaaS and Services — Outside P.L. 86-272 Entirely

- **Categories with no P.L. 86-272 shelter** — Software-as-a-Service (SaaS) — universally treated as a service in income-tax-nexus analyses, regardless of how the state characterizes it for sales tax. Platform-as-a-Service (PaaS), Infrastructure-as-a-Service (IaaS) — cloud computing services. Consulting, professional services, advertising, design services. Financial services, brokerage, insurance — also expressly excluded from P.L. 86-272 by §381(c). Subscription content services, streaming media, digital advertising. Royalties, licensing of intangibles (with the partial exception of canned software licensed as TPP under some state laws).  _(15 U.S.C. §381(c))_
- **SaaS company nexus exposure governance** — A SaaS company has no P.L. 86-272 protection in any state. Its nexus exposure is governed exclusively by: Constitutional nexus under Wayfair (substantial nexus through some virtual or economic presence); State economic-nexus statutes for income tax (see Section 7); and Physical-presence factors (employees, contractors, real property, inventory).  _(South Dakota v. Wayfair, 138 S. Ct. 2080 (2018))_

AUDIT FLASH POINT — SaaS companies: A SaaS company that has not filed state income tax returns in any state where it has customers should not rely on P.L. 86-272 as a shield. There is none. The only question is whether the SaaS company has crossed economic nexus thresholds in particular states. Many SaaS companies cross the $500,000 receipts threshold in 10+ states within their first year of meaningful revenue.

## 7. The Economic Nexus Alternative Path

Even before the MTC's internet erosion of P.L. 86-272, states had been developing an alternative income-tax nexus theory: economic nexus, in which the seller's substantial economic presence in the state — measured by sales, payroll, or property — is sufficient to satisfy the constitutional substantial-nexus requirement, without any physical presence.

### 7.1 Pre-Wayfair history

- **Geoffrey, Inc. v. South Carolina Tax Commission** — The leading pre-Wayfair income-tax economic nexus case is Geoffrey, Inc. v. South Carolina Tax Commission, 437 S.E.2d 13 (S.C. 1993), which upheld South Carolina's imposition of income tax on a Delaware holding company licensing the "Toys R Us" trademark to in-state stores, despite the holding company having no physical presence. Several states adopted similar positions through the 1990s and 2000s.  _(Geoffrey, Inc. v. South Carolina Tax Commission, 437 S.E.2d 13 (S.C. 1993))_

### 7.2 Wayfair and its income-tax aftermath

- **Wayfair and income tax implications** — South Dakota v. Wayfair, 138 S. Ct. 2080 (2018), overruled the physical-presence requirement of Quill Corp. v. North Dakota for sales tax. Although Wayfair did not directly address income tax, its constitutional reasoning — that the Commerce Clause's substantial-nexus requirement does not require physical presence — applies to net income tax as well. In the years following Wayfair, states have adopted income-tax economic nexus statutes or administrative positions. By 2025 most states with a corporate income tax assert some form of economic nexus.  _(South Dakota v. Wayfair, 138 S. Ct. 2080 (2018))_

### 7.3 The MTC Factor Presence Model

- **MTC Factor Presence Nexus Standard thresholds** — A taxpayer is deemed to have nexus in a state if any of the following exists in the state during the tax year: Property of $50,000 or more, or Payroll of $50,000 or more, or Receipts of $500,000 or more, or 25% of the taxpayer's total property, total payroll, or total receipts in the state. USD  _(MTC Factor Presence Nexus Standard (model statute))_
- **State variants of Factor Presence model** — Variants of the Factor Presence model have been adopted by: California — $711,538 in receipts, $71,154 in property, $71,154 in payroll, or 25% of total (2025 indexed amounts — verify against current FTB Pub 1050; thresholds are annually inflation-adjusted under R&TC §23101(b)). California also retains the doing-business rule under R&TC §23101(a). Colorado, Connecticut, Massachusetts, Michigan, New York, Ohio (CAT), Oregon, Tennessee, Washington (B&O) — variant thresholds, generally aligning with the $500,000 receipts trigger. Texas (Franchise Tax) — $500,000 in Texas gross receipts triggers franchise tax filing under R&TC §171.001, even for entities with no Texas physical presence. Hawaii — $100,000 sales OR 200 transactions for income tax under Act 221 (2019).  _(R&TC §23101(a); R&TC §23101(b); R&TC §171.001; Hawaii Act 221 (2019); FTB Pub 1050)_

### 7.4 Critical interaction with P.L. 86-272

**P.L. 86-272 vs Economic Nexus Interaction Table**  _(Section 7.4 Critical interaction with P.L. 86-272)_

| Scenario | P.L. 86-272 Applies? | Economic Nexus Applies? | Result |
| --- | --- | --- | --- |
| TPP sales only, all four requirements met, no MTC-prohibited internet activity | Yes | Overridden | Protected; no income tax return required |
| TPP sales only, all four requirements met, customer accounts + chat on website | Yes (but lost under MTC interpretation in adopting states) | Yes, if thresholds met | Income tax return required in MTC-adopting states; protected in non-adopting states |
| SaaS sales | No (services) | Yes, if thresholds met | Income tax return required |
| Mixed TPP + SaaS | Partially — only TPP shielded | Yes for SaaS portion | Filing required on SaaS income; TPP income may still be shielded |
| TPP sales with in-state employee doing repairs | No (beyond solicitation regardless of MTC) | Yes | Income tax return required |
| TPP sales with FBA inventory in-state | No (in-state inventory destroys shelter) | Yes | Income tax return required |

### 7.5 Non-income state taxes that P.L. 86-272 does NOT shelter

- **P.L. 86-272 shelters only net income tax** — P.L. 86-272 shelters only net income tax. It does not protect against: Gross receipts taxes: Ohio Commercial Activity Tax (CAT), Washington Business & Occupation (B&O) Tax, Oregon Corporate Activity Tax, Nevada Commerce Tax, San Francisco Gross Receipts Tax. Even a TPP-only solicitation-protected seller may owe these. Texas Franchise (Margin) Tax: a margin-based tax that the Texas comptroller treats as not a net income tax for P.L. 86-272 purposes — Texas asserts the margin tax falls outside the federal shelter (a position upheld in Combs v. Newpark Resources, Inc., 422 S.W.3d 46 (Tex. App. — Austin 2013, no pet.) and successor cases). Minimum franchise/privilege taxes: California's $800 minimum franchise tax under R&TC §23153 applies to corporations qualified to do business; the FTB has historically asserted it can apply even to P.L. 86-272-protected entities that are "doing business" in California. Capital stock taxes (Pennsylvania, Tennessee, others — varying). Sales tax, use tax — entirely separate regime governed by Wayfair and state economic nexus. Payroll/withholding tax — separate; triggered by employees physically working in the state. Property tax — separate; based on situs of property. Local income/business taxes (NYC UBT, Philadelphia BIRT, Portland Multnomah BIT) — federal preemption applies to state income tax under §381; whether municipalities are covered varies by jurisdiction and is contested.  _(15 U.S.C. §381; Combs v. Newpark Resources, Inc., 422 S.W.3d 46 (Tex. App. — Austin 2013, no pet.); R&TC §23153)_

AUDIT FLASH POINT — Ohio CAT & Washington B&O: Out-of-state TPP-only sellers who believe they are P.L. 86-272-protected may still owe Ohio CAT (if $150,000+ in Ohio gross receipts under the bright-line test, raised to $3M for tax periods after 2024) and Washington B&O (if $100,000+ in Washington gross receipts). These are not net income taxes and are not within the federal shelter.

## 8. Combined / Unitary Reporting Consequences

Once a member of a corporate group establishes income tax nexus in a combined-reporting state, the consequences cascade beyond that single entity.

### 8.1 Combined reporting basics

- **Combined reporting definition and states** — A combined-reporting state requires all members of a unitary business group (related entities operating an integrated business) to file a single return reporting combined income apportioned by the group's combined apportionment factor. The combined-reporting states include California, Illinois, Michigan, Massachusetts, Minnesota, New York, Oregon, Texas (for franchise tax), Utah, and others.

### 8.2 The "nowhere income" trap

- **Nowhere income trap** — If one entity in a corporate group has income tax nexus in a combined-reporting state, the entire combined group's income is generally subject to apportionment in that state, including the income of entities that are themselves P.L. 86-272-protected. The result is that even a protected entity's income gets pulled into the combined tax base.

### 8.3 Joyce vs. Finnigan

- **Joyce rule** — Joyce rule (named for Appeal of Joyce, Inc., Cal. State Bd. of Equalization 1966): include in the in-state sales factor numerator only the receipts of group members who themselves have nexus in the state. P.L. 86-272-protected members' sales are excluded from the numerator. Joyce is favorable to taxpayers.  _(Appeal of Joyce, Inc., Cal. State Bd. of Equalization 1966)_
- **Finnigan rule** — Finnigan rule (named for Appeal of Finnigan Corp., Cal. State Bd. of Equalization 1990): include in the numerator the receipts of any group member's sales to the state, regardless of whether the selling member is itself nexus-having. Finnigan is unfavorable to taxpayers.  _(Appeal of Finnigan Corp., Cal. State Bd. of Equalization 1990)_
- **States applying Finnigan rule** — California, New York, Massachusetts, Oregon, and several others apply the Finnigan rule (or its equivalent). This means a sister company with no in-state activity at all may have its sales pulled into the in-state sales numerator simply because another group member has nexus.

AUDIT FLASH POINT — Combined Filers: Establishing income tax nexus in California or New York for one entity in a corporate group may pull the entire group's relevant sales into the in-state sales numerator under Finnigan-rule allocation, dramatically increasing the in-state apportionment ratio.

## 9. Practical Planning Under the Post-MTC Regime

### 9.1 The website audit

- **Website audit checklist** — Every client selling TPP and asserting P.L. 86-272 protection should have its website audited for "beyond solicitation" features under the MTC interpretation. The audit checklist: 1. Does the website have a customer login / customer account function? (Beyond solicitation.) 2. Does the website have a live chat widget? Is the chat used post-sale? (Beyond solicitation if used for service rather than the immediate sales pitch.) 3. Does the website host product reviews, photos, or videos uploaded by customers, and is that content moderated by the seller? (Beyond solicitation.) 4. Does the website allow subscription management, return initiation, warranty registration, service ticketing? (Beyond solicitation.) 5. Does the website stream branded content, host product-instructional videos, provide remote software updates? (Beyond solicitation, per MTC.) 6. Does the website set cookies beyond shopping-cart persistence and language preferences? Are cookies used for analytics, retargeting, A/B testing, customer profiling? (Beyond solicitation, per MTC.) 7. Does the website solicit job applications for non-sales positions? (Beyond solicitation.) 8. Does the website offer branded credit cards for general use? (Beyond solicitation.) 9. Does the website host an app that customers download for non-ordering purposes? (Beyond solicitation if non-solicitation functionality.) A client whose website fails any of the above is presumptively outside P.L. 86-272 protection in California, New York, and other MTC-adopting states.

### 9.2 The website remediation playbook (theoretical)

Some companies have explored "geo-fencing" — blocking MTC-state residents from accessing the offending features. This is technically possible but commercially impractical for most businesses. More realistic strategies:

- Move the offending features off the seller-branded website to a third-party platform (e.g., a community forum hosted by an independent association), severing the direct connection to the seller.
- Document a conservative-tax-filing posture: register and file in MTC-adopting states, claim minimal apportionment, position the P.L. 86-272 defense as a protective claim preserved by the filing.
- Adjust the entity structure: place the website and customer-service operations in a separate entity from the TPP-selling entity, so that the TPP entity itself has no in-state internet activity. (Substance and unitary-business doctrine constrain this.)

### 9.3 In-state activity documentation

- **Working-paper file contents** — For any state in which P.L. 86-272 is being claimed, the working-paper file should contain: A written description of the in-state business activity (sales rep visits, frequency, products sold). The sales-rep agreement showing the rep has no authority to bind. The order-approval workflow with date-stamped acknowledgments issued out of state. Shipping records showing all shipments originated outside the state. The website audit documentation (see 9.1). A memorandum to file explaining the protection claim, the four requirements, and any contestable points.

### 9.4 Order workflow design

- **Order workflow design for new clients** — For new clients establishing operations: Centralize order approval at a single out-of-state location. Use written sales contracts that require home-office signature for binding effect. Use shipping carriers that originate outside the customer's state (drop-ship from out-of-state vendor; central fulfillment facility outside the customer's state). Do not use FBA in states where P.L. 86-272 protection is asserted; or accept that FBA states are filing states. Do not have sales reps perform any post-sale function. Do not have sales reps approve credit, accept returns, or take service calls.

## 10. Sales Tax Economic Nexus — Brief Contrast

- **Post-Wayfair sales tax economic nexus thresholds** — $100,000 in sales OR 200 transactions (South Dakota original); or $500,000 (California, New York, Texas) USD  _(South Dakota v. Wayfair, 138 S. Ct. 2080 (2018))_

Although P.L. 86-272 does not protect against sales tax, the sales-tax economic nexus regime (post-Wayfair) interacts with the income-tax analysis often enough to warrant a brief note.

A taxpayer with sales tax nexus in a state typically also has state revenue-department visibility in that state (through marketplace facilitator reports, 1099-K filings, or sales tax registrations). State income tax auditors increasingly cross-reference sales tax registrations against income tax filings: a taxpayer registered for sales tax in a state but not filing income tax is a flagged audit candidate.

AUDIT FLASH POINT — Sales tax to income tax cross-reference: Clients should expect that registering for sales tax in a state will trigger a nexus questionnaire on income tax within 18–36 months. The two regimes are converging in state revenue-department practice.

## 11. Voluntary Disclosure Agreements (VDAs)

- **Voluntary disclosure agreement (VDA)** — A contract between the taxpayer and a state revenue department under which the taxpayer voluntarily reveals previously-unreported tax liability in exchange for limited lookback and penalty waiver.

### 11.1 Typical VDA terms

- **Typical VDA terms** — Lookback period: usually 3–4 years (some states 5–6). Without VDA, the state may assert a back-to-when-nexus-was-established lookback of 7+ years, plus penalties at 25–50% and interest. Penalty waiver: full waiver of late-filing and late-payment penalties. Interest: typically NOT waived; interest accrues on the unpaid tax from the original due date. Confidentiality: many VDAs allow the taxpayer to negotiate anonymously through counsel or an MTC representative until the deal is signed. Future compliance: the taxpayer commits to register, file, and pay going forward.

### 11.2 When a VDA is the right answer

- **Situations favoring a VDA** — Client discovers it has been operating in a state for many years with unrecognized nexus (e.g., FBA inventory, post-MTC internet activity, undisclosed sales rep activity). The state has not yet contacted the client. The client's potential exposure exceeds the cost of voluntary disclosure (typically the case if 5+ years of liability would otherwise be assessed). The client wants to clean up before a transaction (M&A diligence frequently surfaces state nexus issues).

### 11.3 When a VDA is NOT available

- **Situations where VDA unavailable** — The state has already contacted the client (nexus questionnaire, audit letter). The client is already registered in the state. The taxpayer has fraudulently concealed tax liability.

### 11.4 The MTC Multistate Voluntary Disclosure Program

- **MTC National Nexus Program / Multistate Voluntary Disclosure Program** — The MTC operates a National Nexus Program / Multistate Voluntary Disclosure Program that allows a taxpayer to negotiate VDAs with multiple states simultaneously through one MTC-administered process. The taxpayer files one application, anonymously, identifying the states and tax types. The MTC coordinates with each state. Many states participate. This is the standard channel for clients with exposure in 5+ states.

AUDIT FLASH POINT — Pre-acquisition diligence: State income tax nexus is one of the most-frequently-found findings in M&A diligence. A target company that has sold to customers in 30 states without filing in any may face a multi-million-dollar exposure that requires VDAs or escrow provisions in the deal. Begin the analysis 6–9 months before the closing.

## 12. Worked Examples

### 12.1 Example 1 — Pre-internet CD Software Seller (Still Protected)

**Facts:** ClassicShrinkWrap Inc. is a Delaware-incorporated company headquartered in Phoenix, AZ. It sells boxed shrink-wrapped CDs of utility software to retail computer stores nationwide. Five sales representatives travel the country visiting retailers. Reps take written orders and fax them to the Phoenix home office, where the credit department approves the orders and the warehouse ships the CDs by UPS. The company's "website" is a one-page brochure with the corporate phone number and email — no ordering, no customer accounts, no chat, no cookies beyond a session cookie, no reviews. Customers who want to buy call the 800 number and place an order with a Phoenix-based call center.

**Analysis:**

1. **TPP only?** Yes — boxed software CDs are TPP under all relevant state laws.
2. **Solicitation?** Yes — sales reps solicit; they have no authority to approve.
3. **Approval out of state?** Yes — Phoenix home office approves all orders.
4. **Shipped from out of state?** Yes — all shipments originate from Phoenix.

**Internet erosion?** The static one-page website with no customer-facing functionality does not fall within any MTC "beyond solicitation" category. Session cookies for cart persistence are explicitly safe.

**Other nexus triggers?** No in-state employees beyond traveling reps; no in-state inventory; no in-state offices. Each rep works from a personal vehicle; rep home addresses are not held out as company offices.

**Conclusion:** ClassicShrinkWrap is **protected by P.L. 86-272** in every state where it has only this activity profile, including California and New York. It owes no state net income tax (subject to the gross-receipts-tax and minimum-franchise-tax exceptions of Section 7.5 — e.g., it still owes California's $800 minimum franchise tax if it is "doing business" in California for §23101(a) purposes, and may owe Ohio CAT if Ohio gross receipts exceed the threshold).

**Working-paper memo:** Document the four requirements with copies of (a) sample order forms, (b) the rep agreement, (c) the approval workflow, (d) the website snapshot. Renew annually.

### 12.2 Example 2 — SaaS Startup (Zero P.L. 86-272 Protection)

**Facts:** CloudHelm LLC is a Delaware-formed LLC, taxed as a partnership, with its only office in Austin, TX. It sells a project-management SaaS application by subscription. Customers sign up online, pay by credit card, and access the application through a web browser. No physical product is shipped. Revenue in 2025 was $8.2 million, with customers in all 50 states. California customer revenue was $2.1 million; New York customer revenue was $1.4 million.

**Analysis:**

1. **TPP only?** No. SaaS is a service in every state's income-tax characterization. P.L. 86-272 does not apply at all.

**Economic nexus?** Yes — CloudHelm exceeds the receipts threshold in many states:

- **California**: $2.1M > $711,538 threshold → income tax nexus under R&TC §23101(b)(2).
- **New York**: $1.4M > $1,138,000 threshold (or whatever 2025-indexed amount applies) → likely nexus under Article 9-A.
- **Texas**: state of formation? No — Delaware. State of headquarters? Texas. Texas Franchise Tax applies based on $500,000 receipts threshold and based on Texas commercial domicile.
- Additional states will likely cross thresholds.

**Conclusion:** CloudHelm has **no P.L. 86-272 shelter**. It must analyze each state for economic-nexus filing obligations and is likely required to file in 10+ states. As a partnership (LLC taxed as partnership), it must also consider pass-through entity (PTE) tax elections in each state (see `us-pte-state-matrix`).

**Action items:**

- Conduct state-by-state nexus analysis, calculate apportioned income for each, register and file.
- Evaluate VDA for states where CloudHelm has had nexus for prior years without filing.
- Evaluate PTE-elections to allow members to deduct state tax federally.

### 12.3 Example 3 — E-commerce TPP Seller (Lost Protection Post-MTC)

**Facts:** GardenGoods Direct Inc. is a Nevada-incorporated corporation headquartered in Reno, NV. It sells gardening supplies (seeds, tools, fertilizers — all TPP) through its website, gardengoods.com. The website features:

- Customer accounts (sign in, view order history, manage subscriptions for seed-of-the-month club, store payment methods).
- Product reviews uploaded by customers (moderated by a Reno-based content team).
- Live chat staffed by a Reno call center that handles both pre-sale questions and post-sale customer service (returns, replacements, shipping issues).
- Cookies for retargeting and personalized product recommendations.
- Mobile app that allows customers to track shipments and reorder.

Goods ship from a single warehouse in Reno. No in-state offices, employees, or inventory in any other state. 2025 revenue: $15 million, with California customers generating $3.2M, New York $2.1M, New Jersey $1.5M, Oregon $700K.

**Analysis under pre-MTC law (1959–2021):**

1. TPP? Yes.
2. Solicitation only in customer states? Yes — no employees outside Nevada.
3. Approval outside customer state? Yes — order processing in Reno.
4. Shipped from outside customer state? Yes — Reno warehouse.

Under pre-MTC law, GardenGoods would have been comfortably P.L. 86-272-protected in all states.

**Analysis under MTC interpretation (post-2021):**

The website features:

- **Customer accounts**: beyond solicitation (per MTC category #11).
- **Moderated reviews**: beyond solicitation (per MTC category #10).
- **Live chat for post-sale service**: beyond solicitation (per MTC categories #1 and #12).
- **Retargeting cookies**: beyond solicitation (per MTC category #4).
- **App for tracking/reorder**: beyond solicitation if the app does more than place an order — the tracking functionality is independent of the soliciting function.

**State-by-state outcome:**

- **California (FTB Legal Rulings 2022-01 and 2022-02):** Protection **lost**. GardenGoods exceeds the receipts threshold ($3.2M > $711,538). California income tax return required. **Lookback potentially extends 4 years**.
- **New York:** Protection **lost** under 2023 administrative guidance. NY filings required.
- **New Jersey:** Protection **lost** under TB-108. NJ filings required.
- **Oregon:** Protection **lost** under Oregon's adoption of MTC framework. OR filings required.
- **Non-adopting states:** GardenGoods's protection survives in states that have not adopted the MTC framework (varies year-to-year — verify state-by-state).

**Action items:**

- Quantify exposure: estimate apportioned income for each MTC-adopting state, calculate tax + interest + penalty for open years.
- Pursue MTC multistate VDA for all unfiled MTC-adopting states.
- Conduct a website remediation review: can functionality be moved off the seller's domain or geo-fenced? Cost-benefit analysis.
- Consider the constitutional preservation: file protectively, attach a P.L. 86-272 / Internet Tax Freedom Act / Commerce Clause protective claim, monitor ACMA litigation.

> **AUDIT FLASH POINT — Lookback exposure:** California asserts the MTC interpretation is **clarifying** and applies retroactively to all open years (4-year statute). For GardenGoods, with $3.2M annual California receipts, the protective filings should cover **2021–2025 inclusive**. The cost of a VDA limiting lookback to 3 years versus an audit assessment covering 4+ years can be six-figure-meaningful.

### 12.4 Example 4 — Amazon FBA Seller (Multi-State Inventory)

**Facts:** ToolWorks LLC is a single-member LLC owned by a Texas-resident individual. It manufactures specialty hand tools in San Antonio, TX, and sells exclusively through Amazon's FBA program. ToolWorks ships its inventory to Amazon, which redistributes it across Amazon fulfillment centers in CA, AZ, NV, TX, IL, GA, PA, NJ, NY, and FL throughout the year. ToolWorks has no employees outside Texas, no website beyond its Amazon storefront, no sales reps, no in-state offices.

**Analysis:**

1. **TPP?** Yes — physical hand tools.
2. **Solicitation only?** Amazon arguably solicits on ToolWorks's behalf — but more importantly, Amazon **maintains inventory** in each fulfillment-center state.
3. **Approval out of state?** Orders are processed through Amazon's system; from ToolWorks's perspective the order workflow originates with Amazon's facilities in the customer state.
4. **Shipped from outside the state?** **NO.** This is the dispositive failure. FBA inventory is physically located in the fulfillment-center state, and Amazon ships from that in-state warehouse to the in-state customer.

The fourth requirement is failed in **every state where Amazon has stored ToolWorks's inventory**.

**Conclusion:** ToolWorks has **lost P.L. 86-272 protection** in CA, AZ, NV, IL, GA, PA, NJ, NY, FL (every FBA state). Whether it has economic nexus depends on apportioned receipts; with multi-state inventory plus sales the seller almost certainly has both **physical** and **economic** nexus.

Additionally:

- Sales tax nexus in every FBA state (Wayfair plus marketplace facilitator laws — though most marketplace facilitator laws make Amazon, not ToolWorks, the collecting party; but ToolWorks may still need to register for income tax separately).
- Each state's income tax filing obligation must be evaluated.
- For Texas: ToolWorks is a Texas-resident sole proprietor with a disregarded SMLLC; federal income flows on Schedule C. Texas has no state income tax but ToolWorks is subject to Texas Franchise Tax.

**Action items:**

- Pull Amazon's FBA inventory location reports for prior years.
- Quantify state-by-state nexus exposure.
- File MTC multistate VDA for all FBA-state income taxes.
- Reconcile income tax exposure with marketplace facilitator sales tax positions.

> **AUDIT FLASH POINT — FBA inventory reports:** Amazon's Inventory Event Detail report by state is requested in nearly every state revenue department's FBA-seller nexus audit. The report typically shows inventory in 10+ states for any active seller. Sellers asserting P.L. 86-272 protection in any FBA state should expect that defense to fail.

## 13. Quick-Reference Decision Tree

```
START: Is the in-state activity TPP-sales-related?
│
├─ NO (services, SaaS, real estate, intangibles)
│   └─ P.L. 86-272 does NOT apply. Analyze economic nexus directly.
│
└─ YES (TPP sales)
    │
    ├─ Is there ANY in-state inventory (FBA, 3PL, consignment, in-state warehouse)?
    │   └─ YES → Protection LOST in that state. Analyze economic nexus.
    │
    └─ NO in-state inventory.
        │
        ├─ Is order approval made in-state (sales rep authorized to bind)?
        │   └─ YES → Protection LOST. Analyze economic nexus.
        │
        └─ NO — approval is at out-of-state home office.
            │
            ├─ Is there any in-state activity beyond solicitation
            │  (repairs, credit approval, collection, in-state office, post-sale service)?
            │   └─ YES → Protection LOST. Analyze economic nexus.
            │
            └─ NO traditional "beyond solicitation" activity.
                │
                ├─ Does the website have customer accounts, live chat,
                │  moderated reviews, retargeting cookies, post-sale support,
                │  or other MTC-listed "beyond solicitation" internet activities?
                │   │
                │   ├─ YES, AND the state has adopted MTC interpretation
                │   │   (CA, NY, NJ, OR, MN, etc.):
                │   │     → Protection LOST. Analyze economic nexus.
                │   │       Consider VDA for prior years.
                │   │
                │   └─ NO, OR state has not adopted MTC:
                │       → Protection PRESERVED.
                │       → Document the four requirements in working papers.
                │       → Still owe gross-receipts taxes (Ohio CAT, WA B&O),
                │         minimum franchise taxes (CA $800), and similar.
```

## 14. Provenance and Citations

- **Primary federal statute** — Interstate Income Act of 1959, Pub. L. No. 86-272, 73 Stat. 555, codified at 15 U.S.C. §§381–384.  _(15 U.S.C. §§381–384)_
- **Northwestern States Portland Cement Co. v. Minnesota** — Constitutional power upheld; triggered P.L. 86-272.  _(Northwestern States Portland Cement Co. v. Minnesota, 358 U.S. 450 (1959))_
- **Wisconsin Dep't of Revenue v. William Wrigley Jr. Co.** — Controlling interpretation of "solicitation of orders" and "entirely ancillary" activities.  _(Wisconsin Dep't of Revenue v. William Wrigley Jr. Co., 505 U.S. 214 (1992))_
- **Quill Corp. v. North Dakota** — Physical-presence requirement for sales tax — overruled by Wayfair.  _(Quill Corp. v. North Dakota, 504 U.S. 298 (1992))_
- **South Dakota v. Wayfair, Inc.** — Overruling Quill; constitutional foundation for state economic nexus.  _(South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018))_
- **Internet Tax Freedom Act** — Prohibition on discriminatory taxes on electronic commerce.  _(47 U.S.C. §151 note, P.L. 105-277)_
- **Geoffrey, Inc. v. South Carolina Tax Commission** — Economic nexus for intangibles.  _(Geoffrey, Inc. v. South Carolina Tax Commission, 437 S.E.2d 13 (S.C. 1993))_
- **Combs v. Newpark Resources, Inc.** — Texas Margin Tax not a net income tax for P.L. 86-272.  _(Combs v. Newpark Resources, Inc., 422 S.W.3d 46 (Tex. App. — Austin 2013))_
- **California FTB Legal Ruling 2022-01** — Internet activities under P.L. 86-272.  _(California FTB Legal Ruling 2022-01 (Feb. 14, 2022))_
- **California FTB Legal Ruling 2022-02** — Clarification.  _(California FTB Legal Ruling 2022-02 (Jul. 14, 2022))_
- **New York Department of Taxation and Finance administrative guidance** — 2023 administrative guidance.  _(New York Department of Taxation and Finance administrative guidance, 2023)_
- **New Jersey TB-108** — New Jersey guidance on P.L. 86-272 internet activities.  _(New Jersey TB-108 (Sept. 13, 2022))_
- **Appeal of Joyce, Inc.** — Joyce rule for combined-group apportionment.  _(Appeal of Joyce, Inc., Cal. State Bd. of Equalization 1966)_
- **Appeal of Finnigan Corp.** — Finnigan rule.  _(Appeal of Finnigan Corp., Cal. State Bd. of Equalization 1990)_

**American Catalog Mailers Association v. Franchise Tax Board**, Cal. Super. Ct. (San Francisco County), Case No. CGC-22-601363 and successor matters — pending as of `last_updated`.

- **MTC Statement of Information Concerning Practices of Multistate Tax Commission and Signatory States Under Public Law 86-272** — Revised August 4, 2021, with 2024 technical clarifications.  _(MTC Statement of Information Concerning Practices of Multistate Tax Commission and Signatory States Under Public Law 86-272, revised August 4, 2021, with 2024 technical clarifications)_
- **MTC Factor Presence Nexus Standard for Business Activity Taxes** — Model statute (2002).  _(MTC Factor Presence Nexus Standard for Business Activity Taxes, model statute (2002))_
- **MTC National Nexus Program / Multistate Voluntary Disclosure Program** — Ongoing.  _(MTC National Nexus Program / Multistate Voluntary Disclosure Program, ongoing)_

- `us-form-1040-individual-return` — Schedule C sole proprietor flow.
- `us-form-1120-c-corp` — C-corporation income tax computation.
- `us-form-1065-partnership` — partnership income flow-through.
- `us-pte-state-matrix` — state pass-through entity tax election framework.
- `ca-540-individual-return`, `ca-smllc-form-568` — California taxpayer-side compliance.
- `texas-sales-tax`, `tx-franchise-tax` — Texas state tax companions.
- `california-sales-use-tax` — California sales/use tax companion.
- `us-tax-workflow-base` — Tier 1 workflow runbook (load first).

All output of this skill must be reviewed and signed off by a Circular 230 practitioner (EA, CPA, or attorney) before delivery to the taxpayer or any state revenue department. The MTC interpretation is contested; constitutional defenses should be preserved in protective filings; voluntary disclosure decisions involve material commercial judgment beyond the scope of this skill.

**Skill version:** 0.1. **Last updated:** 2025-11-15. **Verified by:** pending. The pending status reflects (a) ACMA litigation not yet final, (b) ongoing state adoption of the MTC framework, and (c) annual updates required as states publish indexed economic-nexus thresholds.

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
