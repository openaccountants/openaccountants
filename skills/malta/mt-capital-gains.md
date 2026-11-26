---
name: mt-capital-gains
description: "Use this skill for capital gains in Malta in basis year 2026 under article 5 of the Income Tax Act. Trigger on CGT Malta, capital gains Malta, sell shares Malta, dispose of shares Malta, Malta tax on investment gains, sell company Malta, Malta no capital gains, foreign property gain Malta, non-dom capital gains. Covers which assets are taxed (securities, business, goodwill, IP, partnership and trust interests, foreign property), the gain computation and losses, listed shares, non-residents and property companies, non-domiciled residents, the company participation exemption, the 35% trust-interest charge, the 7% provisional tax within fifteen days, and the return. Malta property sales are routed to mt-property-transfer-tax-the-sale-immovable. Load before computing Malta tax on any asset disposal."
version: "2.1"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Malta capital gains under article 5, basis year 2026

## Scope

This skill covers how Malta taxes a gain when an **individual** or a **company** transfers a capital asset other than Malta immovable property: shares and other securities, a business or goodwill, business permits, intellectual property, an interest in a partnership, a beneficial interest in a trust, and immovable property outside Malta (or Malta property outside article 5A).

- **Primary year: basis year 2026 = year of assessment 2027.**
- **Prior-year returns:** gains made in 2025 belong to year of assessment 2026; this Guide does not certify their historical rates or deadlines.

**Malta does tax capital gains.** There is no separate capital gains tax act: article 5 of the Income Tax Act, Cap. 123, lists the assets whose gains are taxable and charges them "under article 4(1)". An article 5 gain is added to chargeable income and taxed at the person's normal rates. Assets not in the list (cars, art, coins held as an investment) are outside the charge unless the profit is trading income.

**Malta property is routed elsewhere.** Most transfers of Malta immovable property fall under article 5A, a final tax on the transfer value. Its rates, exemptions and exclusions live in [mt-property-transfer-tax-the-sale-immovable](mt-property-transfer-tax-the-sale-immovable.md) and are not restated here. A Malta property transfer excluded from article 5A comes back to article 5 only after the exclusion conditions have been established. Non-resident certificate and business-asset rollover cases: Check this point with one of our partner accountants.

Related: individual rate tables [malta-income-tax](malta-income-tax.md); crypto-assets [mt-crypto-tax](mt-crypto-tax.md); non-domiciled residents [mt-non-dom](mt-non-dom.md); share sales with duty and MBR steps [selling-a-company-in-malta](selling-a-company-in-malta.md); company tax [mt-corporate-tax](mt-corporate-tax.md); participation exemption detail [mt-holding-company-participation-exemption](mt-holding-company-participation-exemption.md).

Built from the law: not yet approved by an accountant.

## Ask the client first

1. **What exactly was transferred?** Shares (Maltese or foreign, listed or not), fund units, bonds, a business, IP, a partnership interest, a trust interest, foreign property, Malta property? Sold, donated, exchanged, redeemed, or distributed in a winding up?
2. **Who is the transferor, and their residence, domicile and ordinary residence** in the year: resident and domiciled; resident but not domiciled or not ordinarily resident; not resident; or a company (incorporated in Malta or only managed here)?
3. **Dates and amounts.** Date of transfer, date and way of acquisition, consideration, market value, cost and transfer costs. Shares acquired before 25 November 1992?
4. **Trade or investment?** Does the client deal in such assets, or buy to resell at a profit?
5. **Company facts for shares.** Is it a **property company**? Is the holding a **participating holding**? Listed on an exchange recognised by the Commissioner? A controlling interest?
6. **Losses** brought forward from earlier article 5 transfers.

## The method, step by step

