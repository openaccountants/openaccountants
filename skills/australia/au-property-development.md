---
name: au-property-development
description: >
  Use this guide to prepare the income tax evidence on whether profit from an Australian land
  subdivision, development or sale is capital or revenue: mere realisation of a capital asset,
  an isolated profit-making undertaking (TR 92/3), or a business of property development in
  which land is trading stock (TD 92/124, s 70-10 ITAA 1997), including changes of intention
  and lot-level workpapers. Covers individuals, trusts, partnerships and companies for 2026-27.
  Trigger on 'revenue or capital', 'isolated transaction', 'profit-making scheme', 'subdivision
  profit', 'property developer income', 'land as trading stock', 'mere realisation' or
  'change of intention'.
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "2026-27"
tier: 2
last_updated: 2026-11-11
version: 0.1
review_status: pending_review
verified_by: pending
license: FSL-1.1-ALv2
depends_on:
  - workflow-base
---

# Australia Property Development Income: Revenue or Capital v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide loads on `workflow-base` and fills its Section 7 slots for the income tax characterisation of profit from subdividing, developing and selling Australian land. It prepares the evidence and the conditional workpapers for 3 characterisations and leaves the choice to the registered tax agent:

- **(a) Mere realisation of a capital asset.** Profit on the mere realisation of an investment is not income even if the realisation is carried out in an enterprising way (TR 92/3 para 36); the gain falls under CGT.
- **(b) Isolated profit-making undertaking.** A profit from an isolated transaction is generally income where the purpose in entering it was to make a profit and it was entered into, and the profit made, in carrying on a business or carrying out a business operation or commercial transaction (TR 92/3 para 6). It is ordinary income under s 6-5. Section 15-15 does not apply to the sale of property acquired on or after 20 September 1985 (s 15-15(2)(b)).
- **(c) A business of property development.** Land is trading stock if it is held for resale and a business activity dealing in land has commenced (TD 92/124 para 1; s 70-10).

**Not covered here; route to the guide that holds it:**

| Topic | Guide |
|---|---|
| GST: enterprise and registration, taxable supplies of new residential premises and potential residential land, margin scheme, GST at settlement withholding (MT 2006/1 factors) | `au-gst-property` |
| CGT computation: cost base, apportionment across lots, discount, main residence exemption and the changes from 1 July 2027 | `au-capital-gains` |
| Small business CGT concessions | `au-small-business-cgt` |
| Transfer duty | `au-stamp-duty` |
| Land tax | `au-land-tax` |
| Rental property deductions, including a rental property later subdivided | `au-rental-property` |
| Foreign resident sellers and foreign resident capital gains withholding | `au-nonresident-cgt` |
| Company tax rate and losses | `au-company-tax` |
| Whether a primary production business is carried on (TR 97/11 matrix) | `au-primary-production` |

**Period coverage.** Law and ATO guidance as read on 2 November 2026, for sales in the 2026-27 income year. TR 92/3 states it applies to years of income before and after its issue (para 21). The ATO's decision impact statement on *Commissioner of Taxation v Morton* [2026] FCAFC 31 (judgment 27 March 2026) says the decision applied existing case law, does not change the legal principles and turned on its own facts (paras 26-28); TR 92/3 remains the ATO framework.

## Ask the client first

1. The selling entity, its owners, its other activities and any history of property dealings, by it or entities it controls.
2. Acquisition documents: contract, date, price, valuations, loan applications and any stated purpose.
3. How the land has been used since acquisition (home, farm, rental, vacant, business premises).
4. Minutes, resolutions and correspondence recording decisions about the land.
5. Council applications and approvals, with dates; any rezoning and who sought it.
6. Development, project management or joint venture agreements, including any profit or proceeds share.
7. Feasibility studies, budgets, finance documents and the security given.
8. Development costs by phase and by lot; agency and marketing agreements.
9. The sale contract for each lot, and the intended use of each retained lot.
10. ABN and GST registration status (for routing to `au-gst-property`).

