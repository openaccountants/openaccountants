---
name: india-crypto-tax
description: Use this skill whenever asked about India cryptocurrency or virtual digital asset (VDA) taxation. Trigger on phrases like "crypto tax India", "Bitcoin India tax", "VDA tax", "Section 115BBH", "194S TDS crypto", "crypto TDS India", "virtual digital asset India", "crypto income India", "NFT tax India", "mining tax India", "staking tax India", "WazirX tax", "CoinDCX tax", "crypto loss India", "Schedule VDA", "ITR crypto", "30% crypto tax India", "1% TDS crypto", or any question about the income tax, TDS, or reporting treatment of cryptocurrency, tokens, NFTs, or virtual digital assets under Indian tax law. Covers Finance Act 2022 amendments (Sections 115BBH, 194S, 2(47A)), the no-loss-offset rule, ITR Schedule VDA, and advance tax obligations. ALWAYS read this skill before touching any India crypto work.
version: 1.1
jurisdiction: IN
tax_year: 2026
last_updated: 2026-11-15
depends_on:
  - india-income-tax
category: crypto
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: crypto
type: computation
---

# India Crypto and Virtual Digital Asset Tax

## Scope

This skill covers Indian income tax and tax deducted at source (TDS) on crypto, tokens, NFTs and other virtual digital assets (VDAs) for individuals, Hindu undivided families (HUFs) and companies. Figures are for tax year 2026. This means the tax year from 1 April 2026 to 31 March 2027 under the Income-tax Act, 2025, which replaced the Income-tax Act, 1961 from 1 April 2026. Section numbers changed with the new Act: the 1961 Act sections that older material quotes for crypto do not apply to tax year 2026-27, and this skill names only the 2025 Act sections. Income earned up to 31 March 2026 (assessment year 2026-27) is still taxed and returned under the 1961 Act; this skill does not cover it.