1. **Trading or capital?** An asset bought "for the purpose of profit-making by sale", or a trade in such assets, gives trading income under art. 4(1)(a) at normal rates; a gain so taxed "shall not be chargeable again as capital gains" (art. 5(11)).
2. **Malta immovable property?** Go to [mt-property-transfer-tax-the-sale-immovable](mt-property-transfer-tax-the-sale-immovable.md). Return here only if the transfer is excluded from article 5A.
3. **Is it an article 5 asset?** Immovable property; "securities, business, goodwill, business permits, copyright, patents, trademarks and trade-names and any other intellectual property"; a beneficial interest in a trust; an interest in a partnership. "Securities" means "shares and stocks and such like instrument that participate in any way in the profits of the company and whose return is not limited to a fixed rate of return", plus collective investment scheme units and linked long-term insurance units. An instrument whose rights are confined to a fixed return falls outside the profit-participating limb; check the separate fund/insurance limbs and actual rights before concluding it is outside article 5.
4. **Reliefs.** Listed shares (art. 5(6)(b)); non-residents in non-property companies (art. 12(1)(c)(ii)); foreign gains of a person not domiciled or not ordinarily resident (art. 4(1), proviso (ii)); a company's participating holding (art. 12(1)(u)); group transfers, share-for-share reorganisations and business incorporations (art. 5(9), (14), (15)) have conditional no-gain/no-loss provisions. Check this point with one of our partner accountants. Listed, non-resident and non-dom relief conditions are stated below; do not infer them from a label.
5. **Compute the gain using the asset-specific rules.** For securities/business/IP, take account of acquisition cost under S.L. 123.27 rule 4, excluding sums already deducted against income (rule 3; IP also rule 4(2)); do not automatically deduct every transaction fee. Shares acquired after 25 November 1992 use acquisition cost subject to share-option, reserve-capitalisation and partnership-conversion rules; reserve capitalisation has nil cost except for distributable profits and capital redemption reserves (art. 5(3)(c)). Same-class shares acquired at different times use earlier acquisitions first (rule 5C). For shares within rule 5(15), a controlling-interest transfer uses the higher of consideration and prescribed market value; control includes rights at any time in the preceding eighteen months and related transactions (rule 5(1)–(4)), not just majority ownership. The valuation and auditor/form requirements must be completed, not guessed from an agreed price. For immovable property, article 5(2) and rule 2 prescribe acquisition, inflation, ground-rent, improvement, maintenance and expense adjustments. For partnerships use article 5(3A) and adjusted cost/valuation rules 5D–5E. Old shares, fees whose deductibility is unresolved, property valuations and partnership computations: Check this point with one of our partner accountants.

   A donation is a deemed market-value sale. Article 5(2)(e) exempts a donation to the donor's spouse, direct-line descendants/ascendants and their spouses; siblings and their descendants qualify only in the absence of descendants; approved philanthropic institutions also qualify. These provisions extend to securities/business/IP through article 5(3)(f), and relevant partnership interests through article 5(3A)(c). A donee's disposal within five years uses the donor's cost; after five years article 5(2)(f) uses the deed's declared donation value, subject to the relevant acquisition/valuation rules. Do not apply an undifferentiated “close family” exemption. A part-disposal of an asset acquired as an undivided part of a larger asset apportions the whole asset's acquisition cost and other allowable deductions by consideration divided by the whole asset's market value (art. 5(13)(a)).
