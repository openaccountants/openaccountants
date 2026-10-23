---
name: sk-transfer-pricing
description: "Use this skill for Slovak transfer pricing (transferové oceňovanie) in tax year 2026. It covers dependent persons (závislá osoba, Income Tax Act § 2(n) to (r), the 25% test), significant controlled transactions (over EUR 10,000, or loans over EUR 50,000 principal), the arm's length adjustment in § 17(5), corresponding adjustments in § 17(6), methods and the median rule in § 18(1), full, basic and shortened documentation under Ministry of Finance guideline MF/012879/2025-724 and who keeps which, Table I of the corporate return, the 15-day deadline to hand documentation over, penalties and late payment interest under the Tax Code, country-by-country reporting (EUR 750 million) and APAs under § 18(4) to (10). Trigger on: transfer pricing Slovakia, transferové oceňovanie, závislá osoba, kontrolovaná transakcia, transferová dokumentácia, APA Slovakia. Out of scope: corporate tax in general (sk-corporate-income-tax), individual income tax (slovakia-pit), VAT (slovakia-vat-return)."
jurisdiction: SK
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# Slovakia: transfer pricing (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. The law comes from the consolidated texts on Slov-Lex, the guideline from the Ministry of Finance (mfsr.sk) and the return guidance from the Financial Directorate (financnasprava.sk), all read on 23 October 2026. It prepares working papers; it is not authority to file or pay.

This is the transfer pricing (TP) skill for the Slovak pack. It links rather than repeats:

- Corporate income tax, the base, the return and its deadlines: [sk-corporate-income-tax](sk-corporate-income-tax.md) (still on 2025 figures).
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

**Significant controlled transaction** (§ 17(5)(a)): a transaction or group of transactions on which one or more dependent persons book taxable income or a tax expense above EUR 10,000 in the period, and any loan with principal above EUR 50,000. A loan above EUR 50,000 stays significant for its whole life, even after repayments take the balance below that (Financial Directorate, 12/PO/2026/IM, example 2). Transactions that are not significant are outside § 17(5) and are not reported in Table I.

**Domestic deals count too.** The guideline has separate rules for cross-border and domestic significant controlled transactions (MF/012879/2025-724, art. 2(8) and (9)), and Table I takes both (12/PO/2026/IM).

**Out of scope.** A micro-taxpayer (mikrodaňovník, revenue up to EUR 60,000) loses that status if it is a dependent person with a controlled transaction in the period (ITA § 2(w)(1)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Corporate income tax rate (applies to any TP adjustment of a company) | 10% if taxable revenue is up to EUR 100,000; 24% if taxable revenue is above EUR 5,000,000; 21% otherwise | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 15(b)(1)) |
| Dependent person: economic link | at least 25% of capital, voting rights or profit, direct, indirect or derived indirect | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 2(o)(1)) |
| Significant controlled transaction | income or expense above EUR 10,000 in the period; any loan with principal above EUR 50,000 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 17(5)(a)) |
| Full documentation: cross-border transaction value | above EUR 10,000,000 in the period | periods whose return deadline falls after 31 Dec 2025 | https://www.mfsr.sk/files/archiv/49/Usmernenie-2025.pdf (art. 3(1)(b)) |
| Basic documentation: cross-border transaction value | above EUR 1,000,000 in the period | same | https://www.mfsr.sk/files/archiv/49/Usmernenie-2025.pdf (art. 3(2)(b)) |
| Basic documentation: taxpayer's total revenue from operating and financial activity | above EUR 8,000,000 (with a material cross-border transaction) | same | https://www.mfsr.sk/files/archiv/49/Usmernenie-2025.pdf (art. 3(2)(a)) |
| Table I of the corporate return | up to 99 rows electronically (18 on paper) | returns due from 1 Jan 2026 (DPPOv25) | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Aktualne/DP/DPPO/2026/2026.03.26_012_PO_2026_IM.pdf |
| Deadline to hand over documentation on request | 15 days from delivery of the request | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 18(11)) |
| APA fee: unilateral | EUR 10,000 (half for a taxpayer rated highly reliable) | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 18(7)) |
| APA fee: bilateral or multilateral | EUR 30,000 (half for a taxpayer rated highly reliable) | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 18(7)) |
| APA term | up to 5 periods, renewable for up to 5 more; longer if the competent authorities agree it | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 18(4) and (5)) |
| Penalty on tax increased by the tax office | 3 times the ECB base rate a year, at least 10% a year; at least 1% of the amount, at most 100% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html (§ 155(1)(f), (2), (5)) |
| Penalty on tax disclosed in a supplementary return | the ECB base rate a year, at least 3% a year (2 times, at least 7%, if filed within 15 days after an audit starts) | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html (§ 155(1)(g), (h), (5)) |
| Penalty for a missed non-monetary duty (for example documentation not handed over) | EUR 100 to EUR 10,000, can be repeated | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html (§ 154(1)(d), (j); § 155(1)(e), (16)) |
| Late payment interest | 4 times the ECB base rate a year, at least 15% a year, for at most 4 years | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html (§ 156(2)) |
| ECB base rate (main refinancing operations) | 2.15% from 11 June 2025; 2.40% from 17 June 2026; 2.65% from 16 September 2026 | 2026 | https://nbs.sk/en/statistics/financial-markets/interest-rates/ecb-key-interest-rates/ |
| Country-by-country report: group consolidated revenue in the prior year | EUR 750,000,000 or more | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2012/442/20260101.html (§ 22a(h)) |
| Country-by-country report: fines | up to EUR 10,000 for not filing the report; up to EUR 3,000 for a missed notice; both can be repeated | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2012/442/20260101.html (§ 22g(2)) |
| Time limit to assess tax | 5 years from the end of the year the return was due; restarts on an audit report, 10 years at most; 10 years where a tax treaty is applied | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html (§ 69) |

