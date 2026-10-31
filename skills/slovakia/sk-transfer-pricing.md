---
name: sk-transfer-pricing
description: "Use this skill for Slovak transfer pricing (transferové oceňovanie) in tax year 2026. It covers dependent persons (závislá osoba, Income Tax Act § 2(n) to (r), the 25% test), significant controlled transactions (over EUR 10,000, or loans over EUR 50,000 principal), the arm's length adjustment in § 17(5), corresponding adjustments in § 17(6), methods and the median rule in § 18(1), full, basic and shortened documentation under Ministry of Finance guideline MF/012879/2025-724 and who keeps which, Table I of the corporate return, the 15-day deadline to hand documentation over, penalties and late payment interest under the Tax Code, country-by-country reporting (EUR 750 million) and APAs under § 18(4) to (10). Trigger on: transfer pricing Slovakia, transferové oceňovanie, závislá osoba, kontrolovaná transakcia, transferová dokumentácia, APA Slovakia. Out of scope: corporate tax in general (sk-corporate-income-tax), individual income tax (slovakia-pit), VAT (slovakia-vat-return)."
version: 0.3
jurisdiction: SK
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovakia: transfer pricing (2026) v0.3

> **Source-cited draft.** No accountant has reviewed this skill yet. The law comes from the consolidated texts on Slov-Lex, the guideline from the Ministry of Finance (mfsr.sk) and the return guidance from the Financial Directorate (financnasprava.sk), read on 23 October 2026 and supplemented by the 27 October 2026 primary checks below. It prepares working papers; it is not authority to file or pay.

This is the transfer pricing (TP) skill for the Slovak pack. It links rather than repeats:

- Corporate income tax, the base, the return and its deadlines: [sk-corporate-income-tax](sk-corporate-income-tax.md) (2026).
- Individual income tax, including sole traders with § 6 income: [slovakia-pit](slovakia-pit.md).
- VAT: [slovakia-vat-return](slovakia-vat-return.md). Overview: [sk-tax-overview](sk-tax-overview.md).

The law is Act No. 595/2003 Z. z. on Income Tax ("ITA", version in force from 1 January 2026) and Act No. 563/2009 Z. z. on Tax Administration, the Tax Code (daňový poriadok, "TC", version in force from 1 September 2026). Currency: euro (EUR).

## Who this applies to

**Any taxpayer that is a dependent person and has a significant controlled transaction.** The rule in ITA § 17(5) applies to companies and to individuals with business income under § 6, residents and non-residents.

**Dependent persons (závislé osoby), ITA § 2(n) to (r):**

- **Close persons** (blízke osoby, Civil Code §§ 116 and 117) (§ 2(n)(1)).
- **Economically, personally or otherwise linked persons** (§ 2(n)(2)):
  - **Economic link** (§ 2(o)(1)): a direct, indirect or derived indirect share of at least 25% of the registered capital, of the voting rights or of the profit. An indirect share is the product of the direct shares. A derived indirect share is the sum of indirect shares; above 50%, every person in the chain counts as economically linked whatever its own share. Persons acting together on votes or capital count as holding all of it. Shares of close persons are added together, and 25% in total makes them linked.
  - **Personal link** (§ 2(o)(2)): members of the statutory, supervisory or similar bodies of a legal person, in relation to that legal person. Persons under the control or management of the same person, or of its close person, are linked to each other (§ 2(o)).
  - **Other link** (§ 2(p)): a legal or similar relationship set up mainly to reduce the tax base or increase a tax loss.
- **Members of a consolidated group** for consolidation purposes under Accounting Act § 22 (§ 2(n)(3)).
- **Permanent establishments** (§ 2(r)): a resident and its foreign PEs, a non-resident and its Slovak PE, PEs of the same taxpayer, and PEs of linked taxpayers all count as economically linked.

**Controlled transaction** (kontrolovaná transakcia, § 2(ab)): a legal or similar relationship between two or more dependent persons where at least one is an individual with § 6 business income or a legal person with taxable income from activity or from its assets. Two things are not controlled transactions: employment income under § 5, and the rent of a property outside business assets let to an individual for personal use. The real substance of the relationship counts.

**Significant controlled transaction** (§ 17(5)(a)): a transaction or group of transactions on which one or more dependent persons book taxable income or a tax expense above EUR 10,000 in the period, and any loan with principal above EUR 50,000. A loan above EUR 50,000 stays significant for its whole life, even after repayments take the balance below that (Financial Directorate, 12/PO/2026/IM, example 2). Transactions that are not significant are outside §17(5). In the current form, non-significant transactions not included in an aggregated significant group are declared by the part 3 flag rather than itemised in part 1 of Table I; the former DPPOv25 treatment is retained below with its historical vintage.

**Domestic deals count too.** The guideline has separate rules for cross-border and domestic significant controlled transactions (MF/012879/2025-724, art. 2(8) and (9)), and Table I takes both (12/PO/2026/IM).

