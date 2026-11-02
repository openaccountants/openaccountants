---
name: india-crypto-tax
description: Use this skill whenever asked about India cryptocurrency or virtual digital asset (VDA) taxation. Trigger on phrases like "crypto tax India", "Bitcoin India tax", "VDA tax", "Section 115BBH", "194S TDS crypto", "crypto TDS India", "virtual digital asset India", "crypto income India", "NFT tax India", "mining tax India", "staking tax India", "WazirX tax", "CoinDCX tax", "crypto loss India", "Schedule VDA", "ITR crypto", "30% crypto tax India", "1% TDS crypto", or any question about the income tax, TDS, or reporting treatment of cryptocurrency, tokens, NFTs, or virtual digital assets under Indian tax law. Covers Finance Act 2022 amendments (Sections 115BBH, 194S, 2(47A)), the no-loss-offset rule, ITR Schedule VDA, and advance tax obligations. ALWAYS read this skill before touching any India crypto work.
version: 1.0
jurisdiction: IN
tax_year: 2026
last_updated: 2026-10-17
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - in-income-tax
category: crypto
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India Crypto and Virtual Digital Asset Tax

This Guide covers Indian income tax and tax deducted at source (TDS) on crypto, tokens, NFTs and other virtual digital assets (VDAs) for individuals, Hindu undivided families (HUFs) and companies. Figures are for tax year 2026. This means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act, 2025, which replaced the Income-tax Act, 1961 from 1 April 2026. Section numbers changed with the new Act: the 1961 Act sections that older material quotes for crypto do not apply to tax year 2026-27, and this Guide names only the 2025 Act sections. Income earned up to 31 March 2026 (assessment year 2026-27) is still taxed and returned under the 1961 Act; this Guide does not cover it.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | India |
| Tax | Income-tax on income from the transfer of a virtual digital asset, and TDS on the price paid for one |
| Currency | INR |
| Tax year | 1 April to 31 March. Tax year 2026-27 runs from 1 April 2026 to 31 March 2027 |
| Primary law | Income-tax Act, 2025 (30 of 2025): section 2(111) (definition), section 194(1) Table serial 4 (rate and loss rule), section 393(1) Table serial 8(vi) and section 393(4) Table serial 12 (TDS) |
| Rates law for the year | Finance Act, 2026 (4 of 2026), section 3 (surcharge and cess for tax year 2026-27) |
| Procedure | Income-tax Rules, 2026: rule 218 (paying TDS, Form No. 141), rule 219 (exchange statements, Form No. 142), rule 164 (which return form) |
| Tax authority | Income Tax Department, Central Board of Direct Taxes |
| Rate, TDS and thresholds | In the tables in Sections 3 and 7 |

### VDA definition (section 2(111) of the 2025 Act)

| Clause | What it covers |
| --- | --- |
| (a) | Any information, code, number or token, not being Indian currency or foreign currency, generated through cryptographic means or otherwise, that gives a digital representation of value, exchanged with or without consideration, with the promise or representation of having inherent value, or that functions as a store of value or a unit of account, and can be transferred, stored or traded electronically |
| (b) | A non-fungible token or any other token of similar nature, by whatever name called |
| (c) | Any other digital asset the Central Government notifies |
| (d) | Any crypto-asset that relies on a cryptographically secured distributed ledger or similar technology, whether or not it falls in (a), (b) or (c). This clause is new in the 2025 Act text |
| Exclusions | Indian currency and foreign currency are outside clause (a). The Central Government may exclude any digital asset by notification |

The definition is in the Act at https://egazette.gov.in/WriteReadData/2025/265620.pdf and the Act text prints "(not being Indian currency or foreign currency)" and "the Central Government may, by notification, exclude any digital asset from this definition". It does not itself name the Digital Rupee: check for an exclusion notification before treating any central bank digital currency as outside the regime.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown cost of acquisition | Treat cost as nil until the client proves a cost. Stop and ask if the amount is material |
| Unknown whether a trader or an investor | The section 194 rate applies to any income from the transfer of a VDA either way. Classify the head of income separately and refer if it matters |
| Unknown how a receipt from mining, staking or an airdrop is taxed | Do not apply the section 194 rate to the receipt itself. Refer (Section 5) |
| Unknown fair market value at receipt | Use a documented exchange price at the time of the receipt and record the source |
| VDA received free from a non-relative | Test the aggregate fair market value against the section 92(2)(m) threshold in Section 7.4 |

