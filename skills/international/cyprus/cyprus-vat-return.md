---
name: cyprus-vat-return
description: "Use this skill for Cyprus VAT (Φ.Π.Α.) in tax year 2026 (law at 24 October 2026). It covers the 19% standard rate, the 9%, 5% and 3% reduced rates, the temporary 0% on basic goods (baby milk, nappies, feminine hygiene products and listed fruit and vegetables to 31 December 2027; meat and fish 6 April 2026 to 31 May 2027; bread, milk, coffee, sugar and baby food 12 October 2026 to 31 May 2027), household electricity and home solar rates, property VAT, partial exemption, cash accounting, the EUR 15,600 registration threshold, the EUR 10,000 EU distance-sales threshold, quarterly returns and payment by the 10th of the second month, return boxes 1 to 11B, VIES by the 15th, domestic reverse charge (construction, scrap, phones and laptops, precious metals, property in loan restructuring), TFA filing, the EUR 100 late-return charge, 10% additional tax and interest. Trigger on: Cyprus VAT, Φ.Π.Α., VAT return Cyprus, TFA VAT, Cyprus reverse charge, VIES Cyprus. Out of scope: corporate tax (cy-corporate-tax), income tax (cyprus-income-tax), payroll (cyprus-payroll), cross-border income tax (cy-cross-border)."
jurisdiction: CY
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 2.1
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cyprus VAT return: rates, registration, the return and penalties (2026)

This skill sets out who must charge Cyprus VAT (Φόρος Προστιθέμενης Αξίας, Φ.Π.Α.), at what rate, how to fill in and file the periodic VAT return, and what late filing and late payment cost, as the law stands on 24 October 2026. The law is the VAT Law 95(I)/2000 as amended up to Law 109(I)/2026 and order Κ.Δ.Π. 221/2026, with the VAT (General) Regulations Κ.Δ.Π. 314/2001. The tax authority is the Tax Department (Τμήμα Φορολογίας) of the Ministry of Finance. Use it with `vat-workflow-base` (workflow) and `eu-vat-directive` (EU rules).

What changed for 2026:
- Order Κ.Δ.Π. 337/2025 zero-rates baby milk, children's and adult nappies, feminine hygiene products and listed fresh fruit and vegetables from 1 January to 31 December 2026.
- Order Κ.Δ.Π. 362/2026 (16 October 2026) repeats that 0% from 1 January to 31 December 2027.
- Order Κ.Δ.Π. 168/2026 zero-rated fresh and frozen meat, fish, cuttlefish, squid and octopus from 6 April to 30 September 2026. Order Κ.Δ.Π. 354/2026 (30 September 2026) continues that 0% from 1 October 2026 to 31 May 2027.
- Order Κ.Δ.Π. 354/2026 also zero-rates bread, milk, coffee, sugar and baby food from 12 October 2026 to 31 May 2027.
- Order Κ.Δ.Π. 363/2026 (16 October 2026) adds home solar (photovoltaic) systems for household self-consumption to the 9% rate.
- Orders Κ.Δ.Π. 82/2026 and 167/2026 cut VAT on household electricity (tariffs 01, 02, 08 and 56): 9% for April 2026 meter readings, 5% for readings from 1 May 2026 to 31 March 2027.
- Orders Κ.Δ.Π. 102/2026 and 103/2026 redefine "first establishment" for new buildings and renovations from 1 September 2026.
- Law 223(I)/2025 keeps the reverse charge on property transferred in loan restructuring in force to 31 December 2026.
- Law 104(I)/2025 brought in the EU small business scheme (SME-SS) from 1 January 2025.
- The 3% rate is not new for 2026. It dates from Law 75(I)/2023 (art. 18Β, Fifteenth Schedule).

## Who this applies to