## The method, step by step

### Key authorities and tests (read 2 November 2026)

| Item | Rule | Source |
|---|---|---|
| Two elements for an isolated transaction | Purpose of profit-making in entering the transaction, plus a business, business operation or commercial transaction | TR 92/3 paras 6, 35 |
| Purpose | Judged objectively; need not be the sole or dominant purpose, a significant purpose is enough; usually needed when the property is acquired | TR 92/3 paras 7-9, 38-41 |
| Later venture | An asset acquired for another purpose can later be ventured into a business or a profit-making scheme, and the profit is then income | TR 92/3 para 42 |
| Commercial character factors | Nature of the entity; its other activities; money involved and profit sought; nature, scale and complexity; manner carried out (agents, advisers, public market); connection with other parties; nature of the property; timing of the steps | TR 92/3 paras 13, 49 |
| Land as trading stock | Held for resale and a business dealing in land has commenced; the business starts with a definite and continuous cycle of operations designed to lead to sale; one acquisition can be enough | TD 92/124 paras 1-3 |
| Trading stock definition | Anything acquired and held for sale or exchange in the ordinary course of a business | ITAA 1997 s 70-10(1) |
| Multiple purposes | Land can be trading stock when held for more than one purpose; the ATO looks for a 'substantial purpose' of sale at a profit | ATO 'Tax consequences on sales of property' |
| Change of intention | For property bought as a capital asset, the overall gain is split between a capital gain and ordinary income; only the net profit from the undertaking is ordinary income | ATO 'Tax consequences on sales of property' |
| Starting to hold land as trading stock | Treated as sold and bought back for cost or market value just before, as elected; election by the time the return for that year is lodged (or as soon as reasonable after realising), or later if the Commissioner allows | ITAA 1997 s 70-30(1)-(2) |
| CGT event K4 | Happens if you start holding an asset you already own as trading stock and elect market value under s 70-30(1)(a); the time of the event is when you start; gain if that market value exceeds the cost base, loss if it is less than the reduced cost base; disregarded for pre-CGT assets | ITAA 1997 s 104-220 |
| No double tax | A capital gain is reduced by an amount otherwise included in assessable income because of the same event | ITAA 1997 s 118-20(1)-(3) |
| Year-end trading stock | Compare values at the start and end of the year; value each item at cost, market selling value or replacement value | ITAA 1997 ss 70-35, 70-45(1) |
| Subdivided lots | Each subdivided block is a separate asset with the original acquisition date; the original cost base is divided on a reasonable basis | ATO 'Subdividing land' |
| Pre-CGT property | Section 15-15 does not apply to property acquired on or after 20 September 1985 | ITAA 1997 s 15-15(2)(b) |

### Step 1: Build a dated chronology

Record every decision, application, agreement, borrowing, works stage and sale from acquisition to the latest sale, with the purpose each document states. Where documents conflict (a council application, a loan application and a family statement giving different reasons), record each statement, its author, date and purpose side by side in a **conflicting statements register**. None overrides another; the conflict goes to the reviewer. The ATO says written records are the best evidence of purpose and are worth more than recollection in hindsight.

### Step 2: Set out the 3 characterisations without choosing

State (a), (b) and (c) from Scope with their authorities. Record what each would need on the evidence: (b) needs both TR 92/3 elements; (c) needs both TD 92/124 conditions; (a) is the residual where neither applies. Profit-making need not be the dominant purpose (TR 92/3 para 40).

### Step 3: Prepare the factors matrix

One row for each factor in the ATO page, cross-referenced to TR 92/3 para 49: type of entity; its other activities; costs relative to the undeveloped land's value and the financial risk taken; complexity and steps; parties and phases; relationships with other parties; purpose in buying the land; timing and steps of the sale. For each row, record the evidence pointing to capital, the evidence pointing to revenue, document references and gaps. Weigh nothing in isolation and record no conclusion. Indicators the ATO lists include:

