---
name: no-sales-tax-states
description: Use this skill whenever asked about states with no sales tax, Alaska local sales tax, Delaware gross receipts tax, Montana resort tax, New Hampshire meals and rooms tax, Oregon Corporate Activity Tax, or tax obligations in AK, DE, MT, NH, or OR. Trigger on phrases like "no sales tax states", "Alaska sales tax", "Delaware gross receipts", "Montana resort tax", "New Hampshire meals tax", "Oregon CAT", "Oregon no sales tax", or any request involving tax compliance in states that do not impose a general statewide sales tax. ALWAYS load us-sales-tax first for federal context.
---

# No-Sales-Tax States Skill -- AK, DE, MT, NH, OR

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdictions | Alaska (AK), Delaware (DE), Montana (MT), New Hampshire (NH), Oregon (OR) |
| Tax Type | These states impose NO general statewide sales tax; however, each has alternative consumption or business taxes |
| Primary Statutes | AK: AS 29.45 (local tax authority); DE: 30 Del. C. Ch. 27 (Gross Receipts Tax); MT: MCA §7-6-15 (Resort Tax); NH: RSA 78-A (Meals & Rooms Tax); OR: ORS 317A (Corporate Activity Tax) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: fundamental no-sales-tax status, alternative tax existence. T2: local tax rates, applicability of alternative taxes. T3: complex compliance scenarios, multi-state interactions. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Section 1: Overview -- Five States Without a General Sales Tax [T1]

Five US states do **not** impose a general statewide sales tax:

| State | No General Sales Tax | But Has... |
|-------|---------------------|------------|
| **Alaska (AK)** | Correct | Local sales taxes (boroughs/cities up to 7.5%) |
| **Delaware (DE)** | Correct | Gross Receipts Tax on sellers (0.0945% to 1.9914%) |
| **Montana (MT)** | Correct | Resort Tax in certain tourist communities (up to 3%) |
| **New Hampshire (NH)** | Correct | Meals & Rooms Tax (8.5%) |
| **Oregon (OR)** | Correct | Corporate Activity Tax (CAT) (0.57% on commercial activity over $1M) |

**Key principle:** "No sales tax" does NOT mean "no consumption-related taxes." Each of these states has alternative mechanisms that tax some or all commercial activity. [T1]

---

## Section 2: Alaska (AK) [T1/T2]

### 2.1 No State Sales Tax, But Local Sales Taxes Exist [T1]

- Alaska has **no statewide sales tax**. [T1]
- However, Alaska is unique among the no-sales-tax states because it **permits local jurisdictions (boroughs and cities) to impose their own sales taxes**. [T1]
- Approximately **100+ local jurisdictions** in Alaska impose sales tax. [T1]
- Local rates range from **1% to 7.5%**. [T1]

### 2.2 Major Local Sales Tax Rates [T1]

| Jurisdiction | Rate | Notes |
|-------------|------|-------|
| Juneau (City & Borough) | 5.00% | Capital city |
| Fairbanks North Star Borough | 0% | No borough tax; City of Fairbanks = 0% |
| Anchorage (Municipality) | 0% | No local sales tax |
| Kenai Peninsula Borough | 3.00% | Plus city taxes |
| Sitka | 6.00% | |
| Kodiak | 7.00% | One of the highest |
| Skagway | 5.00% | Tourism-driven |
| Ketchikan | 3.50% | Plus borough tax |

**Note:** Anchorage, Alaska's largest city, does NOT impose a local sales tax. [T1]

### 2.3 No Centralized Administration [T2]

- There is **no state-level agency** that administers local sales taxes in Alaska. [T1]
- Each local jurisdiction administers its own tax: registration, filing, collection, and audit. [T1]
- Sellers with nexus in multiple Alaska jurisdictions must register and file **separately with each one**. [T1]
- This creates significant compliance burden, similar to Alabama's self-administered cities. [T2]

### 2.4 Economic Nexus -- Local Level [T2]

- Because there is no state sales tax, there is no state-level economic nexus threshold. [T1]
- However, individual local jurisdictions may assert their own nexus rules for remote sellers. [T2]
- The Alaska Remote Seller Sales Tax Commission (ARSSTC) was formed to create a centralized registration and filing system for remote sellers. [T2]
- Remote sellers can register through ARSSTC to collect a uniform remote seller rate in participating jurisdictions. [T2]
- **Not all jurisdictions participate in ARSSTC.** [T2]

