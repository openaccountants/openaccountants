---
name: canada-gst-hst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Canadian GST/HST return, QST return, or any filing involving federal or provincial sales tax in Canada. Trigger on phrases like "prepare GST return", "file HST", "Canadian sales tax", "GST/HST return", "Form GST34", "input tax credits", "ITC claim", "place of supply", "quick method", "simplified method", or any request involving Canadian indirect tax filing. Also trigger when classifying transactions for GST/HST purposes from bank statements, invoices, or other source data. This skill contains the complete Canada GST/HST classification rules, Form GST34 line mappings, ITC rules, place of supply determination, blocked/restricted categories, registration thresholds, filing deadlines, interprovincial supply rules, and quick method remittance rates required to produce a correct return. ALWAYS read this skill before touching any Canadian GST/HST-related work.
---

# Canada GST/HST Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Canada |
| Jurisdiction Code | CA |
| Primary Legislation | Excise Tax Act (R.S.C., 1985, c. E-15), Part IX |
| Supporting Legislation | New Harmonized Value-added Tax System Regulations; Input Tax Credit Information (GST/HST) Regulations; Place of Supply (GST/HST) Regulations (SOR/2010-117); Provincial sales tax acts (see Step 8) |
| Tax Authority (Federal) | Canada Revenue Agency (CRA) |
| Tax Authority (Quebec) | Revenu Quebec (for QST and GST in Quebec) |
| Filing Portal | CRA My Business Account (https://www.canada.ca/en/revenue-agency/services/e-services/digital-services-businesses.html) |
| Filing Portal (Quebec) | Mon dossier pour les entreprises (https://www.revenuquebec.ca) |
| Contributor | Open Accounting Skills Registry |
| Validation Date | April 2026 |
| Validated By | Deep research verification, April 2026 |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: GST/HST rate determination, line assignment, ITC eligibility, registration threshold, filing deadlines. Tier 2: place of supply for mixed supplies, partial ITC restrictions, Quick Method eligibility edge cases. Tier 3: complex interprovincial group structures, First Nations exemptions, transitional rules on rate changes. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A CPA or qualified tax professional must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

**GATE: Before classifying ANY transaction for a Canadian client, you MUST know these facts. Ask if not already known. If items 1-4 are unknown, STOP. Do not classify any transactions until registration status, province, and reporting period are confirmed.**

| # | Question | Tier | Why It Matters |
|---|----------|------|----------------|
| 1 | **Business name and GST/HST Business Number** (Format: 123456789RT0001) | [T1] | Identity and filing authority |
| 2 | **Province of registration / principal place of business** | [T1] | Determines default GST/HST rate |
| 3 | **Registration status** (Registered / small supplier (not registered) / simplified registration (non-resident)) | [T1] | Determines filing obligation |
| 4 | **Reporting period** (Annual / quarterly / monthly) | [T1] | Determines filing deadline |
| 5 | **Fiscal year end** | [T1] | Determines filing deadline for annual filers |
| 6 | **Accounting method** (Regular / Quick Method (GST74 election) / Simplified Method for ITCs) | [T1] | Changes remittance calculation |
| 7 | **Does the business make exempt supplies?** | [T2] | If yes, ITC allocation required |
| 8 | **Does the business make interprovincial supplies?** | [T1] | If yes, place of supply rules must be applied per transaction |
| 9 | **Does the business have employees with taxable benefits?** | [T1] | Impacts ITC claims under ETA s.175 |
| 10 | **Is the business a charity, NPO, or public service body?** | [T2] | Different thresholds and methods apply |
| 11 | **Does the business operate in Quebec?** | [T1] | If yes, QST filing with Revenu Quebec is required |
| 12 | **Annual taxable supplies (approximate)** | [T1] | Determines reporting period assignment and eligibility for simplified methods |
| 13 | **Does the business deal with non-residents?** | [T1] | If yes, self-assessment under s.218 may apply |

---

## Step 1: Transaction Classification Rules

### 1.1 Supply Type Classification [T1]

**Legislation:** ETA s.123(1) (definitions), Schedule V (exempt), Schedule VI (zero-rated).

Every supply in Canada falls into one of three categories:

| Category | GST/HST Charged | ITC Recovery | Legislation |
|----------|-----------------|--------------|-------------|
| **Taxable** (standard-rated) | Yes (5%, 13%, 14%, or 15% depending on province) | Yes -- full ITC on related inputs | ETA s.165 |
| **Zero-rated** | 0% (but still a "taxable supply") | Yes -- full ITC on related inputs | ETA Schedule VI |
| **Exempt** | No GST/HST | No -- NO ITC on related inputs | ETA Schedule V |

**Critical distinction:** Zero-rated and exempt are NOT the same. Zero-rated supplies are taxable supplies taxed at 0%, so the supplier can still claim ITCs. Exempt supplies are NOT taxable supplies, so the supplier CANNOT claim ITCs on inputs used to make exempt supplies. [T1]

### 1.2 Taxable Supplies -- Standard-Rated [T1]

Most goods and services supplied in Canada are taxable at the applicable GST or HST rate. The rate depends on the **place of supply** (see Step 8.1).

| Supply | Rate | Notes |
|--------|------|-------|
| Office supplies sold in Ontario | 13% HST | Place of supply: ON |
| Consulting services to ON client | 13% HST | Place of supply rules for services |
| Retail goods sold in Alberta | 5% GST | No provincial component |
| Restaurant meals in New Brunswick | 15% HST | Place of supply: NB |
| Software subscription to BC client | 5% GST (+ 7% BC PST separately) | GST only; PST is separate |
| Construction services in NS | 14% HST | Post April 1, 2025 rate |
| Hotel accommodation in PEI | 15% HST | Tourism levy may also apply |

### 1.3 Zero-Rated Supplies (0%, with ITC) [T1]

**Legislation:** ETA Schedule VI.

| Supply | Schedule VI Reference | Notes |
|--------|-----------------------|-------|
| Basic groceries | Part III | Excludes snack foods, candy, soft drinks, alcohol |
| Prescription drugs | Part I, s.2 | Must be dispensed by pharmacist with prescription |
| Medical devices | Part II | Listed devices: wheelchairs, hearing aids, artificial limbs, etc. |
| Exports of goods | Part V | Goods shipped outside Canada |
| Exports of services | Part V, s.7 | Services performed for non-resident, not consumed in Canada |
| Agricultural products | Part IV | Farm livestock, grains, raw wool, etc. |
| Certain fishing supplies | Part IV | Nets, bait, etc. for commercial fishing |
| International transportation | Part VII | Freight and passenger, cross-border |
| Financial services to non-residents | Part IX | Must meet conditions |
| Certain First Nations supplies | Part IX.1 | Supplies on reserve -- see Edge Case EC7 |

### 1.4 Exempt Supplies (No GST/HST, No ITC) [T1]

**Legislation:** ETA Schedule V.

| Supply | Schedule V Reference | Notes |
|--------|-----------------------|-------|
| Sale of used residential property | Part I, s.2-4 | New residential property IS taxable |
| Long-term residential rent (1+ month) | Part I, s.6 | Short-term (< 1 month) IS taxable |
| Most health care services | Part II | Physicians, dentists (most), optometrists, chiropractors, physiotherapists |
| Dental services | Part II, s.5 | Most dental services are exempt |
| Child care services | Part III | Licensed and unlicensed day care |
| Legal aid | Part III | Services funded by legal aid plans |
| Most educational services | Part III | Courses at public colleges/universities; vocational training |
| Most financial services | Part VII | Interest, insurance premiums, most banking fees |
| Insurance (arranging/underwriting) | Part VII | Property and casualty, life insurance |
| Bridge/road/ferry tolls (certain) | Part VI | Government-imposed tolls |
| Supplies by public sector bodies | Part V.1, VI | Certain municipal, hospital, school, charity supplies |
| Music lessons (individual) | Part III, s.5 | Individual instruction in music, dance, etc. |
| Used goods sold by charities | Part V.1 | Below threshold |

### 1.5 Classification Matrix: Goods x Location [T1]

| Goods Type | Domestic (within province) | Interprovincial | Export (outside Canada) |
|------------|---------------------------|-----------------|------------------------|
| Standard goods | Taxable at provincial GST/HST rate | Taxable at DESTINATION province rate (place of supply rules) | Zero-rated (Schedule VI, Part V) |
| Basic groceries | Zero-rated | Zero-rated | Zero-rated |
| Prescription drugs | Zero-rated | Zero-rated | Zero-rated |
| Medical devices (listed) | Zero-rated | Zero-rated | Zero-rated |
| Used residential property | Exempt | Exempt | N/A |
| New residential property | Taxable + possible rebate | Taxable at destination rate | N/A |

### 1.6 Classification Matrix: Services x Location [T1]

| Service Type | Domestic (within province) | Interprovincial | International (non-resident client) |
|-------------|---------------------------|-----------------|-------------------------------------|
| Standard services | Taxable at rate where service performed/recipient located | Taxable at DESTINATION province rate | Zero-rated if conditions met (Schedule VI, Part V, s.7) |
| Financial services | Exempt | Exempt | Zero-rated (to non-resident) |
| Health care | Exempt | Exempt | Exempt (unless zero-rated export) |
| Legal services | Taxable | Taxable at destination rate | Zero-rated if for non-resident |
| Education (qualifying) | Exempt | Exempt | Exempt |
| Real property services | Taxable at rate where property located | Taxable at rate where property located | Taxable at rate where property located |
| Digital services/products | Taxable at recipient location | Taxable at recipient location | Zero-rated if non-resident, non-registered |

---

## Step 2: Box/Line Assignment

### 2.1 Form GST34 -- Line Lookup Table [T1]

**Legislation:** ETA s.238(1) (filing requirement), s.225 (net tax calculation).

| Line | Description | What Goes Here |
|------|-------------|----------------|
| **101** | Sales and other revenue | Total revenue from taxable supplies (excluding GST/HST collected). Includes zero-rated and taxable at all rates. Does NOT include exempt supplies. |
| **103** | GST/HST collected or collectible | Total GST/HST charged on supplies for the period. |
| **104** | Adjustments to GST/HST collected | Add: GST/HST on employee benefits, bad debts recovered, change-of-use self-supply. |
| **105** | Total GST/HST and adjustments | Line 103 + Line 104. |
| **106** | Input tax credits (ITCs) | Total ITCs claimed for GST/HST paid on business purchases. |
| **107** | Adjustments to ITCs | Subtract: change-of-use adjustments, ITCs previously overclaimed. |
| **108** | Total ITCs and adjustments | Line 106 + Line 107. |
| **109** | Net tax | Line 105 minus Line 108. Positive = amount owing. Negative = refund claimed. |
| **110** | Instalments paid | Quarterly instalment amounts already remitted for this period. |
| **111** | Rebates claimed | New housing rebate, employee rebate, etc. claimed on the return. |
| **112** | Total other credits | Line 110 + Line 111. |
| **113A** | Balance -- amount owing | If Line 109 > Line 112: amount to remit. |
| **113B** | Balance -- refund claimed | If Line 112 > Line 109: refund to claim. |
| **205** | GST/HST due on acquisition of taxable real property | Self-assessed tax on purchase of real property. |
| **405** | Other GST/HST rebate | Additional rebates (e.g., public service bodies). |

### 2.2 Transaction-to-Line Mapping Table [T1]

| Transaction Type | Line 101 | Line 103 | Line 106 | Notes |
|-----------------|----------|----------|----------|-------|
| Standard taxable sale | Revenue amount (excl. tax) | GST/HST collected | -- | |
| Zero-rated sale (export, basic groceries) | Revenue amount | $0 | -- | Still reported on Line 101 |
| Exempt sale | NOT included | NOT included | -- | Excluded entirely from return |
| Business purchase (taxable) | -- | -- | GST/HST paid | ITC claimed |
| Business purchase (exempt) | -- | -- | $0 | No ITC on exempt inputs |
| Imported service (self-assessment) | -- | Line 205 | Line 106 | Self-assess then claim ITC if commercial |
| Gift card sale | $0 | $0 | -- | Tax applies on redemption only |
| Gift card redemption | Revenue / 1.rate | GST/HST portion | -- | |
| Employee benefit (taxable) | -- | Line 104 | -- | GST/HST on benefit added as adjustment |

### 2.3 Other Return Forms [T1]

| Form | Purpose | Who Files |
|------|---------|-----------|
| **GST34** | Standard GST/HST return for registrants | All standard registrants |
| **GST62** | GST/HST return for non-residents | Non-resident registrants (same line structure as GST34) |
| **GST494** | Simplified Method election | Small businesses electing Simplified Method for ITCs |
| **RC7200** | Combined GST/QST return (Quebec) | Registrants in Quebec (filed with Revenu Quebec) |
| **GST59** | Return for imported taxable supplies | Self-assessing imported services under ETA s.218 |
| **Schedule A** | Builders and land developers | Builders reporting self-supply under ETA s.191 [T2] |
| **GST190** | New housing rebate (federal) | Individuals claiming GST new housing rebate |
| **GST74** | Quick Method election | Businesses electing Quick Method |

### 2.4 Filing Methods [T1]

| Method | Description | Eligibility |
|--------|-------------|-------------|
| CRA My Business Account | Online portal | All registrants |
| NETFILE | Electronic filing | Registered NETFILE users |
| EDI (Electronic Data Interchange) | Automated filing | Large businesses with approved software |
| GST/HST TELEFILE | Telephone filing | Eligible registrants (simple returns) |
| Paper (mail) | Mail to Summerside Tax Centre | All registrants, but electronic filing is mandatory for registrants with > $1.5M in annual taxable supplies (ETA s.238(1)) |

---

## Step 3: Reverse Charge Mechanics

### 3.1 Self-Assessment on Imported Taxable Supplies [T1]

**Legislation:** ETA s.218 (tax on imported taxable supplies).

**This is Canada's equivalent of the EU reverse charge mechanism.**

When a Canadian GST/HST registrant purchases services or intangible personal property from a non-resident who is NOT registered for GST/HST:

| Step | Action | Line |
|------|--------|------|
| 1 | Calculate GST/HST on the value of the imported taxable supply at the applicable provincial rate | -- |
| 2 | Report and remit the tax | Line 205 (or Form GST59) |
| 3 | Claim an ITC for the same amount (if the service is for commercial activities) | Line 106 |
| 4 | Net effect for fully commercial businesses: **zero** | -- |

### 3.2 Non-Resident Digital Supplier Rules [T1]

**Legislation:** ETA s.211.13-211.23 (effective July 1, 2021).

| Scenario | Obligation |
|----------|------------|
| Non-resident B2C digital supplier, exceeds $30,000 threshold | Must register under Simplified Registration, collect and remit GST/HST, CANNOT claim ITCs |
| Non-resident B2B digital supplier | Canadian business self-assesses under ETA s.218; non-resident need not register |
| Place of supply determination for B2C digital | Customer's usual place of residence (Canadian address or IP geolocation); if cannot be determined, default to 5% GST |

---

## Step 4: Deductibility Check (Input Tax Credits)

### 4.1 General ITC Rule [T1]

**Legislation:** ETA s.169(1).

A registrant may claim an ITC for GST/HST paid or payable on property or services acquired for consumption, use, or supply in the course of **commercial activities** of the registrant.

**Formula:**
```
ITC = Tax paid x (Extent of use in commercial activities / Total use)
```

If 100% commercial use: ITC = 100% of GST/HST paid.
If mixed use (commercial + personal/exempt): ITC must be prorated. [T1]

### 4.2 ITC Eligibility Conditions [T1]

ALL of the following must be met to claim an ITC:

| # | Condition | Legislation |
|---|-----------|-------------|
| 1 | Claimant is a **registrant** (registered or required to register) | ETA s.169(1) |
| 2 | GST/HST was **paid or payable** | ETA s.169(1)(a) |
| 3 | Property or service acquired for use in **commercial activities** | ETA s.169(1)(c) |
| 4 | **Sufficient documentation** held (see 4.3 below) | Input Tax Credit Information Regulations |
| 5 | Claimed within **time limit**: 4 years (most registrants); 2 years (specified persons: LFIs, businesses >$6M annual revenue) | ETA s.225(4) |

### 4.3 Documentation Requirements for ITCs [T1]

**Legislation:** Input Tax Credit Information (GST/HST) Regulations, s.3.

| Purchase Amount (tax-included) | Required Information |
|-------------------------------|---------------------|
| Under $100 | Supplier name (or trade name), date, total amount paid |
| $100 to $499.99 | Above + supplier GST/HST registration number, terms of payment, brief description, total GST/HST charged |
| $500 and over | Above + purchaser name (or trade name), purchaser address, individual item amounts or rate applied |

### 4.4 Completely Blocked ITCs [T1]

**Legislation:** ETA s.170.

| Blocked Category | ETA Reference | Exception |
|-----------------|---------------|-----------|
| **Club memberships** (golf, fitness, dining, recreation, yacht clubs) | s.170(1)(a) | NONE. Even if 100% business client entertainment, NO ITC. |
| **Personal or living expenses** | s.170(1)(b) | If property has BOTH personal and business use, ITC may be available on business-use portion. |
| **Property for use in exempt activities** | s.169(1) | None -- not used in commercial activities. |

### 4.5 Restricted (Partial) ITCs [T1]

| Category | Restriction | ETA Reference | Details |
|----------|-------------|---------------|---------|
| **Meals and entertainment** | 50% of GST/HST | s.236(1) read with ITA s.67.1 | Exception: meals at remote work camps (100%), fundraising events (100%), meals as taxable employee benefit (100%), meals for resale by restaurants (100%), long-haul truck drivers (80%). |
| **Passenger vehicles (CCA Class 10.1)** | ITC capped at GST/HST on $37,000 (non-ZEV) or $61,000 (ZEV Class 54) | s.202, s.235 | GST/HST on excess is irrecoverable. |
| **Leased passenger vehicles** | ITC limited to GST/HST on $950/month (non-ZEV) or $1,100/month (ZEV) | s.202; ITA s.67.3 | |
| **Passenger vehicle operating costs** | ITC prorated to business-use % | s.202 | Fuel, repairs, insurance -- prorate. |
| **Employee benefits -- exempt** | No ITC | s.175 | Group health/dental insurance premiums are exempt financial services. |
| **Employee benefits -- taxable** | ITC available | s.175 | Auto standby charge, etc. -- employer claims ITC on GST/HST component. |
| **Home office expenses** | Prorated ITC | s.169(1) | Business-use portion of shared expenses (internet, utilities, office supplies). Must be reasonable. |

### 4.6 Passenger Vehicle ITC Calculation [T1]

**Legislation:** ETA s.202, s.235; ITA s.13(7)(g) (CCA Class 10.1 ceiling).

| Province | Class 10.1 Max ITC (non-ZEV, $37,000 ceiling) | Class 54 Max ITC (ZEV, $61,000 ceiling) |
|----------|------------------------------------------------|------------------------------------------|
| Alberta (5% GST) | $1,850 | $3,050 |
| Ontario (13% HST) | $4,810 | $7,930 |
| Nova Scotia (14% HST) | $5,180 | $8,540 |
| NB / NL / PEI (15% HST) | $5,550 | $9,150 |

### 4.7 Capital Property ITCs [T1]

**Legislation:** ETA s.169, s.195-211.

| Capital Property Type | ITC Rule | Notes |
|----------------------|----------|-------|
| Real property (land/buildings) | ITC if used >50% in commercial activities | Change-in-use rules apply (see 4.8) |
| Capital personal property (equipment, furniture) | ITC prorated to commercial use | >90% commercial = 100% ITC; <10% = 0% ITC; 10-90% = prorate |
| Improvements to capital property | Follow underlying property rules | |
| Passenger vehicles -- Class 10.1 | ITC capped (see 4.6) | |
| Aircraft | ITC if commercial; prorate for personal use | |
| Computer equipment | Standard capital property rules | |

### 4.8 Change-in-Use Rules [T1]

**Legislation:** ETA s.195-211.

| Change | Rule | Effect |
|--------|------|--------|
| Commercial to exempt (real property) | Deemed sale at FMV | Output tax on FMV; recapture of ITCs |
| Exempt to commercial (real property) | Deemed purchase at FMV | ITC available on deemed GST/HST |
| Commercial to personal (personal property) | Deemed sale at FMV | Output tax on FMV |
| Personal to commercial (personal property) | Deemed purchase at FMV | ITC available on deemed GST/HST |
| Increase in commercial use (personal property) | Positive ITC adjustment | Additional ITC proportional to increase |
| Decrease in commercial use (personal property) | Negative ITC adjustment (output tax) | Repay ITC proportional to decrease |

### 4.9 Restricted ITCs -- Large Business Rule (Historical) [T1]

**As of 2026, no RITC restrictions are in effect in any province.** Ontario RITCs phased out July 1, 2018; PEI RITCs phased out April 1, 2018. Nova Scotia, New Brunswick, and Newfoundland and Labrador never applied RITCs.

**Note for historical returns:** If preparing returns for periods before July 1, 2018 (ON) or April 1, 2018 (PEI), the RITC rules applied to: energy, telecommunications services, road vehicles under 3,000 kg, fuel for such vehicles, meals and entertainment, and certain property and services used in ON/PEI. [T2] -- Escalate to reviewer for historical period calculations.

---

## Step 5: Derived Calculations

### 5.1 Net Tax Calculation (Regular Method) [T1]

**Legislation:** ETA s.225.

```
Line 105 = Line 103 (GST/HST collected) + Line 104 (adjustments)
Line 108 = Line 106 (ITCs) + Line 107 (ITC adjustments)
Line 109 = Line 105 - Line 108
If Line 109 > 0: amount owing (Line 113A)
If Line 109 < 0: refund claimed (Line 113B)
```

### 5.2 Quick Method Calculation [T1]

**Legislation:** ETA s.227; Quick Method of Accounting Regulations (SOR/91-51).

| Step | Action |
|------|--------|
| 1 | Collect GST/HST on sales at the normal rate |
| 2 | Remit a **reduced percentage** (remittance rate) of GST/HST-included revenue |
| 3 | Keep the difference (approximates average ITCs) |
| 4 | Do NOT claim ITCs on operating expenses (except capital equipment >$30,000) |

**Eligibility:** [T1]

| Criterion | Requirement |
|-----------|-------------|
| Annual taxable supplies (including associates) | $400,000 or less (including GST/HST) |
| Filing status | Must be a registrant |
| Excluded businesses | Financial institutions, charities using net-tax method, non-residents, accountants, actuaries, bookkeepers, financial consultants, tax consultants, lawyers |
| Election | Must file Election Form GST74 before the first day of the reporting period |

**Remittance Rates -- Businesses that purchase goods for resale:** [T1]

| Province/Territory | GST/HST Rate | Remittance Rate |
|--------------------|-------------|-----------------|
| AB, NT, NU, YT, BC, SK, MB (GST only) | 5% | 1.8% |
| Ontario | 13% | 4.4% |
| Nova Scotia | 14% | 4.7% |
| NB, NL, PEI | 15% | 5.0% |

**Remittance Rates -- Service providers (NOT purchasing goods for resale):** [T1]

| Province/Territory | GST/HST Rate | Remittance Rate |
|--------------------|-------------|-----------------|
| AB, NT, NU, YT, BC, SK, MB (GST only) | 5% | 3.6% |
| Ontario | 13% | 8.8% |
| Nova Scotia | 14% | 9.4% |
| NB, NL, PEI | 15% | 10.0% |

**First-year credit:** First $30,000 of HST-included revenue in the first year of election is subject to a 1% credit (remittance rate reduced by 1%). [T1]

### 5.3 Simplified Method for Calculating ITCs [T1]

**Legislation:** ETA s.227(1); Simplified Method for Claiming ITCs Regulations.

Eligible for registrants with annual taxable supplies of $1,000,000 or less. Total purchases (tax-included) are multiplied by a factor:

| Province | Factor |
|----------|--------|
| GST-only provinces (5%) | 5/105 = 4.762% |
| Ontario (13% HST) | 13/113 = 11.504% |
| Nova Scotia (14% HST) | 14/114 = 12.281% |
| NB / NL / PEI (15% HST) | 15/115 = 13.043% |

Purchases from multiple provinces must be grouped and calculated separately. [T1]

### 5.4 Charity Net Tax Method [T1]

**Legislation:** ETA s.225.1.

Registered charities can remit 60% of GST/HST collected on taxable supplies and claim NO ITCs. Public service body rebate (50% of GST on exempt-activity inputs) may also apply under ETA s.259.

---

## Step 6: Key Thresholds

| Threshold | Amount | Legislation | Notes |
|-----------|--------|-------------|-------|
| **Small supplier (general)** | $30,000 in taxable supplies in last 4 consecutive calendar quarters, OR in any single quarter | ETA s.148 | [T1] |
| **Small supplier (public service bodies)** | $50,000 in taxable supplies | ETA s.148 | [T1] |
| **Taxi/limo operators** | $0 -- must register regardless | ETA s.240(1.1) | [T1] |
| **Non-resident performers** | $0 -- must register if making taxable supplies in Canada | ETA s.240(2) | [T1] |
| **Registration deadline** | Within 29 days of exceeding threshold | ETA s.240(1) | [T1] The supply that causes the threshold to be exceeded is itself subject to GST/HST. |
| **Voluntary registration** | Any amount -- can register if engaged in commercial activity | ETA s.240(3) | [T1] Benefits: ITCs, credibility with commercial clients. |
| **Cancellation of registration** | Taxable supplies under $30,000 for last 12 months AND registered for at least 1 year | ETA s.242 | [T1] |
| **Mandatory electronic filing** | Annual taxable supplies > $1,500,000 | ETA s.238(1) | [T1] |
| **Monthly reporting mandatory** | Annual taxable supplies > $6,000,000 | ETA s.245-248 | [T1] |
| **Quick Method eligibility** | $400,000 or less (including GST/HST) | Regulations | [T1] |
| **Simplified Method eligibility** | $1,000,000 or less in annual taxable supplies | Regulations | [T1] |
| **Instalment requirement** | Prior year net tax > $3,000 (annual filers) | ETA s.237 | [T1] |
| **ITC documentation -- simplified** | Purchase under $100 tax-included | Regulations s.3 | [T1] |
| **ITC documentation -- intermediate** | $100 to $499.99 tax-included | Regulations s.3 | [T1] |
| **ITC documentation -- full** | $500+ tax-included | Regulations s.3 | [T1] |
| **ITC claim time limit (general)** | 4 years | ETA s.225(4) | [T1] |
| **ITC claim time limit (specified persons)** | 2 years | ETA s.225(4) | [T1] Applies to LFIs, businesses >$6M revenue. |
| **Passenger vehicle CCA ceiling (non-ZEV)** | $37,000 | ITA s.13(7)(g), Class 10.1 | [T1] |
| **Passenger vehicle CCA ceiling (ZEV)** | $61,000 | ITA, Class 54 | [T1] |
| **Lease ceiling (non-ZEV)** | $950/month | ITA s.67.3 | [T1] |
| **Lease ceiling (ZEV)** | $1,100/month | ITA s.67.3 | [T1] |
| **New housing rebate FMV phase-out** | $350,000 -- $450,000 | ETA s.254 | [T1] Federal GST rebate: 36% of GST, max $6,300. |

### 6.1 GST/HST Registration Number Format [T1]

```
123456789 RT 0001
|         |  |
|         |  +-- Account reference number (0001 = first GST/HST account)
|         +---- Program identifier (RT = GST/HST)
+--------- 9-digit Business Number
```

The full 15-character number must be shown on invoices: `123456789RT0001`. [T1]

### 6.2 QST Registration Number Format [T1]

```
1234567890 TQ 0001
```

In Quebec, Revenu Quebec administers both GST and QST. A single registration covers both. The $30,000 small supplier threshold applies separately to QST. [T1]

---

## Step 7: Filing Deadlines

### 7.1 Reporting Periods [T1]

**Legislation:** ETA s.245-248.

| Annual Taxable Supplies | Assigned Reporting Period | Can Elect |
|------------------------|--------------------------|-----------|
| $1,500,000 or less | Annual | Monthly or quarterly |
| $1,500,001 to $6,000,000 | Quarterly | Monthly |
| Over $6,000,000 | Monthly | None (monthly is mandatory) |

### 7.2 Filing and Payment Deadlines [T1]

**Legislation:** ETA s.238(1), s.245.

| Reporting Period | Filing Deadline | Payment Deadline |
|-----------------|-----------------|------------------|
| **Monthly** | 1 month after end of reporting period | Same as filing deadline |
| **Quarterly** | 1 month after end of reporting period | Same as filing deadline |
| **Annual** (individual, Dec 31 year-end) | June 15 of following year | **April 30** of following year |
| **Annual** (non-Dec 31 year-end) | 3 months after end of fiscal year | 3 months after end of fiscal year |
| **Annual** (corporation, Dec 31 year-end) | March 31 of following year | 3 months after fiscal year end |

**Key nuance for annual filers who are individuals:** The FILING deadline is June 15 (aligned with income tax), but the PAYMENT deadline is April 30. Late payment after April 30 incurs interest even if the return is filed by June 15. [T1]

### 7.3 Instalment Requirements for Annual Filers [T1]

**Legislation:** ETA s.237.

Annual filers whose net tax for the preceding fiscal year exceeds $3,000 must pay quarterly instalments:

| Instalment | Due Date | Amount |
|------------|----------|--------|
| Q1 | Last day of first quarter | 1/4 of prior year net tax |
| Q2 | Last day of second quarter | 1/4 of prior year net tax |
| Q3 | Last day of third quarter | 1/4 of prior year net tax |
| Q4 | Last day of fourth quarter | 1/4 of prior year net tax |

Alternatively, instalments can be based on estimated current-year net tax. [T1]

### 7.4 Penalties [T1]

**Legislation:** ETA s.280, s.280.1, s.281.

| Penalty Type | Rate/Amount | ETA Section |
|-------------|-------------|-------------|
| **Interest on overdue amounts** | Prescribed rate (set quarterly by CRA) + 4% per annum, compounded daily | s.280(1) |
| **Failure to file** | 1% of amount owing + 0.25% per month late, up to 12 months (max 4% surcharge) | s.280.1(1) |
| **Repeated failure to file** | 2% of amount owing + 0.5% per month, up to 20 months (max 12% surcharge) | s.280.1(2) |
| **False statements or omissions** | Greater of $250 or 25% of tax sought to be evaded | s.285 |
| **Gross negligence** | Greater of $250 or 25% of tax sought to be evaded | s.285 |
| **Failure to register** | $1,000 to $25,000 fine and/or up to 12 months imprisonment | s.328(1) |

### 7.5 Interest Rate [T1]

**Legislation:** ETA s.280; Regulations s.4301(a).

The prescribed interest rate is set quarterly by CRA based on the Government of Canada Treasury Bill rate.
- Interest on overdue GST/HST = prescribed rate + 4%.
- Interest on GST/HST refunds owed by CRA = prescribed rate + 2%.
- Rates published quarterly in the Canada Gazette. [T1]

### 7.6 Voluntary Disclosure Program (VDP) [T2]

**Legislation:** ETA s.281.

CRA may waive or cancel penalties and interest if a registrant voluntarily discloses errors or omissions before CRA initiates enforcement action. Conditions: voluntary, complete, involves a penalty (at least one year overdue), payment arrangement proposed.

**Flag for reviewer: VDP applications involve significant professional judgement. Always escalate to tax professional.**

---

## Step 8: Place of Supply, Provincial Rates, and Canada-Specific Rules

### 8.1 Rates by Province/Territory (as of April 2026) [T1]

**Legislation:** ETA s.165(1) (GST), s.165(2) (HST provincial component).

| Province/Territory | Code | GST | Provincial Tax | Combined Rate | Tax Type | Administered By |
|--------------------|------|-----|----------------|---------------|----------|-----------------|
| Alberta | AB | 5% | 0% | 5% | GST only | CRA |
| British Columbia | BC | 5% | 7% PST | 12% effective | GST + PST | CRA (GST) + BC Ministry of Finance (PST) |
| Manitoba | MB | 5% | 7% RST | 12% effective | GST + RST | CRA (GST) + MB Ministry of Finance (RST) |
| New Brunswick | NB | 5% | 10% (HST provincial) | 15% HST | HST | CRA |
| Newfoundland and Labrador | NL | 5% | 10% (HST provincial) | 15% HST | HST | CRA |
| Northwest Territories | NT | 5% | 0% | 5% | GST only | CRA |
| Nova Scotia | NS | 5% | 9% (HST provincial) | 14% HST | HST | CRA |
| Nunavut | NU | 5% | 0% | 5% | GST only | CRA |
| Ontario | ON | 5% | 8% (HST provincial) | 13% HST | HST | CRA |
| Prince Edward Island | PE | 5% | 10% (HST provincial) | 15% HST | HST | CRA |
| Quebec | QC | 5% | 9.975% QST | ~14.975% effective | GST + QST | Revenu Quebec (administers BOTH) |
| Saskatchewan | SK | 5% | 6% PST | 11% effective | GST + PST | CRA (GST) + SK Ministry of Finance (PST) |
| Yukon | YT | 5% | 0% | 5% | GST only | CRA |

**Nova Scotia rate change:** Reduced from 15% HST to 14% HST effective April 1, 2025. [T1]

### 8.2 HST Provincial Component Breakdown [T1]

| HST Province | Federal Component | Provincial Component | Total HST |
|-------------|-------------------|---------------------|-----------|
| Ontario | 5% | 8% | 13% |
| New Brunswick | 5% | 10% | 15% |
| Newfoundland and Labrador | 5% | 10% | 15% |
| Nova Scotia | 5% | 9% | 14% |
| Prince Edward Island | 5% | 10% | 15% |

### 8.3 Historical Rate Changes (Reference) [T1]

| Province | Previous Rate | New Rate | Effective Date |
|----------|--------------|----------|----------------|
| Nova Scotia | 15% HST | 14% HST | April 1, 2025 |
| Newfoundland and Labrador | 13% HST | 15% HST | July 1, 2016 |
| Prince Edward Island | 14% HST | 15% HST | October 1, 2016 |
| New Brunswick | 13% HST | 15% HST | July 1, 2016 |
| Ontario | 8% PST (retail) | 13% HST | July 1, 2010 |
| British Columbia | 12% HST | 5% GST + 7% PST | April 1, 2013 (HST repealed by referendum) |
| Prince Edward Island | 10% PST | 14% HST | April 1, 2013 |

**When processing returns that span a rate change date, prorate supplies based on when the tax became payable (generally the earlier of invoice date or payment date). [T2]**

### 8.4 Canada's Multi-Layer Indirect Tax System [T1]

Canada does NOT have a single unified VAT/GST system. Four distinct tax types apply depending on province:

**GST (Goods and Services Tax):** Federal tax at 5%, imposed under ETA s.165(1). Applies in every province and territory. ITCs recoverable by registrants. [T1]

**HST (Harmonized Sales Tax):** Single combined federal + provincial tax, imposed under ETA s.165(2). Federal component is always 5%. Provincial component varies. Administered entirely by CRA. One return, one remittance. ITCs recover the FULL HST amount. [T1]

**PST (Provincial Sales Tax):** Separate provincial retail sales tax. NOT a value-added tax. Imposed by BC, SK, and MB. Generally NOT recoverable by businesses. PST is NOT reported on the GST/HST return. It is a separate provincial filing. **This skill covers GST/HST. PST obligations are noted for context but are separate filings.** [T1]

**QST (Quebec Sales Tax):** Quebec's own VAT-style tax at 9.975%, imposed under AQST. Structurally similar to GST but administered separately by Revenu Quebec. Input Tax Refunds (ITRs) available. In Quebec, Revenu Quebec administers BOTH the GST and the QST. **This skill focuses on GST/HST. QST is referenced for completeness but has its own filing requirements.** [T1]

### 8.5 Place of Supply Rules [T1]

**Legislation:** ETA s.144.1, s.272.1; Place of Supply (GST/HST) Regulations (SOR/2010-117).

**General principle:** Tax follows the destination (where the supply is consumed or delivered), not the origin.

#### Tangible Personal Property (Goods) [T1]

**Legislation:** Place of Supply Regulations s.3.

| Scenario | Place of Supply | Rate Applied |
|----------|----------------|--------------|
| Goods delivered to customer in Ontario | Ontario | 13% HST |
| Goods delivered to customer in Alberta | Alberta | 5% GST |
| Goods delivered to customer in New Brunswick | New Brunswick | 15% HST |
| Goods shipped from Ontario to Alberta | Alberta (destination) | 5% GST |
| Goods shipped from Alberta to Ontario | Ontario (destination) | 13% HST |
| Goods shipped to customer outside Canada | Outside Canada | 0% (zero-rated export) |
| Goods delivered to shipping company for export | Canada (where delivered to carrier) unless exported | Apply rules carefully [T2] |

**Key rule:** The place of supply is where **possession of the goods is transferred to the recipient** (delivery address), NOT where the supplier is located. [T1]

#### Services -- General Rule [T1]

**Legislation:** Place of Supply Regulations s.5.

**General rule:** Place of supply is the province where the **recipient** is located (business address or, for individuals, usual place of residence). [T1]

#### Services -- Specific Overrides [T1]

**Legislation:** Place of Supply Regulations s.6-13.

| Service Type | Place of Supply | Regulation |
|-------------|----------------|------------|
| Services related to **real property** | Province where property is situated | s.6 |
| Services related to **tangible personal property** | Province where property is at time of service | s.7 |
| **Transportation services** (freight) | Province where shipment is delivered | s.8 |
| **Passenger transportation** | Province where journey begins | s.9 |
| **Events** (admission, conference, seminar) | Province where event takes place | s.10 |
| **Acting/performing services** | Province where performance occurs | s.11 |
| **Postage/mailing services** | Province where mail is deposited | s.12 |
| **Telecommunications** | Province of ordinary location of the device | s.13 |
| **Computer-related/IT services** | Province of recipient (general rule applies) | s.5 |

#### Intangible Personal Property (Digital Products, Licences) [T1]

**Legislation:** Place of Supply Regulations s.4.

Place of supply determined by address of recipient. If non-resident, zero-rated if conditions met. [T1]

#### Interprovincial Supply Examples [T1]

| Supplier Location | Customer Location | GST/HST Rate | Why |
|-------------------|-------------------|-------------|-----|
| Alberta (5% GST) | Ontario (13% HST) | 13% HST | Destination-based |
| Ontario (13% HST) | Alberta (5% GST) | 5% GST | Destination-based |
| New Brunswick (15% HST) | Nova Scotia (14% HST) | 14% HST | Destination-based |
| British Columbia (5% GST + 7% PST) | Ontario (13% HST) | 13% HST; no BC PST | GST/HST follows destination |
| Ontario (13% HST) | Quebec (5% GST + 9.975% QST) | 5% GST + QST (separate) | QC is not an HST province |
| Ontario (13% HST) | United States | 0% (zero-rated export) | Exported outside Canada |

### 8.6 Key ETA Sections Reference [T1]

| ETA Section | Subject |
|-------------|---------|
| s.123(1) | Definitions (supply, taxable supply, registrant, etc.) |
| s.141.01 | Use of property -- taxable vs exempt |
| s.148 | Small supplier threshold |
| s.165(1) | Imposition of GST at 5% |
| s.165(2) | Imposition of provincial component of HST |
| s.169 | Input tax credits -- general rule |
| s.170 | Restrictions on ITCs |
| s.171 | ITCs for financial institutions |
| s.202 | Employee and partner ITCs |
| s.211-211.1 | Self-supply rules (real property) |
| s.218 | Tax on imported taxable supplies (reverse charge equivalent) |
| s.218.1 | Selected listed financial institutions -- special rules |
| s.221 | Obligation to collect GST/HST |
| s.225 | Net tax calculation |
| s.227-228 | Quick method / simplified method |
| s.228 | Reporting periods and filing |
| s.237-240 | Registration requirements |
| s.238-239 | Filing and remittance |
| s.256-256.77 | Rebates (new housing, employee, etc.) |
| s.261 | Rebate for overpayment |
| s.272.1 | Place of supply rules |
| s.280 | Interest on overdue amounts |
| s.280.1 | Penalty for failure to file |
| s.281 | Waiver of penalty/interest |
| s.296 | Assessments |
| Schedule V | Exempt supplies |
| Schedule VI | Zero-rated supplies |

### 8.7 Comparison with EU VAT [T1]

| Feature | Canada GST/HST | EU VAT (Directive 2006/112/EC) |
|---------|---------------|-------------------------------|
| Tax type | Multi-rate consumption tax (GST/HST/PST/QST) | Value-added tax |
| Federal vs. state | Federal tax (GST); provincial component varies | Each member state sets own rate within EU minimums |
| Standard rates | 5% (GST), 13-15% (HST) | 15% minimum; most states 19-27% |
| Reduced rates | None federally; provincial components create effective reduced rates | Two reduced rates allowed (min 5%) plus super-reduced/zero |
| Zero-rating | Yes (basic groceries, prescription drugs, exports) | Yes, varies by member state |
| Exempt without credit | Yes (financial services, health care, used residential) | Yes (similar categories) |
| Registration threshold | $30,000 CAD (~EUR 20,000) | Varies by state (EUR 0 to EUR 85,000) |
| Input tax credit/deduction | ITCs under ETA s.169 | Input VAT deduction under Art. 168 |
| Reverse charge | Self-assessment under ETA s.218 | Reverse charge under Art. 196 |
| Interprovincial/intra-community | Place of supply rules (destination principle) | Intra-community acquisition (destination principle) |
| Digital economy | Simplified registration for non-resident B2C (since July 2021) | OSS/IOSS (since July 2021) |

| EU VAT Concept | Canadian Equivalent |
|----------------|-------------------|
| VAT registration | GST/HST registration (BN + RT program) |
| VAT return (periodic) | GST/HST return (Form GST34) |
| Input VAT deduction | Input Tax Credit (ITC) |
| Output VAT | GST/HST collected/collectible |
| Intra-community supply | Interprovincial supply |
| Reverse charge (cross-border services) | Self-assessment under ETA s.218 |
| MOSS/OSS (digital economy) | Simplified Registration for non-residents |
| Pro-rata / partial exemption | ITC allocation for mixed-use inputs |
| Capital goods scheme | Change-in-use rules (ETA s.195-211) |
| EC Sales List | No equivalent in Canada |
| Intrastat | No equivalent in Canada |

---

## PROHIBITIONS [T1]

- NEVER apply HST rate based on supplier's province -- ALWAYS use destination (place of supply) province rate.
- NEVER treat zero-rated supplies the same as exempt supplies -- zero-rated allows ITC recovery; exempt does NOT.
- NEVER claim ITCs on club memberships (ETA s.170(1)(a)) -- blocked under ALL circumstances.
- NEVER claim ITCs on personal or living expenses (ETA s.170(1)(b)).
- NEVER claim more than 50% ITC on meals and entertainment (unless an exception applies).
- NEVER claim ITCs on passenger vehicles above the CCA ceiling ($37,000 non-ZEV / $61,000 ZEV).
- NEVER claim ITCs without proper documentation (supplier name, date, GST/HST number for purchases over $100).
- NEVER charge GST/HST on exempt supplies (Schedule V).
- NEVER charge GST/HST on the sale of gift cards -- tax applies only on redemption.
- NEVER include PST in GST/HST return calculations -- PST is a separate provincial tax with separate filing.
- NEVER apply RITCs (Restricted Input Tax Credits) to current-period returns -- all RITC programs have been fully phased out.
- NEVER register a small supplier ($30,000 threshold) involuntarily unless the threshold is exceeded.
- NEVER file a GST/HST return with CRA for a Quebec registrant -- Quebec registrants file with Revenu Quebec.
- NEVER assume a non-resident digital supplier can claim ITCs under simplified registration -- they CANNOT.
- NEVER guess on First Nations tax exemption -- confirm status, supply type, and delivery location with tax professional.
- NEVER apply a single flat rate across all provinces -- rates vary from 5% to 15%.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Edge Case Registry

### EC1 -- Interprovincial Supply: Ontario Seller to Alberta Buyer [T1]

**Situation:** An Ontario-based business sells goods and ships them to a customer in Alberta.
**Resolution:** Place of supply is Alberta (delivery address). The supplier charges **5% GST only**, NOT 13% HST. The destination-based rule under Place of Supply Regulations s.3 applies.
**Legislation:** ETA s.144.1; Place of Supply Regulations s.3.
**Common error:** Ontario-based suppliers often mistakenly charge 13% HST on all sales regardless of destination.

### EC2 -- Place of Supply for Digital Services: SaaS to Consumer in Multiple Provinces [T2]

**Situation:** A SaaS company sells subscriptions to consumers across Canada.
**Resolution:** The supplier must determine each customer's province of residence and charge the applicable GST/HST rate. If unknown, use best available information (billing address, IP address). If cannot be determined, default to 5% GST.
**Legislation:** Place of Supply Regulations s.4, s.5; ETA s.211.16.
**Flag for reviewer:** High-volume B2C digital sales require system configuration for correct provincial rates.

### EC3 -- Non-Resident Digital Supplier (e.g., Netflix, Spotify) [T1]

**Situation:** A non-resident company provides digital services to Canadian consumers (B2C).
**Resolution:** Since July 1, 2021, must register under Simplified Registration if exceeding $30,000 threshold. Must collect and remit GST/HST. CANNOT claim ITCs. B2B supplies: Canadian business self-assesses under ETA s.218.
**Legislation:** ETA s.211.13-211.23.

### EC4 -- Input Tax Credit Recapture (Historical -- Pre-2018) [T1]

**Situation:** Preparing a return for a large Ontario business for a period before July 1, 2018.
**Resolution:** Large businesses (>$10M annual taxable supplies) in Ontario and PEI were required to recapture the provincial component of HST on specified inputs. Recapture amount reported as negative adjustment on Line 107.
**Current status:** All RITCs fully phased out. No recapture applies to current-period returns. [T1]

### EC5 -- Real Property Self-Supply (Builder) [T2]

**Situation:** A builder constructs a new residential property and rents or occupies it instead of selling.
**Resolution:** ETA s.191 deems a taxable sale AND purchase at FMV. Builder must self-assess GST/HST on FMV (Line 205), claim ITC only if used in commercial activities (e.g., short-term rental). If exempt long-term rental, no ITC. New housing rebate may apply (ETA s.256, s.256.2).
**Flag for reviewer:** FMV determination and rebate eligibility require professional judgement.

### EC6 -- Employee Benefits: Automobile Standby Charge [T1]

**Situation:** Employer provides company car with taxable benefit under ITA s.6(1)(e) and s.6(1)(k).
**Resolution:** Employer can claim ITC on GST/HST component: `ITC = (Taxable benefit x GST/HST rate) / (100% + GST/HST rate)`. Claimed on annual return for the year T4 is issued.
**Legislation:** ETA s.175(1).

### EC7 -- First Nations Tax Exemption [T2]

**Situation:** Supply made to an Indigenous person on a reserve, or supply made on a reserve.
**Resolution:** Under Indian Act s.87 and CRA GST/HST Technical Information Bulletin B-039: tangible goods delivered to a reserve are GST/HST exempt; services performed entirely on a reserve for a Status Indian are exempt; off-reserve purchases are generally subject to GST/HST with possible point-of-sale relief.
**Flag for reviewer:** First Nations tax exemption involves complex fact patterns. Always confirm with tax professional.

### EC8 -- GST/HST New Housing Rebate [T1]

**Situation:** Individual purchases newly constructed home as primary residence.
**Resolution:**

| Tax | Rebate | Maximum | Threshold |
|-----|--------|---------|-----------|
| GST (federal 5%) | 36% of GST paid | $6,300 | Full rebate at FMV $350,000 or less; phased out $350K-$450K; no rebate above $450K |
| Ontario HST (provincial 8%) | 75% of provincial HST | $24,000 | No phase-out based on price |
| Nova Scotia HST (provincial) | Up to $3,000 | $3,000 | Varies |
| Other HST provinces | Varies | Province-specific | Province-specific |

**Filed on:** Form GST190 (federal), Form RC7190-ON (Ontario), or equivalent provincial form.

### EC9 -- Medical and Dental Services -- Exempt vs. Taxable [T1]

| Exempt (No GST/HST) | Taxable (GST/HST applies) |
|---------------------|--------------------------|
| Physician services (medically necessary) | Cosmetic surgery (elective) |
| Dental services (most) | Teeth whitening (cosmetic) |
| Chiropractic services | Some paramedical services not in Schedule V |
| Physiotherapy | Personal training / fitness coaching |
| Optometry (eye exams) | Laser eye surgery (cosmetic -- [T2] may be exempt if medically necessary) |
| Prescription drugs | Over-the-counter supplements and vitamins |
| Medical devices (listed) | Non-listed health products |

### EC10 -- Financial Services -- Exempt Treatment [T1]

| Exempt Financial Services | NOT Exempt (Taxable) |
|--------------------------|---------------------|
| Interest on loans | Advisory/consulting fees (if separately charged) |
| Insurance premiums (arranging, underwriting) | Insurance adjusting fees |
| Trading in securities | Safe deposit box rental |
| Exchange of currency | Financial planning fees (if not part of exempt service) |
| Credit card annual fees | Credit report services |
| Mortgage arrangement | Mortgage brokerage fees [T2] |

**ITC impact:** Financial institutions making primarily exempt supplies have heavily restricted ITC claims. Special allocation methods under ETA s.141.02. [T3] -- Escalate financial institution ITCs to specialist.

### EC11 -- Drop Shipping [T2]

**Situation:** Non-resident sells goods to Canadian customer, shipped from Canadian warehouse.
**Resolution:** Complex multi-party transaction. Non-resident may need to register. If registered, charges GST/HST to Canadian customer. Drop shipper charges GST/HST to non-resident. Special rules under ETA s.179 may allow zero-rating between drop shipper and non-resident.
**Flag for reviewer:** Always confirm full fact pattern with tax professional.

### EC12 -- Supplies by Charities and Non-Profit Organizations [T2]

**Situation:** Registered charity or NPO makes taxable and exempt supplies.
**Resolution:** Small supplier threshold is $50,000 (not $30,000). Net Tax Method available: remit 60% of GST/HST collected, claim no ITCs (ETA s.225.1). Public service body rebate: charities 50% of GST on exempt-activity inputs; municipalities 100% (ETA s.259).
**Flag for reviewer:** Election between net tax and regular method has significant financial implications.

### EC13 -- GST/HST on Imported Services (Reverse Charge) [T1]

**Situation:** Canadian registrant purchases services from non-registered non-resident.
**Resolution:** Self-assess under ETA s.218: calculate GST/HST, remit (Form GST59 or regular return), claim ITC if commercial. Net effect for fully commercial businesses: zero.

### EC14 -- Gift Cards and Vouchers [T1]

Sale of gift card is NOT a taxable supply. GST/HST applies on redemption, not sale. Revenue from gift card sales NOT included in Line 101 or Line 103; include only on redemption.
**Legislation:** ETA s.181.2.

### EC15 -- Tips and Gratuities [T1]

Voluntary tips are NOT consideration for a supply -- NOT subject to GST/HST. Mandatory service charges/auto-gratuities added to the bill ARE consideration -- subject to GST/HST.
**Legislation:** ETA s.123(1); CRA Policy Statement P-202.

### EC16 -- Coupons and Discounts [T1]

- **Store coupons/discounts:** GST/HST on NET (discounted) price. Discount reduces consideration.
- **Manufacturer coupons (third-party reimburses retailer):** GST/HST on FULL price. Coupon is third-party payment, not a reduction.
**Legislation:** ETA s.181 (coupons), s.232 (adjustments).

---

## Test Suite

### Test 1 -- Standard Ontario Sale, 13% HST [T1]

**Input:** Ontario-based retailer sells office furniture to Ontario customer. Invoice: $1,000 + $130 HST = $1,130.
**Expected output:**
- Line 101: $1,000 (sales revenue)
- Line 103: $130 (HST collected)
- No ITC entries for this sale (ITCs relate to purchases, not sales).

### Test 2 -- Interprovincial Sale: ON Seller to AB Buyer [T1]

**Input:** Ontario-based consulting firm provides services to Alberta client. Invoice: $5,000. Place of supply: Alberta.
**Expected output:**
- Line 101: $5,000
- Line 103: $250 (5% GST only, NOT 13% HST)
- Supplier collects 5% GST because destination is Alberta.

### Test 3 -- Zero-Rated Export [T1]

**Input:** Manitoba manufacturer exports goods to US customer. Invoice: USD 10,000 (CAD $13,500). Goods shipped to Minneapolis.
**Expected output:**
- Line 101: $13,500
- Line 103: $0 (zero-rated export)
- ITCs on related manufacturing inputs: fully claimable.

### Test 4 -- Exempt Supply: Used Residential Property [T1]

**Input:** Individual sells used residential home in Ontario for $500,000.
**Expected output:**
- NOT reported on GST/HST return (exempt supply).
- Line 101: $0 (exempt supplies excluded)
- Line 103: $0
- No ITCs claimable on expenses related to this sale.

### Test 5 -- ITC on Business Purchase in New Brunswick [T1]

**Input:** NB registrant purchases office supplies from local supplier. Invoice: $200 + $30 HST (15%) = $230.
**Expected output:**
- Line 106: $30 (ITC claimed for full HST)
- Supporting documentation: supplier name, date, GST/HST reg number, amount.

### Test 6 -- Blocked ITC: Golf Club Membership [T1]

**Input:** Ontario registrant pays $5,000 + $650 HST for annual golf club membership. Used 100% for client entertaining.
**Expected output:**
- Line 106: $0 (ITC BLOCKED under ETA s.170(1)(a))
- $650 HST is an irrecoverable cost.

### Test 7 -- Meals and Entertainment: 50% ITC Restriction [T1]

**Input:** Alberta registrant takes client to restaurant. Bill: $200 + $10 GST = $210.
**Expected output:**
- Line 106: $5 (50% of $10 GST)
- The other $5 GST is a non-recoverable cost.

### Test 8 -- Passenger Vehicle Exceeding CCA Ceiling [T1]

**Input:** Ontario registrant purchases a luxury vehicle for $80,000 + $10,400 HST (13%). 100% business use.
**Expected output:**
- Maximum ITC = 13% x $37,000 = $4,810
- Line 106: $4,810 (NOT $10,400)
- $5,590 HST irrecoverable.

### Test 9 -- Quick Method: Service Business in Ontario [T1]

**Input:** Freelance consultant in Ontario. Annual revenue: $80,000 + $10,400 HST collected = $90,400 (HST-included). Quick Method, first year of election.
**Expected output:**
- First $30,000: remit at 7.8% (8.8% - 1% credit) = $2,340
- Remaining $60,400: remit at 8.8% = $5,315.20
- Total remittance: $7,655.20
- Compared to $10,400 collected -- consultant keeps $2,744.80.

### Test 10 -- Self-Assessment on Imported Service (Reverse Charge) [T1]

**Input:** Ontario registrant purchases legal services from US law firm ($20,000 USD = $27,000 CAD). US firm not registered for GST/HST.
**Expected output:**
- Self-assess: 13% x $27,000 = $3,510 HST payable (Line 205)
- ITC claim: $3,510 (Line 106) -- if 100% commercial use
- Net effect: $0

### Test 11 -- Charity Using Net Tax Method [T1]

**Input:** Registered charity in Ontario. Annual taxable sales: $40,000 + $5,200 HST collected. Uses net tax method.
**Expected output:**
- Remittance = 60% x $5,200 = $3,120
- No ITCs claimed (net tax method).
- Charity may also claim public service body rebate on exempt-activity inputs.

### Test 12 -- Small Supplier Threshold Exceeded Mid-Quarter [T1]

**Input:** Sole proprietor in Alberta. Taxable supplies: Q1 = $8,000, Q2 = $9,000, Q3 = $7,000, Q4 = $10,000. Running four-quarter total after Q4: $34,000.
**Expected output:**
- Registration required within 29 days of Q4 end.
- The supply that caused the threshold to be exceeded is itself subject to GST.
- Must begin collecting 5% GST on all subsequent taxable supplies.

### Test 13 -- New Housing Rebate (Ontario) [T1]

**Input:** Individual purchases new home in Ontario for $400,000 + $52,000 HST (13%) as primary residence. FMV = $400,000.
**Expected output:**
- Federal GST rebate: 36% x ($400,000 x 5%) x (($450,000 - $400,000) / $100,000) = 36% x $20,000 x 50% = $3,600
- Ontario provincial rebate: 75% x ($400,000 x 8%) = 75% x $32,000 = $24,000 (capped at $24,000)
- Total rebate: $3,600 + $24,000 = $27,600
- Net HST after rebate: $52,000 - $27,600 = $24,400

### Test 14 -- Gift Card Sale and Redemption [T1]

**Input:** Ontario retailer sells a $100 gift card. Card is later redeemed for $100 of taxable merchandise.
**Expected output:**
- At time of gift card sale: Line 101 = $0, Line 103 = $0 (no GST/HST on gift card sale).
- At time of redemption: Line 101 = $88.50 ($100 / 1.13), Line 103 = $11.50 ($100 x 13/113).

---

## Reviewer Escalation Protocol

### T2 Escalation Format

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: CPA or qualified Canadian tax professional must confirm before filing.
```

### T3 Escalation Format

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to CPA or qualified Canadian tax professional. Document gap.
```

### Known T3 Situations (Always Escalate)

- Financial institution ITC allocation methods (ETA s.141.02)
- First Nations tax exemption determinations (Indian Act s.87)
- Real property self-supply fair market value assessments (ETA s.191)
- GST/HST group registration and elections (ETA s.156)
- Related party non-arm's length transactions (ETA s.155)
- Insolvency and bankruptcy GST/HST treatment
- GST/HST on amalgamations and wind-ups
- Cross-border transfer pricing adjustments affecting GST/HST
- Selected listed financial institution (SLFI) special rules

---

## Contribution Notes

If you are adapting this skill for another jurisdiction:

1. Replace all legislation references (ETA sections) with equivalent national/state legislation.
2. Replace all form numbers (GST34, etc.) with equivalent local return forms.
3. Replace GST/HST rates with local rates.
4. Replace the $30,000 small supplier threshold with local equivalent.
5. Replace the CCA ceiling ($37,000) with local vehicle cost limitations.
6. Replace the provincial rate table with applicable sub-national rates.
7. Replace blocked/restricted categories with local equivalents.
8. Replace place of supply rules with local rules for determining tax jurisdiction.
9. Have a CPA or qualified tax professional in the target jurisdiction validate every T1 rule before publishing.
10. Add jurisdiction-specific edge cases to the Edge Case Registry.
11. Run all test suite cases against local rules and update expected outputs.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
