---
name: mt-capital-gains
description: "Use this skill for capital gains in Malta in basis year 2026 under article 5 of the Income Tax Act. Trigger on CGT Malta, capital gains Malta, sell shares Malta, dispose of shares Malta, Malta tax on investment gains, sell company Malta, Malta no capital gains, foreign property gain Malta, non-dom capital gains. Covers which assets are taxed (securities, business, goodwill, IP, partnership and trust interests, foreign property), the gain computation and losses, listed shares, non-residents and property companies, non-domiciled residents, the company participation exemption, the 35% trust-interest charge, the 7% provisional tax within fifteen days, and the return. Malta property sales are routed to mt-property-transfer-tax-the-sale-immovable. Load before computing Malta tax on any asset disposal."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mt-capital-gains"
  jurisdiction: "MT"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Malta capital gains under article 5, basis year 2026

## Scope

This skill covers how Malta taxes a gain when an **individual** or a **company** transfers a capital asset other than Malta immovable property: shares and other securities, a business or goodwill, business permits, intellectual property, an interest in a partnership, a beneficial interest in a trust, and immovable property outside Malta (or Malta property outside article 5A).

- **Primary year: basis year 2026 = year of assessment 2027.**
- **Returns being filed now:** gains made in 2025 (year of assessment 2026).

**Malta does tax capital gains.** There is no separate capital gains tax act: article 5 of the Income Tax Act, Cap. 123, lists the assets whose gains are taxable and charges them "under article 4(1)". An article 5 gain is added to chargeable income and taxed at the person's normal rates. Assets not in the list (cars, art, coins held as an investment) are outside the charge unless the profit is trading income.

**Malta property is routed elsewhere.** Most transfers of Malta immovable property fall under article 5A, a final tax on the transfer value. Its rates, exemptions and exclusions live in [mt-property-transfer-tax-the-sale-immovable](mt-property-transfer-tax-the-sale-immovable.md) and are not restated here. A Malta property transfer excluded from 5A (for example a non-resident with a home-country certificate, or a business-asset rollover) comes back to this skill.

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
3. **Is it an article 5 asset?** Immovable property; "securities, business, goodwill, business permits, copyright, patents, trademarks and trade-names and any other intellectual property"; a beneficial interest in a trust; an interest in a partnership. "Securities" means "shares and stocks and such like instrument that participate in any way in the profits of the company and whose return is not limited to a fixed rate of return", plus collective investment scheme units and linked long-term insurance units. A fixed-rate bond or fixed-return preference share is not a security: a non-trading gain on it is not taxed.
4. **Reliefs.** Listed shares (art. 5(6)(b)); non-residents in non-property companies (art. 12(1)(c)(ii)); foreign gains of a person not domiciled or not ordinarily resident (art. 4(1), proviso (ii)); a company's participating holding (art. 12(1)(u)); group transfers, share-for-share reorganisations and business incorporations (art. 5(9), (14), (15)), no gain no loss on conditions: refer.
5. **Compute the gain.** Consideration less cost of acquisition and allowable costs (art. 5(2), (3)). Shares acquired after 25 November 1992 at cost; shares paid up out of reserves (other than distributable profits or a capital redemption reserve) at nil cost; older shares have special rules (refer). A donation is a deemed sale at market value, except to close family or approved charities; a donee selling within five years uses the donor's cost (art. 5(2)(e), (f)). A partial transfer apportions cost by consideration over market value of the whole (art. 5(13)(a)).
6. **Set off losses.** A capital loss "shall not be set off against other income for the year of assessment but shall be carried forward and set off against capital gains in respect of subsequent years of assessment until the full loss is absorbed" (art. 5(10)).
7. **Provisional tax.** Pay 7% of the consideration within fifteen days of the transfer (ITMA art. 43(1)(b)), unless an exception applies.
8. **Report.** Add the gain to chargeable income in the return for the year of assessment after the transfer; the provisional tax is credited only if the gain is declared (ITMA art. 43(4)(b)).

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Individual's article 5 gain | Added to chargeable income at the normal 2026 rates | Rate tables owned by malta-income-tax; single 25% band less EUR 3,400 from EUR 16,001 to EUR 60,000 used in Case 1 | MTCA Tax Rates 2026: https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026 |
| Company rate on chargeable income, including article 5 gains | 35% ("thirty-five cents ... on every euro") | Shareholder refunds outside this skill | Cap. 123 art. 56(6): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Transfer of a beneficial interest in a trust holding taxable trust property | 35% of the consideration, no deductions, no relief or credit | Collected by the trustee | Cap. 123 art. 5(19): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Participating holding | At least 5% of the equity shares, among other tests | Company holder; art. 12(1)(u) exemption | Cap. 123 art. 2(1): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Property company, trading exception | Not a property company if Malta property is not more than 50% of its assets and it has no income from Malta property | Company owning only its own business premises | same |
| Minimum tax, non-dom with foreign income | EUR 5,000 a year | Foreign income of at least EUR 35,000 not fully received in Malta; art. 5A tax does not count | Cap. 123 art. 56(27): https://legislation.mt/getpdf/69d8a9187da37f0580d5140c |
| Provisional tax on article 5 transfers | 7% of the consideration, within fifteen days | 7% of the higher of market value and consideration for a controlling interest in securities or a partnership interest; property-company rates under art. 5(9A) or 27G | Cap. 372 art. 43(1)(b): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Reduced provisional tax on request | Allowed where the gain is less than 20% of the consideration | On application | Cap. 372 art. 43(3): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Individual return and tax settlement | 30 June of the year of assessment (30 June 2027 for 2026 gains) | Online return 31 July (MTCA return cycle) | S.L. 372.16 rule 2(c)(ii): https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 |
| Company return | Later of the last day of the ninth month after the accounting period and 31 March of the year of assessment | Persons under Cap. 123 art. 11(2) | S.L. 372.16 rule 2(c)(i): https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 |
| Interest on late tax | 0.6% for every month or part, capped at the tax | Tax payable on or after 31 August 2022 | Cap. 372 art. 44(2A): https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b |
| Duty on a share transfer | 2% of the higher of consideration and real value; plus 3% where 75% or more of the assets, excluding current assets other than immovable property, are immovable property (directly or through holdings) | Separate from income tax | Cap. 364 art. 42(1), (2): https://legislation.mt/eli/cap/364/eng/pdf |