- **Towards capital:** an individual selling for personal reasons; no history as a developer; minimal works to meet council requirements; minimal involvement; low cost relative to land value; minimal financial risk; a straightforward one-off sale; land held a long time as a home, rental or farm.
- **Towards revenue:** a business entity set up to acquire and develop; approvals sought soon after acquisition; significant improvements or construction; purchase of neighbouring blocks; lobbying for rezoning; significant borrowing against the land; multiple professional parties acting on the owner's instructions; engaging a developer for a fee and sharing in sale profits; a short holding period; land banking.

A comparison with *Morton* is a reviewer question, not support for either side: the ATO says that case turned on its facts and the taxpayer's adherence to his 2 negotiating 'tenets' (DIS para 27).

### Step 4: Test intention over time and work lot by lot

Record the purpose at acquisition and at every later point where the evidence suggests it changed (TR 92/3 para 42). For a proposed change of intention, record its date and the valuation evidence needed at that date; never estimate a value. After subdivision each lot is a separate asset (ATO 'Subdividing land'): keep sold and retained lots, and lots built for different purposes, on separate rows.

### Step 5: Prepare conditional workpapers for each open characterisation

- **Business (c):** a trading stock schedule by lot. Where land already owned starts to be trading stock, record the s 70-30 election options (cost or market value just before), the election deadline and the K4 consequence of a market value election (s 104-220). Value lots on hand at year end under s 70-45 and bring the movement to account under s 70-35. ATO land-sale Example 6 says the CGT discount, small business concessions and main residence exemption do not apply to income from a sale beyond mere realisation, and the ATO page says the main residence exemption does not apply to assets held as trading stock.
- **Isolated undertaking (b):** a net profit computation by lot (proceeds less apportioned land cost, development and selling costs), following ATO land-sale Example 6. The year in which the profit is derived and recognised is not settled by the sources read here: leave recognition timing as Needs Input (R-AU-PD-6).
- **Capital (a):** route the CGT event register, cost base apportionment and any main residence question to `au-capital-gains`, and concessions to `au-small-business-cgt`.
- **Both a profit and a capital gain:** apply s 118-20 so the same amount is not taxed twice, as the ATO's examples do; work the remaining gain in `au-capital-gains`.

Registration alone does not make an amount GST-exclusive; follow the GST treatment of each supply and acquisition. Assessable income leaves out only the GST payable on a taxable supply (ITAA 1997 s 17-5), so the full price of an input taxed sale stays in. A deduction leaves out only an amount relating to an input tax credit the seller is entitled to (s 27-5), so a cost with no credit stays GST-inclusive. Section 27-5 speaks of deductions: for an undertaking's net profit, apply the same split and flag it for the reviewer. Route the GST question itself to `au-gst-property`.

### Step 6: Route and record

Use the same chronology for GST (`au-gst-property`), duty (`au-stamp-duty`) and land tax (`au-land-tax`) so the characterisations stay consistent across workpapers. Record whether the reviewer may wish to consider a private ruling; never apply for one (R-AU-PD-2).

### Permitted factual defaults

These apply only to missing facts where the law above is established. Disclose each one, its alternative and its effect.

| Missing fact | Default | Disclosure |
|---|---|---|
| Shared development or selling costs not allocated by lot | Allocate in the proportions of the valuer's apportionment of the land between lots, as ATO land-sale Example 2 does for subdivision costs; with no valuation, Needs Input | Show the allocation; a contract price basis cannot allocate to lots that are kept |

**No default is permitted** for purpose, the commencement of a business, the date of a change of intention, a market value, the characterisation itself, whether an amount includes GST or carries an input tax credit, or the year of recognition. Each is Needs Input.

### Working paper extension