- **Businesses established in Cyprus.** A person making taxable supplies must register at the end of any month in which its taxable supplies (standard, reduced and zero rated) in the past 12 months passed **EUR 15,600**, or at any time when there are reasonable grounds to expect that supplies in the next 30 days will pass EUR 15,600 (First Schedule, Part I, para. 1; Tax Department registration page). Sales of capital assets are left out of the count.
- **Notice and start date.** Under the 12-month test the business must notify within 30 days of the end of the month in which it passed the threshold; registration runs from the end of the following month or an agreed earlier date. Under the 30-day test it must notify before the end of the 30 days, and registration runs from the start of them. The obligation exists whether or not the business applied: the Commissioner can register it back to the date it became liable, and it owes VAT on its supplies from that date.
- **No threshold for B2B services to other EU states.** A person that supplies services to taxable persons in another member state, where the customer accounts for the VAT, must register from the first such supply and file VIES.
- **Non-established businesses.** A business not established in Cyprus that makes taxable supplies in Cyprus where the customer does not account for the VAT must register as soon as it intends to make them.
- **Acquisitions of goods from other EU states.** A person not otherwise registered (for example an exempt business) must register once its acquisitions from other member states in the calendar year pass **EUR 10,251.61**, or are expected to within the next 30 days.
- **Voluntary registration** is open below the thresholds and to an intending trader.
- **Citrus growers.** A person whose only taxable supplies are zero-rated citrus (lemons, oranges, mandarins, grapefruit, citron) is not required to register but may ask to (First Schedule, Part I, para. 1(1Α)).
- **Deregistration.** A registered person may be removed from the register if it satisfies the Commissioner that its taxable supplies in the coming year will not pass **EUR 13,668.81**. It must notify the end of its taxable activity within 60 days.
- **Summarised here, but refer the computation:** the special schemes (cash accounting, SME-SS, OSS and IOSS, the margin schemes, investment gold, the farmers' scheme, the urban taxi scheme, the tour operators' scheme), partial exemption, and immovable property including the 5% main-residence rate. Ship management is out of this skill.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate (art. 17) | 19% | 2026 | https://www.cylaw.org/nomoi/enop/non-ind/2000_1_95/full.html |
| Reduced rate (art. 18Α, Twelfth Schedule): taxi, tourist, excursion and intercity bus transport; restaurant and catering; hotel and holiday accommodation; domestic sea passenger transport; old people's homes (non-exempt supplies) | 9% | 2026 | https://www.cylaw.org/nomoi/enop/non-ind/2000_1_95/full.html |
| Reduced rate (art. 18, Fifth Schedule): food and drinks except alcohol, beer, wine and soft drinks; water; bottled gas; medicines and vaccines; fertilisers, animal feed and seeds; contraceptives; medical equipment for disabled people; child car seats; urban and rural buses; renovation of private homes (materials up to 50% of value); main residence on conditions; and the other Fifth Schedule items | 5% | 2026 | https://www.cylaw.org/nomoi/enop/non-ind/2000_1_95/full.html |
| Super-reduced rate (art. 18Β, Fifteenth Schedule, from Law 75(I)/2023): books, newspapers and magazines (print and e-format); talking books, wheelchairs, orthopaedic and hearing devices for disabled people; street cleaning, refuse and waste treatment (not by local authorities); sewage; admission to the first performance of theatre, music and dance works | 3% | 2026 | https://www.cylaw.org/nomoi/enop/non-ind/2000_1_95/full.html |
| Zero rate (art. 25, Sixth Schedule): exports; sea-going ships and airline aircraft; international passenger transport to the extent carried out in Cyprus | 0% | 2026 | https://www.cylaw.org/nomoi/enop/non-ind/2000_1_95/full.html |
| Temporary 0%: baby milk, children's and adult nappies, feminine hygiene products, listed fresh fruit and vegetables (Sixth Schedule paras 13 to 15, 25(α) and 25(β)) | 0% from 1 Jan to 31 Dec 2026 | 2026 | https://www.cylaw.org/KDP/data/2025_1_337.pdf (para. 4) |
| Temporary 0%: baby milk, nappies, feminine hygiene products, listed fresh fruit and vegetables, continued | 0% from 1 Jan to 31 Dec 2027 | 2027 | https://www.cylaw.org/KDP/data/2026_1_362.pdf (para. 4) |
| Temporary 0%: fresh and frozen meat and offal, fish, cuttlefish, squid and octopus (Sixth Schedule paras 25(γ) and 25(δ)) | 0% from 6 Apr to 30 Sep 2026, then continued from 1 Oct 2026 to 31 May 2027; 5% food rate before 6 Apr 2026 | 2026 | https://www.cylaw.org/KDP/data/2026_1_168.pdf (para. 4); https://www.cylaw.org/KDP/data/2026_1_354.pdf (para. 4(α)) |
| Temporary 0%: bread, milk, coffee, sugar and baby food (Sixth Schedule para. 25(ε)) | 0% from 12 Oct 2026 to 31 May 2027; 5% food rate before | 2026 | https://www.cylaw.org/KDP/data/2026_1_354.pdf (para. 4(β)) |
| Home solar (photovoltaic) systems of household customers, for self-consumption in their homes (Twelfth Schedule para. 6) | 9% from the order's publication on 16 Oct 2026 (it states no other start date) | 2026 | https://www.cylaw.org/KDP/data/2026_1_363.pdf |
| Household electricity, tariffs 01, 02, 08 and 56 | 9% for readings from 1 Apr 2026 until the 9% entry was deleted on 30 Apr 2026; 5% for readings 1 May 2026 to 31 Mar 2027 | 2026 | https://www.cylaw.org/KDP/data/2026_1_82.pdf; https://www.cylaw.org/KDP/data/2026_1_167.pdf |
| 5% main residence: first 130 m² of buildable area, up to this value | EUR 350,000 | 2026 | https://www.cylaw.org/nomoi/enop/non-ind/2000_1_95/full.html (Fifth Schedule, Table Γ) |
| 5% main residence: lost entirely if total value passes / total buildable area passes | EUR 475,000 / 190 m² | 2026 | https://www.cylaw.org/nomoi/enop/non-ind/2000_1_95/full.html (Fifth Schedule, Table Γ) |
| Registration threshold, established business | EUR 15,600 (past 12 months or next 30 days) | 2026 | https://www.gov.cy/mof-tax/documents/eggrafi-akyrosi-f-p-a/eggrafes-mitrooy-f-p-a/ypochreosi-dikaioma-eggrafis-sto-mitroo-f-p-a/ |
| Registration threshold, acquisitions from other EU states | EUR 10,251.61 a calendar year | 2026 | https://www.gov.cy/mof-tax/documents/eggrafi-akyrosi-f-p-a/eggrafes-mitrooy-f-p-a/ypochreosi-dikaioma-eggrafis-sto-mitroo-f-p-a/ |
| Deregistration threshold | EUR 13,668.81 for the coming year | 2026 | https://www.gov.cy/mof-tax/documents/dikaiomata-kai-ypochreoseis/ |
| EU distance sales and TBE services: below this, VAT stays in the seller's state (art. 10(4Α)) | EUR 10,000 EU-wide, current and previous calendar year | 2026 | https://www.cylaw.org/nomoi/enop/non-ind/2000_1_95/full.html |
| EU small business scheme (SME-SS): EU-wide turnover cap | EUR 100,000 | 2026 | https://www.cylaw.org/nomoi/arith/2025_1_104.pdf |
| Retailer must issue a VAT invoice if a taxable customer asks and the price passes | EUR 85 | 2026 | https://www.gov.cy/mof-tax/documents/dikaiomata-kai-ypochreoseis/ |
| Errors in past returns that may be corrected in the current return (net total, periods under three years old) | Up to EUR 1,708.60 | 2026 | https://www.gov.cy/mof-tax/documents/ypovoli-tropopoiisi-diloseon-f-p-a/sychnes-erotiseis-se-schesi-me-tis-diorthoseis-lathon/ |
| Gifts of goods: output VAT due when cost per gift passes | EUR 17 | 2026 | Tax Department return guide (URL in Sources) |