### Residence and the charge

| Person | Article 5 gains arising in Malta | Article 5 gains arising outside Malta |
|---|---|---|
| Resident and domiciled individual | Taxed | Taxed (worldwide) |
| Resident, not domiciled or not ordinarily resident | Taxed | Not taxed, even if received in Malta: "no tax shall be payable on capital gains arising outside Malta" (art. 4(1), proviso (ii)) |
| Non-resident | Taxed, unless exempt under art. 12(1)(c)(ii) | Not taxed |
| Company incorporated in Malta | Taxed at 35% | Taxed at 35%, subject to the participation exemption |

A company managed in Malta but incorporated abroad is taxed on foreign income only when received in Malta, and on foreign capital gains not at all (art. 4(1) provisos): refer. Non-domiciled residents: see [mt-non-dom](mt-non-dom.md).

**Non-residents and Maltese shares (art. 12(1)(c)(ii)).** Exempt: a non-resident's gain on fund units, linked insurance units, an interest in a partnership that is not a property partnership, "and any shares or securities in a company ... which is not a property company", where the beneficial owner "is not owned and controlled by, directly or indirectly, nor acts on behalf of an individual or individuals who are ordinarily resident and domiciled in Malta". A **property company** owns Malta immovable property or real rights over it, or holds interests in an entity that does, where 5% or more of the value of those interests comes from that property (art. 2(1)), subject to the trading exception in the rates table.

**Leaving Malta.** We found no article in the Act that charges an individual on unrealised gains on ceasing residence. After leaving, the person stays taxable on Malta property and on shares in Malta property companies. Company exit taxation under the anti-tax-avoidance rules outside the Act: refer.