## Section 2: Classification Rules

### One rate for every transfer, no capital versus income split

Section 194(1) of the 2025 Act, Table serial 4, taxes any income from the transfer of any virtual digital asset, for any person, at the rate in the Section 3 table. The rule does not depend on how long the asset was held, how often the person trades, or whether the gain is capital or revenue. The section works in two parts: tax on the VDA income at the section 194 rate, plus the tax the person would pay if total income were reduced by that VDA income (section 194(1)(a) and (b)). So the VDA income is taxed at the flat rate from the first rupee, and the slab rates and the nil band apply only to the rest of the income.

| Question | Answer under the 2025 Act |
| --- | --- |
| Does holding period matter? | No. Section 194 Table serial 4 has one rate for any person and any VDA transfer |
| Does trader versus investor matter? | Not for the rate. It can matter for the return form (Section 7.1) and the due date (Section 7.5) |
| Is a VDA a capital asset? | Section 194(2)(n) applies the section 2(109) meaning of "transfer" to any VDA "whether capital asset or not", so the rate applies either way |
| Does the new-regime rebate cut the tax on VDA income? | No. Section 156(3) caps the section 156(2) rebate at the tax payable at the section 202(1) rates, and VDA income is taxed at the section 194 rate instead |

Source for this table: https://egazette.gov.in/WriteReadData/2025/265620.pdf

### What counts as a transfer

Section 2(109) of the 2025 Act says a transfer includes "(a) the sale, exchange or relinquishment of the asset", the extinguishment of any rights in it, and the other events listed there. Section 194(2)(n) applies that meaning to every VDA. So:

- Selling a VDA for rupees or foreign currency is a sale.
- Swapping one VDA for another is an exchange, which is a transfer of the VDA given up.
- Paying for goods or services with a VDA is an exchange of the VDA.
- Giving a VDA away, and moving a VDA between two wallets the same person owns, are not named in section 2(109). Do not treat either as settled: see Section 9 and the refer list.

## Section 3: Rate Table

### Tax on income from the transfer of a VDA (section 194(1), Table serial 4)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate on income from the transfer of any VDA, any person | 30% | "4. Any Any income from 30% (a) No deduction person. the transfer of any" |
| Deductions allowed | Cost of acquisition only | "expenditure (other than cost of acquisition, if any) or allowance or set off of any loss" |
| Loss on a VDA transfer | Not set off against any income and not carried forward | "no set off of loss from transfer of the virtual digital asset computed herein shall be allowed against income computed under any provision of this Act to the assessee and such loss shall not be allowed to be carried forward to succeeding tax years" |

### Surcharge and cess, tax year 2026-27 (Finance Act, 2026, section 3)

Cess is charged on income-tax plus surcharge. Surcharge depends on total income, including the VDA income. Serial 1, which lists tax under section 194, applies only to a person "not having any income chargeable to tax under section 202", that is, a person who has left the new regime. Serial 10 lists only section 202. This Guide reads serial 10 as covering a new-regime person's whole tax, because section 202(1) makes the new-regime computation "subject to Parts A, B, E" of the Chapter; the Finance Act does not say so in terms. Confirm with an accountant before relying on the 25% cap for VDA tax.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Health and Education Cess, on income-tax plus surcharge | 4% | "calculated at the rate of 4% of such income-tax and surcharge" |
| Surcharge starts where total income exceeds | INR 5,000,000 | "exceeds ₹ 5000000 but does" |
| Surcharge rate, total income above INR 5,000,000 up to INR 10,000,000 (both regimes) | 10% | "rate of 10%;" |
| Next threshold | INR 10,000,000 | "exceeds ₹ 10000000 but does not exceed ₹ 20000000, at the" |
| Surcharge rate, above INR 10,000,000 up to INR 20,000,000 (both regimes) | 15% | "rate of 15%;" |
| Next threshold | INR 20,000,000 | "198 of the said Act) exceeds ₹ 20000000, at the rate of 25%; (iv) where the total income (including dividend income" |
| New regime (serial 10): top surcharge rate, above INR 20,000,000 | 25% | "198 of the said Act) exceeds ₹ 20000000, at the rate of 25%; (iv) where the total income (including dividend income" |
| Old regime (serial 1): rate above INR 20,000,000 up to INR 50,000,000 | 25% | "rate of 25%;" |
| Old regime (serial 1): top threshold | INR 50,000,000 | "(iv) where the total income exceeds ₹ 50000000" |
| Old regime (serial 1): top surcharge rate | 37% | "rate of 37%." |

