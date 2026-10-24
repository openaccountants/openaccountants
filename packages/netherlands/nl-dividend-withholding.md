---
name: nl-dividend-withholding
description: "Dutch dividend tax (dividendbelasting) and the conditional withholding tax (bronbelasting) on interest, royalties and dividends, for tax year 2026, plus how a non-resident company with a Dutch permanent establishment is taxed. Covers the 15% dividend tax, the domestic and EU/EEA/treaty participation exemptions with the anti-abuse test, treaty reductions at source (IB 92 Universeel) and refunds, the one-month return, the 25.8% conditional withholding tax on payments to affiliates in the 2026 low-tax list, the credit of dividend tax against it, the annual return, gross-ups and penalties. Trigger on: dividendbelasting, dividend tax Netherlands, withholding on a BV dividend, IB 92, kwalificatiebeschikking, bronbelasting, conditional withholding tax, low-tax jurisdiction, opgaaf dividendbelasting, buitenlandse belastingplichtige, Dutch permanent establishment. Out of scope: the BV's own corporate tax (nl-corporate-tax), the shareholder's box 2 tax (nl-box2-substantial-interest), residence and emigration (nl-cross-border), transfer pricing (netherlands-transfer-pricing)."
version: 0.1
jurisdiction: NL
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands: dividend tax and conditional withholding tax (2026)

This skill covers the two Dutch taxes withheld at source by a paying company: dividend tax (dividendbelasting) under the Wet op de dividendbelasting 1965 (Wet DB) and the conditional withholding tax (bronbelasting) under the Wet bronbelasting 2021 (Wet BB). It also sets out who is taxable when a foreign company earns profit through a Dutch permanent establishment (Wet Vpb 1969 arts. 3, 17, 17a) and how profit is attributed to it. Related skills: [nl-corporate-tax](nl-corporate-tax.md) (the BV's own tax, participation exemption, filing dates), [nl-box2-substantial-interest](nl-box2-substantial-interest.md) (a Dutch individual's tax on the dividend), [nl-cross-border](nl-cross-border.md) (residence, emigration, treaty relief for individuals), [netherlands-transfer-pricing](netherlands-transfer-pricing.md).

## Who this applies to

**Dividend tax.**
- It is levied on whoever is entitled to the proceeds of shares, profit-sharing certificates and certain hybrid loans in a company established in the Netherlands: an nv, a bv, comparable foreign-law entities, funds for joint account and holding cooperatives (Wet DB art. 1(1)).
- A company incorporated under Dutch law is always treated as established in the Netherlands, wherever it is managed (Wet DB art. 1(3)).
- The paying company is the withholding agent. It withholds when the dividend is made available and pays the tax on a return (Wet DB art. 7(1) to (4)).
- An exempt investment institution (art. 6a Wet Vpb) is outside dividend tax, subject to the exceptions in art. 1(5) (Wet DB art. 1(4)).

**Conditional withholding tax.**
- The taxpayer is an entity entitled to interest, royalties or dividends that is established in a low-tax jurisdiction, or holds the payment through a permanent establishment in one, or holds it in an abuse structure or a hybrid mismatch (Wet BB art. 2.1(1)(a) to (e)).
- It applies only to payments from a withholding agent that is **affiliated** with the recipient (Wet BB arts. 3.3, 3.4, 3.4a). Affiliation means a qualifying interest: an interest that gives enough influence on the entity's decisions to determine its activities, directly or indirectly, either way round or through a common third party (Wet BB art. 1.2(1)(c) and (d)). The Belastingdienst treats more than 50% of the statutory voting rights as always qualifying.
- For dividends, only an affiliated withholding agent in which the recipient holds the qualifying interest counts (Wet BB art. 3.4a(1), referring to art. 1.2(1)(c) 1°, 3°, 4° and 6°). A Dutch BV paying a dividend to its foreign parent is the standard case.
- The withholding agent can be an nv, bv, cooperative, mutual, association, foundation, other Dutch legal person, fund for joint account, comparable foreign-law entity, or a reverse hybrid (Wet BB art. 1.2(1)(b)); for dividends the list is narrower (art. 1.2(3)).