At the ECB base rate of 2.65%: 3 times is 7.95%, so the 10% floor applies to an audit penalty. 1 times is 2.65%, so the 3% floor applies to a supplementary return penalty. 4 times is 10.6%, so the 15% floor applies to late payment interest.

## The taxable base

**The adjustment is one-way.** The base of a dependent person includes the difference by which prices or terms in significant controlled transactions depart from those between independent persons in comparable transactions. This applies only where the difference reduces the base or increases a tax loss (ITA § 17(5)(a)). The tax then follows at the taxpayer's own rate (§ 15).

**Shared costs.** A dependent person may deduct its share of costs that a related person incurred, but only if all four tests are met (§ 17(5)(b)):

1. the costs demonstrably relate to its business;
2. it would pay for the service if an independent person supplied it, or it would do the work itself;
3. it can show the total costs and how they are split among those who benefit;
4. its share is booked in its accounts or tax records.

**Methods** (§ 18(1) to (3)). The law names five methods:

- price methods: comparable uncontrolled price, resale price and cost plus;
- profit methods: profit split and transactional net margin.

A taxpayer may combine them or use another method, but only one that respects the arm's length principle. The OECD Transfer Pricing Guidelines also apply. The comparison looks at functions, risks, the asset or service, contract terms, the market and business strategy.

**The median rule** (§ 18(1)). Where the tax office compares against several independent values and the taxpayer's value is outside arm's length, an audit adjusts to the median of those values. The base goes to another point in the range only if the taxpayer shows that point fits the facts better.

**Corresponding adjustment** (§ 17(6)). Where a treaty partner's tax authority adjusts a related person's base in line with arm's length, the tax office that the Financial Directorate names on its website may allow a matching downward adjustment in Slovakia. Where one Slovak dependent person adjusts its base upward under § 17(5), the other Slovak dependent person may adjust its base the other way. It must adjust where it claims investment aid or incentive relief under § 30a or § 30b. It must also file a notice of the adjustment with its return or supplementary return.

**Permanent establishments** (§ 17(7)). A Slovak PE of a non-resident may not show a lower base, or a higher loss, than an independent enterprise doing the same work. § 18 applies to it, and the non-resident must keep documentation on the method.

**Interest on related-party loans.** Besides the arm's length test, interest on loans from dependent persons is not deductible above 25% of profit before tax plus depreciation and interest expense (§ 21a(1)). Banks, insurers and leasing companies are outside this rule (§ 21a(3)). The corporate skill covers the base around it.

## Deadlines and filing

**Corporate return.** Due within 3 calendar months after the end of the tax period, with the tax paid by the same date (ITA § 49(2)). A notice filed by the deadline extends it by up to 3 full months, or up to 6 months if the taxpayer has foreign-source income (§ 49(3)).