6. **Set off losses.** A capital loss "shall not be set off against other income for the year of assessment but shall be carried forward and set off against capital gains in respect of subsequent years of assessment until the full loss is absorbed" (art. 5(10)).
7. **Provisional tax.** Article 43 applies to article 5(1)(a) transfers even where the gain is taxed as trading income. Its ordinary rule is 7% of consideration (donation: value) within fifteen days; apply its higher-market-value, deemed-transfer, property-company/partnership and group-exit provisions before using that rate. See the table and exceptions below. Trust-interest special collection is described separately; Check this point with one of our partner accountants if both provisions may apply.
8. **Report.** Add the gain to chargeable income in the return for the year of assessment after the transfer; the provisional tax is credited only if the gain is declared (ITMA art. 43(4)(b)).

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Individual's article 5 gain | Added to chargeable income at the normal 2026 rates | Rate tables owned by malta-income-tax; single 25% band less EUR 3,400 from EUR 16,001 to EUR 60,000 used in Case 1 | MTCA Tax Rates 2026: https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026 |
| Company ordinary rate on chargeable income, including article 5 gains | 35% ("thirty-five cents ... on every euro") | Subject to any applicable special or elective regime; shareholder refunds and regime selection: Check this point with one of our partner accountants | Cap. 123 art. 56(6): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Transfer of a beneficial interest in a trust holding taxable trust property | 35% of the consideration, no deductions, no relief or credit | Collected by the trustee | Cap. 123 art. 5(19): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Participating holding, percentage limb | Direct holding of at least 5% of equity shares, conferring at least 5% of any two of voting, profit and winding-up rights | “Equity holding” excludes a property company. Alternative limbs exist; qualification and article 12(1)(u) conditions must be checked | Cap. 123 art. 2(1): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Property company, trading exception | Not a property company if Malta property is not more than 50% of its assets and it has no income from Malta property | Factory, showroom, warehouse or office used solely in its trade/business; no activity deriving income directly or indirectly from Malta immovable property; indirect property interests also tested | same |
| Minimum tax, non-dom with foreign income | EUR 5,000 a year | Ordinarily resident/non-domiciled individual to whom article 4 provisos apply; no other minimum-tax scheme; foreign income at least EUR 35,000 not fully received, spouses aggregated if assessed jointly; pre-double-tax-relief Malta tax excluding article 5A, with Malta withholding counted. Lower worldwide-basis liability may be proved to the Commissioner | Cap. 123 art. 56(27): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Provisional tax on article 5 transfers | 7% of the consideration, within fifteen days | 7% of the higher of market value and consideration for a controlling interest in securities or a partnership interest; property-company/partnership prescribed amount (ceiling 35% of higher value, disregarding the trading-premises exception for this purpose); art. 5(9A)/27G special rules. Transfer of value/deemed partnership transfer: 7% of statutory gains. Check this point with one of our partner accountants for these special computations | Cap. 372 art. 43(1)(b): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Reduced provisional tax on request | Commissioner may authorise a lower rate where proved gain is less than 20% of consideration/donation value | For controlling securities or partnership interest use 20% of higher market value and consideration; no automatic reduction | Cap. 372 art. 43(3): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Individual return and tax settlement | 30 June of the year of assessment (30 June 2027 for 2026 gains) | Statutory individual date; no 31 July 2027 online extension assumed; article 42 and S.L. 372.16 distinguish settlement from filing for other persons | S.L. 372.16 rule 2(c)(ii): https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 |
| Company return | Later of the last day of the ninth month after the accounting period and 31 March of the year of assessment | Persons under Cap. 123 art. 11(2) | S.L. 372.16 rule 2(c)(i): https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 |
| Interest on late tax | 0.6% for every month or part, capped at the tax | Tax payable on or after 31 August 2022; article 44(2B) exceptions may apply (written FSS collection direction, specified additional tax, mutual-agreement procedure). Late provisional tax also falls within article 44(1); liability/remission: Check this point with one of our partner accountants | Cap. 372 art. 44(2A): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Duty on a share transfer | EUR 2 for every EUR 100 or part of the higher of consideration and real value; additional EUR 3 per EUR 100 or part only where art. 42(2) applies | Separate from income tax; art. 42(2)(a) tests 75% immovable assets with current-asset adjustment, and (b) qualifying direct/indirect aggregate holdings; exemptions and document scope must be established | Cap. 364 art. 42(1), (2): https://legislation.mt/eli/cap/364/eng/pdf |

### Residence and the charge