Companies, firms and co-operative societies use other serials of the same Table (for example serials 6, 7 and 9 for companies). Refer.

Marginal relief applies where income only just crosses a surcharge threshold. The formula is in section 3(5) of the Finance Act, 2026 and the First Schedule Part I-B; apply it from the Act, not from a rule of thumb.

Do not quote a single effective rate for VDA income. The rate in the first table, the surcharge band and the cess combine differently for each client; compute each case.

## Section 4: Cost Basis

### What may be deducted

| Item | Allowed? | Basis |
| --- | --- | --- |
| Cost of acquisition | Yes | Section 194 Table serial 4, column E(a): "other than cost of acquisition, if any" |
| Cost of improvement | No | Column E(a) allows no expenditure other than cost of acquisition |
| Exchange fees, gas fees, commissions on sale | No | Same: no other expenditure or allowance |
| Any loss, from a VDA or any other source | No | Column E(a) and (b) |
| Depreciation | No | No allowance is permitted |

Source for this table: https://egazette.gov.in/WriteReadData/2025/265620.pdf

Whether a purchase fee forms part of the "cost of acquisition" is not settled by the Act text. Treat it as not deductible unless an accountant decides otherwise.

### Cost basis methods

The Act says "cost of acquisition, if any" and names no method for matching sales to purchases. Pick one method (first in, first out, or specific identification with records), document it, and apply it consistently across years. An accountant should confirm the method for a large or mixed portfolio.

### Nil-cost cases

Where nothing was paid for a VDA (mining, staking rewards, airdrops, tokens from a fork), there may be no cost of acquisition: the Act's words are "if any". If the receipt was taxed as income when received, an accountant decides whether that taxed value can be the cost on a later sale; the Act does not say so for VDAs (see Section 5 and Section 7.4).

## Section 5: DeFi, Staking, Mining and Airdrops

The 2025 Act has no section written for mining, staking, lending, liquidity pools or airdrops. Only two points are settled by the Act text:

1. A later sale, swap or other transfer of the tokens is a VDA transfer taxed under section 194 (Sections 2 and 3).
2. A VDA received without consideration, or for less than its fair market value, is "property" for section 92(2)(m) when the recipient holds it as a capital asset, so the gift rule in Section 7.4 can apply to it.

Everything else below is a classification question for an accountant. Do not state it as law.

### 5.1 Mining

| Point | Status |
| --- | --- |
| Tax on the tokens when mined | Not settled by the Act. It may be business income or income from other sources at slab rates. Refer |
| Cost of mined tokens on a later sale | "cost of acquisition, if any": possibly nil. Refer if the receipt was taxed |
| Later sale or swap | Section 194 transfer |

### 5.2 Staking

| Point | Status |
| --- | --- |
| Tax on rewards when received | Not settled by the Act. Refer |
| Later sale or swap of reward tokens | Section 194 transfer |

### 5.3 Airdrops

| Point | Status |
| --- | --- |
| Airdrop received for nothing from a non-relative | Section 92(2)(m) can tax it if the aggregate value of such property received in the year passes the threshold in Section 7.4 |
| Airdrop received for doing something (a task, a service) | Not settled by the Act. Refer |
| Later sale of airdropped tokens | Section 194 transfer |

### 5.4 DeFi lending, yield and liquidity pools