**Table I of the corporate return** (DPPOv25, for periods whose return deadline falls on or after 1 January 2026). Every taxpayer with significant controlled transactions fills Table I, domestic and foreign, whatever documentation tier applies. A Slovak PE fills it too, including dealings with its head office (12/PO/2026/IM).

- One row per transaction or group of transactions, split by related person and by transaction code.
- Column 3 shows the total effect on the accounting result (line 100), in euros and cents, with a minus sign for costs. It counts effects in this period and future periods. Example: buying a building from a related person for EUR 2,000,000 is shown as EUR 2,000,000 in the year of purchase, not as the year's depreciation.
- For a loan, report the interest under code 22. The principal does not affect the result and is not reported.
- An interest-free loan therefore puts nothing in Table I. The Financial Directorate points to guideline art. 3(3): where the return does not meet the documentation duty, the shortened file is kept. § 17(5) still applies to the loan.
- A taxpayer with only transactions that are not significant reports none of them, but ticks the box in part I for a link under § 2(n).
- The form allows 99 rows electronically. If that is not enough, the transactions with the lowest values are left out, and those go into the documentation.

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

**Supplementary return.** A taxpayer that finds its tax should be higher must file a supplementary return by the end of the month after the month it found out, and pay by the same date (TC § 16(2)). Once a tax audit starts, a supplementary return for that period is possible only within 15 days of the start (TC § 16(9)).

**Country-by-country reporting** (Act No. 442/2012 Z. z., §§ 22a to 22g). It applies to multinational groups with consolidated revenue of EUR 750,000,000 or more in the prior year (§ 22a(h)).