| Person | Article 5 gains arising in Malta | Article 5 gains arising outside Malta |
|---|---|---|
| Resident and domiciled individual | Taxed | Taxed (worldwide) |
| Resident, not domiciled or not ordinarily resident | Taxed | Outside the charge even if received, only if article 4(1) provisos apply; exceptions below |
| Non-resident | Taxed, unless exempt under art. 12(1)(c)(ii) | Not taxed |
| Company incorporated in Malta | Taxed at ordinary 35%, subject to applicable regime/reliefs | Taxed at ordinary 35%, subject to applicable regime/reliefs |

The article 4(1) remittance provisos do not apply to an individual from the year of grant of long-term resident status or the specified permanent residence certificate/card and subsequent years, or where their spouse is ordinarily resident and domiciled in Malta. Residence, domicile, ordinary residence and source must be established, including when a gain is foreign. A foreign-incorporated company managed in Malta requires its residence/domicile and actual article 4 treatment established; Check this point with one of our partner accountants. Non-domiciled residents: see [mt-non-dom](mt-non-dom.md).

**Non-residents and Maltese shares (art. 12(1)(c)(ii)).** Exempt: a non-resident's gain on fund units, linked insurance units, an interest in a partnership that is not a property partnership, "and any shares or securities in a company ... which is not a property company", where the beneficial owner is also non-resident and “is not owned and controlled by, directly or indirectly, nor acts on behalf of an individual or individuals who are ordinarily resident and domiciled in Malta”. A **property company** owns Malta immovable property or real rights over it, or holds interests in an entity that does, where 5% or more of the value of those interests comes from that property (art. 2(1)), subject to the trading exception in the rates table.

**Leaving Malta.** Departure does not itself prove exemption or establish a gain's source. Individual unrealised-gain treatment, post-departure disposals, treaties and company exit taxation require case-specific analysis. Check this point with one of our partner accountants.

**Trust interests (art. 5(19)).** A written transfer instrument covering “taxable trust property” triggers the special rule: property whose direct transfer by that beneficiary would give rise to taxable gains. The consideration in the instrument is taxed at the article 56(6) rate of 35%, with no deductions, relief, reduction, credit or set-off. Within forty-five days of execution, the transferor provides an authenticated instrument and requires the trustee to collect tax. By the fourteenth day following the collection month the trustee pays and supplies the gains/assets account on the prescribed form, authenticated instrument and latest trust financial statements. Within fifteen days of MTCA's acknowledgement the trustee gives the parties a compliance certificate. The transfer has no legal effect unless the written instrument and transferor/trustee obligations in paragraphs (d)–(e) are fulfilled. Non-disclosure in the transferor's return is subject to ITMA article 10A. Article 5(19)(i) contains a Commissioner-ordered bona fide irrevocable-disclaimer exception and an exception for trusts holding property solely for a designated commercial transaction under article 5(24). Qualification, forms and these exceptions: Check this point with one of our partner accountants.

**Companies.** The ordinary company rate is 35%, subject to applicable special/elective regimes. Article 12(1)(u) can exempt a company registered in Malta's gains from a qualifying participating holding where not included in chargeable income in its return. The definition of equity holding excludes a property company. A holding in a Malta-resident entity, or another entity holding interests in one, has the additional ultimate beneficial-owner test: exemption only to the extent the gain would qualify under article 12(1)(c)(ii) if made by that beneficial owner; later entitlement by a non-qualifying shareholder can trigger tax. The EU non-cooperative-jurisdiction proviso must also be tested where relevant. Do not transplant dividend-only conditions onto a disposal. Participation relief, changes of ownership, group relief, refunds and regime selection: Check this point with one of our partner accountants.

**Listed holdings.** Article 5(6)(b) covers shares listed, or transferred in consequence of a listing, on an exchange recognised for this provision; it excludes collective-investment-scheme securities. The MTCA recognition note lists World Federation of Stock Exchanges member exchanges, NYSE and exchanges in ESMA's EEA regulated-markets register; the UK note adds its specified UK markets. Identify the actual market and recognition at transfer, rather than assuming every product on a familiar platform qualifies. Fund and linked-insurance limbs have their own conditions under article 5(6)(c)–(d). Alternative trading platforms have separate rules under S.L. 123.27 rule 4A. For a specific unresolved listing, fund, insurance or alternative-platform position: Check this point with one of our partner accountants.