**Source:** Alaska Remote Seller Sales Tax Commission (https://arsstc.org).

### 2.5 Exempt and Taxable Items -- Varies by Locality [T2]

- Each local jurisdiction defines its own taxable and exempt categories. [T2]
- Food: Some jurisdictions exempt grocery food; others tax it. [T2]
- Prescription drugs: Generally exempt in most jurisdictions. [T2]
- Clothing: Generally taxable where a local tax applies. [T2]

### 2.6 Filing [T2]

- No state-level sales tax return. [T1]
- Each jurisdiction has its own return form, due date, and filing frequency. [T2]
- ARSSTC provides centralized filing for participating jurisdictions. [T2]
- **Flag for reviewer:** Sellers with Alaska nexus must identify each local jurisdiction and comply separately unless ARSSTC covers their obligations. [T2]

---

## Section 3: Delaware (DE) [T1/T2]

### 3.1 No Sales Tax -- Gross Receipts Tax Instead [T1]

- Delaware has **no sales tax** imposed on buyers. [T1]
- Instead, Delaware imposes a **Gross Receipts Tax (GRT)** on the **seller's** gross receipts from business conducted in Delaware. [T1]
- GRT is a tax on the SELLER, not the buyer. Sellers may NOT pass GRT to buyers as a separate line item labeled "sales tax." [T1]
- Many sellers build GRT into their prices. [T2]

### 3.2 Gross Receipts Tax Rates [T1]

GRT rates vary by business type:

| Business Type | Monthly Rate | Approximate Annual Rate |
|--------------|-------------|------------------------|
| Manufacturers | 0.0945% | ~1.13% |
| Wholesalers | 0.3985% | ~4.78% |
| Retailers | 0.7468% | ~8.96% |
| Grocers/food retailers | 0.0945% | ~1.13% |
| Restaurants | 0.6758% | ~8.11% |
| Lessors of real property | 0.1862% | ~2.23% |
| Lessors of TPP | 0.7468% | ~8.96% |
| Professionals | 0.3944% | ~4.73% |
| Commercial feed dealers | 0.0945% | ~1.13% |
| Contractors | Various | Varies by type |

**Statute:** 30 Del. C. §2901 et seq.

**Note:** These rates are applied MONTHLY to gross receipts. The annual effective rate is 12x the monthly rate. [T1]

### 3.3 No Exemptions for Buyers [T1]

- Because there is no sales tax, there are no buyer-side exemption certificates in Delaware. [T1]
- There is no resale exemption concept (because the tax is on the seller, not the buyer). [T1]
- Certain exclusions from gross receipts exist (e.g., federal government sales, certain exempt organizations). [T2]

### 3.4 Economic Nexus [T2]

- Delaware does not have a traditional sales tax economic nexus threshold. [T1]
- However, businesses operating IN Delaware are subject to GRT. [T1]
- Out-of-state businesses with no Delaware physical presence generally do not owe GRT. [T2]
- Delaware's corporate-friendly environment (incorporation) does not automatically create GRT nexus. [T2]

### 3.5 Filing [T1]

| Field | Detail |
|-------|--------|
| Return Form | Monthly Gross Receipts Tax Return |
| Filing Frequency | Monthly |
| Due Date | 20th of the following month |
| Portal | https://revenue.delaware.gov (Delaware One Stop) |

### 3.6 Business-Friendly Reputation [T1]

- Delaware is famous for its corporation-friendly laws (Court of Chancery, no corporate income tax on out-of-state revenue, no sales tax). [T1]
- The absence of sales tax makes Delaware a popular cross-border shopping destination for residents of neighboring states (PA, NJ, MD). [T1]
- Retailers in Delaware often advertise "tax-free shopping." [T1]

---

## Section 4: Montana (MT) [T1/T2]

### 4.1 No General Sales Tax -- Resort Tax Exists [T1]

- Montana has **no general statewide sales tax**. [T1]
- Montana's Constitution was historically interpreted as prohibiting a general sales tax (though this has been debated). [T2]
- However, Montana imposes a **Resort Tax** in designated resort communities. [T1]

### 4.2 Resort Tax -- Up to 3% [T1]

- Eligible resort communities may impose a resort tax of up to **3%** on the retail value of goods and services sold within the resort area. [T1]
- The resort tax applies to: lodging, restaurants/prepared food, alcoholic beverages, retail goods, and certain services. [T1]

**Resort tax communities include:**
- Big Sky
- Red Lodge
- West Yellowstone
- Whitefish
- Virginia City
- Cooke City/Silver Gate

**Statute:** Montana Code Annotated (MCA) §7-6-1501 et seq.

### 4.3 Lodging Facility Use Tax [T1]

- Montana imposes a **4% Lodging Facility Use Tax** on all transient accommodations statewide. MCA §15-65-111. [T1]
- This applies to hotels, motels, B&Bs, campgrounds, and vacation rentals throughout the state (not just resort communities). [T1]
- Short-term rental platforms must collect and remit. [T1]

### 4.4 Rental Car Tax [T1]

- Montana imposes a **4% Rental Vehicle Tax** on short-term vehicle rentals. MCA §15-68-101. [T1]

### 4.5 No Economic Nexus for Sales Tax [T1]

- Because there is no state sales tax, there is no state-level economic nexus threshold. [T1]
- Resort tax nexus is based on physical presence within the resort community. [T2]

### 4.6 Filing [T2]

- Resort tax: filed with the individual resort community. [T2]
- Lodging tax: filed with the Montana Department of Revenue. [T1]
- **Portal:** https://mtrevenue.gov

---

## Section 5: New Hampshire (NH) [T1/T2]

### 5.1 No General Sales Tax -- Meals & Rooms Tax Exists [T1]

- New Hampshire has **no general sales tax** on the sale of goods. [T1]
- New Hampshire imposes a **Meals and Rooms (Rentals) Tax** of **8.5%** on prepared meals, hotel/lodging stays, and motor vehicle rentals. [T1]

**Statute:** RSA 78-A.

### 5.2 Meals & Rooms Tax Details [T1]

| Category | Rate | Notes |
|----------|------|-------|
| Prepared meals (restaurant food) | 8.5% | Includes takeout and delivery |
| Hotel/motel rooms and lodging | 8.5% | Includes Airbnb/short-term rentals |
| Motor vehicle rentals | 8.5% | Short-term car rentals |
| Campsite rentals | 8.5% | Campgrounds and RV parks |
| Conference/banquet room rental | 8.5% | When provided with meals/lodging |

### 5.3 What Is NOT Taxed [T1]

- Retail goods (clothing, electronics, etc.): **NOT taxed**. [T1]
- Unprepared grocery food: **NOT taxed**. [T1]
- Prescription and OTC drugs: **NOT taxed**. [T1]
- Services (professional, personal): **NOT taxed**. [T1]
- SaaS and digital goods: **NOT taxed**. [T1]

**New Hampshire's tax-free shopping** is a major economic driver, attracting shoppers from bordering states (MA, VT, ME). [T1]

### 5.4 Interest & Dividends Tax -- Repealed [T1]

- New Hampshire's Interest and Dividends Tax was repealed effective January 1, 2025. [T1]
- NH has no general income tax (it never taxed wages; only interest/dividend income was taxed). [T1]

### 5.5 Business Taxes [T2]

- **Business Profits Tax (BPT):** 7.5% on business net income (applicable to businesses, not individuals). [T2]
- **Business Enterprise Tax (BET):** 0.55% on the enterprise value tax base (compensation + interest + dividends). [T2]
- These business taxes are the state's primary business-related revenue source. [T2]

### 5.6 Economic Nexus [T2]

- No state sales tax means no traditional economic nexus threshold. [T1]
- Meals & Rooms Tax: businesses physically operating in NH (restaurants, hotels) must collect. [T1]
- Remote sellers of goods have NO NH tax collection obligation. [T1]

### 5.7 Filing [T1]

| Field | Detail |
|-------|--------|
| Return Form | Meals and Rooms Tax Return (Form MR) |
| Filing Frequency | Monthly |
| Due Date | 15th of the following month |
| Portal | https://www.revenue.nh.gov |

---

## Section 6: Oregon (OR) [T1/T2]

### 6.1 No Sales Tax -- Corporate Activity Tax (CAT) Exists [T1]

- Oregon has **no sales tax** of any kind -- no state-level, no local-level. [T1]
- Oregon is the **purest "no sales tax" state** in the country. [T1]
- However, Oregon enacted the **Corporate Activity Tax (CAT)** effective January 1, 2020. [T1]

### 6.2 Corporate Activity Tax (CAT) [T1]

| Field | Detail |
|-------|--------|
| Tax Type | Gross receipts tax on businesses |
| Rate | $250 + 0.57% on Oregon commercial activity exceeding $1 million |
| Threshold | $1 million in Oregon commercial activity |
| Subtraction | 35% of the greater of cost of goods sold or labor costs (capped at 95% of commercial activity) |
| Statute | Oregon Revised Statutes (ORS) 317A |
| Filing | Annual (due April 15 for calendar year filers) |
| Portal | https://revenueonline.dor.oregon.gov |

**Key features:**
- CAT applies to businesses (not individuals). [T1]
- The tax base is Oregon-sourced commercial activity. [T1]
- The 35% subtraction for COGS or labor partially mitigates the cascading effect. [T1]
- CAT is NOT a sales tax -- it is a business activity tax that cannot be separately stated on customer invoices. [T1]
- Oregon law prohibits businesses from adding CAT as a separate line item on consumer invoices. [T1]

### 6.3 No Local Sales or Gross Receipts Tax [T1]

- Oregon does not permit local sales taxes. [T1]
- Some local jurisdictions have imposed transient lodging taxes on hotel/vacation rentals. [T2]

### 6.4 Lodging Tax [T1]

- Oregon imposes a **1.5% state transient lodging tax** on accommodations. ORS 320.305. [T1]
- Local jurisdictions may impose additional lodging taxes (varying rates). [T2]
- Portland combined lodging tax can exceed 11% (city + county + TID + state). [T2]

### 6.5 Economic Nexus [T1]

- No sales tax means no traditional economic nexus threshold. [T1]
- CAT nexus: businesses with $1 million+ in Oregon commercial activity owe CAT. [T1]
- Remote sellers shipping goods to Oregon customers have NO sales tax obligation. [T1]

### 6.6 Impact on Multi-State Sellers [T1]

- Sellers based in Oregon making sales to customers in OTHER states must still comply with those states' sales tax laws if they have nexus there. [T1]
- Oregon sellers shipping to buyers in California, Washington, etc. must collect the destination state's sales tax if economic nexus is met. [T1]
- The fact that Oregon has no sales tax does not relieve Oregon sellers of obligations in other states. [T1]

### 6.7 Filing [T1]

| Field | Detail |
|-------|--------|
| CAT Return | Annual (ORS 317A.137) |
| Due Date | April 15 (calendar year); quarterly estimated payments required if annual tax >$5,000 |
| Portal | https://revenueonline.dor.oregon.gov |

---

## Section 7: Edge Cases [T2/T3]

### EC1 -- Alaska Local Tax Compliance for Remote Sellers [T2]

**Situation:** An e-commerce seller from Texas ships products to customers throughout Alaska. Some addresses are in jurisdictions with local sales tax; others are not.

**Resolution:**
- The seller must determine whether each delivery address falls within a local taxing jurisdiction. [T1]
- If the seller registers with ARSSTC, they can collect a uniform remote seller rate for participating jurisdictions. [T2]
- Not all Alaska jurisdictions participate in ARSSTC. Non-participating jurisdictions must be handled individually. [T2]
- Anchorage has no local sales tax. Juneau has 5%. [T1]
- **Flag for reviewer:** Alaska local tax compliance is complex. Recommend ARSSTC participation for simplification. [T2]

### EC2 -- Delaware "Tax-Free Shopping" Marketing [T2]

**Situation:** A Delaware retailer advertises "tax-free shopping." Is this accurate?

**Resolution:**
- Delaware has no SALES tax, so shoppers do not pay tax at the register. [T1]
- The retailer pays GRT on its gross receipts, which may be built into prices. [T1]
- The advertising claim is technically accurate from the buyer's perspective. [T1]
- Out-of-state shoppers may owe USE TAX in their home state on purchases brought back. [T1]
- **Flag for reviewer:** Delaware retailers should not describe prices as "completely tax-free" in contexts that might imply no tax burden exists at all. [T2]

### EC3 -- Oregon Seller with Multi-State Customers [T2]

**Situation:** An Oregon-based e-commerce company sells nationwide. It exceeds economic nexus thresholds in 15 states. Does it owe any Oregon tax?

**Resolution:**
- No Oregon sales tax obligation (Oregon has no sales tax). [T1]
- CAT may apply if Oregon commercial activity exceeds $1 million. [T1]
- The company must register, collect, and remit sales tax in each state where it has nexus. [T1]
- Oregon's lack of sales tax does NOT exempt the company from other states' sales tax laws. [T1]
- **Flag for reviewer:** Oregon sellers often mistakenly believe "no sales tax" means no multi-state compliance. [T2]

### EC4 -- New Hampshire Border Shopping [T1]

**Situation:** Massachusetts residents drive to New Hampshire to purchase goods tax-free. Does MA use tax apply?

**Resolution:**
- Items purchased in NH and brought back to MA are technically subject to MA use tax (6.25%). [T1]
- The MA resident should self-assess use tax on their MA income tax return. [T1]
- In practice, enforcement on individual consumer purchases is minimal. [T2]
- For business purchases, the use tax obligation is real and auditable. [T1]
- **Flag for reviewer:** Businesses purchasing in NH for use in other states must comply with use tax in their home state. [T1]

### EC5 -- Montana Resort Tax for Online Seller [T2]

**Situation:** An online seller ships products to a customer in Big Sky, Montana (a resort tax community). Must they collect resort tax?

**Resolution:**
- The resort tax applies to retail sales within the resort community boundaries. [T1]
- Whether remote sellers must collect resort tax is a local determination. [T2]
- There is no statewide centralized collection mechanism for resort tax. [T2]
- **Flag for reviewer:** Montana resort tax collection by remote sellers is unclear. Verify with the specific resort community. [T2]

---

## Section 8: Test Suite [T1]

### Test 1 -- Alaska: Sale to Juneau (Local Tax Applies)

**Input:** Seller ships a $500 item to a customer in Juneau, AK. Juneau local rate = 5%.
**Expected output:** No state tax. Local tax = $500 x 5% = $25.00. Total = $525.00.

### Test 2 -- Alaska: Sale to Anchorage (No Tax)

**Input:** Seller ships a $500 item to a customer in Anchorage, AK.
**Expected output:** No state tax. No local tax (Anchorage has no sales tax). Tax = $0. Total = $500.00.

### Test 3 -- Delaware: No Sales Tax on Buyer

**Input:** Customer purchases $1,000 of electronics at a Delaware store.
**Expected output:** No sales tax charged to the buyer. Price = $1,000. The retailer pays GRT on its gross receipts.

### Test 4 -- New Hampshire: Restaurant Meal

**Input:** Customer has an $80 dinner at a New Hampshire restaurant. Meals & Rooms Tax = 8.5%.
**Expected output:** Tax = $80 x 8.5% = $6.80. Total = $86.80.

### Test 5 -- New Hampshire: Retail Purchase (No Tax)

**Input:** Customer purchases a $500 laptop at a New Hampshire electronics store.
**Expected output:** No sales tax. No meals/rooms tax (not a meal/room). Tax = $0. Total = $500.00.

### Test 6 -- Oregon: No Sales Tax on Any Purchase

**Input:** Customer purchases $2,000 of merchandise at an Oregon retailer.
**Expected output:** No sales tax. No local tax. Tax = $0. Total = $2,000.00. Oregon has no sales tax of any kind.

### Test 7 -- Montana: Purchase in Resort Community

**Input:** Tourist purchases a $200 item in a Big Sky resort shop. Resort tax = 3%.
**Expected output:** No state tax. Resort tax = $200 x 3% = $6.00. Total = $206.00.

---

## Section 9: PROHIBITIONS [T1]

- NEVER state that Alaska has no sales tax without qualifying that local jurisdictions may impose sales tax up to 7.5%. [T1]
- NEVER state that Delaware is "completely tax-free." Delaware imposes a Gross Receipts Tax on sellers. [T1]
- NEVER assume an Oregon seller has no multi-state sales tax obligations. Oregon's lack of sales tax does not exempt sellers from other states' laws. [T1]
- NEVER apply a sales tax rate to a purchase in Oregon. Oregon has zero sales tax everywhere. [T1]
- NEVER forget New Hampshire's 8.5% Meals & Rooms Tax. "No sales tax" does not mean "no tax on dining and lodging." [T1]
- NEVER assume Montana is completely tax-free. Resort communities impose up to 3% resort tax, and lodging is taxed statewide at 4%. [T1]
- NEVER advise a customer that purchases in no-sales-tax states are free of all tax obligations. Use tax may be owed in their home state. [T1]
- NEVER add Oregon's CAT as a separate line item on customer invoices. Oregon law prohibits this. [T1]
- NEVER confuse Delaware's GRT (tax on seller) with a sales tax (tax on buyer). The GRT cannot be itemized as "sales tax" on receipts. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