## The taxable base

- **What is taxed.** Supplies of goods and services in Cyprus for consideration, acquisitions of goods from other member states and imports (art. 17). The rate is 19% unless a schedule names another one. Anything the Fifth, Twelfth, Fifteenth or Sixth Schedule does not list takes 19%.
- **Rate traps.**
  - Taxis and intercity or tourist buses are at 9%. Urban and rural buses are at 5%.
  - Books, newspapers and magazines are at 3%, not 5%.
  - Food is at 5%, but alcohol, beer, wine and soft drinks are at 19%. Food served with support services (a restaurant) is at 9%.
  - Meat and fish stay at 0% after 30 September 2026: Κ.Δ.Π. 354/2026 continues the 0% from 1 October 2026 to 31 May 2027. Bread, milk, coffee, sugar and baby food are at 5% up to 11 October 2026 and 0% from 12 October 2026 to 31 May 2027. Baby milk, nappies, feminine hygiene products and the listed fruit and vegetables are at 0% to 31 December 2026 (Κ.Δ.Π. 337/2025) and again for 2027 (Κ.Δ.Π. 362/2026). The Tax Department rates page (read 24 October 2026) still says all basic goods are at 0% only "μέχρι και 30/9/2026". The orders in the Gazette win over the page.
  - Split every basic-goods sale by date: 6 April 2026 (meat and fish), 12 October 2026 (bread, milk, coffee, sugar, baby food), 31 May 2027 (both end).
  - The same rates page lists only tariff 08 electricity at 5%. Orders Κ.Δ.Π. 82/2026 and 167/2026 cover tariffs 01, 02, 08 and 56. Follow the orders.
- **Renovation at 5%.** Renovation and repair of a private home by plumbers, electricians, carpenters, painters and builders is at 5%, except where materials are more than 50% of the value of the service (Fifth Schedule, Table Β, para. 11; energy and structural upgrades, para. 11Α). From 1 September 2026 a home counts as "old" when at least three years have passed since first establishment, and "first use" means systematic use for at least 18 months (Κ.Δ.Π. 102/2026).
- **Main residence at 5%.** The purchase or building of a main and permanent residence is at 5% on the first 130 m² of buildable area, up to EUR 350,000. If the total value passes EUR 475,000 or the total buildable area passes 190 m², the whole amount is at 19%. A disabled person gets 190 m² whatever the total area. Families with more than three children get 15 m² more per extra child. The buyer files a declaration with the Commissioner (Fifth Schedule, Table Γ). If the home stops being the main residence within ten years, the owner must tell the Commissioner within 30 days and pay the difference; the Tax Department issues a VAT Return for Special Cases. Refer every case.
- **Exempt supplies (Seventh Schedule).** Among others: services of Cyprus Post as a public body; medical care by recognised professionals; education by recognised schools; insurance; credit, bank account and other financial services; lotteries and betting. Card processing, clearing and authorisation, and collecting third parties' debts, are at 19% (Tax Department exemptions page). Exempt sales carry no VAT and give no right to deduct.
- **Input VAT.** VAT on purchases used for taxable supplies is deductible under art. 21 if the business holds a tax invoice dated in the period. Mixed taxable and exempt use is apportioned under regs 64 to 65Γ of Κ.Δ.Π. 314/2001 (refer). Credit notes received reduce Box 4.
- **Partial exemption** (regs 64 and 65 of Κ.Δ.Π. 314/2001). A business with both taxable and exempt sales deducts in full the input VAT on costs used only for taxable sales, nothing on costs used only for exempt sales (or for non-business activity), and on shared costs the proportion that taxable sales bear to all sales in the period. The ratio leaves out sales of the business's capital goods, incidental property and financial transactions, and self-supplies, and is rounded up to the next whole percentage. The Commissioner may approve or direct another method. The deduction in each return is provisional (reg. 64(1)). Refer the annual adjustment and any special method.
- **Input VAT that must not go in Box 4** (return guide): private purchases; business entertainment of employees or company managers; second-hand goods bought under the second-hand scheme; payments to the Tax Department under an assessment. The Tax Department's 2001 General VAT Guide also blocks VAT on ordinary passenger cars (not taxis, hire cars, driving-school cars, vans, vehicles with more than ten seats or over three tonnes) and on business entertainment generally. That guide predates the current law, so this skill keeps the conservative default: block, ask, refer.
- **Output VAT that is easy to miss** (return guide): reverse-charge services and purchases; commission on sales for third parties; sales of fixed assets; goods taken for private use; self-billed invoices; bad-debt relief later recovered; and gifts of goods costing more than EUR 17 each. Credit notes issued reduce Box 1.