## Boundary and exception table

| Situation | Treatment | Why |
|---|---|---|
| Unlisted shares in a Maltese trading company, resident domiciled seller | Article 5 gain at normal rates; ordinary 7% provisional rule subject to control/property-company/special-transfer and exemption tests | Art. 5(1)(a)(ii); ITMA art. 43 |
| Shares listed on a recognised exchange | Article 5(6)(b) relief only for qualifying shares; separate fund/insurance/alternative-platform tests | Recognition and asset tests above; unresolved product: Check this point with one of our partner accountants |
| Non-resident sells shares in a Maltese non-property company | Exempt only if beneficial owner is non-resident, is not owned and controlled by Malta ordinarily resident/domiciled individuals and does not act on their behalf | Art. 12(1)(c)(ii) |
| Non-resident sells shares in a Maltese property company | Exemption in article 12(1)(c)(ii) unavailable; treaty/other relief: Check this point with one of our partner accountants | Art. 12(1)(c)(ii) excludes property companies |
| Non-dom sells foreign shares, proceeds brought to Malta | Outside charge only if article 4 provisos actually apply; permanent-status/spouse/source tests above | Art. 4(1), proviso (ii) |
| Fixed-rate bond sold at a gain, not trading | Outside article 5 only if actual instrument is outside all taxable-asset limbs | No blanket product-label exemption |
| Car, boat, art or investment coins, not trading | Not taxed | Not in the art. 5 list |
| Loss on shares | Carried forward against future capital gains only | Art. 5(10) |
| Gain already taxed as trading income | Not taxed again | Art. 5(11) |
| Transfer by deed of partition, or shares in a public company | No provisional tax | ITMA art. 43(2)(b), (c) |
| Exempt transfer with prescribed form and any required relevant documents submitted | No provisional tax, except where art. 33 applies as a result of claiming art. 12(1)(u) | ITMA art. 43(2)(a) |
| Malta property | Article 5A, not here | [mt-property-transfer-tax-the-sale-immovable](mt-property-transfer-tax-the-sale-immovable.md) |

## Worked cases

All taxpayers are invented; rates are the 2026 law.

### Case 1: unlisted shares, resident single individual, and the provisional tax

A resident, domiciled, single individual with no other income sells shares in a Maltese trading company that is not a property company, bought in 2015 for EUR 20,000, for EUR 70,000 (market value), not a controlling interest. Gain EUR 50,000, in the 25% band of the 2026 single table: EUR 50,000 x 25% less EUR 3,400 = EUR 9,100. Assume the stated non-controlling status is established under the eighteen-month/rights tests, the EUR 20,000 cost is the applicable cost and no additional deductions, losses or reliefs apply. Provisional tax within fifteen days: 7% x EUR 70,000 = EUR 4,900. Balance with the return by 30 June 2027: EUR 4,200. The gain is 71.43% of the consideration, well above 20%, so no reduced provisional tax.

```oa-check
name: Unlisted shares, gain EUR 50,000, single 2026 table and 7 percent provisional tax
inputs:
  cost: 20000
  price: 70000
steps:
  - gain: price - cost
  - tax: gain * 0.25 - 3400
  - provisional: pct(price, 7)
  - balance: tax - provisional
  - gain_share_pct: round(gain / price * 100, 2)
expected:
  gain: 50000.00
  tax: 9100.00
  provisional: 4900.00
  balance: 4200.00
  gain_share_pct: 71.43
```

### Case 2: company sells a subsidiary, participation exemption or tax (a decision)