**Trust interests (art. 5(19)).** Applies only where the trust holds "taxable trust property", assets whose direct transfer by the beneficiary would be taxed. The gain is "equal to the consideration" in the transfer instrument, taxed at 35% with no relief or credit. The transferor gives the trustee a copy of the instrument within forty-five days; the trustee pays by the fourteenth day after the end of the month of collection. The gain is not declared in the transferor's return.

**Companies.** Article 5 gains form part of chargeable income at 35%. Gains of a company registered in Malta "from a participating holding or from the transfer of such holding" are exempt where the company does not show them as chargeable income (art. 12(1)(u)); holdings in property companies raise extra questions: refer.

## Boundary and exception table

| Situation | Treatment | Why |
|---|---|---|
| Unlisted shares in a Maltese trading company, resident domiciled seller | Article 5 gain at normal rates; 7% provisional tax | Art. 5(1)(a)(ii); ITMA art. 43 |
| Shares listed on a recognised exchange | Outside the capital gains rule (not fund units) | Art. 5(6)(b); which exchanges are recognised: confirm |
| Non-resident sells shares in a Maltese non-property company | Exempt, if not owned or controlled by Malta ordinarily resident and domiciled individuals | Art. 12(1)(c)(ii) |
| Non-resident sells shares in a Maltese property company | Taxable | Art. 12(1)(c)(ii) excludes property companies |
| Non-dom sells foreign shares, proceeds brought to Malta | Not taxed | Art. 4(1), proviso (ii) |
| Fixed-rate bond sold at a gain, not trading | Not taxed | Not "securities" |
| Car, boat, art or investment coins, not trading | Not taxed | Not in the art. 5 list |
| Loss on shares | Carried forward against future capital gains only | Art. 5(10) |
| Gain already taxed as trading income | Not taxed again | Art. 5(11) |
| Transfer by deed of partition, or shares in a public company | No provisional tax | ITMA art. 43(2)(b), (c) |
| Exempt transfer with the prescribed form filed | No provisional tax, except where art. 33 applies as a result of claiming art. 12(1)(u) | ITMA art. 43(2)(a) |
| Malta property | Article 5A, not here | [mt-property-transfer-tax-the-sale-immovable](mt-property-transfer-tax-the-sale-immovable.md) |

## Worked cases

All taxpayers are invented; rates are the 2026 law.

### Case 1: unlisted shares, resident single individual, and the provisional tax

A resident, domiciled, single individual with no other income sells shares in a Maltese trading company that is not a property company, bought in 2015 for EUR 20,000, for EUR 70,000 (market value), not a controlling interest. Gain EUR 50,000, in the 25% band of the 2026 single table: EUR 50,000 x 25% less EUR 3,400 = EUR 9,100. Provisional tax within fifteen days: 7% x EUR 70,000 = EUR 4,900. Balance with the return by 30 June 2027: EUR 4,200. The gain is 71.43% of the consideration, well above 20%, so no reduced provisional tax.

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

A Maltese company sells its whole holding in an EU subsidiary that is not a property company, at a gain of EUR 200,000. If the holding is a participating holding and the company does not show the gain as chargeable income, art. 12(1)(u) exempts it: tax nil. If the holding fails the tests (for example under 5% of the equity and no other limb met), the gain is chargeable at 35%: EUR 70,000. Whether the holding qualifies decides the whole EUR 70,000. Provisional tax can still be due where art. 33 applies as a result of claiming 12(1)(u) (ITMA art. 43(2)(a), proviso): refer.

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

- **Non-resident, Maltese software company.** Resident abroad, not controlled from Malta, company owns no Malta property: exempt under art. 12(1)(c)(ii). File the prescribed form to avoid the 7% provisional tax (ITMA art. 43(2)(a)). If the company owned its office and Malta property were more than 50% of its assets, it would be a property company and the gain taxable.
- **Losses.** A EUR 10,000 loss on unlisted shares in 2025 cannot reduce 2025 salary; set against a EUR 15,000 gain in 2026 it leaves EUR 5,000 taxable.
- **Trust interest.** A beneficiary sells an interest in a trust holding Maltese unlisted shares for EUR 100,000: the trustee collects 35%, EUR 35,000, with no deduction.