### Property

- **Letting** of immovable property is exempt (Eighth Schedule para. 1(α)), except: hotel and similar accommodation; parking spaces; fixed equipment and machinery; safes; hire-purchase of property that is itself taxable; and the letting of property to a taxable person for its taxable business, other than as a home (para. 1(α)(vi)). That last letting is taxed at 19% for leases starting on or after the 2017 amending law (No. 3) came into force, unless the landlord tells the Commissioner it opts out of taxing it. The opt-out cannot be reversed later. Since 3 April 2026 the opt-out is made on the form set by Commissioner's notice Κ.Δ.Π. 172/2026, filed through TFA.
- **Sales** of immovable property are exempt (para. 1(β)) except: new buildings, or parts of them with their land, transferred before first establishment (first use); and undeveloped building land meant for building, transferred in the course of an economic activity. These are at 19%, or 5% for a qualifying main residence. From 1 September 2026 the meaning of first establishment changed (Κ.Δ.Π. 102/2026 and 103/2026). Refer every property sale.

### Special schemes

- **Cash accounting (art. 42Ε).** Output VAT is due when the business is paid, and input VAT is deductible when it pays. Open from the start of any tax period if supplies in the previous 12 months did not pass **EUR 25,000**, all returns were filed and paid on time, all assessed tax is paid, and the business has no conviction under art. 46. Some transactions are left out of the scheme (art. 42Ε(3)); refer.
- **EU small business scheme (SME-SS, Law 104(I)/2025, from 1 January 2025).** A business established in another member state can use the Cyprus exemption if its turnover in Cyprus does not pass **EUR 15,600** and its EU-wide annual turnover does not pass **EUR 100,000**. A Cyprus business can use another state's exemption under the same EUR 100,000 EU-wide cap. Refer.
- **Others (refer):** OSS and IOSS, the margin schemes, investment gold, the farmers' scheme, the urban taxi scheme, the tour operators' scheme.

### Domestic reverse charge

The customer, not the supplier, accounts for the VAT on:
- construction, conversion, demolition, repair and maintenance of buildings and civil engineering works, including services supplied with goods, to a business customer (art. 11Β);
- used metals and scrap supplied to a registered buyer whose activity code is 46771 (art. 11Γ);
- transfers of buildings, building land and related rights by a borrower in a loan restructuring or forced transfer to the lender (art. 11Δ), in force to 31 December 2026 (art. 61(3), as extended by Law 223(I)/2025);
- mobile phones, integrated circuit devices (microprocessors and CPUs before they go into end-user products), game consoles, tablets and laptops supplied to a taxable person (art. 11Ε);
- raw and semi-finished precious metals, outside the margin and investment-gold schemes (art. 11ΣΤ);
- gas and electricity supplied by a business established outside Cyprus to a registered person (art. 11Α).

The supplier invoices without VAT. The buyer enters output VAT in Box 1, deducts it in Box 4 under art. 21, and puts the value in Boxes 6 and 7. Records of these transactions must be kept for six years (art. 11Γ(6), 11Ε(5)). Failing to apply the reverse charge costs EUR 200 per tax period, up to EUR 4,000 in total (art. 45(7Β)).

### The return boxes

From the Tax Department's guide to completing the VAT return (file name 06082024). The guide predates the OSS; where it says MOSS, read OSS.

| Box | Meaning |
|---|---|
| 1 | VAT on outputs: sales, plus VAT self-assessed on services from abroad and on domestic reverse-charge purchases |
| 2 | VAT on acquisitions of goods (and linked services) from other EU member states |
| 3 | Total VAT due (Box 1 + Box 2) |
| 4 | Input VAT deductible this period, including on EU acquisitions and reverse-charge purchases |
| 5 | VAT payable or repayable (Box 3 - Box 4) |
| 6 | Total outputs without VAT, including Boxes 8A, 8B, 9, 10 and 11B |
| 7 | Total inputs without VAT, including Boxes 11A and 11B |
| 8A | Supplies of goods (and linked services) to other EU member states |
| 8B | Services to taxable persons in other EU member states where the customer accounts for the VAT |
| 9 | Zero-rated outputs other than 8A and 8B, exports included |
| 10 | Out-of-scope sales with the right to deduct (other than 8B), including triangular sales and OSS sales |
| 11A | Acquisitions of goods (and linked services) from other EU member states |
| 11B | Services received from taxable persons in other EU member states |