```
AUSTRALIA PROPERTY DEVELOPMENT -- REVENUE OR CAPITAL EVIDENCE
Entity: [name]   Income year: 2026-27   Prepared: [date]   Decision: registered tax agent

1. CHRONOLOGY (date | event | document | stated purpose | author)
2. CONFLICTING STATEMENTS REGISTER
3. FACTORS MATRIX (factor | capital evidence | revenue evidence | refs | gaps)
4. INTENTION OVER TIME (purpose at acquisition; each change: date, evidence, valuation needed)
5. CONDITIONAL WORKPAPERS (one set per characterisation still open)
   (a) route to au-capital-gains   (b) net profit by lot   (c) trading stock schedule, s 70-30 options
6. s 118-20 RECONCILIATION (where profit and gain both arise)
7. ROUTING LIST and REVIEWER FLAGS
```

## Worked cases

All facts and figures are hypothetical and set in the 2026-27 income year.

### Case 1: Isolated profit-making undertaking, one lot (TR 92/3; s 118-20)

An individual with no development history buys a block for $600,000, subdivides it into 2 lots, builds a house on lot 2 and sells it; the evidence supports a profit-making purpose at acquisition and a commercial transaction, but no business. A valuer apportions 50% of the land to lot 2. Shared subdivision costs are $80,000; the house costs $450,000; selling costs are $30,000; lot 2 sells for $1,100,000. Proceeds are net of the GST payable on the sale (s 17-5) and costs are net of input tax credits the seller is entitled to (s 27-5): if lot 2 is a taxable supply at a contract price of $1,210,000 including GST, the GST is $110,000, which is 1/11 of the price and not 10% of it (GST Act ss 9-70, 9-75(1)), leaving the $1,100,000 used here. Whether the sale is taxable, GST at 1/11 of the price or under the margin scheme, and GST at settlement withholding are worked in `au-gst-property`. For illustration the CGT cost base is assumed to hold the same elements; the capital proceeds are also $1,100,000, because s 116-20(5) disregards the net GST on the supply in working them out.

```oa-check
name: Isolated profit-making undertaking net profit by lot with s 118-20 2026-27
inputs:
  land_cost_total: 600000
  lot_share_percent: 50
  shared_subdivision_costs: 80000
  lot_build_costs: 450000
  lot_selling_costs: 30000
  lot_proceeds: 1100000
steps:
  - lot_land_cost: pct(land_cost_total, lot_share_percent)
  - lot_shared_costs: pct(shared_subdivision_costs, lot_share_percent)
  - lot_total_costs: lot_land_cost + lot_shared_costs + lot_build_costs + lot_selling_costs
  - lot_net_profit: lot_proceeds - lot_total_costs
  - capital_gain_before_s118_20: lot_proceeds - lot_total_costs
  - capital_gain_after_s118_20: max(capital_gain_before_s118_20 - lot_net_profit, 0)
expected:
  lot_land_cost: 300000
  lot_shared_costs: 40000
  lot_total_costs: 820000
  lot_net_profit: 280000
  capital_gain_before_s118_20: 280000
  capital_gain_after_s118_20: 0
```

The $280,000 net profit is ordinary income if characterisation (b) is adopted, and s 118-20 reduces the capital gain on the same event to nil. Lot 1 stays on its own row. The year of recognition remains Needs Input.

### Case 2: Land already owned becomes trading stock (ss 70-30, 104-220)

A company has held land as a long-term investment since 2015 (CGT cost base $400,000; its s 70-30(3) cost is also $400,000). In September 2026 it resolves to develop and sell 10 lots, and the evidence supports the start of a business dealing in land. A dated valuation puts the land at $1,000,000 just before it became trading stock. Development costs are $800,000 and all 10 lots sell in 2026-27 for $2,500,000, so no lots are on hand at year end. Proceeds are net of the GST payable on the sales (s 17-5) and costs are net of input tax credits the company is entitled to (s 27-5). Whether the sales are taxable, GST at 1/11 of the price or under the margin scheme, and GST at settlement withholding are worked in `au-gst-property`.