**Micro-taxpayers.** A micro-taxpayer (mikrodaňovník, revenue up to EUR 60,000) loses that status if it is a dependent person with a controlled transaction in the period (ITA § 2(w)(1)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Corporate income tax rate (applies to any TP adjustment of a company) | 10% if taxable revenue is up to EUR 100,000; 24% if taxable revenue is above EUR 5,000,000; 21% otherwise | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 15(b)(1)) |
| Dependent person: economic link | at least 25% of capital, voting rights or profit, direct, indirect or derived indirect | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 2(o)(1)) |
| Significant controlled transaction | income or expense above EUR 10,000 in the period; any loan with principal above EUR 50,000 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 17(5)(a)) |
| Full documentation: cross-border transaction value | above EUR 10,000,000 in the period | periods whose return deadline falls after 31 Dec 2025 | https://www.mfsr.sk/files/archiv/49/Usmernenie-2025.pdf (art. 3(1)(b)) |
| Basic documentation: cross-border transaction value | above EUR 1,000,000 in the period | same | https://www.mfsr.sk/files/archiv/49/Usmernenie-2025.pdf (art. 3(2)(b)) |
| Basic documentation: taxpayer's total revenue from operating and financial activity | above EUR 8,000,000 (with a material cross-border transaction) | same | https://www.mfsr.sk/files/archiv/49/Usmernenie-2025.pdf (art. 3(2)(a)) |
| Historical Table I of the corporate return | up to 99 rows electronically (18 on paper) | DPPOv25, deadlines from 1 Jan through 31 Dec 2026; current form below | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Aktualne/DP/DPPO/2026/2026.03.26_012_PO_2026_IM.pdf |
| Deadline to hand over documentation on request | 15 days from delivery of the request | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 18(11)) |
| APA fee: unilateral | EUR 10,000 (half for a taxpayer rated highly reliable) | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 18(7)) |
| APA fee: bilateral or multilateral | EUR 30,000 (half for a taxpayer rated highly reliable) | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 18(7)) |
| APA term | up to 5 periods, renewable for up to 5 more; longer if the competent authorities agree it | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 18(4) and (5)) |
| Penalty on tax increased by the tax office | 3 times the ECB base rate a year, at least 10% a year; at least 1% of the amount, at most 100% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html (§ 155(1)(f), (2), (5)) |
| Penalty on tax disclosed in a supplementary return | the ECB base rate a year, at least 3% a year (2 times, at least 7%, if filed within the §16(9) 15-day window after the audit record or relevant notice) | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html (§ 155(1)(g), (h), (5)) |
| Penalty for a missed non-monetary duty (for example documentation not handed over) | EUR 100 to EUR 10,000; a fine for a breach under § 154(1)(j) can be repeated while it lasts | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html (§ 154(1)(d), (j); § 155(1)(e), (16)) |
| Late payment interest | 4 times the ECB base rate a year, at least 15% a year, for at most 4 years | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html (§ 156(2)) |
| ECB base rate (main refinancing operations) | 2.15% from 11 June 2025; 2.40% from 17 June 2026; 2.65% from 16 September 2026 | 2026 | https://nbs.sk/en/statistics/financial-markets/interest-rates/ecb-key-interest-rates/ |
| Country-by-country report: group consolidated revenue in the prior year | EUR 750,000,000 or more | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2012/442/20260101.html (§ 22a(h)) |
| Country-by-country report: fines | up to EUR 10,000 for not filing the report; up to EUR 3,000 for a missed notice; both can be repeated | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2012/442/20260101.html (§ 22g(2)) |
| Time limit to assess tax | 5 years from the end of the year the return was due; restarts on an audit report, 10 years at most; 10 years where a tax treaty is applied | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html (§ 69) |

At the ECB base rate of 2.65%: 3 times is 7.95%, so the 10% floor applies to an audit penalty. 1 times is 2.65%, so the 3% floor applies to a supplementary return penalty. 4 times is 10.6%, so the 15% floor applies to late payment interest.

## The taxable base

**The adjustment is one-way.** The base of a dependent person includes the difference by which prices or terms in significant controlled transactions depart from those between independent persons in comparable transactions. This applies only where the difference reduces the base or increases a tax loss (ITA § 17(5)(a)). The tax then follows at the taxpayer's own rate (§15). Recalculate that rate after the correction, using taxable revenue rather than the tax base. An income-side TP correction, such as increasing an undercharged sale, enters taxable revenue even if not booked; an expense-side addback, such as the excess management fee or royalty in the examples, increases the base without itself increasing taxable revenue. The Financial Directorate's [taxable-revenue methodology, p.2 item 3 and expense exclusions](https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Metodicke_usmernenia/Priame_dane/2021/2021.02.11_18_DZPaU_2021_MU.pdf) explains that distinction; its historical rate and threshold are not the 2026 rates. Use current §15(b)(1): 10% through EUR 100,000 taxable revenue, 21% above that through EUR 5,000,000, and 24% above EUR 5,000,000, each on the entire ordinary base after loss relief. Compute extra tax as corrected tax less original tax, not invariably adjustment times the old rate. The exact-threshold values still take the lower rate.

