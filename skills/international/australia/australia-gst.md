---
name: australia-gst
description: Use this skill whenever asked to prepare, review, or create an Australian GST return (Business Activity Statement / BAS) for any client. Trigger on phrases like "prepare BAS", "do the GST", "fill in BAS", "create the return", "GST return", "Activity Statement", or any request involving Australian GST filing. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill contains the complete Australian GST classification rules, BAS label mappings, input tax credit rules, reverse charge treatment, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any GST-related work.
---

# Australia GST Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Australia |
| Jurisdiction Code | AU |
| Primary Legislation | A New Tax System (Goods and Services Tax) Act 1999 (GST Act) |
| Supporting Legislation | A New Tax System (Wine Equalisation Tax) Act 1999; A New Tax System (Luxury Car Tax) Act 1999; Taxation Administration Act 1953 (Schedule 1); GST Regulations 2019 |
| Tax Authority | Australian Taxation Office (ATO) |
| Filing Portal | ATO Business Portal (https://bp.ato.gov.au) / myGov (https://my.gov.au) |
| Contributor | Open Accounting Skills Registry |
| Validation Date | April 2026 |
| Skill Version | 1.1 |
| Validated By | Deep research verification, April 2026 |
| Confidence Coverage | Tier 1: BAS label assignment, GST-free/input-taxed classification, derived calculations. Tier 2: apportionment for mixed-use, margin scheme elections, financial supply thresholds. Tier 3: complex GST group structures, non-standard cross-border arrangements, partnership/trust distributions. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A registered tax agent or BAS agent must confirm before lodging.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to registered tax agent and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and ABN** [T1] -- 11-digit ABN
2. **Is the entity registered for GST?** [T1] -- If no, no GST obligations arise
3. **GST reporting period** [T1] -- Monthly, quarterly, or annual
4. **Accounting basis** [T1] -- Cash or accrual
5. **Is the entity on Simpler BAS?** [T1] -- If yes, only G1, 1A, 1B required
6. **Industry/sector** [T2] -- Impacts classification (e.g., financial services = input taxed revenue; food retail = mix of GST-free and taxable)
7. **Does the entity make input taxed supplies?** [T2] -- If yes, apportionment may be required; confirm methodology with tax agent
8. **Is the entity part of a GST group?** [T2] -- If yes, identify representative member
9. **Aggregated turnover** [T1] -- Determines SBE eligibility, reporting obligations, Simpler BAS
10. **Does the entity import goods?** [T1] -- Customs duty and GST at border; import declarations needed

**If items 1-4 are unknown, STOP. Do not classify any transactions until registration status, reporting period, and accounting basis are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1.1 Classification Decision Tree [T1]

For every transaction, determine:

1. **Is it a supply or acquisition?** (Sale = output / Purchase = input)
2. **Is the entity registered for GST?** (If no, no GST obligations)
3. **Is it connected with Australia?** (GST Act, Division 9-25)
4. **Is it GST-free?** (Check Division 38 categories)
5. **Is it input taxed?** (Check Division 40 categories)
6. **If neither GST-free nor input taxed, it is taxable at 10%**

### 1.2 Three Categories of Supplies [T1]

| Category | GST Rate | Input Tax Credits | GST Act Reference | EU VAT Equivalent |
|----------|----------|-------------------|--------------------|--------------------|
| Taxable supply | 10% | Yes -- full credit on related inputs | Division 7, s 9-5 | Standard-rated supply |
| GST-free supply | 0% | Yes -- full credit on related inputs | Division 38 | Zero-rated supply |
| Input taxed supply | No GST | No -- no credit on related inputs | Division 40 | Exempt supply (no credit) |

**Critical distinction:** GST-free and input taxed are NOT the same. GST-free suppliers retain input tax credit entitlements; input taxed suppliers do not. This mirrors the EU distinction between zero-rated and exempt-without-credit supplies.

### 1.3 Taxable Supplies (10%) -- Lookup Table [T1]

**Legislation:** GST Act, s 9-5 (meaning of taxable supply).

| Supply Type | GST Treatment | BAS Label (Sales) | Notes |
|-------------|---------------|-------------------|-------|
| Sale of commercial goods | Taxable 10% | G1 (and G6 derived) | Standard supply |
| Professional services (legal, accounting, consulting) | Taxable 10% | G1 | B2B and B2C |
| Commercial rent (office, retail, warehouse) | Taxable 10% | G1 | Landlord must be registered |
| Sale of new residential premises | Taxable 10% | G1 | "New" = never sold as residential, or created by substantial renovation, or built by developer (GST Act, s 40-75) |
| Construction services | Taxable 10% | G1 | |
| Motor vehicle sale (dealer) | Taxable 10% | G1 | LCT may also apply above threshold |
| Restaurant / cafe meals | Taxable 10% | G1 | Prepared food is taxable |
| Software licences | Taxable 10% | G1 | |
| Telecommunications | Taxable 10% | G1 | |
| Insurance premiums (general) | Taxable 10% | G1 | Life insurance is input taxed |
| Imported goods (> AUD 1,000) | Taxable 10% | Customs collects | GST at border. Credit claimed on BAS. |
| Imported goods (<= AUD 1,000) | Taxable 10% | Vendor collection model | Low-value imported goods since 1 July 2018 |

### 1.4 GST-Free Supplies (0%, Credits Retained) -- Lookup Table [T1]

**Legislation:** GST Act, Division 38.

| Supply Type | Subdivision | BAS Label | Notes |
|-------------|------------|-----------|-------|
| Basic food (bread, milk, meat, fruit, vegetables, flour, rice) | 38-A (s 38-2 to 38-4) | G3 | Excludes prepared/restaurant food, confectionery, soft drinks, alcohol, snack foods |
| Health services (GP, specialist, hospital, allied health) | 38-B (s 38-7 to 38-47) | G3 | Must be listed in health services table; cosmetic/elective procedures may be taxable |
| Education (school, university, TAFE, registered training) | 38-C (s 38-85 to 38-110) | G3 | Must be provided by recognised institution; commercial training may be taxable |
| Childcare services | 38-D (s 38-145 to 38-150) | G3 | Approved child care services |
| Exports of goods | 38-E (s 38-185) | G2 | Goods physically exported from Australia within 60 days |
| Exports of services | 38-E (s 38-190) | G2 | Services provided to non-resident for consumption outside Australia |
| Religious services | 38-F (s 38-220) | G3 | Services by religious institution as part of religious practice |
| Water and sewerage | 38-G (s 38-250 to 38-265) | G3 | Supply of water by government or utility |
| International transport of goods | 38-E (s 38-355) | G2 | Freight services for international carriage |
| International transport of passengers | 38-E (s 38-355) | G2 | International flight/voyage tickets |
| Precious metals (first supply by refiner/dealer) | 38-I (s 38-385 to 38-390) | G3 | Gold, silver, platinum -- first supply; subsequent may be input taxed |
| Going concern | 38-J (s 38-325) | G3 | Sale of a business as a going concern (both parties registered, written agreement) |
| Farmland supply | 38-J (s 38-480) | G3 | Must meet specific farming use requirements |
| Cars for disabled persons | 38-L (s 38-510) | G3 | Modified for disabled access |
| International mail | 38-E | G2 | Australia Post international services |
| Supplies through duty-free shops | 38-E (s 38-185(3)) | G2 | Exported under supervision of Customs |
| Digital currency | -- | G3 | Treated as neither money nor financial supply since 1 July 2017 (Treasury Laws Amendment (2017 Measures No. 6) Act 2017) |

#### Subdivision 38-A: Food Detail [T1]

The food provisions are among the most complex in the GST Act. The basic rule:

- **GST-free:** Food that is NOT listed in Schedule 1 of the GST Act (i.e., basic/staple food)
- **Taxable:** Food listed in Schedule 1 (prepared food, confectionery, soft drinks, snack foods, restaurant meals)

| Food Item | GST Treatment | Reasoning |
|-----------|---------------|-----------|
| Fresh fruit & vegetables | GST-free | Basic food, Subdivision 38-A |
| Fresh meat, poultry, fish | GST-free | Basic food |
| Bread, rolls | GST-free | Basic food |
| Milk, cream, cheese | GST-free | Basic food |
| Rice, pasta, flour | GST-free | Basic food |
| Eggs | GST-free | Basic food |
| Cooking oil, margarine, butter | GST-free | Basic food |
| Baby food / infant formula | GST-free | Basic food |
| Bottled water (plain) | GST-free | Basic food |
| Tea, coffee (unbrewed) | GST-free | Basic food |
| Confectionery (chocolate, lollies) | Taxable 10% | Schedule 1 exclusion |
| Soft drinks, energy drinks | Taxable 10% | Schedule 1 exclusion |
| Ice cream | Taxable 10% | Schedule 1 exclusion |
| Snack foods (chips, pretzels) | Taxable 10% | Schedule 1 exclusion |
| Prepared meals (takeaway, restaurant) | Taxable 10% | Food supplied ready for consumption |
| Hot food (pies, sausage rolls from bakery) | Taxable 10% | Heated for consumption |
| Alcohol | Taxable 10% + excise/WET | Never GST-free |
| Biscuits (plain, not chocolate) | GST-free | Basic food |
| Biscuits (chocolate coated) | Taxable 10% | Confectionery |
| Muesli bars | Taxable 10% | Snack food |
| Nuts (raw, unprocessed) | GST-free | Basic food |
| Nuts (honey roasted, flavoured) | Taxable 10% | Snack food |

#### Subdivision 38-B: Health [T1]

| Supply | GST Treatment | Condition |
|--------|---------------|-----------|
| GP consultations | GST-free | Medicare-eligible service |
| Specialist medical services | GST-free | Medicare-eligible |
| Hospital services (public) | GST-free | Government-funded |
| Hospital services (private) | GST-free | Covered under health services table |
| Prescription medicines (PBS) | GST-free | Listed on Pharmaceutical Benefits Scheme |
| Over-the-counter medicines | GST-free | Must be therapeutic goods |
| Dental services | GST-free | Practitioner must be registered |
| Physiotherapy, chiropractic | GST-free | Registered health practitioner |
| Ambulance services | GST-free | Emergency medical transport |
| Cosmetic surgery (elective) | Taxable 10% | NOT a health service if purely cosmetic |
| Veterinary services | Taxable 10% | Animal health, not human health |

#### Subdivision 38-C: Education [T1]

| Supply | GST Treatment | Condition |
|--------|---------------|-----------|
| Primary / secondary school fees | GST-free | Recognised school |
| University tuition | GST-free | Recognised higher education provider |
| TAFE / vocational training | GST-free | Registered Training Organisation (RTO) |
| Textbooks supplied with course | GST-free | Part of education supply |
| Commercial training / seminars | Taxable 10% | Not a recognised education course |
| Tutoring (private) | Taxable 10% | Not provided by recognised institution [T2] |

#### Subdivision 38-E: Exports [T1]

| Supply | GST Treatment | Condition |
|--------|---------------|-----------|
| Goods exported from Australia | GST-free | Must leave Australia within 60 days of supply |
| Services to non-resident (consumed offshore) | GST-free | Recipient outside Australia, not connected with Australia |
| Tourist Refund Scheme (TRS) | Refund at departure | Purchases > AUD 300 from single ABN, departed within 60 days |

#### Subdivision 38-D: Childcare [T1]

| Supply | GST Treatment |
|--------|---------------|
| Approved childcare (long day care, family day care) | GST-free |
| Before/after school care (registered) | GST-free |
| Occasional care (registered) | GST-free |
| Babysitting (private, unregistered) | Out of scope (unlikely to be enterprise) |

### 1.5 Input Taxed Supplies (No GST, No Credits) -- Lookup Table [T1]

**Legislation:** GST Act, Division 40.

| Supply Type | Section | BAS Label | Notes |
|-------------|---------|-----------|-------|
| Financial supplies (loans, credit, debt) | 40-5, Div 40 Regulation | G4 | Interest, loan fees, currency exchange margins. Reduced input tax credit (RITC) may apply at 75% for certain acquisitions. |
| Residential rent (existing premises) | 40-35 | G4 | Rental of existing residential property. Commercial rent is taxable. |
| Sale of existing residential premises | 40-65 | G4 | "Existing" = previously sold as residential, not new/substantially renovated |
| Sale of residential premises by non-developer | 40-65 | G4 | Private residence sales |
| Life insurance | 40-5 | G4 | General insurance is taxable |
| Share dealings and securities trading | 40-5 | G4 | Sale of shares, bonds, debentures |
| Borrowing and lending money | 40-5 | G4 | Interest income, loan origination |
| Dealing in foreign currency | 40-5 | G4 | Foreign exchange margins |
| Supply of school tuckshop items (certain) | 40-130 | G4 | School-operated fundraising |
| Supply of precious metals (subsequent dealings) | 40-100 | G4 | After first supply by refiner |

#### Financial Supplies Detail (Division 40, Subdivision 40-A) [T1]

**Legislation:** GST Act, s 40-5; Financial Supply (GST-Free) Determination; Reduced Credit Acquisitions Determination.

| Supply | Treatment | Notes |
|--------|-----------|-------|
| Interest income (lending) | Input taxed | No GST, no input credit |
| Interest expense (borrowing) | Input taxed acquisition | No credit for borrower |
| Loan origination fees | Input taxed | Financial supply |
| Credit card fees (issuer) | Input taxed | |
| Foreign exchange conversions | Input taxed | Margins, not commissions |
| Share brokerage commissions | Input taxed | But fee-for-service financial advice may be taxable |
| Guarantee fees | Input taxed | |
| Insurance premiums (life) | Input taxed | General insurance is taxable |
| Superannuation fund management | Input taxed | RITC may apply at 75% |

**Reduced Input Tax Credits (RITC):** Entities making financial supplies can claim a reduced credit (75% or 55%) on certain acquisitions specified in the *A New Tax System (Goods and Services Tax) (Particular Types of Acquisitions) Determination*. This applies to acquisitions of certain services such as:
- Legal services (75% RITC)
- Accounting/audit services (75% RITC)
- Actuarial services (75% RITC)
- IT services (75% RITC)
- Certain outsourced administrative services (55% RITC)

#### Residential Premises (Division 40, Subdivision 40-B) [T1]

| Supply | Treatment | Notes |
|--------|-----------|-------|
| Residential rent | Input taxed | No GST on residential lease |
| Sale of existing residential premises | Input taxed | Previously sold as residential |
| Sale of NEW residential premises | Taxable 10% | First sale after construction/substantial renovation |
| Commercial rent | Taxable 10% | NOT input taxed |
| Short-stay accommodation (hotel, Airbnb) | Taxable 10% | Commercial, not residential [T2 if ambiguous] |

### 1.6 Out-of-Scope Transactions (Not on BAS) [T1]

| Transaction Type | Reason |
|-----------------|--------|
| Wages, salaries, superannuation | Not a supply -- employment relationship |
| Dividends | Not a supply -- return on equity |
| Gifts / donations (no consideration) | No consideration = not a supply (unless token supply) |
| Loan principal repayments | Not a supply -- repayment of capital |
| GST payments to ATO | Tax payment, not a supply |
| Income tax payments | Tax payment, not a supply |
| Private transactions by individuals | Not in course of enterprise |
| Bank interest received (passive) | Input taxed if enterprise; out of scope if no enterprise |
| Directors fees (in some cases) | May be outside scope if not carrying on enterprise -- [T2] flag |

### 1.7 GST Rate Detail [T1]

Australia has a **single GST rate of 10%**. There are no reduced rates, super-reduced rates, or multiple rate tiers as found in EU VAT systems. No rate changes have been enacted for FY 2025-26.

**Legislation:** GST Act, s 9-70.

```
GST = Price x 1/11  (extracting GST from a GST-inclusive price)
GST = Price x 10%   (adding GST to a GST-exclusive price)
GST-inclusive price = GST-exclusive price x 1.1
GST-exclusive price = GST-inclusive price / 1.1
```

### 1.8 Taxable Supply Conditions [T1]

GST applies to **taxable supplies** made in Australia by a registered entity in the course of an enterprise. A supply is taxable if ALL of the following conditions are met (GST Act, s 9-5):

1. The supply is made for consideration;
2. The supply is made in the course or furtherance of an enterprise;
3. The supply is connected with the indirect tax zone (Australia);
4. The supplier is registered or required to be registered; AND
5. The supply is NOT GST-free and NOT input taxed.

---

## Step 2: BAS Label Assignment

### 2.1 Sales (Output) Labels -- Deterministic Lookup Table [T1]

| Label | Description | What to Report |
|-------|-------------|----------------|
| **G1** | Total sales | Total sales and income for the period (including GST-free and input taxed), excluding GST amount. This is GST-exclusive for GST-inclusive sales (back out the GST component). |
| **G2** | Export sales | GST-free export sales (Division 38, Subdivision 38-E). Zero-rated -- no GST charged but input credits retained. |
| **G3** | Other GST-free sales | GST-free sales that are NOT exports (e.g., basic food, health, education). Division 38, Subdivisions 38-A to 38-D and 38-F onwards. |
| **G4** | Input taxed sales | Supplies that are input taxed (Division 40): financial supplies, residential rent, sale of residential premises (not new). No GST charged, no input credits. |
| **G5** | G2 + G3 + G4 (derived) | Total GST-free and input taxed sales. |
| **G6** | G1 minus G5 (derived) | Total taxable sales (the base on which GST is calculated). |
| **G7** | Adjustments | Adjustments to GST on sales (e.g., bad debt relief, change of use, price adjustments). Division 19 adjustment events. |

### 2.2 Purchases (Input) Labels -- Deterministic Lookup Table [T1]

| Label | Description | What to Report |
|-------|-------------|----------------|
| **G10** | Capital purchases | Purchases of capital assets (plant, equipment, vehicles, property) on which GST was charged. GST-inclusive amount. |
| **G11** | Non-capital purchases | All other purchases (operational expenses, stock, overheads) on which GST was charged. GST-inclusive amount. |
| **G12** | G10 + G11 (derived) | Total purchases for the period. |
| **G13** | Purchases for making input taxed sales | Purchases related to making input taxed supplies (no credit available). |
| **G14** | Purchases with no GST in the price | Purchases from unregistered suppliers, GST-free purchases, wages, interest -- items with no GST component. |
| **G15** | Estimated purchases for private use | Private-use portion of business purchases (no credit available). |
| **G16** | G13 + G14 + G15 (derived) | Total non-creditable purchases. |
| **G17** | G12 minus G16 (derived) | Total creditable purchases. |
| **G18** | Adjustments | Adjustments to GST on purchases (Division 19, Division 129 -- change of use adjustments). |

### 2.3 Summary Tax Labels -- Deterministic Lookup Table [T1]

| Label | Description | Calculation |
|-------|-------------|-------------|
| **1A** | GST on sales | GST collected on taxable sales. Derived: G6 x 1/11 (if GST-inclusive) or computed from records. Plus G7 adjustments. |
| **1B** | GST on purchases | GST credits claimed on creditable purchases. Derived: G17 x 1/11 (if GST-inclusive) or computed from records. Plus G18 adjustments. |
| **1C** | Wine equalisation tax payable | WET on wholesale sales of wine (if applicable). |
| **1D** | Wine equalisation tax refundable | WET credits/refunds (if applicable). |
| **1E** | Luxury car tax payable | LCT on sales of luxury cars above threshold (if applicable). |
| **1F** | Luxury car tax refundable | LCT credits/refunds (if applicable). |

### 2.4 Non-GST Labels on the BAS [T1]

#### PAYG Withholding Labels

| Label | Description |
|-------|-------------|
| **W1** | Total salary, wages, and other payments |
| **W2** | Amount withheld from payments at W1 |
| **W3** | Amount withheld where no ABN is quoted |
| **W4** | Amount withheld from investment distributions (managed funds) |
| **W5** | Amount withheld from invoices where voluntary agreement to withhold |

#### PAYG Instalments Labels

| Label | Description |
|-------|-------------|
| **T1** | Instalment income |
| **T2** | Instalment rate (provided by ATO) |
| **T3** | New varied rate (if electing to vary) |
| **T4** | Reason code for variation |
| **T7** | Instalment amount (quarterly -- ATO provides amount) |
| **T8** | Varied instalment amount (if electing to vary) |
| **T9** | PAYG instalment amount (annual) |

#### FBT Instalment Labels

| Label | Description |
|-------|-------------|
| **F1** | ATO-calculated FBT instalment amount |
| **F2** | Varied FBT instalment amount (if electing to vary) |
| **F3** | Reason code for FBT variation |

### 2.5 Reporting Methods [T1]

| Method | Who Can Use It | What It Means |
|--------|---------------|---------------|
| **Calculation method** | Any registered entity | Report actual GST amounts from each transaction. Complete all G labels. |
| **Simpler BAS** | Turnover < $10M (default from 1 July 2017) | Report only G1, 1A, 1B. No need for G2-G18. Simplified reporting. |

**Legislation:** Taxation Administration Act 1953, Schedule 1, s 31-5; ATO Simpler BAS guidance.

### 2.6 Lodgement Channels [T1]

- **ATO Business Portal** (bp.ato.gov.au) -- primary online lodgement for businesses
- **myGov** (my.gov.au) -- for sole traders linking to ATO services
- **Standard Business Reporting (SBR)** -- direct lodgement from accounting software (Xero, MYOB, QuickBooks)
- **Registered tax agent / BAS agent** -- via ATO portals with agent credentials
- **Paper BAS** -- only if ATO has not required electronic lodgement

---

## Step 3: Reverse Charge Mechanics

### 3.1 When Reverse Charge Applies [T1]

**Legislation:** GST Act, Division 83 (offshore intangible supplies); Division 84 (reverse charge on offshore supplies to registered recipients).

The reverse charge mechanism in Australian GST is narrower than in EU VAT. It applies primarily in these situations:

### 3.2 Reverse Charge on Offshore Intangible Supplies (Division 84) [T1]

**When it applies:** A registered recipient must account for GST on an acquisition from a non-resident supplier where:

1. The supply is of an intangible thing (services, rights, digital products);
2. The supply is connected with Australia (s 9-25);
3. The supplier is not registered (or not required to be registered) for Australian GST;
4. The recipient is registered for GST; AND
5. The recipient acquires the supply for a purpose that is **not fully creditable** (i.e., some or all use is for making input taxed supplies or for private purposes).

**Key distinction from EU VAT:** In Australia, if the recipient would be entitled to a **full input tax credit** anyway, the reverse charge does NOT apply. The logic is: if the recipient would claim back 100% of the GST, there is no revenue leakage, so no need to self-assess.

**Legislation:** GST Act, s 84-5 (reverse charge on offshore supplies).

```
Reverse charge applies ONLY IF:
  Recipient is registered AND
  Acquisition is NOT fully creditable (some non-creditable use)
```

### 3.3 "Netflix Tax" -- GST on Digital Supplies to Consumers (Division 83-5) [T1]

**Legislation:** GST Act, Subdivision 40-A (as amended by Treasury Laws Amendment (GST Low Value Goods) Act 2017).

Since 1 July 2017, **non-resident suppliers** of digital products and services to **Australian consumers** (B2C) must:

1. Register for GST if Australian turnover exceeds $75,000;
2. Charge and remit GST at 10% on supplies to Australian consumers;
3. Lodge a simplified GST return (no input tax credits claimable under simplified registration).

**Applies to:**
- Streaming services (Netflix, Spotify, Disney+)
- Digital downloads (apps, e-books, music, games)
- Online professional services
- Cloud computing / SaaS provided to consumers
- Gambling services provided by offshore operators

**Does NOT apply to B2B supplies** where the Australian recipient provides their ABN (registered for GST). In B2B, the reverse charge mechanism in Division 84 applies instead (if the acquisition is not fully creditable).

### 3.4 Reverse Charge on Real Property Supplies [T1]

**Legislation:** GST Act, s 9-25(5) and s 84-5.

Certain supplies of real property connected with Australia by a non-resident may trigger reverse charge obligations on the registered recipient.

### 3.5 Reverse Charge -- BAS Reporting [T1]

When reverse charge applies:

| Element | BAS Treatment |
|---------|--------------|
| Output GST (self-assessed) | Include in **1A** (GST on sales) |
| Input tax credit (if any) | Include in **1B** (GST on purchases) |
| Net effect for fully input taxed use | 1A amount with no 1B offset = net cost |
| Net effect for partially creditable use | 1A amount, partial 1B offset |

**Both sides must appear on the BAS. The reverse charge amount is not reported in G1 (total sales) -- it appears only in the tax labels 1A and 1B.**

### 3.6 Comparison with EU Reverse Charge [T2]

| Feature | Australia | EU VAT |
|---------|-----------|--------|
| B2B services from non-resident | Reverse charge ONLY if not fully creditable | Reverse charge ALWAYS (Art. 196 VAT Directive) |
| B2C digital supplies from non-resident | Supplier registers and charges GST (Netflix tax) | Supplier registers via OSS/IOSS and charges VAT |
| Intra-community supplies | N/A (no equivalent to EU single market) | Zero-rated with reverse charge in destination state |
| Domestic reverse charge | Limited (e.g., certain real property, gold) | Expanded in many member states (construction, electronics) |

---

## Step 4: Deductibility Check

### 4.1 Entitlement to Input Tax Credits [T1]

**Legislation:** GST Act, Division 11.

A registered entity is entitled to an input tax credit for a creditable acquisition if ALL of the following are satisfied (s 11-5):

1. The acquisition is for a **creditable purpose** (related to making taxable supplies or GST-free supplies);
2. The supply was a **taxable supply** (GST was included in the price);
3. The entity provides **consideration** for the supply;
4. The entity is **registered** for GST; AND
5. The entity holds a **tax invoice** (or can produce one within a reasonable time).

### 4.2 Creditable Purpose Test [T1]

**Legislation:** GST Act, s 11-15.

An acquisition is for a creditable purpose to the extent it is acquired in carrying on the enterprise, EXCEPT to the extent:
- It relates to making **input taxed** supplies; OR
- It is of a **private or domestic** nature.

### 4.3 Blocked Input Tax Credits -- Deterministic Lookup Table [T1]

The following acquisitions do NOT give rise to input tax credits even if used in an enterprise:

| Blocked Category | Legislation | Reason |
|-----------------|-------------|--------|
| Acquisitions relating to making input taxed supplies | s 11-15(2)(a) | No credit for costs of producing input taxed supplies |
| Private or domestic use | s 11-15(2)(b) | Not for enterprise purposes |
| Entertainment (non-deductible under income tax) | s 69-5 | FBT interaction: if entertainment is subject to FBT, the employer CAN claim GST credits. If entertainment is exempt from FBT (e.g., minor benefit < $300), no GST credit. |
| Non-deductible expenses (fines, penalties) | s 69-5 | No credit if expense not deductible for income tax (subject to exceptions) |
| Membership fees for social/sporting clubs (non-deductible portion) | s 69-5 | Follows income tax deductibility |
| Residential accommodation for employees | s 69-10 | Specifically excluded |

### 4.4 Motor Vehicles and the Luxury Car Tax (LCT) Threshold [T1]

There is **no specific GST block on motor vehicle purchases** in Australia (unlike Malta's 10th Schedule motor vehicle block). A registered entity can claim full GST credits on a motor vehicle purchased for business use.

**However**, the input tax credit for a car is limited by the **car limit** (also known as the depreciation cost limit for income tax purposes):

| Financial Year | Car Limit (Income Tax) | LCT Threshold (Fuel-Efficient) | LCT Threshold (Other) |
|---------------|----------------------|-------------------------------|----------------------|
| 2024-25 | $69,674 | $91,387 | $76,950 |
| 2025-26 | TBA (indexed annually) | TBA | TBA |

**GST credit cap for cars (s 69-10):**
- Maximum GST credit = Car limit / 11
- For 2024-25: Maximum credit = $69,674 / 11 = $6,334 (approximately)
- If car costs more than the car limit, GST credit is capped at the limit amount

**Luxury Car Tax (LCT):**
- LCT applies to cars above the LCT threshold at **33%** of the value above the threshold
- LCT is a separate tax from GST, reported at labels 1E/1F on the BAS
- Fuel-efficient vehicles have a higher threshold

**Legislation:** GST Act, s 69-10 (car limit); A New Tax System (Luxury Car Tax) Act 1999.

### 4.5 Tax Invoices [T1]

**Legislation:** GST Act, Division 29 (tax invoices), s 29-70.

To claim an input tax credit, the entity must hold a **tax invoice** at the time of lodging the BAS (or obtain one within 4 years). A valid tax invoice must include:

| Requirement | For Supplies < $1,000 | For Supplies >= $1,000 |
|------------|----------------------|----------------------|
| Marked "Tax Invoice" | Yes | Yes |
| Supplier's identity (name, ABN) | Yes | Yes |
| Date of issue | Yes | Yes |
| Brief description of supply | Yes | Yes |
| GST amount (or that price includes GST) | Yes | Yes |
| Recipient's identity (name, ABN) | No | Yes |
| Quantity / volume | No | Yes |

**No ABN withholding:** If a supplier does not provide an ABN on their invoice, the payer must withhold 47% from the payment (top marginal rate + Medicare levy) and remit to ATO. This is reported at BAS label W3. Exceptions apply for supplies < $75 (excl. GST) and certain listed exemptions.

### 4.6 Apportionment for Mixed-Use Acquisitions [T2]

**Legislation:** GST Act, Division 11 (s 11-30); Division 129 (changes in creditable purpose).

Where an acquisition is used partly for a creditable purpose and partly for a non-creditable purpose (e.g., partly for taxable supplies, partly for input taxed supplies, or partly private):

```
Input tax credit = Full GST x (Creditable use % / 100)
```

**Methods of apportionment** (ATO accepts any fair and reasonable method):
- Direct allocation (transaction-by-transaction)
- Turnover-based percentage (taxable turnover / total turnover)
- Floor-area method (for property-related costs)
- Time-based method
- Number of units / outputs method

**Division 129 adjustments:** If the actual use in a subsequent period differs from the original intended use, an adjustment is required. Adjustments continue for the adjustment period:
- General acquisitions: 2 adjustment periods (years)
- Real property / improvements to real property: 10 adjustment periods
- Other capital acquisitions: 5 adjustment periods

**Flag for reviewer: Apportionment methodology must be documented and consistently applied. Tax agent should confirm the chosen method is fair and reasonable.**

---

## Step 5: Derived Calculations

### 5.1 BAS Derived Fields [T1]

```
G5  = G2 + G3 + G4
G6  = G1 - G5
G12 = G10 + G11
G16 = G13 + G14 + G15
G17 = G12 - G16

1A  = GST collected on sales (from records) + G7 adjustments
1B  = GST paid on creditable purchases (from records) + G18 adjustments

GST_payable = 1A - 1B

IF GST_payable > 0 THEN
  Net amount owing to ATO
ELSE
  Net refund from ATO
END

Total BAS liability = GST_payable + W2 + W3 + W4 + W5 + PAYG_instalment + FBT_instalment + 1C - 1D + 1E - 1F
```

---

## Step 6: Key Thresholds

### 6.1 Registration Thresholds [T1]

**Legislation:** GST Act, Division 23 (who is required to be registered), s 23-5.

| Entity Type | GST Turnover Threshold | Measurement |
|-------------|----------------------|-------------|
| General business | **$75,000** per year | Current or projected GST turnover |
| Non-profit organisation | **$150,000** per year | Current or projected GST turnover |
| Taxi / rideshare driver | **$1** (effectively nil) | Must register regardless of turnover |
| Non-resident supplying digital products to AU consumers | **$75,000** per year | Australian turnover |

**GST turnover** (s 188-15) includes the value of all taxable supplies and GST-free supplies but EXCLUDES:
- Input taxed supplies
- Supplies not connected with Australia
- Supplies not for consideration
- Sales of capital assets (unless regularly dealing in those assets)

### 6.2 Voluntary Registration [T1]

Entities below the threshold may **voluntarily register** if they carry on an enterprise. Benefits of voluntary registration:
- Can claim input tax credits on business purchases
- May appear more professional to commercial clients
- Required to charge GST on taxable supplies once registered

**Warning:** Once registered, the entity MUST charge GST on all taxable supplies and lodge BAS returns. Cannot selectively apply GST. Must remain registered for at least 12 months.

### 6.3 ABN (Australian Business Number) [T1]

**Legislation:** A New Tax System (Australian Business Number) Act 1999.

- An ABN is required before registering for GST
- ABN format: **11 digits** (2-digit check digits + 9-digit identifier based on former TFN or allocated number)
- ABN is NOT the same as a TFN (Tax File Number) or ACN (Australian Company Number)
- ABN validation: Modulus 89 check algorithm

### 6.4 Registration Process [T1]

1. Obtain an ABN (via Australian Business Register, abr.gov.au)
2. Register for GST via:
   - ATO Business Portal
   - myGov (linked to ATO)
   - Registered tax agent
   - Phone (13 28 66)
3. Choose reporting period (monthly or quarterly; annual if eligible)
4. Choose accounting basis (cash or accrual)

### 6.5 Cancelling Registration [T1]

An entity must cancel GST registration if:
- GST turnover falls below $75,000 ($150,000 non-profit) AND the entity does not wish to remain registered
- The entity ceases to carry on an enterprise

**Legislation:** GST Act, s 25-50 to 25-57.

### 6.6 Small Business Entity (SBE) Concessions [T1]

**Legislation:** ITAA 1997, Division 328 (small business entity).

Entities with **aggregated turnover < $10M** qualify as SBEs and can access:

| Concession | Description |
|-----------|-------------|
| Simpler BAS | Report G1, 1A, 1B only |
| Cash accounting | Regardless of entity type |
| Annual apportionment | One annual GST adjustment instead of each period |
| PAYG quarterly instalments | ATO-calculated amount |
| Simplified depreciation | Immediate write-off for assets under threshold |
| Two-year amendment period | Reduced from 4 years |

### 6.7 GST Instalment Method [T1]

Small businesses can elect to pay GST by **instalment** instead of calculating actual GST each quarter:

- ATO calculates and notifies instalment amount (label T7 equivalent for GST)
- Entity pays the notified amount each quarter
- Annual reconciliation -- actual GST is calculated for the full year, with a balancing payment or refund
- Reduces compliance burden but may result in overpayment or underpayment during the year

### 6.8 Cash vs. Accrual Basis [T1]

**Legislation:** GST Act, Division 29 (accounting basis), s 29-40 (cash basis), s 29-5 (accrual basis).

| Feature | Cash Basis | Accrual Basis |
|---------|-----------|---------------|
| When GST on sales is reported | When payment is **received** | When invoice is **issued** |
| When input credits are claimed | When payment is **made** | When invoice is **received** |
| Who can use it | GST turnover < $2M (or $10M with SBE concession) | Anyone |
| Advantage | Defers GST payment on unpaid invoices | Matches to accounting periods |

**Election:** Entities eligible for cash basis must elect at registration or notify the ATO of a change. Once on cash basis, must remain for at least 12 months.

---

## Step 7: Filing Deadlines

### 7.1 BAS Lodgement and Payment Deadlines [T1]

**Legislation:** Taxation Administration Act 1953, Schedule 1, Division 31.

| Reporting Period | Who | Lodgement & Payment Deadline | Notes |
|-----------------|-----|------------------------------|-------|
| **Monthly** | Turnover > $20M; or voluntary election | **21st of the following month** | E.g., January BAS due 21 February |
| **Quarterly** (standard) | Turnover <= $20M | **28th of the month after the quarter ends** | See quarterly schedule below |
| **Quarterly** (with tax agent) | Using a registered tax agent | Tax agent concession may apply (varies) | Typically 4 additional weeks |
| **Annual** | Voluntary annual reporters (turnover < $75,000 and voluntarily registered) | **28 February** following the financial year | FY ends 30 June |

#### Quarterly BAS Schedule [T1]

| Quarter | Period | Due Date |
|---------|--------|----------|
| Q1 | 1 July -- 30 September | **28 October** |
| Q2 | 1 October -- 31 December | **28 February** |
| Q3 | 1 January -- 31 March | **28 April** |
| Q4 | 1 April -- 30 June | **28 July** |

**Note:** If a due date falls on a weekend or public holiday, the deadline is the next business day.

### 7.2 Penalties for Late Lodgement [T1]

**Legislation:** Taxation Administration Act 1953, s 286-75 (failure to lodge on time).

**Failure to Lodge (FTL) penalty:**

| Entity Size | Penalty per 28-day period | Maximum Periods |
|------------|--------------------------|-----------------|
| Small entity (turnover < $1M) | 1 penalty unit | 5 periods |
| Medium entity ($1M - $20M) | 2 penalty units | 5 periods |
| Large entity ($20M - $100M) | 5 penalty units | 5 periods |
| Very large entity (> $100M) | 10 penalty units | 5 periods |

**Penalty unit value:** $330 (2024-25, indexed annually under Crimes Act 1914). Maximum FTL penalty = 5 x penalty units applicable.

### 7.3 General Interest Charge (GIC) [T1]

**Legislation:** Taxation Administration Act 1953, s 8AAB to 8AAH.

GIC applies to unpaid tax debts from the due date until the date of payment. The GIC rate is set quarterly by the ATO:

```
GIC rate = 90-day Bank Accepted Bill rate + 7% per annum
```

GIC is calculated daily and compounded. It is **tax deductible** for income tax purposes.

### 7.4 Shortfall Penalties [T1]

**Legislation:** Taxation Administration Act 1953, s 284-75 to 284-90.

If the BAS understates net GST:

| Behaviour | Base Penalty |
|-----------|-------------|
| Reasonable care not taken | 25% of shortfall |
| Recklessness | 50% of shortfall |
| Intentional disregard | 75% of shortfall |

Penalties can be reduced by 20% (voluntary disclosure before ATO audit) or increased by 20% (prior offences).

---

## Step 8: Australia-Specific Sections

### 8.1 Comparison with EU VAT [T1]

| Feature | Australian GST | EU VAT (Directive 2006/112/EC) |
|---------|---------------|-------------------------------|
| **Number of rates** | 1 (10%) | 2-4 per member state (standard, reduced, super-reduced, parking) |
| **Standard rate** | 10% | 15% minimum; ranges from 17% (Luxembourg) to 27% (Hungary) |
| **Reduced rates** | None | At least one reduced rate per member state (typically 5-13%) |
| **Zero-rated (with credit)** | Yes -- "GST-free" (Division 38) | Yes -- but scope varies by member state |
| **Exempt without credit** | Yes -- "Input taxed" (Division 40) | Yes -- "Exempt" (Art. 132-137 VAT Directive) |
| **Registration threshold** | $75,000 AUD (~EUR 45,000) | Varies: EUR 0 (Sweden) to EUR 85,000 (UK, pre-Brexit) |
| **Filing frequency** | Monthly (>$20M) / Quarterly / Annual | Monthly or quarterly (varies by member state) |
| **Return form** | BAS (Business Activity Statement) | VAT return (varies by member state; e.g., VAT3 in Malta, UStVA in Germany) |
| **Tax authority** | ATO (single federal authority) | National tax authority per member state (e.g., CFR Malta, HMRC UK) |
| **Intra-community supplies** | N/A | Zero-rated supply + acquisition in destination state |
| **Reverse charge (B2B cross-border)** | Only if not fully creditable | Always on cross-border B2B services (Art. 196) |
| **Input tax credit blocking** | Limited (entertainment via FBT, car limit cap) | Varies widely by member state (e.g., Malta 10th Schedule blocks vehicles, entertainment, tobacco, alcohol) |
| **Capital goods scheme** | Division 129 adjustments (2/5/10 year periods) | Yes -- adjustment periods vary (e.g., 5-20 years depending on member state) |
| **Invoice requirements** | Tax invoice (Division 29) | VAT invoice (Art. 226 VAT Directive) |
| **Bad debt relief** | Yes (Division 21, after 12 months) | Yes (varies by member state; some require 6-12 months) |
| **GST groups / VAT groups** | Yes (Division 48) | Yes (Art. 11 VAT Directive, optional for member states) |
| **Margin scheme** | Yes (Division 75, property) | Yes (Art. 311-325, second-hand goods, art, etc.) |
| **Digital services to consumers** | Netflix tax (supplier registers) | OSS/IOSS (supplier registers in one member state) |

### 8.2 Key Differences for Practitioners [T1]

1. **Single rate simplicity:** Australia's single 10% rate eliminates rate-classification complexity that plagues EU VAT (which rate applies to which food item varies by member state).

2. **Reverse charge trigger:** In Australia, reverse charge on offshore supplies to registered recipients applies ONLY when the acquisition is not fully creditable. In the EU, reverse charge applies to ALL B2B cross-border services regardless of credit position. This is a fundamental difference.

3. **No intra-community regime:** Australia has no equivalent to EU intra-community acquisitions/supplies. There is no single market with zero-rated dispatches and taxed acquisitions.

4. **Entertainment deductibility:** In Australia, the GST credit for entertainment follows FBT treatment (credit if FBT is paid; no credit if FBT exempt). In Malta/EU, entertainment is simply blocked (10th Schedule in Malta, similar blocks in other EU states).

5. **Motor vehicle treatment:** Australia does not block GST credits on cars outright (unlike Malta's 10th Schedule). Instead, it caps the credit at the car limit / 11. A fully business-use car under the car limit gets full credit.

6. **Financial supplies (input taxed):** Both systems deny input credits for costs of financial supplies. However, Australia provides Reduced Input Tax Credits (75%/55%) for certain service acquisitions by financial suppliers. The EU has no direct equivalent (though some member states have sector-specific schemes).

### 8.3 Out of Scope -- Income Tax and Superannuation (Reference Only) [T3]

This skill does not compute income tax or superannuation obligations. The following is reference information only. Do not execute any of these rules. Escalate to registered tax agent.

- **Company tax rate:** 25% (base rate entity, turnover < $50M) or 30% (other companies). Individuals: progressive rates 0% / 16% / 30% / 37% / 45% (2024-25; rates subject to change from Stage 3 tax cuts).
- **Superannuation Guarantee:** Employers must pay SG at 12% (2025-26, rising from 11.5% in 2024-25) of ordinary time earnings to employees' super funds.
- **PAYG withholding:** Employer obligation for wages; reported on BAS at W1/W2 labels.
- **PAYG instalments:** Prepayment of income tax; reported on BAS at T1/T7/T8 labels.
- **FBT:** Fringe Benefits Tax at 47% (gross-up) on non-cash employee benefits. BAS labels F1/F2.
- **Depreciation:** Effective life / diminishing value or prime cost methods. SBE instant asset write-off for assets under threshold.

---

## PROHIBITIONS [T1]

- **NEVER** let AI guess BAS label assignment -- it is deterministic from the transaction classification rules in this skill.
- **NEVER** apply GST to a supply that is GST-free (Division 38) or input taxed (Division 40).
- **NEVER** claim input tax credits for acquisitions related to making input taxed supplies.
- **NEVER** claim input tax credits without a valid tax invoice (or evidence the entity can obtain one within 4 years).
- **NEVER** apply reverse charge to an offshore acquisition that is fully creditable -- reverse charge only applies when the acquisition is NOT fully creditable.
- **NEVER** confuse GST-free (Division 38, credits retained) with input taxed (Division 40, credits denied). These are fundamentally different and produce opposite input tax credit outcomes.
- **NEVER** apply GST to out-of-scope transactions (wages, dividends, loan repayments, tax payments, private transactions).
- **NEVER** exceed the car limit when calculating input tax credits on car purchases.
- **NEVER** apply WET to beer or spirits (WET is wine only; beer and spirits are subject to excise).
- **NEVER** register a non-resident digital supplier for full GST registration if they should be on simplified registration (no input tax credits under simplified registration).
- **NEVER** allow an unregistered entity to charge GST on invoices.
- **NEVER** report reverse charge amounts in G1 (total sales) -- reverse charge self-assessment appears in 1A and 1B only.
- **NEVER** apply the margin scheme to a property where the seller received full GST credits on the original acquisition.
- **NEVER** compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Edge Case Registry

### EC1 -- Going Concern (GST-Free) [T1]

**Situation:** Client sells an entire business as a going concern.
**Resolution:** The supply is GST-free if ALL conditions are met (GST Act, s 38-325):
1. The supply is of a going concern (the business will continue to operate);
2. Both supplier and recipient are registered for GST;
3. The parties have agreed **in writing** that the supply is a going concern.

If ANY condition is not met, the sale is taxable at 10%. No partial going concern -- it applies to the entire supply or not at all.
**BAS treatment:** G3 (other GST-free sales). Input tax credits on costs of the sale (legal, accounting) are fully claimable.
**Legislation:** GST Act, Subdivision 38-J, s 38-325.

### EC2 -- Margin Scheme for Property [T2]

**Situation:** Developer sells residential or commercial property and elects to use the margin scheme.
**Resolution:** Under the margin scheme (GST Act, Division 75):
- GST is calculated on the **margin** (sale price minus original purchase price), not the full sale price
- GST = Margin x 1/11
- Seller must notify the buyer in writing that the margin scheme is being used
- Buyer CANNOT claim input tax credits on the purchase
- Only available where seller acquired property without full GST credits (e.g., from unregistered seller, or from a supply that was input taxed or GST-free)

**Flag for reviewer: Margin scheme election has significant implications for both parties. Tax agent must confirm eligibility and advise on implications before election.**
**Legislation:** GST Act, Division 75 (margin scheme).

### EC3 -- Wine Equalisation Tax (WET) [T1]

**Situation:** Client is a wine producer or wholesale wine dealer.
**Resolution:** WET is a separate tax at **29%** of the wholesale value of wine (including grape wine, fruit wine, cider, perry, mead, sake). WET is in ADDITION to GST.

| Element | Treatment |
|---------|-----------|
| WET liability | 29% of assessable dealing value (wholesale) |
| WET producer rebate | Up to $350,000 per financial year for eligible producers |
| BAS reporting | Labels 1C (WET payable) and 1D (WET refundable) |
| GST on wine | GST applies to the WET-inclusive price |

**Legislation:** A New Tax System (Wine Equalisation Tax) Act 1999.
**Note:** WET does NOT apply to beer or spirits (these are subject to excise duty instead).

### EC4 -- Luxury Car Tax (LCT) [T1]

**Situation:** Client (car dealer) sells a car above the LCT threshold.
**Resolution:** LCT applies at **33%** of the amount by which the GST-inclusive value exceeds the LCT threshold.

| Element | 2024-25 Value |
|---------|--------------|
| LCT threshold (general) | $76,950 |
| LCT threshold (fuel-efficient) | $91,387 |
| LCT rate | 33% |
| BAS reporting | Labels 1E (LCT payable), 1F (LCT refundable) |

```
LCT = (GST-inclusive value - LCT threshold) x 10/11 x 33%
```

**Fuel-efficient vehicle:** Must have a fuel consumption of 7L/100km or less (combined city/highway cycle).
**Legislation:** A New Tax System (Luxury Car Tax) Act 1999; LCT threshold indexed annually.

### EC5 -- Financial Supply (Input Taxed) vs. Fee-Based Financial Service (Taxable) [T2]

**Situation:** Financial institution charges a fee for financial advice or account-keeping services.
**Resolution:** The distinction is critical:

| Supply | Treatment | Reasoning |
|--------|-----------|-----------|
| Interest on loans | Input taxed | Financial supply (Division 40) |
| Loan establishment fees | Input taxed | Part of financial supply |
| Financial advice fees | Taxable 10% | Fee-for-service, not a financial supply |
| Account-keeping fees | Taxable 10% | Administrative service, not a financial supply |
| Brokerage commissions | Input taxed | Dealing in securities is a financial supply |
| Fee-based financial planning | Taxable 10% | Advisory service, not a financial supply itself |

**Flag for reviewer: The boundary between fee-based services (taxable) and financial supplies (input taxed) can be ambiguous. Tax agent should confirm classification for each revenue line.**
**Legislation:** GST Act, Division 40; A New Tax System (Goods and Services Tax) Regulations 2019, Subdivision 40-A.

### EC6 -- Non-Resident Digital Supply (Supplier Registration) [T1]

**Situation:** Non-resident digital platform supplies streaming services, apps, or digital content to Australian consumers.
**Resolution:**
- Supplier must register for GST if Australian turnover > $75,000
- Supplier charges 10% GST on B2C supplies
- Supplier lodges simplified GST returns (quarterly)
- Supplier under simplified registration **cannot** claim input tax credits
- If recipient provides ABN (B2B), supplier does NOT charge GST; reverse charge may apply to recipient instead

**BAS treatment (for recipient, if reverse charge applies):** Include self-assessed GST in 1A; claim credit in 1B if fully creditable.
**Legislation:** GST Act, Subdivision 40-A (as amended); Treasury Laws Amendment (GST Low Value Goods) Act 2017.

### EC7 -- Hire Purchase / Chattel Mortgage [T2]

**Situation:** Client acquires an asset under a hire purchase agreement.
**Resolution:**
- **Hire purchase:** For GST purposes, treated as a supply of the goods at inception (not a series of rental supplies). Full GST is payable on the cash price at the start. Buyer claims full input tax credit at inception (if entitled).
- **Chattel mortgage:** The financier lends money (financial supply, input taxed). The asset purchase is a separate taxable supply. GST credit is claimed on the asset purchase, not on the finance charges.
- **Operating lease:** Each lease payment is a taxable supply. GST credit claimed on each lease payment.

**Flag for reviewer: Hire purchase vs. operating lease distinction affects timing of GST credits. Tax agent should confirm the arrangement type from the contract.**
**Legislation:** GST Act, Division 156 (hire purchase, supply and acquisition).

### EC8 -- Second-Hand Goods (No Tax Invoice) [T1]

**Situation:** Dealer purchases second-hand goods from an unregistered private individual (no GST charged, no tax invoice available).
**Resolution:**
- No GST was charged on the purchase, so normally no input tax credit
- HOWEVER, Division 66 provides a **notional input tax credit** for second-hand goods purchased from unregistered sellers for the purpose of resale
- Credit = Purchase price x 1/11
- Must maintain records: seller's name, address, description of goods, date, and price paid
- Does NOT apply to real property or financial supplies

**BAS treatment:** Include the notional credit in 1B (GST on purchases).
**Legislation:** GST Act, Division 66 (second-hand goods), s 66-5.

### EC9 -- GST Groups [T2]

**Situation:** A group of related entities wants to form a GST group to simplify reporting.
**Resolution:**
- Members of a GST group are treated as a single entity for GST purposes (GST Act, Division 48)
- One member (the "representative member") lodges the BAS for the entire group
- Intra-group supplies are disregarded (no GST on transactions between group members)
- Requirements: all members must be registered, related (90% common ownership), and have the same tax periods

**Conditions:**
- Each member must satisfy the membership requirements in s 48-10
- The representative member is liable for all GST obligations of the group
- Members remain jointly and severally liable for the group's GST debts

**Flag for reviewer: GST grouping has significant implications. Tax agent must review eligibility, prepare grouping application, and manage ongoing compliance.**
**Legislation:** GST Act, Division 48 (GST groups).

### EC10 -- Adjustment Events (Division 19) [T1]

**Situation:** After a BAS has been lodged, the price of a supply changes (credit note, refund, price adjustment, bad debt).
**Resolution:**
- An **adjustment event** occurs when the consideration for a supply changes, a supply is cancelled, or a supply becomes or ceases to be a taxable supply (s 19-10)
- The adjustment is reported on the BAS for the period in which the adjustment event occurs
- Increasing adjustments (more GST payable): increase 1A
- Decreasing adjustments (less GST payable): decrease 1A or increase 1B (depending on whether it relates to sales or purchases)

**Bad debts specifically:**
- If a debt is written off as bad (12 months overdue), the supplier can claim back the GST previously remitted (decreasing adjustment)
- The debtor must repay the input tax credit previously claimed (increasing adjustment)
- **Legislation:** GST Act, Division 21 (bad debts), s 21-5 to 21-15.

**BAS treatment:** Adjustments go into G7 (adjustments on sales) or G18 (adjustments on purchases) on full BAS. On Simpler BAS, adjustments are incorporated into 1A / 1B directly.
**Legislation:** GST Act, Division 19 (adjustment events).

### EC11 -- Lay-By Sales [T1]

**Situation:** Retailer sells goods on a lay-by arrangement (customer pays in instalments before taking delivery).
**Resolution:**
- GST is accounted for when the supply is made (delivery of goods), NOT when deposits are received
- **Accrual basis:** GST liability arises at delivery, regardless of payment timing
- **Cash basis:** GST liability arises as each payment is received
- If the lay-by is cancelled and a cancellation fee is charged, that fee is a separate taxable supply

**Legislation:** GST Act, s 99-5 to 99-10 (lay-by sales).

### EC12 -- Gift Vouchers and Prepaid Cards [T1]

**Situation:** Business sells gift vouchers / gift cards.
**Resolution:**
- The sale of the voucher itself is NOT a taxable supply (it is a supply of a chose in action / right to receive future supply)
- GST is accounted for when the voucher is **redeemed** (the underlying supply is made)
- If the voucher expires unredeemed, no GST is payable (no supply occurred)
- Exceptions: face-value vouchers for a specific taxable supply may trigger GST at point of sale

**Legislation:** GST Act, Division 100 (vouchers), s 100-5 to 100-25.

### EC13 -- Insurance Settlements and Payouts [T1]

**Situation:** Insured business receives an insurance payout for a claim.
**Resolution:**
- Insurance payouts are generally NOT a supply by the insured (they are consideration for the insurer's supply of insurance services)
- The insured does NOT charge GST on receiving a payout
- HOWEVER, if the payout is for loss/damage to a business asset, there may be a **decreasing adjustment** if the insured previously claimed input tax credits on the asset
- The insurer is entitled to an input tax credit for the settlement payment if it relates to a creditable acquisition (s 78-10)

**Legislation:** GST Act, Division 78 (insurance).

### EC14 -- Barter and Non-Monetary Consideration [T1]

**Situation:** Two businesses exchange goods or services without cash changing hands.
**Resolution:**
- GST applies to barter transactions because there IS consideration (the goods/services received in exchange)
- Each party is making a taxable supply
- The GST-inclusive market value of what is received is the consideration for the supply made
- Both parties must issue tax invoices and account for GST

**Legislation:** GST Act, s 9-15 (consideration), s 9-75 (GST-inclusive market value).

### EC15 -- Deposits and Progress Payments (Construction) [T2]

**Situation:** Builder receives progress payments during a construction project.
**Resolution:**
- **Accrual basis:** GST is reported as each progress claim is issued (regardless of payment)
- **Cash basis:** GST is reported as each progress payment is received
- Retention amounts: GST on retained amounts is reported when the retention is released (cash basis) or when the entitlement arises (accrual basis)
- Defects period holdbacks follow the same logic

**Flag for reviewer: Construction progress claims and retentions can create complex timing differences. Tax agent should review contract terms and accounting basis.**
**Legislation:** GST Act, Division 156 (progressive supplies).

### EC16 -- Taxi and Rideshare Services [T1]

**Situation:** Individual provides taxi or rideshare services (Uber, Ola, DiDi).
**Resolution:**
- **Must register for GST regardless of turnover** (s 144-5 -- supplies of taxi travel)
- GST at 10% applies to all fares
- Input tax credits available on vehicle running costs, fuel, maintenance, phone/data (to the extent of business use)
- Private use percentage must be excluded from input tax credits
- Platform fees (Uber commission) include GST; credit is claimable

**Legislation:** GST Act, s 144-5 (taxi travel); ATO Ruling GSTR 2003/14.

### EC17 -- Grants and Government Subsidies [T2]

**Situation:** Business receives a government grant or subsidy.
**Resolution:**
- If the grant is consideration for a supply to the government (e.g., a service agreement), it is a **taxable supply** and GST applies
- If the grant is a **no-strings-attached** payment (no supply in return), it is NOT consideration for a supply, and NO GST applies
- Many grants fall in a grey area -- [T2] flag

**Flag for reviewer: Whether a government grant is consideration for a supply depends on the terms. Tax agent must review the funding agreement.**
**Legislation:** GST Act, s 9-15 (consideration); GSTR 2012/2 (grants of financial assistance).

---

## Test Suite

### Test 1 -- Standard Local Purchase, 10% GST, Non-Capital [T1]

**Input:** Australian supplier, office supplies, GST-inclusive AUD $220, GST $20, net $200. Entity is GST-registered. Business use 100%.
**Expected output:**
- G11 (non-capital purchases) = $220
- 1B includes $20 input tax credit
- Full credit claimed.

### Test 2 -- Taxable Sale, 10% GST [T1]

**Input:** GST-registered entity invoices Australian customer for consulting services. Invoice: $5,500 GST-inclusive ($5,000 + $500 GST).
**Expected output:**
- G1 (total sales) = $5,000 (GST-exclusive)
- G6 (taxable sales, derived) = $5,000
- 1A includes $500 GST on sales.

### Test 3 -- Export Sale, GST-Free [T1]

**Input:** GST-registered entity exports goods to New Zealand customer. Invoice: $10,000, no GST charged. Goods shipped within 60 days.
**Expected output:**
- G1 = $10,000
- G2 (export sales) = $10,000
- G6 (taxable sales) = $0 (G1 - G5 where G5 includes G2)
- 1A = $0 (no GST on GST-free supply)
- Input credits on related costs (packaging, freight) fully claimable.

### Test 4 -- Residential Rent (Input Taxed) [T1]

**Input:** GST-registered entity receives $2,000/month residential rental income from investment property.
**Expected output:**
- G1 = $2,000
- G4 (input taxed sales) = $2,000
- G6 = $0
- 1A = $0
- Input tax credits on property expenses (repairs, agent fees) = BLOCKED (related to input taxed supply).

### Test 5 -- Capital Purchase (Vehicle Under Car Limit) [T1]

**Input:** GST-registered business purchases a delivery van for $44,000 GST-inclusive ($40,000 + $4,000 GST). 100% business use. Under car limit.
**Expected output:**
- G10 (capital purchases) = $44,000
- 1B includes $4,000 input tax credit
- Full credit (under car limit of $69,674 for 2024-25).

### Test 6 -- Luxury Car (Above Car Limit) [T1]

**Input:** GST-registered business purchases a luxury car for $110,000 GST-inclusive ($100,000 + $10,000 GST). 100% business use. Not fuel-efficient.
**Expected output:**
- G10 (capital purchases) = $110,000
- 1B limited to $69,674 / 11 = **$6,334** (approximately), NOT the full $10,000
- GST credit capped at car limit / 11
- LCT may also apply (reported at 1E if business is a car dealer selling the vehicle).

### Test 7 -- Second-Hand Goods from Private Seller [T1]

**Input:** GST-registered dealer purchases second-hand equipment from unregistered individual for $3,300 cash. No GST charged. Equipment for resale.
**Expected output:**
- No tax invoice (private seller)
- Notional input tax credit under Division 66: $3,300 / 11 = **$300**
- 1B includes $300
- Dealer must record seller name, address, date, description, price.

### Test 8 -- Reverse Charge (Non-Resident, Not Fully Creditable) [T1]

**Input:** GST-registered financial institution (making input taxed supplies) acquires consulting services from US firm for USD $50,000 (AUD $77,000 equivalent). No GST charged by US firm. Acquisition is 60% creditable, 40% for input taxed purpose.
**Expected output:**
- Reverse charge applies (acquisition not fully creditable)
- Self-assessed GST: $77,000 x 10% = $7,700
- 1A += $7,700 (output side of reverse charge)
- 1B += $7,700 x 60% = $4,620 (input credit limited to creditable proportion)
- Net GST cost: $7,700 - $4,620 = $3,080

### Test 9 -- GST-Free Food Sale [T1]

**Input:** GST-registered grocery store sells basic food items (bread, milk, fresh fruit) totalling $500. No GST charged.
**Expected output:**
- G1 = $500
- G3 (other GST-free sales) = $500
- G6 = $0
- 1A = $0
- Input credits on related overheads (shelving, refrigeration, staff wages related to GST-free food) are fully claimable.

### Test 10 -- Entertainment (FBT Interaction) [T1]

**Input:** GST-registered employer pays $1,100 (GST-inclusive, $100 GST) for a staff Christmas party. Entertainment is NOT exempt from FBT (employer chooses to pay FBT on it).
**Expected output:**
- Because employer pays FBT, GST credit IS claimable (s 69-5 exception)
- G11 = $1,100
- 1B includes $100 input tax credit.

### Test 11 -- Entertainment (FBT Exempt, Minor Benefit) [T1]

**Input:** GST-registered employer pays $220 (GST-inclusive, $20 GST) for a minor staff benefit (< $300 per employee). Employer claims FBT exemption under minor benefit rule.
**Expected output:**
- Because FBT exemption is claimed (not paying FBT), GST credit is BLOCKED
- G11 = $220
- 1B does NOT include the $20 (no input tax credit).
- The $20 GST is a cost to the employer.

### Test 12 -- Going Concern Sale [T1]

**Input:** GST-registered entity sells its entire business to another GST-registered entity for $500,000. Both parties agree in writing that the supply is of a going concern. Business continues to operate.
**Expected output:**
- G1 = $500,000
- G3 (other GST-free) = $500,000
- G6 = $0
- 1A = $0
- All three conditions of s 38-325 met: going concern, both registered, written agreement.

### Test 13 -- Bad Debt Adjustment [T1]

**Input:** GST-registered entity wrote off a $11,000 debt (GST-inclusive) 14 months after the invoice date. Original GST of $1,000 was remitted to ATO.
**Expected output:**
- Decreasing adjustment: $1,000 GST recovered
- G7 (adjustments) on full BAS, or adjust 1A directly on Simpler BAS
- Debt qualifies (> 12 months overdue, written off as bad)
- **Debtor** must make an increasing adjustment of $1,000 (repay the input credit previously claimed).

### Test 14 -- Mixed-Use Asset Apportionment [T2]

**Input:** GST-registered entity purchases a laptop for $2,200 GST-inclusive ($2,000 + $200 GST). Used 70% business, 30% private.
**Expected output:**
- G10 (capital purchase) = $2,200
- G15 (estimated private use) = $2,200 x 30% = $660
- G17 (creditable purchases) = G12 - G16 (including G15)
- 1B includes $200 x 70% = $140 input tax credit
- Division 129 adjustment may be required in subsequent years if use changes.

---

## Reviewer Escalation Protocol

### Tier 2 Flag Format [T2]

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Registered tax agent or BAS agent must confirm before lodging.
```

### Tier 3 Escalation Format [T3]

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to registered tax agent. Document gap.
```

---

## Contribution Notes

If you are adapting this skill for another jurisdiction, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all BAS labels with the equivalent fields on your jurisdiction's GST/VAT return form.
3. Replace the GST rate (10%) with your jurisdiction's standard and reduced rates.
4. Replace the registration threshold ($75,000) with your jurisdiction's equivalent.
5. Replace the car limit ($69,674) with your jurisdiction's equivalent vehicle deduction cap, if any.
6. Replace the GST-free and input taxed categories with your jurisdiction's equivalents.
7. Replace the penalty regime with your jurisdiction's FTL and GIC equivalents.
8. Have a registered practitioner in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
10. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a registered practitioner in the relevant jurisdiction.**

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