| Activity | Status |
| --- | --- |
| Interest or yield paid in tokens | Not settled by the Act. Refer |
| Depositing tokens into a pool for LP tokens | Likely an exchange of one VDA for another, so a section 194 transfer. Confirm the facts |
| Withdrawing from the pool | Same |
| Impermanent loss | A loss on a VDA transfer: no set-off and no carry forward (Section 8) |

### 5.5 Forks

| Point | Status |
| --- | --- |
| New tokens from a fork | No price was paid. Cost "if any": refer before using nil |
| Sale of forked tokens | Section 194 transfer |
| Original tokens | Cost unchanged |

## Section 6: NFT Treatment

An NFT is a VDA under section 2(111)(b). Clause (i) of the section says "non-fungible token" means "such digital asset as the Central Government may, by notification, specify". Check whether a notification covers the token before relying on clause (b) alone; clause (d) may still catch it if it runs on a distributed ledger.

| Event | Treatment |
| --- | --- |
| Buying an NFT for rupees | Acquisition. Record the cost |
| Selling an NFT | Section 194 transfer, taxed at the Section 3 rate on proceeds less cost |
| Swapping NFT for NFT, or NFT for a token | Exchange: a section 194 transfer of what is given up |
| An artist minting and selling their own NFT | Section 194 transfer of the NFT. Whether the creator also has business income is not settled. Refer |
| Royalty on a resale paid to the creator | Not settled by the Act. Refer |
| NFT received free from a non-relative | Section 92(2)(m) gift rule (Section 7.4) |
| NFT becomes worthless | Any loss is not set off and not carried forward |

## Section 7: Reporting Requirements

### 7.1 Which return form (rule 164, Income-tax Rules, 2026)

Rule 164 covers returns for the tax year starting 1 April 2026. A person with income taxed under Part A of Chapter XIII of the 2025 Act (which includes section 194) cannot use ITR-1 (rule 164(3)(n)) or ITR-4 (rule 164(6)(o)).

| Taxpayer | Form |
| --- | --- |
| Individual or HUF with VDA income and no business or profession income | ITR-2 (rule 164(4)) |
| Individual or HUF with business or profession income | ITR-3 (rule 164(7)) |
| Company (other than one filing ITR-7) | ITR-6 (rule 164(9)) |

Source: https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf

The return forms for tax year 2026-27 are filed in 2027. Check the VDA schedule in the form when it is released; the schedule layout is not on a page this Guide could read.

### 7.2 What to record for each VDA transfer

Keep, for every transfer: the type of VDA, the date acquired, the date transferred, the cost of acquisition in rupees, the consideration received in rupees, and the TDS deducted. These are the facts the section 194 computation needs. Keep the exchange statements and wallet records that prove them.

### 7.3 TDS on the transfer of a VDA (section 393)

Section 393(1) Table serial 8(vi) applies to "Any person" paying a resident consideration for the transfer of a VDA. Tax is deducted at the time of credit or payment, whichever is earlier. Section 393(4) Table serial 12 switches TDS off where the year's consideration from that payer stays within the limits below.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| TDS rate on consideration for the transfer of a VDA | 1% | "Rate: 1% of consideration for" |
| No TDS if the year's consideration does not exceed, for a payer who is an individual or HUF with business turnover up to one crore rupees or professional receipts up to fifty lakh rupees in the preceding tax year, or with no business or profession income | INR 50,000 | "(a) ₹ 50000, when payable by an individual" |
| No TDS if the year's consideration does not exceed, for any other payer | INR 10,000 | "(b) ₹ 10000, when payable by any person other than the person referred to in clause (a)" |
| Higher TDS where the seller gives no valid PAN | 20% | "at the rate of 5% where tax is required to be deducted under section 393(1) [Table: Sl. No. 8(ii) or 8(v)]; or 20% in any other case" |

Points the Act settles:

- The limits are on consideration "during the tax year", and the turnover test looks at "the tax year immediately preceding the tax year in which such virtual digital asset is transferred". Above the limit, tax is deducted on the entire amount (section 393(1)(a)).
- Where the price is paid wholly in kind, or in another VDA with no cash, or the cash part is too small to cover the tax, the payer "shall ensure that the tax required to be deducted has been paid, before releasing such consideration" (Note 6 to the section 393(1) Table). In a VDA-for-VDA swap, settle on the facts who is the payer on each leg; Note 6 then applies to that payer.
- A payer who is an individual or HUF within serial 12(a) does not need a tax deduction account number (section 397(1)(c)). The Finance Act, 2026 substitutes clause (c) with effect from 1 October 2026; the VDA exemption is kept.
- TDS deducted counts as tax paid on behalf of the seller (section 390(5)) and is credited against the seller's tax for the year.
- Section 393(1) covers payments to residents. For a non-resident seller, refer.