**Shared costs.** A dependent person may deduct its share of costs that a related person incurred, but only if all four tests are met (§ 17(5)(b)):

1. the costs demonstrably relate to its business;
2. it would pay for the service if an independent person supplied it, or it would do the work itself;
3. it can show the total costs and how they are split among those who benefit;
4. its share is booked in its accounts or tax records.

**Materiality for documentation tier selection.** Where guideline art. 3 relies on Accounting Act §17(9), information is material if omitting it or stating it incorrectly could affect a financial-statement user’s judgement or decision. Assess the item in the context of those statements; this is not an extra universal euro threshold replacing the guideline’s actual tests ([Accounting Act §17(9)](https://static.slov-lex.sk/static/SK/ZZ/2002/431/20260101.html#paragraf-17); [guideline art.3](https://www.mfsr.sk/files/archiv/49/Usmernenie-2025.pdf)).

**Methods** (§ 18(1) to (3)). The law names five methods:

- price methods: comparable uncontrolled price, resale price and cost plus;
- profit methods: profit split and transactional net margin.

A taxpayer may combine them or use another method, but only one that respects the arm's length principle. The OECD Transfer Pricing Guidelines also apply. The comparison looks at functions, risks, the asset or service, contract terms, the market and business strategy.

**The median rule** (§ 18(1)). Where the tax office compares against several independent values and the taxpayer's value is outside arm's length, an audit adjusts to the median of those values. The base goes to another point in the range only if the taxpayer shows that point fits the facts better.

**Corresponding adjustment** (§ 17(6)). Where a treaty partner's tax authority adjusts a related person's base in line with arm's length, the tax office that the Financial Directorate names on its website may allow a matching downward adjustment in Slovakia. Where one Slovak dependent person adjusts its base upward under § 17(5), the other Slovak dependent person may adjust its base the other way. It must adjust where it claims investment aid or incentive relief under § 30a or § 30b. It must also file a notice of the adjustment with its return or supplementary return.

**Permanent establishments** (§ 17(7)). A Slovak PE of a non-resident may not show a lower base, or a higher loss, than an independent enterprise doing the same work. § 18 applies to it, and the non-resident must keep documentation on the method.

**Interest on related-party loans.** Besides the arm's length test, interest on loans from dependent persons is not deductible above 25% of profit before tax plus depreciation and interest expense (§ 21a(1)). Banks, insurers and leasing companies are outside this rule (§ 21a(3)). § 21a does not apply where the taxpayer already increased its base under the interest limitation rule in § 17k, which adds back net interest costs above 30% of the adjusted base once they exceed EUR 3,000,000 (§ 17k(2), § 21a(4)). The corporate skill covers the base around it.

## Deadlines and filing

**Corporate return.** Due within 3 calendar months after the end of the tax period, with the tax paid by the same date (ITA § 49(2)). A notice filed by the deadline extends it by up to 3 full months, or up to 6 months if the taxpayer has foreign-source income (§ 49(3)).

**Current Table I: choose the form by the return's filing deadline.** The corporate form MF/014309/2026-721 applies where that deadline falls after 31 December 2026, including an ordinary calendar-2026 return due in March 2027. The earlier MF/012187/2025-721 (DPPOv25) applies where the deadline fell no later than 31 December 2026, including the 2025 return in example 2. These vintages come from [Financial Directorate 14/DZPaU/2026/I, pp.1 and 4–5](https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Novinky_leg/Priame_dane_uct/2026/2026.10.22_014_DZPaU_2026_I.pdf).

The current Table I covers domestic and foreign significant controlled transactions or groups whatever their documentation tier, including a Slovak PE's dealings with its head office. It has three parts:

1. **Significant transactions/groups:** give the sequence number, transaction code, aggregation flag, §2(r) PE-relationship flag, effect on the tax base at return row 400, counterparty residence-country code and name (or the individual's name). The tax-base effect replaces the former accounting-result/row-301 measure; do not automatically copy the acquisition price of an asset into that column.
2. **Related-party loans held during the period:** give the sequence number and loan code, highest principal during the period and year-end balance, and the related person's residence-country code and name. An interest-free loan therefore still has principal information here; it no longer disappears merely because no interest affects the base.
3. **Smaller transactions:** mark transactions below the §17(5)(a) significance level that are not already included in an aggregated group in part 1.

Significant transactions omitted for lack of rows go into shortened documentation. Full/basic files remain separately required where their tests apply, alongside the completed return and Table I. Where shortened documentation applies, a properly completed current return including Table I meets that duty. The current Table L also reconciles booked revenue in row 1 through the descriptions, amounts and associated return-row references in rows 2–98 to taxable revenue in L99, transferred to return row 560; use that reconciliation when a TP income correction changes a rate threshold (FS14, pp.3–5).

**Historical DPPOv25 method retained for its proper vintage (12/PO/2026/IM).** One row per transaction/group, split by counterparty and code; column 3 measured the effect on accounting result at row 100, in euros and cents with costs negative, including current and future effects. Under that old instruction a EUR 2,000,000 related-party building purchase was shown at EUR 2,000,000 in the purchase year rather than that year's depreciation. Loan interest went under code 22, principal was not reported and an interest-free loan put nothing in the old Table I; the shortened file then covered what the return did not document and §17(5) still applied. A taxpayer with only non-significant transactions did not itemise them, but ticked the part-I relationship box under §2(n). The old form allowed 99 electronic rows (18 on paper); if insufficient, the lowest-value transactions were left out and documented separately. These are historical controls, not instructions for the new three-part table.

**Documentation** (ITA § 18(1) and § 17(7); Ministry of Finance guideline MF/012879/2025-724). A taxpayer must keep documentation on its controlled transactions and the method used. The guideline sets the minimum content, and the tax office may ask for more (art. 2(2)). It applies to documentation for periods whose return deadline falls after 31 December 2025, so to 2025 and 2026 (art. 9). The tests are applied period by period (art. 2(1)). For a loan or other financial transaction, the value is the highest principal during the period (art. 2(7)).

| Tier | Who keeps it (art. 3) | Content |
|---|---|---|
| **Full** (úplná) | (a) a cross-border significant transaction material under Accounting Act § 17(9) for a taxpayer that reports under IFRS; (b) a cross-border transaction or group above EUR 10,000,000; (c) a material cross-border transaction with a resident of a non-cooperative state; (d) a material cross-border transaction where the taxpayer claims regional investment aid relief; (e) a transaction covered by an APA request; (f) a transaction covered by a request for a corresponding adjustment, except domestic ones; (g) a transaction covered by a dispute resolution request | Group file (structure, business, profit drivers, supply chains, services, intangibles, financing, consolidated accounts, APAs and rulings) and local file (taxpayer, each transaction with value by counterparty, contract, functional analysis, method and why, tested party, comparables and adjustments, reconciliation to the accounts) (art. 4) |
| **Basic** (základná) | where full does not apply: (a) a material cross-border transaction where the taxpayer's total revenue from operating and financial activity exceeds EUR 8,000,000; (b) a cross-border transaction or group above EUR 1,000,000; (c) a material domestic transaction where the taxpayer claims regional investment aid relief; (d) any cross-border transaction with a resident of a non-cooperative state | Short group file (members, structure, functions, risks, financing) and local file (taxpayer, each transaction with value, contract, functional analysis, description of the TP system) (art. 5) |
| **Shortened** (skrátená) | everyone else | Met by a properly completed return including Table I. A taxpayer that does not meet it that way, for example for lack of rows, keeps the shortened file in the form annexed to the guideline (art. 3(3), art. 6) |

- A Slovak PE also describes how capital and funding costs are attributed to it if it deducts funding costs (art. 7).
- No documentation under full or basic is needed for transactions with no effect on the base in the period, except loans (art. 3(4)).
- Documentation may roll forward from earlier periods if nothing that affects pricing has changed (art. 2(5)).
- Taxpayers linked only through the state or a municipality document only their dealings with that public owner and its bodies (art. 8).

**Handing documentation over.** The tax office or the Financial Directorate may ask for it. The taxpayer must hand it over within 15 days from delivery of the request. The request for a period cannot be sent before the day after that period's return deadline. Documentation may be in another language, but on request a Slovak version is due within 15 days of delivery (ITA § 18(11)). Documentation goes in with any request for a corresponding adjustment or a mutual agreement procedure (§ 18(13)). Keep it for as long as tax can be assessed (§ 18(12); TC § 69).

**APA** (rozhodnutie o odsúhlasení použitia metódy ocenenia, ITA § 18(4) to (10)):

- Apply in writing to the tax office the Financial Directorate names, at least 60 days before the start of the first period the method is to cover. A late application counts as not filed and the fee is refunded (§ 18(4), (8)).
- The application includes the documentation and: the parties, the periods, a description of the transaction, its expected value and the proposed method (§ 18(6)). Full documentation applies to the transaction (guideline art. 3(1)(e)).
- The fee is paid with the application: EUR 10,000 unilateral, EUR 30,000 bilateral or multilateral, halved for a taxpayer rated highly reliable under the tax reliability index (§ 18(7)). If the request is rejected, the fee is not refunded.
- The APA covers up to 5 periods. A renewal for up to 5 more can be requested at least 60 days before it expires, if the conditions have not changed (§ 18(4)). A bilateral APA can cover more periods, including periods not in the request, if the competent authorities agree (§ 18(5)).
- No appeal lies against the decision (§ 18(9)). The office revokes it if it rests on wrong data, and revokes or changes it if material conditions change (§ 18(10)).
- A Slovak PE can get an APA on attributing its base too (§ 17(7)).

**Supplementary return.** A taxpayer that finds its tax should be higher must file by the end of the month following discovery; the newly declared difference is due on that same date (TC §16(2)). The §16(9) audit window is 15 days from the audit-start record, delivery of the audit notice, or delivery of a notice extending the audit to the relevant period or tax. After that window, a supplementary return is barred until the assessment becomes final, or until the audit ends if no assessment proceedings begin. §16(7) separately bars filing after delivery of a notice of tax determination by estimation (podľa pomôcok), for a period already so determined, or after issue of an assessment order (vyrubovací rozkaz). Retain the actual notice and delivery dates; the physical start of fieldwork is not the only trigger ([TC §16](https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html#paragraf-16)).

**Country-by-country reporting** (Act No. 442/2012 Z. z., §§ 22a to 22g). It applies to multinational groups with consolidated revenue of EUR 750,000,000 or more in the prior year (§ 22a(h)).

- A Slovak ultimate parent files the report within 12 months after the end of the reporting year (§ 22b(1)). A Slovak constituent entity files it instead only in the cases in § 22c (the parent's state does not require it, has no exchange agreement, or has failed).
- Every Slovak constituent entity notifies who files and names the group and its parent, by the last day of its own return deadline for that year. The notice is needed again only when the facts change (§ 22e).
- The tax office may not adjust the base on the report's data alone (§ 22f(3)).

## Penalties and interest

- **Audit adjustment.** When the tax office raises tax in an assessment, the penalty is 3 times the ECB base rate a year, at least 10% a year, on the increase (TC § 155(1)(f), (5)). It runs from the day after the return deadline or tax due date to the applicable statutory endpoint in the table below. It is at least 1% of the amount and at most the amount (§ 155(2)). The ECB rate used is the one on the day the assessment is delivered (§ 155(7)). Paying the assessed amount within 15 days of delivery cuts the penalty to two thirds (§ 155(17)).
- **Doubled penalty for abuse.** Where the office adjusts under § 17(5)(a) and also applies the anti-abuse rule (ITA § 50a or TC § 3(6)), the penalty is doubled (ITA § 18a(1)). The doubling falls away if the taxpayer does not appeal and pays within the appeal period (§ 18a(2)).
- **APA requested.** Where the taxpayer asked for an APA and the office audits the period of the request or the two periods before it, an adjustment without abuse carries the lower penalty under TC § 155(1)(g) (ITA § 18a(3)).
- **Self-correction.** Tax disclosed in a supplementary return carries a penalty of the ECB base rate a year, at least 3% a year, on the difference (TC § 155(1)(g), (5)). It runs from the day after the original return deadline or tax due date through the supplementary filing day (§155(2)). The rate is twice the ECB rate, at least 7%, if filed within the §16(9) window after the audit record or relevant notice (§155(1)(h)). Both self-correction rates also have the §155(2) minimum of 1% and maximum of 100% of the relevant amount; later supplementary returns use the difference from the preceding supplementary return (§155(6)).
- **Documentation not handed over, or another non-monetary duty missed.** EUR 100 to EUR 10,000 (TC § 154(1)(j), § 155(1)(e)). The fine can be imposed again in the same amount if it did not lead to a remedy and the breach lasts (§ 155(16)). A tax office does not impose a fine set within a range for a first breach (§ 155(4)).
- **Late payment interest.** First establish the payment's own due date under the statute or assessment: §156(1) charges interest only if that date or required amount is missed. A difference newly declared under §16(2) and paid by its end-of-following-month due date has no late-payment interest merely because it corrects an earlier return; the separate §155 penalty still runs from the original deadline. For an overdue amount, use 4 times the ECB main-refinancing rate on the date arrears arose, at least 15% a year, from the next day after its due date through payment inclusive, use of an overpayment, or compensation under §55. §156(2) specifically cuts interest on an existing overdue balance at the supplementary filing date; this does not turn the newly declared difference into an arrear before its own due date. Keep those balances and dates separate. The maximum is four years. The [official interest calculation method](https://www.financnasprava.sk/sk/elektronicke-sluzby/verejne-sluzby/danove-kalkulacky/urok-z-omeskania) confirms the reference date and endpoints; the [supplementary-return guidance](https://podpora.financnasprava.sk/901749-Dodato%C4%8Dn%C3%A9-da%C5%88ov%C3%A9-priznanie) confirms its payment deadline. Interest of EUR 5 or less is not assessed by the tax/customs office (§156(6)(b)).
- **Country-by-country reporting.** Up to EUR 10,000 for not filing the report, and up to EUR 3,000 for a missed notice, both repeatable (Act 442/2012, § 22g(2)).
- **Time limit.** Tax can be assessed for 5 years from the end of the year in which the return was due. An audit report restarts the period, but never beyond 10 years (TC § 69(1) to (3)). Where a tax treaty is applied, the limit is 10 years (§ 69(5)).

For §155(1)(f)–(h) daily penalties, apply the endpoint that belongs to the procedure (§155(2)):

| Procedure | Last counted day |
|---|---|
| Voluntary supplementary return | Actual supplementary filing day |
| Audit followed by an assessment | Expiry of the applicable §16(9) 15-day supplementary-filing window |
| Tax determined by estimation (podľa pomôcok) | Delivery of the estimation notice |
| Assessment order (vyrubovací rozkaz) | Day tax is assessed by that order |

Split calculations across calendar years using 365 or 366 days for each year. Apply the 1% minimum and 100% maximum to the §155 daily penalty, and round the penalty and §156 interest down to tens of eurocents under §161. Use the actual statutory ECB reference date; the observed history above does not establish a later 2027 or 2028 rate. Separately apply [§155(11)](https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html#paragraf-155): the tax/customs office does not impose a fine of EUR 5 or less; the corresponding municipal limit is EUR 3. For example, a computed supplementary-return fine rounded to EUR 5.00 is not imposed, while EUR 5.10 exceeds the tax/customs non-imposition limit. This is the fine rule, separate from §156(6)'s late-interest threshold.

## Cross-border points

- **Treaties and MAP.** A double taxation case from a TP adjustment can go to the mutual agreement procedure under the treaty's associated enterprises article, or to the EU Arbitration Convention 90/436/EEC. The documentation goes in with the request (ITA § 18(13)). EU disputes can also go under Act No. 11/2019 Z. z. on tax dispute resolution, and full documentation then applies to the transaction (guideline art. 3(1)(g)).
- **Corresponding adjustment after a foreign adjustment.** Allowed only where the other state has a tax treaty with Slovakia and its adjustment is arm's length (ITA § 17(6)). Full documentation applies (guideline art. 3(1)(f)).
- **Non-cooperative states.** A cross-border transaction with a resident of a non-cooperative state needs at least basic documentation whatever its size, and full documentation if it is material (guideline art. 3(1)(c), 3(2)(d)). The list of cooperating states is on the Ministry of Finance website (ITA § 2(x)).
- **Permanent establishments.** Head office dealings with a Slovak PE are controlled transactions (§ 2(r)) and go in Table I. Attribution of profit follows § 17(7).
- **Withholding.** Whether an adjusted amount paid abroad is treated as a dividend or other payment subject to withholding is not covered by this skill (see Not yet confirmed).

## Worked examples

### Example 1: the tax office cuts a management fee paid to a foreign parent

A Slovak s.r.o. has taxable revenue of EUR 3,000,000 in 2026, so its rate is 21%. It pays its Austrian parent a management fee of EUR 250,000 and deducts it in full. Its benchmark gives a range of independent fees with a median of EUR 180,000, and the fee sits above the range. In an audit that starts in June 2028, the office adjusts to the median.

1. Documentation check: the fee is cross-border and above EUR 10,000, so it is significant. The company does not report under IFRS, claims no regional investment aid and Austria is not a non-cooperative state. The fee is below EUR 1,000,000 and the company's revenue is below EUR 8,000,000, so neither full nor basic documentation applies (guideline art. 3(1) and (2)). Table I in the 2026 return meets the duty (guideline art. 3(3)).
2. Adjustment to the median: EUR 250,000 less EUR 180,000 = EUR 70,000 (ITA § 17(5)(a), § 18(1)).
3. Extra tax at 21%: EUR 14,700.
4. Penalty: the ECB rate used is the one on the day the assessment is delivered (TC § 155(7)). The example assumes it is still 2.65%: 3 times is 7.95%, so the 10% floor applies (§ 155(5)). The floor stops applying only if the ECB rate rises above 10/3% (3⅓%). It runs from 1 April 2027 (the day after the 31 March 2027 deadline) to 30 June 2028, the date the § 16(9) window is assumed to close: 457 days. Split the calendar years: 275 days in 2027 over 365, and 182 days in leap year 2028 over 366. Raw penalty is `14,700 × 10% × (275/365 + 182/366) = 1,838.517853…`; Tax Code §161 rounds it down to tens of eurocents, giving EUR 1,838.50. That exceeds the 1% minimum of EUR 147.
5. Paying within 15 days of the assessment cuts the penalty to two thirds: EUR 1,225.60 after the same §161 downward rounding (§155(17)).
6. Late payment interest is separate: establish whether and when an amount is unpaid after its applicable payment due date. It is not computed here because the payment due date, payment date and ECB rate on the date any arrears arise are scenario facts not supplied; the penalty calculation alone does not establish interest.
7. To relieve the double tax, the parent asks Austria for a corresponding adjustment through the treaty's mutual agreement procedure or the EU Arbitration Convention.

```oa-check
name: Management fee cut to the median, audit penalty at the 10% floor (2026)
inputs:
  fee_paid: 250000
  median_fee: 180000
  cit_rate: 21
  penalty_rate: 10
  days_2027: 275
  days_2028: 182
  year_2027: 365
  year_2028: 366
steps:
  - adjustment: fee_paid - median_fee
  - extra_tax: adjustment * cit_rate / 100
  - raw_penalty: extra_tax * penalty_rate / 100 * (days_2027 / year_2027 + days_2028 / year_2028)
  - penalty: floor(raw_penalty * 10) / 10
  - penalty_paid_early: floor(penalty * 2 / 3 * 10) / 10
  - minimum_penalty: extra_tax / 100
expected:
  adjustment: 70000
  extra_tax: 14700
  penalty: 1838.50
  penalty_paid_early: 1225.60
  minimum_penalty: 147
```

### Example 2: a large company corrects a royalty itself and checks its documentation tier

A Slovak a.s. has taxable revenue of EUR 9,000,000, so its rate is 24%. In 2025 it paid its Dutch sister company royalties of EUR 1,200,000 for a licence. It also borrowed EUR 60,000 at a market rate from a Slovak sister company. In October 2026 its new benchmark shows the arm's length royalty for 2025 was EUR 1,080,000. It files a supplementary return on 30 November 2026, before any audit.

1. Documentation tier for 2025: the royalty is cross-border and above EUR 1,000,000, so basic documentation is needed. It is not above EUR 10,000,000, the company does not report under IFRS, and the sister company is not in a non-cooperative state, so full documentation is not (guideline art. 3(1) and (2)).
2. The Slovak loan has principal above EUR 50,000, so it is significant. It is domestic and the company claims no investment aid, so the interest goes in Table I and no separate file is needed.
3. Excess royalty: EUR 1,200,000 less EUR 1,080,000 = EUR 120,000, added back (ITA § 17(5)(a)).
4. Extra tax at 24%: EUR 28,800, paid by the end of the month after the month the company found the error (TC § 16(2)).
5. Penalty: the ECB rate used is the one on the day the supplementary return is filed (TC § 155(7)). Assume it is 2.65% on the future 30 November 2026 filing date; this is a scenario input, not a rate observed at the 27 October read date. It is below 3%, so the 3% floor applies (§155(5)). It runs from 1 April 2026, the day after the 31 March 2026 deadline, to 30 November 2026: 244 days. Raw penalty is `28,800 × 3% × 244 / 365 = 577.578082…`; §161 downward rounding to tens of eurocents gives EUR 577.50.
6. Assume the original declared tax was paid on time and the additional EUR 28,800 is paid by 30 November 2026. Late-payment interest is zero: that is the §16(2) due date for this newly declared difference. If it is instead paid on 10 December, interest runs 1–10 December inclusive, ten days. Assuming the ECB rate when arrears arise remains low enough for the 15% floor, `28,800 × 15% × 10 / 365 = 118.356164…`, rounded down under §161 to EUR 118.30. That future rate is an explicit scenario assumption, not an observed December rate.
7. Had the office found it on audit instead, the 10% floor would apply over the applicable audit period in the endpoint table (TC §155(1)(f), (2)); count the actual dates rather than assume a fixed duration.

**Rate-cliff checks within the same correction method.** The royalty addback is an expense correction and does not change EUR 9,000,000 taxable revenue. Contrast an undercharged sale: taxable revenue of EUR 99,500, an ordinary base after loss relief of EUR 20,000 and a EUR 1,000 income-side TP increase produce EUR 100,500 revenue and EUR 21,000 base. Original tax is `20,000 × 10% = 2,000`; corrected tax is `21,000 × 21% = 4,410`; extra tax is EUR 2,410. At the upper cliff, EUR 4,999,500 revenue and EUR 200,000 base plus the same EUR 1,000 income correction give EUR 5,000,500 revenue, EUR 201,000 base and extra tax of `201,000 × 24% − 200,000 × 21% = 6,240`. At exactly EUR 100,000 or EUR 5,000,000 revenue the lower respective rate remains. These variants assume no other relief or minimum-tax effect (§15(b)(1); revenue classification source above).

```oa-check
name: Royalty self-correction at 24%, supplementary return penalty at the 3% floor (2025 return, corrected 2026)
inputs:
  royalty_paid: 1200000
  royalty_alp: 1080000
  basic_doc_threshold: 1000000
  cit_rate: 24
  penalty_rate: 3
  days: 244
  days_in_year: 365
  late_days_variant: 10
  late_interest_rate_assumed: 15
  small_revenue_before: 99500
  small_base_before: 20000
  large_revenue_before: 4999500
  large_base_before: 200000
  income_adjustment_variant: 1000
steps:
  - add_back: royalty_paid - royalty_alp
  - over_basic_threshold: royalty_paid - basic_doc_threshold
  - extra_tax: add_back * cit_rate / 100
  - raw_penalty: extra_tax * penalty_rate / 100 * days / days_in_year
  - penalty: floor(raw_penalty * 10) / 10
  - late_interest_variant: floor(extra_tax * late_interest_rate_assumed / 100 * late_days_variant / days_in_year * 10) / 10
  - small_revenue_after: small_revenue_before + income_adjustment_variant
  - small_tax_before: small_base_before * 10 / 100
  - small_tax_after: (small_base_before + income_adjustment_variant) * 21 / 100
  - small_extra_tax: small_tax_after - small_tax_before
  - large_revenue_after: large_revenue_before + income_adjustment_variant
  - large_extra_tax: (large_base_before + income_adjustment_variant) * 24 / 100 - large_base_before * 21 / 100
expected:
  add_back: 120000
  over_basic_threshold: 200000
  extra_tax: 28800
  penalty: 577.50
  late_interest_variant: 118.30
  small_revenue_after: 100500
  small_tax_before: 2000
  small_tax_after: 4410
  small_extra_tax: 2410
  large_revenue_after: 5000500
  large_extra_tax: 6240
```

## Ask the client first

1. Who the dependent persons are: the ownership chain with percentages of capital, votes and profit (direct, indirect and derived), shared board members, close persons, and the consolidated group.
2. Which transactions there were with each one in the period, by type, amount and country, and which pass EUR 10,000, or are loans above EUR 50,000 principal.
3. The company's total revenue from operating and financial activity, whether it reports under IFRS, and whether it claims regional investment aid. These set the documentation tier.
4. Whether any counterparty is a resident of a non-cooperative state.
5. How each price was set: the method, any benchmark and the median, and whether a group master file and local file exist.
6. Whether the group's consolidated revenue reached EUR 750 million, and whether any APA, MAP or tax audit is open.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 595/2003 Z. z. on Income Tax, version in force 1 January 2026 to 30 December 2026: §§ 2(n) to (r), (w), (x), (ab), 15, 17(5) to (7), 17k, 18, 18a, 21a, 49, 50a | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html | 2026-10-23 |
| Act No. 595/2003 Z. z., version in force 1 January 2025 to 14 March 2025: § 15 (rates for tax year 2025, used in example 2) | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20250101.html | 2026-10-23 |
| Act No. 595/2003 Z. z., version in force from 1 January 2027 (§§ 17(5) and 18 unchanged) | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20270101.html | 2026-10-23 |
| Act No. 563/2009 Z. z., Tax Code, version in force 1 September 2026 to 31 December 2026: §§ 16, 69, 154, 155, 156 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html | 2026-10-23 |
| Act No. 563/2009 Z. z., version in force from 1 January 2027 (§§ 16, 69, 154 to 156 unchanged) | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20270101.html | 2026-10-23 |
| Act No. 442/2012 Z. z. on international assistance and cooperation in tax administration, version in force from 1 January 2026: §§ 22a to 22g | https://static.slov-lex.sk/static/SK/ZZ/2012/442/20260101.html | 2026-10-23 |
| Ministry of Finance, guideline MF/012879/2025-724 on documentation content | https://www.mfsr.sk/files/archiv/49/Usmernenie-2025.pdf | 2026-10-23 |
| Ministry of Finance, annex to the guideline (shortened documentation form) | https://www.mfsr.sk/files/archiv/73/Usmernenie-2025_priloha.docx | 2026-10-23 |
| Ministry of Finance, transfer pricing page | https://www.mfsr.sk/sk/dane-cla-uctovnictvo/priame-dane/dane-z-prijmu/transferove-ocenovanie/ | 2026-10-23 |
| Financial Directorate, 12/PO/2026/IM, filling Table I of the 2025 corporate return | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Aktualne/DP/DPPO/2026/2026.03.26_012_PO_2026_IM.pdf | 2026-10-23 |
| Národná banka Slovenska, ECB key interest rates | https://nbs.sk/en/statistics/financial-markets/interest-rates/ecb-key-interest-rates/ | 2026-10-23 |
| Financial Administration, penalty-rate guidance: actual calendar-year day denominators; Tax Code §161, downward rounding to tens of eurocents | https://podpora.financnasprava.sk/425494-Pokuty--sadzby-pok%C3%BAt ; https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html#paragraf-161 | 2026-10-27 |
| Accounting Act §17(9), materiality used by documentation guideline art.3 | https://static.slov-lex.sk/static/SK/ZZ/2002/431/20260101.html#paragraf-17 | 2026-10-27 |
| Financial Directorate, 14/DZPaU/2026/I, current return vintage, new Table I and Table L | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Novinky_leg/Priame_dane_uct/2026/2026.10.22_014_DZPaU_2026_I.pdf | 2026-10-27 |
| Financial Directorate, taxable-revenue methodology 18/DZPaU/2021/MU, p.2 item 3 and expense exclusions; classification only, historical rates superseded | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Metodicke_usmernenia/Priame_dane/2021/2021.02.11_18_DZPaU_2021_MU.pdf | 2026-10-27 |
| Financial Administration, late-payment-interest calculation method | https://www.financnasprava.sk/sk/elektronicke-sluzby/verejne-sluzby/danove-kalkulacky/urok-z-omeskania | 2026-10-27 |
| Financial Administration, supplementary returns, filing and payment deadline | https://podpora.financnasprava.sk/901749-Dodato%C4%8Dn%C3%A9-da%C5%88ov%C3%A9-priznanie | 2026-10-27 |
| ECB, actual key-rate history | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html | 2026-10-27 |

Not yet confirmed: whether a TP adjustment paid abroad is treated as a deemed distribution for withholding; the name of the tax office that handles APAs and corresponding adjustments (the law points to the Financial Directorate's website, which was not read); the Financial Directorate's support pages on TP documentation (podpora.financnasprava.sk returned an error); and the public country-by-country reporting rules in the Accounting Act, not covered here.

> Contributed by Michael Cutajar.

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