A Maltese company sells its whole holding in an EU subsidiary that is not a property company, at a gain of EUR 200,000. Assuming all participation-definition, ownership and article 12(1)(u) conditions are satisfied and the gain is excluded from chargeable income, tax is nil. A subsidiary described only as EU/non-property does not establish every test. If the holding fails the tests (for example under 5% of the equity and no other limb met), assuming the ordinary company regime and no other relief/loss, the gain is chargeable at 35%: EUR 70,000. Whether the holding qualifies decides the whole EUR 70,000. Provisional tax can still be due where art. 33 applies as a result of claiming 12(1)(u) (ITMA art. 43(2)(a), proviso). Check this point with one of our partner accountants.

```oa-check
name: Company gain EUR 200,000, participating holding exempt versus 35 percent
inputs:
  gain: 200000
  exempt_share: 0
steps:
  - tax_if_exempt: gain * exempt_share * 0.35
  - tax_if_taxable: pct(gain, 35)
  - value_of_exemption: tax_if_taxable - tax_if_exempt
expected:
  tax_if_exempt: 0.00
  tax_if_taxable: 70000.00
  value_of_exemption: 70000.00
```

### Further cases (prose)

- **Non-resident, Maltese software company.** Resident abroad, not controlled from Malta, company owns no Malta property: exemption also requires the non-resident beneficial-owner and no-Malta-principal tests and no indirect property-company holding. File the prescribed form and any required relevant documents to avoid provisional tax (ITMA art. 43(2)(a)); rule 5(14) provides Schedule E where its scope is met. Check this point with one of our partner accountants for the complete filing package. If the company owned its office and Malta property were more than 50% of its assets, it would be a property company and the gain taxable.
- **Losses.** A EUR 10,000 loss on unlisted shares in 2025 cannot reduce 2025 salary; assuming an allowable, unabsorbed article 5 loss, set against a taxable EUR 15,000 article 5 gain in 2026 it leaves EUR 5,000 before other applicable reliefs.
- **Trust interest.** A beneficiary sells an interest in a trust holding Maltese unlisted shares for EUR 100,000: if their direct transfer would be taxable, the written instrument triggers article 5(19), and no exception applies, the trustee collects 35%, EUR 35,000, with no deduction. Follow all document, payment and certificate steps above; Check this point with one of our partner accountants before treating the transfer as effective.

## When to refuse or refer

- Property dealers and developers, and anyone whose profit may be trading income.
- Transfers by or of shares in property companies; intra-group, reorganisation, incorporation or group-exit cases (art. 5(9), 5(9A), 5(14), 5(15)).
- Trusts, partnerships, capital reductions and value-shifting (art. 5(13)(b), 5(18) to (25)); shares acquired before 25 November 1992; share options.
- Non-residents relying on a double tax treaty; company exit taxation; participation exemption questions on property companies.
- Any case turning on an MTCA form or rule not read.
- Do not say Malta has no tax on gains from shares; do not set a capital loss against salary or business income.

For each specialist case listed above: Check this point with one of our partner accountants. A referral is not permission to use an unverified rate, exemption or deadline.

## Filing and payment

| What | When | Source |
|---|---|---|
| Provisional tax on article 5 transfers | Within fifteen days of the transfer | ITMA art. 43(1)(b) |
| No provisional tax | Qualifying exempt transfers with prescribed form and required documents (article 12(1)(u)/33 proviso applies); partition deeds; shares in public companies | ITMA art. 43(2) |
| Individual return declaring 2026 gains | 30 June 2027 statutory individual return/settlement date; no online extension assumed | S.L. 372.16 rule 2(c)(ii); MTCA return cycle |
| Company return | Later of nine months after the period end and 31 March of the year of assessment | S.L. 372.16 rule 2(c)(i) |
| Trust interest transfer | Transferor to trustee within forty-five days; trustee pays by the fourteenth day after the month of collection | Cap. 123 art. 5(19) |
| Late tax | 0.6% a month or part, capped at the tax, subject to exceptions above; additional-tax rules considered separately | ITMA art. 44(1), (2A), (2B); S.L. 372.28 rule 2 |