### 7.4 Gifts and free receipts of a VDA (section 92(2)(m))

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Property received without consideration: taxable as income from other sources where the aggregate fair market value in the tax year exceeds | INR 50,000 | "(A) without consideration, the aggregate fair market value of which exceeds ₹ 50000, the whole of the aggregate fair market value of such property" |
| Property received for less than fair market value: taxable where the shortfall exceeds | INR 50,000 | "(B) for a consideration which is less than the aggregate fair market value of the property by an amount exceeding ₹ 50000" |

- "Property" means a "capital asset of the assessee" in the section 92(5)(f) list, which ends "(x) virtual digital asset;". A VDA the recipient holds as stock-in-trade of a business is not "property" for this rule: refer.
- It is a cliff. Once the aggregate passes the threshold, the whole aggregate value is taxed, not just the excess. At or below the threshold, nothing is taxed under this rule.
- The test is the aggregate for the year, from "any person or persons", not each gift separately.
- Section 92(3) excludes receipts "(a) from any relative; or (b) on the occasion of marriage of the individual; or (c) under a will or by way of inheritance", and the other cases listed there. "Relative" is defined in section 92(5)(g) (spouse, siblings, siblings of the spouse or parents, lineal ascendants and descendants, and others listed).

### 7.5 Payment and filing deadlines

TDS paid by the payer (Income-tax Rules, 2026, rule 218): within thirty days from the end of the month in which the deduction is made, with a challan-cum-statement in Form No. 141. Form No. 141 has a Schedule D for TDS paid by an individual or HUF on the transfer of a VDA. Where an exchange pays the tax instead of the buyer under guidelines issued under section 400(2), the exchange files a quarterly statement in Form No. 142 (rule 219(2)). Source: https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf

Advance tax (sections 404 and 408 of the 2025 Act). VDA income counts towards advance tax like any other income.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Advance tax is payable when the year's tax is | INR 10,000 | "is ₹10000 or more" |
| By 15 June 2026, at least | 15% | "1. On or before Not less than 15% of such advance tax. the 15th June." |
| By 15 September 2026, at least (cumulative) | 45% | "2. On or Not less than 45% of such advance tax" |
| By 15 December 2026, at least (cumulative) | 75% | "3. On or Not less than 75% of such advance tax" |
| By 15 March 2027 | The whole amount | "4. On or before The whole amount of such advance tax, as the 15th March." |
| Interest for default (section 424), per month or part, from 1 April after the tax year | 1% | "simple interest at the rate of 1% for every month or part of a month, for the period, beginning from the 1st April following such tax year" |
| Default applies where advance tax paid is less than this share of assessed tax | 90% | "is less than 90% of the assessed tax" |
| Interest for deferment (section 425), June, September and December shortfalls | 3% | "15% of the tax Shortfall till 15th day of 3% of June." |
| Interest for deferment, March shortfall | 1% | "100% of the Shortfall till 15th day of 1% of March." |

Section 403(3) exempts a resident aged sixty or more with no business or profession income from advance tax. A gain on a single large sale late in the year still needs the remaining instalments; check section 425 for how a shortfall is measured. Section 425(4) charges no interest under section 425(1) or (3) on a shortfall caused by "underestimation of, or failure to estimate" "capital gains", where the assessee "has paid in full, the tax payable on the said income" "in any of the remaining instalments of advance tax, if any, or by the 31st day of March of the tax year". Whether this covers a VDA gain is not settled: refer.

Return due dates (section 263(1)(c) of the 2025 Act as substituted by the Finance Act, 2026). For tax year 2026-27 these dates fall in 2027.