**Non-resident companies (buitenlandse belastingplichtigen).** A foreign entity comparable to a Dutch company is taxable in the Netherlands if it has Dutch income (Wet Vpb art. 3(1)). See the subsection under Cross-border points.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Dividend tax | 15% of the proceeds | 2026 | https://wetten.overheid.nl/BWBR0002515/2025-01-01 (art. 5) |
| Dividend tax borne by the paying company (gross-up) | Proceeds times 100/85 | 2026 | https://wetten.overheid.nl/BWBR0002515/2025-01-01 (art. 6(1)) |
| Participation test for the withholding exemption | A holding that would qualify for the participation exemption (generally 5% or more) | 2026 | https://wetten.overheid.nl/BWBR0002515/2025-01-01 (art. 4(1), (2)); https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert |
| Conditional withholding tax | Highest Vpb rate in Wet Vpb art. 22: 25.8% | 2026 | https://wetten.overheid.nl/BWBR0042952/2026-01-01 (art. 4.1); https://wetten.overheid.nl/BWBR0002672/2026-01-01 (art. 22) |
| Conditional withholding tax borne by the payer (gross-up) | Payment times 100/(100 - 25.8) | 2026 | https://wetten.overheid.nl/BWBR0042952/2026-01-01 (art. 4.2) |
| Low-tax test | A state designated by ministerial regulation that, on 1 October of the preceding year, has no profit tax or a statutory rate below 9%, or is on the EU list of non-cooperative jurisdictions in force in the preceding year | 2026 | https://wetten.overheid.nl/BWBR0042952/2026-01-01 (art. 1.2(1)(e)) |
| Low-tax jurisdictions designated for 2026 (rate test) | Anguilla, Bahamas, Bahrain, Bermuda, British Virgin Islands, Guernsey, Isle of Man, Jersey, Cayman Islands, Turkmenistan, Turks and Caicos Islands, Vanuatu | 2026 | https://wetten.overheid.nl/BWBR0041785/2026-01-01/0 (art. 2a(a)) |
| Low-tax jurisdictions designated for 2026 (EU list) | US Virgin Islands, American Samoa, Anguilla, Fiji, Guam, Palau, Panama, Russian Federation, Samoa, Trinidad and Tobago, Vanuatu | 2026 | https://wetten.overheid.nl/BWBR0041785/2026-01-01/0 (art. 2a(b)) |
| Delay for a newly listed treaty state | Not low-tax until three calendar years after first designation | 2026 | https://wetten.overheid.nl/BWBR0042952/2026-01-01 (art. 1.2(8)) |
| Vpb rates for a Dutch permanent establishment | 19% up to EUR 200,000; 25.8% above | 2026 | https://wetten.overheid.nl/BWBR0002672/2026-01-01 (art. 22) |
| Beneficial ownership presumption on refunds | Inspector must prove the contrary if dividend tax withheld in the year is EUR 1,000 or less | 2026 | https://wetten.overheid.nl/BWBR0002515/2025-01-01 (arts. 10(1), 10a(3)) |

## The taxable base

**Dividend tax: what counts as proceeds** (Wet DB art. 3(1)):
- Any direct or indirect profit distribution, whatever its name or form, including a share buyback (other than as a temporary investment) above the average paid-up capital on those shares.
- Liquidation distributions above average paid-up capital.
- Bonus shares, unless paid up; a partial repayment of paid-up capital while there is net profit, unless the shareholders resolved it beforehand and the nominal value was reduced by articles amendment.
- Payments on profit-sharing certificates and on hybrid capital and loans (Wet Vpb art. 10(1)(c) and (d)).
- Benefits in kind at market value (art. 3(2)). The inspector can fix the paid-up capital by decision on request (art. 13).