Retain deeds, valuations, cost records, filing acknowledgements and loss computations. ITMA article 19 requires proper and sufficient records for at least nine years after completion of the relevant transactions/acts/operations, subject to alternative Companies Act periods under articles 26, 163(5) or 324(2). For shares in rule 5(15), rules 5(10)–(14) require an auditor statement: Schedule C for control (with prescribed valuation and applicable Perit valuation plus Land Registry site plan signed/stamped by a Perit), D otherwise, E for specified reliefs. Delivery/payment validity requirements apply. MTCA waives D/E/F and supporting auditor/valuation submissions for shares of a public company listed/admitted/dealt on a stock exchange, regulated market or multilateral system; it still requires a return for a taxable gain. This procedural waiver does not itself exempt the gain. Other exemption forms or unresolved filing scope: Check this point with one of our partner accountants.

## Completion checklist

- [ ] Asset classified: Malta property (routed), article 5 asset, or outside the charge.
- [ ] Trading or capital decided and recorded.
- [ ] Residence, domicile and ordinary residence recorded.
- [ ] Cost, allowable costs and losses brought forward computed.
- [ ] Reliefs tested: listed, non-resident, non-dom, participation.
- [ ] Property-company status checked for every share transfer; duty considered.
- [ ] Provisional tax paid within fifteen days, or the applicable exception and all required documents established.
- [ ] Gain declared where required (trust special treatment considered); balance paid by applicable settlement date.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for Cap. 123 arts 2(1) (participating holding, property company), 4(1) proviso (ii), 5(1), (2), (3), (6)(b), (10), (11), (13), (19), 12(1)(c)(ii), 12(1)(u), 56(6) and 56(27) | https://legislation.mt/getpdf/69d8a9187da37f0580d5140c | 2026-11-26 |
| Read for Cap. 372 art. 43(1) to (4) (7% provisional tax, exceptions, 20% rule, declaration) and art. 44(2A) (0.6% interest) | https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b | 2026-11-26 |
| Read for S.L. 372.16 rules 2(c) and 5 (separate return and settlement dates) | https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 | 2026-11-26 |
| Read for Cap. 364 art. 42(1) and (2) (2% share duty and the 3% property-company increase) | https://legislation.mt/eli/cap/364/eng/pdf | 2026-11-26 |
| Read for MTCA Tax Rates 2026, single table (25% band used in Case 1) | https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026 | 2026-11-26 |
| Read for MTCA Tax Return Cycle (current cycle only; no 2027 extension inferred) | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-11-26 |
| Read S.L. 123.27 rules 2–5, 5C–5E, 6–8 for asset-specific computation, controlling-interest tests, auditor statements, FIFO and reorganisation conditions; specialist computations referred | https://legislation.mt/getpdf/6a2faefc0946e208a0f18076 | 2026-11-26 |
| Read S.L. 372.28 rule 2 (interest rate and cap), completed personal-tax read applicability confirmed | https://legislation.mt/eli/sl/372.28/eng/pdf | 2026-11-26 |
| Read recognition categories in MTCA stock-exchange guidance | https://mtca.gov.mt/docs/default-source/documents/mtca-recognized-stock-exchanges.pdf?sfvrsn=a14a0bb0_1 | 2026-11-26 |
| Read UK recognition table in supplementary MTCA note; specific market identity still required | https://mtca.gov.mt/docs/default-source/documents/business-tax/international-affairs/public-owned-companies/mtca-guidance-note-on-recognized-stock-exchanges---united-kingdom.pdf?sfvrsn=4f1fb47e_3 | 2026-11-26 |
| Read public-company Schedule D/E/F submission waiver and retained taxable-return obligation | https://mtca.gov.mt/personal-tax/legal-and-technical/test/submission-of-schedules-under-the-capital-gains-rules | 2026-11-26 |

Source reads supporting unchanged provisions from the completed 26 November personal-tax audits were reused after checking applicability. Source-copy storage is tracked separately. Not yet confirmed: old-share valuations, special property-company provisional tax, exit taxation and unresolved filing forms are non-usable referrals above: Check this point with one of our partner accountants.