| Taxpayer | Due date | Note |
| --- | --- | --- |
| Source | all dates below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| No business or profession income (most investors) | 31 July | "4. Any other assessee. 31st July." |
| Business or profession income, accounts not required to be audited (for example a trader not under audit) | 31 August | "3. (i) Assessee having income Where the 31st August." |
| Company, or a person whose accounts must be audited (no transfer pricing report) | 31 October | "2. (i) Company; Where the 31st October." |
| Revised return | Within twelve months from the end of the tax year, or before assessment is completed, whichever is earlier | "furnish a revised return at any time within twelve months from the end of the relevant tax year" |

A return not filed by the due date may be filed "within nine months from the end of the relevant tax year, or before the completion of the assessment, whichever is earlier" (section 263(4) of the 2025 Act), with a fee under section 428. An updated return may be filed within forty-eight months from the end of the financial year after the tax year (section 263(6)(a)), subject to the conditions there. Source: https://egazette.gov.in/WriteReadData/2025/265620.pdf

## Section 8: Loss Offset and Carry Forward

| Rule | Detail | Authority |
| --- | --- | --- |
| VDA loss against other income | Not allowed | Section 194 Table serial 4, column E(b) |
| VDA loss against a gain on another VDA | Not allowed. Column E(a) bars "set off of any loss" in computing the VDA income, and E(b) bars setting off a VDA loss against income computed under any provision | Section 194 Table serial 4, column E(a) and (b) |
| Carry forward of a VDA loss | Not allowed | Column E(b) |
| Loss from any other head against VDA income | Not allowed | Column E(a) |
| Expenses against VDA income | Not allowed, except cost of acquisition | Column E(a) |

Source for this table: https://egazette.gov.in/WriteReadData/2025/265620.pdf

So each profitable transfer is taxed on its own. A loss on one coin does nothing for a gain on another coin in the same year, or in any later year.

### Example of the no-offset rule (hypothetical amounts, in rupees)

~~~
BTC: bought for 1,000,000, sold for 500,000   -> loss 500,000 (cannot be used)
ETH: bought for 300,000,  sold for 800,000    -> gain 500,000

Tax on VDA income = 30% x 500,000 = 150,000
Cess (no surcharge assumed) = 4% x 150,000 = 6,000
Total = 156,000. The BTC loss is lost for good.
~~~

## Section 9: Anti-Avoidance Rules

### 9.1 No wash-sale rule needed

The 2025 Act has no wash-sale rule for VDAs. Selling at a loss gives no tax benefit anyway, because a VDA loss cannot be set off or carried forward (Section 8).

### 9.2 Provisions that reach VDAs

| Provision | Effect |
| --- | --- |
| General Anti-Avoidance Rule, Chapter XI of the 2025 Act (section 178 onwards) | An arrangement may be declared an impermissible avoidance arrangement and its tax consequence determined under that Chapter |
| Section 92(2)(m) | VDA received free or cheaply from non-relatives above the threshold in Section 7.4 is income |
| Section 104 (unexplained asset) | "asset" includes a VDA. An unrecorded VDA with no satisfactory explanation of its source is deemed income of the year it is found |
| Section 195 | Income deemed under sections 102 to 106 is taxed at the rate in the table below, with no deduction and no loss set-off |
| Search, seizure and block assessment (sections 261, 295 and 301) | The definitions of "asset" and "undisclosed income" used there include VDAs |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate on income deemed under sections 102 to 106, including an unexplained VDA (section 195(1)) | 60% | "at the rate of 60%" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge on tax under section 195(1)(i), any assessee, tax year 2026-27 | 25% | "8. 195(1)(i). Any assessee. 25%." |

### 9.3 TDS as a tracking tool

TDS under section 393(1) Table serial 8(vi) records each VDA sale against the seller's PAN. Crypto-asset service providers also report transactions under section 509 of the 2025 Act, and the Finance Act, 2026 substituted section 446 to penalise a provider that fails to report or reports wrongly. Expect the department to hold transaction data before the return is filed.

## Section 10: Worked Examples

All amounts in these examples are hypothetical and in rupees. Rates are the ones in the Section 3 tables.

### Example 1: simple BTC sale, new regime

