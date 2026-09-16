---
name: australia-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for an Australian GST return (Business Activity Statement / BAS) for any client. Trigger on phrases like "prepare BAS", "do the GST", "fill in BAS", "create the return", "GST return", "Activity Statement", or any request involving Australian GST filing. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill covers Australia only and covers both Simpler BAS and full BAS reporting. GST groups, margin scheme, partial exemption complex, and going concern are all in the refusal catalogue. ALWAYS read this skill before touching any GST-related work.
version: 2.3
jurisdiction: AU
tax_year: 2025
last_updated: 2026-09-16
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Australia GST

## Australia GST

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Australia (Commonwealth of Australia) |
| Standard rate | 10% (single rate -- no reduced rates) |
| GST-free (zero rate equivalent) | 0% -- input tax credits retained (Division 38) |
| Input taxed (exempt equivalent) | No GST -- no input tax credits (Division 40) |
| Return form | BAS (Business Activity Statement) -- Simpler BAS or Full BAS |
| Filing portal | ATO Business Portal (https://bp.ato.gov.au) / myGov (https://my.gov.au) |
| Authority | Australian Taxation Office (ATO) |
| Currency | AUD only |
| Filing frequencies | Monthly (GST turnover >= $20M or another mandatory/elected monthly case); Quarterly (standard); Annual (voluntary, turnover < $75K) |
| Deadline | Monthly: 21st of following month; Quarterly: 28th after quarter, except December quarter due 28 February; Annual: income-tax-return due date, or 28 February if no income-tax return is required |
| Registration threshold | AUD $75,000 (general); AUD $150,000 (non-profit); taxi/ride-sourcing registration regardless of turnover |
| Primary legislation | A New Tax System (Goods and Services Tax) Act 1999 (GST Act) |
| Supporting legislation | Taxation Administration Act 1953 (Schedule 1); GST Regulations 2019; LCT Act 1999; WET Act 1999 |
| Contributor | Open Accounting Skills Registry |
| Validation date | April 2026 |
| Skill version | 2.3 |

**Read this whole section before classifying anything.**

**Key BAS labels table**

| Label | Meaning |
| --- | --- |
| G1 | Total sales (GST-inclusive basis in this worksheet; include GST-free and input-taxed sales and indicate the basis on the BAS) |
| G2 | Export sales (GST-free, Division 38-E) |
| G3 | Other GST-free sales (food, health, education -- Division 38-A to 38-D, 38-F+) |
| G4 | Input taxed sales (financial supplies, residential rent -- Division 40) |
| G5 | G2 + G3 + G4 (derived) |
| G6 | G1 minus G5 (derived -- total taxable sales, the base for output GST) |
| G7 | Adjustments on sales (bad debts, price changes -- Division 19) |
| G10 | Capital purchases (plant, equipment, vehicles -- GST-inclusive) |
| G11 | Non-capital purchases (operational expenses, stock -- GST-inclusive) |
| G12 | G10 + G11 (derived) |
| G13 | Purchases for making input taxed sales (no credit) |
| G14 | Purchases with no GST in the price (from unregistered, GST-free, wages) |
| G15 | Estimated purchases for private use (no credit) |
| G16 | G13 + G14 + G15 (derived) |
| G17 | G12 minus G16 (derived -- total creditable purchases) |
| G18 | Adjustments on purchases (Division 19, Division 129) |
| 1A | GST on sales (output GST) |
| 1B | GST on purchases (input tax credits) |

- **Simpler BAS reporting scope** — Simpler BAS (turnover < $10M, default since 1 July 2017): Report only G1, 1A, 1B. No need for G2-G18.
- **Full BAS reporting scope:** Complete the labels required by the issued BAS. G4–G9 and G12–G19 are calculation-worksheet items, not a requirement to lodge every G label. Use G1, G2, G3, G10, G11, 1A and 1B where required, plus other tax labels that apply. [ATO GST reporting](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst).
- **GST calculation formulas** — GST = GST-inclusive price x 1/11; GST = GST-exclusive price x 10%; GST-inclusive = GST-exclusive x 1.1; GST-exclusive = GST-inclusive / 1.1

**Conservative defaults -- Australian-specific**

| Ambiguity | Default |
| --- | --- |
| Unknown GST status of a sale | Taxable at 10% |
| Unknown GST status of a purchase | No input tax credit claimed |
| Unknown business-use proportion (vehicle, phone, home office) | 0% credit |
| Unknown whether food is basic or prepared | Taxable at 10% (prepared food) |
| Unknown counterparty registration status | Verify registration and supply evidence; withhold unsupported credits and keep the treatment pending |
| Unknown SaaS billing entity location | Non-resident, reverse charge applies |
| Unknown insurance type (general vs life) | Input taxed (no credit) |
| Unknown property type (commercial vs residential) | Residential (input taxed, no credit) |
| Unknown whether transaction is in scope | In scope |
| Cash withdrawal purpose | Owner drawing, exclude |

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | AUD $5,000 |
| HIGH tax-delta on a single conservative default | AUD $500 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net GST position | AUD $10,000 |

### Related guides

| Question | Guide |
| --- | --- |
| The end-to-end BAS preparation sequence, reconciliation, label mapping and corrections | `au-bas-preparation.md` |
| PAYG withholding, PAYG instalment and FBT instalment labels | `au-gst-bas.md` |
| Property supplies, the margin scheme and GST at settlement | `au-gst-property.md` |
| Due dates, penalties, interest and remission | `au-lodgment-deadlines-penalties.md` |
| Account coding, evidence and reconciliation controls | `australia-bookkeeping.md` |

### Required inputs

Minimum viable -- bank statement for the period in CSV, PDF, or pasted text. Must cover the full BAS period. Acceptable from any Australian business bank: CBA, Westpac, ANZ, NAB, Macquarie, Bendigo, Suncorp, Bank of Queensland, Up Bank, ING, Revolut AU, Wise, or any other. Recommended -- sales invoices for the period (especially for exports and GST-free supplies), tax invoices for purchases above $82.50 including GST, unless a lawful exception applies; evidence for all credit claims, the client's ABN in writing (11 digits), prior period BAS. Ideal -- complete accounting software export (Xero, MYOB, QuickBooks), tax invoice register, prior period BAS with any credit carried forward.

If source evidence is incomplete, prepare a provisional transaction list. Withhold unsupported credits from the claimable-credit total and identify them separately for review. A tax invoice is generally required before claiming a purchase above $82.50 including GST; the $500 review-priority flag is not an evidence threshold. A bank statement does not itself establish GST or creditable purpose. [GST Act ss 29-10 and 29-80](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/29-10).

### Australia-specific refusal catalogue

If any trigger fires, stop, output the refusal message verbatim, end the conversation. Refusal is a safety mechanism.

- **R-AU-1 -- Partial exemption complex** — Trigger: client makes both taxable/GST-free supplies AND input taxed supplies, and the input taxed proportion is not de minimis (financial acquisitions threshold exceeded). Message: "You make both taxable and input taxed supplies. Your input tax credits must be apportioned under Division 11 (s 11-30), which requires determining the extent of creditable purpose for each acquisition. This cannot be completed without a documented apportionment methodology confirmed by a registered tax agent. Please escalate."  _(Division 11, s 11-30)_
- **R-AU-2 -- GST groups** — Trigger: client is part of a GST group under Division 48 or asks about group registration. Message: "GST groups under Division 48 require consolidation across the group with a representative member lodging a single BAS. Intra-group supplies are disregarded. This is out of scope for this skill. Please use a registered tax agent."  _(Division 48)_
- **R-AU-3 -- Margin scheme** — Trigger: client sells property using the margin scheme under Division 75. Message: "Margin scheme transactions under Division 75 require computing GST on the margin (sale price minus acquisition cost) and confirming eligibility based on the original acquisition. This is too fact-sensitive for this skill. Please use a registered tax agent."  _(Division 75)_
- **R-AU-4 -- Going concern** — Trigger: client sells or buys a business as a going concern under s 38-325. Message: "Going concern supplies under s 38-325 require verification that all three conditions are met (going concern, both parties registered, written agreement). Incorrect classification results in either 10% GST on the full sale price or a missed GST-free entitlement. Please use a registered tax agent to confirm eligibility before proceeding."  _(s 38-325)_
- **R-AU-5 -- Financial supply complex (financial institution)** — Trigger: client is a financial institution (bank, insurer, super fund) whose primary supplies are input taxed financial supplies, or client asks about Reduced Input Tax Credits (RITC). Message: "Financial institutions making predominantly input taxed supplies require specialist apportionment, RITC calculations (75%/55%), and the financial acquisitions threshold test. This is out of scope. Please use a registered tax agent specialising in financial services GST."  _(RITC 75%/55%)_

## Section 3 -- Supplier pattern library (Australian vendors)

Use merchant patterns to identify candidate treatments. Confirm the actual supply, supplier registration, invoice GST and creditable purpose before computing a credit. Resolve conflicts in favour of source documents and law. A merchant name alone cannot establish taxability or business use.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Australian banks (fees input taxed -- exclude)

**Australian banks table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CBA, COMMONWEALTH BANK, COMMBANK, NETBANK | EXCLUDE for bank fees/charges | Financial supply, input taxed. No GST on bank fees. |
| WESTPAC, ST GEORGE, BANK OF MELBOURNE, BANKSA | EXCLUDE for bank fees/charges | Same -- all Westpac group |
| ANZ, ANZ BANK | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| NAB, NATIONAL AUSTRALIA BANK | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| MACQUARIE, MACQUARIE BANK | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| BENDIGO BANK, ADELAIDE BANK | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| SUNCORP BANK, BOQ, BANK OF QUEENSLAND | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| UP BANK, ING DIRECT, ING AUSTRALIA | EXCLUDE for bank fees/charges | Financial supply, input taxed |
| REVOLUT, WISE (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTEREST, INT PAID, INT RECEIVED | EXCLUDE | Interest income/expense, input taxed or out of scope |
| LOAN, HOME LOAN, PERSONAL LOAN, MORTGAGE | EXCLUDE | Loan principal movement, out of scope |

### 3.2 ATO and government (exclude entirely)

**ATO and government table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATO, AUSTRALIAN TAXATION OFFICE | EXCLUDE | Tax payment (GST, PAYG, income tax), not a supply |
| ATO BAS, BAS PAYMENT | EXCLUDE | GST remittance |
| ASIC, AUSTRALIAN SECURITIES | EXCLUDE | Regulatory fee -- note: ASIC annual review fee has no GST |
| COUNCIL RATES, CITY OF, SHIRE OF | EXCLUDE | Local government rates, not a supply |
| STATE REVENUE, OSR, REVENUE NSW, SRO VIC | EXCLUDE | State tax (payroll tax, stamp duty, land tax) |
| CENTRELINK, SERVICES AUSTRALIA | EXCLUDE | Government benefit, not a supply |
| DEPARTMENT OF, DEPT OF | EXCLUDE | Government fee, sovereign act |
| WORKCOVER, WORKSAFE, ICARE | Domestic 10% | Workers compensation premium -- taxable supply, GST claimable |

### 3.3 Australian utilities (taxable 10%)

**Australian utilities table**

| Pattern | Treatment | BAS Label | Notes |
| --- | --- | --- | --- |
| ORIGIN ENERGY, ORIGIN | Domestic 10% | G11 | Electricity, gas -- overhead |
| AGL, AGL ENERGY | Domestic 10% | G11 | Electricity, gas -- overhead |
| ENERGY AUSTRALIA, ENERGYAUST | Domestic 10% | G11 | Electricity, gas -- overhead |
| TELSTRA, TELSTRA CORP | Domestic 10% | G11 | Telecommunications -- overhead |
| OPTUS, SINGTEL OPTUS | Domestic 10% | G11 | Telecommunications -- overhead |
| TPG, TPG TELECOM, VODAFONE AU, IINET | Domestic 10% | G11 | Telecommunications/broadband -- overhead |
| NBN CO, NBN | Domestic 10% | G11 | National Broadband Network -- overhead |
| ALINTA ENERGY, RED ENERGY, SIMPLY ENERGY | Domestic 10% | G11 | Electricity, gas -- overhead |
| SYDNEY WATER, MELBOURNE WATER, SA WATER | GST-free, subject to actual supply | G11 | Piped water and associated metering are generally GST-free; distinguish separate installation/repair services. GST Act ss 38-285 and 38-290; GSTR 2000/25 |

### 3.4 Australian insurance (mixed treatment)

**Australian insurance table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| QBE, QBE INSURANCE | Domestic 10% | General insurance -- taxable, GST claimable |
| SUNCORP INSURANCE, GIO, AAMI | Domestic 10% | General insurance -- taxable |
| NRMA INSURANCE, NRMA | Domestic 10% | General insurance -- taxable |
| ALLIANZ AUSTRALIA | Domestic 10% | General insurance -- taxable |
| CGU, ZURICH AUSTRALIA | Domestic 10% | General insurance -- taxable |
| AMP LIFE, MLC LIFE, TAL LIFE | EXCLUDE | Life insurance -- input taxed, Division 40 |
| HEALTH INSURANCE, MEDIBANK, BUPA, HCF, NIB | GST-free; no GST credit | Private health insurance is generally GST-free under s 38-55; check actual policy and private use |
| WORKCOVER, WORKSAFE, ICARE | Domestic 10% | Workers comp premium is taxable at 10% |

### 3.5 Australian transport (taxable 10%)

**Australian transport table**

| Pattern | Treatment | BAS Label | Notes |
| --- | --- | --- | --- |
| UBER AU, UBER AUSTRALIA, UBER *AU | Domestic 10% | G11 | Rideshare -- taxable. Driver must be GST-registered regardless of turnover. |
| DIDI, DIDI AU | Domestic 10% | G11 | Rideshare -- taxable |
| 13CABS, SILVER TOP, TAXI | Domestic 10% | G11 | Taxi -- taxable (mandatory GST registration) |
| SYDNEY TRAINS, TRANSPORT NSW, OPAL | Domestic 10% | G11 | Public transport -- taxable at 10% (Australia does not zero-rate public transport) |
| METRO TRAINS MELBOURNE, MYKI, PTV | Domestic 10% | G11 | Public transport -- taxable at 10% |
| TRANSLINK, GO CARD | Domestic 10% | G11 | QLD public transport -- taxable |
| QANTAS, QANTAS AIRWAYS (domestic) | Domestic 10% | G11 | Domestic flights -- taxable at 10% |
| VIRGIN AUSTRALIA (domestic) | Domestic 10% | G11 | Domestic flights -- taxable |
| JETSTAR (domestic) | Domestic 10% | G11 | Domestic flights -- taxable |
| QANTAS (international), VIRGIN (international) | GST-free | G11 | International flights -- GST-free export (Division 38-E). Check ticket destination. |
| TOLL, LINKT, TRANSURBAN, CITYLINK, EASTLINK | Domestic 10% | G11 | Toll road charges -- taxable |

### 3.6 Australian food (basic food GST-free, prepared food 10%)

**Australian food table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| WOOLWORTHS, WOOLWORTHS METRO | TIER 2 -- split required | Supermarket: basic food items GST-free, non-food/prepared food at 10%. Default: treat as mixed, ask for receipt breakdown. If evidence is missing, leave any unsupported credit unclaimed pending review; do not invent a 50/50 split. |
| COLES, COLES EXPRESS | TIER 2 -- split required | Same as Woolworths |
| IGA, FOODWORKS, ALDI | TIER 2 -- split required | Same -- basic food GST-free, other items 10% |
| HARRIS FARM, FRUIT MARKET, GREENGROCER | GST-free | Basic food (fruit, vegetables) -- Division 38-A |
| UBER EATS, DOORDASH, MENULOG, DELIVEROO | Domestic 10% | Prepared/delivered food -- taxable. Delivery fee also taxable. |
| MCDONALD'S, KFC, HUNGRY JACK'S, SUBWAY, DOMINOS | Domestic 10% | Prepared food/restaurant meals -- always taxable |
| RESTAURANT, CAFE, BISTRO, PIZZERIA | Domestic 10% | Prepared food -- always taxable |
| BWS, DAN MURPHY'S, LIQUORLAND, FIRST CHOICE | Domestic 10% | Alcohol -- always taxable at 10% (plus excise/WET) |

### 3.7 SaaS (reverse charge from non-resident suppliers)

**SaaS table**

| Pattern | Billing entity | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Asia Pacific Pte Ltd (SG) or Google LLC (US) | Non-resident supply | If supplier registered for AU GST: 10% charged on invoice, claim credit. If not: reverse charge if not fully creditable. |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) or Microsoft Regional Sales Pte Ltd (SG) | Non-resident supply | Same logic. Check invoice for ABN and GST charge. |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | Non-resident supply | Check invoice |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | Non-resident supply | Check invoice for AU GST |
| SLACK, SALESFORCE | Slack Technologies / Salesforce (US or IE entity) | Non-resident supply | Check invoice |
| ATLASSIAN | Atlassian Pty Ltd (AU) | Domestic 10% | Atlassian is Australian -- domestic taxable supply, full credit |
| CANVA | Canva Pty Ltd (AU) | Domestic 10% | Australian entity -- domestic taxable supply |
| XERO | Xero Limited (NZ) or Xero Australia Pty Ltd | Check invoice | If AU entity: domestic 10%. If NZ entity: non-resident supply. |
| ZOOM | Zoom Video Communications (US) | Non-resident supply | Check invoice for AU GST registration |
| DROPBOX | Dropbox (IE or US) | Non-resident supply | Check invoice |
| AWS, AMAZON WEB SERVICES | Amazon Web Services Inc (US) or AWS Australia Pty Ltd | Check invoice | If AU entity: domestic 10%. If US entity: non-resident. |

- **Non-resident digital supplies note** — Since 1 July 2017, many non-resident digital suppliers (Netflix, Spotify, Google, etc.) have registered for Australian GST and charge 10% on B2C supplies. For B2B supplies where the recipient provides an ABN, the supplier may not charge GST -- reverse charge may apply on the recipient if the acquisition is not fully creditable. Always check the actual invoice.

### 3.8 Payment processors (classify the actual service)

**Payment processors table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE AU, STRIPE PAYMENTS AUSTRALIA | Check invoice and service | Merchant payment processing is not automatically input-taxed credit; claim only verified GST for creditable use |
| PAYPAL, SQUARE AU, TYRO, EFTPOS, MERCHANT FEE | Check invoice and service | Distinguish processing services, cross-border supplies and financial supplies |
| AFTERPAY, ZIP PAY, ZIP MONEY | Check contract and invoice | Classify merchant services separately from lending and other financial supplies |

[GSTR 2019/2](https://www.ato.gov.au/law/view/document?docid=GST/GSTR20192/NAT/ATO/00001) distinguishes credit supplied to a cardholder from payment services supplied to a merchant.

### 3.9 Professional services (taxable 10%)

**Professional services table**

| Pattern | Treatment | BAS Label | Notes |
| --- | --- | --- | --- |
| Accountant names, CPA, CA, CHARTERED ACCOUNTANT | Domestic 10% | G11 | Professional service -- always deductible if business purpose |
| TAX AGENT, BAS AGENT, BOOKKEEPER | Domestic 10% | G11 | Tax/BAS agent fees -- deductible |
| SOLICITOR, LAWYER, BARRISTER, LAW FIRM | Domestic 10% | G11 | Legal fees -- deductible if business purpose |
| ARCHITECT, ENGINEER, SURVEYOR | Domestic 10% | G11 | Professional service |
| MARKETING, ADVERTISING, DESIGN, AGENCY | Domestic 10% | G11 | Business service |
| CLEANER, CLEANING, OFFICE CLEANING | Domestic 10% | G11 | Business service |
| IT SUPPORT, COMPUTER, TECH SUPPORT | Domestic 10% | G11 | Business service |

### 3.10 Property (commercial vs residential)

**Property table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| COMMERCIAL RENT, OFFICE RENT, WAREHOUSE RENT | Domestic 10% | Commercial lease -- landlord must be GST-registered. GST credit claimable. |
| RETAIL LEASE, SHOP RENT, INDUSTRIAL RENT | Domestic 10% | Commercial lease -- taxable |
| RESIDENTIAL RENT, HOME RENT, APARTMENT RENT | EXCLUDE | Residential rent -- input taxed (Division 40). No GST, no credit on related costs. |
| REAL ESTATE AGENT (rental management fee) | TIER 2 | If managing commercial property: 10% taxable, credit claimable. If managing residential property: 10% taxable, but NO credit (cost relates to input taxed supply). |
| STRATA, BODY CORPORATE, OWNERS CORP | Review supply and registration | G11 | A registered body corporate’s supplies to members can be taxable. Residential accommodation being input taxed does not make the levy automatically input taxed. GSTR 2015/3 |
| AIRBNB, STAYZ, BOOKING.COM (income) | Review premises and supply | G1 or G4 as applicable | Residential premises may remain input taxed for short stays; commercial residential premises require their own test. GST Act ss 40-35 and 195-1; GSTR 2012/5 |

### 3.11 Superannuation (not a supply -- exclude)

**Superannuation table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SUPER, SUPERANNUATION, SUPER FUND | EXCLUDE | Employer SG contributions -- not a supply, out of scope for GST |
| AUSTRALIAN SUPER, REST SUPER, HOSTPLUS | EXCLUDE | Super fund contributions -- out of scope |
| SUNSUPER, CBUS, HESTA, UNISUPER | EXCLUDE | Super fund contributions -- out of scope |
| SMSF, SELF MANAGED SUPER | EXCLUDE | SMSF contributions -- out of scope |

### 3.12 Payroll (exclude entirely)

**Payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES, PAYROLL, PAY RUN | EXCLUDE | Employment relationship -- not a supply, out of scope |
| SUPER GUARANTEE, SGC, SG PAYMENT | EXCLUDE | Superannuation contribution -- out of scope |
| WORKCOVER, WORKSAFE PREMIUM, ICARE | Domestic 10% | Exception: workers comp premium IS taxable at 10%, GST credit claimable |
| PAYG WITHHOLDING, TAX WITHHELD | EXCLUDE | PAYG withholding remitted to ATO -- tax payment |
| LEAVE LOADING, ANNUAL LEAVE, LONG SERVICE | EXCLUDE | Employment entitlement -- out of scope |
| DIRECTOR FEE (outgoing) | EXCLUDE | Director fees -- generally out of scope for GST |

## Section 4 -- Worked examples

These are six fully worked classifications drawn from a hypothetical CBA NetBank bank statement of an Australian self-employed IT consultant based in Sydney. They illustrate the trickiest cases. Pattern-match against these when you encounter similar lines in any real statement.

### Example 1 -- Non-resident SaaS, reverse charge not applicable (fully creditable)

**Input line:**
`05.04.2026 ; GOOGLE ASIA PACIFIC PTE LTD ; DEBIT ; Google Workspace Business ; AUD 21.60`

**Reasoning:**
Google Asia Pacific Pte Ltd is a Singapore entity (non-resident). The client is a fully taxable IT consultant (no input taxed supplies). Under Division 84, reverse charge applies ONLY when the acquisition is NOT fully creditable. Since this client would be entitled to a full input tax credit anyway, reverse charge does NOT apply. The supply has no GST component. Treat as a purchase with no GST in the price.

**Example 1 output**

| Date | Counterparty | Gross | Net | GST | Rate | BAS Label | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | GOOGLE ASIA PACIFIC | -21.60 | 21.60 | 0 | N/A | G11 | N | -- | -- |

### Example 2 -- Local utility, standard 10%

**Input line:**
`10.04.2026 ; TELSTRA CORP LTD ; DEBIT ; Monthly plan Apr 2026 ; AUD 99.00`

**Reasoning:**
For this example, a valid tax invoice confirms $9 GST in the $99 charge and the evidence establishes wholly creditable business use. Net expense is $90 and the positive credit is $9. If use is mixed, apportion the credit. Without the required invoice, keep it pending.

**Example 2 output**

| Date | Counterparty | Gross | Net | GST | Rate | BAS Label | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | TELSTRA CORP LTD | -99.00 | 90.00 | 9.00 | 10% | G11 | N | -- | -- |

### Example 3 -- Supermarket purchase (mixed GST-free and taxable)

**Input line:**
`12.04.2026 ; WOOLWORTHS 1234 SYDNEY ; DEBIT ; Grocery purchase ; AUD 87.50`

**Reasoning:**
Woolworths sells a mix of basic food (GST-free under Division 38-A) and taxable items (prepared food, confectionery, soft drinks, household goods). Without a detailed receipt, the split is unknown. Conservative default: treat entire amount as having no GST credit (safest approach -- underclaims rather than overclaims). Flag as Tier 2 -- ask client for receipt to split GST-free and taxable items. If receipt available, split accordingly.

**Example 3 output**

| Date | Counterparty | Gross | Net | GST | Rate | BAS Label | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12.04.2026 | WOOLWORTHS 1234 | -87.50 | 87.50 pending | 0 | -- | G11 | Y | Q1 | "Supermarket: provide receipt to split GST-free food vs taxable items" |

### Example 4 -- Bank fee (input taxed financial supply)

**Input line:**
`15.04.2026 ; CBA ACCOUNT FEE ; DEBIT ; Monthly account keeping fee ; AUD 10.00`

**Reasoning:**
In this example, the statement and fee terms establish an input-taxed account-keeping service. Record the $10 business purchase at G11 with zero GST credit. Classify other bank services from their actual terms and invoice; the bank name alone does not settle GST.

**Example 4 output**

| Date | Counterparty | Gross | Net | GST | Rate | BAS Label | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | CBA ACCOUNT FEE | -10.00 | 10.00 | 0 | -- | G11 | N | -- | "Input taxed financial supply" |

### Example 5 -- Export service sale (GST-free)

**Input line:**
`20.04.2026 ; ACME CORP NZ ; CREDIT ; Invoice AU-2026-042 IT consulting April ; AUD 8,500.00`

**Reasoning:**
Incoming payment from a New Zealand company for IT consulting services. Services provided to a non-resident for consumption outside Australia are GST-free under Division 38-E (s 38-190). No GST charged. Input tax credits on costs related to making this supply are fully claimable. Confirm: (a) recipient is outside Australia; (b) service is consumed outside Australia; (c) invoice shows no GST with a note "GST-free export -- s 38-190". On Simpler BAS, include in G1 only. On Full BAS, include in G1 and G2.

**Example 5 output**

| Date | Counterparty | Gross | Net | GST | Rate | BAS Label | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20.04.2026 | ACME CORP NZ | +8,500.00 | +8,500.00 | 0 | 0% | G2 | Y | Q2 (HIGH) | "Verify NZ recipient and offshore consumption" |

### Example 6 -- Merchant transaction fee

Input: `25.04.2026 ; STRIPE PAYMENTS AU ; DEBIT ; Transaction fees April ; AUD 145.20`.

The name does not settle the GST treatment. In this example a valid Australian tax invoice establishes a taxable processing service with $13.20 GST, wholly for creditable business use. The cash debit is $145.20, net expense $132.00 and positive GST credit $13.20. If that evidence is absent, show a pending treatment and no verified credit until resolved. A supply of credit or a different cross-border arrangement may have a different result. [GSTR 2019/2](https://www.ato.gov.au/law/view/document?docid=GST/GSTR20192/NAT/ATO/00001).

| Date | Counterparty | Bank amount | Net expense | GST credit | Label | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 25.04.2026 | STRIPE PAYMENTS AU | -145.20 | 132.00 | 13.20 | G11 | Valid tax invoice and wholly creditable use |

## Section 5 -- Tier 1 classification rules

Each rule states the legal source and the BAS label mapping. Apply silently if the data is unambiguous.

### 5.1 Taxable supplies (10%)

- **Taxable supply conditions and mapping** — Legislation: GST Act, s 9-5 (meaning of taxable supply), s 9-70 (rate). Default rate for any supply connected with Australia by a GST-registered entity in the course of an enterprise, unless the supply is GST-free (Division 38) or input taxed (Division 40). Australia has a single 10% rate -- no reduced rates, no multiple rate tiers. A supply is taxable if ALL conditions are met (s 9-5): 1. Made for consideration; 2. In the course or furtherance of an enterprise; 3. Connected with the indirect tax zone (Australia); 4. Supplier is registered or required to be registered; AND 5. NOT GST-free and NOT input taxed. Sales: G1 (and G6 derived). Purchases: G10 (capital) or G11 (non-capital). GST on sales: 1A. GST credits on purchases: 1B. Common taxable supplies: professional services (legal, accounting, consulting), commercial rent, construction, telecommunications, general insurance premiums, software licences, motor vehicle sales, restaurant/cafe meals, domestic transport, office supplies, equipment purchases.  _(GST Act, s 9-5, s 9-70)_

### 5.2 GST-free supplies (0%, credits retained)

- **GST-free supplies overview** — GST-free supplies attract 0% GST but the supplier retains full input tax credit entitlements on related costs. This mirrors the EU concept of zero-rated supplies. Sales: G1 and G2 (exports) or G3 (other GST-free). On Simpler BAS, include in G1 only.  _(GST Act, Division 38)_

**Critical categories table**  _(GST Act, Division 38)_

| Category | Subdivision | Key items |
| --- | --- | --- |
| Basic food | 38-A | Bread, milk, meat, fruit, vegetables, flour, rice, eggs, butter, plain water, tea, coffee (unbrewed). EXCLUDES prepared/restaurant food, confectionery, soft drinks, snack foods, alcohol, ice cream. |
| Health services | 38-B | GP, specialist, hospital, dental, physiotherapy, chiropractic, ambulance. Must be Medicare-eligible or registered health practitioner. EXCLUDES cosmetic/elective surgery, veterinary. |
| Education | 38-C | School fees (primary/secondary), university tuition, TAFE/RTO vocational training. EXCLUDES commercial training, private tutoring. |
| Childcare | 38-D | Approved long day care, family day care, before/after school care. |
| Exports of goods | 38-E | Goods physically exported within 60 days of supply. |
| Exports of services | 38-E | Services to non-resident consumed outside Australia. |
| Religious services | 38-F | By religious institution as part of religious practice. |
| Water and sewerage | 38-G | Supply of water by government/utility (basic supply). |
| Going concern | 38-J | Sale of business as going concern (both registered, written agreement) -- but R-AU-4 fires. |

**GST-free food rules (Subdivision 38-A) table**  _(Subdivision 38-A)_

| Food item | Treatment | Reasoning |
| --- | --- | --- |
| Fresh fruit and vegetables | GST-free | Basic food |
| Fresh meat, poultry, fish | GST-free | Basic food |
| Bread, rolls | GST-free | Basic food |
| Milk, cream, cheese | GST-free | Basic food |
| Rice, pasta, flour | GST-free | Basic food |
| Eggs | GST-free | Basic food |
| Cooking oil, margarine, butter | GST-free | Basic food |
| Baby food, infant formula | GST-free | Basic food |
| Bottled water (plain) | GST-free | Basic food |
| Tea, coffee (unbrewed) | GST-free | Basic food |
| Ordinary plain biscuits (not chocolate) | Taxable 10% | GST Act Schedule 1 item 32; specified breakfast-cereal biscuits and infant/invalid rusks have exceptions |
| Raw, unprocessed nuts | GST-free | Basic food |
| Confectionery (chocolate, lollies) | Taxable 10% | Schedule 1 exclusion |
| Soft drinks, energy drinks | Taxable 10% | Schedule 1 exclusion |
| Ice cream | Taxable 10% | Schedule 1 exclusion |
| Snack foods (chips, pretzels) | Taxable 10% | Schedule 1 exclusion |
| Prepared meals (takeaway, restaurant) | Taxable 10% | Food supplied ready for consumption |
| Hot food (pies, sausage rolls heated) | Taxable 10% | Heated for consumption |
| Alcohol | Taxable 10% + excise/WET | Never GST-free |
| Chocolate-coated biscuits | Taxable 10% | Confectionery |
| Muesli bars | Taxable 10% | Snack food |
| Honey-roasted/flavoured nuts | Taxable 10% | Snack food |

### 5.3 Input taxed supplies (no GST, no credits)

- **Input taxed supplies overview** — Input taxed supplies have NO GST charged and the supplier gets NO input tax credits on related costs. This mirrors the EU concept of exempt-without-credit supplies. Sales: G4 (input taxed sales). Purchases related to input taxed supplies: G13 (no credit). Critical distinction: GST-free and input taxed are NOT the same. GST-free suppliers retain input tax credit entitlements; input taxed suppliers do not. Confusing them produces opposite outcomes.  _(GST Act, Division 40)_

**Critical categories table**  _(GST Act, Division 40)_

| Category | Section | Key items |
| --- | --- | --- |
| Financial supplies | 40-5 | Interest, loan fees, currency exchange margins, credit card fees (issuer), share dealings, guarantee fees, life insurance, super fund management |
| Residential rent | 40-35 | Rental of existing residential premises. Commercial rent is taxable. |
| Sale of existing residential premises | 40-65 | Previously sold as residential, not new/substantially renovated |
| Life insurance | 40-5 | General insurance is taxable |

**Residential vs commercial boundary table**

| Supply | Treatment |
| --- | --- |
| Residential rent (existing premises) | Input taxed |
| Sale of existing residential premises | Input taxed |
| Sale of NEW residential premises | Taxable 10% (first sale after construction/substantial renovation) |
| Commercial rent (office, retail, warehouse) | Taxable 10% |
| Short-stay accommodation | Classify the premises and supply | Hotels may be commercial residential premises; an ordinary residential Airbnb stay does not become taxable because it lasts under three months |

### 5.4 Out-of-scope transactions (not on BAS)

**Out-of-scope transactions table**

| Transaction | Reason |
| --- | --- |
| Wages, salaries, superannuation | Not a supply -- employment relationship |
| Dividends | Not a supply -- return on equity |
| Loan principal repayments | Not a supply -- repayment of capital |
| GST/income tax payments to ATO | Tax payment, not a supply |
| Private transactions by individuals | Not in course of enterprise |
| Owner drawings/transfers | Internal, not a supply |
| Gifts/donations (no consideration) | No consideration = not a supply |

### 5.5 Reverse charge (Division 84)

- **Australian reverse charge distinction from EU** — Key Australian distinction from EU: In Australia, reverse charge on offshore supplies to registered recipients applies ONLY when the acquisition is NOT fully creditable. If the recipient would claim 100% input tax credit anyway, no reverse charge -- no revenue leakage. When reverse charge applies: - Output GST (self-assessed): include in 1A - Input tax credit (if any): include in 1B - NOT reported in G1 (total sales) - Both sides appear on BAS  _(Division 84)_
- **Netflix tax** — "Netflix tax" (Division 83-5, since 1 July 2017): Non-resident digital suppliers must register for GST if Australian turnover exceeds $75,000 and charge 10% on B2C supplies. For B2B where recipient provides ABN, supplier does NOT charge GST.  _(Division 83-5)_

### 5.6 Input tax credit entitlement (Division 11)

- **Entitlement conditions:** Establish the s 11-5 creditable acquisition conditions, including taxable supply, consideration, registration and creditable purpose. Apply the attribution rules: generally hold a valid tax invoice before claiming, subject to the $82.50 including-GST exception and other lawful exceptions/discretion. The four-year claim limit is not permission to claim before obtaining required evidence. [GST Act ss 11-5, 29-10, 29-80 and 93-5](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/29-10).
- **Blocked credits** — No credit for acquisitions relating to input taxed supplies (s 11-15), private/domestic use (s 11-15), entertainment where FBT exempt (s 69-5), non-deductible fines/penalties (s 69-5).  _(s 11-15, s 69-5)_
- **Car limit** — Input tax credit for a car is capped at car limit / 11. For 2024-25 and 2025-26: $69,674 / 11 = ~$6,334 maximum credit; for 2026-27: $69,883 / 11 = ~$6,353. No outright block on cars (unlike Malta).  _(s 69-10)_

### 5.7 Tax invoices (Division 29)

**Tax invoice requirements table**  _(Division 29)_

| Requirement | Supplies < $1,000 | Supplies >= $1,000 |
| --- | --- | --- |
| Marked "Tax Invoice" | Yes | Yes |
| Supplier identity (name, ABN) | Yes | Yes |
| Date of issue | Yes | Yes |
| Brief description | Yes | Yes |
| GST amount (or "price includes GST") | Yes | Yes |
| Recipient identity (name, ABN) | No | Yes |

- **No ABN withholding:** Where required, withhold 47% and report at W4, subject to the entity’s withholding reporting class. Apply exceptions, including payments of $75 or less excluding GST and valid supplier statements where relevant. [ATO PAYG withholding](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding).

### 5.8 Adjustments (Divisions 19, 21 and 129)

An adjustment is not an error. It arises because something changed after the original supply or
acquisition was correctly reported. Errors are dealt with under the correction rules; see
`au-bas-preparation.md` Section 7 for the credit error and debit error time and value limits and
for when a revision is required instead.

**The two directions**

| Direction | Effect | Where it goes |
| --- | --- | --- |
| Increasing adjustment | Increases net GST, either more GST on sales or less credit on purchases | 1A if it relates to a supply, 1B if it reduces a credit |
| Decreasing adjustment | Decreases net GST, either less GST on sales or more credit on purchases | 1A if it relates to a supply, 1B if it increases a credit |

**Common adjustment events**

| Event | Division | Treatment |
| --- | --- | --- |
| Price increase or decrease after the supply | Div 19 | Adjustment in the period the adjustment event is accounted for |
| Supply cancelled, or goods returned | Div 19 | As above |
| Bad debt written off by the supplier, or a debt overdue 12 months | Div 21 | Decreasing adjustment for the supplier, increasing adjustment for the recipient who claimed the credit |
| Bad debt later recovered | Div 21 | Reverses the earlier adjustment to the extent recovered |
| Change in the extent of creditable purpose | Div 129 | Compared over prescribed adjustment periods, with thresholds that can remove the need to adjust |
| Goods applied solely to private or domestic use | Div 130 | Increasing adjustment |
| Cancellation of registration, with assets on hand | Div 138 | Increasing adjustment |
| Becoming registered, with assets on hand acquired earlier | Div 129 | Can give rise to a decreasing adjustment |

**Adjustment notes.** A decreasing adjustment arising from an adjustment event on a supply
generally cannot be claimed until an adjustment note is held, subject to the minor adjustment
exemption and the Commissioner's determinations. The supplier issues the adjustment note.
[GST Act ss 29-20, 29-75](https://www.ato.gov.au/law/view/document?docid=PAC/19990055/29-75)

**Attribution.** An adjustment is attributed to the tax period in which the entity becomes aware
of the adjustment event, not to the period of the original supply. Reopening the original period
is the wrong treatment.

**Bad debts, the two-sided rule.** A supplier accounting on a non-cash basis who writes off a
debt as bad, or holds a debt overdue 12 months or more, gets a decreasing adjustment. The
recipient who claimed the credit and has not paid has a matching increasing adjustment. Both sides
must be considered; a client who has not paid a supplier for over 12 months may owe GST back.

**Division 129 in practice.** The most common trigger is a property or asset whose actual use
turns out to differ from the planned use, for example a development intended for sale that is
rented out instead. Division 129 compares planned and actual use over set adjustment periods, and
the number of adjustment periods depends on the value of the acquisition. This is fact-sensitive;
escalate rather than estimate.

**What is not an adjustment**

- A mistake in the original reporting. That is an error.
- A delay in attributing a credit, where the entity simply claims it in a later period under the
  attribution rules.
- A change in the GST rate or law. There is none to date; the rate has been 10% since 1 July 2000.

## Section 6 -- Tier 2 catalogue

For each ambiguity type: pattern, why the bank statement is insufficient, conservative default, question for the client.

### 6.1 Vehicle costs (fuel -- business or private?)

Pattern: BP, Shell, Caltex, Ampol, 7-Eleven fuel, Viva Energy. Why insufficient: business-use proportion unknown. Unlike Malta, Australia does NOT hard-block car GST credits -- but private-use portion must be excluded. Default: 0% credit. Question: "Is this fuel for a business vehicle? What percentage is business use vs private? Do you keep a logbook?"

### 6.2 Home office (utilities -- 70c/hr or actual?)

Pattern: Origin Energy, AGL, Telstra on a residential address; home internet. Why insufficient: if the client works from home, a portion of home expenses may be claimable. The ATO allows either the fixed-rate method (70 cents per hour from 2024-25 under PCG 2023/1; 67c applied for 2022-23 and 2023-24) or the actual-cost method with apportionment. For GST, the actual-cost method requires splitting the taxable portion. Default: 0% credit (cannot determine business proportion). Question: "Do you work from home? How many hours per week? Is this a dedicated business line/service or shared personal?"

### 6.3 Food purchases (Woolworths -- basic food GST-free or prepared?)

Pattern: Woolworths, Coles, IGA, Aldi, any supermarket. Why insufficient: a single supermarket receipt may contain GST-free basic food and taxable prepared food, confectionery, soft drinks, and non-food items. The receipt total alone cannot determine the split. Default: no credit claimed (pending evidence; G11 purchase with no verified credit). Question: "Could you provide the receipt? I need to split GST-free food items from taxable items to claim the correct credit."

### 6.4 Cash withdrawals

Pattern: ATM, cash withdrawal, CBA cash, Westpac cash. Why insufficient: unknown what cash was spent on. Default: exclude as owner drawing. Question: "What was the cash used for? If business expenses, do you have receipts?"

### 6.5 Insurance (some taxable, some input taxed -- which policy?)

Pattern: insurance premium or policy payment. Identify the policy and the invoice components. General insurance can contain GST, stamp duty and other amounts; use the actual GST component. Life insurance is generally input taxed; private health insurance is generally GST-free. Pending identification, show no verified credit. GST Act ss 38-55 and 40-5.

### 6.6 Mixed personal/business subscriptions

Pattern: Netflix, Spotify, Apple, Amazon Prime, gym membership. Why insufficient: if subscription is partly personal and partly business, only the business portion is creditable. Most streaming/entertainment subscriptions are purely personal. Default: exclude as private. Question: "Is this a business expense or personal? If mixed, what percentage is business use?"

### 6.7 Airbnb income (short-stay accommodation -- residential or commercial?)

Pattern: Airbnb or Stayz income. Determine whether the supply is residential premises or commercial residential accommodation from the premises and arrangement, not the booking channel or a three-month threshold. Check registration, taxable turnover and any platform fee separately. An ordinary residential letting is generally input taxed. GST Act ss 40-35 and 195-1; GSTR 2012/5.

### Sheet "Transactions"

Columns:
- A–D: Date, counterparty, bank direction and description.
- E: Signed bank amount in AUD, retained unchanged for bank reconciliation.
- F: Net amount for accounting, based on the invoice and verified GST component.
- G: GST liability for a sale or verified GST credit for a purchase. Use positive amounts for ordinary transactions and negative amounts for supported reversals. For a wholly taxable GST-inclusive amount, G = M * ABS(E)/11, multiplied by the creditable-use proportion for a purchase. For mixed or specially valued supplies, use the invoice’s actual GST component with the reporting sign and creditable proportion instead. GST-free/input-taxed supplies and unsupported credits contribute zero. Record any pending credit in notes.
- H: One primary category: G1 for taxable sales, G2 for export sales, G3 for other GST-free sales, G4 for input-taxed sales, G10 for capital purchases, G11 for non-capital purchases, or EXCLUDED. Split genuinely mixed transactions into supported components without duplicating the bank amount.
- I–L: Provisional flag, question, exclusion reason and notes/evidence.
- M: Reporting sign, 1 for ordinary sales/purchases and -1 for a supported refund or reversal. Infer this from the transaction, not bank direction alone.
- N: GST-inclusive reporting amount = ABS(E) * M. This is positive for ordinary purchases despite the negative bank debit.

For H, use the primary categories above. Earlier G13/G14/G15 references describe calculation-worksheet exclusions and must not replace a G10/G11 purchase category. Keep the exclusion and creditability evidence in I–L. Retain the signed bank amount separately from positive reporting amounts.

### Sheet "BAS Summary" (Full BAS)

Use GST-inclusive reporting amounts consistently. Populate named cells with:

| Label | Formula / rule |
| --- | --- |
| G1 | Sum N for H equal to G1, G2, G3 or G4; exclude loans, transfers and other EXCLUDED credits |
| G2, G3 | Sum N for the corresponding H category |
| G10, G11 | Sum N for the corresponding purchase category, including purchases without credits where required by the BAS instructions |
| 1A | Sum G for sales categories, plus supported GST adjustments |
| 1B | Sum G for G10 and G11, plus supported credit adjustments |
| Net GST | 1A - 1B |

For example, G10 = SUMIFS(Transactions!N:N,Transactions!H:H,"G10"). G1 combines four such SUMIFS for its sales categories. 1B sums the verified credits in G for G10 and G11. Do not subtract non-creditable purchases again from a total of credits. G4–G9 and G12–G19 may support a separate calculation worksheet but are not all lodged BAS labels.

### Sheet "Simpler BAS"

For eligible businesses with GST turnover below $10 million, report G1, 1A and 1B using the same definitions and formulas; complete any other tax obligations on the issued statement. Confirm the G1 GST-inclusive indicator.

### Worksheet checks

- A taxable sale of $1,100 gives G1 $1,100 and 1A $100.
- A wholly creditable taxable purchase of $110 gives 1B $10 even though the bank amount is -$110. Together with the sale, net GST is $90.
- A $110 purchase with 50% creditable use gives a $5 credit if all other requirements are met. Do not exclude its private portion twice.
- A $1,000 loan deposit contributes zero to G1 and 1A. A supported $110 sales refund reduces reported sales by $110 and output GST by $10.
- GST-free purchases contribute no GST credit; unsupported acquisitions remain pending until entitlement and evidence are established.

[ATO GST reporting](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/goods-and-services-tax-gst); GST Act ss 9-70, 11-20 and 29-10.

### Color and formatting conventions

Blue font for hardcoded values from the bank statement (column E of Transactions). Black for formulas. Green for cross-sheet references. Yellow background for any row where Default? = "Y".

## Section 8 -- Australian bank statement reading guide

**CSV format conventions.** CBA NetBank exports use comma delimiters with DD/MM/YYYY dates. Columns typically: Date, Amount, Description, Balance. Westpac exports similar. ANZ uses Date, Transaction Details, Debit, Credit, Balance. NAB similar. Revolut and Wise use ISO dates. Always confirm column mapping before processing.

**CBA NetBank specific.** Description field often contains: merchant name, card number suffix, location. Direct debits show "DIRECT DEBIT" prefix. Transfers show "TRANSFER TO" or "TRANSFER FROM". Pay Anyone shows recipient name. BPAY shows biller name and reference.

**Internal transfers and exclusions.** Own-account transfers between the client's CBA, Westpac, etc. accounts. Labelled "TRANSFER TO [account name]", "INTERNAL TRANSFER", "OWN ACCOUNT". Always exclude.

**Owner drawings.** A sole trader cannot pay themselves wages. Any transfer to their personal account is a drawing. Exclude from BAS. An individual transferring from business to personal: exclude.

**Refunds and reversals.** Identify by "REFUND", "REVERSAL", "CHARGEBACK", "CREDIT ADJUSTMENT". Book as a negative in the same BAS label as the original transaction. Correction is in the period the refund is booked.

**Foreign currency transactions.** Convert to AUD at the transaction date rate. Use the RBA indicative exchange rate or the rate shown on the bank statement. Note the rate used in the Transactions sheet column L.

**BSB and account numbers.** BSB (6 digits, XX-XXXX format) identifies the bank and branch. Not directly relevant to GST classification but helps identify counterparty bank.

**ABN on statements.** Some business bank statements show the client's ABN. Verify it matches the ABN on the GST registration.

**Cryptic descriptions.** Card purchases with merchant terminal codes; BPAY payments with only biller codes. If the counterparty cannot be identified from the description, ask the client. Do not classify unidentified transactions.

**PAYG and FBT lines.** BAS payments to ATO may include PAYG withholding (W2), PAYG instalments (T7), and FBT instalments (F1). These are tax payments, not supplies. Exclude from GST classification but note for BAS completion (labels W1-W5, T1-T9, F1-F3).

## Section 9 -- Onboarding fallback (only when inference fails)

Infer the client profile from the data first. Only ask questions the data could not answer.

### 9.1 Entity type and trading name

Inference rule: sole trader names match account holder; company names end in "Pty Ltd", "Ltd". Fallback question: "Are you a sole trader, partnership, company (Pty Ltd), or trust?"

### 9.2 GST registration status

Verify GST registration and its effective date on the ABR, supported by the ATO account. A request for a BAS does not establish registration. Check PAYG activity statements separately.

### 9.3 ABN

Inference rule: may appear on bank statement header or invoices. Search descriptions. Fallback question: "What is your ABN? (11 digits)"

### 9.4 Reporting period and method

Inference rule: statement date range indicates quarter. Fallback question: "Which BAS period? Q1 (Jul-Sep), Q2 (Oct-Dec), Q3 (Jan-Mar), or Q4 (Apr-Jun)? Monthly or quarterly?"

### 9.5 Simpler BAS or Full BAS

Inference rule: if turnover < $10M (likely for sole traders), Simpler BAS is default. Fallback question: "Are you on Simpler BAS (G1, 1A, 1B only) or do you report full BAS labels?"

### 9.6 Accounting basis

Inference rule: not inferable from bank statement alone. Fallback question: "Are you on cash basis or accrual basis for GST?"

### 9.7 Industry and sector

Inference rule: counterparty mix, sales descriptions. IT, consulting, trades, retail, hospitality are recognisable from transaction patterns. Fallback question: "In one sentence, what does the business do?"

### 9.8 Input taxed supplies

Inference rule: presence of residential rental income, interest income from lending, financial service revenue. Fallback question: "Do you earn any income from residential property, financial services, or share trading?" If yes and non-de-minimis: R-AU-1 or R-AU-5 may fire.

### 9.9 Employees

Inference rule: PAYG withholding payments, super guarantee payments, WorkCover. Fallback question: "Do you have employees? If so, how many?"

### 9.10 Exports

Inference rule: foreign currency credits, overseas counterparty names. Fallback question: "Do you sell goods or services to customers outside Australia?"

### Filing deadlines (quarterly)

**Filing deadlines table**

| Quarter | Period | Due date |
| --- | --- | --- |
| Q1 | 1 July -- 30 September | 28 October |
| Q2 | 1 October -- 31 December | 28 February |
| Q3 | 1 January -- 31 March | 28 April |
| Q4 | 1 April -- 30 June | 28 July |

- **Other deadline notes:** Monthly GST is generally due on the 21st of the next month. Annual GST is generally due with the income-tax return, or 28 February after the year where no return is required. Check the actual statement, extensions and next-business-day rule. [ATO annual GST](https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/lodging-your-bas-or-annual-gst-return).

### Penalties

- **Failure to lodge (FTL):** The base penalty is one unit per 28-day period or part, capped at five units. Apply the relevant entity multipliers, dates and remission rules. The penalty unit is $364 from 1 July 2026. [Crimes (Amount of a Penalty Unit) Instrument 2026](https://www.legislation.gov.au/F2026N00424/asmade/text).
- **General Interest Charge (GIC):** Use the published quarterly ATO rate and applicable daily compounding. GIC and SIC incurred on or after 1 July 2025 are not deductible; preserve the earlier rule only for earlier-incurred interest. [ATO interest](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/deductions-you-can-claim/cost-of-managing-tax-affairs/interest-charged-by-the-ato).
- **Shortfall penalties:** Base rates can be 25%, 50% or 75% according to the conduct. A qualifying pre-notification voluntary disclosure generally reduces the penalty by 80% where the shortfall is at least $1,000 and 100% below that amount. The qualifying post-notification reduction is 20%. Apply the statutory conditions and any other adjustments. [TAA Schedule 1 s 284-225](https://www.ato.gov.au/law/view/document?docid=PAC/19530001/SCH1-284-225).

### Registration thresholds

**Registration thresholds table**  _(GST Act, s 23-5; s 144-5; Division 83-5)_

| Entity type | Threshold | Legislation |
| --- | --- | --- |
| General business | $75,000/year | GST Act, s 23-5 |
| Non-profit | $150,000/year | GST Act, s 23-5 |
| Taxi/rideshare | Registration regardless of turnover | GST Act, s 144-5 |
| Non-resident digital supplier (B2C) | $75,000 Australian turnover | Division 83-5 |

- **GST turnover composition** — GST turnover includes taxable + GST-free supplies. Excludes input taxed, not connected with Australia, capital asset sales (unless regularly dealing).

### Cash vs accrual basis

**Cash vs accrual basis table**

| Feature | Cash | Accrual |
| --- | --- | --- |
| GST on sales reported | To the extent payment is received | Generally the earlier of any consideration or an invoice, subject to special rules |
| Input credits claimed | To the extent payment is made, with required evidence | Generally the earlier of any consideration or an invoice, with required evidence and applicable attribution rules |
| Who can use | Turnover < $2M (or $10M SBE) | Anyone |

### Key thresholds summary

**Key thresholds summary table**  _(s 23-5; TAA 1953; s 29-40; s 69-10; LCT Act; TAA Schedule 1; s 31-5; s 29-70)_

| Threshold | Value | Source |
| --- | --- | --- |
| GST registration | $75,000 | s 23-5 |
| Simpler BAS eligibility | Turnover < $10M | TAA 1953 |
| Cash basis eligibility | Turnover < $2M (or $10M SBE) | s 29-40 |
| Car limit (2024-25) | $69,674 | s 69-10 |
| LCT threshold (2025-26, general / other vehicles) | $80,567 | LCT Act / ATO car thresholds |
| LCT threshold (2024-25, fuel-efficient) | $91,387 | LCT Act |
| No ABN withholding exemption | Payments of $75 or less excluding GST, subject to applicable rules | TAA Schedule 1 |
| Monthly reporting | GST turnover >= $20M or another mandatory/elected monthly case | GST Act Division 27 |
| Tax invoice -- simplified | Supplies < $1,000 | s 29-70 |

### Comparison with EU VAT (for practitioners familiar with EU systems)

**Comparison table**

| Feature | Australian GST | EU VAT |
| --- | --- | --- |
| Number of rates | 1 (10%) | 2-4 per member state |
| Reverse charge trigger (B2B cross-border) | ONLY if not fully creditable | ALWAYS (Art. 196) |
| Intra-community regime | N/A | Zero-rated supply + acquisition |
| Entertainment credit | Follows FBT (credit if FBT paid) | Typically blocked outright |
| Motor vehicle credit | Allowed, capped at car limit | Often blocked (e.g. Malta 10th Schedule) |
| Financial supply credits | RITC at 75%/55% for certain services | No equivalent |

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the Malta v2.0 structure. It supersedes v1.1 (April 2026, standalone monolithic skill). The Australian-specific content (BAS label mappings, rates, thresholds, GST-free food rules, input taxed categories) has been verified against the GST Act 1999, ATO guidance, and GST Regulations 2019.

### Sources

**Primary legislation:**
1. A New Tax System (Goods and Services Tax) Act 1999 -- https://www.legislation.gov.au
2. Taxation Administration Act 1953, Schedule 1
3. GST Regulations 2019
4. A New Tax System (Luxury Car Tax) Act 1999
5. A New Tax System (Wine Equalisation Tax) Act 1999

**ATO guidance:**
6. ATO BAS instructions -- https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/lodging-your-bas
7. ATO GST registration -- https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/registering-for-gst
8. ATO Simpler BAS -- https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/lodging-your-bas/simpler-bas
9. ATO food and GST -- https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/in-detail/rules-for-specific-transactions/gst-and-food

### Known gaps

1. The supplier pattern library in Section 3 covers the most common Australian counterparties but does not cover every local SME or regional brand. Add patterns as they emerge.
2. The worked examples are drawn from a hypothetical IT consultant in Sydney. They do not cover hospitality, retail, construction, or agriculture specifically.
3. The GST-free food table covers the most common items but Schedule 1 of the GST Act is detailed -- edge cases (e.g. specific bakery items, health food products) should be flagged [T2].
4. Car limit and LCT thresholds are 2024-25 values. Verify annually as they are indexed.
5. The reverse charge section is simplified for the common case (fully creditable recipient where reverse charge does NOT apply). Partially creditable recipients require more detailed treatment.
6. Wine Equalisation Tax and Luxury Car Tax are noted but not fully worked -- these are specialist areas.
7. Red flag thresholds (AUD $5,000 single transaction, $500 tax-delta, $10,000 absolute position) are conservative starting values for a typical Australian self-employed client -- not empirically calibrated.

### Change log

- **v2.0 (April 2026):** Full rewrite to align with Malta v2.0 structure. Ten sections: quick reference (1), inputs and refusals (2), supplier pattern library with 12 sub-tables (3), six worked examples from CBA NetBank format (4), Tier 1 rules compressed (5), Tier 2 catalogue with 7 items (6), Excel template (7), bank statement reading guide (8), onboarding fallback with inference rules (9), reference material (10). Five Australia-specific refusals (R-AU-1 through R-AU-5).
- **v1.1 (April 2026):** Monolithic skill with classification rules, BAS labels, reverse charge, thresholds, edge cases, and test suite. Comprehensive but not aligned with v2.0 architecture.

### Self-check (v2.3)

1. Quick reference at top with BAS label table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 12 sub-tables).
3. Worked examples from bank statement format: yes (Section 4, 6 examples from CBA NetBank).
4. Tier 1 rules compressed: yes (Section 5, 7 rules).
5. Tier 2 catalogue compressed with questions: yes (Section 6, 7 items).
6. Excel template specification: yes (Section 7).
7. Onboarding as fallback only, inference rules first: yes (Section 9, 10 items).
8. All 5 Australia-specific refusals present: yes (Section 2, R-AU-1 through R-AU-5).
9. Reference material at bottom: yes (Section 10).
10. GST-free food detail table explicit: yes (Section 5.2, 22-item food table).
11. Input taxed vs GST-free distinction explicit: yes (Section 5.2 and 5.3).
12. Reverse charge Australian exception (fully creditable = no reverse charge) explicit: yes (Section 5.5 + Example 1).
13. Bank fees as financial supply (input taxed, exclude) explicit: yes (Section 3.1 + Example 4).
14. Payment processor fees as financial supply explicit: yes (Section 3.8 + Example 6).
15. Supermarket split (GST-free food vs taxable items) explicit: yes (Section 3.6 + Example 3).

## End of Australia GST Return Preparation Skill v2.3

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

> Contributed by Ryan Duguid.

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