- A Slovak ultimate parent files the report within 12 months after the end of the reporting year (§ 22b(1)). A Slovak constituent entity files it instead only in the cases in § 22c (the parent's state does not require it, has no exchange agreement, or has failed).
- Every Slovak constituent entity notifies who files and names the group and its parent, by the last day of its own return deadline for that year. The notice is needed again only when the facts change (§ 22e).
- The tax office may not adjust the base on the report's data alone (§ 22f(3)).

## Penalties and interest

- **Audit adjustment.** When the tax office raises tax in an assessment, the penalty is 3 times the ECB base rate a year, at least 10% a year, on the increase (TC § 155(1)(f), (5)). It runs for each day from the day after the return deadline until the 15-day window under § 16(9) after the audit starts closes. It is at least 1% of the amount and at most the amount (§ 155(2)). The ECB rate used is the one on the day the assessment is delivered (§ 155(7)). Paying the assessed amount within 15 days of delivery cuts the penalty to two thirds (§ 155(17)).
- **Doubled penalty for abuse.** Where the office adjusts under § 17(5)(a) and also applies the anti-abuse rule (ITA § 50a or TC § 3(6)), the penalty is doubled (ITA § 18a(1)). The doubling falls away if the taxpayer does not appeal and pays within the appeal period (§ 18a(2)).
- **APA requested.** Where the taxpayer asked for an APA and the office audits the period of the request or the two periods before it, an adjustment without abuse carries the lower penalty under TC § 155(1)(g) (ITA § 18a(3)).
- **Self-correction.** Tax disclosed in a supplementary return carries a penalty of the ECB base rate a year, at least 3% a year, on the difference (TC § 155(1)(g), (5)). It runs from the day after the return deadline until the supplementary return is filed (§ 155(2)). The rate is twice the ECB rate, at least 7%, if filed within 15 days after an audit starts (§ 155(1)(h)).
- **Documentation not handed over, or another non-monetary duty missed.** EUR 100 to EUR 10,000, which can be repeated while the breach lasts (TC § 155(1)(e), (16)). A tax office does not impose a fine set within a range for a first breach (§ 155(4)).
- **Late payment interest.** 4 times the ECB base rate on the day the arrears arose, at least 15% a year, for each day until payment, for at most 4 years (TC § 156(2)). Interest under EUR 5 is not charged (§ 156(6)(b)).
- **Country-by-country reporting.** Up to EUR 10,000 for not filing the report, and up to EUR 3,000 for a missed notice, both repeatable (Act 442/2012, § 22g(2)).
- **Time limit.** Tax can be assessed for 5 years from the end of the year in which the return was due. An audit report restarts the period, but never beyond 10 years (TC § 69(1) to (3)). Where a tax treaty is applied, the limit is 10 years (§ 69(5)).

## Cross-border points

- **Treaties and MAP.** A double taxation case from a TP adjustment can go to the mutual agreement procedure under the treaty's associated enterprises article, or to the EU Arbitration Convention 90/436/EEC. The documentation goes in with the request (ITA § 18(13)). EU disputes can also go under Act No. 11/2019 Z. z. on tax dispute resolution, and full documentation then applies to the transaction (guideline art. 3(1)(g)).
- **Corresponding adjustment after a foreign adjustment.** Allowed only where the other state has a tax treaty with Slovakia and its adjustment is arm's length (ITA § 17(6)). Full documentation applies (guideline art. 3(1)(f)).
- **Non-cooperative states.** A cross-border transaction with a resident of a non-cooperative state needs at least basic documentation whatever its size, and full documentation if it is material (guideline art. 3(1)(c), 3(2)(d)). The list of cooperating states is on the Ministry of Finance website (ITA § 2(x)).
- **Permanent establishments.** Head office dealings with a Slovak PE are controlled transactions (§ 2(r)) and go in Table I. Attribution of profit follows § 17(7).
- **Withholding.** Whether an adjusted amount paid abroad is treated as a dividend or other payment subject to withholding is not covered by this skill (see Not yet confirmed).

## Worked examples

### Example 1: the tax office cuts a management fee paid to a foreign parent

A Slovak s.r.o. has taxable revenue of EUR 3,000,000 in 2026, so its rate is 21%. It pays its Austrian parent a management fee of EUR 250,000 and deducts it in full. Its benchmark gives a range of independent fees with a median of EUR 180,000, and the fee sits above the range. In an audit that starts in June 2028, the office adjusts to the median.

1. Documentation check: the fee is cross-border and above EUR 10,000, so it is significant. It is below EUR 1,000,000 and the company's revenue is below EUR 8,000,000, so neither full nor basic documentation applies. Table I in the 2026 return meets the duty (guideline art. 3(3)).
2. Adjustment to the median: EUR 250,000 less EUR 180,000 = EUR 70,000 (ITA § 17(5)(a), § 18(1)).
3. Extra tax at 21%: EUR 14,700.
4. Penalty: at the current ECB rate of 2.65%, 3 times is 7.95%, so the 10% floor applies (TC § 155(5)). It runs from 1 April 2027 (the day after the 31 March 2027 deadline) to 30 June 2028, the date the § 16(9) window is assumed to close: 457 days. On a 365-day year: 14,700 x 10% x 457 / 365 = EUR 1,840.52. That is above the 1% minimum of EUR 147.
5. Paying within 15 days of the assessment cuts the penalty to two thirds: EUR 1,227.01 (§ 155(17)).
6. Late payment interest is extra and is not computed here, because the ECB rate on the day the arrears arose is not yet known.
7. To relieve the double tax, the parent asks Austria for a corresponding adjustment through the treaty's mutual agreement procedure or the EU Arbitration Convention.

```oa-check
name: Management fee cut to the median, audit penalty at the 10% floor (2026)
inputs:
  fee_paid: 250000
  median_fee: 180000
  cit_rate: 21
  penalty_rate: 10
  days: 457
  days_in_year: 365
steps:
  - adjustment: fee_paid - median_fee
  - extra_tax: adjustment * cit_rate / 100
  - penalty: round(extra_tax * penalty_rate / 100 * days / days_in_year, 2)
  - penalty_paid_early: round(penalty * 2 / 3, 2)
  - minimum_penalty: extra_tax / 100
expected:
  adjustment: 70000
  extra_tax: 14700
  penalty: 1840.52
  penalty_paid_early: 1227.01
  minimum_penalty: 147
```

### Example 2: a large company corrects a royalty itself and checks its documentation tier

A Slovak a.s. has taxable revenue of EUR 9,000,000, so its rate is 24%. In 2025 it paid its Dutch sister company royalties of EUR 1,200,000 for a licence. It also borrowed EUR 60,000 at a market rate from a Slovak sister company. In October 2026 its new benchmark shows the arm's length royalty for 2025 was EUR 1,080,000. It files a supplementary return on 30 November 2026, before any audit.

1. Documentation tier for 2025: the royalty is cross-border and above EUR 1,000,000, so basic documentation is needed. It is not above EUR 10,000,000, the company does not report under IFRS, and the sister company is not in a non-cooperative state, so full documentation is not (guideline art. 3(1) and (2)).
2. The Slovak loan has principal above EUR 50,000, so it is significant. It is domestic and the company claims no investment aid, so the interest goes in Table I and no separate file is needed.
3. Excess royalty: EUR 1,200,000 less EUR 1,080,000 = EUR 120,000, added back (ITA § 17(5)(a)).
4. Extra tax at 24%: EUR 28,800, paid by the end of the month after the month the company found the error (TC § 16(2)).
5. Penalty: the ECB rate is 2.65%, below 3%, so the 3% floor applies (TC § 155(5)). It runs from 1 April 2026, the day after the 31 March 2026 deadline, to 30 November 2026: 244 days. On a 365-day year: 28,800 x 3% x 244 / 365 = EUR 577.58.
6. Had the office found it on audit instead, the 10% floor would apply over a longer period (TC § 155(1)(f)).

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
steps:
  - add_back: royalty_paid - royalty_alp
  - over_basic_threshold: royalty_paid - basic_doc_threshold
  - extra_tax: add_back * cit_rate / 100
  - penalty: round(extra_tax * penalty_rate / 100 * days / days_in_year, 2)
expected:
  add_back: 120000
  over_basic_threshold: 200000
  extra_tax: 28800
  penalty: 577.58
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
| Act No. 595/2003 Z. z. on Income Tax, version in force 1 January 2026 to 30 December 2026: §§ 2(n) to (r), (w), (x), (ab), 15, 17(5) to (7), 18, 18a, 21a, 49, 50a | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html | 2026-10-23 |
| Act No. 595/2003 Z. z., version in force from 1 January 2027 (§§ 17(5) and 18 unchanged) | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20270101.html | 2026-10-23 |
| Act No. 563/2009 Z. z., Tax Code, version in force 1 September 2026 to 31 December 2026: §§ 16, 69, 154, 155, 156 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html | 2026-10-23 |
| Act No. 442/2012 Z. z. on international assistance and cooperation in tax administration, version in force from 1 January 2026: §§ 22a to 22g | https://static.slov-lex.sk/static/SK/ZZ/2012/442/20260101.html | 2026-10-23 |
| Ministry of Finance, guideline MF/012879/2025-724 on documentation content | https://www.mfsr.sk/files/archiv/49/Usmernenie-2025.pdf | 2026-10-23 |
| Ministry of Finance, annex to the guideline (shortened documentation form) | https://www.mfsr.sk/files/archiv/73/Usmernenie-2025_priloha.docx | 2026-10-23 |
| Ministry of Finance, transfer pricing page | https://www.mfsr.sk/sk/dane-cla-uctovnictvo/priame-dane/dane-z-prijmu/transferove-ocenovanie/ | 2026-10-23 |
| Financial Directorate, 12/PO/2026/IM, filling Table I of the 2025 corporate return | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Aktualne/DP/DPPO/2026/2026.03.26_012_PO_2026_IM.pdf | 2026-10-23 |
| Národná banka Slovenska, ECB key interest rates | https://nbs.sk/en/statistics/financial-markets/interest-rates/ecb-key-interest-rates/ | 2026-10-23 |

Not yet confirmed: the day-count basis the tax office uses for per-day penalties and interest (the examples assume 365 days); whether interest also runs on tax disclosed in a timely supplementary return, alongside the § 155(1)(g) penalty; the end date of the audit penalty where no § 16(9) window applies; whether a TP adjustment that raises income counts towards the EUR 100,000 and EUR 5,000,000 revenue tests in § 15; whether a TP adjustment paid abroad is treated as a deemed distribution for withholding; the materiality test in Accounting Act § 17(9) that the guideline uses (not read); the name of the tax office that handles APAs and corresponding adjustments (the law points to the Financial Directorate's website, which was not read); the Financial Directorate's support pages on TP documentation (podpora.financnasprava.sk returned an error); and the public country-by-country reporting rules in the Accounting Act, not covered here.