Current Tax Year 2026-27 primary provisions are confirmed below. Entity provisions remain for routing/preservation, but companies/firms/trusts, RNOR/nonresidents and stock-in-trade portfolios require the existing professional referral; the worked computations assume ordinarily resident individuals. Income recognition and earlier TDScredit/payment event are distinct: a March 2026 credit/Aprilcashpayment stays in the old TDSperiod, even while a separate later transfer may be current. [ss.1,3,393,536](https://egazette.gov.in/WriteReadData/2025/265620.pdf).

### Section 1: Quick reference

| Field | Value; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| Country | India; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Tax | Income-tax on income from the transfer of a virtual digital asset, and TDS on the price paid for one; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Currency | INR; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Tax year | 1 April to 31 March. Tax year 2026-27 runs from 1 April 2026 to 31 March 2027; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Primary law | Income-tax Act, 2025 (30 of 2025): section 2(111) (definition), section 194(1) Table serial 4 (rate and loss rule), section 393(1) Table serial 8(vi) and section 393(4) Table serial 12 (TDS); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rates law for the year | Finance Act, 2026 (4 of 2026), section 3 (surcharge and cess for tax year 2026-27); https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Procedure | Income-tax Rules, 2026: rule 218 (paying TDS, Form No. 141), rule 219 (exchange statements, Form No. 142), rule 164 (which return form); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Tax authority | Income Tax Department, Central Board of Direct Taxes; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate, TDS and thresholds | In the tables in Sections 3 and 7; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

### VDA definition (section 2(111) of the 2025 Act)

| Clause | What it covers; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| (a) | Any information, code, number or token, not being Indian currency or foreign currency, generated through cryptographic means or otherwise, that gives a digital representation of value, exchanged with or without consideration, with the promise or representation of having inherent value, or that functions as a store of value or a unit of account, and can be transferred, stored or traded electronically; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| (b) | A non-fungible token or any other token of similar nature, by whatever name called; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| (c) | Any other digital asset the Central Government notifies; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| (d) | Any crypto-asset that relies on a cryptographically secured distributed ledger or similar technology, whether or not it falls in (a), (b) or (c). This clause is new in the 2025 Act text; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Exclusions | Indian currency and foreign currency are outside clause (a). The Central Government may exclude any digital asset by notification; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

The definition is in the Act at https://egazette.gov.in/WriteReadData/2025/265620.pdf and the Act text prints "(not being Indian currency or foreign currency)" and "the Central Government may, by notification, exclude any digital asset from this definition". It does not itself name the Digital Rupee: check for an exclusion notification before treating any central bank digital currency as outside the regime.

### Conservative defaults

| Ambiguity | Default; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| Unknown cost of acquisition | Do not finalize an unknown cost as nil. A nil-cost conservative estimate may show maximum exposure, clearly labelled; retrieve acquisition proof, then refer unresolved material cost; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Unknown whether a trader or an investor | The section 194 rate applies to any income from the transfer of a VDA either way. Classify the head of income separately and refer if it matters; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Unknown how a receipt from mining, staking or an airdrop is taxed | Do not apply the section 194 rate to the receipt itself. Refer (Section 5); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Unknown fair market value at receipt | Collect a documented contemporaneous exchange price as valuation evidence; it is not automatically the prescribed statutory fair market value. Apply s.92(5)(c)/valuation rules or refer before finalizing; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| VDA received free from a non-relative | Test the aggregate fair market value against the section 92(2)(m) threshold in Section 7.4; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

## Ask the client first

- When did each transfer happen: before 1 April 2026 (1961 Act) or from 1 April 2026 (2025 Act)?
- Are you staying in the new tax regime, or have you opted out? This changes the surcharge table and the rebate.
- Do you have business or profession income (including trading as a business), and are your accounts audited? This changes the return form and the due date.
- Did you receive any VDA for free or below value (gifts, airdrops, rewards), and from whom: a relative, or someone else?
- Did you buy any VDA directly from another person rather than through an exchange? You may have had to deduct and pay TDS.
- Are you resident in India for the tax year, and did you trade on a foreign exchange or pay tax on VDAs abroad? See `in-tax-residency`.
- Acquisition invoices, all wallet/exchange transfers, cash/crypto consideration, purchase versus sale fees, matching method, statutory valuation evidence, each payer's prior-year category and cumulative purchases, actual deduction/deposit/certificate and credit-assessability year? Missing evidence is a hold, not permission to assume zero cost.

## The method, step by step

1. Confirm the tax year. For transfers from 1 April 2026 to 31 March 2027 use the 2025 Act; separately fix earliercredit/payment TDSdate; for earlier transfers use the 1961 Act and not this Guide. Income-tax Act, 2025, section 1(3): https://egazette.gov.in/WriteReadData/2025/265620.pdf
2. Confirm each asset is a VDA under section 2(111) of the 2025 Act, including clause (d) for crypto-assets on a distributed ledger, and check for any exclusion notification. https://egazette.gov.in/WriteReadData/2025/265620.pdf
3. List every transfer in the year (sales, swaps, payments in VDA) under the section 2(109) meaning of transfer applied by section 194(2)(n). Separate receipts (mining, staking, airdrops, gifts) for Section 5 and Section 7.4. https://egazette.gov.in/WriteReadData/2025/265620.pdf
4. For each transfer, compute consideration less cost of acquisition only, under section 194(1) Table serial 4. Do not offset losses against gains. Sale fees/other expenses are disallowed; purchase-fee allocation and uncertain acquisition cost remain held rather than silently set to zero. Add supported positive transfer incomes only. https://egazette.gov.in/WriteReadData/2025/265620.pdf
5. Tax the total VDA gains at the section 194 rate, then add surcharge for the person's regime and total income and cess under section 3 of the Finance Act, 2026. https://egazette.gov.in/WriteReadData/2026/271439.pdf
6. Tax the rest of the income at the normal rates (section 194(1)(b)); do not let the new-regime rebate reduce VDA tax (section 156(3)). https://egazette.gov.in/WriteReadData/2025/265620.pdf
7. Test gifts and free receipts against section 92(2)(m) and the relative and other exclusions in section 92(3). https://egazette.gov.in/WriteReadData/2025/265620.pdf
8. Collect the TDS deducted under section 393(1) Table serial 8(vi) and check it against the exchange statements; credit it under section 390(5). If the client bought VDAs from other people (peer to peer), check whether the client had to deduct TDS, apply rule 218(3)/219(5)30 day month-end Form 141 rule and verify the actual Form 141 Schedule D/individual-HUF caption against payer category before final filing, and whether the section 393(4) serial 12 limits applied. https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf
9. Check advance tax paid against sections 404 and 408, and review current 424/425 interest if short; ordinary 425(2)/(3)construction remains held in in-advance-tax, so do not finalize that amount from the conditional table below. https://egazette.gov.in/WriteReadData/2025/265620.pdf
10. File the return in the form rule 164 requires (ITR-2 or ITR-3 for individuals and HUFs, never ITR-1 or ITR-4) by the section 263(1)(c) due date. https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf and https://egazette.gov.in/WriteReadData/2026/271439.pdf

### Section 2: Classification Rules

#### One rate for every transfer, no capital versus income split

Section 194(1) of the 2025 Act, Table serial 4, taxes any income from the transfer of any virtual digital asset, for any person, at the rate in the Section 3 table. The rule does not depend on how long the asset was held, how often the person trades, or whether the gain is capital or revenue. The section works in two parts: tax on the VDA income at the section 194 rate, plus the tax the person would pay if total income were reduced by that VDA income (section 194(1)(a) and (b)). So the VDA income is taxed at the flat rate from the first rupee, and the slab rates and the nil band apply only to the rest of the income.

| Question | Answer under the 2025 Act; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| Does holding period matter? | No. Section 194 Table serial 4 has one rate for any person and any VDA transfer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Does trader versus investor matter? | Not for the rate. It can matter for the return form (Section 7.1) and the due date (Section 7.5); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Is a VDA a capital asset? | Section 194(2)(n) applies the section 2(109) meaning of "transfer" to any VDA "whether capital asset or not", so the rate applies either way; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Does the new-regime rebate cut the tax on VDA income? | No. Section 156(3) caps the section 156(2) rebate at the tax payable at the section 202(1) rates, and VDA income is taxed at the section 194 rate instead; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

Source for this table: https://egazette.gov.in/WriteReadData/2025/265620.pdf

#### What counts as a transfer

Section 2(109) of the 2025 Act says a transfer includes "(a) the sale, exchange or relinquishment of the asset", the extinguishment of any rights in it, and the other events listed there. Section 194(2)(n) applies that meaning to every VDA. So:

- Selling a VDA for rupees or foreign currency is a sale.
- Swapping one VDA for another is an exchange, which is a transfer of the VDA given up.
- Paying for goods or services with a VDA is an exchange of the VDA.
- Giving a VDA away, and moving a VDA between two wallets the same person owns, are not named in section 2(109). Do not treat either as settled: see Section 9 and the refer list.

### Section 3: Rate Table

#### Tax on income from the transfer of a VDA (section 194(1), Table serial 4)

| Item | Value | Note; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate on income from the transfer of any VDA, any person | 30% | "30%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Deductions allowed | Cost of acquisition only | "expenditure (other than cost of acquisition, if any) or allowance or set off of any loss"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Loss on a VDA transfer | Not set off against any income and not carried forward | "no set off of loss from transfer of the virtual digital asset computed herein shall be allowed against income computed under any provision of this Act to the assessee and such loss shall not be allowed to be carried forward to succeeding tax years"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

#### Surcharge and cess, tax year 2026-27 (Finance Act, 2026, section 3)

Cess is charged on income-tax plus surcharge. Surcharge depends on total income, including the VDA income. Serial 1, which lists tax under section 194, applies only to a person "not having any income chargeable to tax under section 202", that is, a person who has left the new regime. Serial 10 lists only section 202. The original reading was that serial 10 covers a new-regime person's whole tax, because section 202(1) makes the new-regime computation "subject to Parts A, B, E" of the Chapter; the Finance Act does not say so in terms. The precise s.194/new-regime surcharge interaction is **Not yet confirmed** here: neither 25% cap nor a band labelled both regimes is a final VDA filing instruction until that interpretation is resolved. The underlying Finance Acttable figures are retained, not silently deleted.

| Item | Value | Note; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Health and Education Cess, on income-tax plus surcharge | 4% | "calculated at the rate of 4% of such income-tax and surcharge"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge starts where total income exceeds | INR 5,000,000 | "exceeds ₹ 5000000 but does"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge rate, total income above INR 5,000,000 up to INR 10,000,000 (underlying bands; new-regime VDA interaction held) | 10% | "rate of 10%;"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Next threshold | INR 10,000,000 | "exceeds ₹ 10000000 but does not exceed ₹ 20000000, at the"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge rate, above INR 10,000,000 up to INR 20,000,000 (underlying bands; new-regime VDA interaction held) | 15% | "rate of 15%;"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Next threshold | INR 20,000,000 | "at the rate of 25%;"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| New regime (serial 10): top surcharge rate, above INR 20,000,000 | 25% | "at the rate of 25%;"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime (serial 1): rate above INR 20,000,000 up to INR 50,000,000 | 25% | "rate of 25%;"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime (serial 1): top threshold | INR 50,000,000 | "(iv) where the total income exceeds ₹ 50000000"; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Old regime (serial 1): top surcharge rate | 37% | "rate of 37%."; https://egazette.gov.in/WriteReadData/2026/271439.pdf |

Companies, firms and co-operative societies use other serials of the same Table (for example serials 6, 7 and 9 for companies). Refer.

Marginal relief applies where income only just crosses a surcharge threshold. The formula is in section 3(5) of the Finance Act, 2026 and the First Schedule Part I-B; apply it from the Act, not from a rule of thumb.

Do not quote a single effective rate for VDA income. The rate in the first table, the surcharge band and the cess combine differently for each client; compute each case.

### Section 4: Cost Basis

#### What may be deducted

| Item | Allowed? | Basis; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- | --- |
| Cost of acquisition | Yes | Section 194 Table serial 4, column E(a): "other than cost of acquisition, if any"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Cost of improvement | No | Column E(a) allows no expenditure other than cost of acquisition; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Exchange fees, gas fees, commissions on sale | No | Same: no other expenditure or allowance; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Any loss, from a VDA or any other source | No | Column E(a) and (b); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Depreciation | No | No allowance is permitted; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

Source for this table: https://egazette.gov.in/WriteReadData/2025/265620.pdf

Whether a purchase fee forms part of the "cost of acquisition" is not yet confirmed here from the cited section 194 provisions. Treat it as not deductible unless an accountant decides otherwise.

#### Cost basis methods

The cited section 194 Table serial 4 says "cost of acquisition, if any"; that table does not prescribe the matching of sales to purchases. The original alternatives remain first in, first out and specific identification with records, but that cited table does not authorize a free choice. Document each acquisition/disposal and proposed matching consistently; obtain confirmation of the applicable method before any final computation, not only for large portfolios.

#### Nil-cost cases

Where nothing was paid for a VDA (mining, staking rewards, airdrops, tokens from a fork), there may be no cost of acquisition: the Act's words are "if any". If the receipt was taxed as income when received, an accountant decides whether that taxed value can be the cost on a later sale; that VDA basis is not yet confirmed here from the cited provisions (see Section 5 and Section 7.4).

### Section 5: De Fi, Staking, Mining and Airdrops

The cited provisions do not by themselves settle every mining, staking, lending, liquidity-pool or airdrop receipt. Preserve these as classification/referral topics, without claiming a full-Act search proves the absence of any other applicable rule. Two rules confirmed here are:

1. A later sale, swap or other transfer of the tokens is a VDA transfer taxed under section 194 (Sections 2 and 3).
2. A VDA received without consideration, or for less than its fair market value, is "property" for section 92(2)(m) when the recipient holds it as a capital asset, so the gift rule in Section 7.4 can apply to it.

Everything else below is a classification question for an accountant. Do not state it as law.

#### 5.1 Mining

| Point | Status; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| Tax on the tokens when mined | Not yet confirmed here from the cited provisions. It may be business income or income from other sources at slab rates. Refer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Cost of mined tokens on a later sale | "cost of acquisition, if any": possibly nil. Refer if the receipt was taxed; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Later sale or swap | Section 194 transfer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

#### 5.2 Staking

| Point | Status; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| Tax on rewards when received | Not yet confirmed here from the cited provisions. Refer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Later sale or swap of reward tokens | Section 194 transfer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

#### 5.3 Airdrops

| Point | Status; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| Airdrop received for nothing from a non-relative | Section 92(2)(m) can tax it if the aggregate value of such property received in the year passes the threshold in Section 7.4; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Airdrop received for doing something (a task, a service) | Not yet confirmed here from the cited provisions. Refer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Later sale of airdropped tokens | Section 194 transfer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

#### 5.4 De Fi lending, yield and liquidity pools

| Activity | Status; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| Interest or yield paid in tokens | Not yet confirmed here from the cited provisions. Refer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Depositing tokens into a pool for LP tokens | Likely an exchange of one VDA for another, so a section 194 transfer. Confirm the facts; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Withdrawing from the pool | Same; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Impermanent loss | If a loss is realized on a VDA transfer, section 194 bars set-off and carry forward (Section 8); a valuation/impermanent loss alone does not establish a transfer or a deduction; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

#### 5.5 Forks

| Point | Status; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| New tokens from a fork | No price was paid. Cost "if any": refer before using nil; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Sale of forked tokens | Section 194 transfer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Original tokens | No unsupported cost reallocation is made; original-token cost treatment on a fork remains held with the fork allocation question; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

### Section 6: NFT Treatment

An NFT is a VDA under section 2(111)(b). Clause (i) of the section says "non-fungible token" means "such digital asset as the Central Government may, by notification, specify". Check whether a notification covers the token before relying on clause (b) alone; clause (d) may still catch it if it runs on a distributed ledger.

| Event | Treatment; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| Buying an NFT for rupees | Acquisition. Record the cost; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Selling an NFT | Section 194 transfer, taxed at the Section 3 rate on proceeds less cost; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Swapping NFT for NFT, or NFT for a token | Exchange: a section 194 transfer of what is given up; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| An artist minting and selling their own NFT | Section 194 transfer of the NFT. Whether the creator also has business income is not settled. Refer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Royalty on a resale paid to the creator | Not yet confirmed here from the cited provisions. Refer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| NFT received free from a non-relative | Section 92(2)(m) gift rule (Section 7.4); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| NFT becomes worthless | A loss from an actual VDA transfer is not set off or carried forward; other impairment/disposal treatment is not yet confirmed here, so refer; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

### Section 7: Reporting Requirements

#### 7.1 Which return form (rule 164, Income-tax Rules, 2026)

Rule 164 covers returns for the tax year starting 1 April 2026. A person with income taxed under Part A of Chapter XIII of the 2025 Act (which includes section 194) cannot use ITR-1 (rule 164(3)(n)) or ITR-4 (rule 164(6)(o)).

| Taxpayer | Form; https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| --- | --- |
| Individual or HUF with VDA income and no business or profession income | ITR-2 (rule 164(4)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Individual or HUF with business or profession income | ITR-3 (rule 164(7)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |
| Company (other than one filing ITR-7) | ITR-6 (rule 164(9)); https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf |

Source: https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf

The return forms for tax year 2026-27 are filed in 2027. Check the VDA schedule in the form when it is released; the schedule layout is not on a page this Guide could read.

#### 7.2 What to record for each VDA transfer

Keep, for every transfer: the type of VDA, the date acquired, the date transferred, the cost of acquisition in rupees, the consideration received in rupees, and the TDS deducted. These are the facts the section 194 computation needs. Keep the exchange statements and wallet records that prove them.

#### 7.3 TDS on the transfer of a VDA (section 393)

Section 393(1) Table serial 8(vi) applies to "Any person" paying a resident consideration for the transfer of a VDA. Tax is deducted at the time of credit or payment, whichever is earlier. Section 393(4) Table serial 12 switches TDS off where the year's consideration from that payer stays within the limits below.

| Item | Value | Note; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| TDS rate on consideration for the transfer of a VDA | 1% | "Rate: 1%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| No TDS if the year's consideration does not exceed, for a payer who is an individual or HUF with business turnover up to INR10,000,000 (in words on the page) or professional receipts up to INR5,000,000 (in words on the page) in the preceding tax year, or with no business or profession income | INR 50,000 | "(a) ₹ 50000, when payable by an individual"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| No TDS if the year's consideration does not exceed, for any other payer | INR 10,000 | "(b) ₹ 10000, when payable by any person other than the person referred to in clause (a)"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Higher TDS where the seller gives no valid PAN | Highest of provision rate, rates in force, and 20% floor (not a universal fixed 20%) | "at the rate of 5% where tax is required to be deducted under section 393(1) [Table: Sl. No. 8(ii) or 8(v)]; or 20% in any other case"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

Points the Act settles:

- The limits are on consideration "during the tax year", and the turnover test looks at "the tax year immediately preceding the tax year in which such virtual digital asset is transferred". Above the limit, tax is deducted on the entire amount (section 393(1)(a)).
- Where the price is paid wholly in kind, or in another VDA with no cash, or the cash part is too small to cover the tax, the payer "shall ensure that the tax required to be deducted has been paid, before releasing such consideration" (Note 6 to the section 393(1) Table). In a VDA-for-VDA swap, settle on the facts who is the payer on each leg; Note 6 then applies to that payer.
- A payer satisfying the specific section 393(4)Table 12 C(a)category has the section 397(1)(c)TANexception, subject to the actual period and transaction wording; this is not a waiver for every VDA buyer. The Finance Act, 2026 substitutes clause (c) with effect from 1 October 2026; the VDA exemption is kept.
- TDS counts as payment on behalf of the seller under 390(5), but the credit year/proportion and return evidence follow rule 203 assessability controls; it is not automatically all credited in the cash-payment year. Match statement/certificate/PAN; preserve 401 protection where tax actually deducted, without fabricating credit.
- Section 393(1) covers payments to residents. For a non-resident seller, refer.

#### 7.4 Gifts and free receipts of a VDA (section 92(2)(m))

| Item | Value | Note; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Property received without consideration: taxable as income from other sources where the aggregate fair market value in the tax year exceeds | INR 50,000 | "(A) without consideration, the aggregate fair market value of which exceeds ₹ 50000, the whole of the aggregate fair market value of such property"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Property received for less than fair market value: taxable where the shortfall exceeds | INR 50,000 | "(B) for a consideration which is less than the aggregate fair market value of the property by an amount exceeding ₹ 50000"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

- "Property" means a "capital asset of the assessee" in the section 92(5)(f) list, which ends "(x) virtual digital asset;". A VDA the recipient holds as stock-in-trade of a business is not "property" for this rule: refer.
- For free property, once aggregate fair market value exceeds 50,000, the WHOLE aggregate value is included; at or below, no inclusion under this limb. For property bought below value, test whether the aggregate FMV-minus-consideration shortfall exceeds 50,000; if so, include that whole SHORTFALL, not the entire property value. Both require capital-asset property and all s.92(3)exceptions, not every token receipt.
- The test is the aggregate for the year, from "any person or persons", not each gift separately.
- Section 92(3) excludes receipts "(a) from any relative; or (b) on the occasion of marriage of the individual; or (c) under a will or by way of inheritance", plus contemplation of donor death; specified local authority; qualifying registered nonprofit receipts subject related-person exception; the specifically listed s.70 transactions; a trust from an individual solely for that individual's relatives; prescribed persons/conditions. Do not assume every trust or nonprofit qualifies. "Relative" is defined in section 92(5)(g) (spouse, siblings, siblings of the spouse or parents, lineal ascendants and descendants, and others listed).

#### 7.5 Payment and filing deadlines

TDS paid by the payer under the literal rule 218(3)(d)/219(5)(d) enumeration of 8(vi): within30days (in words on the page) from the end of the month in which the deduction is made, with a challan-cum-statement in Form No. 141. Form No. 141 has a Schedule D for TDS paid by an individual or HUF on the transfer of a VDA. Rule 219(2)Form 142 applies only where the exchange agreed under 400(2)guidelines to pay tax on a transfer of a VDA OWNED BY IT as the buyer's deduction alternative; do not infer every exchange trade is 142. Form 141 Schedule Dcaption identifies individual/HUF payments while rule 218(3)/219(5)text enumerates 8(vi)without that qualifier: actual nonindividual utility/form treatment is held for clarification, not invented. Rule 215 requires Form 132 for 8(vi), within 15 days of Form 141 due date; certificate must be generated/downloaded from the specified portal. Confirm applicable modes/fields before filing. Source: https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf

Advance tax (sections 404 and 408 of the 2025 Act). VDA income enters the advance-tax computation. The table below is the ordinary schedule. If the assessee also declares profits under section 58(2) Table serial 1 or 3, section 408(2) applies to that assessee; obtain professional review of the mixed VDA/presumptive-income schedule before finalizing. Do not invent a split by income component.

| Item | Value | Note; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Advance tax payable under section 404 when the amount computed under section 405, including its conditional TDS/TCS reduction, is at least (not gross VDA tax) | INR 10,000 | "is ₹10000 or more"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| By 15 June 2026, at least | 15% | "Not less than 15% of such advance tax."; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| By 15 September 2026, at least (cumulative) | 45% | "Not less than 45% of such advance tax"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| By 15 December 2026, at least (cumulative) | 75% | "Not less than 75% of such advance tax"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| By 15 March 2027 | The whole amount | "The whole amount of such advance tax"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Interest for default (section 424), per month or part, from 1 April after the tax year | 1% | "simple interest at the rate of 1% for every month or part of a month, for the period, beginning from the 1st April following such tax year"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Default applies where advance tax paid is less than this share of assessed tax | 90% | "is less than 90% of the assessed tax"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Conditional table transcription, section 425 June/September/December; ordinary 425(2)/(3)construction held | 3% (not a finalized charge) | "3%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Conditional March table transcription, same construction hold | 1% (not a finalized charge) | "1%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

Section 403(3) exempts a resident aged60or more (in words on the page) with no business or profession income from advance tax. A large late-year gain requires an updated advance-tax estimate and statutory relief review; check section 425 for how a shortfall is measured. Section 425(4) charges no interest under section 425(1) or (3) on a shortfall caused by "underestimation of, or failure to estimate" "capital gains", where the assessee "has paid in full, the tax payable on the said income" "in any of the remaining instalments of advance tax, if any, or by the 31st day of March of the tax year". Whether this covers a VDA gain is not settled: refer.

Return due dates (section 263(1)(c) of the 2025 Act as substituted by the Finance Act, 2026). For tax year 2026-27 these dates fall in 2027.

| Taxpayer | Due date | Note; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- | --- |
| Source | all dates below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| No business or profession income (most investors) | 31 July | "31st July."; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Business/profession not required audit, or partner of non-audit firm and spouse where s.10 apportionment applies | 31 August | "31st August."; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Company, or a person whose accounts must be audited under this/other law, specified firm partner/spouse cases (no higher-priority transfer-pricing category) | 31 October | "31st October."; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Revised return | Within12months (in words on the page) from the end of the tax year, or before assessment is completed, whichever is earlier | "furnish a revised return at any time within twelve months from the end of the relevant tax year"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

A return not filed by the due date may be filed "within nine months from the end of the relevant tax year, or before the completion of the assessment, whichever is earlier" (section 263(4) of the 2025 Act), with a fee under section 428. An updated return may be filed within48months (in words on the page) from the end of the financial year after the tax year (section 263(6)(a)), subject to the conditions there. Source: https://egazette.gov.in/WriteReadData/2025/265620.pdf

### Section 8: Loss Offset and Carry Forward

| Rule | Detail | Authority; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- | --- |
| VDA loss against other income | Not allowed | Section 194 Table serial 4, column E(b); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| VDA loss against a gain on another VDA | Not allowed. Column E(a) bars "set off of any loss" in computing the VDA income, and E(b) bars setting off a VDA loss against income computed under any provision | Section 194 Table serial 4, column E(a) and (b); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Carry forward of a VDA loss | Not allowed | Column E(b); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Loss from any other head against VDA income | Not allowed | Column E(a); https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Expenses against VDA income | Not allowed, except cost of acquisition | Column E(a); https://egazette.gov.in/WriteReadData/2025/265620.pdf |

Source for this table: https://egazette.gov.in/WriteReadData/2025/265620.pdf

So each profitable transfer is taxed on its own. A loss on one coin does nothing for a gain on another coin in the same year, or in any later year.

#### Example of the no-offset rule (hypothetical amounts, in rupees)

~~~
BTC: bought for 1,000,000, sold for 500,000   -> loss 500,000 (cannot be used)
ETH: bought for 300,000,  sold for 800,000    -> gain 500,000

Tax on VDA income = 30% x 500,000 = 150,000
Cess (no surcharge assumed) = 4% x 150,000 = 6,000
Total = 156,000. The BTC loss is lost for good.
~~~

### Section 9: Anti-Avoidance Rules

#### 9.1 No wash-sale rule needed

The cited s.194 loss rules give no loss-offset benefit from a VDA loss sale; no separate wash-sale absence is established by these cited paragraphs. Any other anti-avoidance application remains referred. Selling at a loss gives no tax benefit anyway, because a VDA loss cannot be set off or carried forward (Section 8).

#### 9.2 Provisions that reach VDAs

| Provision | Effect; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- |
| General Anti-Avoidance Rule, Chapter XI of the 2025 Act (section 178 onwards) | An arrangement may be declared an impermissible avoidance arrangement and its tax consequence determined under that Chapter; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 92(2)(m) | VDA received free or cheaply from non-relatives above the threshold in Section 7.4 is income; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 104 (unexplained asset) | "asset" includes a VDA. An unrecorded VDA with no satisfactory explanation of its source is deemed income of the year it is found; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Section 195 | Income deemed under sections 102 to 106 is taxed at the rate in the table below, with no deduction and no loss set-off; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Search, seizure and block assessment (sections 261, 295 and 301) | The definitions of "asset" and "undisclosed income" used there include VDAs; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

| Item | Value | Note; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| Rate on income deemed under sections 102 to 106, including an unexplained VDA (section 195(1)) | 60% | "at the rate of 60%"; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

| Item | Value | Note; https://egazette.gov.in/WriteReadData/2025/265620.pdf |
| --- | --- | --- |
| Source | all figures below | https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Surcharge on tax under section 195(1)(i), any assessee, tax year 2026-27 | 25% | "25%."; https://egazette.gov.in/WriteReadData/2026/271439.pdf |

#### 9.3 TDS as a tracking tool

TDS under section 393(1) Table serial 8(vi) records each VDA sale against the seller's PAN. Section 509 imposes information duties on reporting entities as prescribed, with prescribed period/form/manner, and the Finance Act, 2026 substituted section 446 to penalise a provider that fails to report or reports wrongly. Retain the reporting-risk warning, but do not assert every provider has already reported before the return: exact prescribed entity/form/deadline applicability and implementation remain held. Finance Act 2026 s.101 substitutes 446; the source does not by itself prove any specific transaction was reported.

#### Complete current filing and payment boundary

The 31 August 2027 category also covers a non-audit firm's partner and spouse where s.10 apportionment applies, even if the individual's own income would otherwise be nonbusiness. Required s.172 report cases, including the prescribed firm-partner/spouse s.10 apportionment cases, take 30 November 2027; the 31 Octobercategory includes a partner of a firm required to be audited and corresponding spouse where 10 applies. Required audit, not only completed audit, controls; review report 63/rule 47 timing separately. Current 428(a)late-return fee 1,000 if income at most 500,000,5,000 otherwise; 428(b)revised-return fee beyond 9 months from tax-year end same income-based amounts, as substituted by Finance Act 2026 s.96. Insufficient self-assessment payment 266(3)goes first fee, then interest, then tax; tax alone is not total cash required. Current ordinary 425(2)/(3)construction remains held, including whether the literal table applies given the words “or, who is liable to pay advance tax under section 404”. A later VDA capital-gain treatment/425(4)relief is a separate unresolved classification, not automatic. [ss.263/266/424-425/428](https://egazette.gov.in/WriteReadData/2025/265620.pdf); [Finance Act 2026 ss.66,67,96](https://egazette.gov.in/WriteReadData/2026/271439.pdf).

A transaction potentially also under platform 8(v)uses VDA 8(vi)priority under 393(1)Note 4. For all deduction calculations apply whole consideration once aggregate strictly EXCEEDS the relevant 12 threshold; equality stays exempt, and deduction timing of earlier amounts when crossing needs factual/statutory review rather than assuming tax only on excess. Missing PAN requires all 3 rates test. Amounts for taxpayer-specific surcharge/cost/valuation/interest held above cannot be finalized merely because arithmetic runs. [393/397](https://egazette.gov.in/WriteReadData/2025/265620.pdf).

## Worked cases

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

Staking reward 25,000           treatment not yet confirmed here from the cited provisions: refer
~~~

### Example 3: a VDA gift from a friend

A receives 0.5 BTC from a friend (not a relative) with a fair market value of 1,500,000 at receipt. A receives no other gifts in the year. A later sells the BTC for 2,000,000.

~~~
Gift: aggregate value 1,500,000 is above the section 92(2)(m) threshold
      -> whole 1,500,000 is income from other sources, taxed at slab rates

Later sale: proceeds 2,000,000, section 194 transfer
      cost of acquisition: not settled for a VDA (see below)
~~~

Section 73 Table serial 17 of the 2025 Act makes the value taxed under section 92(2)(m) the cost of a "capital asset" when "the capital gain arises" on its transfer. A VDA held as an investment is a capital asset (section 2(22)), and section 194 only sets the rate on income from its transfer; but section 194 allows only "cost of acquisition, if any", and the cited passages do not expressly resolve that section 73/194 interaction. Whether the cost on the sale is 1,500,000 or nil is a question for an accountant. Refer before filing. Using nil overstates the gain by 1,500,000; using 1,500,000 without support risks an addition.


### Recomputing check 1: sale gain, disallowed sale fee and TDS credit

Hypothetical ordinary-resident individual; supported cost; no surcharge threshold crossed; no special surcharge interpretation is needed because its base is zero. This is the VDA component only: salary and its credits are not silently assumed zero. A 50,000 TDScredit is assumed supported and assessable in this year, not merely shown as a net bank receipt. Outputs derived.

```oa-check
name: India VDA gain, sale fee and supported credit
inputs:
  proceeds: 5000000
  cost: 2000000
  sale_fee: 5000
steps:
  gain: proceeds - cost
  tax: gain * 0.30
  cess: tax * 0.04
  total_vda: tax + cess
  tds: proceeds * 0.01
  vda_component_after_credit: total_vda - tds
  wrong_fee_deducted_gain: gain - sale_fee
expected:
  gain: 3000000
  tax: 900000
  cess: 36000
  total_vda: 936000
  tds: 50000
  vda_component_after_credit: 886000
  wrong_fee_deducted_gain: 2995000
```

### Recomputing check 2: loss cannot offset another coin's gain

Hypothetical SOLgain 300,000/DOGEloss 300,000; no surcharge; staking 25,000 receipt remains held and is not silently included or exempted. Derive taxable positive-transfer income and compare the invalid netting result; this is not the whole year's return.

```oa-check
name: India VDA separate profit and loss transfers
inputs:
  sol_cost: 200000
  sol_proceeds: 500000
  doge_cost: 400000
  doge_proceeds: 100000
steps:
  sol_gain: sol_proceeds - sol_cost
  doge_loss: doge_cost - doge_proceeds
  taxable_vda: max(0,sol_gain) + max(0,doge_proceeds-doge_cost)
  tax: taxable_vda * 0.30
  cess: tax * 0.04
  total_vda: tax + cess
  invalid_net: sol_gain-doge_loss
expected:
  sol_gain: 300000
  doge_loss: 300000
  taxable_vda: 300000
  tax: 90000
  cess: 3600
  total_vda: 93600
  invalid_net: 0
```

### Recomputing check 3: free versus discounted capital-asset property

Hypothetical nonrelative, no other gift or 92(3)exception, established statutory FMV. Free 0.5 BTCworth 1,500,000 gives full 1,500,000 other-source inclusion. A separate below-value acquisition at FMV 1,500,000 paid 1,440,000 gives 60,000 shortfall, above 50,000, so 60,000 included; at 1,450,000 paid the 50,000 equalitydoesnotcross. Do not combine these as one client's actual gifts. Later-sale cost in original Example 3 remains professionally held; this block does not select nil or 1,500,000 cost.

```oa-check
name: India VDA free and cheap property threshold comparison
inputs:
  fmv: 1500000
  paid: 1440000
  boundary_paid: 1450000
  threshold: 50000
steps:
  free_inclusion: fmv
  shortfall: fmv-paid
  boundary_shortfall: fmv-boundary_paid
  excess_for_test: shortfall-threshold
  boundary_excess: boundary_shortfall-threshold
expected:
  free_inclusion: 1500000
  shortfall: 60000
  boundary_shortfall: 50000
  excess_for_test: 10000
  boundary_excess: 0
```

## When to refuse or refer

Refer to an accountant when:

- Income from mining, staking, lending, yield, liquidity pools, a paid airdrop, or an NFT royalty needs a head of income: it is not yet confirmed here from the cited provisions.
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

For the general income-tax computation (slabs, regimes, rebate) see `india-income-tax`. For instalments see `in-advance-tax`.
- Hold current new-regime VDA surcharge interaction, nonindividual Form 141 Schedule Dcaption, exact acquisition method/cost/valuation, prescribed 509 reporting scope and current 425 construction until confirmed; no blanket tax-free token receipt or automatic zero basis.

## Filing and payment

Use current ITR 2/ITR 3(or referred company ITR 6)as rule 164 requires, actual VDA schedule when the TY 2026-27 utility is issued; no invented boxnumbers. For deduction apply 218/219/215 form/deadline controls and held caption mismatch above; retainchallan/ack/certificate/PAN/walletaudittrail. Pay supported net self-assessment liability including fee/interest before filing, then use category-specific 164 verification. This skill prepares a reviewed working, not authorization to submit or pay. [rules 164/215/218/219](https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf); [266](https://egazette.gov.in/WriteReadData/2025/265620.pdf).

## Completion checklist

- [ ] Every transfer from 1 April 2026 taxed at the section 194 rate, with surcharge for the right regime and cess on tax plus surcharge?
- [ ] No VDA loss used anywhere, in the year or later?
- [ ] Only cost of acquisition deducted?
- [ ] New-regime rebate kept away from the VDA tax?
- [ ] TDS deducted by exchanges matched and credited; TDS owed on peer-to-peer purchases checked?
- [ ] Gifts and free receipts tested on the aggregate for the year, with relatives excluded?
- [ ] Advance tax instalments checked, including for a large sale late in the year?
- [ ] Return form ITR-2 or ITR-3 (not ITR-1 or ITR-4) and the right due date?
- [ ] Every unsettled classification (Section 5) referred, not guessed?

### Prohibitions

- Never set off a VDA loss against any income, including a gain on another VDA. Section 194 Table serial 4, column E.
- Never deduct exchange fees, gas fees or any cost other than cost of acquisition.
- Never apply a holding-period distinction or a capital gains exemption to VDA income.
- Never carry a VDA loss forward.
- Never apply the section 194 rate to a mining, staking or airdrop receipt as if the Act settled it.
- Never use the 1961 Act section numbers for tax year 2026-27.
- Never ignore TDS on a VDA purchase from another person.
- Never present a crypto tax position as definitive; label it as an estimate for professional review.
- [ ] Every unresolved source/valuation/cost/surcharge/current 425/form-caption/utility item held or resolved, rather than marked final because a sample calculation passes.

## Sources

| Official source | Read for | Actual read date |
|---|---|---|
| https://egazette.gov.in/WriteReadData/2025/265620.pdf | Read for 1/3/536 period; 2(109)/(111)whole and 2(22)capitalasset scope; 194 whole includingserial 4 and 194(2)(n),195 whole; 92(2)(m),(3)-(5)whole; 73(1)Table 17; 104 whole; 178-180 GAAR; 261(b),295 whole,301(e)searchscope; 390(5),393(1)serial 8(vi)and Notes 3-6,393(4)serial 12,397 PAN/TAN,400-401; 403-410 and 423-425 whole; 263/266/428 relevantfee/payment provisions; 509 whole. Exact individual 509 rules/notifications and final utility not inferred | 2026-11-15 |
| https://egazette.gov.in/WriteReadData/2026/271439.pdf | Read for individual tax/surcharge/cess s.3/First Schedule I-BPara A/F,66-67 return/payment amendments,87 TANfrom 1 October,96 fees,101 crypto-reporting 446 substitution. VDA/new-regime surcharge interaction held, not a claim every corporate table is reviewed | 2026-11-15 |
| https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-03/En-Notified-IT-Rules-2026-20-03-2026.pdf | Read for 164 entireforms/modes; 203 credit,215 certificates,218/219 entirepayment/statementcontrols and Form 141 Schedule Dcaption plus Form 142 caption; 47 auditreport. Form 141 nonindividualcaption applicability held, finalutilitynotclaimed | 2026-11-15 |

**Not yet confirmed:** current VDA/new-regime surcharge interaction; ordinary 425(2)/(3)construction and VDAcapital-gain/425(4)relief classification; Form 141 nonindividual Schedule Dcaption/actualutility instructions; final TY 2026-27 VDAschedulefields/extensions; prescribed 509 reportingentity/form/period/implementation; bindingmatching/acquisition-costmethod/purchasefee, gifted/free-tokenlaterbasis including 73 interaction; mining/staking/paidairdrop/royalty/De Fi/LP/forkclassificationandvaluation; NFT/exclusionnotifications/CBDCcoverage; gift/wallet-transfer/nonresident/stock-in-trade/crossborder consequences. Older-incomeperiod is out of scope, not silently mapped to currentforms. Underlying held rules/cases are preserved as referral topics.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained on the OpenAccountants site. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