## When to refuse or refer

- Property dealers and developers, and anyone whose profit may be trading income.
- Transfers by or of shares in property companies; intra-group, reorganisation, incorporation or group-exit cases (art. 5(9), 5(9A), 5(14), 5(15)).
- Trusts, partnerships, capital reductions and value-shifting (art. 5(13)(b), 5(18) to (25)); shares acquired before 25 November 1992; share options.
- Non-residents relying on a double tax treaty; company exit taxation; participation exemption questions on property companies.
- Any case turning on an MTCA form or rule not read.
- Do not say Malta has no tax on gains from shares; do not set a capital loss against salary or business income.

## Filing and payment

| What | When | Source |
|---|---|---|
| Provisional tax on article 5 transfers | Within fifteen days of the transfer | ITMA art. 43(1)(b) |
| No provisional tax | Exempt transfers with the prescribed form; partition deeds; shares in public companies | ITMA art. 43(2) |
| Individual return declaring 2026 gains | 30 June 2027, tax due the same day; online by 31 July 2027 | S.L. 372.16 rule 2(c)(ii); MTCA return cycle |
| Company return | Later of nine months after the period end and 31 March of the year of assessment | S.L. 372.16 rule 2(c)(i) |
| Trust interest transfer | Transferor to trustee within forty-five days; trustee pays by the fourteenth day after the month of collection | Cap. 123 art. 5(19) |
| Late tax | 0.6% a month or part, capped at the tax | ITMA art. 44(2A) |

Keep the deeds, valuations, cost records and loss computations with the return.

## Completion checklist

- [ ] Asset classified: Malta property (routed), article 5 asset, or outside the charge.
- [ ] Trading or capital decided and recorded.
- [ ] Residence, domicile and ordinary residence recorded.
- [ ] Cost, allowable costs and losses brought forward computed.
- [ ] Reliefs tested: listed, non-resident, non-dom, participation.
- [ ] Property-company status checked for every share transfer; duty considered.
- [ ] Provisional tax paid within fifteen days, or the exemption form filed.
- [ ] Gain declared in the return; balance paid.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for Cap. 123 arts 2(1) (participating holding, property company), 4(1) proviso (ii), 5(1), (2), (3), (6)(b), (10), (11), (13), (19), 12(1)(c)(ii), 12(1)(u), 56(6) and 56(27) | https://legislation.mt/getpdf/69d8a9187da37f0580d5140c | 2026-11-14 |
| Read for Cap. 372 art. 43(1) to (4) (7% provisional tax, exceptions, 20% rule, declaration) and art. 44(2A) (0.6% interest) | https://legislation.mt/getpdf/69c65a5c7da36921dcc4f04b | 2026-11-14 |
| Read for S.L. 372.16 rule 2(c) (tax return dates) | https://legislation.mt/getpdf/6022595cbc8272018c0f2ad2 | 2026-11-14 |
| Read for Cap. 364 art. 42(1) and (2) (2% share duty and the 3% property-company increase) | https://legislation.mt/eli/cap/364/eng/pdf | 2026-11-14 |
| Read for MTCA Tax Rates 2026, single table (25% band used in Case 1) | https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026 | 2026-11-14 |
| Read for MTCA Tax Return Cycle (31 July online return date) | https://mtca.gov.mt/personal-tax/individual/tax-return-cycle | 2026-11-14 |

Not yet confirmed: which stock exchanges the Commissioner recognises for art. 5(6)(b); the prescribed valuation rules for shares acquired before 25 November 1992; the name of the prescribed exemption form under ITMA art. 43(2)(a); the provisional tax rate prescribed for property-company securities under art. 5(9A) and 27G; company exit taxation under the anti-tax-avoidance rules; whether MTCA extends the 2027 return date for 2026 gains.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mt-capital-gains` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mt-capital-gains. If neither is available, confirm every figure against the official source pages cited above before relying on it.