Resident individual, new regime. Bought 1 BTC for 2,000,000 in May 2026. Sold it for 5,000,000 in September 2026 on an Indian exchange. Exchange fee on sale: 5,000 (not deductible). Other income: salary taxed at slab rates, total income below the first surcharge threshold.

~~~
Consideration                 5,000,000
Cost of acquisition          -2,000,000
Income from VDA transfer      3,000,000

Tax at 30% x 3,000,000          900,000
Cess at 4% x 900,000             36,000
Tax on the VDA income           936,000

TDS deducted at 1% x 5,000,000   50,000  (credit against the year's tax)
The 5,000 fee is not deducted.
~~~

The salary is taxed separately at the section 202 slab rates. The rebate under section 156(2) cannot reduce the 900,000.

### Example 2: two coins and a staking reward

Resident individual in tax year 2026-27. Sold SOL: cost 200,000, proceeds 500,000, gain 300,000. Sold DOGE: cost 400,000, proceeds 100,000, loss 300,000. Received staking rewards worth 25,000 at receipt.

~~~
SOL gain                        300,000 -> tax 30% x 300,000 = 90,000
DOGE loss                       cannot reduce the SOL gain
Cess at 4% x 90,000             3,600
Tax on VDA income               93,600

Staking reward 25,000           treatment not settled by the Act: refer
~~~

### Example 3: a VDA gift from a friend

A receives 0.5 BTC from a friend (not a relative) with a fair market value of 1,500,000 at receipt. A receives no other gifts in the year. A later sells the BTC for 2,000,000.

~~~
Gift: aggregate value 1,500,000 is above the section 92(2)(m) threshold
      -> whole 1,500,000 is income from other sources, taxed at slab rates

Later sale: proceeds 2,000,000, section 194 transfer
      cost of acquisition: not settled for a VDA (see below)
~~~

Section 73 Table serial 17 of the 2025 Act makes the value taxed under section 92(2)(m) the cost of a "capital asset" when "the capital gain arises" on its transfer. A VDA held as an investment is a capital asset (section 2(22)), and section 194 only sets the rate on income from its transfer; but section 194 allows only "cost of acquisition, if any", and no page links that phrase to section 73. Whether the cost on the sale is 1,500,000 or nil is a question for an accountant. Refer before filing. Using nil overstates the gain by 1,500,000; using 1,500,000 without support risks an addition.

## The method, step by step

1. Confirm the tax year. For transfers from 1 April 2026 to 31 March 2027 use the 2025 Act; for earlier transfers use the 1961 Act and not this Guide. Income-tax Act, 2025, section 1(3): https://egazette.gov.in/WriteReadData/2025/265620.pdf
2. Confirm each asset is a VDA under section 2(111) of the 2025 Act, including clause (d) for crypto-assets on a distributed ledger, and check for any exclusion notification. https://egazette.gov.in/WriteReadData/2025/265620.pdf
3. List every transfer in the year (sales, swaps, payments in VDA) under the section 2(109) meaning of transfer applied by section 194(2)(n). Separate receipts (mining, staking, airdrops, gifts) for Section 5 and Section 7.4. https://egazette.gov.in/WriteReadData/2025/265620.pdf
4. For each transfer, compute consideration less cost of acquisition only, under section 194(1) Table serial 4. Ignore any losses and fees. Add up only the gains. https://egazette.gov.in/WriteReadData/2025/265620.pdf
5. Tax the total VDA gains at the section 194 rate, then add surcharge for the person's regime and total income and cess under section 3 of the Finance Act, 2026. https://egazette.gov.in/WriteReadData/2026/271439.pdf
6. Tax the rest of the income at the normal rates (section 194(1)(b)); do not let the new-regime rebate reduce VDA tax (section 156(3)). https://egazette.gov.in/WriteReadData/2025/265620.pdf
7. Test gifts and free receipts against section 92(2)(m) and the relative and other exclusions in section 92(3). https://egazette.gov.in/WriteReadData/2025/265620.pdf
8. Collect the TDS deducted under section 393(1) Table serial 8(vi) and check it against the exchange statements; credit it under section 390(5). If the client bought VDAs from other people (peer to peer), check whether the client had to deduct TDS, pay it within thirty days of the month end with Form No. 141 (rule 218), and whether the section 393(4) serial 12 limits applied. https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
9. Check advance tax paid against sections 404 and 408, and compute interest under sections 424 and 425 if short. https://egazette.gov.in/WriteReadData/2025/265620.pdf
10. File the return in the form rule 164 requires (ITR-2 or ITR-3 for individuals and HUFs, never ITR-1 or ITR-4) by the section 263(1)(c) due date. https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf and https://egazette.gov.in/WriteReadData/2026/271439.pdf

## Ask the client first

- When did each transfer happen: before 1 April 2026 (1961 Act) or from 1 April 2026 (2025 Act)?
- Are you staying in the new tax regime, or have you opted out? This changes the surcharge table and the rebate.
- Do you have business or profession income (including trading as a business), and are your accounts audited? This changes the return form and the due date.
- Did you receive any VDA for free or below value (gifts, airdrops, rewards), and from whom: a relative, or someone else?
- Did you buy any VDA directly from another person rather than through an exchange? You may have had to deduct and pay TDS.
- Are you resident in India for the tax year, and did you trade on a foreign exchange or pay tax on VDAs abroad? See `in-tax-residency`.

## When to refuse or refer

Refer to an accountant when:

- Income from mining, staking, lending, yield, liquidity pools, a paid airdrop, or an NFT royalty needs a head of income: the Act does not settle it.
- The cost of a gifted or free VDA on a later sale matters (Example 3), or a fork or airdrop needs a cost.
- The client gave a VDA away, or moved VDAs between wallets and the department may see the move as a transfer.
- The seller is a non-resident, or the client is a non-resident or not ordinarily resident.
- The client is a company, a firm or a trust, or VDAs are held as stock-in-trade of a business.
- There are cross-border transactions between related parties (see `india-transfer-pricing`).
- There is a notice about an unexplained asset under section 104, a search, or a block assessment.
- The client's question is about income earned before 1 April 2026.

Refuse to:

- Set a VDA loss against any income, or carry it forward.
- Deduct fees, gas, commissions or any expense other than cost of acquisition.
- Apply a capital gains exemption or a holding-period rate to VDA income.
- Present any crypto computation as final without an accountant's review.

For the general income-tax computation (slabs, regimes, rebate) see `in-income-tax`. For instalments see `in-advance-tax`.

## Self-Checks

- [ ] Every transfer from 1 April 2026 taxed at the section 194 rate, with surcharge for the right regime and cess on tax plus surcharge?
- [ ] No VDA loss used anywhere, in the year or later?
- [ ] Only cost of acquisition deducted?
- [ ] New-regime rebate kept away from the VDA tax?
- [ ] TDS deducted by exchanges matched and credited; TDS owed on peer-to-peer purchases checked?
- [ ] Gifts and free receipts tested on the aggregate for the year, with relatives excluded?
- [ ] Advance tax instalments checked, including for a large sale late in the year?
- [ ] Return form ITR-2 or ITR-3 (not ITR-1 or ITR-4) and the right due date?
- [ ] Every unsettled classification (Section 5) referred, not guessed?

## Prohibitions

- Never set off a VDA loss against any income, including a gain on another VDA. Section 194 Table serial 4, column E.
- Never deduct exchange fees, gas fees or any cost other than cost of acquisition.
- Never apply a holding-period distinction or a capital gains exemption to VDA income.
- Never carry a VDA loss forward.
- Never apply the section 194 rate to a mining, staking or airdrop receipt as if the Act settled it.
- Never use the 1961 Act section numbers for tax year 2026-27.
- Never ignore TDS on a VDA purchase from another person.
- Never present a crypto tax position as definitive; label it as an estimate for professional review.

## Sources

- Income-tax Act, 2025 (30 of 2025), Gazette of India, 21 August 2025: https://egazette.gov.in/WriteReadData/2025/265620.pdf
- Finance Act, 2026 (4 of 2026), Gazette of India, 30 March 2026: https://egazette.gov.in/WriteReadData/2026/271439.pdf
- Income-tax Rules, 2026, notified 20 March 2026: https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained on the OpenAccountants site. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