```oa-check
name: Land becoming trading stock s 70-30 election comparison 2026-27
inputs:
  land_cost_base_cgt: 400000
  land_cost_70_30: 400000
  land_mv_at_start: 1000000
  development_costs: 800000
  lot_sales: 2500000
steps:
  - mv_election_k4_gain: land_mv_at_start - land_cost_base_cgt
  - mv_election_trading_profit: lot_sales - land_mv_at_start - development_costs
  - mv_election_total: mv_election_k4_gain + mv_election_trading_profit
  - cost_election_trading_profit: lot_sales - land_cost_70_30 - development_costs
  - total_difference: mv_election_total - cost_election_trading_profit
expected:
  mv_election_k4_gain: 600000
  mv_election_trading_profit: 700000
  mv_election_total: 1300000
  cost_election_trading_profit: 1300000
  total_difference: 0
```

The total gain is the same; the election moves $600,000 between a K4 capital gain and trading profit. A cost election gives no K4 event (s 104-220(1)(b)). The election belongs to the company and must be made by the time its 2026-27 return is lodged (s 70-30(2)); record it, do not make it. For an individual or trust, the treatment of the K4 gain goes to `au-capital-gains`.

### Case 3: Mere realisation of a home block

An individual buys a home on a large block, later subdivides off the part he does not need to reduce his home loan, does only the council-required works and sells the vacant lot (ATO land-sale Example 2). Purchase as a home, no prior dealings, a straightforward subdivision and no further value-adding work point to characterisation (a). Record the factors; route the cost base apportionment and the CGT computation to `au-capital-gains`.

### Case 4: Mixed purposes within one development