Where things go:
- Services from another EU state (place of supply Cyprus, art. 11): output VAT in Box 1 (not Box 2), input in Box 4, value in Boxes 6, 7 and 11B.
- Services from outside the EU: output VAT in Box 1, input in Box 4, value in Boxes 6 and 7. Nothing in 11B.
- Goods from another EU state: output VAT in Box 2, input in Box 4, value in Boxes 7 and 11A. The tax point is the earlier of the supplier's invoice and the 15th day of the month after dispatch.
- Imports from outside the EU: VAT paid at import in Box 4; value in Box 7.
- Exports and other zero-rated sales: Boxes 9 and 6. EU B2B goods: 8A and 6. EU B2B services: 8B and 6. Both go on VIES.
- Exempt sales go in Box 6 only. Exempt purchases go in Box 7 only.
- Triangular sales as the middle supplier: purchase value in Box 7, sale value in Boxes 6 and 10.

Format rules: Boxes 1 to 5 are amounts with two decimals and a comma as the decimal sign, no thousands separators, a minus sign for a negative, "0" when empty. Boxes 6 to 11B are rounded to whole euro. Box 3 must equal Box 1 + Box 2, and Box 5 must equal Box 3 - Box 4. Box 6 must be at least 8A + 8B + 9 + 10 + 11B, and Box 7 at least 11A + 11B. Leave out of Box 6: capital put in, loans, dividends, insurance claims and share dealing (unless a financial institution). Leave out of Box 7: wages, contributions to funds, money donations, interest, dividends, taxes and fees. A negative Box 5 is a credit: carry it forward, set it off against other tax, or claim it on form 4B with the return if the refund conditions are met.

### Classifying a bank statement

Defaults when a fact is missing: unknown sale rate 19%; unknown purchase status not deductible; unknown counterparty country Cyprus; unknown EU customer status B2C with Cyprus VAT; unknown business use no recovery; unknown SaaS billing entity non-EU reverse charge; unknown blocked status blocked; unknown scope in scope. Flag for the reviewer any large single item, any default that moves the VAT due materially, one counterparty dominating the quarter, many defaults in one quarter, and a large net payable or repayable.

| Pattern on the statement | Treatment |
|---|---|
| Bank fees: Bank of Cyprus, Hellenic Bank, RCB, Eurobank Cyprus, Astrobank; Revolut, Wise, N26 fee lines | Exempt: no input VAT, value in Box 7. Check for taxable subscription invoices |
| Interest (tokoi), loan principal (daneio), dividends (merisma), own transfers, salaries (misthos), Social Insurance, Tax Department, Registrar of Companies | Exclude from the return |
| EAC electricity | 19% for business tariffs; household tariffs as in the rates table |
| Water Board | 5% |
| CYTA, Epic, PrimeTel telecoms; lawyers, accountants, notaries | 19% |
| Insurers (General Insurance Cyprus, CNP Cyprialife, Allianz, Atlantic) | Exempt: no input VAT, value in Box 7 |
| Cyprus Post | Exempt. Private couriers (Akis Express, ACS) at 19%. DHL: check the billing entity |
| Taxis, intercity buses | 9%. Urban and rural buses 5%. Airlines: no Cyprus VAT unless the ticket shows it |
| Supermarkets, restaurants | Block by default (private provisioning, entertainment); ask who and why |
| Google, Microsoft, Adobe, Meta, LinkedIn, Dropbox, Slack, Zoom (Irish entities), Spotify (SE), Atlassian (NL), AWS EMEA (LU) | EU reverse charge: Boxes 1, 4, 6, 7, 11B |
| Notion, Anthropic, OpenAI, Figma (US), Canva (AU); GitHub unless billed from the EU | Non-EU reverse charge: Boxes 1, 4, 6, 7 |
| Stripe, PayPal fees | 19% reverse charge (11B when billed from the EU) unless the invoice shows an exempt payment service |
| Rent (enoikio) | 19% only if the invoice shows VAT; otherwise no input VAT; refer property questions |
| Fuel, cars | No recovery by default; ask vehicle type and business use |
| ATM and cash withdrawals | Exclude by default; ask the purpose |

Bank exports from Bank of Cyprus and Hellenic Bank usually use comma delimiters and DD/MM/YYYY dates. Greek words to recognise: enoikio (rent), misthos (salary), tokoi (interest), metafora (transfer). An IBAN starting CY is Cyprus; IE, DE, NL and other EU prefixes are EU; US and GB are outside the EU.

## Deadlines and filing