**Dividend tax: no withholding** (exemptions on the payer's side):
- **Domestic participation.** The recipient's holding qualifies for the participation exemption or credit and belongs to its Dutch business, or payer and recipient are in one fiscal unity (Wet DB art. 4(1)).
- **EU, EEA and treaty participation.** The recipient is an entity established in an EU or EEA state, or in a treaty state whose treaty has a dividend article, and its interest would qualify for the participation exemption if it were Dutch (Wet DB art. 4(2)). This does not apply if the recipient is treaty-resident in a third state without such a treaty, performs an investment-institution function, or holds the interest with a main purpose of avoiding tax on someone else through an artificial arrangement without valid business reasons reflecting economic reality (art. 4(3)).
- **Beneficial ownership.** Both exemptions apply only where the recipient shows it is the ultimate beneficial owner (art. 4(4)); dividend stripping arrangements are excluded (art. 4(7), (8)).
- **Safe harbour for the anti-abuse test.** The recipient is treated as holding the interest for valid business reasons, unless the inspector shows otherwise, if it meets all the substance conditions in Uitvoeringsbeschikking dividendbelasting 1965 art. 1bis: at least half of its statutory and decision-making directors live or are established in its home state and have the knowledge to do their job; qualified staff; board decisions taken, main bank accounts held and books kept in that state; wage costs of at least EUR 100,000 times the country factor in the annex; and an office with usual facilities available for at least 24 months (Wet DB art. 4(12)). If the conditions are not met, the recipient or the payer must show there is no main purpose of avoiding tax, or that there are valid business reasons.
- **Statement.** For the art. 4(2) exemption, the paying company must give the inspector a statement that the conditions are met within one month after making the dividend available (art. 4(11)). The Belastingdienst calls this the opgaaf dividendbelasting.
- **Exempt bodies.** Dutch legal persons not subject to Vpb, and EU/EEA bodies that are not subject to profit tax at home and would not be in the Netherlands, may be paid without withholding if they hold a qualification decision (kwalificatiebeschikking) and the payer has a copy when it pays (art. 4a(1), (6)). The decision lasts at most four years (art. 4a(7)).

**Conditional withholding tax: what counts.**
- Interest: all payments on loans owed by an affiliated withholding agent, including costs (Wet BB art. 3.3).
- Royalties: payments for copyrights (including software and films), patents, trademarks, designs, plans, secret formulas or processes, and know-how (art. 3.4).
- Dividends: the same items as Wet DB art. 3(1), paid by an affiliated Dutch withholding agent (art. 3.4a).
- Non-arm's-length terms are corrected to arm's length (art. 3.2).
- Timing: interest and royalties when paid, set off, made available, interest-bearing, or due and collectable; accrued but unpaid amounts are treated as received on 31 December. Dividends when made available (art. 3.5).
- **Credit for dividend tax.** The conditional withholding tax on a dividend is reduced by the dividend tax withheld on the same dividend (art. 5.2). The total on a dividend to a low-tax affiliate is therefore 25.8%, whatever the split.

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Withhold dividend tax | When the dividend is made available | Wet DB art. 7(3) |
| Dividend tax return and payment | Within 1 month after the day the dividend is made available | Belastingdienst, dividend tax return and payment; AWR art. 19(3) |
| Opgaaf for a fully or partly exempt participation dividend to a foreign shareholder (art. 4(2)) | Within 1 month after making the dividend available | Wet DB art. 4(11); Belastingdienst participation dividend page |
| Return when the whole dividend is exempt | No return, unless a qualification decision is used for a portfolio dividend, or the Belastingdienst invites a return | Belastingdienst, dividend tax return page |
| Treaty rate at source on a portfolio dividend | Shareholder hands the payer a completed IB 92 Universeel before the dividend is made available; upload with the return | Belastingdienst, portfolio dividend to a foreign shareholder |
| Treaty rate at source on a participation dividend (no art. 4(2) exemption) | Payer needs a permit (vergunning) from Belastingdienst Arnhem, Team dividendbelasting, applied for by letter, before applying the lower rate | Belastingdienst, participation dividend to a foreign shareholder |
| Refund to an exempt body (Wet DB art. 10) | Within 3 years after the end of the calendar year the dividend was made available | Uitvoeringsregeling AWR 1994 art. 21c(1) |
| Refund of the excess over Dutch tax for an EU/EEA or designated-state shareholder (Wet DB art. 10a) | Individuals: within 5 years after the end of the calendar year the dividend was made available. Companies: within 3 years after the end of the financial year it was made available. One claim per year, after the year ends | Uitvoeringsregeling AWR 1994 art. 21c(2), (3) |
| Treaty-based refund | The term depends on the basis of the claim. The Belastingdienst accepts claims within 5 years after the year the dividend was made available; a claim filed after a 3-year term but within 5 years is handled ex officio, with no right of objection | Belastingdienst, refund procedure |
| Dividend note (dividendnota) to the shareholder | When paid; not needed if no tax is withheld or the shareholder holds a substantial interest | Wet DB art. 9(1), (3) |
| Conditional withholding tax return and payment | Once a year, for the calendar year (also with a broken financial year), within 1 month after the year ends; for 2026, by 31 January 2027 | Belastingdienst, conditional withholding tax return; Wet BB art. 5.1(3); AWR art. 19(1) |
| Treaty exemption or reduced rate for conditional withholding tax | Needs a permit; exempt payments are reported on the form Opgaaf Bronbelasting renten, royalty's en dividenden | Belastingdienst, conditional withholding tax return |
| Correcting a wrong conditional withholding tax return | Tell the inspector within 2 weeks of finding out | Wet BB art. 6.3(1) |

Returns are filed through Mijn Belastingdienst Zakelijk, tax software, or a tax service provider. Both taxes are paid to NL04 RABO 0200 1818 90 with the return number, not to the account used for Vpb or VAT (Belastingdienst pages).

## Penalties and interest

| Default | Penalty | Source |
|---|---|---|
| Return filed late or not at all | Up to EUR 165 | AWR art. 67b(1) |
| Tax paid late, in part or not at all | Up to EUR 6,709 | AWR art. 67c(1) |
| No art. 4(11) statement or no dividend note | Up to EUR 6,709 | AWR art. 67ca(1)(c) |
| Late or short payment through intent or gross negligence | Up to 100% of the unpaid tax | AWR art. 67f |
| Not correcting a wrong conditional withholding tax return through intent or gross negligence | Up to 100% of the tax that would not have been levied | Wet BB art. 6.4 |

- An additional assessment (naheffingsaanslag) for conditional withholding tax can go to the withholding agent or to the taxpayer, reduced by dividend tax paid on the same dividend (Wet BB art. 6.1).
- The Belastingdienst says paying on time avoids a penalty and possibly tax interest (belastingrente). Rates are in [nl-corporate-tax](nl-corporate-tax.md).

## Cross-border points

**Foreign shareholders: three routes to a lower rate.**
1. **Exemption at source** for a qualifying corporate parent in the EU, EEA or a treaty state with a dividend article (Wet DB art. 4(2)), with the art. 4(3) anti-abuse test and the opgaaf.
2. **Treaty rate at source.** Portfolio dividend: the IB 92 Universeel before payment (residents of treaty states other than the US and Aruba; US pension funds use IB 96 USA with Form 6166). Participation dividend: a permit first.
3. **Refund after withholding.** Through the online form Teruggaaf dividendbelasting in Mijn Belastingdienst Zakelijk, after a one-time registration. An individual or company in the EU or EEA may also claim the excess of dividend tax over the Dutch tax a resident would have paid (Wet DB art. 10a(1)), as may a resident of a designated state with exchange of information, for portfolio investments only (art. 10a(2)); not where the home state gives a full treaty credit (art. 10a(5)). Bodies not subject to profit tax in the EU or EEA can claim a full refund (art. 10(2)); outside the EU or EEA only for portfolio investments from a designated state with exchange of information (art. 10(3)).

**Conditional withholding tax and treaties.**
- **Safe harbour for the abuse test (art. 2.1(1)(c)).** The same substance conditions as for dividend tax (Uitvoeringsregeling bronbelasting 2021 art. 2, including wage costs of at least EUR 100,000 times the country factor and an office for at least 24 months) shift the burden to the inspector (Wet BB art. 2.1(6)).
- A recipient in a listed state is outside the tax if it shows it is also resident in a non-low-tax state under that state's rules, is treated there as entitled to the payment, and is not treaty-resident in another state (Wet BB art. 2.1(2)).
- Where a treaty allows only the residence state to tax, or a reduced rate, the payer needs a permit to apply it (Belastingdienst).

**Non-resident companies with a Dutch permanent establishment.**
- **Who.** A non-Dutch entity comparable to a Dutch company is taxable on its Dutch income (Wet Vpb art. 3(1)). An entity comparable to a Dutch association, foundation or public body is taxable only if it runs a business (art. 3(3)).
- **Permanent establishment.** Where a treaty applies, the treaty definition; otherwise a fixed place of business through which the business is carried on, with a building or construction site counting only if it lasts more than 12 months (art. 3(4)). Storage, display, delivery, purchasing and information gathering are excluded if preparatory or auxiliary (art. 3(5)), unless the activities form part of a cohesive business with an affiliate (art. 3(6)). A dependent agent who habitually concludes contracts creates one (art. 3(8)); an independent agent does not, unless acting almost exclusively for affiliates (art. 3(9)).
- **Dutch income.** Taxable profit from a business carried on through a Dutch permanent establishment or permanent representative (art. 17(3)(a)), and income from a substantial interest in a Dutch company held in an abuse structure (art. 17(3)(b)). Dutch real estate and rights to it, profit shares in a business managed in the Netherlands (not from securities), receivables on a Dutch company in which it holds such a substantial interest, and director or supervisory board work for a Dutch body are treated as part of a Dutch business (art. 17a(a) to (d)), as are some North Sea activities and interests in a reverse hybrid (art. 17a(e) to (g)).
- **Computing the tax.** Tax is on the taxable Dutch amount: Dutch income less Dutch losses (art. 17(1), (2)). Profit follows the resident rules listed in art. 18(1). Losses offset one year back and forward, capped at EUR 1,000,000 plus 50% of the excess (art. 20(2)). The rates are the resident rates, 19% and 25.8% (art. 22).
- **No dividend tax on branch profit.** Dividend tax applies only to companies established in the Netherlands (Wet DB art. 1(1)), so moving profit from the branch to head office is not a dividend. Interest and royalties a non-resident pays that are charged to its Dutch permanent establishment can fall within the conditional withholding tax (Wet BB arts. 3.3(1)(b), 3.4(1)(b)).
- **Attributing profit to the permanent establishment.** The permanent establishment is taxed on the profit it would have earned as a separate, independent enterprise with the same functions, assets and risks: the Authorised OECD Approach (AOA) of the OECD report on the attribution of profits to permanent establishments. The Belastingdienst applies it in treaty cases and, for a non-resident with no treaty, by reference to the current OECD Model art. 7 (Besluit winstallocatie vaste inrichtingen 2022, paras. 1.3, 2.1, 2.2).
  1. Allocate assets and risks to the permanent establishment on a functional analysis, following where the significant people functions are carried out. Then allocate equity and debt; the Belastingdienst prefers the capital allocation approach, which gives the permanent establishment the same creditworthiness as the company as a whole (para. 2.2.1).
  2. Determine the permanent establishment's profit at arm's length, including its dealings with head office. Interest expense follows the fungibility approach: the company's interest is allocated pro rata to the debt allocated to the permanent establishment (para. 1.3).
  Transactions between the company and other group companies are priced at arm's length under Wet Vpb art. 8b, which applies to non-residents through art. 18(1). A group with consolidated revenue of at least EUR 50 million in the preceding year keeps a local file that also supports the profit allocation to permanent establishments (art. 29g(1), (3), (4)). Pricing method detail is in [netherlands-transfer-pricing](netherlands-transfer-pricing.md).
- **Filing.** The non-resident files a Vpb return; deadlines and extensions are in [nl-corporate-tax](nl-corporate-tax.md).

## Worked examples

**Example 1: portfolio dividend to an individual in a treaty country.** A Dutch BV pays a dividend of EUR 100,000 in 2026 to an individual shareholder who lives in a country whose treaty with the Netherlands caps Dutch dividend tax at 10%. The shareholder holds less than 5%, so it is a portfolio dividend. If the shareholder did not give the BV a completed IB 92 Universeel before the dividend was made available, the BV withholds 15%, EUR 15,000, and files and pays within one month. The shareholder then claims the EUR 5,000 above the treaty rate through Teruggaaf dividendbelasting. File by 31 December 2029 (3 years after 2026): the Belastingdienst handles a treaty claim filed after a 3-year term only ex officio, with no right of objection. If the shareholder did give the IB 92 Universeel in time, the BV withholds EUR 10,000 at source, uploads the form with its return, and no refund is needed. Either way the final Dutch tax is EUR 10,000 and the shareholder keeps EUR 90,000.

```oa-check
name: NL portfolio dividend EUR 100,000 to a treaty-country individual, 10% treaty rate (2026)
inputs:
  dividend: 100000
  dividend_tax_pct: 15
  treaty_pct: 10
steps:
  - withheld_without_form: dividend * dividend_tax_pct / 100
  - treaty_tax: dividend * treaty_pct / 100
  - refund: withheld_without_form - treaty_tax
  - net_after_refund: dividend - withheld_without_form + refund
  - net_with_form_at_source: dividend - treaty_tax
expected:
  withheld_without_form: 15000
  treaty_tax: 10000
  refund: 5000
  net_after_refund: 90000
  net_with_form_at_source: 90000
```

**Example 2: dividend to a 100% parent in a listed low-tax jurisdiction.** A Dutch BV pays a dividend of EUR 100,000 in 2026 to its 100% parent, a company established in the Cayman Islands, which is on the 2026 list (Regeling art. 2a(a)). The parent has a qualifying interest, so the BV is an affiliated withholding agent. Assume no Dutch treaty or arrangement with a dividend article covers the parent, so the art. 4(2) exemption is not available. The BV withholds 15% dividend tax, EUR 15,000, and files and pays within one month. It also owes conditional withholding tax of 25.8%, EUR 25,800, less the EUR 15,000 dividend tax, so EUR 10,800, declared on the annual return by 31 January 2027. Total Dutch tax is EUR 25,800 and the parent receives EUR 74,200. If no dividend tax were withheld on the dividend, there would be nothing to credit under Wet BB art. 5.2 and the conditional withholding tax would be the full EUR 25,800.

```oa-check
name: NL dividend EUR 100,000 to a 100% parent in a listed low-tax jurisdiction (2026)
inputs:
  dividend: 100000
  dividend_tax_pct: 15
  cwt_pct: 25.8
steps:
  - dividend_tax: dividend * dividend_tax_pct / 100
  - cwt_gross: dividend * cwt_pct / 100
  - cwt_due: cwt_gross - dividend_tax
  - total_dutch_tax: dividend_tax + cwt_due
  - net_to_parent: dividend - total_dutch_tax
expected:
  dividend_tax: 15000
  cwt_gross: 25800
  cwt_due: 10800
  total_dutch_tax: 25800
  net_to_parent: 74200
```

## Ask the client first

1. Who receives the payment: an individual or a company, where it is resident for tax, and whether that state is on the 2026 low-tax list or has a treaty with the Netherlands with a dividend article.
2. What percentage of the shares and votes the recipient holds, directly or through others, and whether anyone acting with it holds more.
3. Whether the recipient is the beneficial owner, and what substance and business reasons it has in its home state.
4. Whether the payer holds the shareholder's IB 92 Universeel, a kwalificatiebeschikking or a permit before the payment date.
5. What is being paid: an ordinary dividend, a buyback, a liquidation payment, a capital repayment, interest, or a royalty; and the paid-up capital on the shares.
6. For a foreign company: whether it has a fixed place, a construction site, a dependent agent, or Dutch real estate in the Netherlands.

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet op de dividendbelasting 1965, arts. 1, 3, 4, 4a, 5, 6, 7, 9, 10, 10a, 13 (version in force from 1 January 2025) | https://wetten.overheid.nl/BWBR0002515/2025-01-01 | 2026-10-23 |
| Wet bronbelasting 2021, arts. 1.2, 2.1, 3.1 to 3.5, 4.1, 4.2, 5.1, 5.2, 6.1, 6.3, 6.4 | https://wetten.overheid.nl/BWBR0042952/2026-01-01 | 2026-10-23 |
| Regeling laagbelastende staten en niet-coöperatieve rechtsgebieden voor belastingdoeleinden, art. 2a (2026) | https://wetten.overheid.nl/BWBR0041785/2026-01-01/0 | 2026-10-23 |
| Wet op de vennootschapsbelasting 1969, arts. 3, 8b, 17, 17a, 18, 20, 22, 29g | https://wetten.overheid.nl/BWBR0002672/2026-01-01 | 2026-10-23 |
| Algemene wet inzake rijksbelastingen, arts. 19, 67b, 67c, 67ca, 67f | https://wetten.overheid.nl/BWBR0002320/2026-10-01 | 2026-10-23 |
| Uitvoeringsregeling Algemene wet inzake rijksbelastingen 1994, art. 21c (refund terms for Wet DB arts. 10 and 10a) | https://wetten.overheid.nl/BWBR0006736/2026-01-01 | 2026-10-23 |
| Uitvoeringsbeschikking dividendbelasting 1965, art. 1bis (safe harbour for Wet DB art. 4(12)) | https://wetten.overheid.nl/BWBR0002517/2024-07-01 | 2026-10-23 |
| Uitvoeringsregeling bronbelasting 2021, art. 2 (safe harbour for Wet BB art. 2.1(6)) | https://wetten.overheid.nl/BWBR0044605/2024-01-01 | 2026-10-23 |
| Besluit winstallocatie vaste inrichtingen 2022, 14 June 2022, nr. 2022-0000143421, Stcrt. 2022, 16683 | https://zoek.officielebekendmakingen.nl/stcrt-2022-16683.html | 2026-10-23 |
| Belastingdienst, dividend tax when you pay a dividend | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert | 2026-10-23 |
| Belastingdienst, dividend tax return and payment | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert/dividendbelasting-aangifte-betalen | 2026-10-23 |
| Belastingdienst, portfolio dividend to a shareholder outside the Netherlands | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert/beleggingsdividend_uitkeren_aan_aandeelhouder_buiten_nederland | 2026-10-23 |
| Belastingdienst, participation dividend to a shareholder outside the Netherlands | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_uitkeert/deelnemingsdividend-uitkeren-aan-aandeelhouder-buiten-nederland | 2026-10-23 |
| Belastingdienst, refund procedure for portfolio dividends received abroad | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/dividendbelasting/als_u_dividend_ontvangt/ontvanger_dividend_in_buitenland_teruggaaf_dividendbelasting/ontvanger_beleggingsdividend_in_buitenland_teruggaafprocedure_dividendbelasting/ontvanger_beleggingsdividend_in_buitenland_teruggaafprocedure/ontvanger_beleggingsdividend_in_buitenland_teruggaafprocedure_dividendbelasting | 2026-10-23 |
| Belastingdienst, conditional withholding tax on interest, royalties and dividends | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/bronbelasting-rente-en-royalty/bronbelasting-op-renten-en-royalty | 2026-10-23 |
| Belastingdienst, conditional withholding tax return and payment | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/bronbelasting-rente-en-royalty/aangifte-doen-en-betalen-+bronbelasting | 2026-10-23 |

Not yet confirmed: which states have a treaty with the Netherlands containing a dividend article, and each treaty's dividend rate (the 10% in example 1 is an assumed treaty rate, and example 2 assumes no treaty covers the Cayman parent); the time limit for each treaty-based refund (3 or 5 years, by treaty); and how a non-resident individual's box 2 charge interacts with the dividend tax (see nl-cross-border).

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