An owner of 17 years demolishes the home and builds 3 townhouses: one to live in, one to rent and one to sell; illness then forces sale of all 3 (the ATO's 'Mr Block' example). The ATO treats the gain on the townhouse built to sell as ordinary income from a profit-making undertaking, and the other 2 as realisations of capital assets. Keep 3 rows with separate characterisations; route GST, where the ATO found registration required, to `au-gst-property`.

### Case 5: Conflicting statements

A family company's minutes record land bought 'for long-term investment', but the director later signs an agreement sharing sale profits with a builder. Record both documents in the chronology and the conflicting statements register, and the agreement's terms in the 'relationships with other parties' row. The ATO lists engaging a developer and sharing in sale profits as pointing towards a commercial deal; the minutes point the other way. Do not characterise the sale.

### Case 6: Input taxed resale by a registered trader (GST Act ss 40-65, 11-15; ss 17-5, 27-5)

A GST-registered company in the business of dealing in land buys a house as trading stock for $600,000 and sells it in the same year for $900,000. The house is neither new nor commercial residential premises and is to be used predominantly for residential accommodation, so the sale is input taxed (GST Act s 40-65) and no GST is payable on it. The agent's fee of $11,000 includes $1,000 of GST. It relates to the input taxed sale, so it carries no input tax credit (GST Act s 11-15(2)(a)).

```oa-check
name: Input taxed resale keeps non-creditable GST in selling costs 2026-27
inputs:
  proceeds: 900000
  stock_cost: 600000
  selling_costs_including_gst: 11000
  gst_in_selling_costs: 1000
  creditable_percent: 0
steps:
  - input_tax_credit: pct(gst_in_selling_costs, creditable_percent)
  - deductible_selling_costs: selling_costs_including_gst - input_tax_credit
  - profit: proceeds - stock_cost - deductible_selling_costs
expected:
  input_tax_credit: 0
  deductible_selling_costs: 11000
  profit: 289000
```

The profit is $289,000. Recording the fee at $10,000 because the seller is registered would overstate it by $1,000. The classification of the premises stays with `au-gst-property`.

## When to refuse or refer

Stop the affected calculation where a fact, source condition or scope requirement above is unresolved, and return Needs Input or the refusal below.

### Refusal catalogue

| Code | Trigger | Message (verbatim) |
|---|---|---|
| R-AU-PD-1 | Asked to decide the characterisation | "Whether this profit is capital or revenue is a judgement for the registered tax agent. I have prepared the chronology, factors matrix and conditional workpapers only." |
| R-AU-PD-2 | Asked to apply for, or draft, a private ruling | "A private ruling application is the taxpayer's or registered tax agent's decision. I have noted it as an option for the reviewer." |
| R-AU-PD-3 | A main residence, CGT discount or cost base question | "That is a CGT computation. Route it to au-capital-gains." |
| R-AU-PD-4 | Primary production land, a farming business winding down, or reliance on TR 97/11 | "Whether a primary production business is carried on is worked through the TR 97/11 matrix in `au-primary-production`; capital gains on farm land go to `au-capital-gains`. Refer the characterisation of this sale to the reviewer." |
| R-AU-PD-5 | A foreign resident seller, or a trust or partnership whose members' residence affects the outcome | "Foreign resident consequences are outside this guide. Route to au-nonresident-cgt and a specialist." |
| R-AU-PD-6 | The year in which a profit-making undertaking's profit is derived or recognised, or staged settlements across years | "The recognition year for this profit is not established by the sources this guide relies on. Refer to the reviewer before allocating profit to a year." |
| R-AU-PD-7 | Land acquired before 20 September 1985 | "Pre-CGT land engages s 15-15 and s 25A ITAA 1936 rules this guide does not cover. Refer to a specialist." |

### Reviewer attention thresholds

The reviewer attention threshold is **AUD 0**: every characterisation, s 70-30 election option and s 118-20 reconciliation requires review whatever its amount. Flag regardless of amount: any entry in the conflicting statements register; any change of intention without a dated valuation; any development or joint venture agreement with a profit or proceeds share; any borrowing secured on the land; and any lot whose characterisation differs from another lot's.

### Prohibitions

- NEVER characterise a sale, or weigh one factor in isolation.
- NEVER estimate a market value at a change of intention.
- NEVER apply the CGT discount, small business concessions or main residence exemption to trading stock or to a revenue profit.
- NEVER tax the same amount as both profit and capital gain; apply s 118-20.
- NEVER treat *Morton* as support for capital treatment; it turned on its facts.
- NEVER present figures as definitive.

## Completion checklist

- [ ] Chronology runs from acquisition to the latest sale, every entry citing a document.
- [ ] Conflicting statements register records author, date and purpose for each statement.
- [ ] Factors matrix covers every ATO factor, with evidence both ways and gaps, and no conclusion.
- [ ] Each change of intention has a date and the valuation evidence needed.
- [ ] Lot-level proceeds and costs agree to contracts and the ledger; sold and retained lots are separate rows.
- [ ] Conditional workpapers exist for each characterisation still open; s 118-20 reconciliation done where both arise.
- [ ] Any s 70-30 election is recorded as the taxpayer's, with its deadline.
- [ ] GST, duty and land tax routed using the same chronology.
- [ ] Every unresolved item records the evidence needed, owner, status and next action.

## Sources

| Source | URL | Read on |
|---|---|---|
| TR 92/3, whether profits on isolated transactions are income: paras 6-9, 13, 21, 35-42, 49 | https://www.ato.gov.au/law/view/document?docid=TXR/TR923/NAT/ATO/00001 | 2026-11-02 |
| TD 92/124, when land is trading stock (consolidated 7 April 2004): paras 1-3 | https://www.ato.gov.au/law/view/document?docid=TXD/TD92124/NAT/ATO/00001 | 2026-11-02 |
| ATO, Tax consequences on sales of property (QC71028, last updated 27 February 2025): factors, multiple purposes, change of intention, examples | https://www.ato.gov.au/businesses-and-organisations/assets-and-property/property/tax-consequences-on-sales-of-property | 2026-11-02 |
| ATO, Examples of tax consequences on sales of land including small-scale land subdivision: Examples 2 and 6 | https://www.ato.gov.au/law/view/document?DocID=GUI/tax-consequences-land-sales&PiT=99991231235958 | 2026-11-02 |
| ATO, Subdividing land (QC23640, last updated 22 June 2026) | https://www.ato.gov.au/individuals-and-families/investments-and-assets/property-and-land/land-vacant-land-and-subdividing/subdividing-land | 2026-11-02 |
| ATO decision impact statement, *Commissioner of Taxation v Morton* [2026] FCAFC 31: paras 1-2, 18, 22-23, 26-28 | https://www.ato.gov.au/law/view/document?docid=LIT/ICD/VID578of2025/00001 | 2026-11-02 |
| ITAA 1997 s 6-5 (ordinary income) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/6-5 | 2026-11-02 |
| ITAA 1997 s 15-15 (profit-making undertaking or plan) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/15-15 | 2026-11-02 |
| ITAA 1997 s 70-10 (trading stock) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/70-10 | 2026-11-02 |
| ITAA 1997 s 70-30 (starting to hold as trading stock) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/70-30 | 2026-11-02 |
| ITAA 1997 s 70-35 (trading stock in assessable income) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/70-35 | 2026-11-02 |
| ITAA 1997 s 70-45 (year-end valuation) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/70-45 | 2026-11-02 |
| ITAA 1997 s 104-220 (CGT event K4) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/104-220 | 2026-11-02 |
| ITAA 1997 s 118-20 (reducing capital gains if amount otherwise assessable) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/118-20 | 2026-11-02 |
| ITAA 1997 s 17-5 (GST and increasing adjustments) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/17-5 | 2026-11-06 |
| ITAA 1997 s 27-5 (input tax credits and decreasing adjustments) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/27-5 | 2026-11-06 |
| GST Act s 11-15 (meaning of creditable purpose) | https://www.ato.gov.au/law/view/document?DocID=PAC/19990055/11-15 | 2026-11-06 |
| GST Act s 40-65 (sales of residential premises) | https://www.ato.gov.au/law/view/document?DocID=PAC/19990055/40-65 | 2026-11-06 |
| GST Act ss 9-70, 9-75 (amount of GST; value of a taxable supply) | https://www.ato.gov.au/law/view/document?DocID=PAC/19990055/9-75 | 2026-11-11 |
| ITAA 1997 s 116-20(5) (net GST disregarded in capital proceeds) | https://www.ato.gov.au/law/view/document?DocID=PAC/19970038/116-20 | 2026-11-11 |

Named in the sources but not read in this session: TR 97/11 (primary production business), MT 2006/1 (held by `au-gst-property`), TD 97/3 (subdivided land as separate assets) and s 25A ITAA 1936.

**Currency and revision.** Version 0.1, currency date 2 November 2026. Change log: v0.1 (2 November 2026) first draft from primary sources read that day; 6 November 2026 correction: registration alone does not make an amount GST-exclusive (ss 17-5, 27-5); 11 November 2026 correction: the worked cases restated net of GST under ss 17-5 and 27-5, with a 1/11 example under GST Act ss 9-70 and 9-75 and capital proceeds under s 116-20(5); awaiting qualified Australian review.

Method adapted by its author from the `au-property-development-income` skill in ryanduguid/australian-accounting-skills (commit 3e110da). This guide is licensed under FSL-1.1-ALv2, not the OA Guide License; see LICENSING.md.

Topic chosen from the public Ask Nagaris skill list (names only); no Nagaris text was used.

Copyright 2026 Ryan Duguid. From github.com/ryanduguid/australian-accounting-skills, FSL-1.1-ALv2. Copies and adaptations of this file must keep this notice.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