- **Tax periods.** Usually quarterly, set at registration from the business's activity code; the Commissioner may allow or require monthly periods (Κ.Δ.Π. 314/2001 reg. 17). Quarters are not always calendar quarters: the official calendar shows quarters such as May to July and June to August.
- **Return and payment.** By the 10th day after the end of the month that follows the end of the period (reg. 17). Examples from the official calendar: quarter January to March 2026 due 10 May 2026; April to June 2026 due 10 August 2026; May to July 2026 due 10 September 2026. A deadline on a weekend or public holiday moves to the next working day.
- **Where.** Electronically through Tax For All (TFA). Before the deadline a business can amend its own return in TFA. Boxes 6 to 11B of a return whose deadline is after 27 March 2023 can be amended in TFA by the business; older returns need a written request.
- **Correcting errors.** Errors in earlier returns go in the current period's VAT account under reg. 24 only if the net total of all errors found is not more than EUR 1,708.60 and the period is less than three years old. The net total sets under-declared output VAT and over-claimed input VAT against over-declared output VAT and under-claimed input VAT. Otherwise the business writes to the Tax Department through TFA.
- **VIES recapitulative statement.** Monthly, by the 15th day after the end of each month in which the business supplied goods or services to a person registered in another member state (art. 42Γ(2)). A corrective statement is due within one month of the end of the month it concerns.
- **Records and invoices.** Keep records as the Tenth Schedule para. 5 and regs 22 and 23 require. A retailer must issue a VAT invoice to a taxable customer who asks for one when the price passes EUR 85 (reg. 14).

## Penalties and interest

| Failure | Charge | Source |
|---|---|---|
| Late notification of the obligation to register | EUR 85 for each month the failure lasts | VAT Law art. 45(1) |
| Return not received by the deadline | EUR 100 per return | VAT Law art. 45(2) |
| VAT shown on a return not paid by the deadline, or VAT assessed by the Commissioner | Additional tax of 10% of the VAT due | VAT Law art. 45(3) |
| Interest on VAT subject to the 10% | 9% a year from the day the VAT became due | VAT Law art. 45(4) |
| Reverse charge not applied (arts 11 to 11Ε, 12Α) | EUR 200 per tax period, at most EUR 4,000 | VAT Law art. 45(7Β) |
| VIES statement not received by the deadline | EUR 50 | VAT Law art. 45Β |
| VIES statement wrong and not corrected in time | EUR 15 | VAT Law art. 45Α(1) |
| Not issuing a legal receipt to a consumer | Up to 20% of the transaction value | Tax Department rights and obligations page |

The Tax Department VAT return FAQ confirms the EUR 100 charge, the 10% additional tax and default interest for a missing return, and says TFA also raises an estimated assessment. The EUR 51 late-return figure sometimes quoted is not the law in force: art. 45(2) says EUR 100.

## Cross-border points

- **EU B2B services out:** no Cyprus VAT; Boxes 8B and 6; VIES. Check the customer's VAT number in VIES before invoicing.
- **EU B2B goods out:** 0%; Boxes 8A and 6; VIES.
- **EU distance sales of goods and TBE services to consumers:** while the EU-wide total stays within EUR 10,000 in the current and previous calendar year, Cyprus VAT applies; above it, VAT is due in the customer's state, usually through the OSS (art. 10(4Α)). Refer OSS and IOSS work.
- **Non-established businesses** register as soon as they make taxable supplies in Cyprus where the customer does not self-account.
- **EU small business scheme (Law 104(I)/2025, from 1 January 2025):** a Cyprus business with EU turnover up to EUR 100,000 can use another state's exemption, and a business from another state can use the Cyprus exemption. Refer.
- **Imports:** VAT is paid at customs and claimed in Box 4.
- **Passenger transport:** domestic sea passenger transport is at 9%; international passenger transport is 0% to the extent it takes place in Cyprus.

## Worked examples

### Example 1: a Limassol consultancy's January to March 2026 return

A registered consultancy in Limassol sells EUR 40,000 of consulting to Cyprus clients in January to March 2026, all at 19%. It buys Google Ads from Google Ireland Ltd for EUR 2,000 (an EU service, so the business reverse-charges it) and has Cyprus purchase invoices showing EUR 3,800 of input VAT, all for its taxable business.

Output VAT on sales is 40,000 x 19% = EUR 7,600. The Google service adds 2,000 x 19% = EUR 380 to Box 1 and the same EUR 380 to Box 4. Box 1 is EUR 7,980. Box 4 is 3,800 + 380 = EUR 4,180. Box 5 is EUR 3,800. Box 6 includes the EUR 2,000 service as well as the EUR 40,000 of sales, and Boxes 7 and 11B include the EUR 2,000. The return and payment are due on 10 May 2026.

```oa-check
name: Limassol consultancy, Q1 2026, 19% sales plus an EU reverse-charge service
inputs:
  sales: 40000
  google_ads: 2000
  domestic_input_vat: 3800
steps:
  - vat_sales: sales * 19 / 100
  - vat_reverse_charge: google_ads * 19 / 100
  - box_1: vat_sales + vat_reverse_charge
  - box_4: domestic_input_vat + vat_reverse_charge
  - box_5: box_1 - box_4
expected:
  vat_sales: 7600
  vat_reverse_charge: 380
  box_1: 7980
  box_4: 4180
  box_5: 3800
```

### Example 2: a grocer's August to October 2026 quarter, filed and paid late

A Nicosia grocer has a quarter running August to October 2026. Its sales, without VAT, are: fresh fish EUR 30,000 in August and September and EUR 10,000 in October; listed fresh fruit and vegetables EUR 20,000 across the quarter; bread and milk EUR 12,000 from 1 August to 11 October and EUR 4,000 from 12 to 31 October; other food EUR 50,000; soft drinks EUR 8,000. Input VAT on purchase invoices is EUR 3,000.

Fish is at 0% for the whole quarter: to 30 September under Κ.Δ.Π. 168/2026 and from 1 October under Κ.Δ.Π. 354/2026. The fruit and vegetables are at 0% (Κ.Δ.Π. 337/2025 runs to 31 December 2026). Bread and milk are at the 5% food rate up to 11 October, 12,000 x 5% = EUR 600, and at 0% from 12 October (Κ.Δ.Π. 354/2026). Other food is at 5%: EUR 2,500. Soft drinks are excluded from the food rate, so 19%: EUR 1,520. Output VAT is 600 + 2,500 + 1,520 = EUR 4,620 and Box 5 is 4,620 - 3,000 = EUR 1,620.

The return and payment were due on 10 December 2026. The grocer files and pays in January 2027. The late return costs EUR 100 (art. 45(2)) and the late payment adds 10% of the VAT due, EUR 162 (art. 45(3)): EUR 262 before interest at 9% a year (art. 45(4)).

```oa-check
name: Grocer, Aug-Oct 2026, basic goods split by date, late return and payment
inputs:
  fish_aug_sep: 30000
  fish_oct: 10000
  fruit_veg: 20000
  bread_milk_to_11_oct: 12000
  bread_milk_from_12_oct: 4000
  other_food: 50000
  soft_drinks: 8000
  input_vat: 3000
  late_return_charge: 100
steps:
  - vat_fish: (fish_aug_sep + fish_oct) * 0 / 100
  - vat_fruit_veg: fruit_veg * 0 / 100
  - vat_bread_milk_5: bread_milk_to_11_oct * 5 / 100
  - vat_bread_milk_0: bread_milk_from_12_oct * 0 / 100
  - vat_food: other_food * 5 / 100
  - vat_drinks: soft_drinks * 19 / 100
  - output_vat: vat_fish + vat_fruit_veg + vat_bread_milk_5 + vat_bread_milk_0 + vat_food + vat_drinks
  - vat_payable: output_vat - input_vat
  - additional_tax: vat_payable * 10 / 100
  - charges_before_interest: late_return_charge + additional_tax
expected:
  vat_fish: 0
  vat_bread_milk_5: 600
  vat_food: 2500
  vat_drinks: 1520
  output_vat: 4620
  vat_payable: 1620
  additional_tax: 162
  charges_before_interest: 262
```

## Ask the client first

- Which tax period does the VAT registration certificate show (quarter ending which month, or monthly)?
- Do you make any exempt supplies (financial services, insurance, medical care, education, letting)? If so, refer for partial exemption.
- Do you sell to customers in other EU countries, and are they businesses with VAT numbers or consumers? (Boxes 8A and 8B, VIES, the EUR 10,000 distance-sales threshold.)
- Which entity bills you for services and goods from abroad? (Box 1 or Box 2, and 11A or 11B.)
- Do you buy or sell construction work, scrap metal, phones, laptops, tablets or consoles, or precious metals? (Domestic reverse charge.)
- Did you sell meat, fish, bread, milk, coffee, sugar, baby food, baby milk, nappies, hygiene products or fruit and vegetables in the period, and on which dates? Have you found errors in earlier returns, and what is their net total?

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Law 95(I)/2000, consolidated to Law 109(I)/2026 and Κ.Δ.Π. 221/2026 (CyLaw): arts 10, 11 to 11ΣΤ, 17, 18, 18Α, 18Β, 42Γ, 42Ε, 45, 45Α, 45Β, 61; First, Fifth, Sixth, Seventh, Eighth, Twelfth and Fifteenth Schedules | https://www.cylaw.org/nomoi/enop/non-ind/2000_1_95/full.html | 2026-10-24 |
| Κ.Δ.Π. 337/2025 (0% on baby milk, nappies, hygiene products, fruit and vegetables, 1 Jan to 31 Dec 2026) | https://www.cylaw.org/KDP/data/2025_1_337.pdf | 2026-10-24 |
| Κ.Δ.Π. 168/2026 (0% on meat and fish, 6 Apr to 30 Sep 2026) | https://www.cylaw.org/KDP/data/2026_1_168.pdf | 2026-10-24 |
| Κ.Δ.Π. 354/2026 (0% on meat and fish 1 Oct 2026 to 31 May 2027; bread, milk, coffee, sugar, baby food 12 Oct 2026 to 31 May 2027) | https://www.cylaw.org/KDP/data/2026_1_354.pdf | 2026-10-24 |
| Κ.Δ.Π. 362/2026 (0% on baby milk, nappies, hygiene products, fruit and vegetables, 1 Jan to 31 Dec 2027) | https://www.cylaw.org/KDP/data/2026_1_362.pdf | 2026-10-24 |
| Κ.Δ.Π. 363/2026 (9% on home solar systems) | https://www.cylaw.org/KDP/data/2026_1_363.pdf | 2026-10-24 |
| Κ.Δ.Π. 172/2026 (form to opt out of VAT on a commercial lease) | https://www.cylaw.org/KDP/data/2026_1_172.pdf | 2026-10-24 |
| CyLaw index of 2026 regulatory acts (Κ.Δ.Π.) | https://www.cylaw.org/KDP/2026.html | 2026-10-24 |
| Κ.Δ.Π. 82/2026 (9% household electricity from 1 Apr 2026) | https://www.cylaw.org/KDP/data/2026_1_82.pdf | 2026-10-24 |
| Κ.Δ.Π. 167/2026 (5% household electricity, readings 1 May 2026 to 31 Mar 2027) | https://www.cylaw.org/KDP/data/2026_1_167.pdf | 2026-10-24 |
| Κ.Δ.Π. 102/2026 and 103/2026 (renovation and first establishment, from 1 Sep 2026) | https://www.cylaw.org/KDP/data/2026_1_102.pdf; https://www.cylaw.org/KDP/data/2026_1_103.pdf | 2026-10-24 |
| Κ.Δ.Π. 221/2026 (Seventh Schedule wording) | https://www.cylaw.org/KDP/data/2026_1_221.pdf | 2026-10-24 |
| VAT (Amendment) (No. 2) Law 223(I)/2025 | https://www.cylaw.org/nomoi/arith/2025_1_223.pdf | 2026-10-24 |
| VAT (Amendment) Law 104(I)/2025 (SME-SS) | https://www.cylaw.org/nomoi/arith/2025_1_104.pdf | 2026-10-24 |
| VAT (Amendment) Law 109(I)/2026 | https://www.cylaw.org/nomoi/arith/2026_1_109.pdf | 2026-10-24 |
| VAT (General) Regulations Κ.Δ.Π. 314/2001, regs 17, 24, 64 and 65 | https://www.cylaw.org/KDP/data/2001_1_314.pdf | 2026-10-24 |
| Tax Department, VAT rates | https://www.gov.cy/mof-tax/documents/syntelestes-f-p-a/ | 2026-10-24 |
| Tax Department, obligation and right to register | https://www.gov.cy/mof-tax/documents/eggrafi-akyrosi-f-p-a/eggrafes-mitrooy-f-p-a/ypochreosi-dikaioma-eggrafis-sto-mitroo-f-p-a/ | 2026-10-24 |
| Tax Department, rights and obligations | https://www.gov.cy/mof-tax/documents/dikaiomata-kai-ypochreoseis/ | 2026-10-24 |
| Tax Department, VAT return FAQ | https://www.gov.cy/mof-tax/documents/ypovoli-tropopoiisi-diloseon-f-p-a/sychnes-erotiseis-dilosis-f-p-a/ | 2026-10-24 |
| Tax Department, FAQ on correcting errors | https://www.gov.cy/mof-tax/documents/ypovoli-tropopoiisi-diloseon-f-p-a/sychnes-erotiseis-se-schesi-me-tis-diorthoseis-lathon/ | 2026-10-24 |
| Tax Department, deadline calendar (VAT) | https://www.gov.cy/mof-tax/prothesmies/ | 2026-10-24 |
| Tax Department, guide to completing the VAT return (06082024) | https://www.gov.cy/media/sites/167/2026/01/%CE%9F%CE%B4%CE%B7%CE%B3%CF%8C%CF%82-%CE%B3%CE%B9%CE%B1-%CE%A3%CF%85%CE%BC%CF%80%CE%BB%CE%AE%CF%81%CF%89%CF%83%CE%B7-%CE%94%CE%AE%CE%BB%CF%89%CF%83%CE%B7%CF%82-%CE%A6%CE%A0%CE%91-06082024.pdf | 2026-10-02 (still published 2026-10-24) |
| Tax Department, exempt transactions | https://www.gov.cy/mof-tax/documents/exairoymenes-synallages/ | 2026-10-02 |
| Tax Department, General VAT Guide (Information Leaflet 10, November 2001) | https://www.gov.cy/media/sites/167/2026/01/%CE%93%CE%B5%CE%BD%CE%B9%CE%BA%CF%8C%CF%82-%CE%9F%CE%B4%CE%B7%CE%B3%CF%8C%CF%82-%CE%A6.%CE%A0.%CE%91.-%CE%95%CE%BD%CE%B7%CE%BC%CE%B5%CF%81%CF%89%CF%84%CE%B9%CE%BA%CF%8C-%CE%88%CE%BD%CF%84%CF%85%CF%80%CE%BF-10.pdf | 2026-10-02 |

Not yet confirmed: the VAT rate on household electricity for meter readings from 1 January to 31 March 2026 (Κ.Δ.Π. 337/2025 deleted the earlier 5% entry); whether the Tax Department charges VAT default interest at a rate other than the 9% in art. 45(4); the euro amendment that set the EUR 15,600 registration threshold (the CyLaw consolidation still prints the old Cyprus pound figure in the First Schedule); the euro amounts of the art. 45(5) to (7) charges still printed in Cyprus pounds; the input VAT block on cars and entertainment in current law (only the 2001 guide states it); the box guide, the EUR 17 gift limit and the exemptions page were read on 2 October 2026, not re-read in full today; the Cyprus VAT number format.
